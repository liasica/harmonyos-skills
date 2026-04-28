---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-3
title: Scan Kit无法识别多个码图
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit常见问题 > Scan Kit无法识别多个码图
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1c3c405141df6b152c3c44e65f9480870b835c1a2941f19278bc5e150b16e6e2
---

**问题现象**

实时扫描多个码图时，只返回一个码图结果。

**解决措施**

1. 检查[ScanOptions](../harmonyos-references/scan-scanbarcode-api.md#scanoptions)的enableMultiMode参数是否设置为true，开启多码扫描。
2. 检查ScanOptions的scanTypes参数是否已设置相应的码类型。
3. 检查码图类型是否在Scan Kit所定义支持的码图类型内。
4. 目前实时扫描多个码图时，最多仅支持返回4个码图。
5. 如还未解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。
