def validate_api_response(response):
    if not isinstance(response, dict):
        return False

    if "status_code" not in response:
        return False

    if "body" not in response:
        return False

    return True


# Example usage
response = {
    "status_code": 200,
    "body": {"message": "Success"}
}

print(validate_api_response(response))