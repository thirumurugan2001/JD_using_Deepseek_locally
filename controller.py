from ConnectAPI import *

# This validateData function is use to Validate the payload is not empty and string format.
def validateData(data):
    try:
        if data["company"] != ""  and data["location"] != "" and data["job-type"] != ""  and data["experience"] != "" and data["skills"] and data['education'] and data['job-title']:
            return openai(data)
        else:
            return {
                "message":"Invaild data !",
                "status":400
            }
    except Exception as e:
        return {
                "Error":str(e),
                "statusCode":500
            }

