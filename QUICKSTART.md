# Quickstart

## Cách dùng skill này

### Cho AI Agent (Claude)
Skill này được thiết kế cho Claude Skills format. Khi user nhờ phân tích/thiết kế hệ thống, agent sẽ:
1. Đọc `SKILL.md` để biết tổng quan.
2. Đọc reference của phase hiện tại (vd `references/01-functional-modeling.md`).
3. Áp dụng template tương ứng trong `templates/`.
4. Chạy checklist trong `checklists/` trước khi đóng phase.

### Cho con người (manual workflow)

**Phase 1 — Functional Modeling**
1. Đọc `references/01-functional-modeling.md`.
2. Tạo use case catalog: copy `templates/use-case-catalog.md` → điền.
3. Vẽ use case diagram: dùng `templates/mermaid/use-case-overview.mmd`.
4. Mỗi UC importance High → tạo description theo `templates/use-case-description.md`.
5. Mỗi UC importance High → tạo activity diagram theo `templates/mermaid/activity-flow.mmd`.
6. Chạy `checklists/diagram-quality.md` mục B + C + I.

**Phase 2 — Structural Modeling**
1. Đọc `references/02-structural-modeling.md`.
2. Object identification (textual analysis, brainstorming, common object lists, patterns).
3. Tạo CRC card cho mỗi class: copy `templates/crc-card.md` → điền.
4. Role-play CRC với 1-2 use case quan trọng.
5. Vẽ class diagram theo `templates/mermaid/class-diagram.mmd`.
6. Chạy `checklists/diagram-quality.md` mục D + E.
7. Chạy `checklists/balancing-models.md` Quy tắc 1-4.

**Phase 3 — Behavioral Modeling**
1. Đọc `references/03-behavioral-modeling.md`.
2. Mỗi UC importance High → vẽ sequence diagram theo `templates/mermaid/sequence-diagram.mmd`.
3. Mỗi class có lifecycle phức tạp → vẽ state machine theo `templates/mermaid/state-machine.mmd`.
4. (Tùy chọn) Tạo CRUDE matrix.
5. Chạy `checklists/diagram-quality.md` mục F + G.
6. Chạy `checklists/balancing-models.md` Quy tắc 5-11.

**Phase 4 — Design Modeling**
1. Đọc `references/04-design-modeling.md`.
2. Tạo package design theo `templates/package-design.md`.
3. Tạo component & deployment theo `templates/component-deployment.md`.
4. Refine class diagram thành design class diagram.
5. Tạo NFR theo `templates/quality-attributes.md`.
6. Chạy `checklists/diagram-quality.md` mục H.
7. Chạy `checklists/balancing-models.md` Quy tắc 12-14.

**Closure**
1. Tạo traceability matrix theo `templates/traceability-matrix.md`.
2. Tạo gap report theo `templates/gap-report.md`.
3. Walkthrough với reviewer.
4. Final balancing check.

## Prompt mẫu cho AI Agent

```
Áp dụng skill system-analysis-uml cho project [tên project].
Bắt đầu Phase 1: Functional Modeling.
Domain: [mô tả ngắn].
Tài liệu input: [file/folder].
Mode: review (không commit).
Output: artifact theo templates trong skill.
```

```
Tiếp tục Phase 2: Structural Modeling.
Sử dụng output từ Phase 1.
Trước khi sang phase mới, chạy balancing check Quy tắc 1-4.
```

## Adapt cho domain khác

Skill là **domain-agnostic**. Khi áp dụng cho domain ngoài library:
- Thay placeholder trong template (`<EntityName>`, `<UseCaseName>`) bằng class/UC của domain.
- Glossary của domain phải nhất quán xuyên suốt.
- Ví dụ trong `examples/library-system.md` chỉ là minh họa cấu trúc, không phải template để copy.

## Câu hỏi thường gặp

**Có bắt buộc làm tất cả 4 phase không?**
Có, nhưng độ sâu của mỗi phase tùy vào scope project. Project nhỏ có thể giảm bớt số UC chi tiết, số CRC, số sequence — nhưng vẫn nên có ít nhất 1 artifact mỗi loại.

**Có thể skip phase 3 (behavioral) cho project đơn giản không?**
KHÔNG nên. Behavioral modeling là chỗ phát hiện gap nhiều nhất. Có thể giảm số sequence diagram, nhưng nên có ít nhất 1 cho UC quan trọng nhất.

**State machine có cần cho mọi class không?**
Không. Chỉ class có lifecycle phức tạp (status đổi nhiều theo event) mới cần.

**Mermaid hay PlantUML?**
Default Mermaid. Dùng PlantUML khi Mermaid không support (use case diagram chuẩn UML, communication diagram, object diagram). Xem `references/notation-uml-mermaid.md`.
