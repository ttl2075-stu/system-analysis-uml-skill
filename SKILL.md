# SKILL: system-analysis-uml

## Purpose
Chuẩn hóa quy trình để AI Agent phân tích và thiết kế hệ thống theo hướng **design-first**, với ký pháp UML ưu tiên **Mermaid**.

## When to use
Dùng khi cần:
- phân tích hệ thống mới hoặc hệ thống hiện có theo chuẩn,
- xây tài liệu requirements/analysis/design/traceability,
- chuẩn hóa sơ đồ và chất lượng tài liệu kỹ thuật.

## Inputs expected
- Bối cảnh hệ thống và phạm vi
- Codebase/docs hiện trạng (nếu có)
- Mục tiêu tài liệu (backend/fullstack)

## Mandatory workflow
Agent **phải** tuân theo `method-core.md` (Step 1 → Step 8), không nhảy bước khi chưa pass gate.

## Files in this skill pack
- `method-core.md`: quy trình 8 bước + stop rules
- `notation-rules.md`: chuẩn ký pháp UML/Mermaid
- `diagram-qa-checklist.md`: checklist chất lượng sơ đồ
- `runtime-rules.md`: guardrails vận hành
- `runtime-checklist.md`: checklist thực thi từng lượt
- `templates/*`: mẫu tài liệu
- `templates/mermaid/*`: mẫu sơ đồ
- `validation-report.md`: báo cáo validation
- `fix-list.md`: backlog cải tiến
- `quickstart.md`: cách dùng nhanh

## Execution mode
- Mặc định: **review mode** (không commit/push)
- Chỉ commit khi có lệnh explicit từ người dùng.

## Output contract
Mỗi lượt chạy phải trả:
1. Đã làm gì
2. Evidence từ đâu
3. Còn thiếu gì
4. Bước tiếp theo
