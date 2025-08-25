![FIT-DNU](https://github.com/user-attachments/assets/2f53f6dd-ff4b-4890-b05a-ba7935ed6f9f)
🦺 Ứng Dụng Giám Sát An Toàn Lao Động Bằng AI
📌 Giới thiệu

Ứng dụng web này cho phép người dùng tải lên video/camera giám sát công trường và sử dụng công nghệ AI (YOLOv11) để:
Nhận diện và theo dõi người lao động trong công trường.
Phát hiện và trích xuất thông tin quan trọng: tình trạng đội mũ bảo hộ, mặc áo phản quang, đi giày bảo hộ.
Thống kê và hiển thị báo cáo trực quan về việc tuân thủ an toàn lao động.
<img width="1920" height="1096" alt="image" src="https://github.com/user-attachments/assets/ccfa02d2-0c79-40e4-a02b-31d1d5ff6f0d" />

🚀 Tính năng chính
Nhận diện PPE (Đồ bảo hộ): Tự động phát hiện mũ bảo hộ, áo phản quang, giày bảo hộ trong video/camera công trường.
Phân tích thông minh: AI xác định tình trạng thiếu đồ bảo hộ (thiếu mũ, áo, giày) và hiển thị cảnh báo trực tiếp.
Thống kê & báo cáo:
Đếm số lượng người lao động tuân thủ và vi phạm.
Biểu đồ trực quan về tỉ lệ an toàn lao động.
Xem trực tiếp & tra cứu:
Xem kết quả phát hiện theo thời gian thực từ video/camera.
Tìm kiếm và xem lại kết quả đã xử lý.
Xuất dữ liệu:
Lưu báo cáo thống kê dưới dạng Excel (.xlsx).
Xuất danh sách vi phạm an toàn lao động.
Quản lý giám sát:
Xem lại video/ảnh đã phân tích.
Lọc và xóa dữ liệu không cần thiết.
🛠️ Công nghệ sử dụng

Frontend: Streamlit (Python), HTML5, CSS3

AI / Detection: YOLOv11 (Ultralytics)

Xử lý video: OpenCV

Thống kê & trực quan hóa: Pandas, Plotly Express

Lưu trữ dữ liệu: (Tuỳ chọn) Firebase / SQLite / Google Drive

Triển khai: Ngrok / Streamlit Cloud / Docker
📂 Cấu trúc chính

PPE.py → Giao diện web + toàn bộ logic xử lý.
Ứng dụng được xây dựng trên Streamlit, hỗ trợ:

Tab “Giám sát trực tiếp”: Kết nối camera hoặc tải video để phát hiện mũ, áo, giày bảo hộ.

Tab “Thống kê & Báo cáo”: Hiển thị số liệu tuân thủ/vi phạm, biểu đồ trực quan.

Tab “Dữ liệu đã lưu”: Xem lại kết quả, báo cáo hoặc xuất Excel.
⚡ Cách chạy

Clone hoặc tải source code về máy.

Bước 1: Cài đặt thư viện cần thiết:
pip install -r requirements.txt
!pip install -r requirements.txt
!pip install pyngrok ultralytics streamlit
!streamlit run app.py --server.port 8501 &
!pip install streamlit pyngrok
!pip install streamlit pyngrok ultralytics opencv-python-headless
Bước 2: streamlit run PPE.py
Bước 3: from pyngrok import ngrok

!ngrok authtoken 31hCjltcn2orcsPQ2SLnFgmfVve_vWQJowKySFYrDUQ5dGmW

# Chạy Streamlit
get_ipython().system_raw("streamlit run app.py --server.port 8501 &")

# Tạo link public
public_url = ngrok.connect(8501, "http")
print(public_url)
Truy cập địa chỉ hiển thị (thường là http://localhost:8501) để sử dụng.

Chọn Tải video / Kết nối camera để thử nghiệm.

Kết quả phát hiện hiển thị ở cột bên phải, kèm theo số lượng, biểu đồ và cảnh báo.
📸 Giao diện

Giao diện hiện đại, đơn giản, sử dụng Streamlit + CSS tùy chỉnh.

Hỗ trợ chế độ upload video hoặc camera trực tiếp.

Hiển thị khung phát hiện đối tượng (bounding box) trên video.

Cột bên phải hiển thị:

Thống kê số lượng PPE đầy đủ/thiếu.

Biểu đồ trực quan.

Nút xuất Excel hoặc lưu dữ liệu.
✨ Đây là một giải pháp hữu ích cho các doanh nghiệp xây dựng, khu công nghiệp, nhà máy hoặc công trình thi công trong việc giám sát an toàn lao động. Ứng dụng giúp tự động nhận diện việc công nhân có trang bị đầy đủ mũ bảo hộ, áo phản quang, giày bảo hộ hay không thông qua camera giám sát hoặc video.
