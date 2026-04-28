---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-kit-3
title: 在室内时，在持续定位场景中设置interval为1，为何不生效
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 在室内时，在持续定位场景中设置interval为1，为何不生效
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:52+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1691cfe91e78319ceba790d8d707a5a99433590fc43bfc31743d3f391591f6d6
---

在室内由于没有GNSS信号，返回的是网络位置。WLAN扫描功耗较大，系统限制每20秒扫描一次。因此，即使将interval设置为1，在室内也只能每20秒获取一次位置。
