# Traceability Matrix — Template

## Mục đích
Liên kết end-to-end mọi artifact để khi requirement đổi → biết chỗ nào cần update; khi test fail → biết requirement nào bị ảnh hưởng.

## Master Traceability Matrix

| UC ID | Use Case | Class(es) | Operation(s) | Sequence Diagram | State Machine | Component | Test Case | Coverage |
|---|---|---|---|---|---|---|---|---|
| UC-001 | <name> | <ClassA, ClassB> | <op1, op2> | <SD-001> | <SM-001 nếu có> | <Comp1> | <test_id::case_name> | Y/N |
| UC-002 | | | | | | | | |
| ... | | | | | | | | |

## Quy tắc bắt buộc
1. **Mỗi UC importance High** phải có đủ cả: class, operation, sequence, test case.
2. **Coverage = Y** chỉ khi test case tồn tại và pass ở lần chạy gần nhất.
3. **State machine** chỉ điền cho class có lifecycle phức tạp.
4. **Component** điền tên đầy đủ (vd `circulation.borrow-service`).
5. **Test case** ghi đường dẫn + tên test (vd `tests/integration/test_borrow.py::test_borrow_success`).

## Sub-matrices (chi tiết)

### A. Use Case → Class

| UC ID | Use Case | Classes Involved | Notes |
|---|---|---|---|
| UC-001 | | | |

> Verification: Quy tắc 1 balancing — mỗi class trên class diagram phải xuất hiện ở ≥1 row.

### B. Class → Operation → Message → Test

| Class | Operation | Sequence Message (SD-ID:msg#) | Test Case |
|---|---|---|---|
| <ClassA> | <op1> | SD-001:msg-3 | test_x |

> Verification: Quy tắc 8 balancing — mỗi message phải gọi operation tồn tại.

### C. Component → Class → Package

| Component | Classes | Package | Layer |
|---|---|---|---|
| <Comp> | <Class list> | <package.name> | Presentation/Business/Data |

> Verification: Quy tắc 13 + 14 balancing.

## Gap Detection

Sau khi điền matrix, list các gap:

| Gap ID | Description | Impact | Priority | Action |
|---|---|---|---|---|
| GAP-001 | UC-005 không có test case | Không validate được | P1 | Viết integration test |
| ... | | | | |

## Validation
- [ ] Mỗi UC có row trong master matrix.
- [ ] Cột Class không trống cho UC importance High.
- [ ] Cột Test không trống cho UC importance High.
- [ ] Coverage = Y có nghĩa test pass thật, không lazy.
- [ ] Có gap report kèm theo nếu có row "N".
