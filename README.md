## Chú thích
  1. Để có thể sử dụng được update, trước tiên bạn phải huấn luyện mô hình (train).
  2. Tập tin label.csv có giá trị "0" vì lúc bạn chưa huấn luyện mô hình thì chưa có ID nào được lưu vào.
  3. data_name.csv có giá trị ở vị trí [0] là NoName vì khi đối chiếu với ID trong mô hình LBP ID bắt đầu từ 1, 2, 3 ..... ứng với ID là tên ở vị trí của người đó.
  
## Máy dò khuôn mặt với Dlib
Dlib sử dụng Thuật toán HOG là bộ mô tả tính năng được sử dụng rộng rãi trong thị giác máy tính, xử lý hình ảnh với mục đích dùng để phát hiện đối tượng.
Phương pháp HOG dựa trên việc đếm số lần xuất hiện của các hướng đạo hàm (gradient orientation) trong các vùng cục bộ của ảnh.

Để có thể phát hiện khuôn mặt với dlib ta thực hiện các bước sau:

Bước 1: Xử dụng OpenCV2 đọc ảnh và chuyển ảnh về mạng màu xám

Bước 2: Khởi tạo máy dò khuôn mặt dlib.get_frontal_face_detector()

Bước 3: Sau khi cho hình ảnh vào máy dò khuôn mặt ta sẽ được 1 biến faces lưu chữ 4 biến rectangle(x1, y1, x2, y2)

Chú thích:

x1: là tọa độ bên trái của khuôn mặt nằm trong tấm hình

y1: là tọa độ bên trên của khuôn mặt nằm trong tấm hình

x2: là tọa độ bên phải của khuôn mặt nằm trong tấm hình

y2: là tọa độ bên dưới của khuôn mặt nằm trong tấm hình

## Chuẩn bị dữ liệu để huấn luyện mô hình
Để có thể huấn luyện được mô hình ta cần một tập dữ liệu hình ảnh. Mỗi file là một ID bên trong file sẽ là hình ảnh của người cần huấn luyện, với mỗi người sẽ có 1 ID riêng.
Cách tốt nhất cho việc chuẩn bị là nên chọn hình ảnh chỉ có một người trong ảnh tránh việc máy dò tìm loại bỏ đi ảnh khi phát hiện có 2 người trong ảnh.

Sau khi có tập dữ liệu chúng ta sẽ sử dụng máy dò khuôn mặt để lấy được vị trí của khuôn mặt nằm trong tấm hình và lưu nó vào 1 mảng kèm theo ID của thư mục ảnh.

## Huấn luyện mô hình
LBP là một toán tử có kết cấu đơn giản nhưng rất hiệu quả, nó gắn nhãn các pixel của hình ảnh bằng các ngưỡng vùng lân cận của mỗi pixel và coi kết quả là một số nhị phân.

Thuật toán LBP rút trích đặc trưng hình ảnh, bằng cách so sánh giá trị của một pixel với các pixel khác bao quanh nó. 
Để xây dựng được LBP trước tiên phải chuyển hình ảnh đầu vào về dạng grayscale, với mỗi pixel chúng ta chọn ra vùng lân cận bao quanh pixel trung tâm và mô hình có kích thước là
3x3 pixel

Sau khi có 2 mảng gổm 1 mảng lưu mảng giá trị hình ảnh chứa khuôn mặt và 1 mảng lưu id của ảnh thì chúng ta bắt đầu việc huấn luyện mô hình với các bước sau:

Bước 1: Khởi tạo mô hình huấn luyện với câu lệnh recognizer = cv2.face.LBPHFaceRecognizer_create()

Bước 2: Truyền 2 tham số bên trên vào để huấn luyện cognizer.train(faces, numpy.array(labels)), lưu ý chuyển mảng chứa giá trị tham số về mảng numpy.array

Bước 3: Lưu mô hình vào file có tên với đuôi là .yml recognizer.save('training.yml')

Bước 4: Lưu ID vào file labels.csv để giúp cho việc cập nhật mô hình.

## Cập nhật mô hình
Cập nhật mô hình là thư viện có sẳn bên trong LBP, để có thể sử dụng được bạn chỉ cần so sánh id của những file bạn mới tải vào thư mục anh data với những id đã được
train trước đó và lưu trong file labels.csv.

Các bước thực hiện việc cập nhật mô hình:

Bước 1: Khởi tạo mô hình huấn luyện với câu lệnh recognizer = cv2.face.LBPHFaceRecognizer_create().

Bước 2: Đọc file mô hình đã được lưu sau khi huấn luyện recognizer.read('training.yml').

Bước 3: Truyền 2 tham số bên trên vào để huấn luyện cognizer.update(faces, numpy.array(labels)), lưu ý chuyển mảng chứa giá trị tham số về mảng numpy.array
Các tham số hình ảnh cũng như id đã được xử lý so sánh trước khi được lưu vào 2 mảng, nếu trùng đã bị loại bỏ.

Bước 4: Lưu mô hình vừa cập nhật vào đúng file mô hình đã huấn luyện recognizer.save('training.yml')


  
  
