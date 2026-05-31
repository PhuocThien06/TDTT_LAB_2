# 📝 NOTE APP USING FASTAPI + STREAMLIT + FIREBASE

## 1. Thông tin sinh viên
- **Họ tên:** Đỗ Phước Thiện  
- **MSSV:** 24120139  
- **Môn học:** Tư duy tính toán  

---

## 2. Công nghệ sử dụng
- **Backend:** FastAPI  
- **Frontend:** Streamlit  
- **Database:** Firebase Firestore  
- **Authentication:** Firebase Authentication (Email/Password)  

---

## 3. Mô tả hệ thống
Hệ thống xây dựng một ứng dụng ghi chú (Note App) cho phép người dùng:

- Đăng nhập bằng tài khoản Firebase  
- Thêm ghi chú  
- Xem danh sách ghi chú  
- Xóa ghi chú  

Hệ thống có **phân quyền**, mỗi người dùng chỉ có thể thao tác trên dữ liệu của mình.

---

## 4. Cài đặt môi trường (Environment)

### Yêu cầu
- Python **3.10**

### Cài đặt thư viện
```bash
pip install -r requirements.txt
```

---

## 5. Cấu hình Firebase

1. Truy cập: https://console.firebase.google.com  
2. Tạo project mới  
3. Bật:
   - Authentication → Email/Password  
   - Firestore Database  
4. Tạo Service Account  
5. Tải file JSON  

```bash
backend/firebase_key.json
```

## 6. Chạy backend

```bash
cd backend
uvicorn main:app --reload
```
Truy cập:
```
http://127.0.0.1:8000
```
Kiểm tra:
```
http://127.0.0.1:8000/health
```

---

## 7. Chạy frontend

Mở terminal khác:

```bash
cd frontend
streamlit run app.py
```
Truy cập:
```
http://localhost:8501
```

---

## 8. API

### 🔹 GET /
Kiểm tra hệ thống

```json
{
  "message": "API running"
}
```

---

### 🔹 GET /health
Kiểm tra trạng thái

```json
{
  "status": "ok"
}
```

---

### 🔹 POST /notes
Tạo ghi chú

**Request:**
```
content=Hello
```

**Header:**
```
Authorization: Bearer <Firebase Token>
```

**Response:**
```json
{
  "message": "Note saved"
}
```

---

### 🔹 GET /notes
Lấy danh sách ghi chú

```json
[
  {
    "content": "Hello",
    "created_at": "...",
    "id": "..."
  }
]
```

---

### 🔹 DELETE /notes/{note_id}
Xóa ghi chú

```json
{
  "message": "Deleted"
}
```

---

## 9. Kiểm thử

- Cách 1: Sử dụng giao diện Streamlit  
- Cách 2: Sử dụng Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 10. Phân quyền

- Người dùng phải đăng nhập để sử dụng hệ thống  
- Mỗi ghi chú được gắn `user_id`  
- Người dùng chỉ có thể:
  - Xem note của mình  
  - Xóa note của mình  

---

## 11. Video demo

Link:
```
https://drive.google.com/drive/folders/1m4FotHrMV7Yq_RrY7lzoDnQGLkhpIBjL?usp=sharing

---

## 12. Ghi chú

- Backend xác thực bằng Firebase ID Token  
- Frontend tự động cập nhật dữ liệu sau khi thêm/xóa  
- Ứng dụng chạy local trên máy
