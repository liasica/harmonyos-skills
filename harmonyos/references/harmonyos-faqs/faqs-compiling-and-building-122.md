---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-122
title: 如何解决编译报错“ Error: 'icon' value `$media:icons` invalid value.”的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决编译报错“ Error: 'icon' value `$media:icons` invalid value.”的问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:33+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e1d508250e8e6754178e052611e20501c92a439ba05aaf0699c376a2763b20c2
---

**问题现象**

编译报错。

```
1. ERROR: Failed :entry:default@CompileResource...
2. ERROR: Tools execution failed.
3. Error: ref `$media:icons` don't be defined.
4. Error: 'icon' value `$media:icons` invalid value.
5. at D:\project\process_profile\default\module.json
6. Detail: Please check the message from tools.
```

**报错原因**

引用的资源不存在时，编译错误指向build目录中的文件路径。

**常见场景**

1. 资源文件未添加。
2. 资源文件被意外删除。

**解决方案**

根据报错的资源ID全局搜索，使用右上角的查找按钮，确认报错的资源是否存在。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/xXlBFvplR1WhuUFgC-x8kQ/zh-cn_image_0000002262335589.png?HW-CC-KV=V1&HW-CC-Date=20260428T002932Z&HW-CC-Expire=86400&HW-CC-Sign=2786F74E6B0A16021019340156A9E1B21EA739D3FD131EB3E381BFE495839748 "点击放大")
