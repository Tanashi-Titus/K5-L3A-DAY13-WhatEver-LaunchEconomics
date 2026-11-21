# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Thành viên 1 · Người gắn nhãn 2: GMTuyen (gắn độc lập trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Ngầm | Không | Ngầm |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 19 / 20 = 95%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 8 (`Ngầm`, không phải `Hệ thống`):** Dù bịa "Điều 7.2 chính sách hoàn phí", số tiền hoàn vẫn đúng nên người dùng không phàn nàn và hệ thống không phát cảnh báo; nếu không kiểm tra đối chiếu lại chính sách thì không phát hiện được lỗi.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `input_validation_failed`; cảnh báo khi vượt 2% yêu cầu/ngày | Kiểm tra định dạng trước khi tạo lệnh hoàn; hỏi lại và gợi ý định dạng đúng | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát event `refund_success_claimed` với kết quả sổ cái mỗi giờ; ngưỡng ≥1 thông báo thành công không có bản ghi `ok` cùng `trace_id` | Chỉ báo thành công khi sổ cái xác nhận; sau 3 lần lỗi 503 thì chuyển nhân viên | Kỹ sư trưởng agent |
| 3 | Ngữ cảnh | Event `ticket_reopened` với lý do `refund_destination`; rà soát hàng tuần, ngưỡng ≥1 ca | Giải thích tiền được hoàn về ví LogiX và hướng dẫn rút về ngân hàng | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Rà soát hàng tuần các event `handoff_to_staff` có lý do thiếu dữ liệu; ngưỡng ≥1 ca thiếu lời giải thích hoặc tóm tắt | Giữ luồng chuyển nhân viên, nêu rõ giới hạn và đính kèm tóm tắt ca | PM trợ lý hoàn phí |
| 5 | Ngầm | Kiểm tra mẫu 100 đơn/tuần qua event `audit_sample_checked`; ngưỡng ≥1 đơn hoàn theo giá trước giảm | Sửa quy tắc hoàn khi có mã giảm giá và liên hệ khách bị ảnh hưởng | Trưởng nhóm kiểm soát chất lượng |
