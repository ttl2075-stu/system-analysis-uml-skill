# Phase 3 — Behavioral Modeling

> Nguồn: Dennis, Wixom & Tegarden — *Systems Analysis & Design with UML* (4th ed.), Chapter 6.

## 1. Mục tiêu phase
Mô tả **hành vi** hệ thống:
- Object tương tác với nhau như thế nào (sequence, communication).
- Object thay đổi trạng thái như thế nào (state machine).
- Class nào liên quan đến use case nào ở mức nào (CRUDE).

## 2. Artifacts của phase

### 2.1 Sequence Diagram

**Mục đích**: mô tả tương tác giữa các object **theo thời gian** cho 1 scenario cụ thể của use case.

**Thành phần**:
- **Actor / Object** (lifeline): hộp ở trên, đường đứt nét xuống dưới.
- **Execution occurrence** (activation bar): hình chữ nhật dài trên lifeline khi object đang xử lý.
- **Message**:
  - Synchronous (mũi tên đầy): `caller->>callee: method()`
  - Asynchronous (mũi tên mảnh): `caller->>callee: method()` (Mermaid không phân biệt rõ — dùng note).
  - Return (mũi tên đứt): `callee-->>caller: result`
  - Self-message: object gửi cho chính nó.
- **Frame** (Mermaid: `alt/opt/loop/par`): biểu diễn điều kiện, lặp, song song.

**Phân loại**:
- **Generic sequence diagram**: cho cả use case (mọi flow).
- **Instance sequence diagram**: cho 1 scenario cụ thể (1 main flow hoặc 1 alt flow).

**Quy trình tạo (Dennis)**:
1. Xác định scope: use case nào, scenario nào.
2. List các object/actor tham gia (lấy từ class diagram + use case description).
3. Sắp xếp object theo thứ tự xuất hiện (left → right).
4. Vẽ message theo thứ tự thời gian (top → bottom).
5. Bổ sung điều kiện (alt/opt) nếu là generic.
6. Validate: mỗi message phải tương ứng với 1 operation trên class diagram.

**Guidelines (Dennis — 6 quy tắc)**:
1. **Top-to-bottom + left-to-right**: message ở trên trước, object xuất hiện trước đặt bên trái.
2. **Tên nhất quán**: nếu actor và object đại diện cùng khái niệm (vd "Receptionist" actor và "Receptionist" object trong UI), đặt cùng tên.
3. **Justify message names**: tên method phải ý nghĩa, không quá kỹ thuật.
4. **Indicate condition trên message** (`[condition] method()`) khi cần.
5. **Use `*` cho repeat** thay vì vẽ nhiều message giống nhau.
6. **Don't show return** trừ khi giá trị return mang thông tin quan trọng — vẽ nhiều quá rối diagram.

### 2.2 Communication Diagram

**Mục đích**: thể hiện **mối quan hệ tương tác** giữa object — nhấn mạnh structural connection thay vì timing.

**So sánh với Sequence**:
- Sequence: **time-focused** (ai làm gì khi nào).
- Communication: **relationship-focused** (ai nói chuyện với ai).
- Hai diagram này **biểu diễn cùng 1 thông tin**, chỉ khác viewpoint. Thường chọn 1 trong 2.

**Thành phần**:
- Object/Actor (hình chữ nhật).
- Link (đường nối).
- Message (mũi tên kèm số thứ tự `1:`, `1.1:`, `2:` để biểu diễn sequence).

**Mermaid limitation**: Mermaid **không có** syntax chuẩn cho communication diagram. Dùng PlantUML, hoặc dùng `flowchart` với convention số thứ tự message.

### 2.3 Behavioral State Machine

**Mục đích**: mô tả vòng đời (lifecycle) của 1 instance class — đi qua các state nào, transition theo event nào.

**Khi nào dùng**: chỉ cho class có **lifecycle phức tạp** (vd: BookItem có Available/Borrowed/Reserved/Lost; Order có Draft/Submitted/Paid/Shipped/Delivered).

**Thành phần**:
- **State**: hình chữ nhật bo tròn — tập giá trị describe object tại 1 thời điểm.
- **Initial state**: `[*]` hoặc dấu chấm đầy.
- **Final state**: `[*]` hoặc dấu chấm có viền.
- **Transition**: mũi tên giữa state, label `event [guard] / action`.
  - **Event**: trigger gây ra transition.
  - **Guard**: điều kiện boolean phải đúng.
  - **Action**: hành động khi transition xảy ra.
- **Composite state**: state chứa state khác (substates).

**Quy trình tạo**:
1. Chọn class có lifecycle phức tạp.
2. List tất cả state của instance.
3. Xác định initial + final state.
4. List event có thể xảy ra trong lifetime.
5. Vẽ transition + guard + action.
6. Kiểm tra: không có **black hole state** (vào không ra) hoặc **miracle state** (ra không vào).

### 2.4 CRUDE Analysis

**Mục đích**: ma trận giúp validate độ tương tác giữa class và use case, gợi ý collaboration còn thiếu.

**CRUDE viết tắt**: **C**reate, **R**ead, **U**pdate, **D**elete, **E**xecute.

**Cấu trúc ma trận**:

| | Class A | Class B | Class C |
|---|---|---|---|
| Class A | — | C, U | R |
| Class B | R | — | E |
| Class C | — | R | — |

Mỗi ô chứa các action mà class hàng tác động lên class cột trong toàn bộ use case.

**Cách dùng**:
- Hàng/cột rỗng → class đó có thể không cần.
- Chỉ có R → class chỉ đọc, có thể là reference data.
- Có C/U/D ở nhiều cột → class này là "central" — kiểm tra responsibility có quá lớn không.

## 3. Mermaid support cho phase này
- Sequence diagram: **`sequenceDiagram`** — hỗ trợ tốt, có alt/opt/loop/par/note.
- State machine: **`stateDiagram-v2`** — hỗ trợ tốt, có composite state, fork/join.
- Communication diagram: **không có syntax chuẩn**. Dùng `flowchart` với label số thứ tự, hoặc PlantUML.
- CRUDE matrix: **bảng markdown thường**.

## 4. Verification & Validation
- Mỗi message trong sequence có khớp với operation trong class diagram không?
- Mỗi state trong state machine có liên quan đến giá trị attribute thay đổi không?
- Mỗi transition có trigger rõ không?
- Có dead-end state hoặc unreachable state không?
- CRUDE có row/col rỗng → cần xem lại class identification.

Chi tiết: `checklists/diagram-quality.md` mục E & F.

## 5. Anti-patterns
- Sequence diagram bỏ qua return message ngay cả khi return data quan trọng.
- State machine cho mọi class (chỉ class có lifecycle phức tạp mới cần).
- State name là động từ (Borrowing, Returning) thay vì danh từ trạng thái (Borrowed, Returned).
- Trộn sequence + state trong cùng diagram.
- Vẽ sequence diagram **đúng cú pháp Mermaid nhưng sai semantic** — vd: gọi method không có trong class diagram, hoặc thứ tự trái với business rule.
