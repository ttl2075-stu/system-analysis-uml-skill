# Notation Core — UML/Mermaid Ruleset (Phase 2)

## 1) Mục tiêu
Chuẩn hóa ký pháp biểu diễn để mọi agent tạo sơ đồ có cấu trúc nhất quán, đúng ngữ nghĩa phân tích–thiết kế, và dễ review.

## 2) Quy ước chung (áp dụng cho mọi sơ đồ)
1. Ngôn ngữ: ưu tiên **Mermaid**.
2. Naming:
   - Actor/Role: `PascalCase` hoặc nhãn tự nhiên (Member, Librarian).
   - Use case/Action: động từ + bổ ngữ (Borrow BookItem, Renew Loan).
   - Entity/Class: `PascalCase` (BorrowTransaction, SystemSetting).
   - Event/State: danh từ trạng thái rõ nghĩa (Available, Reserved, Overdue).
3. Không dùng viết tắt mơ hồ nếu không có glossary.
4. Một sơ đồ chỉ nên phục vụ **một mục tiêu chính** (không nhồi nhiều viewpoint).
5. Mọi sơ đồ phải có tiêu đề + mô tả ngắn “purpose”.

## 3) Quy tắc theo loại sơ đồ

### 3.1 Use Case (Mermaid: flowchart)
**Mục tiêu**: thể hiện actor ↔ mục tiêu nghiệp vụ.

**Bắt buộc**
- Có boundary logic của hệ thống (ghi rõ backend scope trong mô tả).
- Use case đặt tên bằng động từ nghiệp vụ.
- Actor kết nối trực tiếp use case liên quan.

**Không nên**
- Nhét chi tiết kỹ thuật (API/repo/db) vào use case diagram.
- Dùng use case để mô tả trình tự thời gian (đó là sequence/activity).

### 3.2 Activity (Mermaid: flowchart TD)
**Mục tiêu**: mô tả quy trình nghiệp vụ theo luồng.

**Bắt buộc**
- Có điểm bắt đầu và kết thúc rõ.
- Có decision nodes cho nhánh điều kiện.
- Có ít nhất 1 nhánh ngoại lệ với core flow.

**Không nên**
- Mô tả chi tiết class hoặc cấu trúc dữ liệu trong activity.

### 3.3 Domain/Class (Mermaid: classDiagram)
**Mục tiêu**: mô tả cấu trúc miền nghiệp vụ và quan hệ.

**Bắt buộc**
- Class chính có thuộc tính cốt lõi.
- Quan hệ có hướng/ngữ nghĩa rõ (association/composition nếu cần).
- Cardinality thể hiện khi có ý nghĩa nghiệp vụ.

**Không nên**
- Đưa SQL index/DDL chi tiết vào domain model.
- Trộn domain class với infra classes trong cùng sơ đồ.

### 3.4 Sequence (Mermaid: sequenceDiagram)
**Mục tiêu**: mô tả tương tác theo thời gian giữa actor và các layer.

**Bắt buộc**
- Participant theo tầng chuẩn: Client/API/Service/Repository/Model/Queue.
- Luồng request/response đầy đủ.
- Nhánh lỗi chính hoặc note lỗi.

**Không nên**
- Bỏ qua bước orchestration tại service layer nếu kiến trúc có service.

### 3.5 State (Mermaid: stateDiagram-v2)
**Mục tiêu**: vòng đời đối tượng nghiệp vụ.

**Bắt buộc**
- Có state khởi đầu và state kết thúc (nếu có).
- Transition phải có trigger rõ.
- Nếu có guard thì ghi dạng `[condition]`.

**Không nên**
- Trộn state của nhiều entity không liên quan trong 1 sơ đồ.

### 3.6 Component (Mermaid: flowchart)
**Mục tiêu**: mô tả thành phần runtime và phụ thuộc.

**Bắt buộc**
- Thể hiện thành phần chính: client, API, DB, queue, worker.
- Chỉ rõ hướng phụ thuộc/giao tiếp.

**Không nên**
- Đi quá sâu vào method-level call (đó là sequence).

### 3.7 Deployment (Mermaid: flowchart)
**Mục tiêu**: mô tả topology triển khai.

**Bắt buộc**
- Có môi trường mục tiêu (dev/staging/prod hoặc tương đương).
- Có node/chức năng chính và luồng kết nối.

**Không nên**
- Trộn deployment chi tiết bảo mật nhạy cảm vào tài liệu public.

## 4) Anti-patterns cần tránh
1. Diagram kể chuyện lan man, không có mục tiêu rõ.
2. Lẫn lộn analysis và design trong cùng một sơ đồ.
3. Dùng tên kỹ thuật thấp tầng cho use case nghiệp vụ.
4. Thiếu nhánh lỗi/ngoại lệ ở luồng quan trọng.
5. Sơ đồ không khớp với glossary và thuật ngữ trong tài liệu.

## 5) Mapping UML intent → Mermaid syntax
- Use case intent → `flowchart` (actor node + use case nodes)
- Activity intent → `flowchart TD` + decision labels
- Class intent → `classDiagram`
- Sequence intent → `sequenceDiagram`
- State intent → `stateDiagram-v2`
- Component/Deployment intent → `flowchart` theo node/component topology

## 6) Definition of Done cho Phase 2
- Có ruleset cho toàn bộ sơ đồ cốt lõi.
- Có anti-patterns và naming conventions.
- Có mapping rõ giữa intent UML và cú pháp Mermaid.
