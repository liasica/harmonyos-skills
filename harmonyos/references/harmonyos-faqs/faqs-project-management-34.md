---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-34
title: 项目入口的Ability配置错误，导致项目启动白屏
breadcrumb: FAQ > DevEco Studio > 工程管理 > 项目入口的Ability配置错误，导致项目启动白屏
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:eef4215e1b742a488c68dcf50e416cee9c3f8dc80c86d9dd944c9898acb9a324
---

## 问题现象

工程中存在多个模块，其中包括HAP模块hapA中依赖了HAR模块harA，现在选择模块hapA，然后启动项目后，应用界面呈现白屏。工程目录如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/yIvezrz1S5mha6U1q-9x6A/zh-cn_image_0000002628567966.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=A2FD92018A9420A1E7E28A82C9482DE6CD23093C727CDEBC006FD44037E6DAF5 "点击放大")

## 背景知识

* HAP是应用安装和运行的基本单元。HAP包是由代码、资源、第三方库、配置文件等打包生成的模块包，其主要分为两种类型：entry和feature。详情可参考[HAP](../harmonyos-guides/hap-package.md)。
* HAR是静态共享包，可以包含代码、C++库、资源和配置文件。通过HAR可以实现多个模块或多个工程共享ArkUI组件、资源等相关代码。HAR不支持在设备上单独安装或运行，只能作为应用模块的依赖项被引用。详情可参考[HAR](../harmonyos-guides/har-package.md)。
* Stage模型应用程序中，HAR模块支持在配置文件中声明UIAbility组件，但不支持在配置文件中声明page页面，可以包含page页面，并通过[命名路由](../harmonyos-guides/arkts-routing.md#命名路由)的方式进行跳转，详情可参考[Stage模型应用程序包结构](../harmonyos-guides/application-package-structure-stage.md)选择合适的包类型。

## 问题定位

* 在DevEco中展开HAR模块harA的模块目录，检查下是否模块创建后手动添加了UIAbility组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/OVIbH4HfRjK9Ek_AA81QVw/zh-cn_image_0000002658927287.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=02E2B8E0D26D08FE5A3D4583991D12C456A6F727B69D56142F7EAFCB329C95BD)
* 在DevEco中依次选择“hapA”-“Edit Configurations”-“Launch Options”-“Ability”,查看项目入口的Ability配置的是否正确。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/qzM6LSF3Sf61uiwHvD89_A/zh-cn_image_0000002658807331.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=C647DF94BE8977CB214373CB355A94BB12AC1F9ED83F8940DC3A7FB17AA53DB0)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/pwQNto-pTb2pJHmGf3F6vg/zh-cn_image_0000002628408070.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=D666CB7E3B78E0998D60F573791C6E46CA903FB1D22B15EB3F9B92429EF9DF8D "点击放大")

## 分析结论

在选择模块hapA启动项目时，由于模块harA中手动添加并声明了UIAbility组件，而HAR模块中不支持在配置文件中声明page页面，模块hapA依赖了harA，项目入口的Ability配置成了模块harA的UIAbility，所以启动后应用呈现白屏。

## 修改建议

在DevEco中依次选择“hapA”-“Edit Configurations”-“Launch Options”-“Ability”,将项目入口的Ability配置成模块hapA的UIAbility。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/CRm6aNcIR-CloVLalh59cw/zh-cn_image_0000002628567970.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=A2938575020BA584B19592E25B283447EFED363AC3E0557381E4844832AB8638)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/hl7pxYkpRw66UmQgYyOiHw/zh-cn_image_0000002658927289.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=717013221E67CA5ABB2744A633029DD579264DB03195D709F15B6545D12E3F59 "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/n9FnXiIPTfC58pLH7Udh4A/zh-cn_image_0000002658807335.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=2939BCC34D90010560A5112AE048C221B2AA88FE3E42DBDEE1C6A1A154A82D74 "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/I8kpg_KaQGy3rlNh1hqTLw/zh-cn_image_0000002628408074.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=ACBBC5E40F07DA52CD6B18B1804CA6E338D2C4D5E0BD68D8EDE19284863845F3 "点击放大")
