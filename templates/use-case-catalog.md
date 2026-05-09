# Use Case Catalog — Template

## Mục đích
Liệt kê toàn bộ use case của hệ thống, cho phép xem nhanh phạm vi và prioritize.

## Catalog Table

| UC ID | Use Case Name | Primary Actor | Type | Importance | Brief Description | Status |
|---|---|---|---|---|---|---|
| UC-001 | <verb + noun> | <Actor> | Detail/Essential | High/Medium/Low | <1 câu> | Draft/Reviewed/Approved |
| UC-002 | | | | | | |
| ... | | | | | | |

## Actors Reference

| Actor ID | Actor Name | Type | Description |
|---|---|---|---|
| A-001 | <name> | Primary/Secondary | <vai trò> |
| ... | | | |

## Use Case Diagram
> Tham khảo `templates/mermaid/use-case-overview.mmd` cho diagram template.

## Notes
- Use case không phải CRUD đơn thuần. "Insert User" không phải UC nghiệp vụ.
- Nếu một actor không có UC nào → có thực sự là actor không?
- Nếu một UC không có actor primary → ai trigger?
- Nếu hệ thống >30 UC → cân nhắc nhóm theo subsystem.

## Validation
- [ ] Mỗi UC có verb + noun.
- [ ] Mỗi actor có ≥1 UC primary.
- [ ] Mỗi UC có ≥1 actor primary.
- [ ] Importance được đánh giá (không "TBD" hết).
- [ ] Use case overview diagram khớp với catalog.
