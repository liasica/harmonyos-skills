---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-36
title: 编译报错 “Unknown resource name”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错 “Unknown resource name”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:29+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:0855a36886d2087347dfe4db7290b2ec7ddae043d830c67d9b434e50894d0aa9
---

**场景一：**

**问题现象**

工程中模块A引用了模块B，编译模块A时出现错误，提示 "Unknown resource name 'xxxx'"，找不到模块B的资源。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/ZZqvfcioTjKQaTGcqb9z9A/zh-cn_image_0000002229603765.png?HW-CC-KV=V1&HW-CC-Date=20260429T062027Z&HW-CC-Expire=86400&HW-CC-Sign=F0B75457FF7F6198E7E7D1BC1AE9BBD0FBCB864A33D20781FC5370F18F3A5FE2)

**解决措施**

需要满足以下条件：

1. 资源需放置在模块B目录resource/base路径下，参考链接：[应用资源](../best-practices/bpta-multi-device-resource.md#应用资源)。
2. 模块B已安装。
3. 模块A中不能使用相对路径引用模块B的资源，应直接通过定义的模块名称来引用。

**场景二：**

**问题现象**

引用模块的方式不正确，如果引用的是其他模块的代码，也会导致资源未找到的错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/kw6ssAz9QDmSQGUVUQTg_A/zh-cn_image_0000002194158372.png?HW-CC-KV=V1&HW-CC-Date=20260429T062027Z&HW-CC-Expire=86400&HW-CC-Sign=2D80885AA2F8759CF54EAEB28C85A2026A56FE24338F2122621DECE18D14672D)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/ksuQvZCrQqOPyT8-l0NyNQ/zh-cn_image_0000002229603773.png?HW-CC-KV=V1&HW-CC-Date=20260429T062027Z&HW-CC-Expire=86400&HW-CC-Sign=5F6D7963647D19212735772A3C2E7C83156C16332B630C5D7CBDB84B841B479B)

**解决措施**

在oh-package.json5中引入该模块。通过定义的模块名称来引用。

如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/pRcfsCP4RoiDcLIiDVmCkQ/zh-cn_image_0000002194317992.png?HW-CC-KV=V1&HW-CC-Date=20260429T062027Z&HW-CC-Expire=86400&HW-CC-Sign=5436F8E09634D43F7978715B33672CE6497F5082EC5EE54384176613B9036BAD)

**场景三：**

**问题现象**

HSP A 申请了某个权限并引用了资源。在构建所有依赖 A 的组件时，报错提示找不到 A 引用的资源。

**解决措施**

在引用方的配置文件中手动添加对应资源可以解决此问题。
