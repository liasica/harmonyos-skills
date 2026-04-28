---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-160
title: Stack布局设置Alignment.Bottom没有生效
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Stack布局设置Alignment.Bottom没有生效
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:42+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8237876507da67a6515b5f90308b21eee58fb3f67e93640551dc68fc5f6c8d54
---

**问题现象**

在build()中使用Stack作为容器，设置alignContent为Alignment.Bottom，同时设置align为Alignment.Center。但alignContent为Alignment.Bottom未生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/qMUALhWoTZqL9QL5auu_VQ/zh-cn_image_0000002229604149.png?HW-CC-KV=V1&HW-CC-Date=20260428T002540Z&HW-CC-Expire=86400&HW-CC-Sign=34E99C59A762D347A93139E0320F90109255E5532CA3764555F2D3E3A5B18409)

**解决措施**

由于Stack布局默认采用单一对齐策略，当同时设置alignContent与align属性时，后设置的值将生效。
