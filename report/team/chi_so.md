# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: Tỉ lệ yêu cầu trong phạm vi của nhóm can thiệp có mở gợi ý trợ lý | Số yêu cầu nhóm can thiệp (`arm = treatment`, thuộc `noi_dia` hoặc `hang_nang`) có event `agent_suggestion_shown`, chia tổng số yêu cầu trong phạm vi của nhóm can thiệp | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ đơn hoàn sai số tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | Số đơn có `so_tien_da_hoan != so_tien_dung` trong `audit_sample_checked`, chia tổng số đơn được kiểm tra mẫu (100 đơn/tuần) | Không cần tính |

Chỉ số trong đợt chạy thử (1.200 yêu cầu) là 82,83% (chính), 27,12% (bỏ qua gợi ý) và 4,25% (mở lại trong 7 ngày); không kết luận trợ lý đã nâng chỉ số so với 0,70 vì đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Mười một event (vượt yêu cầu tối thiểu 6), mọi event đều mang `trace_id` để nối với trace của agent và phục vụ đối soát chi phí thật thay cho cột `_simulated`.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id, loai, so_tien_vnd, arm, trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Agent | `run_id, attempt, tokens_in, tokens_out, tool_calls, status, trace_id` | Sau mỗi lần chạy của agent, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện CSKH | `request_id, staff_id, arm, so_tien_de_xuat, trace_id` | Khi gợi ý của trợ lý hiển thị cho nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `staff_id, quyet_dinh (giu/sua/bo), phut_xem_lai, trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý (đo phút thật) |
| `staff_rework_completed` | Nhân viên CSKH | `staff_id, phut_lam_lai, ly_do, trace_id` | Khi nhân viên hoàn tất làm lại một ca sai (đo phút thật) |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key, so_tien_vnd, ket_qua (ok/loi), trace_id` | Khi ghi lệnh hoàn tiền vào sổ cái (đối soát chống hoàn trùng) |
| `refund_success_claimed` | Agent | `request_id, ledger_status, message_id, trace_id` | Khi agent gửi thông báo đã hoàn tiền thành công cho khách; đối soát với kết quả sổ cái |
| `handoff_to_staff` | Agent | `reason, tom_tat, trace_id` | Khi agent chuyển yêu cầu sang nhân viên (ca 4) |
| `ticket_closed` | Hệ thống ticket | `request_id, closed_at, trace_id` | Khi yêu cầu hoàn phí được đóng |
| `ticket_reopened` | Khách hàng / Hệ thống ticket | `request_id, reopened_at, reason, trace_id` | Khi khách mở lại yêu cầu sau khi đóng (ca 3) |
| `audit_sample_checked` | Nhóm kiểm soát chất lượng / Kế toán | `request_id, so_tien_da_hoan, so_tien_dung, trace_id` | Khi kiểm tra mẫu 100 đơn hằng tuần (bắt lỗi ngầm ca 5, 17) |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Cả 5/5 chỉ số đều tính được trực tiếp từ danh sách event trên qua khoá nối `trace_id` / `request_id`:

- **Chính (% đóng trong 24 giờ và không mở lại trong 7 ngày):** `refund_request_created` (mốc tạo yêu cầu, `arm`) + `ticket_closed` (`closed_at − created_at ≤ 24h`) + `ticket_reopened` (không xuất hiện trong vòng 7 ngày sau `closed_at`).
- **Dùng (Tỉ lệ bỏ qua gợi ý):** `staff_review_decision` (`quyet_dinh` thuộc `sua` hoặc `bo` chia tổng số event `staff_review_decision`).
- **An toàn (Tỉ lệ lỗi lọt đến khách — mở lại trong 7 ngày):** `ticket_reopened` (trong vòng 7 ngày sau `ticket_closed`) chia tổng số `refund_request_created`.
- **Dùng tự đề xuất (% yêu cầu trong phạm vi của nhóm can thiệp có mở gợi ý trợ lý):** `agent_suggestion_shown` (lọc `arm = treatment`, ghép `loai` từ `refund_request_created`) chia tổng `refund_request_created` thuộc `noi_dia` + `hang_nang` của nhóm can thiệp; đồng thời dùng `staff_id` trên `agent_suggestion_shown` để kiểm soát rò rỉ sang nhóm đối chứng.
- **An toàn tự đề xuất (% đơn hoàn sai số tiền qua kiểm tra mẫu hằng tuần):** `audit_sample_checked` (số đơn có `so_tien_da_hoan != so_tien_dung` chia tổng số đơn mẫu kiểm tra trong tuần); kết hợp `refund_ledger_write` để bắt ca hoàn trùng hoặc báo thành công không khớp sổ cái (`trace_id`).
- **Bổ trợ đo chi phí thật trong pilot:** `agent_run_completed` (token, tool mọi lần chạy) + `staff_review_decision` (`phut_xem_lai` đo thật) + `staff_rework_completed` (`phut_lam_lai` đo thật) thay cho hai cột `_simulated`.
- **Đối soát an toàn:** `refund_success_claimed` phải ghép với `refund_ledger_write` cùng `trace_id`; ngưỡng dừng là ≥1 thông báo thành công không có bản ghi sổ cái `ok`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng (yếu tố nhạy nhất) | Làm lại gấp đôi: 4.472 → 6.787 đ mỗi việc thành công (+51,8%) [simulated] | Tỉ lệ yêu cầu `ket_qua` = `lam_lai` theo tuần, nối event với `trace_id`; cảnh báo khi vượt 2 lần mức đợt chạy thử | Rà nguyên nhân trong bảng lỗi, thu hẹp loại yêu cầu có tỉ lệ làm lại cao; vượt ngưỡng 2 tuần liền thì dừng mở rộng | PM trợ lý hoàn phí |
| Tỉ lệ xem lại hoặc thời gian xem lại tăng | Xem lại gấp đôi: 6.292 đ (+40,7%); xem lại 100% `noi_dia` + `hang_nang`: 11.743 đ = 0,98× của 12.000 đ, hoà vốn khi mỗi lần xem lại ≤ 5,1 phút [simulated] | Phút xem lại trung bình mỗi yêu cầu và tỉ lệ yêu cầu được xem lại, theo tuần | Giữ xem lại theo mẫu thay vì 100%; trung bình vượt 5 phút/lần thì rút gọn màn hình xem lại hoặc giảm phạm vi | Trưởng nhóm CSKH |
| Khối lượng pilot nhỏ làm chi phí cố định mỗi việc tăng | 40 triệu đ/tháng: 1.185 đ/việc ở 45.000 yêu cầu/tháng, 2.370 đ/việc ở một nửa khối lượng → 0,38× lên 0,48× [simulated] | Số việc thành công mỗi tháng trong phạm vi pilot | Báo cáo chi phí kèm khối lượng; khối lượng dưới một nửa kế hoạch thì tính lại trước ngày quyết định | Giám đốc vận hành |
