# CRC Card — Template

> Theo Dennis et al. (4th ed., Chapter 5). Mỗi class 1 thẻ CRC với 2 mặt.

---

## Front Side (Mặt trước)

| | | |
|---|---|---|
| **Class Name**: <ClassName> | **ID**: CRC-NN | **Type**: Concrete / Abstract |
|  |  | Domain / Utility / Persistence / GUI |
| **Description**: <1-2 câu mô tả vai trò của class trong hệ thống> | | |
| **Associated Use Cases**: UC-001, UC-002, ... | | |

| **Responsibilities** | **Collaborators** |
|---|---|
| <Responsibility 1 — knowing or doing> | <Class A, Class B> |
| <Responsibility 2> | <Class C> |
| <Responsibility 3> | — |
| ... | ... |

> **Knowing responsibilities**: thông tin instance phải biết → sẽ thành **attributes** trên class diagram.
> **Doing responsibilities**: hành vi instance phải làm → sẽ thành **operations** trên class diagram.
> **Collaborator** trống: không cần phối hợp với class khác để hoàn thành responsibility đó.

---

## Back Side (Mặt sau)

### Attributes
| Name | Type | Description |
|---|---|---|
| <attributeName> | String / Integer / Date / Money / ... | <ý nghĩa nghiệp vụ> |
| ... | ... | ... |

### Relationships

**Generalization (a-kind-of)**:
- <Parent class — class này kế thừa từ>

**Aggregation / Composition (has-parts)**:
- <Part class> [multiplicity] — <semantic>

**Other Associations**:
- <Other class> [multiplicity] — <role / nature of association>

---

## Validation checklist (chạy sau khi tạo CRC)

- [ ] Tên class là danh từ số ít, PascalCase.
- [ ] Có ≥1 responsibility (knowing hoặc doing).
- [ ] Có ≥1 use case liên quan (Quy tắc 1 balancing).
- [ ] Mỗi knowing responsibility tương ứng với attribute hoặc relationship trên mặt sau.
- [ ] Mỗi doing responsibility cần collaborator → đã list collaborator.
- [ ] Attributes không trùng với attributes của parent class (nếu có generalization).
- [ ] Multiplicity hợp lý nghiệp vụ (không lười dùng `*` mọi nơi).

---

## Role-playing CRC (Dennis recommendation)

Sau khi có bộ CRC, làm role-play:
1. Mỗi thành viên team cầm 1 CRC card, "đóng vai" class đó.
2. Walk through main flow của 1 use case quan trọng.
3. Khi 1 class cần "gọi" class khác, người cầm card phải "yêu cầu" người đó thực hiện.
4. Phát hiện: responsibility thiếu, collaborator thiếu, class không cần thiết.
5. Update CRC + class diagram theo phát hiện.
