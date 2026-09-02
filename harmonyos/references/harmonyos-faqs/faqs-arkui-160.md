---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-160
title: Stack布局设置Alignment.Bottom没有生效
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Stack布局设置Alignment.Bottom没有生效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:5719fd33c37f33f001905569be9aa5a857caa65002d3efc4e8bcace94421cf46
---

**问题现象**

在build()中使用Stack作为容器，设置alignContent为Alignment.Bottom，同时设置align为Alignment.Center。但alignContent为Alignment.Bottom未生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/J_f91_UcTP2tQHauzWytGw/zh-cn_image_0000002654795287.png "点击放大")

**解决措施**

由于Stack布局默认采用单一对齐策略，当同时设置alignContent与align属性时，后设置的值将生效。
