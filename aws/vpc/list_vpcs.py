from shared.aws_session import get_session


def list_vpcs():
    session = get_session()

    ec2 = session.client("ec2")

    response = ec2.describe_vpcs()

    for vpc in response["Vpcs"]:

        print("=" * 60)
        print(f"VPC ID: {vpc['VpcId']}")
        print(f"CIDR: {vpc['CidrBlock']}")
        print(f"State: {vpc['State']}")


if __name__ == "__main__":
    list_vpcs()