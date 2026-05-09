# Sequence Design — Template

## Mục đích
Mô tả tương tác theo thời gian giữa các object/actor cho 1 scenario của use case.

## Scope
- **Use Case**: <UC-ID + tên>
- **Scenario**: <main flow / alt flow / exception flow — chọn 1>
- **Type**:
  - [ ] **Generic sequence diagram**: cho cả use case (có alt/opt frame).
  - [ ] **Instance sequence diagram**: cho 1 scenario cụ thể.

## Participants

| Participant | Type | Class on Class Diagram | Role |
|---|---|---|---|
| <name> | actor / object | <ClassName hoặc —> | <vai trò trong scenario> |
| ... | | | |

> Quy tắc: tham gia phải có theo thứ tự xuất hiện (left → right).

## Sequence Diagram
> Mermaid template: `templates/mermaid/sequence-diagram.mmd`

## Messages Inventory

| # | From | To | Message | Return | Operation in Class Diagram |
|---|---|---|---|---|---|
| 1 | Actor | UI | <action> | — | — |
| 2 | UI | Controller | <method()> | <result> | <Class.method()> |
| ... | | | | | |

> Quy tắc: mỗi message phải gọi đến **operation tồn tại** trên class diagram (Quy tắc 8 balancing).

## Conditions / Loops / Parallel
- **alt** <condition>: <description>
- **opt** <condition>: <description>
- **loop** <condition>: <description>
- **par**: <description>

## Notes
- KHÔNG vẽ return cho mọi message — chỉ vẽ khi return value mang thông tin quan trọng.
- KHÔNG bỏ qua bước orchestration (vd: Controller gọi Service) khi kiến trúc thực sự có layer đó.
- Object xuất hiện trước đặt bên trái.

## Validation
- [ ] Mỗi participant có trên class diagram (hoặc là actor).
- [ ] Mỗi message khớp với operation/method trên class diagram.
- [ ] Có message khớp với mỗi bước trong use case description (Quy tắc 6 balancing).
- [ ] Có nhánh lỗi/alt cho exception flow.
- [ ] Thứ tự message hợp lý nghiệp vụ.
