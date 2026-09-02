---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-122
title: "如何解决编译报错“ Error: 'icon' value `$media:icons` invalid value.”的问题"
breadcrumb: "FAQ > DevEco Studio > 编译构建 > 如何解决编译报错“ Error: 'icon' value `$media:icons` invalid value.”的问题"
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:b707889517f5438b6337d5921caf7253b6a29b63dee8957204ff277b8595de35
---

**问题现象**

编译报错。

```text
ERROR: Failed :entry:default@CompileResource...
ERROR: Tools execution failed.
Error: ref `$media:icons` don't be defined.
Error: 'icon' value `$media:icons` invalid value.
at D:\project\process_profile\default\module.json
Detail: Please check the message from tools.
```

**报错原因**

引用的资源不存在时，编译错误指向build目录中的文件路径。

**常见场景**

1. 资源文件未添加。
2. 资源文件被意外删除。

**解决方案**

根据报错的资源ID全局搜索，使用右上角的查找按钮，确认报错的资源是否存在。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/1wFRKM86RW2sy2UhA7UO_A/zh-cn_image_0000002624478600.png "点击放大")
