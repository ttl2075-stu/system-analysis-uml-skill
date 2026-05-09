# Diagram Quality Checklist

Chạy checklist này trước khi đóng mỗi phase. Mỗi mục fail → KHÔNG đóng phase.

## A. Checklist chung (áp dụng mọi diagram)

- [ ] Diagram có **tiêu đề** rõ ràng.
- [ ] Có ghi chú **mục đích** (1-2 câu) — diagram này trả lời câu hỏi gì.
- [ ] Thuật ngữ **nhất quán** với glossary của project.
- [ ] Một diagram **chỉ phục vụ 1 mục đích chính** (không nhồi nhiều viewpoint).
- [ ] Naming convention nhất quán (PascalCase cho class/actor, camelCase cho attr/op, etc.).

## B. Use Case Diagram

- [ ] Có **system boundary** rõ ràng.
- [ ] Mỗi actor có ≥1 use case.
- [ ] Mỗi use case có ≥1 actor primary.
- [ ] Use case đặt theo **động từ + bổ ngữ** (Borrow Books, Submit Order).
- [ ] Không dùng tên kỹ thuật cho use case nghiệp vụ ("Save to DB" sai).
- [ ] Quan hệ include/extend đúng nghĩa (include = luôn bao gồm; extend = mở rộng có điều kiện).
- [ ] Không có use case "lỏng lẻo" không kết nối với actor nào.
- [ ] Số use case phù hợp với scope (5-30 cho hệ thống vừa; >30 cần nhóm theo subsystem).

## C. Use Case Description

- [ ] Có đủ **8 trường overview** (Name, ID, Type, Importance, Primary Actor, Brief Desc, Trigger, Trigger Type).
- [ ] **Stakeholders and Interests**: ≥1 stakeholder ngoài primary actor.
- [ ] **Relationships** rõ (Include/Extend/Generalization).
- [ ] **Normal flow**: 3-7 bước, viết theo SVDPI.
- [ ] **Subflows** dùng đúng (chỉ khi 1 bước phức tạp).
- [ ] **Alternate / Exception flows** có cho UC importance High.
- [ ] **Preconditions / Postconditions** rõ.
- [ ] Bird's-eye view (không từ góc nhìn user/system riêng).
- [ ] Cùng level abstraction giữa các bước.

## D. Class Diagram

- [ ] Mỗi class có **≥1 attribute** hoặc **≥1 operation**.
- [ ] Class name là **danh từ số ít, PascalCase**.
- [ ] Attribute name **camelCase**, có type (analysis có thể không có visibility).
- [ ] Operation name **camelCase, bắt đầu bằng động từ**, có signature (design phase).
- [ ] **Multiplicity** có ý nghĩa nghiệp vụ (không lười `*` mọi nơi).
- [ ] Quan hệ phù hợp:
  - [ ] Association cho "biết về"
  - [ ] Aggregation cho "có một phần" (part tồn tại độc lập)
  - [ ] Composition cho "sở hữu" (part không tồn tại độc lập)
  - [ ] Generalization cho "is-a" thực sự (không dùng để share code)
- [ ] **Analysis class diagram** không có infrastructure class (Repository, DAO, Controller).
- [ ] **Design class diagram** có visibility, signature đầy đủ.
- [ ] Không có inheritance "rỗng" (subclass không bổ sung gì).

## E. CRC Cards

- [ ] Mỗi class trên class diagram có **CRC card tương ứng**.
- [ ] Mặt trước có đủ: Name, ID, Type, Description, Use Cases, Responsibilities, Collaborators.
- [ ] Mặt sau có đủ: Attributes, Generalization, Aggregation, Other Associations.
- [ ] Mỗi CRC có **≥1 use case liên quan** (Quy tắc 1 balancing).
- [ ] **Knowing responsibility** tương ứng với attribute hoặc relationship.
- [ ] **Doing responsibility** tương ứng với operation trên class diagram.
- [ ] Có collaborator cho responsibility cần phối hợp với class khác.

## F. Sequence Diagram

- [ ] Có UC + scenario rõ trong title.
- [ ] **Participants** sắp xếp theo thứ tự xuất hiện (left → right).
- [ ] Mỗi participant là actor hoặc class trên class diagram (không bịa).
- [ ] Mỗi message gọi **operation tồn tại** trên class diagram (Quy tắc 8 balancing).
- [ ] Có message khớp với **mỗi bước** trong use case description (Quy tắc 6 balancing).
- [ ] Có nhánh **alt/exception** cho exception flow.
- [ ] Return message chỉ vẽ khi cần thiết (không vẽ tất cả).
- [ ] Không bỏ qua bước orchestration (vd: Service layer) khi kiến trúc có.
- [ ] Self-message dùng có chủ đích, không tùy tiện.

## G. State Machine

- [ ] Class này thực sự cần state machine (lifecycle phức tạp, không phải CRUD đơn).
- [ ] Có **initial state** rõ.
- [ ] Có **final state** nếu object có lifecycle kết thúc.
- [ ] State name là **danh từ trạng thái** (Active, Closed) không phải động từ.
- [ ] Mỗi state có **mô tả** + tương ứng với giá trị attribute (Quy tắc 9 balancing).
- [ ] Mọi state **reachable** từ initial.
- [ ] Không có **black hole state** (vào không ra) trừ final.
- [ ] Không có **miracle state** (ra không vào) trừ initial.
- [ ] Mỗi transition có **trigger event** rõ.
- [ ] **Guard condition** dạng `[boolean]`.
- [ ] **Action** (nếu có) tương ứng với operation trên class diagram.

## H. Package / Component / Deployment

### Package
- [ ] Có **strategy phân chia** rõ (layer / subsystem / 2D matrix).
- [ ] Mỗi class thuộc **đúng 1 package** (Quy tắc 13 balancing).
- [ ] **Không có cyclic dependency** giữa các package.
- [ ] Tên package có ý nghĩa (không "package1", "module2").

### Component
- [ ] Mỗi component có **≥1 provided interface**.
- [ ] **Required interface** của A khớp với **provided interface** của B.
- [ ] Stereotype rõ (≪service≫, ≪library≫, ≪application≫).
- [ ] Operation trong interface tương ứng với class trên design class diagram (Quy tắc 14 balancing).
- [ ] Không có "God component".

### Deployment
- [ ] Có ≥1 environment (thường production).
- [ ] Mỗi node có ≥1 component host.
- [ ] **Communication path** có protocol và port rõ.
- [ ] Không lộ thông tin nhạy cảm (IP nội bộ, password).
- [ ] Stereotype phù hợp (≪device≫, ≪executionEnvironment≫).

## I. Activity Diagram

- [ ] Có **Initial node** và **Final node**.
- [ ] Mỗi decision có **≥2 nhánh** + label điều kiện.
- [ ] Có **≥1 nhánh exception** cho core flow nếu UC importance High.
- [ ] Không có activity "treo" (vào không ra hoặc ra không vào).
- [ ] Khớp với normal flow + alternate flow trong use case description (Quy tắc 7 balancing).
- [ ] **Object node** (nếu có) khớp với class trên class diagram (Quy tắc 3 balancing).
- [ ] **Swimlane** (nếu có) khớp với actor/system trên use case.

## J. Glossary Consistency

- [ ] Cùng 1 khái niệm dùng cùng 1 thuật ngữ xuyên suốt diagrams (vd: chọn "Member" thì không lúc thì "User" lúc thì "Customer").
- [ ] Domain term tiếng Việt/tiếng Anh nhất quán (chọn 1, tránh trộn).

## K. Anti-pattern Checklist (final sweep)

- [ ] Không có diagram "kể chuyện lan man" không có mục tiêu rõ.
- [ ] Không trộn analysis và design trong 1 diagram.
- [ ] Không có tên kỹ thuật thấp tầng cho UC nghiệp vụ.
- [ ] Không thiếu nhánh lỗi/ngoại lệ ở luồng quan trọng.
- [ ] Không có Mermaid "đúng cú pháp nhưng sai semantic" (gọi method không tồn tại, thứ tự trái business rule).
