def lambda_handler(event, context):
    print('lambda function fass is triggered !!')
    import anchor
    
    key = event['Records'][0]['s3']['object']['key']
    print("Processing file - ",key)    
    source_bucket = event['Records'][0]['s3']['bucket']['name']
     
    source = {'Bucket': source_bucket, 'Key': key}
    print("Source is - ",source)
    
    anchor.move_file(source_bucket, key);
