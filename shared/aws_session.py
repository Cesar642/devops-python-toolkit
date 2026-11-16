import boto3


def get_session(profile=None, region="us-east-1"):
    if profile:
        session = boto3.Session(
            profile_name=profile,
            region_name=region
        )
    else:
        session = boto3.Session(region_name=region)

    return session