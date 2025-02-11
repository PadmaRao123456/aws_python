import boto3
#create EC2 Client
ec2=boto3.client('ec2')
#your Ec2 Instance ID
instance_id  = "i-08d49b255d44a745e"
#def check_instance_status(instance_id):
#    try:
#        response = ec2.describe_instance_status(InstanceIds=[instance_id])
#        print(response)
#    except Exception as e:
#        print(f"Error checking instance {instance_id} : {str(e)}")
#check_instance_status(instance_id)

#call describe instances
response=ec2.describe_instance_status(InstanceIds=[instance_id])
#print only first item in the list
if "InstanceStatuses"  in response  and len(response["InstanceStatuses"]) > 0:
    print(response["InstanceStatuses"][0])
else:
    print(f"No Status available for instance {instance_id}")    