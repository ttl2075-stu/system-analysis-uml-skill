# Approved Example — Backend (Condensed End-to-End)

## A. Context & Scope
- In-scope: Auth, Catalog Search, Borrow/Return, Reservation, Fine, Notifications.
- Out-of-scope: Frontend UX details, external BI pipelines.
- Actors: Member, Librarian, Admin, Worker.

## B. Use Case (sample UC-004 Borrow)
- Preconditions: actor authenticated; member active; item exists.
- Main flow: request borrow -> validate member/policy -> create borrow transaction -> update item status -> enqueue notification -> success.
- Exception flow: item unavailable -> reserve suggestion.
- Postconditions: transaction active; item borrowed.

## C. Activity (sample)
```mermaid
flowchart TD
A[Borrow request] --> B{Authenticated?}
B -- No --> X[Reject]
B -- Yes --> C[Validate member + policy]
C --> D{Item available?}
D -- No --> E[Offer reservation]
D -- Yes --> F[Create BorrowTransaction]
F --> G[Update BookItem status]
G --> H[Enqueue notification]
H --> I[Success]
```

## D. Domain model (sample)
```mermaid
classDiagram
class Member {+id UUID +status string}
class BookItem {+id UUID +status string}
class BorrowTransaction {+id UUID +dueAt datetime +status string}
Member "1" --> "*" BorrowTransaction : borrows
BookItem "1" --> "*" BorrowTransaction : referenced_by
```

## E. Sequence (sample)
```mermaid
sequenceDiagram
participant C as Client
participant API as API
participant S as CirculationService
participant R as BorrowRepository
participant Q as Queue
C->>API: POST /circulation/borrow
API->>S: validate + process
S->>R: create transaction + update status
S->>Q: enqueue notification
S-->>API: success payload
API-->>C: 200 OK
```

## F. Traceability sample
| Use Case | Endpoint | Service | Repository | Model | Test |
|---|---|---|---|---|---|
| UC-004 Borrow | POST /circulation/borrow | CirculationService.borrow | BorrowRepository.create | BorrowTransaction, BookItem | tests/integration/test_circulation_api.py::test_borrow_success |

## G. Quality/Gap snapshot
- Strength: consistent layering and flow.
- Gap: missing explicit idempotency contract for retry of async notification.
