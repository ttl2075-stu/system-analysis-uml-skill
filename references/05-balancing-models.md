# Balancing Models — Verification & Validation

> Nguồn: Dennis et al. (4th ed.), Chapter 7 "Moving on to Design".

Đây là phần **quan trọng nhất** của OOAD và cũng là phần dễ bị bỏ qua nhất. Phân tích-thiết kế UML không phải là **vẽ rời rạc** từng loại sơ đồ — mà là tạo một **mạng lưới mô hình nhất quán**.

## 1. Triết lý cân bằng

> "The object-oriented analysis models are highly interrelated… The process of ensuring the consistency among them is known as **balancing the models**." — Dennis et al.

Bốn nhóm mô hình phải nhất quán với nhau:
- **Functional**: use case diagram, use case description, activity diagram.
- **Structural**: CRC card, class diagram, object diagram.
- **Behavioral**: sequence diagram, communication diagram, state machine, CRUDE.
- **Design**: package, component, deployment, design class.

## 2. Functional ↔ Structural (4 quy tắc Dennis)

### Quy tắc 1: Class ↔ Use Case
- Mỗi **class** trên class diagram và mỗi **CRC card** phải gắn với **ít nhất 1 use case**, và ngược lại mỗi use case phải có ít nhất 1 class tham gia.
- **Cách check**: cột "Associated Use Cases" trên CRC card không được rỗng.

### Quy tắc 2: Activity/Event ↔ Responsibility/Operation
- Mỗi **activity** trên activity diagram và mỗi **event** (bước) trong use case description phải tương ứng với **ít nhất 1 responsibility** trên CRC và **ít nhất 1 operation** trên class diagram.
- **Cách check**: lấy bước use case description → tìm class nào "làm" bước đó → confirm class đó có operation tương ứng.

### Quy tắc 3: Object Node ↔ Class/Attribute
- Mỗi **object node** trên activity diagram phải tương ứng với **instance của class** (object) hoặc **attribute** của 1 class.
- **Cách check**: nếu object node không match → hoặc thiếu class trên class diagram, hoặc object node thừa.

### Quy tắc 4: Attribute/Association ↔ Use Case Subject/Object
- Mỗi **attribute** và **association** trên CRC/class diagram nên tương ứng với **subject hoặc object** của event nào đó trong use case description.
- **Cách check**: attribute không xuất hiện trong bất kỳ use case description nào → có thực sự cần?

## 3. Functional ↔ Behavioral (3 quy tắc)

### Quy tắc 5: Use Case ↔ Sequence Diagram
- Mỗi **use case** quan trọng (importance: high) phải có **ít nhất 1 sequence diagram** (cho main flow).
- Use case quan trọng có nhiều flow → có thể có nhiều sequence diagram.

### Quy tắc 6: Use Case Step ↔ Sequence Message
- Mỗi **bước** trong normal/alternate flow của use case description phải tương ứng với **ít nhất 1 message** trên sequence diagram.

### Quy tắc 7: Activity ↔ Sequence
- Activity diagram và sequence diagram của cùng use case phải biểu diễn **cùng business logic**, chỉ khác viewpoint.

## 4. Structural ↔ Behavioral (4 quy tắc)

### Quy tắc 8: Class Operation ↔ Sequence Message
- Mỗi **message** trên sequence diagram phải gọi đến **operation tồn tại** trong class diagram.
- Operation chưa có → bổ sung vào class diagram.

### Quy tắc 9: Class Attribute ↔ State
- **State** trong state machine phải tương ứng với **giá trị của 1 hoặc nhiều attribute** trên class diagram.
- Vd: state "Borrowed" tương ứng `BookItem.status = "borrowed"`.

### Quy tắc 10: Class with Lifecycle ↔ State Machine
- Class có lifecycle phức tạp (status thay đổi nhiều lần theo event) → phải có state machine.
- Class chỉ có CRUD đơn giản → không cần state machine.

### Quy tắc 11: CRUDE ↔ Sequence
- CRUDE matrix phải khớp với tổng hợp tất cả sequence diagram (mỗi message trong sequence là 1 cell trong CRUDE).

## 5. Analysis ↔ Design (3 quy tắc)

### Quy tắc 12: Analysis Class ↔ Design Class
- Mỗi **analysis class** phải có **design class tương ứng** (có thể đổi tên, thêm visibility, getter/setter).
- Design class có thể có thêm class infra (boundary, control, utility) không có trong analysis.

### Quy tắc 13: Class ↔ Package
- Mỗi class phải nằm trong **đúng 1 package**.
- Package phụ thuộc nhau → tương ứng dependency giữa class.

### Quy tắc 14: Component ↔ Class
- Mỗi component phải gom **các class có cohesion cao** (cùng package thường mapping 1-1 với component).
- Provided interface của component = operation public của class trong component.

## 6. Walkthrough — phương pháp V&V chính

Theo Dennis, **walkthrough** là cách V&V hiệu quả nhất:

**Quy trình**:
1. Author trình bày từng artifact cho 1 nhóm reviewer (3-5 người).
2. Reviewer đặt câu hỏi và phát hiện lỗi.
3. Author **không sửa lỗi tại chỗ** — chỉ ghi nhận.
4. Sau walkthrough, author sửa và quay lại review nếu cần.

**Vai trò**:
- **Presenter**: author trình bày.
- **Coordinator**: điều phối.
- **Scribe**: ghi lỗi/issue.
- **Reviewer**: đặt câu hỏi.

**Tip**: kể cả tự walkthrough (đọc to artifact của chính mình) cũng giúp phát hiện lỗi rất hiệu quả ("hearing it helps you see it more completely" — Dennis).

## 7. Khi nào quay lại sửa mô hình cũ?

Quy trình OOAD **không tuyến tính**. Trong các tình huống sau, phải quay lại:
- Khi vẽ sequence diagram phát hiện class thiếu operation → sửa class diagram.
- Khi role-play CRC phát hiện class thiếu collaborator → sửa CRC + class diagram.
- Khi vẽ state machine phát hiện attribute thiếu → sửa class diagram.
- Khi vẽ activity diagram phát hiện flow chưa rõ → sửa use case description.
- Khi user feedback có yêu cầu mới → sửa use case → cascading update.

**Quan trọng**: ghi lại mỗi lần update vào "decision log" hoặc commit message để tránh drift.

## 8. Checklist tổng hợp

Xem `checklists/balancing-models.md` để có checklist từng dòng tick được.
