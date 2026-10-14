---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-multi-thread-check
title: 方舟运行时检测
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 方舟运行时检测
category: harmonyos-guides
scraped_at: 2026-10-15T07:06:49+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:107e0a1dd28fb1b0af124dfc3d49c65b549b5bda9a25a2549be7ba8faef87f3f
---

## 方舟多线程检测

在JS运行时环境中，多线程的安全问题是一个重要的考虑因素。由于JavaScript主线程是单线程的，在主线程中创建的JS对象（尤其是DOM相关对象）只能在主线程上进行操作。如果违反了这一规则，就会导致多线程安全问题。针对该场景，鸿蒙电脑DevEco Studio集成多线程检测能力，并通过FaultLog展示错误的堆栈详情及导致错误的代码行。关于多线程检测的原理请参考[原理介绍](../best-practices/bpta-stability-ark-runtime-detection.md#section18515155816101)。

开启多线程检测会有较大性能损耗，请开发者按需开启。

### 开启方舟多线程检测

可通过以下方式开启方舟多线程检测。

* **方式一**
  1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/HKCFRxdyQ_-1FzuzzoRQwg/zh-cn_image_0000002779608827.png)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/PfpgT2ErQxCJ9ll1dQHazg/zh-cn_image_0000002779728979.png "点击放大")按钮打开配置界面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/xo3wykotSmSXDFisgdfMyQ/zh-cn_image_0000002779728981.png)
  2. 在配置界面点击**故障分析**，勾选**多线程检测**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/aCM32IYKRcm7_g7QEcL6Ng/zh-cn_image_0000002750009910.png)

* **方式二**

  通过命令行开启。

  ```screen
  hdc shell aa start -a {abilityName} -b {bundleName} -R
  ```

### 使用方舟多线程检测

1. 运行或调试当前应用。
2. 当程序出现多线程安全问题时，会弹出Crash log信息，点击信息中的链接即可跳转至引起多线程安全问题的代码处。关于多线程安全问题的分析方法请参考[使用Node-API接口产生的异常日志/崩溃分析](use-napi-about-crash.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/weNV_-d6ShSHbvbHUX409g/zh-cn_image_0000002779728975.png)

## 方舟native模块加载异常信息增强

在进行ArkTS项目开发中可能存在需要加载native模块的场景，开启方舟native模块加载异常信息增强功能后，可以丰富ArkTS项目中因加载native模块导致的报错信息，以便更准确地进行native问题定位。

### 开启方舟native模块加载异常信息增强

可以通过以下两种方式开启方舟native模块加载异常信息增强。

* 方式一
  1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/w0h3AkxxRdGy2mZUXuzH_A/zh-cn_image_0000002779608833.png)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/A-Fd9n4oQv-ZlmRmmP9Hnw/zh-cn_image_0000002779728971.png "点击放大")按钮打开配置界面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/B4SLdKExTO2iz_LUNSCrbA/zh-cn_image_0000002750169810.png)
  2. 在配置界面点击**故障分析**，勾选**增强错误信息**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/_py_0rwqT0-JKlS2iF96ZA/zh-cn_image_0000002779608823.png)

* 方式二

  通过命令行开启。

  ```screen
  hdc shell aa start {abilityName} {bundleName} -E
  ```

### 使用方舟native模块加载异常信息增强

1. 运行或调试当前应用。
2. 当程序出现因native模块加载导致的报错信息时，会显示更详细准确的错误信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/SRJauSaZQRSqelrVQqTs4w/zh-cn_image_0000002779728977.png)
