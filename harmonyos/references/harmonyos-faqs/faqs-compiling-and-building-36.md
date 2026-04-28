---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-36
title: 编译报错 “Unknown resource name”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错 “Unknown resource name”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:15+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:ea943fd7b801d2f72f4d0c116072435048555cf250b3fb2bdebea06babc570a1
---

**场景一：**

**问题现象**

工程中模块A引用了模块B，编译模块A时出现错误，提示 "Unknown resource name 'xxxx'"，找不到模块B的资源。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/ZZqvfcioTjKQaTGcqb9z9A/zh-cn_image_0000002229603765.png?HW-CC-KV=V1&HW-CC-Date=20260428T002914Z&HW-CC-Expire=86400&HW-CC-Sign=426328682AB710C39E87FC6CF3C5B7F7922B69E2A4780C2D39F2D37D37E04E47)

**解决措施**

需要满足以下条件：

1. 资源需放置在模块B目录resource/base路径下，参考链接：[应用资源](../best-practices/bpta-multi-device-resource.md#应用资源)。
2. 模块B已安装。
3. 模块A中不能使用相对路径引用模块B的资源，应直接通过定义的模块名称来引用。

**场景二：**

**问题现象**

引用模块的方式不正确，如果引用的是其他模块的代码，也会导致资源未找到的错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/kw6ssAz9QDmSQGUVUQTg_A/zh-cn_image_0000002194158372.png?HW-CC-KV=V1&HW-CC-Date=20260428T002914Z&HW-CC-Expire=86400&HW-CC-Sign=65D789B80A270E94555E9AB5505394ABB82EF268CE8457617D6FE1FB03F61B25)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/ksuQvZCrQqOPyT8-l0NyNQ/zh-cn_image_0000002229603773.png?HW-CC-KV=V1&HW-CC-Date=20260428T002914Z&HW-CC-Expire=86400&HW-CC-Sign=D89E7CC00C9B814DEB07D9DEDE508AEA5C1A7184A9FD326CFE4D072227143534)

**解决措施**

在oh-package.json5中引入该模块。通过定义的模块名称来引用。

如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/pRcfsCP4RoiDcLIiDVmCkQ/zh-cn_image_0000002194317992.png?HW-CC-KV=V1&HW-CC-Date=20260428T002914Z&HW-CC-Expire=86400&HW-CC-Sign=735B5388E37C49523C29FB731142CFA0C6358FC03C34165010C1CAB39BD609C5)

**场景三：**

**问题现象**

HSP A 申请了某个权限并引用了资源。在构建所有依赖 A 的组件时，报错提示找不到 A 引用的资源。

**解决措施**

在引用方的配置文件中手动添加对应资源可以解决此问题。
