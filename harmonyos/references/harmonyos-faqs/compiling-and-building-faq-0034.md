---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0034
title: "如何解决编译报错“ Error: 'icon' value `$media:icons` invalid value.”的问题"
breadcrumb: "FAQ > DevEco Studio > 编译构建 > 常见问题 > 如何解决编译报错“ Error: 'icon' value `$media:icons` invalid value.”的问题"
category: harmonyos-faqs
scraped_at: 2026-10-30T07:59:14+08:00
doc_updated_at: 2026-10-29
content_hash: sha256:f2f653e8cec6372562e75e30b0c06c3e4068909fbbfce285d2be34709a1c3519
---

**Q：如何解决编译报错“ Error: 'icon' value $media:icons invalid value.”的问题？**

**A**：编译报错。

```text
ERROR: Failed :entry:default@CompileResource...
ERROR: Tools execution failed.
Error: ref `$media:icons` don't be defined.
Error: 'icon' value `$media:icons` invalid value.
at D:\project\process_profile\default\module.json
Detail: Please check the message from tools.
```

报错原因：引用的资源不存在时，编译错误指向build目录中的文件路径。

常见场景：

1. 资源文件未添加。
2. 资源文件被意外删除。

解决方案：根据报错的资源ID全局搜索，使用右上角的查找按钮，确认报错的资源是否存在。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/WRGoGuxGSBKCZziRhSCkaA/zh-cn_image_0000002804575767.png "点击放大")
