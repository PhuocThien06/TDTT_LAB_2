from fastapi import APIRouter, Header, HTTPException
from firebase_config import db
from datetime import datetime
from auth import verify_token

router = APIRouter()

@router.post("/notes")
def create_note(content: str, authorization: str = Header(...)):
    user_id = verify_token(authorization)

    note = {
        "user_id": user_id,
        "content": content,
        "created_at": str(datetime.now())
    }

    db.collection("notes").add(note)
    return {"message": "Note saved"}


@router.get("/notes")
def get_notes(authorization: str = Header(...)):
    user_id = verify_token(authorization)

    docs = db.collection("notes").where("user_id", "==", user_id).stream()

    result = []
    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        result.append(data)

    return result


@router.delete("/notes/{note_id}")
def delete_note(note_id: str, authorization: str = Header(...)):
    user_id = verify_token(authorization)

    doc_ref = db.collection("notes").document(note_id)
    doc = doc_ref.get()

    if not doc.exists:
        raise HTTPException(status_code=404, detail="Note not found")

    data = doc.to_dict()

    if data["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Not allowed")

    doc_ref.delete()
    return {"message": "Deleted"}