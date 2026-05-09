# Balancing Models Checklist

> Theo Dennis et al. (4th ed., Chapter 7). Chạy **bắt buộc** trước khi sang phase tiếp theo hoặc đóng project.

Reference: `references/05-balancing-models.md`.

---

## Functional ↔ Structural

### Quy tắc 1: Class ↔ Use Case
- [ ] Mỗi **class** trên class diagram gắn với ≥1 use case.
- [ ] Mỗi **CRC card** có cột "Associated Use Cases" không rỗng.
- [ ] Mỗi **use case** có ≥1 class tham gia.

### Quy tắc 2: Activity/Event ↔ Responsibility/Operation
- [ ] Mỗi **bước** trong use case description tương ứng với ≥1 responsibility trên CRC.
- [ ] Mỗi **bước** có ≥1 operation trên class diagram để thực hiện.
- [ ] Mỗi **activity** trên activity diagram có class hoặc actor thực hiện.

### Quy tắc 3: Object Node ↔ Class/Attribute
- [ ] Mỗi **object node** trên activity diagram là instance của class hoặc là attribute của class nào đó.
- [ ] Object node "lạ" → cần thêm class hoặc xóa node.

### Quy tắc 4: Attribute/Association ↔ UC Subject/Object
- [ ] Mỗi **attribute** xuất hiện ở subject/object của ≥1 use case event.
- [ ] Mỗi **association** giữa class A-B xuất hiện ở event nào đó.
- [ ] Attribute "treo" không xuất hiện trong UC nào → có thực sự cần?

---

## Functional ↔ Behavioral

### Quy tắc 5: Use Case ↔ Sequence Diagram
- [ ] Mỗi **UC importance High** có ≥1 sequence diagram cho main flow.
- [ ] UC có alternate flow phức tạp → có sequence riêng cho alt flow.

### Quy tắc 6: UC Step ↔ Sequence Message
- [ ] Mỗi **bước** trong normal flow có ≥1 message trong sequence.
- [ ] Mỗi **bước** trong alt/exception flow được thể hiện qua alt frame.

### Quy tắc 7: Activity ↔ Sequence
- [ ] Activity diagram và sequence diagram của cùng UC có **cùng business logic**.
- [ ] Số bước/decision giữa 2 diagram tương đương.

---

## Structural ↔ Behavioral

### Quy tắc 8: Class Operation ↔ Sequence Message
- [ ] Mỗi **message** trong sequence gọi operation **tồn tại** trên class diagram.
- [ ] Operation chưa có → bổ sung vào class diagram.
- [ ] Class diagram có operation **không bao giờ được gọi** → còn cần không?

### Quy tắc 9: Class Attribute ↔ State
- [ ] Mỗi **state** trong state machine tương ứng với giá trị attribute trên class.
- [ ] State không khớp giá trị → bổ sung attribute hoặc xóa state.

### Quy tắc 10: Class with Lifecycle ↔ State Machine
- [ ] Class có **status thay đổi nhiều** theo event → có state machine.
- [ ] Class chỉ CRUD đơn → KHÔNG cần state machine.

### Quy tắc 11: CRUDE ↔ Sequence
- [ ] Mỗi cell trong CRUDE matrix khớp với message trong sequence diagram.
- [ ] Class trong CRUDE có row/col rỗng → kiểm tra lại class identification.

---

## Analysis ↔ Design

### Quy tắc 12: Analysis Class ↔ Design Class
- [ ] Mỗi **analysis class** có **design class tương ứng**.
- [ ] Design class có thêm: visibility, signature đầy đủ, có thể thêm boundary/control/utility class.
- [ ] Không có analysis class bị "mất" trong design.

### Quy tắc 13: Class ↔ Package
- [ ] Mỗi class **nằm trong đúng 1 package**.
- [ ] Package phụ thuộc nhau khớp với association giữa class.
- [ ] Không có cyclic dependency.

### Quy tắc 14: Component ↔ Class
- [ ] Mỗi component gom **các class có cohesion cao** (thường là 1 package).
- [ ] **Provided interface** của component = subset operation public của class trong component.
- [ ] **Required interface** khớp với class công cụ ngoài component.

---

## Cross-cutting

### Glossary Consistency
- [ ] Cùng 1 khái niệm dùng cùng 1 thuật ngữ xuyên suốt mọi artifact.
- [ ] Tiếng Việt / tiếng Anh nhất quán (không trộn).

### Traceability Coverage
- [ ] Master traceability matrix đầy đủ row cho mọi UC.
- [ ] UC importance High → đủ Class, Operation, Sequence, Test.
- [ ] Coverage = Y có nghĩa test pass thật ở lần chạy gần nhất.

### Gap Closure
- [ ] Có gap report kèm theo nếu balancing fail.
- [ ] Gap P1 có owner và action plan.

---

## Walkthrough Recommendation

Sau khi tự check xong, vẫn nên **walkthrough với ≥1 reviewer khác**:
1. Author trình bày artifact.
2. Reviewer đặt câu hỏi và chỉ ra điểm mơ hồ/sai.
3. Author **không sửa tại chỗ** — chỉ ghi nhận.
4. Sau walkthrough, sửa rồi review lại nếu cần.

> "Hearing the representation helps the analyst to see the representation more completely." — Dennis et al.
