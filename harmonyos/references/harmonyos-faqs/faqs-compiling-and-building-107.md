---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-107
title: 编译报错“Duplicated files found in module entry. This may cause unexpected errors at runtime”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Duplicated files found in module entry. This may cause unexpected errors at runtime”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:43+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:edcf61e6d61129aa4a5e064582cf076073c98fa0dec5e789bee00c2b6d66ba80
---

**问题现象**

编译构建时，报错“Duplicated files found in module entry. This may cause unexpected errors at runtime”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/D1FR-ZAzRLyLscBwFKyBlg/zh-cn_image_0000002229603833.png?HW-CC-KV=V1&HW-CC-Date=20260429T062041Z&HW-CC-Expire=86400&HW-CC-Sign=EE1DAF11453186BF1E7E0800A390A4B22DD437FEDE4A7369086EDCCC51759C4E "点击放大")

**解决措施**

该报错是从不同的包中收集到了相同名称的so包，导致so包冲突，可在模块级build-profile.json5文件中添加enableOverride字段并设置true。更多内容可参考[模块级build-profile.json5文件](../harmonyos-guides/ide-hvigor-build-profile.md)。

```
1. "buildOption": {
2. "nativeLib": {
3. "filter": {
4. "enableOverride": true
5. }
6. }
7. },
```

[build-profile.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/library2/build-profile.json5#L5-L11)
