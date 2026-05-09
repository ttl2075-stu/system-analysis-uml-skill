# system-analysis-uml

Skill pack hướng dẫn phân tích và thiết kế hệ thống hướng đối tượng theo chuẩn UML, dựa trên giáo trình **Dennis, Wixom & Tegarden — *Systems Analysis & Design with UML* (4th ed.)**.

## Cấu trúc

```
system-analysis-uml/
├── SKILL.md                        # Entry point cho AI agent
├── README.md                       # File này
├── QUICKSTART.md                   # Hướng dẫn dùng nhanh
├── LICENSE
├── references/                     # Lý thuyết theo Dennis et al.
│   ├── 01-functional-modeling.md   # Chapter 4
│   ├── 02-structural-modeling.md   # Chapter 5
│   ├── 03-behavioral-modeling.md   # Chapter 6
│   ├── 04-design-modeling.md       # Chapter 7-12
│   ├── 05-balancing-models.md      # Chapter 7 - V&V
│   ├── notation-uml-mermaid.md     # Quy ước Mermaid/PlantUML
│   └── runtime-rules.md            # Quy tắc thực thi cho agent
├── templates/                      # Mẫu artifact
│   ├── use-case-catalog.md
│   ├── use-case-description.md
│   ├── activity-model.md
│   ├── crc-card.md
│   ├── class-diagram.md
│   ├── sequence-design.md
│   ├── state-model.md
│   ├── package-design.md
│   ├── component-deployment.md
│   ├── traceability-matrix.md
│   ├── quality-attributes.md
│   ├── gap-report.md
│   └── mermaid/                    # Mã Mermaid mẫu
│       ├── use-case-overview.mmd
│       ├── activity-flow.mmd
│       ├── class-diagram.mmd
│       ├── sequence-diagram.mmd
│       ├── state-machine.mmd
│       ├── package-component.mmd
│       └── deployment.mmd
├── checklists/                     # Checklist V&V
│   ├── diagram-quality.md          # QA cho từng loại sơ đồ
│   ├── balancing-models.md         # Cân bằng giữa các mô hình
│   └── runtime.md                  # Per-turn checklist cho agent
└── examples/
    └── library-system.md           # Ví dụ end-to-end (domain-agnostic)
```

## Triết lý cốt lõi

1. **Iterative**: phân tích-thiết kế là vòng lặp, không tuyến tính.
2. **Balancing models**: 4 nhóm mô hình (functional/structural/behavioral/design) phải nhất quán với nhau.
3. **Evidence-first**: mọi phát biểu hiện trạng phải có nguồn xác thực.
4. **Domain-agnostic**: skill không gắn với domain cụ thể.

## Phạm vi

Skill này phù hợp cho:
- Phân tích hệ thống mới hoặc hiện có theo OOAD.
- Tạo bộ tài liệu UML đầy đủ (use case, activity, class, CRC, sequence, state, package, component, deployment).
- Kiểm tra chất lượng và balancing tài liệu UML.

Skill này **không** phù hợp cho:
- Yêu cầu code generation (chỉ phân tích-thiết kế).
- Phân tích nghiệp vụ thuần túy không cần mô hình (BPMN, Lean Canvas).

## Liên quan

- Dennis, A., Wixom, B. H., & Tegarden, D. (2012). *Systems Analysis and Design with UML* (4th ed.). Wiley.
- Cockburn, A. (2001). *Writing Effective Use Cases*. Addison-Wesley.
- Larman, C. (2004). *Applying UML and Patterns* (3rd ed.). Prentice Hall.
