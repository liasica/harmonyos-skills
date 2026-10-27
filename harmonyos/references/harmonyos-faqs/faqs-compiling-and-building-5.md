---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-5
title: "编译报错“ERROR: Failed :entry:default@CompileResource”"
breadcrumb: "FAQ > DevEco Studio > 编译构建 > 编译报错“ERROR: Failed :entry:default@CompileResource”"
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:52+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:9f4a281e9cd8905a6c28ed44d480b11198774758b907b07b1641d70ecfd6bcaa
---

**问题现象**

在构建依赖HSP的HAP模块时，如果出现“ERROR: Failed :entry:default@CompileResource”错误，提示某资源文件不存在，但该资源文件实际存在于HSP内，请检查以下几点：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/EYf0Ga82QgG7zS7GPH6QCQ/zh-cn_image_0000002624638376.png)

**问题原因**

出现该问题的原因是HSP的module.json5中声明了权限申请等配置项时，引用了HSP自身的资源文件。构建时会将HSP的资源配置合并到HAP中，但运行时HAP无法直接访问HSP的资源文件。

**解决措施**

* 在各引用的HSP的module.json5中搜索对应资源，确认引入该资源的来源；
* 可以在引用方HAP内或appScope中添加相应资源以规避问题；
* 在引用方HAP的module.json5中声明相同的内容，可以在合并冲突时优先使用引用方HAP中的内容。例如，上图中的报错是由于HSP申请权限引起的，可以通过在引用方HAP中申请相同的权限来避免合并HSP中的这部分内容。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/X9Cc4NfQQFKYrBz5BaCD0g/zh-cn_image_0000002654837781.png)
