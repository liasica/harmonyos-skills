---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-139
title: 编译报错“Method setProperty validate failed in hvigorfile.ts”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Method setProperty validate failed in hvigorfile.ts”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a5c9374c1ed6d162642466acba621b8e6697b5e10ef95f66c74378a657ab61e8
---

**错误描述**

setProperty方法在hvigorfile.ts中校验失败。

**可能****原因**

在hvigorfile.ts中使用setProperty方法时，传入的参数未通过 Schema 校验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/XDfDeD-ORnqPcKc0gXMYlg/zh-cn_image_0000002194318124.png?HW-CC-KV=V1&HW-CC-Date=20260428T002936Z&HW-CC-Expire=86400&HW-CC-Sign=2D6E249FCC1CD920FA0777FD730CFC52E48CCAA7F569D79F37CF4AFDD82A2D5E)

**解决措施**

请根据报错提示信息，修改hvigorfile.ts文件中的配置字段。
