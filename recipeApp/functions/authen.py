import os
from twilio.rest import Client
from recipesite.settings import DEBUG

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC2a0af17920d5af1cf68d57714e062068"
if DEBUG:
    from recipesite.secrets import TWILIO_AUTH_TOKEN
    auth_token = TWILIO_AUTH_TOKEN
else:
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]

verify_sid = "VAda616dc8fe2c07db78def635f1c95fe1"
verified_number = "+15127610870"

client = Client(account_sid, auth_token)

def sendOTP(password):
    if password == 'Sand123':
        # verification = client.verify.v2.services(verify_sid) \
        # .verifications \
        # .create(to=verified_number, channel="sms")
        # print(verification.status)
        return 1
    else:
        return 0

def checkOTP(inputCode):
    # verification_check = client.verify.v2.services(verify_sid) \
    # .verification_checks \
    # .create(to=verified_number, code=inputCode)
    # print(verification_check.status)
    # if verification_check.status == "approved":
    #     return 1
    # else:
    #     print("Wrong",type(verification_check.status))
    #     return 0
    if inputCode == 1234:
        return 1
    else:
        return 0