import os
import hmac



import sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration


SENTRY_DSN=os.getenv("SENTRY_DSN")

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[
        AwsLambdaIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)

# header validation
#https://developer.hashicorp.com/terraform/cloud-docs/api-docs/notification-configurations#notification-authenticity
def verify_signature(req, token):
    received_sign = req.headers.get('X-TFE-Notification-Signature')
    secret = secret.encode()
    expected_sign = hmac.HMAC(key=token, msg=req.data, digestmod=hashlib.sha256).hexdigest()
    return hmac.compare_digest(received_sign, expected_sign)




def handler(event, context):
    pass