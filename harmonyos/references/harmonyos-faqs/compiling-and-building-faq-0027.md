---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0027
title: build-profile.json5配置编译报错问题排查
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > build-profile.json5配置编译报错问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:51+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:dc9ba116cb3ba5164031a8ed1e2bf0a97bbf19b6a8dc8fc0a8d53513353bd7cf
---

**Q：编译报错“The required attribute module-srcPath is missing”。**

**A**：错误描述：缺少必需属性：module-srcPath。

可能原因：build-profile.json5文件中缺少模块的相对路径，具体表现为module-srcPath字段缺失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/fawzmO8ES0GJxuEN6FiuWw/zh-cn_image_0000002802195783.png "点击放大")

解决措施：进入项目根目录下的build-profile.json5文件，确保module下srcPath字段存在且非空。

**Q：编译报错“useNormalizedOHMUrl can be true only when Compatible SDK Version is 5.0.0 (12) or later”？**

**A**：错误描述：仅当兼容SDK版本为5.0.0(12)及以上版本时，useNormalizedOHMUrl才可以设置为true。

可能原因：当compatibleSdkVersion为5.0.0(12)以下版本时，设置useNormalizedOHMUrl为true导致。

解决措施：检查工程级build-profile.json5文件中的compatibleSdkVersion配置。如果compatibleSdkVersion为 4.1.0(11) 及之前版本，请将[useNormalizedOHMUrl](../harmonyos-guides/ide-hvigor-build-profile-app.md#section13181758123312)设置为false。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/1YWZh4huRH-Gh61VoZ4nNQ/zh-cn_image_0000002773075918.png "点击放大")

**Q：编译报错“please check deviceType or distroFilter/distributionFilter of the module”，HarmonyOS DevEco Studio编译时出现错误，提示如下之一：**

* Module: (xxx) and Module: (xxx) are entry, please check deviceType or distroFilter of the module.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/eBnWwBqwRCyoDwUfTelh8A/zh-cn_image_0000002802275689.png "点击放大")
* Module: (xxx) and Module: (xxx) have the same moduleName, please check deviceType or distroFilter of the module.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/sIPBA213TuCR_mf-dsrevA/zh-cn_image_0000002772915952.png "点击放大")
* Module: (xxx) and Module: (xxx) have the same packageName, please check deviceType or distroFilter of the module.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/6LD56F5hSkOf19oRTfSR2A/zh-cn_image_0000002802195789.png "点击放大")
* Module: (xxx) and Module: (xxx) have the same ability name.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/whKk_AX7RRWK1nVLjGgoxg/zh-cn_image_0000002773075924.png "点击放大")

**A**：解决措施如下：

* 可能是打包时工程未满足HAP唯一性校验逻辑，请参考[HAP唯一性校验逻辑](../harmonyos-guides/ide-hvigor-verification-rule.md)修改工程配置，满足校验逻辑即可正常打包。
* 如果工程中仅有一种设备类型，请确保工程级build-profile.json5文件中，同一模块的不同目标target的applyToProducts字段对应的product不相同。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/9OlbZfkzTiqCH70D9aQzIA/zh-cn_image_0000002802275697.png)

**Q：编译时未出现异常，但编译构建失败，提示“Property xxx does not exist on type 'typeof BuildProfile'”，使用了自定义参数BuildProfile，如何解决？**

**A**：检查当前模块下build-profile.json5文件中的targets > buildProfileFields配置的自定义参数的key值是否一致。如果不一致，请将 targets内所有buildProfileFields的key值统一。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/OiC59MVASIaQh8E_EB05ng/zh-cn_image_0000002772914818.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/TloMVYsEROWWvZLaTo1A7A/zh-cn_image_0000002802274539.png)

**Q：HSP模块对外提供的接口中使用了HAP未定义的自定义参数buildProfileFields，导致编译失败，提示“Property 'XX' does not exist on type 'typeof BuildProfile'”，如何解决？**

**A**：解决该问题的两种方法：

1. 在HAP中配置与HSP相同的自定义参数BuildProfileFields。
2. 将与HSP相同的自定义参数buildProfileFields配置到工程级 build-profile.json5 中，这会使HSP中的自定义参数在全局生效。

**Q：编译时标红，原因是使用了自定义参数BuildProfile，编译器提示“Property xxx does not exist on type 'typeof BuildProfile'”，导致构建失败，如何解决？**

**A**：请检查当前模块下的build-profile.json5文件中buildProfileFields内是否已添加所使用的自定义参数，确保该参数已配置在buildProfileFields内。
