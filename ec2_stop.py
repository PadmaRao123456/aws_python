import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Your EC2 Instance ID (Replace with actual ID)
instance_id = "i-08d49b255d44a745e"

def stop_ec2_instance(instance_id):
    try:
        response = ec2.stop_instances(InstanceIds=[instance_id])
        print(f"Stopping instance {instance_id} ...")
        
        # Print the current state
        for instance in response['StoppingInstances']:
            print(f"Instance ID: {instance['InstanceId']}, State: {instance['CurrentState']['Name']}")

    except Exception as e:
        print(f"Error stopping instance {instance_id}: {str(e)}")

# Call the function
stop_ec2_instance(instance_id)
