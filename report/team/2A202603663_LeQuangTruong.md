# Báo cáo cá nhân — LeQuangTruong-2A202603663

## 1. Thông tin thành viên

- Họ tên: Lê Quang Trường
- MSSV: 2A202603663
- Email:26ai.truonglq@vinuni.edu.vn
- GitHub: Letruong238
- Vai trong nhóm: Người kiểm số

## 2. Phần việc phụ trách

- Tính tay một số con số chính để đối chiếu với kết quả của `src/lab13.py` (lệch cho phép ≤ 2%).
- Điền bảng chi phí nhiệm vụ A và B trong `report/team/bang_chi_phi.md`.
- Cung cấp số liệu cho nhiệm vụ D (chú thích D1, tỉ lệ mở lại, kế hoạch pilot) và nhiệm vụ E (ba chỉ số, rủi ro kinh tế).
- Soát lại tỉ lệ đồng thuận trong bảng lỗi của hai người gắn nhãn.

## 3. Đóng góp cụ thể

- **Nhiệm vụ A, B (`bang_chi_phi.md`):** điền đủ bảng A1 (3 phép thử ĐẠT: 1,20 · 1,25 · 1,25), A2 (9 dòng, hai dòng xem lại và làm lại ghi nhãn simulated), A3 (4 loại yêu cầu), A4 (chi phí cố định), B1 (9 kịch bản), B2 (cặp yếu tố và xếp hạng), B3, B4; viết câu trả lời ngắn có số cho từng phần.
- **Đối chiếu tay:** tính tay độc lập 7 con số và so với code, tất cả khớp:
  - A1: (1 − 0,2²) / 0,8 = 1,20; hệ số tối đa 3 lần = 1 / 0,8 = 1,25.
  - A2: tiền xem lại 890 phút × 2.000 đ = 1.780.000 đ; chi phí mỗi việc thành công 4.373.585 / 978 = 4.472 đ [simulated].
  - A4: 40.000.000 / (45.000 × 900 / 1.200) = 1.185 đ mỗi việc.
  - B3: chi phí cả hệ thống với giới hạn 2 lần = 4.093.220 + 234 × 12.000 = 6.901.220 đ [simulated].
  - B4: (9.480.000 + 864.000 + 224.513) / 900 = 11.743 đ = 0,98× của 12.000 đ [simulated].
- **Nhiệm vụ C (`bang_loi.md`):** soát lại tỉ lệ đồng thuận 19/20 = 95% (đạt ≥ 80%); kiểm tra bảng khắc phục đủ năm loại, mỗi dòng có cách phát hiện đo được và một vai trò phụ trách.
- **Nhiệm vụ D (`pilot_plan.yaml`):** điền chú thích D1 (a–e), tỉ lệ `mo_lai_trong_7_ngay` hiện tại 4,25% (51/1.200), chọn cách chia theo nhân viên 20 + 20 với mức chênh 6 điểm (859 mẫu hiệu dụng mỗi nhóm, DE 6,96), viết D2, đánh đổi (power 0,64 nếu tác động thật chỉ 5 điểm), 4 luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ, rollback, ngày quyết định và danh sách số simulated. File đọc được bằng `yaml.safe_load`, không còn dấu `?`.
- **Nhiệm vụ E (`chi_so.md`):** tính thử ba chỉ số: chính 82,83% (994/1.200), dùng 27,12% (48/177), an toàn 4,25% (51/1.200); viết 3 dòng rủi ro kinh tế lấy số từ bảng độ nhạy (làm lại +51,8%, xem lại +40,7%, chi phí cố định 1.185 → 2.370 đ/việc) [simulated].

## 4. Bằng chứng

- Commit `a15364b` — `docs(report): điền bảng chi phí A–B, chú thích D1 và ba chỉ số E1`.
- File: `report/team/bang_chi_phi.md` (mục "Đối chiếu của người kiểm số" ở cuối file), `report/team/pilot_plan.yaml`, `report/team/chi_so.md` (bảng E1 và E2).
- Con số chính: chi phí mỗi việc thành công 4.472 đ, gấp 16,3 lần hoá đơn token chia số yêu cầu; so với nhân viên tự làm 0,49× (cả hệ thống) và 0,38× trong phạm vi pilot đã cộng cố định [simulated].

## 5. Công cụ AI đã dùng

- **Claude (Claude Code trong VS Code):** dùng để đọc đề và xác định phần việc của vai người kiểm số, chạy `src/lab13.py`, điền số vào các bảng hồ sơ và gợi ý cách viết kế hoạch pilot.
- **Cách tự kiểm tra:**
  - Tính tay lại 7 con số (ghi ở mục 3) và so với số code in ra: tất cả khớp.
  - So mọi số trong bảng với "số để tự đối chiếu" trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`: lệch dưới 2%.
  - Kiểm tra quy tắc tuyến tính của bảng độ nhạy: kịch bản giảm một nửa luôn bằng −½ kịch bản gấp đôi (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9).
  - Chạy `yaml.safe_load` cho `pilot_plan.yaml` và kiểm tra không còn dấu `?`, không có từ cấm trong hồ sơ.
- Không dùng AI để bịa số, nhãn lỗi hay kết quả duyệt chéo: mọi số lấy từ `src/lab13.py` hoặc tính tay có ghi cách tính.

## 6. Tự đánh giá

- **Làm tốt:** các bảng A, B đủ dòng và khớp đáp án; có phần đối chiếu tay ghi rõ cách tính; các số giả lập đều gắn nhãn simulated.
- **Hiểu được:** vì sao tử số tính mọi lần chạy kể cả lần lỗi còn mẫu số chỉ đếm 978 việc thành công; vì sao số ca làm lại là yếu tố nhạy nhất chứ không phải giá token; vì sao chia theo nhân viên cần chấp nhận mức chênh 6 điểm.
- **Cần cải thiện:** dựa vào trợ lý AI khá nhiều cho phần viết kế hoạch pilot; lần sau cần tự viết nháp luật dừng trước rồi mới nhờ soát.
