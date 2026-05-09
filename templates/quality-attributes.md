# Quality Attributes — Template

> Theo Dennis et al. (4th ed.) — Non-Functional Requirements taxonomy.

## Mục đích
Mô tả các yêu cầu phi chức năng (NFR). Mỗi NFR phải **measurable** (đo được).

## 1. Operational Requirements

### 1.1 Technical Environment
- **Target platform**: <OS, browser, mobile platform>
- **Network**: <bandwidth, latency assumption>
- **Hardware**: <minimum spec>

### 1.2 System Integration
- <Hệ thống nào hệ thống này phải tích hợp>
- Protocol / API contract: <REST/SOAP/GraphQL/gRPC/file-based>

### 1.3 Portability
- <Có cần chạy trên nhiều môi trường không>

### 1.4 Maintainability
| Tiêu chí | Mục tiêu đo | Ngưỡng chấp nhận |
|---|---|---|
| Code change | thời gian thay đổi 1 module nhỏ | < X giờ |
| Bug fix turnaround | từ phát hiện đến fix | < X ngày |
| Documentation coverage | % API có doc | > 90% |

## 2. Performance Requirements

### 2.1 Speed
| Tiêu chí | Đo lường | Mục tiêu |
|---|---|---|
| API response time (p95) | từ request đến response | < 500ms |
| API response time (p99) | | < 1s |
| Page load (TTI) | | < 3s |
| Background job | thời gian xử lý | < X phút |

### 2.2 Capacity / Throughput
| Tiêu chí | Đo lường | Mục tiêu |
|---|---|---|
| Concurrent users | peak | X users |
| Requests per second | sustained | X RPS |
| Data volume | | X TB total |
| Daily transactions | | X txn/day |

### 2.3 Reliability
| Tiêu chí | Đo lường | Mục tiêu |
|---|---|---|
| Uptime | monthly | > 99.9% |
| MTBF | trung bình giữa lỗi | > X giờ |
| MTTR | trung bình khôi phục | < X phút |
| Data backup | tần suất + retention | hàng ngày, giữ X tháng |

## 3. Security Requirements

### 3.1 System Value / Data Sensitivity
- **Classification**: Public / Internal / Confidential / Highly Confidential
- **Compliance**: <GDPR / HIPAA / PCI-DSS / SOC2 / VN PDPL>

### 3.2 Authentication
- **Method**: <password / SSO / OAuth / SAML / multi-factor>
- **Password policy**: <length, complexity, rotation>
- **Session**: <timeout, refresh strategy>

### 3.3 Authorization
- **Model**: <RBAC / ABAC / ACL>
- **Granularity**: <function-level / resource-level / field-level>

### 3.4 Encryption
- **In transit**: <TLS 1.3 cho tất cả endpoint>
- **At rest**: <AES-256 cho database / file>
- **Key management**: <KMS / vault / HSM>

### 3.5 Audit & Logging
- **Audit events**: <login, data change, permission change, ...>
- **Retention**: <X năm>
- **Tamper-proof**: <write-once / digital signature>

### 3.6 Other
- **Vulnerability scan**: <quarterly / on-demand>
- **Penetration test**: <annually>

## 4. Cultural & Political Requirements

### 4.1 Multilinguality
- **Languages**: <list>
- **RTL support**: <yes/no>
- **Localization scope**: UI / data / both

### 4.2 Customization
- <Mức độ user/admin được tùy chỉnh hệ thống>

### 4.3 Legal / Regulatory
- <Luật / quy định cụ thể: GDPR right-to-be-forgotten, data residency, ...>

### 4.4 Accessibility
- <WCAG level: A / AA / AAA>

## Quy tắc viết NFR
- ❌ Sai: "Hệ thống phải nhanh."
- ✅ Đúng: "API GET dưới 1000 RPS có 95th percentile response time < 500ms."

- ❌ Sai: "Hệ thống phải bảo mật."
- ✅ Đúng: "Mọi API call phải authenticate qua OAuth 2.0; data at rest mã hóa AES-256."

## Validation
- [ ] Mỗi NFR có chỉ số đo (con số/đơn vị cụ thể).
- [ ] Mỗi NFR có ngưỡng chấp nhận rõ ràng.
- [ ] Mỗi NFR có thể test được (có cách verify).
- [ ] NFR phù hợp với importance/scale của hệ thống (không over-engineer).
