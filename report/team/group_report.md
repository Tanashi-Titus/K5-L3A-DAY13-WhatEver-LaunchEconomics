# Báo cáo nhóm · WhatEver

## 1. Thông tin nhóm

- Lớp: L3A. Thành viên và phân vai: xem `TEAM.md`.
- Repo nhóm: [K5-L3A-DAY13-WhatEver-LaunchEconomics](https://github.com/Tanashi-Titus/K5-L3A-DAY13-WhatEver-LaunchEconomics).

## 2. Mục tiêu và cách tiếp cận

Nhóm đánh giá kinh tế của trợ lý hoàn phí LogiX-VN và đề xuất thiết kế pilot Gate 2a. Nhóm dùng mẫu giả lập gồm 1.200 yêu cầu và 1.624 lần chạy, tính cả chi phí token, tool, thời gian xem lại/làm lại và chi phí chuyển nhân viên. Kết quả chạy thử được mô tả như số liệu trong mẫu; do chưa có nhóm đối chứng trong dữ liệu hồi cứu, nhóm không kết luận trợ lý đã gây ra mức tăng chỉ số.

## 3. Giải pháp

- **A–B:** `src/lab13.py` tính chi phí thành công, tách theo loại yêu cầu, chi phí cố định và 9 kịch bản độ nhạy; các bảng và đối chiếu tay nằm trong `bang_chi_phi.md`.
- **C:** Hai người gắn nhãn làm độc lập; đạt đồng thuận 19/20 ca (95%). `bang_loi.md` ghi quy tắc xử lý ca 8 và cách phát hiện/khắc phục cho 5 loại lỗi.
- **D:** `pilot_plan.yaml` đề xuất chia ngẫu nhiên theo nhân viên 20/20, MDE 6 điểm, 859 mẫu hiệu dụng mỗi nhóm (tương ứng 299 yêu cầu mỗi nhân viên). Kế hoạch có luật dừng an toàn, chi phí và sử dụng; chờ Giám đốc vận hành ký chấp nhận đánh đổi cỡ mẫu.
- **E:** `chi_so.md` đã tính ba chỉ số thử nghiệm và ba rủi ro kinh tế. Danh sách event cùng hai chỉ số nhóm tự đề xuất vẫn cần hoàn thiện.

## 4. Kết quả và đề xuất

Chi phí mỗi việc thành công của toàn mẫu là **4.472 đ** [simulated]. Trong phạm vi `noi_dia` + `hang_nang`, chi phí là **4.599 đ/việc** sau khi cộng chi phí cố định ở quy mô 45.000 yêu cầu/tháng [simulated]. Chi phí cả hệ thống của mẫu là **5.865 đ/yêu cầu**, bằng **0,49×** mức 12.000 đ nhân viên tự làm [simulated]. Nhóm đề xuất pilot chỉ cho `noi_dia` và `hang_nang`; loại `quoc_te` khỏi phạm vi vì chi phí **1,88×** mức nhân viên tự làm và tỉ lệ thành công 27,3% [simulated].

Trong mẫu, chỉ số chính là 82,83%, chỉ số dùng là 27,12%, và tỉ lệ mở lại trong 7 ngày là 4,25%. Hồ sơ launch v0 hiện đề xuất **Go có điều kiện**: xác nhận khóa chống trùng/đối soát sổ cái, Giám đốc vận hành chấp nhận MDE 6 điểm và power 0,64 nếu tác động thật chỉ là 5 điểm, đồng thời hoàn thiện logging có `trace_id`. **Kết quả duyệt chéo chưa được ghi nhận**; `phieu_cham.md` còn chờ buổi hội đồng.

## 5. Khó khăn và cách xử lý

Với 40 nhân viên, phân cụm theo nhân viên không đủ lực thống kê để phát hiện mức chênh 5 điểm; nhóm chọn MDE 6 điểm và nêu rõ power chỉ còn 0,64 nếu hiệu quả thật là 5 điểm. Tỉ lệ mở lại hiện tại đã là 4,25%, nên kế hoạch dùng ngưỡng chênh so với đối chứng và trần tuyệt đối 6% thay cho ngưỡng tuyệt đối 3% có thể làm pilot dừng ngay.

## 6. Tổng hợp đóng góp

- **Hoàng Đăng Kiên — người viết code:** triển khai mô hình chi phí, độ nhạy, cỡ mẫu và các chỉ số tính thử trong `src/lab13.py`.
- **Lê Quang Trường — người kiểm số:** tính tay đối chiếu các số A–B, điền và soát bảng chi phí, cung cấp số cho pilot và rủi ro.
- **Giáp Mạnh Tuyên — người gắn nhãn 2, giữ hồ sơ:** gắn nhãn độc lập, đề xuất biện pháp khắc phục, tổng hợp hồ sơ launch v0.
- **Đỗ Hoàng Phúc — người gắn nhãn 1:** gắn nhãn độc lập và cùng đối chiếu 20 ca lỗi.

## 7. Hạn chế và hướng cải thiện

Dữ liệu và thời gian nhân viên đều giả lập; số chi phí cần được thay bằng thời gian đo thật trong pilot. Dữ liệu chạy thử chưa có đối chứng nên các chỉ số mô tả hiện trạng, chưa chứng minh tác động nhân quả. Trước khi gửi hồ sơ cuối, nhóm cần hoàn thiện event có `trace_id`, thêm hai chỉ số tự đề xuất, xác nhận các ngưỡng vận hành, lấy chữ ký chấp nhận đánh đổi pilot và ghi kết quả duyệt chéo.

## 8. Tài liệu tham khảo

- `docs/du_lieu_va_cong_thuc.md` — dữ liệu, giả định và công thức.
- `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` — hướng dẫn nhiệm vụ A–E và số đối chiếu.
- `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` — đề bài và 20 ca lỗi.
- Google PAIR, [People + AI Guidebook: Errors + Graceful Failure](https://pair.withgoogle.com/guidebook/chapters/errors-graceful-failure/).
