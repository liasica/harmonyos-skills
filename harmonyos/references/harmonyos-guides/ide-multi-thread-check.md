---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-multi-thread-check
title: 方舟运行时检测
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 方舟运行时检测
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:01+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:b3dd07cc8cc8cdfa6a10eb87f9ac1cdda02a2ca7f92782a29ca606641a3d3893
---

## 方舟多线程检测

在JS运行时环境中，多线程的安全问题是一个重要的考虑因素。由于JavaScript主线程是单线程的，在主线程中创建的JS对象（尤其是DOM相关对象）只能在主线程上进行操作。如果违反了这一规则，就会导致多线程安全问题。针对该场景，DevEco Studio集成多线程检测能力，并通过FaultLog展示错误的堆栈详情及导致错误的代码行。关于多线程检测的原理请参考[原理介绍](../best-practices/bpta-stability-ark-runtime-detection.md#section18515155816101)。

开启多线程检测会有较大性能损耗，请开发者按需开启。

### 开启方舟多线程检测

可通过以下方式开启方舟多线程检测。

* **方式一**

  点击**Run > Edit Configurations >** **Diagnostics**，勾选**Multi Thread Check**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/vaCPhRcRQm-b65n2FXz-cA/zh-cn_image_0000002779567500.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=13CF7356CE205500DBC97401FBCB0D47E5CF08AAEBC277D50ECF12E327839605)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/YdirOZTTS_WspRzWxWcPvg/zh-cn_image_0000002808767079.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=594EA745885B15F70F8796A07DB8E2B87321B5CB95F9ECD3CD8AC0430426A4D7)

## 方舟native模块加载异常信息增强

在进行ArkTS项目开发中可能存在需要加载native模块的场景，开启方舟native模块加载异常信息增强功能后，可以丰富ArkTS项目中因加载native模块导致的报错信息，以便更准确地进行native问题定位。

### 开启方舟native模块加载异常信息增强

可以通过以下两种方式开启方舟native模块加载异常信息增强。

* 方式一

  点击**Run > Edit Configurations >** **Diagnostics**，勾选**Enhanced Error Info**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/SNaa0OCAQ42wDnHpCvSkRw/zh-cn_image_0000002808887161.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=903CF705E5726B11AF107A3B6C3536BF70E67F343167F0F65C3CAF57423C1DB8)

* 方式二

  通过命令行开启。

  ```bash
  hdc shell aa start {abilityName} {bundleName} -E
  ```

### 使用方舟native模块加载异常信息增强

1. 运行或调试当前应用。
2. 当程序出现因native模块加载导致的报错信息时，会显示更详细准确的错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/fZL6KywwRWKxN7PZ7GHjmw/zh-cn_image_0000002779407524.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=864DA92142CA2F6C183FE8C618412A28E02D8B82568DFA10A18CEAD498055175)
