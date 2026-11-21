# Báo cáo cá nhân — HoVaTen-MSSV

Copy file này và đổi tên theo quy tắc `MSSV_HoTen.md`. Giữ nguyên file mẫu.

Ví dụ: `20241234_NguyenVanAn.md`.

## 1. Thông tin thành viên

- Họ tên: Hoàng Đăng Kiên
- MSSV: 2A202603636
- Email: 26ai.kienhd@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): người viết code

## 2. Phần việc phụ trách

- Thiết lập môi trường Python (`src/.venv`) từ `src/requirements.txt` và đảm bảo đọc dữ liệu `src/logix_requests.csv` đúng quy ước (`keep_default_na=False`), không chỉnh sửa `src/lab13_starter.py` hay hai file CSV gốc.
- Viết và chạy `src/lab13.py` cho các phần tính toán định lượng của nhóm:
  - **CP1 (Nhiệm vụ A1–A4):** 3 hàm kinh tế chạy lại, hàm `mo_hinh(...)` tính chi phí mỗi việc thành công từ trace, tách theo 4 loại yêu cầu kèm tỉ lệ `ok` theo lần thử, và tính chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang`.
  - **CP2 (Nhiệm vụ B1–B4):** bảng độ nhạy 9 kịch bản, kịch bản đổi cặp & xếp hạng top 3 yếu tố nhạy nhất, chi phí cả hệ thống theo giới hạn 1–3 lần chạy, và kịch bản xem lại 100%.
  - **CP4 (Nhiệm vụ D1, D3) & CP5 (Nhiệm vụ E1):** tính cỡ mẫu theo 3 cách chia (dùng công thức chuẩn z và `statsmodels`), tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại và 3 chỉ số chạy thử trên 1.200 yêu cầu.
- Phối hợp bàn giao kết quả in ra cho **Người kiểm số** đối chiếu tay và cho nhóm điền các file hồ sơ trong `report/team/`.

## 3. Đóng góp cụ thể

- Hoàn thiện toàn bộ phần cài đặt và code tính toán trong `src/lab13.py` chạy thông suốt từ đầu đến cuối:
  - **A1:** Cài đặt `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`, vượt qua 3/3 phép thử đáp án biết trước (`1,20` · `1,25` · `1,25` → `ĐẠT`).
  - **A2–A4:** Cài đặt `mo_hinh(...)` cộng mọi lần chạy (kể cả lỗi) ở tử số và chỉ chia cho số yêu cầu `ket_qua == 'thanh_cong'` ở mẫu số; tính ra CPS = `4.472 đ` [simulated] (gấp `16,3×` hoá đơn `274,7 đ`/yêu cầu), chi phí cả hệ thống `5.865 đ`/yêu cầu (`0,49×` của `12.000 đ`) [simulated], phân tách 4 loại (`quoc_te` = `22.515 đ` = `1,88×` [simulated] với tỉ lệ `ok` giảm từ `30,0%` → `11,4%` → `2,2%`), và cộng chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` (`4.599 đ` = `0,38×` ở 45.000 yc/tháng và `5.784 đ` = `0,48×` ở nửa khối lượng) [simulated].
  - **B1–B4:** Tái sử dụng `mo_hinh(...)` cho 9 kịch bản độ nhạy (xác nhận top 3 yếu tố nhạy nhất là số ca làm lại `+51,8%`, tỉ lệ xem lại `+40,7%`, lương nhân viên `+23,1%` [simulated]), chỉ ra giới hạn 2 lần chạy rẻ nhất cho toàn hệ thống (`6.901.220 đ` [simulated]) thay vì 1 lần chạy (`4.111 đ`/việc nhưng đẩy thêm 85 ca sang nhân viên), và tính kịch bản xem lại 100% (`11.743 đ` = `0,98×` với 9 phút làm lại và `12.415 đ` = `1,03×` theo trung bình dữ liệu 15,3 phút [simulated]).
  - **D1, D3 & E1:** Tính đủ 5 câu cỡ mẫu D1 (`1.251` yc/nhóm; `DE = 2,48` → 42 NV/nhóm; trần cụm `1.000` với 20 NV và `300` với 6 depot; MDE +6 điểm cần `859` yc/nhóm hay `m ≥ 299` yc/NV với `DE = 6,96`, power ở mức +5 điểm còn `0,64`), tỉ lệ mở lại hiện tại `4,25%` (`3,97%` trong phạm vi pilot), và 3 chỉ số trong đợt chạy thử (chỉ số chính `82,83%`, tỉ lệ bỏ qua gợi ý `27,12%`, an toàn `4,25%`).
- Rà soát tiến độ và checklist kỹ thuật của repo (kiểm tra cú pháp YAML, dấu `?` còn sót trong `pilot_plan.yaml`, và kiểm tra không dùng từ cấm trong `report/team/`).

## 4. Bằng chứng

- **Commit:** `7d6f945` — `feat(lab13): implement cost model, sensitivity, sample size and trial metrics`
- **File code:** `src/lab13.py` (không sửa `src/lab13_starter.py`, `src/logix_runs.csv`, `src/logix_requests.csv`).
- **Kết quả kiểm chứng chéo với Người kiểm số:** Khớp 7/7 con số tính tay trong mục *"Đối chiếu của người kiểm số"* ở `report/team/bang_chi_phi.md` (commit `a15364b`), gồm: `1,20`, `1,25`, tiền xem lại `1.780.000 đ` [simulated], CPS `4.472 đ` [simulated], cố định `1.185 đ`/việc, cả hệ thống giới hạn 2 lần `6.901.220 đ` [simulated], và xem lại 100% `11.743 đ` [simulated].

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity (trợ lý AI dùng mô hình Gemini).
- **Mục đích sử dụng:** Rà soát phân vai trong `TEAM.md` và `CHECKPOINTS.md`, gợi ý cấu trúc hàm và cách định dạng bảng in ra trong `src/lab13.py`, hỗ trợ kiểm tra chéo điều kiện nộp bài theo `SUBMISSION.md`. Không dùng AI để bịa số liệu hay gắn nhãn lỗi thay nhóm.
- **Tự kiểm tra:**
  - Tự chạy trực tiếp `src/.venv/Scripts/python.exe lab13.py` trong thư mục `src/` để xác nhận code vượt qua 3/3 phép thử bắt buộc ở A1 (`Ba phép thử đáp án biết trước: ĐẠT`) và không phát sinh lỗi khi đọc `logix_requests.csv` với `keep_default_na=False`.
  - Tự kiểm tra tính tuyến tính của bảng độ nhạy B1 bằng điều kiện đối chiếu ngay trong code (mỗi kịch bản giảm một nửa có mức giảm bằng đúng −½ mức tăng của kịch bản gấp đôi: `ĐẠT`).
  - Tự đối chiếu toàn bộ số đầu ra với công thức gốc trong `docs/du_lieu_va_cong_thuc.md` và bảng tính tay độc lập của Người kiểm số ở `report/team/bang_chi_phi.md` (khớp 7/7 con số, độ lệch 0%).
  - Đã rà lại và nắm rõ 3 cơ chế cốt lõi để tự giải thích khi bảo vệ: vì sao tử số tính mọi lần chạy kể cả lần lỗi còn mẫu số chỉ đếm `thanh_cong`; công thức hệ số thiết kế `DE = 1 + (m − 1) × ICC` và trần cỡ mẫu hiệu dụng `c / ICC`; và đánh đổi giữa tối ưu chi phí mỗi việc thành công với chi phí cả hệ thống.

## 6. Tự đánh giá

- **Điểm làm tốt:** Hoàn thành sớm và gọn phần code đúng phạm vi vai **Người viết code**, cấu trúc hàm rõ ràng để tái sử dụng xuyên suốt A–B–D–E, gắn nhãn `simulated` đầy đủ trên mọi con số giả lập và kiểm chứng khớp 100% với phần tính tay của Người kiểm số.
- **Điểm cần cải thiện / tiếp tục hoàn thiện:** Cần đảm bảo một thành viên khác chạy xác nhận lại `src/lab13.py` trên máy thứ 2, và phối hợp chặt với nhóm hoàn thiện nốt `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md` trước mốc duyệt chéo.
