# Phase 4 — Design Modeling

> Nguồn: Dennis et al. *Systems Analysis & Design with UML* (4th ed.), Chapters 7–12.

## 1. Mục tiêu phase
Chuyển từ **analysis model** (mô tả problem domain) sang **design model** (mô tả solution):
- Cấu trúc package/component.
- Triển khai vật lý (deployment).
- Design class diagram (chi tiết hơn analysis class — có visibility, getter/setter, design pattern).
- Quality attributes (non-functional requirements).
- Lựa chọn make/buy/outsource và kiến trúc.

## 2. Artifacts của phase

### 2.1 Package Diagram

**Mục đích**: chia hệ thống thành các nhóm logic (package) để quản lý complexity.

**Thành phần UML**:
- **Package**: hình tab (rectangle có tab nhỏ).
- **Dependency**: mũi tên đứt từ package phụ thuộc → package được phụ thuộc.
- **Nested package**: package chứa package.

**Nguyên tắc phân chia**:
- **High cohesion**: class trong cùng package liên quan chặt chẽ về responsibility.
- **Low coupling**: dependency giữa package tối thiểu.
- **Acyclic dependency**: tránh vòng lặp phụ thuộc giữa package.
- **Stable abstraction principle**: package càng được nhiều package khác dùng, càng nên ổn định và abstract.

**Cách phân package phổ biến**:
- **Theo layer**: presentation, business logic, data access, infrastructure.
- **Theo subsystem nghiệp vụ**: catalog, circulation, member, billing.
- **Theo tier deployment**: client, server, middleware.
- Thường kết hợp 2D: layer × subsystem.

### 2.2 Component Diagram

**Mục đích**: mô tả thành phần triển khai (component) — đơn vị độc lập có interface rõ ràng.

**Thành phần**:
- **Component**: hình chữ nhật có icon component (≪component≫ stereotype).
- **Provided interface** (lollipop ─○): interface component cung cấp.
- **Required interface** (socket ─⊃): interface component cần.
- **Port**: điểm kết nối ngoài của component.
- **Connector**: nối required interface với provided interface.

**Phân biệt với class**:
- Class: đơn vị logic (trong code).
- Component: đơn vị triển khai (binary, jar, dll, container, microservice).

### 2.3 Deployment Diagram

**Mục đích**: mô tả topology vật lý — node nào chạy component nào.

**Thành phần**:
- **Node**: hình hộp 3D — server, container, device.
- **Artifact**: file vật lý (jar, war, dll).
- **Communication path**: đường nối giữa node + protocol (HTTP, TCP, AMQP).
- **Stereotype**: ≪device≫, ≪executionEnvironment≫, ≪deviceContainer≫.

**Cấu trúc thường dùng**:
- Multi-environment: dev / staging / production.
- Mỗi env: node web, node app, node db, node queue, node worker.

### 2.4 Design Class Diagram (vs Analysis Class Diagram)

**Khác biệt** (Dennis):
| Aspect | Analysis | Design |
|---|---|---|
| Focus | Problem domain | Solution domain |
| Class | Domain class only | Domain + entity + boundary + control + utility |
| Attribute | High-level | Đầy đủ type, visibility, default |
| Operation | Responsibility (doing) | Method signature đầy đủ |
| Relationship | Conceptual | Implementable (collection type, navigation direction) |

**Quy trình tạo design class diagram**:
1. Bắt đầu từ analysis class diagram.
2. Apply design pattern (factory, observer, strategy…) nếu phù hợp.
3. Identify boundary class (UI/API), control class (orchestration), entity class (data).
4. Refine attribute: thêm visibility, type chính xác, default value.
5. Refine operation: thêm signature đầy đủ.
6. Refine association: navigation direction, multiplicity chính xác, qualifier nếu cần.
7. Bổ sung utility class, exception class.

### 2.5 Quality Attributes (Non-Functional Requirements)

**Phân loại theo Dennis** (chi tiết: `templates/quality-attributes.md`):

- **Operational requirements**:
  - Technical environment (OS, browser, network)
  - System integration
  - Portability
  - Maintainability
- **Performance requirements**:
  - Speed (response time)
  - Capacity (throughput, concurrent users)
  - Reliability (uptime, MTBF)
- **Security requirements**:
  - System value (data sensitivity)
  - Access control (authN, authZ)
  - Encryption / authentication
  - Virus control
- **Cultural & political requirements**:
  - Multilinguality
  - Customization
  - Legal compliance (GDPR, HIPAA…)
  - Local regulations

**Quy tắc viết NFR**: phải **đo được** (measurable). Sai: "hệ thống phải nhanh"; đúng: "95th percentile response time < 500ms cho API GET dưới 1000 RPS".

### 2.6 Architecture Decision: Make / Buy / Outsource

Theo Dennis, design phase cần quyết định cấp cao:
- **Make**: tự build từ đầu.
- **Buy**: dùng package software có sẵn (COTS).
- **Outsource**: thuê bên ngoài build.

Tiêu chí quyết định: business need, in-house experience, project skills, project management, time, cost, control.

## 3. Traceability — bắt buộc

Sau khi có đủ artifact analysis + design, **bắt buộc** xây traceability matrix kết nối:

```
Use Case → Class (CRC) → Operation → Sequence Message → Design Class Method → Component → Test
```

Xem template: `templates/traceability-matrix.md`.

Mục đích:
- Khi requirement thay đổi → biết artifact nào cần update.
- Khi test fail → biết requirement nào bị ảnh hưởng.
- Khi review → confirm coverage.

## 4. Verification & Validation
- Package có acyclic không? Nếu có cycle → refactor.
- Component interface có khớp với operation trong design class không?
- Deployment có node nào không có component, hoặc component không có node?
- Design class có đầy đủ visibility cho mọi attribute/operation không?
- NFR có measurable không?
- Traceability matrix có row/col rỗng cho core flow không?

Chi tiết: `checklists/diagram-quality.md` mục G & H.

## 5. Anti-patterns
- Package phân theo loại file (.java, .py, .sql) thay vì responsibility.
- Component "God component" gom tất cả interface.
- Deployment diagram lộ thông tin nhạy cảm (IP nội bộ, password).
- Design class chỉ là copy của analysis class — không thêm gì.
- NFR mơ hồ ("user-friendly", "fast") không đo được.
- Traceability matrix chỉ điền vào lúc cuối phase (lazy traceability) → đã quá muộn để phát hiện gap.
