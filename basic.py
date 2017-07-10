import jwt
import datetime
import time

payload = {
    "uid": 23,
    "name": "raghu",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=2)
}

SECRET_KEY = "N0TV3RYS3CR3T"

token = jwt.encode(payload=payload, key=SECRET_KEY)

print("Generated token: {}".format(token.decode()))

decoded_payload = jwt.decode(jwt=token, key=SECRET_KEY)

print("Decoded payload: {}".format(decoded_payload))
