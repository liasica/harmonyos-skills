---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-5
title: 编译报错“ERROR: Failed :entry:default@CompileResource”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“ERROR: Failed :entry:default@CompileResource”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5ac472e34a4fafc84b4d58b3939186aabfbee3c6a741bb475eaa08a83f482acf
---

**问题现象**

在构建依赖HSP的HAP模块时，如果出现“ERROR: Failed :entry:default@CompileResource”错误，提示某资源文件不存在，但该资源文件实际存在于HSP内，请检查以下几点：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/jiDV1X63RImYwRZw2BAdOw/zh-cn_image_0000002194318592.png?HW-CC-KV=V1&HW-CC-Date=20260429T062021Z&HW-CC-Expire=86400&HW-CC-Sign=52C14F6F32AD6445F4BEC6F33E0ACBBC3BF38B288A874A87285EA822511827A5)

**问题原因**

出现该问题的原因是HSP的module.json5中声明了权限申请等配置项时，引用了HSP自身的资源文件。构建时会将HSP的资源配置合并到HAP中，但运行时HAP无法直接访问HSP的资源文件。

**解决措施**

* 在各引用的HSP的module.json5中搜索对应资源，确认引入该资源的来源；
* 可以在引用方HAP内或appScope中添加相应资源以规避问题；
* 在引用方HAP的module.json5中声明相同的内容，可以在合并冲突时优先使用引用方HAP中的内容。例如，上图中的报错是由于HSP申请权限引起的，可以通过在引用方HAP中申请相同的权限来避免合并HSP中的这部分内容。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/hSJkiCfZSDe20ZP3nbvlkg/zh-cn_image_0000002229758857.png?HW-CC-KV=V1&HW-CC-Date=20260429T062021Z&HW-CC-Expire=86400&HW-CC-Sign=B9168A690388CDF8F916A1C51C58CF08FE20394C602950E53BC578E48F2E1BBB)
