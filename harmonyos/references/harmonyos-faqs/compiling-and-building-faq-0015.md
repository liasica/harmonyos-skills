---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0015
title: 编译报错“Cannot read properties of undefined (reading 'split')”问题排查
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > 编译报错“Cannot read properties of undefined (reading 'split')”问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:51+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:ac05cc94a8af58d8c225f6528daeeb19d959e4c1d4b259cf08832d561e1c8175
---

**Q：当前使用的DevEco Studio版本与SDK版本不配套，导致DevEco Studio抛出异常：“TypeError: Cannot read properties of undefined (reading 'split')”，如何解决？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/wPYjBlPbQ5SBDt4_0r2RRg/zh-cn_image_0000002772204844.png "点击放大")

**A**：解决措施如下：

1. 访问华为[开发者官网](https://developer.huawei.com/consumer/cn/download/deveco-studio)下载最新版DevEco Studio。
2. 使用新版本DevEco Studio打开待迁移项目。
3. 根据DevEco Studio自动弹出的迁移提示进行操作。
   * 点击“Migrate Assistant”功能。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/NjddGryGRCWJ9A16Preo6g/zh-cn_image_0000002801444643.png "点击放大")
   * 从版本列表中选择目标迁移版本。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/KjZz-GF3QCSAiwOTiOT2-w/zh-cn_image_0000002772044894.png "点击放大")
   * 按照向导完成项目迁移流程。

**Q：当工程级 build-profile.json5 文件未配置工程外模块依赖，而模块级 oh-package.json5 声明了工程外模块依赖并在代码中实际引用时，编译阶段会抛出异常：“Error: Cannot read properties of undefined (reading 'split')”，如何解决？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/-Lupx7COTJqsQw9VUpiScQ/zh-cn_image_0000002801444657.png "点击放大")

**A**：解决措施如下：

1. 检查下报错子模块中所引用的依赖，确保目标模块已在工程级 build-profile.json5 文件的 modules 字段中正确声明。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/klbnNiuOQ8eLL25al0nZ6A/zh-cn_image_0000002801324795.png)
2. 确认当前子模块的 oh-package.json5 中，该模块已添加到 dependencies 依赖列表。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/-psJsVHqQqucxdPp6jeYsw/zh-cn_image_0000002772204922.png)
3. 若发现配置缺失，请手动补充完整。删除项目中的 oh\_modules 缓存目录，然后重新执行编译。

**Q：在HAP依赖字节码HAR进行编译的场景下，当import语句中的模块别名与dependencies中声明的别名大小写不一致时，编译系统将无法正确识别该依赖为字节码HAR，进而导致编译错误，如何解决？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/uJ5WD5cJT6isBFzTwSLyaA/zh-cn_image_0000002772204930.png "点击放大")

**A**：请检查并确保所有import语句的模块别名与其在dependencies中的声明保持完全一致的大小写格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/mB3pEqrITZa1ugcnit393g/zh-cn_image_0000002801444725.png "点击放大")

**Q：在编译字节码HAR时，若将依赖配置于devDependencies下，hvigor构建系统在编译阶段不会收集devDependencies中的依赖项，导致依赖解析失败并引发编译错误，如何解决？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/qf6fsZMWSHGTIr_LlgQzAA/zh-cn_image_0000002772044970.png "点击放大")

**A**：请将依赖项从devDependencies移至dependencies。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/Zu3Dc66NTXmkeJlU0IzMlQ/zh-cn_image_0000002801324813.png "点击放大")
