---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-24
title: 下载账单文件后，应该使用哪种格式来解析日期？
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > Payment Kit常见问题 > 下载账单文件后，应该使用哪种格式来解析日期？
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9b2f01a1c25b3ee35128fb0001028da2f1ffa9ec15188620c575ac005612752e
---

1. 不建议用Excel文件格式去解析，Excel打开后可能会被默认格式化处理，导致通过Excel打开文件后，单元格日期格式显示为 “yyyy/MM/dd HH:mm”，双击后显示 “yyyy/MM/dd HH:mm:ss”，以“yyyy/MM/dd HH:mm:ss”格式解析不出来，以“yyyy/MM/dd HH:mm”格式可以解析。
2. 建议使用csv文件格式，yyyy/MM/dd HH:mm:ss时间格式做解析。
