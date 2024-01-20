# LANE DETECTION

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


