# django-tiny-app $\rightarrow$ Ứng dụng quản lý chi tiêu cá nhân
## a. Thông tin cá nhân
- **Tên**: Phan Tôn Bá Sang <br>
- **MSSV**: 22677351<br>
## b. Mô tả Project
Project này là xây dựng 1 ứng dụng web đơn giản giúp cho người dùng có thể quản lý chi tiêu cá nhân của mình hằng ngày 1 cách hiệu quả. Ứng dụng có các chức năng chính:
### 1. **Đăng ký/Đăng nhập**
- Người dùng có thể tạo tài khoản mới bằng cách đăng ký với các thông tin cá nhân như: (tên, email, mật khẩu).
- Người dùng đã có tài khoản có thể đăng nhập vào hệ thống.

### 2. **Thêm chi tiêu**
- Người dùng có thể thêm các khoản chi tiêu với các thông tin như:
  - **Số tiền**: Số tiền đã chi tiêu.
  - **Danh mục**: Danh mục chi tiêu (ví dụ: ăn uống, mua sắm, giải trí, v.v.).
  - **Ngày tháng**: Ngày thực hiện chi tiêu.
  - **Ghi chú**: Mô tả ngắn gọn về khoản chi tiêu.

### 3. **Xem lịch sử chi tiêu**
- Người dùng có thể xem danh sách các khoản chi tiêu đã được thêm vào.
- Danh sách chi tiêu được hiển thị theo thứ tự thời gian (mới nhất lên đầu).

### 4. **Sửa chi tiêu**
- Người dùng có thể chỉnh sửa thông tin của các khoản chi tiêu đã thêm:
  - Thay đổi số tiền, danh mục, ngày tháng hoặc ghi chú.
  - Lưu lại thay đổi sau khi chỉnh sửa.

### 5. **Xóa chi tiêu**
- Người dùng có thể xóa các khoản chi tiêu không cần thiết.
- Hỗ trợ xóa nhiều khoản chi tiêu cùng lúc.

### 6. **Phân tích chi tiêu**
- Thống kê chi tiêu theo danh mục (ví dụ: tổng chi tiêu cho ăn uống, mua sắm, v.v.).
- Hiển thị biểu đồ hoặc báo cáo chi tiêu theo tuần/tháng/năm.

### 7. **Phân trang**
- Danh sách chi tiêu được chia thành các trang, mỗi trang hiển thị tối đa 10 khoản chi tiêu.
- Người dùng có thể chuyển đổi giữa các trang để xem thêm chi tiêu.

### 8. **Trang admin**
- Quản trị viên có thể quản lý người dùng:
  - **Khóa tài khoản**: Ngăn người dùng đăng nhập nếu vi phạm quy định.
  - **Reset mật khẩu**: Hỗ trợ người dùng quên mật khẩu.
- Hiển thị thông báo khi tài khoản bị khóa.

## c. Hướng dẫn cài đặt, chạy
### Các bước cài đặt
1. **Clone repository**:
```bash
   git clone https://github.com/your-username/django-tiny-app.git
```
2. **Di chuyển vào thư mục Project

```bash
    cd django-tiny-app
```
## d. Link Project đã triển khai của bạn


