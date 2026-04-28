---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-faq-16
title: 在沙盒环境进行测试，但是实际需要真实支付是为什么？
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > IAP Kit常见问题 > 在沙盒环境进行测试，但是实际需要真实支付是为什么？
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d7e554c9d72e4de9ce8c1fc78f46e06045dd2c7f8103837c1656c44d25bb3fe3
---

有可能是debug包切换为release包之后，手机进程缓存没有失效导致。切换debug包和release包后，要保证进程缓存失效，比如锁屏5分钟或者重启。
