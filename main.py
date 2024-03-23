from fastapi import FastAPI, HTTPException
import json
import requests
from crypto import encrypt, decrypt

app = FastAPI()

# Load configuration from file

with open("config.json", "r") as config_file:
    config = json.load(config_file)

headers = {
            "Content-Type": "application/json"
        }
# Example route to encrypt a payload
@app.post("/encrypt_decrypt")
def encrypt_decrypt(payload: dict):
    try:
        # Encrypt the payload
        encrypted_payload = encrypt(json.dumps(payload), config["encryption_key"])

        # Construct the request data for decryption
        decryption_data = {
            "payload": encrypted_payload,
            "uId": "AGEN5500134316"
        }

        # Send the encrypted payload to the API endpoint
        response = requests.post(config["api_endpoint_url"], json=decryption_data, headers=headers)

        # Decrypt the response payload
        decrypted_payload = decrypt(response.json()["payload"], config["encryption_key"])

        return {"decrypted_payload": json.loads(decrypted_payload),"full responce" : response.json()}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
