import boto3

ec2 = boto3.resource('ec2', region_name='us-east-2', api_version='2016-04-01', aws_access_key_id='AKIA5DCDMB67XVRNYFUH', aws_secret_access_key= '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') 

# how many instance running
instancesCount=0
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    instancesCount+=1
print("instances:",instancesCount)


# create vpc and subnet 
vpc = ec2.create_vpc(CidrBlock='10.10.0.0/16')
vpc.create_tags(Tags=[{"Key": "Name", "Value": "Deloitte_VPC"}])
subnet = ec2.create_subnet(CidrBlock='10.10.0.0/16', VpcId=vpc.id)
# vpc.wait_until_available()

# opsworks = boto3.connect_opsworks(aws_access_key_id='AKIA5DCDMB67XVRNYFUH', aws_secret_access_key='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')
# create ec2 in the vpc
instances = ec2.create_instances(
    ImageId='ami-0952fb5203ddacf5c',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='keypair6/11/20',
    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True}],
    id='1'
 )