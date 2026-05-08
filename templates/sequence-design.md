# Sequence Design Template

## Mục tiêu
Mô tả tương tác theo thời gian qua các layer.

## Sequence list
- Login/refresh
- Borrow
- Return + fine
- Reservation queue

## Mẫu participant
Client -> API -> Service -> Repository -> Model/DB -> Queue/Worker

## Checklist
- Có request và response.
- Có nhánh lỗi chính.
