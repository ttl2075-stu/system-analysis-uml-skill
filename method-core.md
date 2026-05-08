# Method Core — system-analysis-uml (Phase 1)

## 1) Mục tiêu
Định nghĩa workflow chuẩn để AI Agent phân tích và thiết kế hệ thống theo hướng design-first, có thể áp dụng nhất quán cho backend-centric projects.

## 2) Workflow 8 bước bắt buộc

### Step 1 — Context & Scope Definition
**Input bắt buộc**
- Mục tiêu hệ thống
- Phạm vi nghiệp vụ (in-scope / out-of-scope)
- Bối cảnh triển khai (runtime, team, constraints)

**Output**
- `actors-and-scope.md`
- danh sách bounded modules

**Quality checks**
- Có ranh giới rõ giữa business scope và technical scope
- Có giả định và ràng buộc cụ thể

**Stop rule**
- Không sang Step 2 nếu scope còn mơ hồ hoặc chưa xác định actor chính

---

### Step 2 — Actors & Use Case Catalog
**Input bắt buộc**
- Scope đã chốt
- Bản đồ module sơ bộ

**Output**
- `use-case-catalog.md`
- sơ đồ use case overview (Mermaid)

**Quality checks**
- Use case viết theo động từ nghiệp vụ
- Mỗi actor có ít nhất 1 mục tiêu nghiệp vụ rõ ràng

**Stop rule**
- Không sang Step 3 nếu chưa có catalog core use cases

---

### Step 3 — Use Case Descriptions
**Input bắt buộc**
- Use case catalog

**Output**
- `use-case-descriptions.md` theo mẫu:
  - preconditions
  - main flow
  - alternative/exception flows
  - postconditions
  - impacted modules

**Quality checks**
- Flow không mâu thuẫn business rules
- Có ít nhất 1 flow ngoại lệ cho use case quan trọng

**Stop rule**
- Không sang Step 4 khi use case core chưa có mô tả chi tiết

---

### Step 4 — Functional Modeling (Activity)
**Input bắt buộc**
- Use case descriptions đã duyệt

**Output**
- `activity-models.md`
- Mermaid activity diagrams cho luồng trọng yếu

**Quality checks**
- Mỗi activity có start/decision/end rõ
- Nhánh lỗi (error/exception) được thể hiện

**Stop rule**
- Không sang Step 5 nếu activity còn thiếu nhánh nghiệp vụ chính

---

### Step 5 — Structural Modeling (Domain/Class)
**Input bắt buộc**
- Activity + use case đã ổn định
- Danh sách entity từ nghiệp vụ và code scan

**Output**
- `domain-model.md`
- class/domain diagram (Mermaid classDiagram)

**Quality checks**
- Entity có trách nhiệm rõ
- Quan hệ và cardinality hợp lý

**Stop rule**
- Không sang Step 6 nếu domain model chưa map được về module dữ liệu chính

---

### Step 6 — Behavioral Modeling (Sequence/State)
**Input bắt buộc**
- Domain model
- Use case chi tiết

**Output**
- `sequence-design.md`
- `state-models.md`
- sequence/state diagrams Mermaid

**Quality checks**
- Sequence thể hiện đúng ranh giới API/Service/Repo
- State model có trigger/guard/transition rõ

**Stop rule**
- Không sang Step 7 nếu chưa mô tả được lifecycle đối tượng cốt lõi

---

### Step 7 — Design Modeling
**Input bắt buộc**
- Functional + structural + behavioral models

**Output**
- `package-design.md`
- `component-design.md`
- `deployment-design.md` (nếu có)
- `data-management-design.md`
- `security-design.md`
- `error-handling-and-exceptions.md`

**Quality checks**
- Có phân lớp trách nhiệm rõ ràng
- Có nguyên tắc transaction và consistency
- Có error taxonomy + authZ mapping

**Stop rule**
- Không sang Step 8 nếu chưa có runtime view và non-functional decisions

---

### Step 8 — Traceability, Quality & Gap
**Input bắt buộc**
- Toàn bộ artifacts từ Step 1-7

**Output**
- `usecase-to-code-matrix.md`
- `api-service-repo-model-matrix.md`
- `quality-attributes.md`
- `gap-report.md`

**Quality checks**
- Truy vết đủ chuỗi: use case → endpoint → service → repo → model → test
- Có backlog gap theo ưu tiên

**Stop rule**
- Chưa kết thúc nếu thiếu traceability cho core flows

---

## 3) Quy tắc thực thi bắt buộc cho Agent
1. Không nhảy bước khi chưa qua stop rule bước trước.
2. Mọi nhận định “hiện trạng” phải có evidence từ code/docs/tests.
3. Phân biệt rõ:
   - **Analysis fact** (sự thật hiện trạng)
   - **Design proposal** (đề xuất mục tiêu)
4. Ưu tiên Mermaid nhất quán ký pháp trong toàn bộ artifacts.
5. Nếu thiếu dữ liệu đầu vào, agent phải đặt câu hỏi làm rõ thay vì suy diễn.

## 4) Definition of Done cho Phase 1
- Có workflow 8 bước đầy đủ input/output/check/stop-rule.
- Có execution rules cho agent.
- Có thể dùng ngay để dẫn dắt tạo tài liệu backend theo chuẩn.
