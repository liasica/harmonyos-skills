---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-160
title: Stack布局设置Alignment.Bottom没有生效
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Stack布局设置Alignment.Bottom没有生效
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:02+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:8dfc8a907ae854a1f766157b179014a5c861cabbf0ce772de23643737235a866
---

**问题现象**

在build()中使用Stack作为容器，设置alignContent为Alignment.Bottom，同时设置align为Alignment.Center。但alignContent为Alignment.Bottom未生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/fmbmBcWjSPCBbdr-wlcCHA/zh-cn_image_0000002654795287.png "点击放大")

**解决措施**

由于Stack布局默认采用单一对齐策略，当同时设置alignContent与align属性时，后设置的值将生效。
