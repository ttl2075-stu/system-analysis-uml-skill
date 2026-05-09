# Runtime Rules — Quy tắc thực thi

Quy tắc bắt buộc agent tuân thủ khi áp dụng skill này.

## 1. Evidence-first

### Nguyên tắc
Mọi phát biểu về **hiện trạng** hệ thống phải có nguồn xác thực được:
- Trích đoạn code (file path + line range).
- Trích đoạn tài liệu (file + section).
- Phỏng vấn / observation (ghi rõ người, thời gian).
- Test/log run thực tế.

### Phân loại 3 nhãn phát biểu (bắt buộc)
| Nhãn | Khi dùng | Vd |
|---|---|---|
| **[FACT]** | Quan sát từ source xác thực | "[FACT] `BookService.borrow()` ở `services/book.py:45-89` gọi `BookRepository.update()` — nguồn: code scan." |
| **[PROPOSAL]** | Đề xuất design/cải tiến | "[PROPOSAL] Tách BorrowService và FineService để giảm coupling." |
| **[OPEN]** | Chưa đủ thông tin | "[OPEN] Chưa rõ business rule cho overdue: charge ngay sau due date hay sau 1 ngày grace period?" |

### Khi không có evidence
- KHÔNG suy diễn từ "common practice".
- Đặt câu hỏi cho user, hoặc đánh dấu **[OPEN]**.

## 2. No step-skipping (nhưng iterative)

### Quy trình tiêu chuẩn
Phase 1 (Functional) → Phase 2 (Structural) → Phase 3 (Behavioral) → Phase 4 (Design) → V&V.

### Khi được phép quay lại bước trước
- Phát hiện lỗi/thiếu khi balancing models (xem `references/05-balancing-models.md`).
- User feedback đổi requirement.
- Stakeholder phát hiện gap khi walkthrough.

→ Quay lại sửa **đồng thời** mọi artifact bị ảnh hưởng. KHÔNG sửa 1 chỗ và phớt lờ chỗ khác (drift).

### Khi không được phép skip
- KHÔNG sang Phase 2 nếu chưa có catalog use case + ít nhất description cho core use case.
- KHÔNG sang Phase 3 nếu chưa có CRC + class diagram cơ bản.
- KHÔNG sang Phase 4 nếu chưa có sequence cho core use case.
- KHÔNG đóng project nếu thiếu traceability + V&V cho core flow.

## 3. Domain-agnostic

### Quy tắc
Skill này KHÔNG gắn với bất kỳ domain cụ thể.
- Khi tạo template hoặc generic guidance: dùng placeholder (`<EntityName>`, `<UseCaseName>`).
- Khi giải thích: có thể minh họa bằng ví dụ (library, e-commerce, hospital) nhưng phải nói rõ "ví dụ minh họa, có thể thay bằng domain của bạn".
- KHÔNG copy ví dụ library/hospital vào template như "default content".

## 4. Output discipline

### Mỗi response của agent phải kết thúc với 4 phần
```
## Đã làm
- [danh sách artifact đã tạo/cập nhật]

## Evidence
- [nguồn dữ liệu, file path, đoạn trích, hoặc đánh dấu là giả định]

## Còn thiếu
- [input/decision còn cần từ user]

## Bước kế tiếp
- [phase / artifact đề xuất tiếp theo]
```

### Khi không có thay đổi file
Phải giải thích lý do thay vì chỉ trả lời chung chung.

## 5. Scope discipline

### Trong context yêu cầu phân tích/thiết kế tài liệu
- KHÔNG tự ý chỉnh code runtime.
- KHÔNG xóa/ghi đè tài liệu cũ trừ khi user yêu cầu rõ.
- Khi có conflict giữa tài liệu cũ và phát hiện mới: tạo file mới hoặc đề xuất diff, KHÔNG silent overwrite.

### Git behavior
- **Default review mode**: dừng ở `git status`, không commit/push.
- **Commit mode**: chỉ khi user explicit yêu cầu commit.

## 6. Quality gates

Trước khi đóng mỗi phase, agent **phải** chạy checklist:
- Phase 1: `checklists/diagram-quality.md` mục B (Use Case) + C (Activity).
- Phase 2: `checklists/diagram-quality.md` mục D (Class) + E (CRC).
- Phase 3: `checklists/diagram-quality.md` mục F (Sequence) + G (State).
- Phase 4: `checklists/diagram-quality.md` mục H (Package/Component/Deployment).
- Trước khi sang phase tiếp / đóng project: `checklists/balancing-models.md`.

Fail checklist → KHÔNG đóng phase.

## 7. Khi gặp blocker

1. Ghi blocker dưới dạng **[OPEN]** trong artifact.
2. Đưa 1-3 phương án xử lý kèm trade-off.
3. Đặt câu hỏi tối thiểu để mở khóa (1 câu thường đủ).
4. Tạm dừng phase hiện tại, không nhảy sang phase khác để "tránh blocker".
