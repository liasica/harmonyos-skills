---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-139
title: 编译报错“Method setProperty validate failed in hvigorfile.ts”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Method setProperty validate failed in hvigorfile.ts”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:36057afdf61c5a92331de13ad800b28d5d295e23e8192a9a19410ae44a67aaa1
---

**错误描述**

setProperty方法在hvigorfile.ts中校验失败。

**可能****原因**

在hvigorfile.ts中使用setProperty方法时，传入的参数未通过 Schema 校验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/0j6oyN_1QFKkaWctVPyYVA/zh-cn_image_0000002624478622.png)

**解决措施**

请根据报错提示信息，修改hvigorfile.ts文件中的配置字段。
