# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: chờ bộ độc lập · Người gắn nhãn 2: bộ nhãn đã cung cấp (độc lập)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | — | Do người dùng | Chờ đối chiếu | Chờ đối chiếu |
| 2 | — | Hệ thống | Chờ đối chiếu | Chờ đối chiếu |
| 3 | — | Ngữ cảnh | Chờ đối chiếu | Chờ đối chiếu |
| 4 | — | Giới hạn hệ thống | Chờ đối chiếu | Chờ đối chiếu |
| 5 | — | Ngầm | Chờ đối chiếu | Chờ đối chiếu |
| 6 | — | Do người dùng | Chờ đối chiếu | Chờ đối chiếu |
| 7 | — | Hệ thống | Chờ đối chiếu | Chờ đối chiếu |
| 8 | — | Ngầm | Chờ đối chiếu | Chờ đối chiếu |
| 9 | — | Do người dùng | Chờ đối chiếu | Chờ đối chiếu |
| 10 | — | Ngữ cảnh | Chờ đối chiếu | Chờ đối chiếu |
| 11 | — | Giới hạn hệ thống | Chờ đối chiếu | Chờ đối chiếu |
| 12 | — | Ngầm | Chờ đối chiếu | Chờ đối chiếu |
| 13 | — | Giới hạn hệ thống | Chờ đối chiếu | Chờ đối chiếu |
| 14 | — | Do người dùng | Chờ đối chiếu | Chờ đối chiếu |
| 15 | — | Hệ thống | Chờ đối chiếu | Chờ đối chiếu |
| 16 | — | Ngữ cảnh | Chờ đối chiếu | Chờ đối chiếu |
| 17 | — | Ngầm | Chờ đối chiếu | Chờ đối chiếu |
| 18 | — | Ngữ cảnh | Chờ đối chiếu | Chờ đối chiếu |
| 19 | — | Giới hạn hệ thống | Chờ đối chiếu | Chờ đối chiếu |
| 20 | — | Hệ thống | Chờ đối chiếu | Chờ đối chiếu |

**Tỉ lệ đồng thuận:** Chưa tính; chờ bộ nhãn độc lập của người gắn nhãn 1.

## Quy tắc phân biệt cho các ca không trùng

Điền sau khi hai bộ nhãn đã được đối chiếu; hiện chưa xác định ca nào không trùng.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Các nhãn dưới đây giữ nguyên bộ phân loại do người gắn nhãn 2 cung cấp. Mỗi cách phát hiện nêu event, ngưỡng và tần suất; người phụ trách là một vai trò.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `input_validation_failed`; cảnh báo khi vượt 2% yêu cầu/ngày | Kiểm tra định dạng trước khi tạo lệnh hoàn; hỏi lại và gợi ý định dạng đúng | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát event `refund_success_claimed` với kết quả sổ cái mỗi giờ; ngưỡng ≥1 thông báo thành công không có bản ghi `ok` cùng `trace_id` | Chỉ báo thành công khi sổ cái xác nhận; sau 3 lần lỗi 503 thì chuyển nhân viên | Kỹ sư trưởng agent |
| 3 | Ngữ cảnh | Event `ticket_reopened` với lý do `refund_destination`; rà soát hàng tuần, ngưỡng ≥1 ca | Giải thích tiền được hoàn về ví LogiX và hướng dẫn rút về ngân hàng | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Rà soát hàng tuần các event `handoff_to_staff` có lý do thiếu dữ liệu; ngưỡng ≥1 ca thiếu lời giải thích hoặc tóm tắt | Giữ luồng chuyển nhân viên, nêu rõ giới hạn và đính kèm tóm tắt ca | PM trợ lý hoàn phí |
| 5 | Ngầm | Kiểm tra mẫu 100 đơn/tuần qua event `audit_sample_checked`; ngưỡng ≥1 đơn hoàn theo giá trước giảm | Sửa quy tắc hoàn khi có mã giảm giá và liên hệ khách bị ảnh hưởng | Trưởng nhóm kiểm soát chất lượng |
