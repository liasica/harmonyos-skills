---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-40
title: 使用DevEco Studio执行单元测试脚本常见问题和解决方案
breadcrumb: FAQ > DevEco Studio > 应用测试 > 使用DevEco Studio执行单元测试脚本常见问题和解决方案
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:36+08:00
doc_updated_at: 2026-08-05
content_hash: sha256:e9f499228238789816fb3528f171045818c8f76dc88d39aa0a095e5cc6848fa3
---

## 问题现象

* **问题一：**

  单元测试debug运行时卡住：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/zlShtgbFSt-kGD00aIr_Iw/zh-cn_image_0000002688438687.png "点击放大")
* **问题二：**

  使用Instrument Test调用getContext()报错"Error in xxx, Parameter error. The context is invalid."。
* **问题三：**

  在UI测试框架中如何通过resourceManager来获得string.json里的内容？
* **问题四：**

  @ohos/hypium仓库强制升级至1.0.23，提示需要API版本升级至5.0.5（17）对用户体验不友好，若用户升级应用，是否需要同步升级系统版本？是否有什么降级方案？
* **问题五：**

  针对A组件的a方法编写单元测试脚本，a方法内引用了B组件的b方法，那么在执行单元测试时，方法a是否会调用方法b？
* **问题六：**

  集成态HSP执行Local Test时无法运行，一直处于running状态，如何解决？
* **问题七：**

  单元测试中调用SysTestKit.existKeyword方法，获取到的结果是一直false，如何解决？
* **问题八：**

  单元测试用例执行15000ms后会超时退出，如何解决？
* **问题九：**

  在src/main/module.json5中申请相关权限，执行Instrument Test用例会超时，如何解决？
* **问题十：**

  执行模块单元测试时，ohosTest会同时编译全量包和模块测试包，多一轮全量编译导致单测执行速度较慢，如何指定只编译test包以提高单测效率？

## 解决方案

* **问题一解决方案：**

  单击工具栏help->Show Log in Explorer，跳转到previewer.log所在路径，找到previewer.log并打开，发现报错提示"module name not exist"：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/vm7RPUhQRICYIZTR3OBGpg/zh-cn_image_0000002658559890.png "点击放大")

  即用户引用了不存在的模块，建议用户排查工程中引用的模块，把报错模块的编译产物删除，再重新编译。
* **问题二解决方案：**

  在测试脚本中，直接使用getContext()会报错"Error in xxx, Parameter error. The context is invalid."。可以通过[AbilityDelegator.getAppContext](../harmonyos-references/js-apis-inner-application-abilitydelegator.md#getappcontext9)获取应用的Context。
* **问题三解决方案：**

  可以基于问题二的解决方案，获取到应用的Context，通过Context获取[resourceManager](../harmonyos-references/js-apis-resource-manager.md)，参考[getStringValue](../harmonyos-references/js-apis-resource-manager.md#getstringvalue9)的用法即可。
* **问题四解决方案：**

  IDE新建工程目录后会在oh-package.json5文件自动生成配套@ohos/hypium的具体版本号，hypium和工具链没有强配套关系，不需要写到工具配套里去。
* **问题五解决方案：**

  执行单元测试时，a方法会自动调用b方法。
* **问题六解决方案：**

  请使用DevEco Studio 6.0.1 Release Build Version:6.0.1.260及之后的版本。
* **问题七解决方案：**

  请使用DevEco Studio 6.0.2 Release Build Version:6.0.2.640及之后的版本，且配套的@ohos/hypium需为"1.0.25"及之后的版本。
* **问题八解决方案：**

  方案一：在DevEco Studio中Run/Debug Configurations中修改用例执行超时配置参数，避免用例执行超时。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/JXsuFFHRQLWtVh3c1Qn3lw/zh-cn_image_0000002688559699.png "点击放大")

  方案二：用例执行超时时长配置参考以下命令，timeout为测试用例执行的超时时间，正整数（单位ms），如不设置默认为5000ms：hdc shell aa test -b xxx -m xxx -s unittest OpenHarmonyTestRunner -s timeout 15000。

  同时要确保用例代码逻辑正确，即使断言失败场景也能保证用例执行结束，这可以避免用例因未及时执行到done函数而导致的超时错误。

  **说明** 

  以上方案只支持Instrument Test测试用例，Local Test测试用例不支持修改超时时间。
* **问题九解决方案：**

  在Instrument Test中执行用例，src/ohosTest/module.json5中同样需要申请相关权限。具体可参考[在配置文件中声明权限](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)。
* **问题十解决方案：**

  当前暂不支持指定只编译test包以提高单测效率。
