---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-160
title: Stack布局设置Alignment.Bottom没有生效
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Stack布局设置Alignment.Bottom没有生效
category: harmonyos-faqs
scraped_at: 2026-04-29T14:16:40+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6e15640c2ca3541718398252ffa8a89bfc4043838bb4fcc2627ebf7d744af33a
---

**问题现象**

在build()中使用Stack作为容器，设置alignContent为Alignment.Bottom，同时设置align为Alignment.Center。但alignContent为Alignment.Bottom未生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/qMUALhWoTZqL9QL5auu_VQ/zh-cn_image_0000002229604149.png)

**解决措施**

由于Stack布局默认采用单一对齐策略，当同时设置alignContent与align属性时，后设置的值将生效。
