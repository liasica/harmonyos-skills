---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-16
title: 应用/服务的启动界面信息缺失，提示“Schema validate failed”报错
breadcrumb: FAQ > DevEco Studio > 编译构建 > 应用/服务的启动界面信息缺失，提示“Schema validate failed”报错
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b975e079a1fd82b473cb24d0563c30d5d9b1248750df20d732d5b78525cb80f1
---

**问题现象**

在工程同步或编译构建时，出现“Schema validate failed”的错误提示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/GnGGwfbZSfCd2OgSntf0kQ/zh-cn_image_0000002229604277.png?HW-CC-KV=V1&HW-CC-Date=20260428T002909Z&HW-CC-Expire=86400&HW-CC-Sign=8FE67FDC83E79479368D3298DF51FE6F7709CCDDEACC1AE0DE0670A62FDB3FD3)

**解决措施**

在开发应用/服务时，创建工程后，默认设置了启动界面信息。如果开发者误删其中某个字段，将导致报错。下面以重新设置启动界面信息为例，为提高冷启动性能，可以通过以下方式设置启动界面的图标和背景颜色。

1. 在模块的**resources > base > element**目录下，右键点击并选择**New > Element Resource File**来创建资源文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/_PZCohmQSg2GqTyxVgQQjQ/zh-cn_image_0000002194318512.png?HW-CC-KV=V1&HW-CC-Date=20260428T002909Z&HW-CC-Expire=86400&HW-CC-Sign=8305F1873FE1664FF0002F066E004D7A3FBF97C213904E83D7E7616B1D3D6F6C)
2. 在弹出的对话框中，开发者可以自定义“File name”，例如 color；“Root element”请选择 **color**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/Z-FL6ZQlSa61_L4PvTAXCw/zh-cn_image_0000002194158900.png?HW-CC-KV=V1&HW-CC-Date=20260428T002909Z&HW-CC-Expire=86400&HW-CC-Sign=6DC886CD4C83F2CB74DE2B7CD79AA81F0A550CAE8E69C7BEA6E1B484F5CF0BF6)

   创建完成后，color.json文件如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/npSKNcRmT0KEoOP2-HirVw/zh-cn_image_0000002194318508.png?HW-CC-KV=V1&HW-CC-Date=20260428T002909Z&HW-CC-Expire=86400&HW-CC-Sign=CAEB0F57B65915B2595481DF19938F9FE708774A07B4856BB5894703694E6DA7)
3. 将[2](faqs-compiling-and-building-16.md#zh-cn_topic_0000001233028585_li124901748185712)创建的color.json文件拷贝至模块的**ohosTest > resources > base > element**目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/6G-R42gPT1iCSEXqZE3R0Q/zh-cn_image_0000002229604281.png?HW-CC-KV=V1&HW-CC-Date=20260428T002909Z&HW-CC-Expire=86400&HW-CC-Sign=DE78B062591036C4B7BE99A8CB06EDB268AD12B95AF740D62428C909A4230D7C)
4. 在模块的**src > main > module.json5**文件的abilities数组中，添加startWindowIcon和startWindowBackground字段。若缺少任一字段，将出现ERROR: Schema validate failed报错。startWindowIcon字段索引模块下**resources > base > media**中的图标资源，startWindowBackground字段索引**resources > base > element > color.json**中的颜色。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/Lqy8hztnRoCEQ7rz3vOmeg/zh-cn_image_0000002194318504.png?HW-CC-KV=V1&HW-CC-Date=20260428T002909Z&HW-CC-Expire=86400&HW-CC-Sign=A7A9E8B09373D2A4BBCFAE1434A481916B130F42B5C380142EF40C3B25E68D73)
5. 在**src > ohosTest > module.json5**文件的abilities数组中，添加startWindowIcon和startWindowBackground字段。其中，startWindowIcon字段引用模块ohosTest下 **resources > base > media**中的图标资源，startWindowBackground字段引用 **resources > base > element > color.json**中的颜色。
