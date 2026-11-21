# Team

## Thông tin nhóm

- Tên nhóm: WhatEver
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-WhatEver-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/Tanashi-Titus/K5-L3A-DAY13-WhatEver-LaunchEconomics

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 |Hoàng Đăng Kiên|2A202603636|26ai.kienhd@vinuni.edu.vn|kienHD03|Người viết code|
|   2 |Giáp Mạnh Tuyên|2A202603648|26ai.tuyengm@vinuni.edu.vn|Tanashi-Titus|Người gắn nhãn 2|
|   3 |Lê Quang Trường|2A202603663|26ai.truonglq@vinuni.edu.vn|Letruong238|Người kiểm số|
|   4 |Đỗ Hoàng Phúc|2A202603652|26ai.phucdh@vinuni.edu.vn|Codeforlife-MagicWed|Người gắn nhãn 1|

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## Hoàng Đăng Kiên-2A202603636

### Phần việc phụ trách

- Vai trò **Người viết code**: thiết lập môi trường Python (`src/.venv`), viết và chạy `src/lab13.py` cho toàn bộ phần tính toán định lượng của CP1 (A1–A4), CP2 (B1–B4), CP4 (D1, D3) và CP5 (E1).
- Bàn giao số liệu in ra từ `src/lab13.py` cho Người kiểm số đối chiếu tay và hỗ trợ kiểm tra kỹ thuật các file hồ sơ nộp bài.

### Đóng góp cụ thể

- Hoàn thiện `src/lab13.py`: cài đặt 3 hàm A1 đạt 3/3 phép thử đáp án biết trước (`1,20` · `1,25` · `1,25`); viết hàm `mo_hinh(...)` tính chi phí mỗi việc thành công từ trace (`4.472 đ` [simulated], gấp `16,3×` hoá đơn `274,7 đ`/yc), tách 4 loại yêu cầu kèm tỉ lệ `ok` theo lần thử, và tính chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` (`4.599 đ` ở 45.000 yc/tháng và `5.784 đ` ở nửa khối lượng) [simulated].
- Viết phần độ nhạy CP2 (B1–B4): 9 kịch bản đổi từng yếu tố qua kiểm tra tuyến tính, đổi cặp + xếp hạng top 3 yếu tố nhạy nhất (`Làm lại`, `Xem lại`, `Lương`), chi phí cả hệ thống theo giới hạn 1–3 lần chạy (`2 lần` rẻ nhất: `6.901.220 đ` [simulated]), và kịch bản xem lại 100% (`11.743 đ` với 9 phút làm lại và `12.415 đ` theo trung bình dữ liệu 15,3 phút [simulated]).
- Viết phần cỡ mẫu D1 (`1.251`, `DE = 2,48`, trần cụm `1.000` / `300`, MDE +6 điểm `859` cần `m ≥ 299` với `DE = 6,96`, power ở +5 điểm `0,64`), tỉ lệ `mo_lai_trong_7_ngay` hiện tại (`4,25%` toàn mẫu, `3,97%` trong phạm vi pilot) và 3 chỉ số chạy thử E1 (`82,83%`, `27,12%`, `4,25%`).
- Viết báo cáo cá nhân tại `report/team/2A202603636_HoangDangKien.md`.

### Bằng chứng

- Commit `7d6f945` (`feat(lab13): implement cost model, sensitivity, sample size and trial metrics`).
- File code: `src/lab13.py` (chạy đạt 3/3 phép thử A1 và kiểm tra tuyến tính B1).
- Đối chiếu khớp 7/7 con số với phần tính tay của Người kiểm số trong `report/team/bang_chi_phi.md` (commit `a15364b`).
- Báo cáo cá nhân: `report/team/2A202603636_HoangDangKien.md`.

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-
