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
Sơ đồ các bước.
1. Import Libraries (Nhập thư viện): Bước này bắt đầu bằng việc nhập các thư viện và công cụ
cần thiết cho quy trình, ví dụ: OpenCV để xử lý hình ảnh và numpy để làm việc với mảng
dữ liệu.

2. Read the Image (Đọc Ảnh): Bạn đọc ảnh đầu vào (thường là ảnh từ camera hoặc video)
bằng OpenCV để tiếp tục xử lý.

3. Convert Image to Grayscale (Chuyển ảnh thành ảnh xám): Chuyển ảnh màu (ảnh RGB)
sang ảnh xám (grayscale) để giảm chi phí tính toán và tập trung vào việc phát hiện cạnh.

4. Apply Gaussian Blur (Áp dụng làm mờ Gaussian): Để giảm nhiễu và làm cho việc phát hiện
cạnh dễ dàng hơn, bạn áp dụng làm mờ Gaussian lên ảnh xám.

5. Detect Edge Using Canny (Phát hiện biên bằng Canny): Sử dụng thuật toán Canny để phát
hiện biên trong ảnh, tạo ra ảnh biên (edges) trong đó các cạnh của đối tượng được sáng lên.

6. Region of Interest (Vùng quan tâm): Bạn xác định một vùng quan tâm (Region of Interest -
ROI) trên ảnh. Vùng này thường là khu vực mà bạn mong muốn phát hiện làn đường. Các
điểm nằm ngoài ROI sẽ bị loại bỏ khỏi quá trình phát hiện.

7. Hough Transform (Biến đổi Hough): Áp dụng biến đổi Hough lên ảnh biên để tìm các đường
thẳng trong ảnh. Biến đổi Hough giúp chúng ta xác định các đường thẳng trong không gian
rho (fi) và theta (fi).

8. Draw Lines on the Image (Vẽ đường trên ảnh): Bước này dựa trên kết quả của biến đổi
Hough, chúng ta có thể tìm ra các đường thẳng trong ảnh.

9. Overlaying the Lines on the Original Image (Đè các đường lên ảnh gốc): Sau khi tìm được
các đường, chúng ta đè chúng lên ảnh gốc để hiển thị các đường đó trên hình ảnh thực tế.

10. Display Result (Hiển thị kết quả): Cuối cùng, bạn hiển thị ảnh đã xử lý với các đường làn
đã được phát hiện, thường là để theo dõi, kiểm tra hoặc làm video demo của quá trình phát
hiện làn đường.

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
Đầu tiên, chúng ta sẽ đọc hình ảnh mà chúng ta muốn phát hiện làn đường. Chúng ta sẽ sử dụng imread()chức năng của OpenCV để đọc hình ảnh.
```python
# Đọc ảnh đầu vào
image = cv2.imread('road7.jpg')
# Hiển thị ảnh
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Input Image')
plt.show()
```
    
1. **Chuyển đổi hình ảnh sang ảnh xám:**
   ```python
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
Dòng mã gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) sử dụng hàm cvtColor của thư viện OpenCV để chuyển đổi một hình ảnh màu từ không gian màu BGR (Blue-Green-Red) sang không gian màu độ xám.

frame: Là hình ảnh ban đầu, được giả định là ở định dạng màu BGR.

cv2.COLOR_BGR2GRAY: Là hằng số cho biết hàm cvtColor sẽ thực hiện chuyển đổi sang không gian màu độ xám. Trong trường hợp này, cv2.COLOR_BGR2GRAY chỉ định rằng hình ảnh đầu vào sẽ được chuyển đổi thành hình ảnh độ xám.

Hàm cvtColor sẽ thực hiện việc tính toán trung bình có trọng số của các giá trị màu BGR để tạo ra giá trị màu độ xám tương ứng. Kết quả của dòng mã này là một hình ảnh độ xám, giảm chiều sâu màu của hình ảnh. Điều này thường được thực hiện để đơn giản hóa việc xử lý ảnh và giảm độ phức tạp của dữ liệu.

2. **Làm mờ ảnh xám:**
   ```python
   blur = cv2.GaussianBlur(gray, (5, 5), 0)
Dòng mã blur = cv2.GaussianBlur(gray, (5, 5), 0) sử dụng hàm GaussianBlur từ thư viện OpenCV để áp dụng bộ lọc Gaussian (lọc Gauss) cho một hình ảnh xám.

Giải thích từng tham số:

gray: Là hình ảnh đầu vào đã được chuyển đổi sang thang độ xám (độ sáng).

(5, 5): Là kích thước của kernel (bộ lọc) Gaussian, được xác định bởi chiều rộng và chiều cao của kernel. Trong trường hợp này, kernel là một ma trận vuông kích thước 5x5. Kích thước của kernel ảnh hưởng đến độ mờ của hình ảnh sau khi áp dụng bộ lọc Gaussian. Kernel lớn hơn sẽ tạo ra hiệu ứng làm mờ lớn hơn.

0: Là độ lệch chuẩn (standard deviation) của Gaussian. Trong trường hợp này, giá trị 0 chỉ định rằng OpenCV sẽ tự động xác định độ lệch chuẩn dựa trên kích thước của kernel. Đối với nhiều trường hợp, việc sử dụng giá trị 0 là lựa chọn phổ biến vì nó tự động tính toán độ lệch chuẩn phù hợp.

Mục đích của dòng code:

Dòng này thực hiện việc áp dụng bộ lọc Gaussian để làm mờ hình ảnh xám. Bộ lọc Gaussian giúp giảm nhiễu trong hình ảnh và làm mờ các chi tiết không mong muốn. Việc này thường được thực hiện để chuẩn bị cho các bước xử lý tiếp theo trong quá trình xử lý ảnh, như việc phát hiện biên bằng Canny hay phát hiện đường bằng Hough.







   




