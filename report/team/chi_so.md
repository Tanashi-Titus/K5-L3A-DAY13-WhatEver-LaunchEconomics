# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: ... | ... | Không cần tính |
| An toàn | Nhóm tự đề xuất: ... | ... | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- ...

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng (yếu tố nhạy nhất) | Làm lại gấp đôi: 4.472 → 6.787 đ mỗi việc thành công (+51,8%) [simulated] | Tỉ lệ yêu cầu `ket_qua` = `lam_lai` theo tuần, nối event với `trace_id`; cảnh báo khi vượt 2 lần mức đợt chạy thử | Rà nguyên nhân trong bảng lỗi, thu hẹp loại yêu cầu có tỉ lệ làm lại cao; vượt ngưỡng 2 tuần liền thì dừng mở rộng | PM trợ lý hoàn phí |
| Tỉ lệ xem lại hoặc thời gian xem lại tăng | Xem lại gấp đôi: 6.292 đ (+40,7%); xem lại 100% `noi_dia` + `hang_nang`: 11.743 đ = 0,98× của 12.000 đ, hoà vốn khi mỗi lần xem lại ≤ 5,1 phút [simulated] | Phút xem lại trung bình mỗi yêu cầu và tỉ lệ yêu cầu được xem lại, theo tuần | Giữ xem lại theo mẫu thay vì 100%; trung bình vượt 5 phút/lần thì rút gọn màn hình xem lại hoặc giảm phạm vi | Trưởng nhóm CSKH |
| Khối lượng pilot nhỏ làm chi phí cố định mỗi việc tăng | 40 triệu đ/tháng: 1.185 đ/việc ở 45.000 yêu cầu/tháng, 2.370 đ/việc ở một nửa khối lượng → 0,38× lên 0,48× [simulated] | Số việc thành công mỗi tháng trong phạm vi pilot | Báo cáo chi phí kèm khối lượng; khối lượng dưới một nửa kế hoạch thì tính lại trước ngày quyết định | Giám đốc vận hành |
