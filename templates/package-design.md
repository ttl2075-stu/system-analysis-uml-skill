# Package Design — Template

## Mục đích
Phân chia hệ thống thành các package (nhóm logic) để quản lý complexity.

## Strategy
Chọn 1 hoặc kết hợp:
- [ ] **Theo layer**: Presentation / Business Logic / Data Access / Infrastructure.
- [ ] **Theo subsystem nghiệp vụ**: <module 1> / <module 2> / ...
- [ ] **Theo tier deployment**: Client / Server / Middleware.
- [ ] **2D matrix**: layer × subsystem.

## Package Diagram
> Mermaid template: `templates/mermaid/package-component.mmd`

## Package Inventory

| Package | Description | Key Classes/Components | Dependencies |
|---|---|---|---|
| <package.name> | <vai trò> | <ClassA, ClassB> | <package.X, package.Y> |
| ... | | | |

## Dependency Rules

Liệt kê các quy tắc phụ thuộc bắt buộc cho hệ thống này:

- <Vd: Presentation chỉ phụ thuộc Business Logic, không phụ thuộc Data Access trực tiếp.>
- <Vd: Business Logic không phụ thuộc Presentation.>
- <Vd: Data Access không phụ thuộc Business Logic.>
- <...>

## Cohesion / Coupling Analysis

| Package | Cohesion | Coupling | Notes |
|---|---|---|---|
| <name> | High/Med/Low | High/Med/Low | <observation> |

## Validation
- [ ] Không có cyclic dependency giữa các package.
- [ ] Mỗi class nằm trong đúng 1 package (Quy tắc 13 balancing).
- [ ] Tên package có ý nghĩa nghiệp vụ hoặc kiến trúc rõ.
- [ ] Dependency direction nhất quán với layer architecture.
- [ ] Package không quá nhỏ (1-2 class) hoặc quá to (>20 class).
