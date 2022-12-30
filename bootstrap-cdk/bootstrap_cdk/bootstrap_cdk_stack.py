from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as lambda_,
    aws_lambda_python_alpha as lambda_alpha_,
    aws_apigateway as apigateway,
    aws_logs as logs
)
from constructs import Construct


class BootstrapCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        self.build_infrastructure()

    def build_infrastructure(self):
        self.build_fastapiexample_function()
        self.build_fastapiexample_api_gateway()

    def build_fastapiexample_function(self):
        self.function_fastapiexample_api = lambda_alpha_.PythonFunction(self,
                                                                        "function-fastapiexample-api",
                                                                        entry="../app",
                                                                        index="main.py",
                                                                        handler="handler",
                                                                        runtime=lambda_.Runtime.PYTHON_3_8)

    def build_fastapiexample_api_gateway(self):
        prod_log_group = logs.LogGroup(self, "ProdLogs")
        self.apigateway_fastapiexample_api = apigateway.LambdaRestApi(self,
                                                                      "apigateway-fastapiexample-api",
                                                                      handler=self.function_fastapiexample_api,
                                                                      proxy=True,
                                                                      cloud_watch_role=True,
                                                                      deploy_options=apigateway.StageOptions(             
                                                                          stage_name="prod",
                                                                          logging_level=apigateway.MethodLoggingLevel.INFO,                                                             
                                                                          access_log_destination=apigateway.LogGroupLogDestination(
                                                                              prod_log_group),
                                                                          access_log_format=apigateway.AccessLogFormat.json_with_standard_fields(
                                                                              caller=False,
                                                                              http_method=True,
                                                                              ip=True,
                                                                              protocol=True,
                                                                              request_time=True,
                                                                              resource_path=True,
                                                                              response_length=True,
                                                                              status=True,
                                                                              user=True
                                                                          ), 
                                                                      )
                                                                      )
