# Runtime Behavior Spec — system-analysis-uml (Phase 4)

## 1) Mục tiêu
Định nghĩa hành vi vận hành bắt buộc để agent thực thi đúng quy trình phân tích–thiết kế, tránh trả lời cảm tính hoặc nhảy bước.

## 2) Runtime Contract

### 2.1 Nguyên tắc điều phối
1. Agent phải chạy theo thứ tự Step 1 → Step 8 trong `method-core.md`.
2. Mỗi bước chỉ được coi là hoàn thành khi thỏa `quality checks` và không vi phạm `stop rule`.
3. Nếu thiếu input bắt buộc, agent phải:
   - nêu rõ thiếu gì,
   - đặt câu hỏi làm rõ,
   - tạm dừng bước hiện tại.

### 2.2 Phân loại phát biểu bắt buộc
Mọi kết luận phải được gắn nhãn tư duy:
- **Analysis fact**: sự thật quan sát từ code/docs/tests.
- **Design proposal**: đề xuất mục tiêu/định hướng.
- **Open issue**: điểm chưa đủ dữ liệu.

### 2.3 Evidence-first policy
- Mọi nhận định về hiện trạng bắt buộc có evidence:
  - đường dẫn file,
  - tên module/endpoint/test,
  - hoặc trích đoạn có thể kiểm chứng.
- Không được suy diễn hiện trạng nếu chưa scan evidence tối thiểu.

## 3) Phase Gates (cổng chuyển pha)

### Gate G1 (Scope Gate)
Pass khi:
- Có actors-and-scope rõ ràng.
- In-scope/out-of-scope được chốt.

Fail nếu:
- Không có actor chính.
- Scope dùng từ mơ hồ ("nhiều", "đầy đủ") mà không định nghĩa.

### Gate G2 (Use Case Gate)
Pass khi:
- Có catalog use case core.
- Mỗi actor chính có ít nhất 1 use case.

Fail nếu:
- Use case đặt theo kỹ thuật thấp tầng (ví dụ "call repository").

### Gate G3 (Functional Gate)
Pass khi:
- Có activity diagram cho core flows.
- Có nhánh ngoại lệ chính.

### Gate G4 (Structural Gate)
Pass khi:
- Domain model có entity cốt lõi và quan hệ chính.
- Mapping sơ bộ tới layer dữ liệu có thể kiểm chứng.

### Gate G5 (Behavioral Gate)
Pass khi:
- Có sequence cho use case trọng yếu.
- Có state model cho đối tượng có vòng đời.

### Gate G6 (Design Gate)
Pass khi:
- Có package/component/runtime view.
- Có nguyên tắc transaction, security, error.

### Gate G7 (Traceability Gate)
Pass khi:
- Matrix truy vết đủ chuỗi use case → test.
- Có danh sách gap ưu tiên.

## 4) Output Discipline

### 4.1 Quy tắc tạo output
- Mỗi lượt chạy phải tạo hoặc cập nhật artifact cụ thể.
- Cập nhật nhật ký tiến độ (phase, kết quả, blocker).
- Nếu không có thay đổi file, phải giải thích lý do.

### 4.2 Quy tắc trình bày
- Báo cáo theo format ngắn:
  1) Đã làm gì
  2) Evidence từ đâu
  3) Còn thiếu gì
  4) Bước kế tiếp

## 5) Safety & Change Control

### 5.1 Git behavior modes
- **Review mode (mặc định):** không commit/push, dừng ở `git status`.
- **Commit mode:** chỉ commit khi có lệnh explicit từ người dùng.

### 5.2 Không tự ý thay đổi ngoài scope
- Không chỉnh module runtime nếu nhiệm vụ chỉ là tài liệu.
- Không xóa/ghi đè tài liệu cũ nếu chưa đánh dấu thay thế.

## 6) Mermaid Quality Enforcement
- Mọi sơ đồ mới phải pass `diagram-qa-checklist.md`.
- Nếu fail checklist, không được đánh dấu phase completed.

## 7) Exception Handling Policy
Khi gặp blocker:
1. Ghi blocker vào nhật ký phase.
2. Đưa 1–3 phương án xử lý.
3. Chỉ đặt câu hỏi tối thiểu cần thiết để mở khóa.

## 8) Completion Criteria cho Phase 4
Phase 4 hoàn thành khi:
- Có runtime rules đầy đủ cho điều phối, gate, evidence, output, safety.
- Có checklist vận hành để agent tự kiểm định mỗi lượt chạy.
