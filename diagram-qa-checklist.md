# Diagram QA Checklist (Phase 2)

## A. Kiểm tra chung
- [ ] Sơ đồ có tiêu đề và mục đích rõ ràng
- [ ] Thuật ngữ nhất quán với tài liệu
- [ ] Không trộn analysis và design trong cùng mục tiêu sơ đồ
- [ ] Có nhánh ngoại lệ/lỗi (nếu là flow nghiệp vụ)

## B. Use Case
- [ ] Actor và use case tách biệt rõ
- [ ] Use case dùng động từ nghiệp vụ
- [ ] Không chứa chi tiết kỹ thuật thấp tầng

## C. Activity
- [ ] Có start/end
- [ ] Có decision nodes cho điều kiện chính
- [ ] Có tối thiểu 1 nhánh lỗi cho core flow

## D. Class/Domain
- [ ] Class cốt lõi có thuộc tính chính
- [ ] Quan hệ và cardinality có ý nghĩa nghiệp vụ
- [ ] Không lẫn infra concerns vào domain model

## E. Sequence
- [ ] Participant phản ánh đúng layer kiến trúc
- [ ] Có request/response rõ ràng
- [ ] Có luồng lỗi/ngoại lệ chính

## F. State
- [ ] Có initial state
- [ ] Transition có trigger rõ
- [ ] Guard condition được biểu diễn nếu có

## G. Component/Deployment
- [ ] Thể hiện đầy đủ các thành phần runtime chính
- [ ] Luồng kết nối có hướng và ý nghĩa
- [ ] Không đưa thông tin nhạy cảm không cần thiết
