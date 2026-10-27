---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-109
title: 构建报错“Duplicated files found in module xxx. This may cause unexpected errors at runtime”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 构建报错“Duplicated files found in module xxx. This may cause unexpected errors at runtime”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:70f276a3acc7d4a9e254eebfceaf989126f4b7b9e37f4cbf9ded44602846c658
---

**问题现象**

编译构建时，出现错误信息“Duplicated files found in module xxx. This may cause unexpected errors at runtime”。

构建时存在不同版本的同名SO文件会导致问题。例如，将har模块产物中的SO文件拷贝到entry模块的libs目录下，此时har模块和entry模块中都有一个名为libhar.so的文件。如果再配置entry依赖har，构建entry时就会出现错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/JUYtwcOvRQiQvl6FaWC7ew/zh-cn_image_0000002654797905.png)

**解决措施**

使用select、pickFirsts、pickLasts等配置项选择要使用的.so文件。select提供对 native 产物的精准选择，优先级高于excludes、pickFirsts等配置项。pickFirsts和pickLasts按照.so文件的优先级顺序打包，优先级顺序基于依赖收集的顺序，越晚被收集的优先级越高。

具体可参考：[模块级build-profile.json5文件](../harmonyos-guides/ide-hvigor-build-profile.md)。

在entry/build-profile.json5中，配置select选中har模块中的so文件，package选中包名为har的模块，include选中libhar.so文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/H_fda3QlQz-bbpOFAVBHzg/zh-cn_image_0000002624638450.png)
