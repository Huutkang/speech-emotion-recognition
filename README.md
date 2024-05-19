# **Nhận diện cảm xúc thông qua giọng nói**

## **Tổng quan**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Khả năng nhận diện cảm xúc của con người là một kỹ năng quan trọng trong giao tiếp và tương tác. Nghiên cứu này tập trung vào việc phát triển một hệ thống AI có khả năng nhận diện các cảm xúc cơ bản như vui, buồn, giận dữ, sợ hãi thông qua phân tích giọng nói. Bằng cách kết hợp các kỹ thuật AI như học máy, mạng nơ-ron..., mục tiêu là xây dựng được mô hình nhận diện cảm xúc chính xác và hiệu quả</br>
&nbsp;&nbsp;&nbsp;&nbsp;Cảm xúc được nhân diện qua ngữ âm và ngữ nghĩa. trong đề tài này, chỉ dùng ngữ âm để nhận diện.&nbsp;

### Phạm vi nghiên cứu bao gồm các nội dung chính sau:
-	Thu thập và xây dựng bộ dữ liệu giọng nói cảm xúc
-	Tiền xử lý dữ liệu giọng nói
-	Trích xuất các đặc trưng liên quan đến giọng nói
-	Phát triển mô hình AI cho nhận diện cảm xúc
-	Đánh giá hiệu suất của mô hình
-	Triển khai và ứng dụng trong thực tế
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

## Tập dữ liệu
Dữ liệu được lấy từ 4 tập dữ liệu trên Kaggle có tên là SAVEE, RAVDESS, TESS, EMOTION.
Và một tập dữ liệu do nhóm tự cắt trong phim ra. bằng phần mềm do tôi tự phát triển: 
link github: https://github.com/Huutkang/speech-emotion-labeling.git


## Các yêu cầu phụ thuộc

### Yêu cầu phiên bản python: 3.12 

### Các thư viện trong python được sử dụng gồm: 
- keras 
- librosa
- pandas
- matplotlib
- seaborn
- numpy
- scikit-learn
- pygame
- pyaudio
- noisereduce


## Các bước cài đặt:

### Bước 1:
mở một Terminal và gõ: git clone https://github.com/Huutkang/speech-emotion-recognition.git
hoặc bạn cũng có thể tải file zip và giải nén ra

### Bước 2:
Mở ứng dụng VScode hoặc các IDE có hỗ trợ python và mở đúng thư mục speech-emotion-recognition
hoặc bạn có thể mở một terminal và chuyển vị trí đứng vào trong thư mục speech-emotion-recognition

### Bước 3:
chạy file setup.py để setup thư mục làm việc và để cài đặt một số thư viện phụ thuộc.
nếu trong quá trình cài đặt các thư viện phụ thuộc mà bị lỗi thì bạn tự fix nhé. mình dùng win11 và python 3.12.3 thì không có vấn đề gì.

### Bước 4:
Sau khi cài đặt xong thư viện, tiếp tục tải data từ đường dẫn đã ghi trên phần "tập dữ liệu".
thực hiện giải nén và đưa vào thư mục data trong thu mục speech-emotion-labeling. đã có sẵn một ảnh chụp cấu trúc thư mục data.

### Bước 5:
Sau khi hoàn thành các bước trên bạn vào file main. setup các thông số cần thiết. và chạy
có một số cách setup các thông số gây ra lỗi như: tạo một mảng mà không phải hình chữ nhật. khi đó mảng không phải ma trận. và đưa vào mô hình học máy sẽ gây ra lỗi. và đó là lỗi từ bạn. không phải từ phía chúng tôi.

## Đóng góp
Chúng tôi hoan nghênh mọi đóng góp từ cộng đồng để cải thiện chất lượng và tính năng của ứng dụng.

## Liên hệ
Nếu bạn có bất kỳ câu hỏi hoặc góp ý gì thú vị về project, vui lòng liên hệ với chúng tôi theo địa chỉ email này nguyenhuuthang011@gmail.com . Xin chân thành cảm ơn!
