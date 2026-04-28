---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-multi-thread-check
title: 方舟运行时检测
breadcrumb: 指南 > 编写与调试应用 > 日志与故障分析 > 故障分析 > 方舟运行时检测
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0911cd55f08ae0604c9261945ebfd6aa931a5eee4c4232645ee0e11558baf037
---

## 方舟多线程检测

在JS运行时环境中，多线程的安全问题是一个重要的考虑因素。由于JavaScript主线程是单线程的，在主线程中创建的JS对象（尤其是DOM相关对象）只能在主线程上进行操作。如果违反了这一规则，就会导致多线程安全问题。针对该场景，DevEco Studio集成多线程检测能力，并通过FaultLog展示错误的堆栈详情及导致错误的代码行。关于多线程检测的原理请参考[原理介绍](../best-practices/bpta-stability-ark-runtime-detection.md#section18515155816101)。

开启多线程检测会有较大性能损耗，请开发者按需开启。

### 开启方舟多线程检测

可通过以下方式开启方舟多线程检测。

* **方式一**

  点击**Run > Edit Configurations >** **Diagnostics**，勾选**Multi Thread Check**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/pBCjn0xpRpuQ5ADQxnXA0A/zh-cn_image_0000002561753747.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=CF973B1302CBBB30C015980E57E4323F3467E7CE165F47FB48680476DF380B92)

* **方式二**

  通过命令行开启。

  ```
  1. hdc shell aa start -a {abilityName} -b {bundleName} -R
  ```

* **方式三**

  通过调用[setMultithreadingDetectionEnabled接口](../harmonyos-references/js-apis-util.md#setmultithreadingdetectionenabled23)开启。

### 使用方舟多线程检测

1. 运行或调试当前应用。
2. 当程序出现多线程安全问题时，会弹出Crash log信息，点击信息中的链接即可跳转至引起多线程安全问题的代码处。关于多线程安全问题的分析方法请参考[使用Node-API接口产生的异常日志/崩溃分析](use-napi-about-crash.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/2a3JWjEbTiSQq2AHyyssqA/zh-cn_image_0000002561753751.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=80B55F2D2515D3799C3E6856638D6DA71F090141D6CD8FC7581B1BE51DD7EDAE)

## 方舟native模块加载异常信息增强

在进行ArkTS项目开发中可能存在需要加载native模块的场景，开启方舟native模块加载异常信息增强功能后，可以丰富ArkTS项目中因加载native模块导致的报错信息，以便更准确地进行native问题定位。

### 开启方舟native模块加载异常信息增强

可以通过以下两种方式开启方舟native模块加载异常信息增强。

* 方式一

  点击**Run > Edit Configurations >** **Diagnostics**，勾选**Enhanced Error Info**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/SNwh2AtgTFuKVI7W18xmzA/zh-cn_image_0000002530753806.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=B6FC1644E9E509F2CCC529BD22A074B7C3221069B664715E398E507CFC3594DE)

* 方式二

  通过命令行开启。

  ```
  1. hdc shell aa start {abilityName} {bundleName} -E
  ```

### 使用方舟native模块加载异常信息增强

1. 运行或调试当前应用。
2. 当程序出现因native模块加载导致的报错信息时，会显示更详细准确的错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/mZ1gFdXUQkKS_SWimmFY8Q/zh-cn_image_0000002530753810.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=E371DBD1A60883DB9EF586CCA17D8A9CA1219F7AA4B269381AB627A31969246E)
