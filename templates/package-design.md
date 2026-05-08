# Package Design Template

## Mục tiêu
Phân tách package theo trách nhiệm kỹ thuật.

## Package inventory
- api
- services
- repositories
- models
- tasks
- common (utils/exceptions/security)

## Nguyên tắc phụ thuộc
- API phụ thuộc Service.
- Service phụ thuộc Repository.
- Repository phụ thuộc Model.
- Không phụ thuộc ngược chiều.
