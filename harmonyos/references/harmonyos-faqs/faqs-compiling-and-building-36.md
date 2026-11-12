---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-36
title: 编译报错 “Unknown resource name”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错 “Unknown resource name”
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:a6bf31aa7a7705e637fbe4ff2aaaff0b805641381c88ea49664630b84113bf5c
---

**场景一：**

**问题现象**

工程中模块A引用了模块B，编译模块A时出现错误，提示 "Unknown resource name 'xxxx'"，找不到模块B的资源。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/_vt7li03TBmqJVzmcfSSCg/zh-cn_image_0000002624478506.png?HW-CC-KV=V1&HW-CC-Date=20261112T233209Z&HW-CC-Expire=31536000000&HW-CC-Sign=68AC674ADED79A614E00C61F1E0407BB71837C39FC05888B28FEB9AE63758CAB)

**解决措施**

需要满足以下条件：

1. 资源需放置在模块B目录resource/base路径下，参考链接：[应用资源](../best-practices/bpta-multi-device-resource.md#应用资源)。
2. 模块B已安装。
3. 模块A中不能使用相对路径引用模块B的资源，应直接通过定义的模块名称来引用。

**场景二：**

**问题现象**

引用模块的方式不正确，如果引用的是其他模块的代码，也会导致资源未找到的错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/NxYq7IuDSEOFDrvtfpITPw/zh-cn_image_0000002654797865.png?HW-CC-KV=V1&HW-CC-Date=20261112T233209Z&HW-CC-Expire=31536000000&HW-CC-Sign=ADCE9C62ECA5A3F6BDCB8F79A4DA592AC085A8E3A275F028EC6C216129CB6777)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/3-NED7XjQM-BdHQV7i0WTw/zh-cn_image_0000002624638408.png?HW-CC-KV=V1&HW-CC-Date=20261112T233209Z&HW-CC-Expire=31536000000&HW-CC-Sign=E41A812295A2646B0C57588B22F28D188C1BEEB31840C4A3F20CEAD31AA44786)

**解决措施**

在oh-package.json5中引入该模块。通过定义的模块名称来引用。

如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/Lk0PyVj8SEeDKBQ8t73u0Q/zh-cn_image_0000002654837817.png?HW-CC-KV=V1&HW-CC-Date=20261112T233209Z&HW-CC-Expire=31536000000&HW-CC-Sign=575EE16AC3E83D28FC0618E993C9C470FC879D83E3537CCBA5C8816DD7616527)

**场景三：**

**问题现象**

HSP A 申请了某个权限并引用了资源。在构建所有依赖 A 的组件时，报错提示找不到 A 引用的资源。

**解决措施**

在引用方的配置文件中手动添加对应资源可以解决此问题。
