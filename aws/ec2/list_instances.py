from shared.aws_session import get_session


def list_ec2_instances():
    session = get_session()

    ec2 = session.client("ec2")

    response = ec2.describe_instances()

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:

            instance_id = instance.get("InstanceId")
            instance_type = instance.get("InstanceType")
            state = instance["State"]["Name"]

            private_ip = instance.get("PrivateIpAddress", "N/A")
            public_ip = instance.get("PublicIpAddress", "N/A")

            print("=" * 60)
            print(f"Instance ID: {instance_id}")
            print(f"Type: {instance_type}")
            print(f"State: {state}")
            print(f"Private IP: {private_ip}")
            print(f"Public IP: {public_ip}")


if __name__ == "__main__":
    list_ec2_instances()