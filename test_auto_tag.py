import logging
import pytest
from botocore.stub import Stubber, ANY

from tests import fixtures
from tests.load_fixture import load_fixture
import src.auto_tag as func
from src.shared import map_prefix_to_app
from src.ses import SES
from src.cloudtrail import cloudTrail


def test_map_prefix_to_app():
    app = map_prefix_to_app("rightspub-lds-etl-int2-bucket")
    assert app == "rightspub"


def test_s3tagger_get_non_tagged():
    tagger = func.s3Tagger()
    with Stubber(tagger.client) as stubber:
        responses = [[], [{"Key": "app", "Value": "test"}]] * 5
        stubber.add_response("list_buckets", fixtures.list_buckets, {})
        for i in range(10):
            stubber.add_response(
                "get_bucket_tagging", {"TagSet": responses[i]}, {"Bucket": ANY}
            )
        non_tagged = tagger.get_non_tagged()

    assert len(non_tagged) == 5


def test_s3tagger_is_tagged():
    bucket_name = "my_bucket_env"
    expected_params = {"Bucket": bucket_name}
    response = {"TagSet": [{"Key": "app", "Value": "my"}]}

    tagger = func.s3Tagger()
    with Stubber(tagger.client) as stubber:
        stubber.add_response("get_bucket_tagging", response, expected_params)
        actual = tagger.is_tagged(bucket_name)
    assert actual is True


def test_s3tagger_is_tagged_not():
    bucket_name = "my_bucket_env"
    expected_params = {"Bucket": bucket_name}
    response = {"TagSet": []}

    tagger = func.s3Tagger()
    with Stubber(tagger.client) as stubber:
        stubber.add_response("get_bucket_tagging", response, expected_params)
        actual = tagger.is_tagged(bucket_name)
    assert actual is False


@pytest.mark.parametrize(
    "error_code,expected", [("NoSuchBucket", None), ("NoSuchTagSet", False)]
)
def test_s3tagger_is_tagged_exception(error_code, expected):
    bucket_name = "my_bucket_env"
    expected_params = {"Bucket": bucket_name}

    tagger = func.s3Tagger()
    with Stubber(tagger.client) as stubber:
        stubber.add_client_error(
            "get_bucket_tagging",
            service_error_code=error_code,
            expected_params=expected_params,
        )
        actual = tagger.is_tagged(bucket_name)
    assert actual is expected


def test_s3tagger_tag_it():
    bucket_name = "my_bucket_env"
    # get_bucket_tagging
    expected_params1 = {"Bucket": bucket_name}
    response1 = {"TagSet": []}
    # put_bucket_tagging
    expected_params2 = {
        "Bucket": bucket_name,
        "Tagging": {"TagSet": [{"Key": "app", "Value": "my"}]},
    }
    response2 = {}

    tagger = func.s3Tagger()
    with Stubber(tagger.client) as stubber:
        stubber.add_response("get_bucket_tagging", response1, expected_params1)
        stubber.add_response("put_bucket_tagging", response2, expected_params2)
        actual = tagger.tag_it(bucket_name, "my")

    assert actual is None


def test_s3tagger_tag_it_exception():
    bucket_name = "my_bucket_env"
    # get_bucket_tagging
    expected_params1 = {"Bucket": bucket_name}
    # put_bucket_tagging
    expected_params2 = {
        "Bucket": bucket_name,
        "Tagging": {"TagSet": [{"Key": "app", "Value": "my"}]},
    }
    response2 = {}

    tagger = func.s3Tagger()

    with Stubber(tagger.client) as stubber:
        stubber.add_client_error("get_bucket_tagging", expected_params=expected_params1)
        stubber.add_response("put_bucket_tagging", response2, expected_params2)
        actual = tagger.tag_it(bucket_name, "my")

    assert actual is None


def test_ec2tagger_tag_it():
    resource_id = "i-0d9ee9f6ae876eb6b"
    # put_bucket_tagging
    expected_params = {
        "Resources": [resource_id],
        "Tags": [{"Key": "app", "Value": "my"}],
    }
    response = {}

    tagger = func.ec2Tagger()
    with Stubber(tagger.client) as stubber:
        stubber.add_response("create_tags", response, expected_params)
        actual = tagger.tag_it(resource_id, "my")

    assert actual is None


def test_rdstagger_tag_it():
    resource_arn = "arn:aws:rds:us-east-1:992648334831:my-app-env-rds"
    # put_bucket_tagging
    expected_params = {
        "ResourceName": resource_arn,
        "Tags": [{"Key": "app", "Value": "my"}],
    }
    response = {}

    tagger = func.rdsTagger()
    with Stubber(tagger.client) as stubber:
        stubber.add_response("add_tags_to_resource", response, expected_params)
        actual = tagger.tag_it(resource_arn, "my")

    assert actual is None


def test_get_create_user():
    trail = cloudTrail()
    expected_params = {"LookupAttributes": ANY, "StartTime": ANY}
    with Stubber(trail.client) as stubber:
        stubber.add_response("lookup_events", fixtures.lookup_events, expected_params)
        creator = trail.get_create_user("test_bucket")

    assert creator == "ci_integration"


def test_send_email():
    ses = SES()
    expected_params = {"Destinations": [], "RawMessage": fixtures.raw_message}
    with Stubber(ses.client) as stubber:
        stubber.add_response("send_raw_email", fixtures.email_response, expected_params)
        ses.send_email("user", "resource", "msg")
        # Runs StubAssertion that msg_dict that gets built as part of
        # send_email() is same as expected_params['RawMessage'].
        # Not using explicit assert.


def test_cloudformation_handler_tagged(mocker):
    mock_tag_if_not = mocker.patch("src.auto_tag.CloudformationTagger.tag_if_not")
    mock_tag_if_not.return_value = {
        "stack_name": "portals-fe-pprd-es",
        "success": True,
        "message": "already tagged",
    }

    event = load_fixture("createStack.json")
    response = func.cloudformation_handler(event, {})
    assert response["message"] == "already tagged"


def test_ec2_handler_tagged(monkeypatch):
    def mockreturn(*args):
        return {"is_tagged": True, "name": "test"}

    monkeypatch.setattr(func.ec2Tagger, "is_tagged", mockreturn)
    response = func.ec2_handler(fixtures.ec2_event, "")
    assert response["message"] == "already tagged"


def test_ec2_handler_not_tagged(monkeypatch):
    def mockreturn1(*args):
        return {"is_tagged": False, "name": "af-test"}

    def mockreturn2(*args):
        return ""

    monkeypatch.setattr(func.ec2Tagger, "is_tagged", mockreturn1)
    monkeypatch.setattr(func.ec2Tagger, "tag_it", mockreturn2)
    response = func.ec2_handler(fixtures.ec2_event, "")
    assert response["message"] == "added tag"


def test_rds_handler_tagged(monkeypatch):
    def mockreturn(*args):
        return True

    monkeypatch.setattr(func.rdsTagger, "is_tagged", mockreturn)
    response = func.rds_handler(fixtures.rds_event, "")
    assert response["message"] == "already tagged"


def test_rds_handler_not_tagged(monkeypatch):
    def mockreturn1(*args):
        return False

    def mockreturn2(*args):
        return ""

    monkeypatch.setattr(func.rdsTagger, "is_tagged", mockreturn1)
    monkeypatch.setattr(func.rdsTagger, "tag_it", mockreturn2)
    response = func.rds_handler(fixtures.rds_event, "")
    assert response["message"] == "added tag"


def test_s3_handler_tagged(monkeypatch):
    def mockreturn(*args):
        return True

    monkeypatch.setattr(func.s3Tagger, "is_tagged", mockreturn)
    response = func.s3_handler(fixtures.s3_event, "")
    assert response["message"] == "already tagged"


def test_s3_handler_not_tagged(monkeypatch):
    def mockreturn1(*args):
        return False

    def mockreturn2(*args):
        return ""

    monkeypatch.setattr(func.s3Tagger, "is_tagged", mockreturn1)
    monkeypatch.setattr(func.s3Tagger, "tag_it", mockreturn2)
    response = func.s3_handler(fixtures.s3_event, "")
    assert response["message"] == "added tag"


def test_format_list():
    input_list = ["one", "two", "three"]
    expected_output = "<ul><li>one</li><li>two</li><li>three</li></ul>"
    assert func.format_list(input_list) == expected_output
