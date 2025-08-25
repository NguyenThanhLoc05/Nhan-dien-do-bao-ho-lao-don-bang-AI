![FIT-DNU](https://github.com/user-attachments/assets/2f53f6dd-ff4b-4890-b05a-ba7935ed6f9f)
st.markdown("""
# 🦺 Ứng Dụng Giám Sát An Toàn Lao Động Bằng AI
## 📌 Giới thiệu

Ứng dụng web này cho phép người dùng tải lên video hoặc kết nối camera giám sát công trường và sử dụng AI (YOLOv11) để:

Nhận diện và theo dõi người lao động trong công trường.

Phát hiện & trích xuất tình trạng đội mũ bảo hộ, mặc áo phản quang, đi giày bảo hộ.

Thống kê & hiển thị báo cáo trực quan về mức độ tuân thủ an toàn lao động.

<img width="1920" height="1096" alt="image" src="https://github.com/user-attachments/assets/8d936cfa-1957-48f4-b0d1-2664de47ebed" />


## 🚀 Tính năng chính

Nhận diện PPE (Đồ bảo hộ)

Phát hiện mũ bảo hộ, áo phản quang, giày bảo hộ trong video/camera.

<img width="1920" height="1051" alt="image" src="https://github.com/user-attachments/assets/44d5c708-f392-4c04-8fed-41c0c8e07a8c" />

Phân tích thông minh

Xác định tình trạng thiếu PPE và hiển thị cảnh báo trực tiếp trên video.

<img width="1920" height="1047" alt="image" src="https://github.com/user-attachments/assets/db7d84ad-0fd9-407b-8502-e7c3c208c496" />

Thống kê & báo cáo

Đếm số lượng công nhân tuân thủ/vi phạm.

Biểu đồ trực quan về tỉ lệ an toàn lao động.

<img width="1920" height="632" alt="image" src="https://github.com/user-attachments/assets/5b198860-d5eb-4fc0-889d-066ca7d7a32e" />

Xem trực tiếp & tra cứu

Hiển thị kết quả phát hiện theo thời gian thực.

Tìm kiếm & xem lại dữ liệu đã xử lý.

Xuất dữ liệu, video để xem kết quả

## 🛠️ Công nghệ sử dụng

Frontend: Streamlit (Python), HTML5, CSS3

AI / Detection: YOLOv11 (Ultralytics)

Xử lý video: OpenCV

Thống kê & trực quan hóa: Pandas, Plotly Express

Triển khai: Ngrok / Streamlit Cloud / Docker

## 📂 Cấu trúc chính

PPE.py → Giao diện web + toàn bộ logic xử lý.
Ứng dụng được xây dựng trên Streamlit, hỗ trợ:

Tab “Giám sát trực tiếp”: Kết nối camera hoặc tải video để phát hiện mũ, áo, giày bảo hộ.

Tab “Thống kê & Báo cáo”: Hiển thị số liệu tuân thủ/vi phạm, biểu đồ trực quan.

Tab “Dữ liệu đã lưu”: Xem lại kết quả, báo cáo hoặc xuất Excel.
## ⚡ Cách chạy

Clone hoặc tải source code về máy.

Bước 1: Cài đặt thư viện cần thiết:
pip install -r requirements.txt
pip install streamlit pyngrok ultralytics opencv-python-headless

Bước 2: Chạy ứng 
streamlit run PPE.py
Bước 3: Kết nối Ngrok để public
from pyngrok import ngrok
ngrok.set_auth_token("YOUR_TOKEN")
public_url = ngrok.connect(8501, "http")
print(public_url)

## 📸 Giao diện

Hiển thị video với bounding box PPE.

Cột bên phải: thống kê, biểu đồ, báo cáo.

Có thể xuất Excel hoặc lưu dữ liệu.

## 🌟 Ý nghĩa & giá trị thực tiễn

Ứng dụng mang lại giải pháp quản lý an toàn lao động thông minh cho:

Doanh nghiệp xây dựng: Giám sát công nhân tại công trường.

Khu công nghiệp, nhà máy: Đảm bảo tuân thủ PPE.

Cơ quan quản lý: Dễ dàng thống kê, lập báo cáo định kỳ.



✨ **Đây là một công cụ hữu ích cho doanh nghiệp xây dựng, khu công nghiệp và nhà máy** trong việc giám sát an toàn lao động.  
Ứng dụng giúp **tự động nhận diện** công nhân có trang bị đầy đủ mũ bảo hộ, áo phản quang, giày bảo hộ hay không thông qua **camera giám sát hoặc video**.  
""")

