# LANE DETECTION

## Giới Thiệu

Dự án này tập trung vào việc phát hiện và theo dõi làn đường trong hình ảnh hoặc video sử dụng các thuật toán xử lý ảnh và máy học. Mục tiêu của dự án là cung cấp một giải pháp thông minh để nhận diện cấu trúc đường và hỗ trợ các ứng dụng liên quan đến giao thông và lái xe tự động.

## Ứng Dụng Trong Đời Sống

### 1. Hệ Thống Làm Chủ Giao Thông
- Giám sát và quản lý luồng giao thông trên các tuyến đường.
- Tối ưu hóa đèn giao thông và dòng chảy của phương tiện.

### 2. Hỗ Trợ Hành Trình và Bảo Dưỡng Xe
- Cung cấp thông tin về vị trí và tình trạng của làn đường.
- Tối ưu hóa hành trình và bảo dưỡng hệ thống lái.

### 3. An Toàn Xe Tự Lái
- Phát hiện và theo dõi làn đường để đảm bảo an toàn cho hành khách và người tham gia giao thông.
- Hỗ trợ chức năng lái tự động và tăng cường khả năng đánh lái an toàn.

### 4. Hệ Thống Cảnh Báo Lái Xe
- Cảnh báo lái xe về sự thay đổi đột ngột trong làn đường hoặc tiếp xúc không an toàn với các phương tiện khác.

### 5. Nghiên Cứu và Phát Triển Xe Tương Lai
- Hỗ trợ nghiên cứu và phát triển các công nghệ xe tự lái và ứng dụng thị giác máy tính trong lĩnh vực ô tô.

## Mô tả quy trình :

![Đường](dexuat.png)

---
**Lưu ý:** Đây là một mô tả tổng quan và có thể được mở rộng thêm theo yêu cầu và cụ thể của dự án.


<pre>
import cv2
import numpy as np
from moviepy.editor import VideoFileClip
</pre>

## I. Import các thư viện :
    Giải thích mỗi dòng mã:

1. **Import thư viện OpenCV:**
   ```python
   import cv2
Dòng này thực hiện việc import thư viện OpenCV (Open Source Computer Vision). OpenCV là một thư viện mã nguồn mở cung cấp các công cụ và thuật toán cho xử lý ảnh và thị giác máy tính.

2. **Import thư viện  NumPy:**
   ```python
   import numpy as np
Thực hiện việc import thư viện NumPy, một thư viện Python chuyên về tính toán số học và thực hiện các phép toán trên mảng nhiều chiều. NumPy thường được sử dụng trong xử lý dữ liệu số và thị giác máy tính.

3. **Import lớp VideoFileClip từ thư viện MoviePy:**
   ```python
   from moviepy.editor import VideoFileClip
Thực hiện việc import lớp VideoFileClip từ thư viện MoviePy. MoviePy là một thư viện được sử dụng để làm việc với video trong Python. Lớp VideoFileClip được sử dụng để tạo một đối tượng video từ một tệp video có sẵn để sau đó có thể thực hiện các xử lý và chỉnh sửa trên video đó.

## II. Hàm xử lý ảnh và thuật toán :
Ta lấy ví dụ là ảnh sau:

![Đường](road7.jpg)

    Giải thích mỗi dòng mã:
1. **Chuyển đổi hình ảnh sang ảnh xám:**
   ```python
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
Dòng mã gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) sử dụng hàm cvtColor của thư viện OpenCV để chuyển đổi một hình ảnh màu từ không gian màu BGR (Blue-Green-Red) sang không gian màu độ xám.

frame: Là hình ảnh ban đầu, được giả định là ở định dạng màu BGR.

cv2.COLOR_BGR2GRAY: Là hằng số cho biết hàm cvtColor sẽ thực hiện chuyển đổi sang không gian màu độ xám. Trong trường hợp này, cv2.COLOR_BGR2GRAY chỉ định rằng hình ảnh đầu vào sẽ được chuyển đổi thành hình ảnh độ xám.

Hàm cvtColor sẽ thực hiện việc tính toán trung bình có trọng số của các giá trị màu BGR để tạo ra giá trị màu độ xám tương ứng. Kết quả của dòng mã này là một hình ảnh độ xám, giảm chiều sâu màu của hình ảnh. Điều này thường được thực hiện để đơn giản hóa việc xử lý ảnh và giảm độ phức tạp của dữ liệu.







   




