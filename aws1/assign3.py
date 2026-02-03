import boto3

rekognition = boto3.client( "rekognition",region_name="ap-south-1"  )
translate = boto3.client("translate")
response = rekognition.detect_text(
    Image={'S3Object': {'Bucket': 'aks-amazon-a1', 'Name': 'p2.png'}}
)
text = " ".join(item['DetectedText']
    for item in response['TextDetections']
    if item['Type'] == 'LINE')
translated = translate.translate_text(Text=text,SourceLanguageCode="auto",
    TargetLanguageCode="en")

print("Detected:", text)
print("Translated:", translated["TranslatedText"])
