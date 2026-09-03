---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-multi-thread-check
title: 方舟运行时检测
breadcrumb: 指南 > 编写与调试应用 > 日志与故障分析 > 故障分析 > 方舟运行时检测
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c9c264e8415a71fa479a91722bbf0d063e2303631c391ab4b495c82c93d337ab
---

## 方舟多线程检测

在JS运行时环境中，多线程的安全问题是一个重要的考虑因素。由于JavaScript主线程是单线程的，在主线程中创建的JS对象（尤其是DOM相关对象）只能在主线程上进行操作。如果违反了这一规则，就会导致多线程安全问题。针对该场景，DevEco Studio集成多线程检测能力，并通过FaultLog展示错误的堆栈详情及导致错误的代码行。关于多线程检测的原理请参考[原理介绍](../best-practices/bpta-stability-ark-runtime-detection.md#section18515155816101)。

开启多线程检测会有较大性能损耗，请开发者按需开启。

### 开启方舟多线程检测

可通过以下方式开启方舟多线程检测。

* **方式一**

  点击**Run > Edit Configurations >** **Diagnostics**，勾选**Multi Thread Check**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/nZzhf-3URZmGzuhafshUOQ/zh-cn_image_0000002701823648.png)

* **方式二**

  通过命令行开启。

  ```bash
  hdc shell aa start -a {abilityName} -b {bundleName} -R
  ```

* **方式三**

  通过调用[setMultithreadingDetectionEnabled接口](../harmonyos-references/js-apis-util.md#setmultithreadingdetectionenabled23)开启。

### 使用方舟多线程检测

1. 运行或调试当前应用。
2. 当程序出现多线程安全问题时，会弹出Crash log信息，点击信息中的链接即可跳转至引起多线程安全问题的代码处。关于多线程安全问题的分析方法请参考[使用Node-API接口产生的异常日志/崩溃分析](use-napi-about-crash.md)。

   如果是通过方式三调用setMultithreadingDetectionEnabled接口开启，发生多线程安全问题时，该接口支持应用崩溃和不崩溃两种场景。若设置为崩溃，则应用退出并生成cppcrash日志；若设置为不崩溃，应用不会退出，同时生成arktsenvsan日志，此时应用可通过[hiAppEvent订阅地址越界事件](hiappevent-watcher-address-sanitizer-events-arkts.md)来感知多线程安全问题，并生成hilog日志。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/xa3WInLdT_2G9VOWLzGpGQ/zh-cn_image_0000002701663728.png)

## 方舟native模块加载异常信息增强

在进行ArkTS项目开发中可能存在需要加载native模块的场景，开启方舟native模块加载异常信息增强功能后，可以丰富ArkTS项目中因加载native模块导致的报错信息，以便更准确地进行native问题定位。

### 开启方舟native模块加载异常信息增强

可以通过以下两种方式开启方舟native模块加载异常信息增强。

* 方式一

  点击**Run > Edit Configurations >** **Diagnostics**，勾选**Enhanced Error Info**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/p2nMbVygSOORkaH_kRb0sQ/zh-cn_image_0000002731542921.png)

* 方式二

  通过命令行开启。

  ```bash
  hdc shell aa start {abilityName} {bundleName} -E
  ```

### 使用方舟native模块加载异常信息增强

1. 运行或调试当前应用。
2. 当程序出现因native模块加载导致的报错信息时，会显示更详细准确的错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/Fd5Cl2KwR3S6E60pX_OJ2w/zh-cn_image_0000002701823644.png)
