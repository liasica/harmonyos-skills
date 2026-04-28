---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-7
title: 条形码识别坐标信息为空
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit常见问题 > 条形码识别坐标信息为空
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:44+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:aa1ec03fbf3c6b3e4452e478f83b7806f523e053186dd058572cf693e233d697
---

**问题现象**

条形码识别场景下，存在识别成功后，返回位置信息为空的现象。

**解决措施**

由于条形码识别逻辑中，算法返回的位置信息可能位于同一行或同一列，无法返回外接矩形。在此场景下，开发者需判断位置信息是否为空，并进行相应处理。
