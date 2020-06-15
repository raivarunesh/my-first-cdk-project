from aws_cdk import (
    aws_s3 as _s3,
    core)


class MyFirstCdkProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        _s3.Bucket(
            self,
            "myBucketId",
            bucket_name="my-first-project-bucket-22113344",
            encryption=_s3.BucketEncryption.S3_MANAGED,
            versioned=False,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL

        )

        mybucket=_s3.Bucket(self,
        "myBucketid1",
        )

        output1=core.CfnOutput(
            self,
            "myBucketOutput1",
            value=mybucket.bucket_name,
            description=f"My First CDK bucket",
            export_name="myBucketOutput1"
        )