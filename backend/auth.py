from fastapi import APIRouter, Header, HTTPException
from firebase_admin import auth

router = APIRouter()

def verify_token(authorization: str):
    try:
        token = authorization.split(" ")[1]
        decoded = auth.verify_id_token(token)
        return decoded["uid"]
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.get("/auth/me")
def get_me(authorization: str = Header(...)):
    uid = verify_token(authorization)
    return {"uid": uid}