# State Model — Template

## Mục đích
Mô tả vòng đời (lifecycle) của 1 instance class — đi qua các state nào, transition theo event nào.

## Scope
- **Class**: <ClassName trên class diagram>
- **Why state machine**: lifecycle phức tạp, status thay đổi theo nhiều event.

> KHÔNG vẽ state machine cho class chỉ có CRUD đơn giản.

## State Machine
> Mermaid template: `templates/mermaid/state-machine.mmd`

## States Inventory

| State | Description | Related Attribute Value(s) |
|---|---|---|
| <StateName> | <object đang trong state này có ý nghĩa gì> | <vd: status = "available"> |
| ... | | |

> Quy tắc: state name là **danh từ trạng thái** (Available, Borrowed, Overdue), KHÔNG phải động từ ("Borrowing").

## Transitions

| From | To | Event (Trigger) | Guard | Action |
|---|---|---|---|---|
| <StateA> | <StateB> | <event name> | [<condition>] | <action / op() trên class> |
| ... | | | | |

> Format Mermaid: `StateA --> StateB: event [guard] / action`

## Initial / Final States
- **Initial**: <state object bắt đầu>
- **Final** (nếu có): <state object kết thúc lifecycle>

## Validation
- [ ] Có initial state.
- [ ] Mọi state đều reachable từ initial state.
- [ ] Không có **black hole state** (vào không ra) trừ final state.
- [ ] Không có **miracle state** (ra không vào) trừ initial state.
- [ ] Mỗi transition có trigger (event) rõ.
- [ ] Guard condition viết dưới dạng `[boolean expression]`.
- [ ] Action (nếu có) tương ứng với operation trên class diagram.
- [ ] State tương ứng với giá trị attribute trên class diagram (Quy tắc 9 balancing).
