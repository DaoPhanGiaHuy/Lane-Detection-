# Import thư viện
import cv2
import numpy as np
from moviepy.editor import VideoFileClip

def process_frame(frame):
    #Chuyển đổi hình ảnh sang thang độ xám
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Áp dụng Gaussian Blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Sử dụng Canny để phát hiện biên
    edges = cv2.Canny(blur, 50, 150)
    #Vùng quan tâm
    height, width = frame.shape[:2]
    roi_vertices = [(0, height), (width // 2, height // 2), (width, height)]
    mask_color = 255
    mask = np.zeros_like(edges)
    cv2.fillPoly(mask, np.array([roi_vertices], dtype=np.int32), mask_color)
    masked_edges = cv2.bitwise_and(edges, mask)
    #Biến đổi Hough
    lines = cv2.HoughLinesP(masked_edges, rho=6, theta=np.pi/60, threshold=160, minLineLength=40, maxLineGap=25)
    # Vẽ các đoạn thẳng lên ảnh
    line_image = np.zeros_like(frame)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 5)
    #Xếp chồng các dòng trên ảnh gốc
    final_image = cv2.addWeighted(frame, 0.8, line_image, 1, 0)
    
    return final_image

def process_video(input_path, output_path):
    clip = VideoFileClip(input_path)
    processed_clip = clip.fl_image(process_frame)
    processed_clip.write_videofile(output_path, audio=False)

# Thay đổi tên video đầu vào và tên video đầu ra ở đây
input_video_path = 'test2.mp4'
output_video_path = 'D:/daura.mp4'

# Gọi hàm xử lý video và tạo video đầu ra
process_video(input_video_path, output_video_path)

