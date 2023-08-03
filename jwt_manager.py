from jwt import encode, decode

def create_token(data: dict) -> str:
    token: str = encode(payload=data, key="my_secret_key", algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    data: dict = decode(token, key="my_secret_key", algorithm=['HS256'])
    return data

'''
# Alternativa mas robusta al codigo anterior:

from jwt import encode, decode, InvalidTokenError

def create_token(data: dict) -> str:
    try:
        token: str = encode(payLoad=data, key="my_secret_key", algorithm="HS256")
        return token
    except Exception as e:
        print(f"Error creating token: {e}")
        return ""

def validate_token(token: str) -> dict:
    try:
        data: dict = decode(token, key="my_secret_key", algorithm=['HS256'])
        return data
    except InvalidTokenError:
        print("Invalid token")
        return {}
    except Exception as e:
        print(f"Error validating token: {e}")
        return {}
'''