---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-multi-thread-check
title: 方舟运行时检测
breadcrumb: 指南 > 编写与调试应用 > 日志与故障分析 > 故障分析 > 方舟运行时检测
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0798bcb5a4889b39a9fcd74bdf47be7e286da46dfcf9b3a6e0b0922c77b4e249
---

## 方舟多线程检测

在JS运行时环境中，多线程的安全问题是一个重要的考虑因素。由于JavaScript主线程是单线程的，在主线程中创建的JS对象（尤其是DOM相关对象）只能在主线程上进行操作。如果违反了这一规则，就会导致多线程安全问题。针对该场景，DevEco Studio集成多线程检测能力，并通过FaultLog展示错误的堆栈详情及导致错误的代码行。关于多线程检测的原理请参考[原理介绍](../best-practices/bpta-stability-ark-runtime-detection.md#section18515155816101)。

开启多线程检测会有较大性能损耗，请开发者按需开启。

### 开启方舟多线程检测

可通过以下方式开启方舟多线程检测。

* **方式一**

  点击**Run > Edit Configurations >** **Diagnostics**，勾选**Multi Thread Check**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/mrLAxFp6T5-txLtq33xpgA/zh-cn_image_0000002561753747.png?HW-CC-KV=V1&HW-CC-Date=20260429T054655Z&HW-CC-Expire=86400&HW-CC-Sign=AED219C4142231D2D373993210BEEE8A7A1FD5E1240EFB053AF083D89E0B9184)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/IXzALhjFR-KAe8UN6bBqMg/zh-cn_image_0000002561753751.png?HW-CC-KV=V1&HW-CC-Date=20260429T054655Z&HW-CC-Expire=86400&HW-CC-Sign=EA4AC36AE7FECB2E8369C974E7660317B4189CF05F46AB2690E2466EF7159BE1)

## 方舟native模块加载异常信息增强

在进行ArkTS项目开发中可能存在需要加载native模块的场景，开启方舟native模块加载异常信息增强功能后，可以丰富ArkTS项目中因加载native模块导致的报错信息，以便更准确地进行native问题定位。

### 开启方舟native模块加载异常信息增强

可以通过以下两种方式开启方舟native模块加载异常信息增强。

* 方式一

  点击**Run > Edit Configurations >** **Diagnostics**，勾选**Enhanced Error Info**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/I9GgY_zpRAO-Y7nN5Rr0Xw/zh-cn_image_0000002530753806.png?HW-CC-KV=V1&HW-CC-Date=20260429T054655Z&HW-CC-Expire=86400&HW-CC-Sign=5F32605D65C678C5C165ED231092E4F447BF1ED24ECB6D45E667A37C291525AB)

* 方式二

  通过命令行开启。

  ```
  1. hdc shell aa start {abilityName} {bundleName} -E
  ```

### 使用方舟native模块加载异常信息增强

1. 运行或调试当前应用。
2. 当程序出现因native模块加载导致的报错信息时，会显示更详细准确的错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/9wq1XQ1DR2uudt8SK4DzVg/zh-cn_image_0000002530753810.png?HW-CC-KV=V1&HW-CC-Date=20260429T054655Z&HW-CC-Expire=86400&HW-CC-Sign=A3BEBB5D3A33CC969AE29C68B77EAA7A183F951C2DC95FE6AE2B55239E09F036)
