import streamlit as st
import requests

API_KEY = "AIzaSyAY5tzmHZHhUXY8cPRCj9Sro4JteFRgrI8"
BACKEND_URL = "http://127.0.0.1:8000"

st.title("📝 Note App")

# LOGIN
st.subheader("🔐 Đăng nhập")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if "token" not in st.session_state:
    st.session_state.token = None

if st.button("Login"):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"

    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    res = requests.post(url, json=payload)

    if res.status_code == 200:
        data = res.json()
        st.session_state.token = data["idToken"]
        st.session_state.email = data["email"]
        st.success("Login thành công!")
        st.rerun()
    else:
        st.error("Sai tài khoản hoặc mật khẩu")

# SAU LOGIN
if st.session_state.token:

    headers = {
        "Authorization": f"Bearer {st.session_state.token}"
    }

    st.success(f"Đã đăng nhập: {st.session_state.email}")

    if st.button("Logout"):
        st.session_state.token = None
        st.rerun()

    # THÊM NOTE
    st.subheader("Thêm ghi chú")
    content = st.text_area("Nội dung")

    if st.button("Lưu note"):
        if content.strip() == "":
            st.warning("⚠️ Vui lòng nhập nội dung")
        else:
            res = requests.post(
                f"{BACKEND_URL}/notes",
                params={"content": content},
                headers=headers
            )

            if res.status_code == 200:
                st.success("✅ Lưu note thành công!")
                st.toast("Đã lưu ghi chú 🎉")
                st.rerun()
            else:
                st.error("❌ Lỗi khi lưu note")

    # DANH SÁCH NOTE
    st.subheader("Danh sách ghi chú")

    res = requests.get(
        f"{BACKEND_URL}/notes",
        headers=headers
    )

    if res.status_code == 200:
        data = res.json()

        if len(data) == 0:
            st.info("📭 Chưa có ghi chú")
        else:
            for note in data:
                st.markdown(f"### 📝 {note['content']}")
                st.caption(f"⏱ {note['created_at']}")

                if st.button("❌ Xóa", key=note["id"]):
                    res = requests.delete(
                        f"{BACKEND_URL}/notes/{note['id']}",
                        headers=headers
                    )

                    if res.status_code == 200:
                        st.success("Đã xóa")
                        st.toast("Đã xóa 🗑️")
                        st.rerun()
                    else:
                        st.error("Không xóa được")

                st.divider()
    else:
        st.error("❌ Không tải được danh sách")