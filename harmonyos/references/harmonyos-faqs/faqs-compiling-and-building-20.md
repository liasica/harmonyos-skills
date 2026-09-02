---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-20
title: 编译报错“please check deviceType or distroFilter/distributionFilter of the module”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“please check deviceType or distroFilter/distributionFilter of the module”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:25+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8aa526308ed5c9691c229538bbfca260dd4dd2fc1ccf03660215fde36c98bee8
---

**问题现象**

HarmonyOS DevEco Studio编译时出现错误，提示如下之一：

* Module: (xxx) and Module: (xxx) are entry, please check deviceType or distroFilter of the module.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/pkwq_9RuSvyatlRt5LXt-A/zh-cn_image_0000002229604261.png)
* Module: (xxx) and Module: (xxx) have the same moduleName, please check deviceType or distroFilter of the module.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/yKd1BACCQmOQecgl7mSxCA/zh-cn_image_0000002194158880.png)
* Module: (xxx) and Module: (xxx) have the same packageName, please check deviceType or distroFilter of the module.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/GofzxongTOmso_KPXP--BQ/zh-cn_image_0000002194318488.png)
* Module: (xxx) and Module: (xxx) have the same ability name.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/zUABTNt4SnqmiVrRm3_-mw/zh-cn_image_0000002194318492.png)

**解决措施**

* 可能是打包时工程未满足HAP唯一性校验逻辑，请参考[HAP唯一性校验逻辑](../harmonyos-guides/ide-hvigor-verification-rule.md)修改工程配置，满足校验逻辑即可正常打包。
* 如果工程中仅有一种设备类型，请确保工程级build-profile.json5文件中，同一模块的不同目标target的applyToProducts字段对应的product不相同。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/rOTuWf9jRKqOta3di72lAA/zh-cn_image_0000002194158884.png)
