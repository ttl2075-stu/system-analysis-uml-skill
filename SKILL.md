---
name: system-analysis-uml
description: Use when analyzing or designing software systems with UML — building use case diagrams/descriptions, activity diagrams, CRC cards, class/domain diagrams, sequence diagrams, communication diagrams, state machines, package/component/deployment diagrams, or producing traceability matrices and design documents. Triggers on requests like "phân tích hệ thống", "thiết kế hệ thống", "vẽ use case", "class diagram", "sequence diagram", "OOAD", "UML", or any system analysis/design deliverable. Methodology follows Dennis, Wixom & Tegarden — Systems Analysis & Design with UML v2 (4th ed.).
---

# System Analysis & Design with UML

## Mục đích
Hướng dẫn quy trình **phân tích và thiết kế hệ thống hướng đối tượng** theo chuẩn UML, dựa trên giáo trình Dennis et al. *Systems Analysis & Design with UML* (4th ed.). Skill này chuẩn hóa cách tạo và kiểm tra các artifact UML để đảm bảo tính nhất quán giữa các mô hình.

## Khi nào dùng
- Phân tích hệ thống mới hoặc hệ thống hiện có theo phương pháp OOAD.
- Tạo bộ tài liệu phân tích-thiết kế: requirements → analysis → design → traceability.
- Vẽ và kiểm tra sơ đồ UML (use case, activity, class/CRC, sequence, communication, state, package, component, deployment).
- Review/cải thiện tài liệu UML hiện có theo chuẩn academic.

## Triết lý cốt lõi (theo Dennis et al.)
1. **Iterative, không tuyến tính**: phân tích-thiết kế là vòng lặp giữa functional, structural, behavioral models — phát hiện điểm thiếu ở mô hình này thì quay lại sửa mô hình kia.
2. **Balancing models**: bốn nhóm mô hình (functional/structural/behavioral/design) phải nhất quán với nhau. Sau mỗi mô hình mới, cross-check lại các mô hình cũ.
3. **Evidence-first**: mọi phát biểu về hiện trạng phải có nguồn (code, tài liệu, phỏng vấn, observation). Nếu không có nguồn, ghi rõ là **giả định** hoặc **đề xuất**, không phải sự thật.
4. **Phân biệt 3 loại phát biểu**: *Analysis fact* (quan sát) ≠ *Design proposal* (đề xuất) ≠ *Open issue* (chưa đủ thông tin).

## Quy trình tổng quan
Skill chia thành 4 phase chính. **KHÔNG phải bắt buộc tuyến tính** — agent quay lại bước trước khi cần (theo nguyên tắc iterative của Dennis).

| Phase | Mục tiêu | Reference |
|---|---|---|
| **1. Requirements (Functional)** | Actors, Use Case Diagram, Use Case Descriptions, Activity Diagrams | `references/01-functional-modeling.md` |
| **2. Analysis (Structural)** | Object identification, CRC Cards, Class Diagram, Object Diagram | `references/02-structural-modeling.md` |
| **3. Analysis (Behavioral)** | Sequence Diagram, Communication Diagram, Behavioral State Machine, CRUDE Matrix | `references/03-behavioral-modeling.md` |
| **4. Design** | Package Diagram, Component Diagram, Deployment Diagram, Design class diagram, Quality Attributes | `references/04-design-modeling.md` |

Sau mỗi phase, **bắt buộc** chạy verification & validation:
- `references/05-balancing-models.md` — quy tắc cân bằng giữa các mô hình
- `checklists/diagram-quality.md` — checklist chất lượng từng loại sơ đồ

## File trong skill này

### Workflow & lý thuyết (đọc khi vào phase tương ứng)
- `references/01-functional-modeling.md` — use case + activity (Chapter 4)
- `references/02-structural-modeling.md` — CRC + class diagram (Chapter 5)
- `references/03-behavioral-modeling.md` — sequence + state (Chapter 6)
- `references/04-design-modeling.md` — package + component + deployment (Chapter 7-12)
- `references/05-balancing-models.md` — verification & validation (Chapter 7)
- `references/notation-uml-mermaid.md` — quy ước Mermaid/PlantUML cho từng loại UML
- `references/runtime-rules.md` — quy tắc thực thi cho agent (evidence-first, no step-skipping)

### Templates (sao chép khi cần tạo artifact)
- `templates/use-case-description.md` — mẫu Dennis-style đầy đủ
- `templates/use-case-catalog.md`
- `templates/activity-model.md`
- `templates/crc-card.md` — bộ thẻ CRC mặt trước/sau
- `templates/class-diagram.md`
- `templates/sequence-design.md`
- `templates/state-model.md`
- `templates/package-design.md`
- `templates/component-deployment.md`
- `templates/traceability-matrix.md`
- `templates/quality-attributes.md`
- `templates/gap-report.md`
- `templates/mermaid/*.mmd` — code mẫu Mermaid cho từng loại sơ đồ

### Checklists (chạy trước khi đóng phase)
- `checklists/diagram-quality.md` — QA cho từng loại sơ đồ
- `checklists/balancing-models.md` — kiểm tra nhất quán giữa các mô hình
- `checklists/runtime.md` — checklist mỗi lượt agent chạy

### Examples
- `examples/library-system.md` — ví dụ hoàn chỉnh end-to-end (domain-agnostic, có thể adapt)

## Output contract (mỗi lượt chạy)
Mỗi response của agent phải kết thúc với 4 phần:
1. **Đã làm**: artifact nào đã tạo/cập nhật
2. **Evidence**: nguồn dữ liệu (file, đoạn trích, phỏng vấn, giả định)
3. **Còn thiếu**: input/decision còn cần
4. **Bước kế tiếp**: phase/artifact đề xuất tiếp theo

## Quy tắc quan trọng
- **Domain-agnostic**: skill này không gắn với bất kỳ domain cụ thể (library, e-commerce, banking…). Templates dùng placeholder, examples chỉ là minh họa.
- **Không bịa evidence**: nếu không có code/docs để xác nhận, ghi rõ là giả định hoặc đặt câu hỏi.
- **Iterative, không cứng nhắc**: thấy bất nhất giữa mô hình mới và mô hình cũ → quay lại sửa, không phớt lờ.
- **Mermaid là default, PlantUML là alternative** khi Mermaid không hỗ trợ (use case diagram chuẩn UML, object diagram).
