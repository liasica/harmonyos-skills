---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-107
title: 编译报错“Duplicated files found in module entry. This may cause unexpected errors at runtime”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Duplicated files found in module entry. This may cause unexpected errors at runtime”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:ee455874bd6202d172fe3ed92a2fc548f0e1f9a9fd6370058e1dc07e696d81a3
---

**问题现象**

编译构建时，报错“Duplicated files found in module entry. This may cause unexpected errors at runtime”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/arNWtS-vS3Gjy1f6FdK8yA/zh-cn_image_0000002654837855.png "点击放大")

**解决措施**

该报错是从不同的包中收集到了相同名称的so包，导致so包冲突，可在模块级build-profile.json5文件中添加enableOverride字段并设置true。更多内容可参考[模块级build-profile.json5文件](../harmonyos-guides/ide-hvigor-build-profile.md)。

```json
"buildOption": {
  "nativeLib": {
    "filter": {
      "enableOverride": true
    }
  }
},
```
