# Phase 1 — Functional Modeling

> Nguồn: Dennis, Wixom & Tegarden — *Systems Analysis & Design with UML* (4th ed.), Chapter 4.

## 1. Mục tiêu phase
Mô tả **chức năng** hệ thống dưới góc nhìn nghiệp vụ:
- Hệ thống làm gì cho ai (use case diagram).
- Mỗi chức năng diễn ra theo quy trình nào (use case description + activity diagram).

## 2. Artifacts của phase

### 2.1 Use Case Diagram
**Mục đích**: thể hiện mối quan hệ giữa actor và use case ở mức tổng quan.

**Thành phần**:
- **Actor**: người/hệ thống ngoài hệ thống đang phân tích, có vai trò (role) chứ không phải con người cụ thể.
- **Use case**: mục tiêu nghiệp vụ actor muốn đạt — đặt theo cấu trúc **động từ + bổ ngữ** (vd: "Borrow Books", "Cancel Appointment").
- **System boundary**: ranh giới hệ thống.
- **Quan hệ**:
  - `<<include>>`: use case A luôn bao gồm hành vi của B.
  - `<<extend>>`: use case B mở rộng A trong điều kiện cụ thể.
  - **Generalization**: kế thừa giữa actor hoặc giữa use case.

**Quy trình tạo (Dennis)**:
1. Xác định business value của hệ thống.
2. Identify primary actors (người trigger use case).
3. Identify primary use cases cho từng actor.
4. Identify relationships giữa actors và use cases.
5. Liệt kê stakeholders để bổ sung use case bị bỏ sót.

### 2.2 Use Case Description
**Mục đích**: mô tả chi tiết mỗi use case dưới dạng văn bản có cấu trúc.

**Phân loại theo Dennis**:
- **Overview** vs **Detail**: tổng quan ban đầu vs chi tiết đầy đủ.
- **Essential** vs **Real**: implementation-independent vs cụ thể đến mức kỹ thuật.
  - Trong analysis: dùng **essential** (không nhắc đến UI/database cụ thể).
  - Trong design/testing: dùng **real**.

**Cấu trúc bắt buộc** (xem `templates/use-case-description.md`):
1. **Overview Information**:
   - Use case name (verb + noun)
   - ID
   - Type (overview/detail × essential/real)
   - Primary actor
   - Stakeholders and Interests
   - Brief description
   - Importance level (high/medium/low)
   - Trigger (external/temporal)
2. **Relationships**:
   - Association (actors)
   - Include / Extend / Generalization
3. **Flow of Events**:
   - Normal flow (3-7 bước chính)
   - Subflows (decompose bước phức tạp)
   - Alternate/Exceptional flows

### 2.3 Quy tắc viết flow of events (Dennis — 7 guidelines)

1. **SVDPI sentences**: Subject–Verb–Direct object–(Preposition–Indirect object). Vd: "The Patient provides the Receptionist with his name." Cấu trúc này giúp identify class và operation ở phase sau.
2. **Initiator vs Receiver rõ ràng**: initiator là chủ ngữ, receiver là tân ngữ.
3. **Bird's-eye view**: viết từ góc nhìn người quan sát độc lập, không từ góc nhìn user hay hệ thống.
4. **Cùng level of abstraction**: mỗi bước tiến cùng mức tới mục tiêu.
5. **Decompose nếu quá phức tạp**: bước phức tạp → tách thành subflow, hoặc thành use case riêng (qua include/extend).
6. **Repeating steps**: viết "Repeat steps A through E until [condition]" thay vì cấu trúc loop kiểu lập trình.
7. **3-7 bước chính** trong normal flow. Quá dài → cần decompose.

### 2.4 Activity Diagram
**Mục đích**: mô tả luồng hoạt động (workflow) chi tiết hơn use case description, có decision/parallel.

**Thành phần UML chuẩn**:
- Initial node `(●)`, Final node `(◉)`
- Action / Activity (hình rounded rectangle)
- Decision/Merge (hình thoi)
- Fork/Join (thanh ngang) — biểu diễn parallel
- Swimlane / Partition — chia trách nhiệm theo actor/system
- Object node — dữ liệu trao đổi giữa các activity
- Control flow / Object flow (mũi tên)

**Quy trình tạo (Dennis)**:
1. Xác định scope của activity diagram (1 use case hay 1 process lớn).
2. Identify activities, control flows, decision points.
3. Identify parallel activities (nếu có).
4. Identify swimlanes (nếu cần phân vai).
5. Identify object flows (dữ liệu).
6. Refine và validate.

## 3. Mermaid limitations cho phase này
- **Use case diagram**: Mermaid không có cú pháp chuẩn UML use case. Có 2 lựa chọn:
  - Dùng `flowchart` với convention rõ ràng (actor là `(())`, use case là `[]`, boundary là `subgraph`).
  - Dùng PlantUML cho use case diagram thực sự (xem `notation-uml-mermaid.md`).
- **Activity diagram**: dùng `flowchart TD` của Mermaid là OK cho cơ bản, nhưng **không hỗ trợ swimlane chuẩn UML**. Khi cần swimlane → PlantUML.

## 4. Verification & Validation
Trước khi sang phase 2, walkthrough qua:
- Mỗi actor có ≥1 use case không?
- Mỗi use case có description đầy đủ 3 phần (overview/relationships/flow) không?
- Activity diagram có khớp với normal + alternate flow trong description không?
- Use case có dùng tên kỹ thuật (vd "call API") thay vì nghiệp vụ (vd "Borrow Books") không?

Chi tiết: `checklists/diagram-quality.md` mục B & C.

## 5. Anti-patterns thường gặp
- Use case đặt theo CRUD database ("Insert Patient", "Delete Order") → đây không phải mục tiêu nghiệp vụ.
- Use case description thiếu exception flow ở core flow.
- Activity diagram không có start/end rõ.
- Trộn lẫn essential và real trong cùng description (lúc viết chung chung, lúc đề cập "click button X").
- Dùng activity diagram để mô tả tương tác (đó là việc của sequence diagram).
