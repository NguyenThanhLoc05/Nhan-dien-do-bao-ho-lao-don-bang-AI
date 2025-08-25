# app.py
import streamlit as st
from ultralytics import YOLO
import cv2
import os
import pandas as pd
import plotly.express as px

# --- Streamlit page config ---
st.set_page_config(
    page_title="🦺 Giám sát an toàn lao động AI",
    layout="wide",
    page_icon="🦺"
)

# --- CSS chung & style cho 2 khung ---
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #fdfcfb, #e2d1c3);
        color: #333333;
        font-family: 'Segoe UI', sans-serif;
    }
    .stApp { background: linear-gradient(135deg, #fdfcfb, #e2d1c3); }

    h1, h2, h3, h4 {
        text-align: center;
        color: #2c3e50;
        font-weight: bold;
        text-shadow: 1px 1px 3px rgba(255,255,255,0.6);
    }

    .stButton>button {
        background: linear-gradient(90deg, #FFD194, #D1913C);
        color: white;
        border-radius: 10px;
        padding: 0.6em 1.2em;
        font-size: 16px;
        font-weight: bold;
        transition: 0.3s ease-in-out;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #D1913C, #FFD194);
        transform: scale(1.05);
    }

    .stFileUploader>div>div>label { color: #2c3e50; font-size: 16px; font-weight: bold; }
    .stSelectbox>div>div>select {
        background-color: #f0f0f0; color: #2c3e50; border-radius: 6px;
        padding: 0.3em; border: 1px solid #ccc;
    }
    table { color: #2c3e50 !important; }

    /* Hiệu ứng vào khung */
    @keyframes fadeInUp { from {opacity:0; transform: translateY(8px);} to {opacity:1; transform:none;} }

    div[data-testid="stVerticalBlockBorderWrapper"]:has(> .stat1),
    div[data-testid="stVerticalBlockBorderWrapper"]:has(> .stat2){
        border: 5px solid #000;
        border-radius: 14px;
        background: rgba(255,255,255,0.95);
        box-shadow: 6px 10px 24px rgba(0,0,0,0.35);
        padding: 16px;
        margin-top: 16px;
        animation: fadeInUp .45s ease both;
        transition: transform .25s ease, box-shadow .25s ease, background .25s ease;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:has(> .stat1):hover,
    div[data-testid="stVerticalBlockBorderWrapper"]:has(> .stat2):hover{
        transform: scale(1.01);
        box-shadow: 8px 12px 28px rgba(0,0,0,0.4);
        background: rgba(255,255,255,0.98);
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:has(> .stat1) h2,
    div[data-testid="stVerticalBlockBorderWrapper"]:has(> .stat2) h2,
    div[data-testid="stVerticalBlockBorderWrapper"]:has(> .stat1) h3,
    div[data-testid="stVerticalBlockBorderWrapper"]:has(> .stat2) h3{
        color: #000 !important; text-shadow: none; font-weight: 800;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:has(> .stat1) table,
    div[data-testid="stVerticalBlockBorderWrapper"]:has(> .stat2) table,
    div[data-testid="stVerticalBlockBorderWrapper"]:has(> .stat1) th,
    div[data-testid="stVerticalBlockBorderWrapper"]:has(> .stat2) th,
    div[data-testid="stVerticalBlockBorderWrapper"]:has(> .stat1) td,
    div[data-testid="stVerticalBlockBorderWrapper"]:has(> .stat2) td{
        color: #000 !important; font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True
)

# --- TITLE ---
st.title("🦺 Giám sát an toàn lao động bằng AI")

# --- Chọn công trường ---
st.header("📷 Camera công trường")
camera_choice = st.selectbox("Chọn công trường:", ["Công trường 1", "Công trường 2"])

# --- Video mặc định ---
camera_videos = {
    "Công trường 1": "videos/Công trường 1.mp4",
    "Công trường 2": "videos/Công trường 2.mp4"
}
video_path = camera_videos.get(camera_choice, None)

# --- Upload video khác ---
st.header("🎥 Hoặc upload video khác")
uploaded_file = st.file_uploader("Chọn video", type=["mp4", "avi"])
if uploaded_file is not None:
    os.makedirs("videos", exist_ok=True)
    video_path = os.path.join("videos", uploaded_file.name)
    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())

if video_path:
    processing_placeholder = st.empty()
    processing_placeholder.info("⏳ Đang phân tích video... Vui lòng chờ một chút")

    # --- Load YOLO model ---
    model = YOLO('runs/detect/train/weights/best.pt')

    # --- Chuẩn bị lưu video kết quả ---
    os.makedirs("results", exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        st.error(f"Không thể mở video: {video_path}")
    else:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(
            'results/output_video.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS),
            (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        )

        # Bộ nhớ lưu object đã đếm
        detected_objects = {
            "Person": set(), "Safety-Helmet": set(),
            "Safety-Vest": set(), "Safety-Boots": set()
        }
        counts = {k: 0 for k in detected_objects.keys()}
        first_frame = None

        # --- Xử lý video ---
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            results = model(frame)
            frame_result = results[0].plot()  # vẽ bounding box
            out.write(frame_result)

            if first_frame is None and len(results[0].boxes) > 0:
                first_frame = frame_result.copy()

            # Thống kê đồ bảo hộ (mỗi đối tượng chỉ đếm 1 lần trong video)
            for box in results[0].boxes:
                cls_id = int(box.cls)
                cls_name = model.names[cls_id]
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                obj_key = (round((x1+x2)/2, -1), round((y1+y2)/2, -1))

                if cls_name in detected_objects and obj_key not in detected_objects[cls_name]:
                    detected_objects[cls_name].add(obj_key)
                    counts[cls_name] += 1

        cap.release()
        out.release()

        processing_placeholder.empty()
        st.success("✅ Video đã được xử lý xong!")

        if first_frame is not None:
            first_frame_rgb = cv2.cvtColor(first_frame, cv2.COLOR_BGR2RGB)
            st.subheader("📸 Ảnh nhận diện trong video")
            st.image(first_frame_rgb, use_container_width=True)

        with open('results/output_video.mp4', 'rb') as f:
            st.download_button("📥 Tải video giám sát", f, file_name="output_video.mp4")

        # =================== KHUNG 1: Thống kê đồ bảo hộ ===================
        stat1 = st.container(border=True)
        with stat1:
            st.markdown('<div class="stat1"></div>', unsafe_allow_html=True)
            st.subheader("📊 Thống kê đồ bảo hộ")

            if counts:
                df = pd.DataFrame(list(counts.items()), columns=['Đồ bảo hộ', 'Số lượng'])
                fig = px.bar(
                    df, x='Đồ bảo hộ', y='Số lượng', text='Số lượng',
                    color='Đồ bảo hộ', color_discrete_sequence=px.colors.qualitative.Bold
                )
                ymax = float(df['Số lượng'].max()) if len(df) else 1.0
                fig.update_yaxes(range=[0, ymax * 1.15], automargin=True)
                fig.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='black', size=14),
                    xaxis=dict(tickfont=dict(color='black', size=14), title_text="Đồ bảo hộ"),
                    yaxis=dict(tickfont=dict(color='black', size=14), title_text="Số lượng"),
                    margin=dict(t=80, r=40, b=40, l=40)
                )
                fig.update_traces(
                    textposition='outside',
                    textfont=dict(color='black', size=16, family='Arial'),
                    cliponaxis=False
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("❌ Không phát hiện đồ bảo hộ nào trong video.")

        # =================== KHUNG 2: Phát hiện đồ bảo hộ thiếu ===================
        stat2 = st.container(border=True)
        with stat2:
            st.markdown('<div class="stat2"></div>', unsafe_allow_html=True)
            st.subheader("⚠️ Phát hiện đồ bảo hộ thiếu")

            standard_items = ["Helmet", "Vest", "Boots"]
            missing_items = []
            for item in standard_items:
                count_detected = counts.get(item, 0)
                if count_detected == 0:
                    missing_items.append((item, 0))

            if missing_items:
                df_missing = pd.DataFrame(missing_items, columns=['Đồ bảo hộ', 'Số lượng thiếu'])
                st.table(df_missing.style.set_properties(**{'color': 'black', 'font-weight': 'bold'}))
            else:
                st.info("✅ Không phát hiện đồ bảo hộ thiếu trong video.")
