---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-22
title: http请求响应为空，报错:"The request has been canceled or the number of requests exceeds 100"
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > http请求响应为空，报错:"The request has been canceled or the number of requests exceeds 100"
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9126cc0126000fa3d8ba7399eaeb3a166486aa446b40303053373e14b87a1552
---

这条错误信息是判断当前不存在httpRequest对象，原因则可能是httpRequest请求次数超过100次，导致创建失败，或者是被调用了destroy方法删掉了导致请求失败。
