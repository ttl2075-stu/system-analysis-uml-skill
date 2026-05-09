# Component & Deployment Design — Template

## Phần 1: Component Design

### Mục đích
Mô tả các đơn vị triển khai độc lập (component) và interface giữa chúng.

### Component Inventory

| Component | Stereotype | Provided Interfaces | Required Interfaces | Description |
|---|---|---|---|---|
| <Name> | ≪service≫/≪library≫/≪application≫ | <I1, I2> | <I3> | <vai trò> |
| ... | | | | |

### Component Diagram
> Mermaid template: `templates/mermaid/package-component.mmd` (workaround với `flowchart`).

### Interface Definitions

**Interface: <IName>**
- Provided by: <component>
- Required by: <component(s)>
- Operations:
  - `<operation signature>` — <description>

### Validation Component
- [ ] Mỗi component có ≥1 provided interface.
- [ ] Required interface của component A khớp với provided interface của component B nào đó.
- [ ] Component dùng operation trên design class diagram (Quy tắc 14 balancing).
- [ ] Không có "God component" gom mọi interface.

---

## Phần 2: Deployment Design

### Mục đích
Mô tả topology vật lý của hệ thống — node nào chạy component nào.

### Environments

- [ ] Development
- [ ] Staging / UAT
- [ ] Production
- [ ] Disaster Recovery (nếu có)

### Topology per Environment

#### Production (ví dụ)

| Node | Stereotype | Hardware/Container | Hosted Components | Connections |
|---|---|---|---|---|
| <node-name> | ≪device≫/≪executionEnvironment≫ | <spec> | <ComponentA, ComponentB> | <other nodes> |
| ... | | | | |

### Communication Paths

| From Node | To Node | Protocol | Port | Encryption | Notes |
|---|---|---|---|---|---|
| <Node A> | <Node B> | HTTPS/TCP/AMQP | <port> | TLS 1.3 | |

### Deployment Diagram
> Mermaid template: `templates/mermaid/deployment.mmd` (workaround).
> PlantUML preferred cho deployment diagram chuẩn.

### Constraints / Decisions
- <Vd: tất cả production traffic đi qua load balancer.>
- <Vd: database không expose ra internet.>

### Validation Deployment
- [ ] Mỗi component có node để host.
- [ ] Không có node "thừa" không host gì.
- [ ] Communication path có protocol rõ.
- [ ] Không lộ thông tin nhạy cảm (IP nội bộ thật, password, secret).
- [ ] Diagram có ≥1 environment (thường là production).
