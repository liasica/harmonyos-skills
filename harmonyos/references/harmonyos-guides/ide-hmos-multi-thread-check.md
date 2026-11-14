---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-multi-thread-check
title: 方舟运行时检测
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 方舟运行时检测
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:17+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:607b9c0fb58e827c983bad469cf8d6dc74b6c3c498853b13454322075b2cd488
---

## 方舟多线程检测

在JS运行时环境中，多线程的安全问题是一个重要的考虑因素。由于JavaScript主线程是单线程的，在主线程中创建的JS对象（尤其是DOM相关对象）只能在主线程上进行操作。如果违反了这一规则，就会导致多线程安全问题。针对该场景，鸿蒙电脑DevEco Studio集成多线程检测能力，并通过FaultLog展示错误的堆栈详情及导致错误的代码行。关于多线程检测的原理请参考[原理介绍](../best-practices/bpta-stability-ark-runtime-detection.md#section18515155816101)。

开启多线程检测会有较大性能损耗，请开发者按需开启。

### 开启方舟多线程检测

可通过以下方式开启方舟多线程检测。

* **方式一**
  1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/N9jWCjBMQTiDWZ2X6tYc_Q/zh-cn_image_0000002781471294.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C032A89BAA540313FC3CF279DDB414B5663FA26755D14B540696BD72822FF1D)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/uvqIYdVPRieyLcnd7ERnRg/zh-cn_image_0000002781471296.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=C8A3C2E6FCFEBAA3052FDE2CB16B15396CA7E00CD5B48AF98E0CD623FC6556A6 "点击放大")按钮打开配置界面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/yvd2ziOmTe6q1P6GEAQhgg/zh-cn_image_0000002781311362.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=26D49276563051741729714929C9387C8DEC3E23DC1026075D387DEB79B68161)
  2. 在配置界面点击**故障分析**，勾选**多线程检测**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/9nqwJMZfTdGFvvX5JB3_qw/zh-cn_image_0000002810630845.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2494AC755A1E7958D01E2685CB89AD483AFB95457E3010A3FB6A5668F0297A3)

* **方式二**

  通过命令行开启。

  ```screen
  hdc shell aa start -a {abilityName} -b {bundleName} -R
  ```

### 使用方舟多线程检测

1. 运行或调试当前应用。
2. 当程序出现多线程安全问题时，会弹出Crash log信息，点击信息中的链接即可跳转至引起多线程安全问题的代码处。关于多线程安全问题的分析方法请参考[使用Node-API接口产生的异常日志/崩溃分析](use-napi-about-crash.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/7hCK6njeQEig4BK1tiCXLA/zh-cn_image_0000002810630847.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=12C621ED64AC4AA06FF2156E69AA8AC736AE007C820C4B7898382B3D0B6CA01F)

## 方舟native模块加载异常信息增强

在进行ArkTS项目开发中可能存在需要加载native模块的场景，开启方舟native模块加载异常信息增强功能后，可以丰富ArkTS项目中因加载native模块导致的报错信息，以便更准确地进行native问题定位。

### 开启方舟native模块加载异常信息增强

可以通过以下两种方式开启方舟native模块加载异常信息增强。

* 方式一
  1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/fjlxYcX9RVWr7qiwtezsWA/zh-cn_image_0000002810630849.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=C1823D91C73944D677DA6B0B101626D58C5007313DD128F6203EF0F3B6EC8642)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/xJ7DrEd8S96ArwL9VfYWQw/zh-cn_image_0000002810750953.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=3BF284A6BE8A4014910B27196C178712A359EE4D7A60FE508D836F04FD86788F "点击放大")按钮打开配置界面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/I7rIOQQVS9KrfdEXBuur2A/zh-cn_image_0000002810750957.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=632F7813BC596BBA589120741B9A4677CDF6A93062E60B85B0EE1AE0DDE15191)
  2. 在配置界面点击**故障分析**，勾选**增强错误信息**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/aQIR49CFSGaqOoyfaWjG8A/zh-cn_image_0000002810630843.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=CF4616BA41EAE2ECF662F80D19B3E5DC591074EEADB4C19310CED807E5499D85)

* 方式二

  通过命令行开启。

  ```screen
  hdc shell aa start {abilityName} {bundleName} -E
  ```

### 使用方舟native模块加载异常信息增强

1. 运行或调试当前应用。
2. 当程序出现因native模块加载导致的报错信息时，会显示更详细准确的错误信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/MgFxiZEdQrW33GIg5i3evw/zh-cn_image_0000002781311360.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BCBF4A1C4A1ABD3C980A59622690742996B4185AF21925BF00589870661D661)
