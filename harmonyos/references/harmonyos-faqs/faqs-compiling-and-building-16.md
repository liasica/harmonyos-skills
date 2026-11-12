---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-16
title: 应用/服务的启动界面信息缺失，提示“Schema validate failed”报错
breadcrumb: FAQ > DevEco Studio > 编译构建 > 应用/服务的启动界面信息缺失，提示“Schema validate failed”报错
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:73f25c8a04f62a396eae668277909c91f4226c163f23b859472408d30e2dd141
---

**问题现象**

在工程同步或编译构建时，出现“Schema validate failed”的错误提示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/AoxDriVkRg-9VVoYWIuxEA/zh-cn_image_0000002654837795.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=27315685BC0DA9A76A82A34E61CDB5290C936B837C6127EECA221FD8EE880235)

**解决措施**

在开发应用/服务时，创建工程后，默认设置了启动界面信息。如果开发者误删其中某个字段，将导致报错。下面以重新设置启动界面信息为例，为提高冷启动性能，可以通过以下方式设置启动界面的图标和背景颜色。

1. 在模块的**resources > base > element**目录下，右键点击并选择**New > Element Resource File**来创建资源文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/BHl-EnW1Q-ubLntW2m3gdA/zh-cn_image_0000002624478484.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=F571B97959FB41AAA0454118F8C0867BD6B5D22459F032C481D27CA9A718368B)
2. 在弹出的对话框中，开发者可以自定义“File name”，例如 color；“Root element”请选择 **color**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/qML8wroZRcqMyl9jhbofug/zh-cn_image_0000002654797845.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=DAF575B576C3CEF1455E15E83731925E34D53AA4B91BB344C925D808326517B2)

   创建完成后，color.json文件如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/Nlu2p0RUR8-2TQE96wKgkQ/zh-cn_image_0000002624638390.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=F2057D8BD4A6DE97F0F136575AFAAAAB595659B11D87314AB96227388EC0BF84)
3. 将[2](faqs-compiling-and-building-16.md#zh-cn_topic_0000001233028585_li124901748185712)创建的color.json文件拷贝至模块的**ohosTest > resources > base > element**目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/_zU0Sn8gTCaBKGmOpldgvA/zh-cn_image_0000002654837797.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=B03E45DFC1B61A922CCDAC4DE830799677ACB3B4F0906CD25646B815EBBB4FA3)
4. 在模块的**src > main > module.json5**文件的abilities数组中，添加startWindowIcon和startWindowBackground字段。若缺少任一字段，将出现ERROR: Schema validate failed报错。startWindowIcon字段索引模块下**resources > base > media**中的图标资源，startWindowBackground字段索引**resources > base > element > color.json**中的颜色。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/dlVlcoQkTia7YT8XDzKavQ/zh-cn_image_0000002624478486.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=47A921554A92D9B1CAF7AC2A70883CB700D6043BEBBA7E24040DCA9ADE0D9CA2)
5. 在**src > ohosTest > module.json5**文件的abilities数组中，添加startWindowIcon和startWindowBackground字段。其中，startWindowIcon字段引用模块ohosTest下 **resources > base > media**中的图标资源，startWindowBackground字段引用 **resources > base > element > color.json**中的颜色。
