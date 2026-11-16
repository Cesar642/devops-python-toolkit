from shared.aws_session import get_session


def list_buckets():
    session = get_session()

    s3 = session.client("s3")

    response = s3.list_buckets()

    print("\nS3 Buckets:\n")

    for bucket in response["Buckets"]:
        print(f"- {bucket['Name']}")


if __name__ == "__main__":
    list_buckets()