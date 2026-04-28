---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-74
title: http模块证书验证的逻辑是什么
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > http模块证书验证的逻辑是什么
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6e71aa31069553616d89aa4770b5b742e5f49b44a523523e949dc9964a734516
---

http模块进行证书验证时，默认使用系统CA证书进行单向认证。当开发者设置参数caPath时，将优先使用指定的CA证书进行认证，若失败则使用系统默认CA证书认证。两者只要有一个认证通过，则证书验证成功。
