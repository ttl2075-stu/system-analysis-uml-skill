# Gap Report — Template

## Mục đích
Liệt kê các điểm thiếu/yếu phát hiện trong quá trình phân tích-thiết kế, kèm priority và action plan.

## Categories
- **Requirements gap**: thiếu use case, actor, hoặc business rule.
- **Analysis gap**: thiếu class, CRC, hoặc balancing inconsistency.
- **Behavior gap**: thiếu sequence, state, hoặc CRUDE coverage.
- **Design gap**: thiếu component interface, NFR measurable, deployment topology.
- **Traceability gap**: row/col rỗng trong matrix.

## Gap Inventory

| Gap ID | Category | Description | Impact | Priority | Proposed Action | Owner | Status |
|---|---|---|---|---|---|---|---|
| GAP-001 | Requirements | UC-005 không có exception flow | High — UC core không complete | P1 | Phỏng vấn business để bổ sung | TBD | Open |
| GAP-002 | Traceability | Không có integration test cho UC-003 | Medium | P2 | Viết test | TBD | Open |
| ... | | | | | | | |

## Priority Definition
- **P1 — Must fix**: blocker cho release / phase tiếp.
- **P2 — Should fix**: cải thiện chất lượng đáng kể.
- **P3 — Nice to have**: không blocking.

## Status Values
- **Open**: chưa xử lý.
- **In Progress**: đang xử lý.
- **Resolved**: đã xử lý.
- **Deferred**: hoãn (kèm lý do).
- **Closed**: đã verify hoặc không còn relevant.

## Summary

| Priority | Open | In Progress | Resolved | Total |
|---|---|---|---|---|
| P1 | | | | |
| P2 | | | | |
| P3 | | | | |
