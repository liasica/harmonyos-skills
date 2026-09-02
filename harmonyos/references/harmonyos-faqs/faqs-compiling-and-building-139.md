---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-139
title: 编译报错“Method setProperty validate failed in hvigorfile.ts”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Method setProperty validate failed in hvigorfile.ts”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:52+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7fc3ee2d120686ca623f611fe6cf2c054f63652af0682d025c891c73c6b13b4d
---

**错误描述**

setProperty方法在hvigorfile.ts中校验失败。

**可能****原因**

在hvigorfile.ts中使用setProperty方法时，传入的参数未通过 Schema 校验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/XDfDeD-ORnqPcKc0gXMYlg/zh-cn_image_0000002194318124.png)

**解决措施**

请根据报错提示信息，修改hvigorfile.ts文件中的配置字段。
