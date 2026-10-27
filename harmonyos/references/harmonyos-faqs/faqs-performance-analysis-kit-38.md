---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-38
title: 如何解决hdc server和client版本不一致的问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何解决hdc server和client版本不一致的问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:44+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:c180708c8c483e4a9a8ba46576658aee7388c31f1e5fd6750322e70be3a9f35b
---

**问题现象**

hdc.log 中的报错信息为“Daemon Session Handshake failed”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/bSTwWw8DSDegMmFysamQJg/zh-cn_image_0000002624476472.png "点击放大")

**解决措施**

1. 通过以下命令检查server和client的版本是否匹配。

   hdc checkserver
2. 执行以下命令，终止其他版本的服务器。

   hdc kill
