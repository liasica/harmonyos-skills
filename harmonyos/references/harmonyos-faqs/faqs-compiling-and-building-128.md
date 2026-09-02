---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-128
title: 如何解决编译报错“ The inferred type of 'xxx' cannot be named without a reference to 'xxx'. This is likely not portable. A type annotation is necessary.”的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决编译报错“ The inferred type of 'xxx' cannot be named without a reference to 'xxx'. This is likely not portable. A type annotation is necessary.”的问题
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:49+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:955148a5ee064850bacf46385db222500907c7edaaf7d541059472b20ee71d79
---

**问题现象**

编译报错“The inferred type of 'xxx' cannot be named without a reference to 'xxx'. This is likely not portable. A type annotation is necessary”。

**问题原因**

HSP生成的.d.ts声明文件缺少类型注解，因为原始文件中未注明类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/uHiT9QliTouP1x9Cg-tzPw/zh-cn_image_0000002229758869.png "点击放大")

**解决方案**

在报错位置添加类型注解。
