from fastapi import FastAPI, HTTPException
import json
from crypto import encrypt, decrypt
app = FastAPI()


import os
import base64

# Generate a random Secret Key
secret_key = base64.b64encode(os.urandom(32)).decode()

print("Random Secret Key:", secret_key)

# Load configuration from file
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Define your routes using the configuration
@app.get("/")
def read_root():
    return {"message": "Test credentials loaded successfully!"}

@app.get("/test")
def test_credentials():
    return {
        "api_endpoint_url": config["api_endpoint_url"],
        "encryption_key": config["encryption_key"],
        "ag_id": config["ag_id"],
        "m_id": config["m_id"],
        "session_id": config["session_id"],
        "u_id": config["u_id"]
    }

# secret_key="123456"

# Example route to encrypt a payload
@app.post("/encrypt")
def encrypt_payload(payload: dict):
    try:
        encrypted_payload = encrypt(json.dumps(payload), secret_key)
        return {"encrypted_payload": encrypted_payload}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Example route to decrypt a payload
@app.post("/decrypt")
def decrypt_payload(encrypted_payload: str):
    try:
        decrypted_payload = decrypt(encrypted_payload, secret_key)
        return {"decrypted_payload": json.loads(decrypted_payload)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
