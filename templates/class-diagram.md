# Class Diagram — Template

## Mục đích
Mô hình hóa cấu trúc các đối tượng nghiệp vụ (analysis) hoặc đối tượng triển khai (design).

## Type
- [ ] **Analysis class diagram**: chỉ domain class, chưa có visibility, chưa có getter/setter.
- [ ] **Design class diagram**: có domain + boundary + control + entity + utility, có visibility, signature đầy đủ.

## Bounded Context
> Phạm vi nghiệp vụ class diagram này phục vụ: <subsystem name hoặc context>

## Class Diagram
> Template Mermaid: `templates/mermaid/class-diagram.mmd`

## Class Inventory

| Class | Type | Stereotype | Description |
|---|---|---|---|
| <ClassName> | concrete/abstract | ≪entity≫/≪control≫/≪boundary≫/— | <vai trò> |

## Relationships

| From | To | Type | Multiplicity | Role/Name |
|---|---|---|---|---|
| <A> | <B> | Association | 1..* | has |
| <A> | <C> | Aggregation | 1..1 | contains |
| <A> | <D> | Composition | 1..1 | owns |
| <Sub> | <Super> | Generalization | — | inherits |

## Domain Rules / Invariants
- <Rule 1: vd "BorrowTransaction.dueDate phải sau borrowDate">
- <Rule 2>

## Notes
- KHÔNG đưa infrastructure class (Repository, DAO, Controller) vào analysis class diagram.
- Multiplicity phải có ý nghĩa nghiệp vụ — không lười `*` mọi nơi.
- Nếu attribute là enum → định nghĩa enum value rõ.

## Validation
- [ ] Mỗi class có ≥1 attribute hoặc ≥1 operation.
- [ ] Mỗi class trong diagram có CRC card tương ứng (Quy tắc 1 balancing).
- [ ] Mỗi class có liên quan tới ≥1 use case (Quy tắc 1).
- [ ] Multiplicity hợp lý nghiệp vụ.
- [ ] Không có inheritance "rỗng" (subclass không bổ sung gì).
- [ ] Không trộn analysis + design (visibility, getter/setter chỉ có trong design).
- [ ] Naming: PascalCase cho class, camelCase cho attribute/operation.
