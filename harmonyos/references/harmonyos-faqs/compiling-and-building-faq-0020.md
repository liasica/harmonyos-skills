---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0020
title: HSP包编译类型注解报错问题排查
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > HSP包编译类型注解报错问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:52+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:6e29faecc8c8309859efc60a21414962aff7a52bff08a35fd2b7383fb6a3a02d
---

**Q：如何解决编译报错“The inferred type of 'xxx' cannot be named without a reference to 'xxx'. This is likely not portable. A type annotation is necessary”的问题？**

**A**：HSP生成的.d.ts声明文件缺少类型注解，因为原始文件中未注明类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/XVmh2aZQSP6CJYnPp8NKEw/zh-cn_image_0000002772860978.png "点击放大")

在报错位置添加类型注解。
