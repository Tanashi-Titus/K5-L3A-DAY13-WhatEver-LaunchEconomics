# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 (ĐẠT) |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 (ĐẠT) |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 (ĐẠT, = 1/p vì k triệt tiêu) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` (5.600 lần gọi × 15 đ) | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút × 2.000 đ) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút × 2.000 đ) | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 / 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (245.585 + 84.000) / 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,3 lần** hoá đơn chia số yêu cầu (4.472 / 274,7) [simulated].
- Khoản lớn nhất là **làm lại, 51,8%** tổng chi phí, tiếp theo là xem lại 40,7% [simulated]; giờ nhân viên chiếm 92,5%.
- So công bằng với nhân viên tự làm (cộng 222 ca không thành công × 12.000 đ): 5.865 đ/yêu cầu = **0,49×** của 12.000 đ [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× |

- **quoc_te** không đáng để trợ lý xử lý: 1,88× của 12.000 đ, chỉ thành công 27,3% [simulated].
- Chạy lại tới 3 lần không giúp: tỉ lệ ok của quoc_te lần 1 là 30,0%, lần 2 còn 11,4%, lần 3 còn 2,2%; lỗi lặp lại nên chạy lại chỉ tốn thêm tiền.
- doi_tac sát ngưỡng (0,85×) và có điều khoản riêng, nên cũng để ngoài phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Phạm vi: 982 yêu cầu, 900 thành công, tổng 3.072.513 đ → chi phí mỗi việc thành công 3.414 đ [simulated].

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× |
| Một nửa khối lượng (22.500) | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× |

- Không đổi kết luận: ở 45.000 yêu cầu/tháng vẫn 0,38×, ở nửa khối lượng 0,48× [simulated].
- Nhưng chi phí cố định mỗi việc tăng gấp đôi (1.185 → 2.370 đ) khi khối lượng giảm một nửa, nên giai đoạn pilot khối lượng nhỏ phải ghi rõ con số đã cộng cố định.

## B1 · Đổi từng yếu tố

Gốc (A2): 4.472 đ [simulated].

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

Tất cả số trong bảng là simulated. Tự kiểm tra: mỗi kịch bản "giảm một nửa" bằng đúng −½ mức của "gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9): ĐẠT.

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)** [simulated], đúng bằng tổng hai tác động riêng (+5,6% + 40,7%) vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. Số ca làm lại (±51,8%) · 2. Tỉ lệ xem lại (±40,7%) · 3. Lương nhân viên (+23,1%) [simulated].

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công. Tất cả là simulated.

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ (rẻ nhất)** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn **2 lần** rẻ nhất cho công ty (6.901.220 đ), **không trùng** với giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ) [simulated].
- Tối ưu riêng chi phí mỗi việc thành công sẽ đẩy thêm 85 việc (319 − 234) sang nhân viên.

## B4 · Nếu phải xem lại tất cả

- Phạm vi 982 yêu cầu: 948 yêu cầu có lần chạy ok × 5 phút × 2.000 đ = 9.480.000 đ; 48 ca làm lại × 9 phút × 2.000 đ = 864.000 đ; token + tool 224.513 đ → tổng 10.568.513 đ / 900 = **11.743 đ = 0,98×** của 12.000 đ [simulated].
- Nếu dùng phút làm lại theo dữ liệu (trung bình 15,3 phút, trung vị 14,5): **12.415 đ = 1,03×**, đắt hơn nhân viên tự làm [simulated]. Hoà vốn khi mỗi lần xem lại ≤ 5,1 phút (9 phút làm lại) hoặc ≤ 4,8 phút (15,3 phút).
- Pilot phải học được tỉ lệ xem lại giảm an toàn xuống mức nào và mỗi lần xem lại có dưới 5 phút được không, vì xem lại 100% gần như xoá hết phần tiết kiệm (tiền xem lại chiếm ~90% chi phí).

## Đối chiếu của người kiểm số

Tính tay độc lập với code, so với số `src/lab13.py` in ra (cho phép lệch ≤ 2%):

| Con số | Cách tính tay | Tính tay | Code | Khớp |
| --- | --- | ---: | ---: | --- |
| A1 · tối đa 2 lần | (1 − 0,2²) / 0,8 | 1,20 | 1,20 | Có |
| A1 · tối đa 3 lần | [(1 − 0,2³) / 0,8] / (1 − 0,2³) = 1 / 0,8 | 1,25 | 1,25 | Có |
| A2 · tiền xem lại | 890 phút × 2.000 đ | 1.780.000 | 1.780.000 | Có |
| A2 · chi phí mỗi việc thành công | (245.585 + 84.000 + 1.780.000 + 2.264.000) / 978 | 4.472 | 4.472 | Có |
| A4 · cố định mỗi việc | 40.000.000 / (45.000 × 900 / 1.200) | 1.185 | 1.185 | Có |
| B3 · cả hệ thống, 2 lần | 4.093.220 + 234 × 12.000 | 6.901.220 | 6.901.220 | Có |
| B4 · xem lại 100% | (9.480.000 + 864.000 + 224.513) / 900 | 11.743 | 11.743 | Có |
