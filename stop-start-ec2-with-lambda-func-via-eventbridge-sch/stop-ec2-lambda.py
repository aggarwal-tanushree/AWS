import boto3

region = 'eu-central-1'


def lambda_handler(event, context):
    ec2_resource = boto3.resource("ec2", region_name=region)
    
    # Apply filter to check for EC2 instances in 'running' state
    instances = ec2_resource.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    print("EC2 region is: ", region)
    print("instances= ", instances)
    
    # Count running instances
    count = len(list(instances))
    print(f"{count} instances running")
    
    # Stopping EC2 instances        
    for instance in instances:
        instance.stop()
        print(instance, ": Stopping!!! .")
        
