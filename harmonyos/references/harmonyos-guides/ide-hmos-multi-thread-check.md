---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-multi-thread-check
title: 方舟运行时检测
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 方舟运行时检测
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:46+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:bef94fead066daa141f7596973109836fe8291e32c57112cdb9dc345495bd81c
---

## 方舟多线程检测

在JS运行时环境中，多线程的安全问题是一个重要的考虑因素。由于JavaScript主线程是单线程的，在主线程中创建的JS对象（尤其是DOM相关对象）只能在主线程上进行操作。如果违反了这一规则，就会导致多线程安全问题。针对该场景，鸿蒙电脑DevEco Studio集成多线程检测能力，并通过FaultLog展示错误的堆栈详情及导致错误的代码行。关于多线程检测的原理请参考[原理介绍](../best-practices/bpta-stability-ark-runtime-detection.md#section18515155816101)。

开启多线程检测会有较大性能损耗，请开发者按需开启。

### 开启方舟多线程检测

可通过以下方式开启方舟多线程检测。

* **方式一**
  1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/4B6n3XfmREKhW8L-CvkCVg/zh-cn_image_0000002791840922.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=288E60CBC2838BA8A044AABECF3195DB9E1EAC03E95BD18A9E041CA53B668CAE)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/rGYEiuysSYyzzdegSrXjbw/zh-cn_image_0000002820680847.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=99D9D8323AB24029BACEFDEC9DBA5AD1BECDC614F6FC5C9E6803E1A7BCFAE04E "点击放大")按钮打开配置界面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/RniIbG86TS2sexu3Hq7trw/zh-cn_image_0000002820680855.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=879E81442432BDBBA1F4DF7DEECE12344C85F9CD2D595377314AD2A495D3F028)
  2. 在配置界面点击**故障分析**，勾选**多线程检测**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/5qS4t2pZRO6af47zsyOjsg/zh-cn_image_0000002792000890.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA4FA697F29815DC54C3CB68096E1792C2655EE28779ED358927893DFF50DBD6)

* **方式二**

  通过命令行开启。

  ```screen
  hdc shell aa start -a {abilityName} -b {bundleName} -R
  ```

### 使用方舟多线程检测

1. 运行或调试当前应用。
2. 当程序出现多线程安全问题时，会弹出Crash log信息，点击信息中的链接即可跳转至引起多线程安全问题的代码处。关于多线程安全问题的分析方法请参考[使用Node-API接口产生的异常日志/崩溃分析](use-napi-about-crash.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/w3IPfxFKRFuVcLxPLHsfew/zh-cn_image_0000002820720857.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B7C8536FC4CBFD023EF1FF48E913E812A2CAC16B36F8058C92C51AF3923919F)

## 方舟native模块加载异常信息增强

在进行ArkTS项目开发中可能存在需要加载native模块的场景，开启方舟native模块加载异常信息增强功能后，可以丰富ArkTS项目中因加载native模块导致的报错信息，以便更准确地进行native问题定位。

### 开启方舟native模块加载异常信息增强

可以通过以下两种方式开启方舟native模块加载异常信息增强。

* 方式一
  1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/gX9MFoTbQ0O_Co6baJE3-g/zh-cn_image_0000002820720855.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=8B1A7B858AB8658F30915C5653D87B4C4647B18768FC5006911DBD9E05698FC4)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/zqpBCyI1TXqiifs-b-KHUA/zh-cn_image_0000002792000884.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=63439FF799F18A05327A1D45302D6B2F4D0ABFCCE1594A249454855905E376A7 "点击放大")按钮打开配置界面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/r0gO-1EHRiWLfcW3nSvLpg/zh-cn_image_0000002792000888.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=444287E288DE1A0FCF743B70010E33C6E8516AA3D4097A5FA48BCB372316AC4C)
  2. 在配置界面点击**故障分析**，勾选**增强错误信息**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/LGSxTk1fS-uslM3zDS-oBA/zh-cn_image_0000002820720859.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=0405488844DC0AFFB21BA506E069EF7FAFA2D9746A966C32D6EA980856081136)

* 方式二

  通过命令行开启。

  ```screen
  hdc shell aa start {abilityName} {bundleName} -E
  ```

### 使用方舟native模块加载异常信息增强

1. 运行或调试当前应用。
2. 当程序出现因native模块加载导致的报错信息时，会显示更详细准确的错误信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/siTRz7u8TeeEDzzWSrSspQ/zh-cn_image_0000002792000894.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C4DB1154CCC8E84B60C629DE5FBC35CBA16685001B659CD53F1551953ACD75A)
