# Activity Model — Template

## Mục đích
Mô tả luồng hoạt động (workflow) của 1 use case hoặc 1 business process.

## Scope
- **Use Case / Process**: <UC-ID hoặc tên process>
- **Level**: business / system / detailed
- **Swimlanes** (nếu có): <list actor/system tham gia>

## Activity Diagram
> Mermaid template: xem `templates/mermaid/activity-flow.mmd`.
> PlantUML cho swimlane: xem `references/notation-uml-mermaid.md`.

## Activities List

| Activity | Actor/System | Input | Output | Notes |
|---|---|---|---|---|
| <Activity 1> | <Actor> | <data in> | <data out> | |
| <Activity 2> | | | | |

## Decision Points
| Decision | Condition | Outcome True | Outcome False |
|---|---|---|---|
| <Decision 1> | <boolean condition> | <next activity> | <next activity> |

## Object Flows (nếu có)
| Object | From Activity | To Activity | State Change |
|---|---|---|---|
| <Order> | <Submit> | <Validate> | Pending → Validated |

## Validation
- [ ] Có Initial node và Final node rõ.
- [ ] Mỗi decision có ≥2 nhánh + label điều kiện.
- [ ] Có ≥1 nhánh exception cho core flow (nếu UC importance High).
- [ ] Không có activity "treo" (vào không ra hoặc ra không vào).
- [ ] Khớp với Normal Flow + Alternate Flow trong use case description tương ứng.
- [ ] Object node (nếu có) khớp với class trên class diagram (kiểm tra ở balancing).
