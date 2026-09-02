---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-34
title: 项目入口的Ability配置错误，导致项目启动白屏
breadcrumb: FAQ > DevEco Studio > 工程管理 > 项目入口的Ability配置错误，导致项目启动白屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:965a2a795b518d510ea44fb6889a351680ab4f861f9c90a3cc2b242ccb7b7c22
---

## 问题现象

工程中存在多个模块，其中包括HAP模块hapA中依赖了HAR模块harA，现在选择模块hapA，然后启动项目后，应用界面呈现白屏。工程目录如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/LpjXK-VcQTmHVejr7kJ4qA/zh-cn_image_0000002628567966.png "点击放大")

## 背景知识

* HAP是应用安装和运行的基本单元。HAP包是由代码、资源、第三方库、配置文件等打包生成的模块包，其主要分为两种类型：entry和feature。详情可参考[HAP](../harmonyos-guides/hap-package.md)。
* HAR是静态共享包，可以包含代码、C++库、资源和配置文件。通过HAR可以实现多个模块或多个工程共享ArkUI组件、资源等相关代码。HAR不支持在设备上单独安装或运行，只能作为应用模块的依赖项被引用。详情可参考[HAR](../harmonyos-guides/har-package.md)。
* Stage模型应用程序中，HAR模块支持在配置文件中声明UIAbility组件，但不支持在配置文件中声明page页面，可以包含page页面，并通过[命名路由](../harmonyos-guides/arkts-routing.md#命名路由)的方式进行跳转，详情可参考[Stage模型应用程序包结构](../harmonyos-guides/application-package-structure-stage.md)选择合适的包类型。

## 问题定位

* 在DevEco中展开HAR模块harA的模块目录，检查下是否模块创建后手动添加了UIAbility组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/-T2QGj7zRzut2QyK37VjBg/zh-cn_image_0000002658927287.png)
* 在DevEco中依次选择“hapA”-“Edit Configurations”-“Launch Options”-“Ability”,查看项目入口的Ability配置的是否正确。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/gkpMwar4Tlm_D7dlzhwucw/zh-cn_image_0000002658807331.png)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/PxSCGeQuT6iVnbE9JoOHHw/zh-cn_image_0000002628408070.png "点击放大")

## 分析结论

在选择模块hapA启动项目时，由于模块harA中手动添加并声明了UIAbility组件，而HAR模块中不支持在配置文件中声明page页面，模块hapA依赖了harA，项目入口的Ability配置成了模块harA的UIAbility，所以启动后应用呈现白屏。

## 修改建议

在DevEco中依次选择“hapA”-“Edit Configurations”-“Launch Options”-“Ability”,将项目入口的Ability配置成模块hapA的UIAbility。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/oELakd_wQ0SIbjs7Rgejnw/zh-cn_image_0000002628567970.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/jMUzFQCnTD-3Gzm8ATnVXg/zh-cn_image_0000002658927289.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/u40XEXiRQ-WFcE1VoPG2kw/zh-cn_image_0000002658807335.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/jZJxSA_iQ7WxK43WHDVE9w/zh-cn_image_0000002628408074.png "点击放大")
