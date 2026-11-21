# Báo cáo cá nhân — Giáp Mạnh Tuyên-2A202603648

## 1. Thông tin thành viên

- Họ tên: Giáp Mạnh Tuyên
- MSSV: 2A202603648
- Email: 26ai.tuyengm@vinuni.edu.vn
- GitHub: Tanashi-Titus
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Gắn nhãn độc lập 20 ca lỗi theo năm loại của Google PAIR trước khi so với bộ nhãn của người gắn nhãn 1.
- Ghi lý do và đề xuất cách phát hiện, khắc phục lỗi; cùng nhóm hoàn thiện bảng khắc phục 5 loại.
- Giữ hồ sơ launch v0, tổng hợp số liệu A–E do các thành viên cung cấp vào `report/team/ho_so_launch_v0.md`.

## 3. Đóng góp cụ thể

- Tự phân loại và ghi lý do cho 20 ca trong `report/team/bang_loi.md`.
- Sau khi đối chiếu, ghi nhận hai bộ nhãn trùng 19/20 ca (95%); giải thích bất đồng ở ca 8 và thống nhất nhãn Ngầm vì chỉ kiểm tra đối chiếu chính sách mới phát hiện dẫn chiếu sai.
- Đề xuất biện pháp khắc phục cho năm loại lỗi. Bảng ghi event, ngưỡng, tần suất theo dõi và vai trò phụ trách; các ngưỡng vận hành cần được nhóm xác nhận trước khi pilot.
- Tổng hợp bản hồ sơ launch v0 từ kết quả nhóm và nêu các điều kiện còn cần ký/xác nhận trước pilot.

## 4. Bằng chứng

- `report/team/bang_loi.md`: bộ nhãn người gắn nhãn 2, quy tắc ca 8 và bảng khắc phục 5 loại.
- `report/team/ho_so_launch_v0.md`: bản tổng hợp 7 mục và đề xuất Go có điều kiện.
- Commit `28f6c84`: ghi bộ nhãn và phần khắc phục của người gắn nhãn 2.

## 5. Công cụ AI đã dùng

- **Codex:** hỗ trợ đọc yêu cầu, trích nội dung 20 ca từ đề bài, định dạng nhãn do tôi cung cấp, và đề xuất cấu trúc event/ngưỡng/tần suất cho bảng khắc phục và hồ sơ launch.
- **Cách tự kiểm tra:** tự quyết định bộ nhãn trước khi đối chiếu; kiểm tra phép tính đồng thuận `19 / 20 = 95%`; rà mỗi dòng khắc phục có event, ngưỡng, tần suất và một vai trò phụ trách. Tôi không dùng AI để chọn nhãn lỗi thay mình.

## 6. Tự đánh giá

- **Làm tốt:** hoàn thành bộ nhãn độc lập cho đủ 20 ca, nêu được lý do ở ca bất đồng và tổng hợp kết quả thành hồ sơ có điều kiện dừng rõ.
- **Cần cải thiện:** xác nhận các ngưỡng cảnh báo và khả năng ghi event với nhóm kỹ thuật/vận hành trước khi chốt hồ sơ; tiếp tục cập nhật hồ sơ khi nhóm thống nhất đề xuất cuối.
