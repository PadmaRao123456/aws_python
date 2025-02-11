import boto3
#create EC2 Client
ec2=boto3.client('ec2')
#your Ec2 Instance ID
instance_id  = "i-08d49b255d44a745e"
def check_instance_status(instance_id):
    try:
        response = ec2.describe_instance_status(Instance_ids=[instance_id])
        print(response)
    except Exception as e:
        print(f"Error checking instance {instance_id} : {str(e)}")
check_instance_status(instance_id)
