---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-data-prevention-7
title: Asset Store是否会被其他应用获取？是否会出现跨设备同步的情况
breadcrumb: FAQ > 系统开发 > 安全 > 数据安全存储（Data Prevention） > Asset Store是否会被其他应用获取？是否会出现跨设备同步的情况
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:55+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:70811affab882a5b1f10d6ad4f746ecbc2648f9f1dbcea84d01a92464cbe4f2c
---

1. Asset Store关键资产存储服务当前未实现应用共享数据功能，仅写入数据的应用可以访问。

2. 如果开发者不希望跨设备同步数据，在添加关键资产时需将SyncType属性设置为never。
