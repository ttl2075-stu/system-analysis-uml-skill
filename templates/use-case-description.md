# Use Case Description — Template

> Theo Dennis et al. (4th ed., Chapter 4). Sao chép template này và điền cho từng use case.

---

## Overview Information

| Field | Value |
|---|---|
| **Use Case Name** | (động từ + bổ ngữ, vd: "Borrow Books") |
| **ID** | UC-NNN |
| **Type** | Detail / Overview · Essential / Real |
| **Importance Level** | High / Medium / Low |
| **Primary Actor** | (actor trigger use case) |
| **Brief Description** | (1 câu mô tả) |
| **Trigger** | (sự kiện kích hoạt — external/temporal) |
| **Trigger type** | External / Temporal |

## Stakeholders and Interests
- **<Stakeholder 1>** — wants/needs:
- **<Stakeholder 2>** — wants/needs:
- ...

## Relationships
- **Association**: (actors liên quan)
- **Include**: (use case bị include)
- **Extend**: (use case mở rộng use case này)
- **Generalization**: (use case cha, nếu có)

## Normal Flow of Events
1. <Subject> <verb> <direct object> [<preposition> <indirect object>].
2. ...
3. ...

> Quy tắc: 3-7 bước, SVDPI sentences, bird's-eye view, cùng level abstraction.

## Subflows
**S-1: <Subflow Name>**
1. ...
2. ...

**S-2: <Subflow Name>**
1. ...
2. ...

> Dùng subflow khi 1 bước trong normal flow quá phức tạp (vd bước 3 có nhiều case con).

## Alternate / Exceptional Flows

**A-1: <điều kiện thay thế>** (tham chiếu bước nào trong normal flow)
1. ...
2. Quay về bước X của normal flow.

**E-1: <điều kiện ngoại lệ>**
1. ...
2. Use case kết thúc với failure.

> Quy tắc: mỗi use case importance High **bắt buộc** có ít nhất 1 alternate hoặc exception flow.

## Preconditions
- <điều kiện phải thỏa trước khi use case bắt đầu>

## Postconditions
- <điều kiện thỏa sau khi use case kết thúc thành công>

## Notes / Issues
- [OPEN] <câu hỏi chưa rõ>
- ...

---

## Validation checklist (chạy trước khi đóng UC này)

- [ ] Tên use case là động từ + bổ ngữ, không phải kỹ thuật ("Save Data" sai).
- [ ] Có đủ Overview Information (8 field).
- [ ] Có ≥1 stakeholder ngoài primary actor.
- [ ] Normal flow 3-7 bước, viết SVDPI.
- [ ] Importance High → có ≥1 exception flow.
- [ ] Pre/Post conditions rõ ràng.
- [ ] Bước trong flow không reference đến UI/database cụ thể (nếu là Essential).
- [ ] Mỗi bước có thể trace tới ≥1 responsibility/operation trên class diagram (kiểm tra ở phase 2).
