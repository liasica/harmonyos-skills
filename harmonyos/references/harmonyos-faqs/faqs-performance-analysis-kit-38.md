---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-38
title: 如何解决hdc server和client版本不一致的问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何解决hdc server和client版本不一致的问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:17+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ab428601055c35cd05ca6fdfeeee8f7dbba37740effc7f1932ddfd7fe7da68b5
---

**问题现象**

hdc.log 中的报错信息为“Daemon Session Handshake failed”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/TM3f0phZSLC1p7y9jeuQNw/zh-cn_image_0000002194318252.png?HW-CC-KV=V1&HW-CC-Date=20260428T002316Z&HW-CC-Expire=86400&HW-CC-Sign=36610877A2045BC802A780A1E974B66ED6ED256B8C4905893153E30B287B549C "点击放大")

**解决措施**

1. 通过以下命令检查server和client的版本是否匹配。

   hdc checkserver
2. 执行以下命令，终止其他版本的服务器。

   hdc kill
