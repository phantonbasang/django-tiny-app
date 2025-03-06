# Django-Tiny-app: Blog-app To-do-list
## a. Thông tin cá nhân
Họ tên: Phan Tôn Bá Sang
Mã sinh viên: 22677351
## b. Mô tả project
Blog-app To-do-list là một ứng dụng web cho phép người dùng tạo, quản lý và theo dõi các nhiệm vụ hàng ngày một cách dễ dàng. Ý tưởng chính của dự án là xây dựng một công cụ trực quan, thân thiện với người dùng, giúp tối ưu hóa việc sắp xếp công việc. Ứng dụng tập trung vào các chức năng CRUD (Create, Read, Update, Delete) để quản lý danh sách nhiệm vụ.

### Các chức năng chính (CRUD):
**Create (Tạo mới):** <br>
Người dùng có thể thêm một nhiệm vụ mới bằng cách nhập các thông tin như:
Tên nhiệm vụ (bắt buộc).
Mô tả chi tiết (tùy chọn).
Sau khi tạo, nhiệm vụ sẽ được lưu và hiển thị trong danh sách.<br>
**Read (Đọc):** <br>
Người dùng có thể xem toàn bộ danh sách nhiệm vụ hiện có. 
Tìm kiếm các task theo các từ, cụm từ.
Mỗi nhiệm vụ hiển thị thông tin cơ bản như tên, mô tả và trạng thái.<br>
**Update (Cập nhật):** <br>
Người dùng có thể chỉnh sửa thông tin của một nhiệm vụ đã tạo, bao gồm:
Thay đổi tên, mô tả, hoặc ngày hết hạn.
Đánh dấu nhiệm vụ là "đã hoàn thành" hoặc "chưa hoàn thành".
Các thay đổi được cập nhật tức thì trong danh sách.<br>
**Delete (Xóa):** <br>
Người dùng có thể xóa bỏ các task không còn cần thiết. Khi xóa, các task được chọn sẽ bị loại bỏ hoàn toàn khỏi danh sách và cơ sở dữ liệu.<br>
## c. Hướng dẫn cài đặt và chạy
Để cài đặt và chạy ứng dụng blog-app To-do-list trên máy local, vui lòng làm theo các bước dưới đây:
### 1. Yêu cầu tiên quyết
Trước khi bắt đầu, hãy đảm bảo bạn đã cài đặt các phần mềm sau:<br>
Git: Để clone repository.<br>
Một trình soạn thảo mã như VS Code hoặc jupyter.<br>
### 2.Chạy và cài đặt
- Clone repository:
```bash
git clone https://github.com/phantonbasang/django-tiny-app.git
```
- Di chuyển vào thư mục project
```bash
cd blog-app
```
- Tạo môi trường ảo
```bash
python -m venv venv
```
- Sau đó kích hoạt môi trường ảo:
  - Trên Window:
    ```bash
    venv\Scripts\activate
    ```
  - Trên macOS/Linux:
     ```bash
    source venv/bin/activate
    ```
- Cài đặt các gói phụ thuộc:
Cài đặt các thư viện cần thiết (bao gồm Django) từ file requirements.txt (nếu có):
```bash
pip install -r requirements.txt
```
Nếu không có file ``requirements.txt``, bạn có thể cài Django thủ công:
```bash
pip install django
```
- Chạy migrations
Áp dụng các migrations để tạo cơ sở dữ liệu:
```bash
python manage.py makemigrations
python manage.py migrate
```
- (Tùy chọn) Tạo superuser
```bash
python manage.py createsuperuser
```
- Chạy ứng dụng:
```bash
python manage.py runserver
```
    
