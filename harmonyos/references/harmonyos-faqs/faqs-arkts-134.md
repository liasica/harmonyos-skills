---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-134
title: 对于@ohos.net.http模块是否需要使用TaskPool处理
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 对于@ohos.net.http模块是否需要使用TaskPool处理
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:16+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:91ebe5e80715efa6e22c64b90ff4fe21f38c708d19bbc48f8c5a11affc368af2
---

根据业务场景和实现需求决定是否使用TaskPool。如果业务中网络请求较少且后续数据处理耗时较短，则无需使用TaskPool，以避免额外的线程管理和数据传递开销。如果业务中需要处理大量网络请求且数据处理耗时较长，建议使用TaskPool进行网络请求和数据处理，以减轻UI主线程的负载。
