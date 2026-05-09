# Phase 2 — Structural Modeling

> Nguồn: Dennis, Wixom & Tegarden — *Systems Analysis & Design with UML* (4th ed.), Chapter 5.

## 1. Mục tiêu phase
Mô tả **cấu trúc thông tin** mà hệ thống quản lý:
- Những đối tượng (object/class) hệ thống cần biết.
- Quan hệ giữa chúng.

## 2. Artifacts của phase

### 2.1 Object Identification (4 kỹ thuật của Dennis)

#### 2.1.1 Textual Analysis
Đọc use case description, áp dụng quy tắc:
- **Common noun** → có thể là class.
- **Proper noun** → có thể là instance.
- **Doing verb** → có thể là operation.
- **Being verb** (is, has) → có thể là quan hệ generalization/aggregation.
- **Stative verb** → có thể là quan hệ.
- **Adjective** → có thể là attribute.
- **Adverb** → có thể là attribute của operation.

#### 2.1.2 Brainstorming
Nhóm phát triển + user tự do nêu các candidate class. Sau đó lọc.

#### 2.1.3 Common Object Lists
Theo Ross: 6 nhóm để rà soát:
- Physical objects (book, vehicle…)
- Specifications/designs/descriptions
- Roles played (member, librarian…)
- Incidents (events, transactions)
- Interactions
- People/Places/Things

#### 2.1.4 Patterns
Tham khảo analysis patterns có sẵn (Coad, Eriksson-Penker, Fowler, Hay).

### 2.2 CRC Cards (Class–Responsibility–Collaboration)

**Vai trò trong quy trình**: CRC là **bước trung gian bắt buộc** giữa object identification và class diagram (Dennis).

**Phân loại trách nhiệm**:
- **Knowing responsibilities**: thông tin instance phải biết → tương ứng **attributes** + **relationships**.
- **Doing responsibilities**: hành vi instance thực hiện → tương ứng **operations**.

**Khái niệm collaboration**:
- **Client object**: gửi request.
- **Server object**: nhận request và thực hiện.
- **Contract**: ràng buộc giữa client và server.

**Cấu trúc 2 mặt** (xem `templates/crc-card.md`):

**Mặt trước**:
- Class name + ID + Type (concrete/abstract; domain/utility/persistence/etc.)
- Description
- Associated use cases
- Responsibilities (knowing + doing)
- Collaborators (cho từng responsibility cần phối hợp)

**Mặt sau**:
- Attributes (kèm type)
- Relationships:
  - Generalization (a-kind-of)
  - Aggregation/Composition (has-parts)
  - Other associations

**Role-Playing CRC Cards**: thành viên team cầm card, đóng vai class, "gửi message" cho nhau theo use case scenario → phát hiện responsibility thiếu hoặc thừa.

### 2.3 Class Diagram

**Thành phần**:
- **Class**: tên + attributes + operations.
- **Attribute notation**: `visibility name : type [= defaultValue]`
  - Visibility: `+` public, `-` private, `#` protected, `~` package.
- **Operation notation**: `visibility name(param: type) : returnType`
- **Relationships**:
  - **Association**: đường thẳng + multiplicity (1, 0..1, *, 1..*) + role + name.
  - **Aggregation** (◇—): "has-a", part có thể tồn tại độc lập.
  - **Composition** (◆—): "owns-a", part không tồn tại độc lập với whole.
  - **Generalization** (—▷): inheritance.
  - **Dependency** (- - ->): client phụ thuộc supplier.
  - **Realization** (- -▷): class implements interface.

**Quy trình tạo**:
1. Bắt đầu từ CRC cards đã ổn định.
2. Mỗi card → 1 class.
3. Knowing responsibilities → attributes.
4. Doing responsibilities → operations.
5. Collaborators → associations (xác định multiplicity).
6. Generalization từ mặt sau CRC.
7. Simplify: gộp class trùng lặp, tách class quá to.

### 2.4 Object Diagram
**Mục đích**: snapshot tại 1 thời điểm — instance cụ thể với giá trị cụ thể, dùng để minh họa hoặc test class diagram.

**Lưu ý Mermaid**: Mermaid không có syntax chuẩn cho object diagram. Dùng PlantUML (`@startuml ... @enduml` với `object Name { ... }`) hoặc bảng markdown.

## 3. Quy tắc đặt tên (Dennis)
- Class name: **danh từ số ít, PascalCase** (Patient, BookItem, BorrowTransaction).
- Attribute name: **camelCase**, mô tả ý nghĩa nghiệp vụ.
- Operation name: **camelCase**, bắt đầu bằng động từ (calculateFine, validateMember).
- Tránh tên kỹ thuật ngầm hiểu (data, info, thing, manager… một mình) trừ khi rõ context.

## 4. Verification & Validation cho phase này
Walkthrough qua:
- Mỗi class có ≥1 attribute và ≥1 responsibility không?
- Multiplicity hợp lý nghiệp vụ chưa?
- Có inheritance "rỗng" (subclass không bổ sung gì so với superclass) không?
- Có class nào không có collaborator → có thực sự cần không?
- Class diagram có khớp với CRC cards không (4 quy tắc balancing — xem `references/05-balancing-models.md`)?

Chi tiết: `checklists/diagram-quality.md` mục D.

## 5. Anti-patterns
- Đưa **infrastructure class** (DAO, Repository, Controller) vào class diagram analysis — đây là design concerns, không phải domain.
- Class chỉ có data, không có behavior (anemic domain) → cần xem có phải đúng "data class" hay đang thiếu responsibility.
- Inheritance dùng để "share code" thay vì biểu diễn quan hệ "is-a" thực sự.
- Multiplicity lười (`*` mọi nơi) thay vì suy nghĩ ràng buộc nghiệp vụ thật.
- Trộn analysis class diagram với design class diagram (analysis: chưa có visibility, getter/setter; design: có đầy đủ).
