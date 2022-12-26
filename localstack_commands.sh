#list lambda
aws lambda list-functions \
    --endpoint-url http://localhost:4566

#create lambda with hotswap
aws lambda create-function \
    --function-name test-function \
    --runtime python3.8 \
    --code S3Bucket="__local__",S3Key="/home/jsmith/source/repos/sandbox/fastapi-app/app" \
    --handler main.handler \
    --role cool-stacklifter \
    --endpoint-url http://localhost:4566

#create lambda
aws lambda create-function \
    --function-name test-function \
    --runtime python3.8 \
    --zip-file fileb://./zips/function.zip \
    --handler main.handler \
    --role cool-stacklifter \
    --endpoint-url http://localhost:4566

#update lambda code
aws lambda update-function-code \
    --function-name test-function \
    --zip-file fileb://./zips/function.zip \
    --endpoint-url http://localhost:4566

#update lambda config
aws lambda update-function-configuration \
    --function-name test-function \
    --handler main.handler \
    --endpoint-url http://localhost:4566

#create lambda URL
aws lambda create-function-url-config \
    --function-name test-function \
    --auth-type NONE \
    --endpoint-url http://localhost:4566

#http://7697f655b17e5db7dccc160077b2fd34.lambda-url.us-east-1.localhost.localstack.cloud:4566/docker p s

#create cloud watch
aws cloudwatch put-metric-data \
    --namespace test \
    --metric-data '[{"MetricName": "Orders", "Value": 20}]' \
    --endpoint-url http://localhost:4566

#get cloud watch metrics
aws cloudwatch get-metric-data \
    --metric-data-queries '[{"Id": "my-id","MetricStat": {"Metric": {"Namespace": "test","MetricName": "Orders"},"Period": 3600, "Stat": "Sum" }}]' \
    --start-time 2022-05-04T08:00:00Z \
    --end-time  2023-05-04T19:00:00Z \
    --endpoint-url http://localhost:4566
