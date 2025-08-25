# 🦺 Ứng Dụng Giám Sát An Toàn Lao Động Bằng AI  

![FIT-DNU](https://github.com/user-attachments/assets/2f53f6dd-ff4b-4890-b05a-ba7935ed6f9f)

---

## 📌 Nội dung

<details>
  <summary>📖 Giới thiệu</summary>

Ứng dụng web này cho phép người dùng tải lên video hoặc kết nối camera giám sát công trường và sử dụng AI (**YOLOv11**) để:

- Nhận diện và theo dõi người lao động trong công trường.  
- Phát hiện & trích xuất tình trạng đội mũ bảo hộ, mặc áo phản quang, đi giày bảo hộ.  
- Thống kê & hiển thị báo cáo trực quan về mức độ tuân thủ an toàn lao động.  

<img width="1920" height="1096" alt="image" src="https://github.com/user-attachments/assets/8d936cfa-1957-48f4-b0d1-2664de47ebed" />

</details>

---

<details>
  <summary>🚀 Tính năng chính</summary>

- **Nhận diện PPE (Đồ bảo hộ):** Mũ bảo hộ, áo phản quang, giày bảo hộ.  
- **Phân tích thông minh:** Xác định tình trạng thiếu PPE và hiển thị cảnh báo trực tiếp trên video.  
- **Thống kê & báo cáo:** Đếm số lượng công nhân tuân thủ/vi phạm, biểu đồ trực quan.  
- **Xem trực tiếp & tra cứu:** Hiển thị kết quả theo thời gian thực, tìm kiếm & xem lại dữ liệu đã xử lý.  
- **Xuất dữ liệu:** Lưu Excel, video kết quả.  

<img width="1920" height="1051" alt="image" src="https://github.com/user-attachments/assets/44d5c708-f392-4c04-8fed-41c0c8e07a8c" />  
<img width="1920" height="1047" alt="image" src="https://github.com/user-attachments/assets/db7d84ad-0fd9-407b-8502-e7c3c208c496" />  
<img width="1920" height="632" alt="image" src="https://github.com/user-attachments/assets/5b198860-d5eb-4fc0-889d-066ca7d7a32e" />  

</details>

---

<details>
  <summary>🛠️ Công nghệ sử dụng</summary>

- **Frontend:** Streamlit (Python), HTML5, CSS3  
- **AI / Detection:** YOLOv11 (Ultralytics)  
- **Xử lý video:** OpenCV  
- **Thống kê & trực quan hóa:** Pandas, Plotly Express  
- **Triển khai:** Ngrok / Streamlit Cloud / Docker  

</details>

---

<details>
  <summary>📂 Cấu trúc chính & Cách chạy</summary>

**Cấu trúc**  
- `PPE.py` → Giao diện web + logic xử lý  
- `models/` → Chứa file huấn luyện YOLO + data.yaml  
- `data/` → Video, hình ảnh test  
- `reports/` → Lưu kết quả thống kê, Excel  

**Cách chạy**  
```bash
# Bước 1: Cài đặt thư viện
pip install -r requirements.txt
pip install streamlit pyngrok ultralytics opencv-python-headless plotly pandas

# Bước 2: Chạy ứng dụng
streamlit run PPE.py

# Bước 3: (Tùy chọn) Kết nối Ngrok để public
from pyngrok import ngrok
ngrok.set_auth_token("YOUR_TOKEN")
public_url = ngrok.connect(8501, "http")
print(public_url)

