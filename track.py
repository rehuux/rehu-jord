# Developer: @istgrehu
# Owner: Syed Rehan

import json
import requests

def handler(event, context):

    # Query Params
    params = event.get("queryStringParameters", {}) or {}
    num = params.get("num", "")

    # Validation
    if not num or len(num) != 10 or not num.isdigit():
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "success": False,
                "message": "Invalid mobile number",
                "developer": "@istgrehu",
                "owner": "Syed Rehan"
            })
        }

    try:
        # YOUR API URL (this is correct)
        api_url = f"https://splexxo-bhai.vercel.app/api/seller?mobile={num}&key=SPLEXXO"

        r = requests.get(api_url, timeout=30)
        data = r.json()

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "success": True,
                "developer": "@istgrehu",
                "owner": "Syed Rehan",
                "data": data
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "success": False,
                "message": str(e),
                "developer": "@istgrehu",
                "owner": "Syed Rehan"
            })
        }
