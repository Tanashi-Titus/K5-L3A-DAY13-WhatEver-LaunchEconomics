# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): WhatEver (Hoàng Đăng Kiên, Giáp Mạnh Tuyên, Lê Quang Trường, Đỗ Hoàng Phúc)
- Nhóm được chấm: Nhóm 6 DTL (Lục Anh Tuấn – 2A202603634, Nguyễn Thùy Lam – 2A202603632, Mai Lâm Tấn Đạt – 2A202603645)
- Ghi chú: hai nhóm duyệt chéo lẫn nhau tại buổi; nhóm 6 DTL đồng thời là hội đồng chấm hồ sơ của WhatEver (xem `group_report.md`).

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất khớp với số của nhóm (chi phí trong phạm vi 0,38× của 12.000 đ ở 45.000 yêu cầu/tháng); nhóm nêu cả điều kiện bất lợi về thời gian xem lại (hoà vốn khi mỗi lần ≤ 5,1 phút) và đặt điều kiện xử lý tương ứng [simulated] |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Các số tính từ hai cột `_simulated` (phút xem lại, phút làm lại, ngưỡng hoà vốn 5,1 phút) đều có nhãn simulated; phạm vi pilot được thu hẹp, có lý do bằng chi phí so với mức 12.000 đ của nhân viên tự làm |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Có nhóm đối chứng, chia ngẫu nhiên, tối đa 20 nhân viên dùng trợ lý; có danh sách 8 event, ngày bắt đầu 07/12 và mốc kiểm tra 14/12; chỉ số an toàn đặt ngưỡng 0 ca hoàn sai số tiền; luật dừng có ngưỡng, thời hạn và vai trò có quyền dừng |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go

**Lý do:** Hồ sơ đạt mức tối đa ở cả ba tiêu chí: đề xuất bám sát số liệu của chính nhóm (0,38× của 12.000 đ, hoà vốn khi xem lại ≤ 5,1 phút [simulated]), số giả lập được gắn nhãn đầy đủ, và kế hoạch pilot có đối chứng, 8 event, mốc thời gian và luật dừng cụ thể. Đội trình trả lời thuyết phục cả năm câu hỏi của hội đồng; hội đồng hài lòng cao với hồ sơ.

**Câu hỏi cho đội trình** (hội đồng đặt năm câu):

1. Hai người gắn nhãn khớp 20/20 ca. Các bạn có bằng chứng hai người làm độc lập không, và ca 8 (bịa "Điều 7.2" nhưng số tiền vẫn đúng) các bạn xếp vào loại nào, vì sao?
2. Hồ sơ ghi hoà vốn khi mỗi lần xem lại ≤ 5,1 phút với giả định làm lại 9 phút. Nhưng dữ liệu cho thấy làm lại trung bình 15,3 phút, khi đó hoà vốn chỉ khoảng 4,8 phút. Vậy ngưỡng "≤ 5 phút" ở điều kiện (4) có còn hoà vốn không?
3. Lỗi ngầm như ca 5 và ca 17 hoàn sai số tiền mà không ai phàn nàn. Trong 8 event, event nào giúp phát hiện loại lỗi này, và chỉ số an toàn "ngưỡng 0 ca" được tính bằng cách nào?
4. Điều kiện (3) yêu cầu bật đủ 8 event trước ngày bắt đầu 07/12, nhưng đến 14/12 mới kiểm tra. Nếu lúc đó mới phát hiện thiếu event thì tuần pilot đầu tiên có còn dùng được không, và ai có quyền dừng?
5. Trong pilot chỉ có tối đa 20 nhân viên dùng trợ lý, nên khối lượng thấp hơn nhiều so với 45.000 yêu cầu/tháng. Ở khối lượng thật của pilot, chi phí cố định mỗi việc là bao nhiêu, và con số 0,38× có còn đúng không?

**Câu trả lời của đội trình (ghi lại tại buổi):** Đội trình trả lời lần lượt cả năm câu; các thành viên hội đồng WhatEver đều đồng tình với câu trả lời. Hội đồng không ghi lại chi tiết từng câu trả lời tại buổi.
