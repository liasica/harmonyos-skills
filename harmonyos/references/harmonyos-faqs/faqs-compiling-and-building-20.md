---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-20
title: 编译报错“please check deviceType or distroFilter/distributionFilter of the module”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“please check deviceType or distroFilter/distributionFilter of the module”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:52+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:c53f57f91e481b7eb0ea223c74ce7afd533fc98faae05662c0e1fb3266fe0bb8
---

**问题现象**

HarmonyOS DevEco Studio编译时出现错误，提示如下之一：

* Module: (xxx) and Module: (xxx) are entry, please check deviceType or distroFilter of the module.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/XN40q921SBW8V7WwP7j63g/zh-cn_image_0000002654797849.png)
* Module: (xxx) and Module: (xxx) have the same moduleName, please check deviceType or distroFilter of the module.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/7uQTSUVyREWSFRf-uwFIvw/zh-cn_image_0000002624638394.png)
* Module: (xxx) and Module: (xxx) have the same packageName, please check deviceType or distroFilter of the module.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/3V6KIqlXRbe1i07-GRv8gw/zh-cn_image_0000002654837803.png)
* Module: (xxx) and Module: (xxx) have the same ability name.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/RgrF24BhRUuzf7KhYaR5HA/zh-cn_image_0000002624478490.png)

**解决措施**

* 可能是打包时工程未满足HAP唯一性校验逻辑，请参考[HAP唯一性校验逻辑](../harmonyos-guides/ide-hvigor-verification-rule.md)修改工程配置，满足校验逻辑即可正常打包。
* 如果工程中仅有一种设备类型，请确保工程级build-profile.json5文件中，同一模块的不同目标target的applyToProducts字段对应的product不相同。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/X9P4h4Y0Q7S7ZqTUlxevsQ/zh-cn_image_0000002654797851.png)
