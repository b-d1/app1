import requests
import json

def send_message_prod(api_body):
    try:
        print("sending message")
        response = requests.post(url="http://app2-prod-service.prod:5001/api/v1/api", json=api_body)
        response_json = json.loads(response.content.decode())
        if response.status_code == 200:
            return {"status": "success", "response": response_json}, 200
        else:
            return {"status": "error", "response": response_json}, 500
    except Exception as ex:
        print("error received")
        return {
            'error': str(ex)
        }, 400


def send_message_dev(api_body):
    try:
        print("sending message")
        response = requests.post(url="http://app2-dev-service.dev:5001/api/v1/api", json=api_body)
        response_json = json.loads(response.content.decode())
        if response.status_code == 200:
            return {"status": "success", "response": response_json}, 200
        else:
            return {"status": "error", "response": response_json}, 500
    except Exception as ex:
        print("error received")
        return {
            'error': str(ex)
        }, 400


def send_message_test(api_body):
    try:
        print("sending message")
        response = requests.post(url="http://app2-test-service.test:5001/api/v1/api", json=api_body)
        response_json = json.loads(response.content.decode())
        if response.status_code == 200:
            return {"status": "success", "response": response_json}, 200
        else:
            return {"status": "error", "response": response_json}, 500
    except Exception as ex:
        print("error received")
        return {
            'error': str(ex)
        }, 400
