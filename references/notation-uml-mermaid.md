# UML Notation — Mermaid & PlantUML Reference

## 1. Triết lý
- **Default**: Mermaid (render được trực tiếp trong Markdown, GitHub, hầu hết viewer).
- **Fallback**: PlantUML khi Mermaid không hỗ trợ (use case diagram chuẩn UML, communication diagram, object diagram).

## 2. Bảng tra cứu nhanh

| UML Diagram | Mermaid syntax | PlantUML syntax | Ghi chú |
|---|---|---|---|
| Use Case | `flowchart` (workaround) | `@startuml ... @enduml` với `actor`, `usecase`, `:UC1:` | Mermaid không có UC chuẩn; PlantUML là chuẩn |
| Activity | `flowchart TD` | `@startuml ... :Action;` | Mermaid OK cơ bản; thiếu swimlane |
| Class | `classDiagram` | `@startuml ... class A {} @enduml` | Cả hai đều tốt |
| Object | (không có chuẩn) | `@startuml ... object obj1 ... @enduml` | Dùng PlantUML |
| Sequence | `sequenceDiagram` | `@startuml ... A->B: msg @enduml` | Cả hai đều rất tốt |
| Communication | (không có chuẩn) | `@startuml ... A "1: msg" --> B @enduml` | Dùng PlantUML hoặc bảng |
| State | `stateDiagram-v2` | `@startuml ... [*] --> A @enduml` | Cả hai đều tốt |
| Package | `flowchart` với `subgraph` | `@startuml package "P1" {} @enduml` | PlantUML chuẩn hơn |
| Component | `flowchart` với `subgraph` | `@startuml component A @enduml` | PlantUML chuẩn hơn |
| Deployment | `flowchart` với `subgraph` | `@startuml node "Server" {} @enduml` | PlantUML chuẩn hơn |

## 3. Quy ước đặt tên (áp dụng mọi diagram)
- **Actor / Role**: PascalCase hoặc nhãn tự nhiên (Member, Librarian, AdminUser).
- **Use case / Action**: động từ + bổ ngữ (Borrow Books, Submit Order).
- **Class / Entity**: PascalCase, danh từ số ít (Patient, BookItem, BorrowTransaction).
- **Attribute**: camelCase (firstName, dueDate, totalAmount).
- **Operation/Method**: camelCase, bắt đầu bằng động từ (calculateFine(), validateMember()).
- **State**: danh từ trạng thái (Available, Reserved, Overdue) — KHÔNG phải động từ ("Borrowing" sai, "Borrowed" đúng).
- **Event** (transition trigger): động từ hoặc danh từ sự kiện (borrowRequested, paymentReceived).
- **Package**: PascalCase hoặc lowercase với dấu chấm (CatalogManagement hoặc catalog.management).
- **Component**: PascalCase với stereotype ≪component≫.
- **Glossary nhất quán**: nếu đã chọn "Member" thì xuyên suốt là "Member", không khi nào "User" khi khác "Customer".

## 4. Mermaid examples chuẩn

### 4.1 Use Case Diagram (workaround với flowchart)
```mermaid
flowchart LR
  subgraph SystemBoundary [System]
    UC1[Borrow Books]
    UC2[Return Books]
    UC3[Reserve Book]
    UC4[Validate Member]
  end
  Member((Member)) --> UC1
  Member --> UC2
  Member --> UC3
  Librarian((Librarian)) --> UC1
  Librarian --> UC2
  UC1 -. include .-> UC4
  UC2 -. include .-> UC4
```

### 4.2 Activity Diagram
```mermaid
flowchart TD
  Start([Start]) --> A[Patient contacts office]
  A --> B{Existing patient?}
  B -- No --> C[Register new patient]
  B -- Yes --> D[Look up record]
  C --> E[Schedule appointment]
  D --> E
  E --> F{Slot available?}
  F -- No --> G[Suggest alternative]
  F -- Yes --> H[Confirm appointment]
  G --> H
  H --> End([End])
```

### 4.3 Class Diagram
```mermaid
classDiagram
  class Member {
    -id: UUID
    -name: String
    -status: MemberStatus
    +canBorrow(): boolean
    +recordViolation(): void
  }
  class BookItem {
    -id: UUID
    -title: String
    -status: ItemStatus
    +reserve(): void
    +markAsBorrowed(): void
  }
  class BorrowTransaction {
    -id: UUID
    -dueDate: Date
    -returnedDate: Date
    +calculateFine(): Money
    +renew(): boolean
  }
  Member "1" --> "*" BorrowTransaction : has
  BookItem "1" --> "*" BorrowTransaction : referenced_by
```

### 4.4 Sequence Diagram
```mermaid
sequenceDiagram
  actor M as Member
  participant UI as Borrow Screen
  participant CT as CirculationController
  participant BS as BorrowService
  participant DB as Database
  M->>UI: scan book
  UI->>CT: requestBorrow(memberId, itemId)
  CT->>BS: borrow(memberId, itemId)
  BS->>DB: getMember(memberId)
  DB-->>BS: member
  BS->>DB: getItem(itemId)
  DB-->>BS: item
  alt member can borrow & item available
    BS->>DB: createTransaction(...)
    BS-->>CT: success
    CT-->>UI: confirm
    UI-->>M: success message
  else cannot borrow
    BS-->>CT: failure(reason)
    CT-->>UI: error
    UI-->>M: error message
  end
```

### 4.5 State Machine
```mermaid
stateDiagram-v2
  [*] --> Available
  Available --> Reserved: reserve [member valid]
  Available --> Borrowed: borrow [member valid]
  Reserved --> Borrowed: pickup [within hold period]
  Reserved --> Available: expire [hold period ended]
  Borrowed --> Available: return
  Borrowed --> Overdue: dueDateReached
  Overdue --> Available: return / chargeFine
  Available --> Lost: markLost
  Borrowed --> Lost: declareLost
  Lost --> [*]
```

### 4.6 Package / Component (workaround flowchart)
```mermaid
flowchart TB
  subgraph Presentation
    UI[Web UI]
    Mobile[Mobile App]
  end
  subgraph BusinessLogic
    Circulation[Circulation Service]
    Catalog[Catalog Service]
    Member[Member Service]
  end
  subgraph DataAccess
    BookRepo[BookRepository]
    MemberRepo[MemberRepository]
  end
  UI --> Circulation
  UI --> Catalog
  Mobile --> Circulation
  Circulation --> BookRepo
  Circulation --> MemberRepo
  Catalog --> BookRepo
  Member --> MemberRepo
```

## 5. PlantUML examples (khi cần UML đúng nghĩa)

### 5.1 Use Case Diagram
```plantuml
@startuml
left to right direction
actor Member
actor Librarian
rectangle "Library System" {
  usecase "Borrow Books" as UC1
  usecase "Return Books" as UC2
  usecase "Validate Member" as UC4
}
Member --> UC1
Member --> UC2
Librarian --> UC1
Librarian --> UC2
UC1 ..> UC4 : <<include>>
UC2 ..> UC4 : <<include>>
@enduml
```

### 5.2 Object Diagram
```plantuml
@startuml
object "alice : Member" as alice {
  id = "M001"
  status = "Active"
}
object "tx-1234 : BorrowTransaction" as tx {
  dueDate = "2024-12-31"
  returnedDate = null
}
object "book-5678 : BookItem" as book {
  title = "UML Distilled"
  status = "Borrowed"
}
alice --> tx
tx --> book
@enduml
```

### 5.3 Communication Diagram
```plantuml
@startuml
object Member as M
object UI as U
object Controller as C
object Service as S

M -> U : 1: clickBorrow()
U -> C : 2: borrow(memberId, itemId)
C -> S : 3: validateAndProcess()
S -> S : 3.1: checkMember()
S -> S : 3.2: checkItem()
S -> S : 3.3: createTx()
@enduml
```

## 6. Anti-patterns ký pháp
1. **Diagram đa mục đích**: 1 sơ đồ kể nhiều câu chuyện (cấu trúc + hành vi + triển khai). Mỗi diagram chỉ 1 mục đích.
2. **Trộn analysis & design** trong 1 diagram (vd: domain class + Repository + Controller cùng lúc).
3. **Tên kỹ thuật cho UC nghiệp vụ** ("Save User to DB" thay vì "Register Member").
4. **Multiplicity lười** (`*` mọi nơi).
5. **State name là động từ** ("Borrowing" thay vì "Borrowed").
6. **Sequence không khớp class** (gọi method không có trong class diagram).
7. **Activity không có start/end** rõ.
8. **Use case description có "click button" trong essential flow** (đó là real flow).
9. **Không có exception flow** ở use case quan trọng.
10. **Glossary trượt giữa diagram** (chỗ "Member", chỗ "User", chỗ "Customer" cho cùng khái niệm).
