import pytest
import botocore.session
from botocore.stub import Stubber
from src.cloudformation import CloudformationTagger
from tests.load_fixture import load_fixture


def test_tag_if_not_already():
    response = load_fixture("cloudformation-describe-stacks.json")
    client = botocore.session.get_session().create_client("cloudformation")
    with Stubber(client) as stubber:
        stubber.add_response("describe_stacks", response, {})
        tagger = CloudformationTagger(client)
        actual = tagger.tag_if_not()

    assert len(actual) == 1
    assert actual[0]["success"] is True
    assert actual[0]["stack_name"] == "portals-fe-int2-es"
    assert actual[0]["message"] == "Cloudformation stack is already tagged"


def test_tag_if_not_not(mocker):
    mock_tag_it = mocker.patch("src.cloudformation.CloudformationTagger.tag_it")
    mock_tag_it.return_value = {}

    response = load_fixture("cloudformation-describe-stacks.json")
    response["Stacks"][0]["Tags"] = []
    client = botocore.session.get_session().create_client("cloudformation")
    with Stubber(client) as stubber:
        stubber.add_response("describe_stacks", response, {})
        tagger = CloudformationTagger(client)
        actual = tagger.tag_if_not()

    assert len(actual) == 1
    assert actual[0]["success"] is True
    assert actual[0]["stack_name"] == "portals-fe-int2-es"
    assert actual[0]["message"] == "Auto-tagged based on stack name"


def test_tag_if_not_not_unknown_app(mocker):
    mock_tag_it = mocker.patch("src.cloudformation.CloudformationTagger.tag_it")
    mock_tag_it.return_value = {}
    mock_notify = mocker.patch("src.cloudformation.CloudformationTagger.notify")
    mock_notify.return_value = False

    response = load_fixture("cloudformation-describe-stacks.json")
    response["Stacks"][0]["Tags"] = []
    response["Stacks"][0]["StackName"] = "project-fe-int2-es"
    client = botocore.session.get_session().create_client("cloudformation")
    with Stubber(client) as stubber:
        stubber.add_response("describe_stacks", response, {})
        tagger = CloudformationTagger(client)
        actual = tagger.tag_if_not()

    assert len(actual) == 1
    assert actual[0]["success"] is False
    assert actual[0]["stack_name"] == "project-fe-int2-es"
    assert actual[0]["message"] == "Resource is untagged and creator is unknown."


def test_tag_if_not_not_known_app(mocker):
    mock_tag_it = mocker.patch("src.cloudformation.CloudformationTagger.tag_it")
    mock_tag_it.return_value = {}
    mock_notify = mocker.patch("src.cloudformation.CloudformationTagger.notify")
    mock_notify.return_value = True

    response = load_fixture("cloudformation-describe-stacks.json")
    response["Stacks"][0]["Tags"] = []
    response["Stacks"][0]["StackName"] = "project-fe-int2-es"
    client = botocore.session.get_session().create_client("cloudformation")
    with Stubber(client) as stubber:
        stubber.add_response("describe_stacks", response, {})
        tagger = CloudformationTagger(client)
        actual = tagger.tag_if_not()

    assert len(actual) == 1
    assert actual[0]["success"] is False
    assert actual[0]["stack_name"] == "project-fe-int2-es"
    assert actual[0]["message"] == "Resource is untagged, notifying user"
