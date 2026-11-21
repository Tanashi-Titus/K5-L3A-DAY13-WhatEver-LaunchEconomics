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

## Lê Quang Trường-2A202603663

### Phần việc phụ trách

- Vai trò **Người kiểm số**: tính tay các con số chính để đối chiếu với `src/lab13.py` (lệch cho phép ≤ 2%) và điền bảng chi phí nhiệm vụ A, B.
- Cung cấp số liệu cho CP4 (`pilot_plan.yaml`) và CP5 (`chi_so.md`); soát tỉ lệ đồng thuận trong bảng lỗi CP3.

### Đóng góp cụ thể

- Điền đầy đủ `report/team/bang_chi_phi.md`: A1 (`1,20` · `1,25` · `1,25`), A2 đủ 9 dòng (hai dòng xem lại, làm lại có nhãn simulated), A3 4 loại, A4 chi phí cố định, B1 9 kịch bản, B2 xếp hạng, B3, B4 kèm câu trả lời có số.
- Tính tay độc lập 7 con số và đối chiếu khớp 7/7 với code: `1,20`, `1,25`, tiền xem lại `1.780.000 đ`, chi phí mỗi việc thành công `4.472 đ`, cố định `1.185 đ`/việc, chi phí cả hệ thống giới hạn 2 lần `6.901.220 đ`, xem lại 100% `11.743 đ = 0,98×` [simulated].
- Soát bảng lỗi: tỉ lệ đồng thuận `19/20 = 95%`, bảng khắc phục đủ 5 loại, mỗi dòng có cách phát hiện đo được và một vai trò phụ trách.
- Hoàn thiện `report/team/pilot_plan.yaml`: chú thích D1 (a–e), D2, đánh đổi (MDE 6 điểm, power `0,64` ở +5 điểm), ngưỡng an toàn (cao hơn đối chứng ≥ 2 điểm, trần 6%; hiện tại `4,25%`), cách chia theo nhân viên 20 + 20 (`n_per_arm 859`, `DE 6,96`), 4 luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ, rollback, ngày quyết định, danh sách số simulated.
- Điền `report/team/chi_so.md`: tính thử 3 chỉ số E1 (`82,83%`, `27,12%`, `4,25%`) và 3 dòng rủi ro kinh tế E2 lấy số từ bảng độ nhạy (làm lại `+51,8%`, xem lại `+40,7%`, cố định `1.185 → 2.370 đ`/việc) [simulated].
- Viết báo cáo cá nhân tại `report/team/2A202603663_LeQuangTruong.md`.

### Bằng chứng

- Commit `a15364b` (`docs(report): điền bảng chi phí A–B, chú thích D1 và ba chỉ số E1`).
- Commit `5100ce0` (`docs(report): hoàn thiện kế hoạch pilot, rủi ro kinh tế và báo cáo cá nhân người kiểm số`).
- File: `report/team/bang_chi_phi.md` (mục "Đối chiếu của người kiểm số"), `report/team/pilot_plan.yaml`, `report/team/chi_so.md`.
- Báo cáo cá nhân: `report/team/2A202603663_LeQuangTruong.md`.

## Giáp Mạnh Tuyên-2A202603648

### Phần việc phụ trách

- Vai trò **Người gắn nhãn 2**: phân loại độc lập 20 ca lỗi ở CP3 trước khi trao đổi với người gắn nhãn 1.
- Vai trò **kiêm giữ hồ sơ**: theo dõi và cập nhật `report/team/ho_so_launch_v0.md` từ đầu buổi, tổng hợp số liệu A–E do các thành viên cung cấp.

### Đóng góp cụ thể

- Tự phân loại độc lập 20 ca lỗi và ghi lý do cho từng nhãn trong `report/team/bang_loi.md`.
- Sau khi đối chiếu hai bộ nhãn, ghi nhận đồng thuận `19/20 = 95%`; giải thích bất đồng ở ca 8 và quy tắc phân biệt giữa lỗi hệ thống đã lộ ra với lỗi ngầm chỉ phát hiện khi kiểm tra.
- Đề xuất cách khắc phục cho năm loại lỗi, kèm event, ngưỡng, tần suất phát hiện và vai trò phụ trách.
- Tổng hợp bản dự thảo 7 mục trong `report/team/ho_so_launch_v0.md` từ kết quả A–E; mục pilot còn chờ Giám đốc vận hành ký chấp nhận đánh đổi cỡ mẫu và nhóm ghi kết quả duyệt chéo.

### Bằng chứng

- `report/team/bang_loi.md`: bộ nhãn người gắn nhãn 2, phần đối chiếu 19/20 và bảng khắc phục 5 loại.
- Commit `28f6c84`: ghi bộ nhãn và phần khắc phục của người gắn nhãn 2.
- Dùng Codex hỗ trợ cấu trúc bảng và tiêu chí phát hiện; các nhãn lỗi do người gắn nhãn 2 tự quyết định độc lập.

## Đỗ Hoàng Phúc-2A202603652

### Phần việc phụ trách

- Vai trò **Người gắn nhãn 1**: đọc đề, theo dõi điều kiện "Xong khi" và kiểm tra tiêu chí chấm điểm (`RUBRIC.md`) cho các checkpoint CP1–CP5.
- Gắn nhãn độc lập 20 ca lỗi ở CP3 theo khung 5 loại của Google PAIR, đối chiếu với Người gắn nhãn 2 và hoàn thiện `report/team/bang_loi.md`.
- Cài đặt môi trường Python (`src/.venv`) trên máy cá nhân và chạy kiểm tra chéo `src/lab13.py` (xác nhận đạt 3/3 phép thử A1 và các bảng A, B, D1, E1).

### Đóng góp cụ thể

- Tự phân tích và gắn nhãn độc lập 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` vào cột `Nhãn người 1` của `report/team/bang_loi.md` (không trao đổi trước khi so nhãn).
- Đối chiếu với bộ nhãn của Người gắn nhãn 2 (`Giáp Mạnh Tuyên`): đạt tỉ lệ đồng thuận `19/20 = 95%` (vượt ngưỡng ≥ 80% của rubric).
- Thống nhất cùng nhóm nhãn cho ca không trùng duy nhất (Ca 8: `Ngầm`) và viết quy tắc phân biệt trong `report/team/bang_loi.md`.
- Rà soát các file hồ sơ nộp (`bang_chi_phi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`) theo điều kiện "Xong khi" của `CHECKPOINTS.md` và viết báo cáo cá nhân tại `report/team/2A202603652_DoHoangPhuc.md`.

### Bằng chứng

- Commit `ab5937e` (`docs(report): complete annotator 1 labels and 95% agreement in bang_loi.md`).
- Commit `2e7b08e` (`docs(report): update case 8 agreed label to Ngầm in bang_loi.md`).
- Commit `0eeff7e` (`docs(report): add personal report for Do Hoang Phuc`).
- File: `report/team/bang_loi.md`, `report/team/2A202603652_DoHoangPhuc.md`.
