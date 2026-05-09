# Runtime Checklist (per-turn)

Chạy mỗi lượt agent thực thi.

## Trước khi bắt đầu
- [ ] Đã xác định **phase hiện tại** (1/2/3/4 hoặc V&V).
- [ ] Đã đọc artifact đầu vào bắt buộc của phase.
- [ ] Đã xác định **mode**: review (default) / commit.

## Trong khi xử lý
- [ ] Mọi phát biểu hiện trạng có **[FACT]** + nguồn.
- [ ] Đề xuất gắn nhãn **[PROPOSAL]**.
- [ ] Câu hỏi/blocker gắn nhãn **[OPEN]**.
- [ ] Không nhảy qua phase chưa pass quality gate.
- [ ] Diagram mới pass `checklists/diagram-quality.md` cho loại tương ứng.
- [ ] Update artifact đúng template (`templates/`).

## Trước khi kết thúc lượt
- [ ] Output có đủ **4 phần** (Đã làm / Evidence / Còn thiếu / Bước kế tiếp).
- [ ] Báo blocker rõ (nếu có) kèm 1-3 phương án xử lý.
- [ ] Nếu sang phase mới → đã chạy `checklists/balancing-models.md` cho phase cũ.
- [ ] Mode review: dừng ở `git status`, không commit/push.
