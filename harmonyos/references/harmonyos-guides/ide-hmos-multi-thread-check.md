---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-multi-thread-check
title: 方舟运行时检测
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 方舟运行时检测
category: harmonyos-guides
scraped_at: 2026-11-04T08:31:48+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:79f7892d2fd3ec80541436306dc7738e9f25822a3b805a863b017cd0daf5fda9
---

## 方舟多线程检测

在JS运行时环境中，多线程的安全问题是一个重要的考虑因素。由于JavaScript主线程是单线程的，在主线程中创建的JS对象（尤其是DOM相关对象）只能在主线程上进行操作。如果违反了这一规则，就会导致多线程安全问题。针对该场景，鸿蒙电脑DevEco Studio集成多线程检测能力，并通过FaultLog展示错误的堆栈详情及导致错误的代码行。关于多线程检测的原理请参考[原理介绍](../best-practices/bpta-stability-ark-runtime-detection.md#section18515155816101)。

开启多线程检测会有较大性能损耗，请开发者按需开启。

### 开启方舟多线程检测

可通过以下方式开启方舟多线程检测。

* **方式一**
  1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/wmqBr_2iQKSCiW-aR5Emrg/zh-cn_image_0000002779608827.png)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/mvAeSszXTVaQKT5031J8ug/zh-cn_image_0000002779728979.png "点击放大")按钮打开配置界面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/jRRIjhv5Twaug4TyUfDT1Q/zh-cn_image_0000002779728981.png)
  2. 在配置界面点击**故障分析**，勾选**多线程检测**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/o8MQ8u3LQsa9ofu7fwYFVA/zh-cn_image_0000002750009910.png)

* **方式二**

  通过命令行开启。

  ```screen
  hdc shell aa start -a {abilityName} -b {bundleName} -R
  ```

### 使用方舟多线程检测

1. 运行或调试当前应用。
2. 当程序出现多线程安全问题时，会弹出Crash log信息，点击信息中的链接即可跳转至引起多线程安全问题的代码处。关于多线程安全问题的分析方法请参考[使用Node-API接口产生的异常日志/崩溃分析](use-napi-about-crash.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/Y8nQnhZWRw-7q5auhmjV8g/zh-cn_image_0000002779728975.png)

## 方舟native模块加载异常信息增强

在进行ArkTS项目开发中可能存在需要加载native模块的场景，开启方舟native模块加载异常信息增强功能后，可以丰富ArkTS项目中因加载native模块导致的报错信息，以便更准确地进行native问题定位。

### 开启方舟native模块加载异常信息增强

可以通过以下两种方式开启方舟native模块加载异常信息增强。

* 方式一
  1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/K-AvX7YsSKWUZMemmD_xIw/zh-cn_image_0000002779608833.png)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/K1vL-sH9Q52JFNzil3kY2g/zh-cn_image_0000002779728971.png "点击放大")按钮打开配置界面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/Z-9i6dMHSoeah695bRAr3w/zh-cn_image_0000002750169810.png)
  2. 在配置界面点击**故障分析**，勾选**增强错误信息**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/aFi05KUYQKyzDrkAaIjW9w/zh-cn_image_0000002779608823.png)

* 方式二

  通过命令行开启。

  ```screen
  hdc shell aa start {abilityName} {bundleName} -E
  ```

### 使用方舟native模块加载异常信息增强

1. 运行或调试当前应用。
2. 当程序出现因native模块加载导致的报错信息时，会显示更详细准确的错误信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/UvELrehATba6-AV53pqWvg/zh-cn_image_0000002779728977.png)
