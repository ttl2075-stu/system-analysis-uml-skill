# Phase 7 — Release & Adoption Package

## 1) Mục tiêu
Hoàn thiện gói bàn giao để skill `system-analysis-uml` được áp dụng ổn định trong thực tế dự án.

## 2) Nội dung bàn giao

### 2.1 Core pack
- `SKILL.md`
- `method-core.md`
- `notation-rules.md`
- `diagram-qa-checklist.md`
- `runtime-rules.md`
- `runtime-checklist.md`

### 2.2 Authoring pack
- `templates/*`
- `templates/mermaid/*`
- `examples/approved/backend-sample-outline.md`

### 2.3 Quality pack
- `validation-report.md`
- `fix-list.md`
- `CHANGELOG.md`

## 3) Quy trình áp dụng trong team
1. Khởi tạo tài liệu bằng `quickstart.md`.
2. Thực thi từng step theo `method-core.md`.
3. Review ký pháp bằng `notation-rules.md` + `diagram-qa-checklist.md`.
4. Kiểm soát vận hành bằng `runtime-rules.md` + `runtime-checklist.md`.
5. Chốt traceability và gap report trước khi kết thúc.

## 4) Tiêu chí nghiệm thu nội bộ
- Có artifacts đủ 8 bước.
- Mọi sơ đồ Mermaid pass checklist.
- Traceability matrix có mapping đến test.
- Báo cáo chất lượng và gap có mức ưu tiên.

## 5) Kế hoạch vận hành sau phát hành
- Sprint review định kỳ cho tài liệu.
- Update CHANGELOG khi điều chỉnh rules/templates.
- Ưu tiên xử lý P1 trong `fix-list.md` trước vòng phát hành kế tiếp.

## 6) Trạng thái
- Release nội bộ: **v1.0.0**
- Trạng thái Phase 7: **Completed**
