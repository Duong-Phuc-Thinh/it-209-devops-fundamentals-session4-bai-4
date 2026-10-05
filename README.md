# Bài tập 4: Quản lý tệp tin bỏ qua (.gitignore) và Sửa lịch sử (Amend)

## Giới thiệu bài tập
Bài tập này giải quyết tình huống thực tế: Người phát triển vô tình commit nhầm tệp tin chứa thông tin bảo mật (`credentials.txt`) lên Git. Mục tiêu là gỡ bỏ tệp tin này khỏi sự theo dõi (tracking) của Git mà không xóa tệp vật lý trên máy cục bộ, cấu hình để Git tự động bỏ qua tệp này trong tương lai qua `.gitignore`, và sửa đổi thông điệp commit gần nhất sạch sẽ bằng `git commit --amend`.

## Các bước thực hiện chi tiết

### Bước 1: Gỡ bỏ tệp tin khỏi Git Cache (không xóa vật lý)
Sử dụng tùy chọn `--cached` của lệnh `git rm` giúp xóa file khỏi Git index (staging area) nhưng giữ nguyên file vật lý trên đĩa cứng:
```bash
git rm --cached credentials.txt
```

### Bước 2: Cấu hình tệp tin ẩn `.gitignore`
Tạo hoặc cập nhật tệp `.gitignore` trong thư mục gốc của dự án và thêm dòng sau để ngăn Git theo dõi lại tệp này:
```text
credentials.txt
```

### Bước 3: Thêm tệp `.gitignore` vào Staging Area
```bash
git add .gitignore
```

### Bước 4: Sửa lịch sử commit gần nhất bằng `--amend`
Sử dụng lệnh `git commit --amend` để gộp thay đổi của `.gitignore` vào commit trước đó, đồng thời thay đổi thông điệp commit cũ (thông điệp lỗi) thành thông điệp mới sạch sẽ:
```bash
git commit --amend -m "Khởi tạo dự án và cấu hình bỏ qua thông tin nhạy cảm"
```

---

## Kết quả kiểm tra hiển thị

### 1. Kiểm tra trạng thái tệp tin (`git status`)
Sau khi thực hiện các bước trên, chạy lệnh:
```bash
git status
```
**Kết quả đầu ra mong đợi:**
```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```
*(Tệp `credentials.txt` không còn xuất hiện trong danh sách Git theo dõi, đồng thời không hiển thị là untracked vì đã nằm trong `.gitignore`)*

### 2. Kiểm tra lịch sử commit gần nhất (`git log -n 1`)
Để chứng minh đã sử dụng `--amend` thành công và cập nhật lại thông điệp commit:
```bash
git log -n 1
```
**Kết quả đầu ra thực tế/mong đợi:**
```text
commit d4a1b2c3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9 (HEAD -> main)
Author: Hoc Vien <hocvien@example.com>
Date:   Mon May 20 14:00:00 2024 +0700

    Khởi tạo dự án và cấu hình bỏ qua thông tin nhạy cảm
```

---

## Hướng dẫn chạy file mã nguồn hỗ trợ (`main.py`)
Chúng tôi đã cung cấp một tệp mã nguồn Python `main.py` để tự động hóa hoặc hướng dẫn trực tiếp quy trình này trên máy của bạn.

Cách chạy:
```bash
python main.py
```
Tệp tin sẽ tự động tạo file `.gitignore` thích hợp và hiển thị các bước giải quyết chi tiết một cách trực quan.
