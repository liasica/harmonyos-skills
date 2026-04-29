---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-161
title: 编译报错“Duplicate 'routerMap' object names detected.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Duplicate 'routerMap' object names detected.”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:59+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:47b22db4834c1e1021da6b0460af027440b208118bad5d8e87859dde7091943c
---

**错误描述**

routerMap配置中存在重复名称。

**可能原因**

当前模块的router\_map.json文件中存在name重复的routerMap配置，或者当前模块与依赖模块之间存在name重复的routerMap配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/MzOAKxNZRz-SRgZphnlB2Q/zh-cn_image_0000002229603813.png?HW-CC-KV=V1&HW-CC-Date=20260429T062058Z&HW-CC-Expire=86400&HW-CC-Sign=658D72378A2E40C5FA79109B10A2D4262C0CD1EA33EEAB1A7AA75D331807B007)

**解决措施**

修改router\_map.json文件中的name字段，确保其值唯一。
