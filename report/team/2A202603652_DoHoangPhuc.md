# Báo cáo cá nhân — DoHoangPhuc-2A202603652

## 1. Thông tin thành viên

- Họ tên: Đỗ Hoàng Phúc
- MSSV: 2A202603652
- Email: 26ai.phucdh@vinuni.edu.vn
- GitHub: Codeforlife-MagicWed
- Vai trong nhóm: Người gắn nhãn 1

## 2. Phần việc phụ trách

- Thiết lập môi trường Python (`src/.venv`) trên máy cá nhân và chạy kiểm tra chéo `src/lab13.py` (xác nhận đạt 3 phép thử A1 và khớp số liệu các nhiệm vụ A, B, D1, E1).
- Đọc đề, theo dõi điều kiện "Xong khi" và kiểm tra tiêu chí chấm điểm (`RUBRIC.md`) cho các checkpoint, đặc biệt rà soát `report/team/bang_chi_phi.md` (CP1–CP2).
- Thực hiện Nhiệm vụ C (CP3) với vai trò **Người gắn nhãn 1**: gắn nhãn độc lập 20 ca lỗi theo 5 loại của Google PAIR, đối chiếu với Người gắn nhãn 2 (`GMTuyen`), tính tỉ lệ đồng thuận, thống nhất ca lệch và hoàn thiện `report/team/bang_loi.md`.

## 3. Đóng góp cụ thể

- Cài đặt thư viện từ `src/requirements.txt` và chạy xác nhận `src/lab13.py` cho ra kết quả khớp bảng trong `report/team/bang_chi_phi.md`.
- Tự phân tích và gắn nhãn độc lập 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` vào cột `Nhãn người 1` của `report/team/bang_loi.md` (không trao đổi trước khi so nhãn).
- Đối chiếu với bộ nhãn của Người gắn nhãn 2 (`GMTuyen`): đạt **19/20 ca trùng khớp (95%)**, vượt ngưỡng ≥ 80% của rubric.
- Thảo luận cùng nhóm thống nhất nhãn cho ca không trùng duy nhất (Ca 8: `Ngầm`) kèm quy tắc phân biệt rõ ràng.
- Cập nhật thông tin nhóm vào `TEAM.md` và hoàn thiện báo cáo cá nhân.

## 4. Bằng chứng

- Commit `ab5937e`: `docs(report): complete annotator 1 labels and 95% agreement in bang_loi.md` (gộp bộ nhãn Người gắn nhãn 1 + Người gắn nhãn 2, tính đồng thuận 19/20 = 95%).
- Commit `2e7b08e`: `docs(report): update case 8 agreed label to Ngầm in bang_loi.md` (cập nhật nhãn thống nhất Ca 8 và quy tắc phân biệt theo quyết định chung của nhóm).
- File sản phẩm: `report/team/bang_loi.md`, `TEAM.md`, `report/team/2A202603652_DoHoangPhuc.md`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI (Antigravity / Gemini).
- **Mục đích sử dụng:** Giải thích cấu trúc đề bài, ý nghĩa từng file trong repo và quy trình làm việc theo 5 checkpoint; giải thích khung 5 loại lỗi Google PAIR theo nguyên nhân gốc; tạo phiếu trực quan hỗ trợ đọc 20 ca lỗi (`phieu_gan_nhan_1.html`) để tự rà soát; hỗ trợ thao tác Git và định dạng file Markdown.
- **Cách tự kiểm tra:** Tự chạy lại `src/lab13.py` trong môi trường ảo `src/.venv` để đối chiếu toàn bộ số liệu tính toán; tự đọc và rà soát từng ca trong 20 ca lỗi trước khi chốt cột `Nhãn người 1`, không sửa bộ nhãn độc lập sau khi đối chiếu với Người gắn nhãn 2, và trao đổi thống nhất Ca 8 (`Ngầm`) cùng nhóm trước khi push.

## 6. Tự đánh giá

- Hoàn thành đúng tiến độ các đầu việc của vai trò **Người gắn nhãn 1** (CP3 đạt đồng thuận 95%, tuân thủ quy tắc gắn nhãn độc lập và giữ nguyên bộ nhãn gốc sau khi so).
- Cần tiếp tục phối hợp cùng nhóm hoàn tất phần kiểm tra cuối buổi cho CP4 (`pilot_plan.yaml`), CP5 (`chi_so.md`, `ho_so_launch_v0.md`), duyệt chéo Gate 2a (`phieu_cham.md`) và nộp link repo lên LMS đúng hạn.
