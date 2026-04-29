---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-139
title: 编译报错“Method setProperty validate failed in hvigorfile.ts”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Method setProperty validate failed in hvigorfile.ts”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:52+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8dd26efa00b52917899a913de361cc04af31a058787d9c0b39cd18da806aabc8
---

**错误描述**

setProperty方法在hvigorfile.ts中校验失败。

**可能****原因**

在hvigorfile.ts中使用setProperty方法时，传入的参数未通过 Schema 校验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/XDfDeD-ORnqPcKc0gXMYlg/zh-cn_image_0000002194318124.png?HW-CC-KV=V1&HW-CC-Date=20260429T062051Z&HW-CC-Expire=86400&HW-CC-Sign=0D5155FB5CEDA10F5277C170CB13BE91A767857E2F63368E15418148752E9B16)

**解决措施**

请根据报错提示信息，修改hvigorfile.ts文件中的配置字段。
