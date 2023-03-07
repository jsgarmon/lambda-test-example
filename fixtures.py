import datetime
from dateutil.tz import tzutc, tzlocal

list_buckets = {
    "ResponseMetadata": {
        "RequestId": "35EABA6C",
        "HostId": "wU0H5Q4PXsnR0b1nKQp6ybkDvHh2qHTaUWuGIS",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amz-id-2": "wU0H5Q4PXsnR0b1nKQp6ybkDvHh2qHTaUW",
            "x-amz-request-id": "35EABA6C",
            "date": "Tue, 03 Sep 2019 19:49:49 GMT",
            "content-type": "application/xml",
            "transfer-encoding": "chunked",
            "server": "AmazonS3",
        },
        "RetryAttempts": 0,
    },
    "Buckets": [
        {
            "Name": "16xxxxxxxxx9-us-east-1-chromeless",
            "CreationDate": datetime.datetime(2018, 5, 22, 18, 41, 35, tzinfo=tzutc()),
        },
        {
            "Name": "af-sftp-int1-s3",
            "CreationDate": datetime.datetime(2019, 3, 13, 15, 29, 36, tzinfo=tzutc()),
        },
        {
            "Name": "af-sftp-int2-fe-s3",
            "CreationDate": datetime.datetime(2019, 4, 7, 21, 16, 47, tzinfo=tzutc()),
        },
        {
            "Name": "af-sftp-int2-s3",
            "CreationDate": datetime.datetime(2019, 4, 2, 13, 15, 57, tzinfo=tzutc()),
        },
        {
            "Name": "af-winbox-int-s3",
            "CreationDate": datetime.datetime(2015, 8, 25, 16, 42, 58, tzinfo=tzutc()),
        },
        {
            "Name": "app-dev-eduffy",
            "CreationDate": datetime.datetime(2018, 5, 1, 19, 16, 23, tzinfo=tzutc()),
        },
        {
            "Name": "app-dev-jbertheussen",
            "CreationDate": datetime.datetime(2016, 12, 22, 16, 29, 19, tzinfo=tzutc()),
        },
        {
            "Name": "aws-athena-query-results-16xxxxxxxxx9-us-east-1",
            "CreationDate": datetime.datetime(2016, 12, 14, 15, 56, 7, tzinfo=tzutc()),
        },
        {
            "Name": "aws-glue-scripts-16xxxxxxxxx9-us-east-1",
            "CreationDate": datetime.datetime(2018, 6, 8, 1, 0, 8, tzinfo=tzutc()),
        },
        {
            "Name": "aws-logs-16xxxxxxxxx9-us-east-1",
            "CreationDate": datetime.datetime(2016, 4, 5, 21, 14, 14, tzinfo=tzutc()),
        },
    ],
    "Owner": {"DisplayName": "awsdev", "ID": "7e9dc35f29e355ca833f4cc7b754"},
}


lookup_events = {
    "Events": [
        {
            "EventId": "3269819c",
            "EventName": "DeleteBucket",
            "ReadOnly": "false",
            "AccessKeyId": "ASIAJ2HPQ",
            "EventTime": datetime.datetime(2019, 8, 28, 17, 23, 4, tzinfo=tzlocal()),
            "EventSource": "s3.amazonaws.com",
            "Username": "ci_integration",
            "Resources": [
                {
                    "ResourceType": "AWS::S3::Bucket",
                    "ResourceName": "portals-int99-sync-useruploads",
                }
            ],
            "CloudTrailEvent": '{"eventVersion":"1.05","userIdentity":{"type":"IAMUser","principalId":"AIDAJHZ7G2","arn":"arn:aws:iam::16xxxxxxxxx9:user/ci_integration","accountId":"16xxxxxxxxx9","accessKeyId":"ASIAJ2HPQ","userName":"ci_integration","sessionContext":{"attributes":{"mfaAuthenticated":"false","creationDate":"2019-08-28T21:23:02Z"}},"invokedBy":"cloudformation.amazonaws.com"},"eventTime":"2019-08-28T21:23:04Z","eventSource":"s3.amazonaws.com","eventName":"DeleteBucket","awsRegion":"us-east-1","sourceIPAddress":"cloudformation.amazonaws.com","userAgent":"cloudformation.amazonaws.com","requestParameters":{"host":["portals-int99-sync-useruploads.s3.amazonaws.com"],"bucketName":"portals-int99-sync-useruploads"},"responseElements":null,"additionalEventData":{"SignatureVersion":"SigV4","CipherSuite":"ECDHE-RSA-AES128-SHA","AuthenticationMethod":"AuthHeader","vpcEndpointId":"vpce-00dc1369"},"requestID":"60DFD05","eventID":"3269819c","eventType":"AwsApiCall","recipientAccountId":"16xxxxxxxxx9","vpcEndpointId":"vpce-00dc1369"}',
        },
        {
            "EventId": "1f16b5a7",
            "EventName": "CreateBucket",
            "ReadOnly": "false",
            "AccessKeyId": "ASIASMR3",
            "EventTime": datetime.datetime(2019, 8, 17, 11, 16, 41, tzinfo=tzlocal()),
            "EventSource": "s3.amazonaws.com",
            "Username": "ci_integration",
            "Resources": [
                {
                    "ResourceType": "AWS::S3::Bucket",
                    "ResourceName": "portals-int99-sync-useruploads",
                }
            ],
            "CloudTrailEvent": '{"eventVersion":"1.05","userIdentity":{"type":"IAMUser","principalId":"AIDAJHZ7G2","arn":"arn:aws:iam::16xxxxxxxxx9:user/ci_integration","accountId":"16xxxxxxxxx9","accessKeyId":"ASIAJ2HPQ","userName":"ci_integration","sessionContext":{"attributes":{"mfaAuthenticated":"false","creationDate":"2019-08-28T21:23:02Z"}},"invokedBy":"cloudformation.amazonaws.com"},"eventTime":"2019-08-28T21:23:04Z","eventSource":"s3.amazonaws.com","eventName":"CreateBucket","awsRegion":"us-east-1","sourceIPAddress":"cloudformation.amazonaws.com","userAgent":"cloudformation.amazonaws.com","requestParameters":{"host":["portals-int99-sync-useruploads.s3.amazonaws.com"],"bucketName":"portals-int99-sync-useruploads"},"responseElements":null,"additionalEventData":{"SignatureVersion":"SigV4","CipherSuite":"ECDHE-RSA-AES128-SHA","AuthenticationMethod":"AuthHeader","vpcEndpointId":"vpce-00dc1369"},"requestID":"60DFD05","eventID":"3269819c","eventType":"AwsApiCall","recipientAccountId":"16xxxxxxxxx9","vpcEndpointId":"vpce-00dc1369"}',
        },
    ],
    "ResponseMetadata": {
        "RequestId": "8ec3d06a-ef6e-4ae1-9ae5-8a3b683c9233",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "8ec3d06a-ef6e-4ae1-9ae5-8a3b683c9233",
            "content-type": "application/x-amz-json-1.1",
            "content-length": "49825",
            "date": "Wed, 04 Sep 2019 20:43:21 GMT",
        },
        "RetryAttempts": 0,
    },
}

email_response = {
    "MessageId": "0100016cfddfdf5b-eb2d021a-5ce9-4bc3-9733-4a7ef7b36ad0-000000",
    "ResponseMetadata": {
        "RequestId": "7471c05f-572a-4ca1-9afc-f7c9bb6a200e",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "7471c05f-572a-4ca1-9afc-f7c9bb6a200e",
            "content-type": "text/xml",
            "content-length": "338",
            "date": "Wed, 04 Sep 2019 20:03:22 GMT",
        },
        "RetryAttempts": 0,
    },
}

raw_message = {
    "Data": "From: systemengineering@soundexchange.com\n"
    "To: user@soundexchange.com\n"
    "Subject: [sxdev] Resource resource not properly "
    "tagged\n"
    "MIME-Version: 1.0\n"
    "Content-Type: text/html;\n"
    "\n"
    "msg\n"
    "<p>A list of valid tags is available on <a "
    'href="https://confluence.prod.soundexchange.com/display/EN/Project+Abbreviations">Confluence</a>.</p>\n'  # noqa
    "<hr/>\n"
    "<p>This is an automated message from <a "
    'href="https://bitbucket.prod.soundexchange.com/projects/CO/repos/cloudops-aws-auto-tag/browse">this '  # noqa
    "Lambda Function</a>.</p>\n"
}

s3_event = {
    "version": "0",
    "id": "91076974",
    "detail-type": "AWS API Call via CloudTrail",
    "source": "aws.s3",
    "account": "16xxxxxxxxx9",
    "time": "2019-09-09T02:59:40Z",
    "region": "us-east-1",
    "resources": [],
    "detail": {
        "eventVersion": "1.05",
        "userIdentity": {
            "type": "IAMUser",
            "principalId": "AIDASMR3E",
            "arn": "arn:aws:iam::16xxxxxxxxx9:user/fake_user",
            "accountId": "16xxxxxxxxx9",
            "accessKeyId": "ASIASMR3E",
            "userName": "fake_user",
            "sessionContext": {
                "attributes": {
                    "mfaAuthenticated": "true",
                    "creationDate": "2019-09-09T02:55:59Z",
                }
            },
            "invokedBy": "signin.amazonaws.com",
        },
        "eventTime": "2019-09-09T02:59:40Z",
        "eventSource": "s3.amazonaws.com",
        "eventName": "CreateBucket",
        "awsRegion": "us-east-1",
        "sourceIPAddress": "108.51.236.64",
        "userAgent": "signin.amazonaws.com",
        "requestParameters": {
            "host": ["s3.amazonaws.com"],
            "bucketName": "af-aws-auto-tag-test",
        },
        "responseElements": None,
        "additionalEventData": {
            "SignatureVersion": "SigV4",
            "CipherSuite": "ECDHE-RSA-AES128-SHA",
            "AuthenticationMethod": "AuthHeader",
            "vpcEndpointId": "vpce-f40",
        },
        "requestID": "FC6474EC235EC88A",
        "eventID": "7ed7f22f",
        "eventType": "AwsApiCall",
        "vpcEndpointId": "vpce-f40",
    },
}

ec2_event = {
    "version": "0",
    "id": "a96fe4c3",
    "detail-type": "AWS API Call via CloudTrail",
    "source": "aws.ec2",
    "account": "16xxxxxxxxx9",
    "time": "2019-09-11T20:40:53Z",
    "region": "us-east-1",
    "resources": [],
    "detail": {
        "eventVersion": "1.05",
        "userIdentity": {
            "type": "AssumedRole",
            "principalId": "AROAJX7XB3F4JG24WCRCC:AutoScaling",
            "arn": "arn:aws:sts::16xxxxxxxxx9:assumed-role/AWSServiceRoleForAutoScaling/AutoScaling",
            "accountId": "16xxxxxxxxx9",
            "sessionContext": {
                "sessionIssuer": {
                    "type": "Role",
                    "principalId": "AROAJX7XB",
                    "arn": "arn:aws:iam::16xxxxxxxxx9:role/aws-service-role/autoscaling.amazonaws.com/AWSServiceRoleForAutoScaling",
                    "accountId": "16xxxxxxxxx9",
                    "userName": "AWSServiceRoleForAutoScaling",
                },
                "webIdFederationData": {},
                "attributes": {
                    "mfaAuthenticated": "false",
                    "creationDate": "2019-09-11T20:31:06Z",
                },
            },
            "invokedBy": "autoscaling.amazonaws.com",
        },
        "eventTime": "2019-09-11T20:40:53Z",
        "eventSource": "ec2.amazonaws.com",
        "eventName": "RunInstances",
        "awsRegion": "us-east-1",
        "sourceIPAddress": "autoscaling.amazonaws.com",
        "userAgent": "autoscaling.amazonaws.com",
        "requestParameters": {
            "instancesSet": {
                "items": [
                    {
                        "imageId": "ami-06ddd6d23",
                        "minCount": 1,
                        "maxCount": 1,
                        "keyName": "fake_user",
                    }
                ]
            },
            "groupSet": {"items": [{"groupId": "sg-4b4f"}]},
            "userData": "<sensitiveDataRemoved>",
            "instanceType": "t3.medium",
            "blockDeviceMapping": {},
            "availabilityZone": "us-east-1b",
            "monitoring": {"enabled": False},
            "subnetId": "subnet-ad37e8c2",
            "disableApiTermination": False,
            "clientToken": "8075b488",
            "iamInstanceProfile": {
                "name": "dp-app-int-iam-DPInstanceProfile-66FFH5JYSPE2"
            },
            "tagSpecificationSet": {
                "items": [
                    {
                        "resourceType": "instance",
                        "tags": [
                            {"key": "app", "value": "dp"},
                            {
                                "key": "aws:autoscaling:groupName",
                                "value": "dp-rights-int1-as",
                            },
                            {"key": "build_id", "value": "dp-rights-19.10.0-b13703"},
                            {
                                "key": "daily_build_tag",
                                "value": "dp-rights-19.10.0-b13703",
                            },
                            {"key": "asset", "value": "dp-rights"},
                            {"key": "env", "value": "int1"},
                            {"key": "Name", "value": "dp-rights-int1"},
                        ],
                    }
                ]
            },
        },
        "responseElements": {
            "requestId": "85e201c7",
            "reservationId": "r-0f66579fe",
            "ownerId": "16xxxxxxxxx9",
            "groupSet": {},
            "instancesSet": {
                "items": [
                    {
                        "instanceId": "i-0a17f7327",
                        "imageId": "ami-06ddd6d23e",
                        "instanceState": {"code": 0, "name": "pending"},
                        "privateDnsName": "ip-172-21-71-164.ec2.internal",
                        "keyName": "fake_user",
                        "amiLaunchIndex": 0,
                        "productCodes": {},
                        "instanceType": "t3.medium",
                        "launchTime": 1568234453000,
                        "placement": {
                            "availabilityZone": "us-east-1b",
                            "tenancy": "default",
                        },
                        "monitoring": {"state": "disabled"},
                        "subnetId": "subnet-ad37e8c2",
                        "vpcId": "vpc-bea761d1",
                        "privateIpAddress": "172.21.71.164",
                        "stateReason": {"code": "pending", "message": "pending"},
                        "architecture": "x86_64",
                        "rootDeviceType": "ebs",
                        "rootDeviceName": "/dev/xvda",
                        "blockDeviceMapping": {},
                        "virtualizationType": "hvm",
                        "hypervisor": "xen",
                        "tagSet": {
                            "items": [
                                {
                                    "key": "aws:autoscaling:groupName",
                                    "value": "dp-rights-int1-as",
                                },
                                {"key": "env", "value": "int1"},
                                {
                                    "key": "daily_build_tag",
                                    "value": "dp-rights-19.10.0-b13703",
                                },
                                {
                                    "key": "build_id",
                                    "value": "dp-rights-19.10.0-b13703",
                                },
                                {"key": "Name", "value": "dp-rights-int1"},
                                {"key": "asset", "value": "dp-rights"},
                            ]
                        },
                        "clientToken": "8075b488-3acd-121b-2043-0301bdbff9a0_subnet-ad37e8c2_1",
                        "groupSet": {
                            "items": [
                                {"groupId": "sg-4b4f9424", "groupName": "all-int-sg"}
                            ]
                        },
                        "sourceDestCheck": True,
                        "networkInterfaceSet": {
                            "items": [
                                {
                                    "networkInterfaceId": "eni-0966aa108cd0381a7",
                                    "subnetId": "subnet-ad37e8c2",
                                    "vpcId": "vpc-bea761d1",
                                    "ownerId": "16xxxxxxxxx9",
                                    "status": "in-use",
                                    "macAddress": "12:ca:be:f7:d8:be",
                                    "privateIpAddress": "172.21.71.164",
                                    "privateDnsName": "ip-172-21-71-164.ec2.internal",
                                    "sourceDestCheck": True,
                                    "interfaceType": "interface",
                                    "groupSet": {
                                        "items": [
                                            {
                                                "groupId": "sg-4b4f9424",
                                                "groupName": "all-int-sg",
                                            }
                                        ]
                                    },
                                    "attachment": {
                                        "attachmentId": "eni-attach-070c0c3347f50958d",
                                        "deviceIndex": 0,
                                        "status": "attaching",
                                        "attachTime": 1568234453000,
                                        "deleteOnTermination": True,
                                    },
                                    "privateIpAddressesSet": {
                                        "item": [
                                            {
                                                "privateIpAddress": "172.21.71.164",
                                                "privateDnsName": "ip-172-21-71-164.ec2.internal",
                                                "primary": True,
                                            }
                                        ]
                                    },
                                    "ipv6AddressesSet": {},
                                    "tagSet": {},
                                }
                            ]
                        },
                        "iamInstanceProfile": {
                            "arn": "arn:aws:iam::16xxxxxxxxx9:instance-profile/dp-app-int-iam-DPInstanceProfile-66FFH5JYSPE2",
                            "id": "AIPAITTE6R7S462ARDGYQ",
                        },
                        "ebsOptimized": False,
                        "cpuOptions": {"coreCount": 1, "threadsPerCore": 2},
                        "capacityReservationSpecification": {
                            "capacityReservationPreference": "open"
                        },
                        "enclaveOptions": {"enabled": False},
                    }
                ]
            },
            "requesterId": "940372691376",
        },
        "requestID": "85e201c7",
        "eventID": "835e6146",
        "eventType": "AwsApiCall",
    },
}

rds_event = {
    "version": "0",
    "id": "7405fb31",
    "detail-type": "AWS API Call via CloudTrail",
    "source": "aws.rds",
    "account": "16xxxxxxxxx9",
    "time": "2019-09-11T17:18:12Z",
    "region": "us-east-1",
    "resources": [],
    "detail": {
        "eventVersion": "1.05",
        "userIdentity": {
            "type": "IAMUser",
            "principalId": "AIDASMR",
            "arn": "arn:aws:iam::16xxxxxxxxx9:user/fake_user",
            "accountId": "16xxxxxxxxx9",
            "accessKeyId": "ASIASMR",
            "userName": "fake_user",
            "sessionContext": {
                "attributes": {
                    "mfaAuthenticated": "true",
                    "creationDate": "2019-09-11T14:35:11Z",
                }
            },
            "invokedBy": "signin.amazonaws.com",
        },
        "eventTime": "2019-09-11T17:18:12Z",
        "eventSource": "rds.amazonaws.com",
        "eventName": "CreateDBInstance",
        "awsRegion": "us-east-1",
        "sourceIPAddress": "65.213.219.178",
        "userAgent": "signin.amazonaws.com",
        "requestParameters": {
            "dBName": "",
            "dBInstanceIdentifier": "af-auto-tag-test",
            "allocatedStorage": 20,
            "dBInstanceClass": "db.t2.micro",
            "engine": "postgres",
            "masterUsername": "postgres",
            "masterUserPassword": "****",
            "vpcSecurityGroupIds": ["sg-62cf030d"],
            "dBSubnetGroupName": "int-subnet-group-172-21",
            "dBParameterGroupName": "default.postgres10",
            "backupRetentionPeriod": 7,
            "port": 5432,
            "multiAZ": False,
            "engineVersion": "10.6",
            "autoMinorVersionUpgrade": True,
            "optionGroupName": "default:postgres-10",
            "publiclyAccessible": False,
            "storageType": "gp2",
            "storageEncrypted": False,
            "copyTagsToSnapshot": True,
            "enableIAMDatabaseAuthentication": False,
            "enablePerformanceInsights": True,
            "performanceInsightsRetentionPeriod": 7,
            "enableCloudwatchLogsExports": [],
            "deletionProtection": False,
            "maxAllocatedStorage": 1000,
        },
        "responseElements": {
            "dBInstanceIdentifier": "af-auto-tag-test",
            "dBInstanceClass": "db.t2.micro",
            "engine": "postgres",
            "dBInstanceStatus": "creating",
            "masterUsername": "postgres",
            "allocatedStorage": 20,
            "preferredBackupWindow": "03:21-03:51",
            "backupRetentionPeriod": 7,
            "dBSecurityGroups": [],
            "vpcSecurityGroups": [
                {"vpcSecurityGroupId": "sg-62cf030d", "status": "active"}
            ],
            "dBParameterGroups": [
                {
                    "dBParameterGroupName": "default.postgres10",
                    "parameterApplyStatus": "in-sync",
                }
            ],
            "dBSubnetGroup": {
                "dBSubnetGroupName": "int-subnet-group-172-21",
                "dBSubnetGroupDescription": "Integration environment subnet group for the VPC in 172.21. Uses private subnets.",
                "vpcId": "vpc-bea761d1",
                "subnetGroupStatus": "Complete",
                "subnets": [
                    {
                        "subnetIdentifier": "subnet-ad37e8c2",
                        "subnetAvailabilityZone": {"name": "us-east-1b"},
                        "subnetStatus": "Active",
                    },
                    {
                        "subnetIdentifier": "subnet-2e36e941",
                        "subnetAvailabilityZone": {"name": "us-east-1c"},
                        "subnetStatus": "Active",
                    },
                    {
                        "subnetIdentifier": "subnet-0f36e960",
                        "subnetAvailabilityZone": {"name": "us-east-1d"},
                        "subnetStatus": "Active",
                    },
                ],
            },
            "preferredMaintenanceWindow": "thu:08:27-thu:08:57",
            "pendingModifiedValues": {"masterUserPassword": "****"},
            "multiAZ": False,
            "engineVersion": "10.6",
            "autoMinorVersionUpgrade": True,
            "readReplicaDBInstanceIdentifiers": [],
            "licenseModel": "postgresql-license",
            "optionGroupMemberships": [
                {"optionGroupName": "default:postgres-10", "status": "in-sync"}
            ],
            "publiclyAccessible": False,
            "storageType": "gp2",
            "dbInstancePort": 0,
            "storageEncrypted": False,
            "dbiResourceId": "db-ZNKQO",
            "cACertificateIdentifier": "rds-ca-2015",
            "domainMemberships": [],
            "copyTagsToSnapshot": True,
            "monitoringInterval": 0,
            "dBInstanceArn": "arn:aws:rds:us-east-1:16xxxxxxxxx9:db:af-auto-tag-test",
            "iAMDatabaseAuthenticationEnabled": False,
            "performanceInsightsEnabled": True,
            "performanceInsightsKMSKeyId": "arn:aws:kms:us-east-1:16xxxxxxxxx9:key/0dcbc123-2895",
            "performanceInsightsRetentionPeriod": 7,
            "deletionProtection": False,
            "associatedRoles": [],
            "httpEndpointEnabled": False,
            "maxAllocatedStorage": 1000,
        },
        "requestID": "9203197d",
        "eventID": "1e3cca87",
        "eventType": "AwsApiCall",
    },
}
