---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-multi-thread-check
title: 方舟运行时检测
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 方舟运行时检测
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:56+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:538d2a30f2c87b54ea6785f7a17117eadc9243d2b0c94104ce9b0446942589ca
---

## 方舟多线程检测

在JS运行时环境中，多线程的安全问题是一个重要的考虑因素。由于JavaScript主线程是单线程的，在主线程中创建的JS对象（尤其是DOM相关对象）只能在主线程上进行操作。如果违反了这一规则，就会导致多线程安全问题。针对该场景，鸿蒙电脑DevEco Studio集成多线程检测能力，并通过FaultLog展示错误的堆栈详情及导致错误的代码行。关于多线程检测的原理请参考[原理介绍](../best-practices/bpta-stability-ark-runtime-detection.md#section18515155816101)。

开启多线程检测会有较大性能损耗，请开发者按需开启。

### 开启方舟多线程检测

可通过以下方式开启方舟多线程检测。

* **方式一**
  1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/Ub-Otc13TeCYteQery27Kw/zh-cn_image_0000002791840922.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8214476EBDBD70F1D035A24612253338EEBA2EF183B4E573F15E1D596C1F229)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/KiTBnSfQRdqS7Yi2iG9FzA/zh-cn_image_0000002820680847.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=F84812CF0E43D55A11BDB84EDB9AB23768674D7CF699DFF029AD850F0F1AFD12 "点击放大")按钮打开配置界面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/Ys9lrYTyRHKV4ShXK2spJQ/zh-cn_image_0000002820680855.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=A4A91D9B1C2CB585499DE08B39730B6DDDA333C986917EB39D8197C61C1327DF)
  2. 在配置界面点击**故障分析**，勾选**多线程检测**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/VO64CK69QaqyLbbQg5fPdA/zh-cn_image_0000002792000890.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=8FFA7B93A9211CEE29A10547A69333BFC037955774AA11AD271CD2EDDD805D02)

* **方式二**

  通过命令行开启。

  ```screen
  hdc shell aa start -a {abilityName} -b {bundleName} -R
  ```

### 使用方舟多线程检测

1. 运行或调试当前应用。
2. 当程序出现多线程安全问题时，会弹出Crash log信息，点击信息中的链接即可跳转至引起多线程安全问题的代码处。关于多线程安全问题的分析方法请参考[使用Node-API接口产生的异常日志/崩溃分析](use-napi-about-crash.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/dC6ItNtoRLW1AIn5nJUQWw/zh-cn_image_0000002820720857.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=FB603F40B827AC72C76DBBA7163E8B952A0D0748D891A6F13BCD692377FA2558)

## 方舟native模块加载异常信息增强

在进行ArkTS项目开发中可能存在需要加载native模块的场景，开启方舟native模块加载异常信息增强功能后，可以丰富ArkTS项目中因加载native模块导致的报错信息，以便更准确地进行native问题定位。

### 开启方舟native模块加载异常信息增强

可以通过以下两种方式开启方舟native模块加载异常信息增强。

* 方式一
  1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/5Fm-JebeTC6spRaD2ezkiw/zh-cn_image_0000002820720855.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=4158B0CB61AF8B7E3386CC86E603063496DD8041A4A979C3FE9908320B2AB16C)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/yCZq-L3HTQagiXu8pRQrUQ/zh-cn_image_0000002792000884.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=D39F2AD78E8612E420806D64EAB1C1B6C8DAF16AAB217F0909932862ABB53794 "点击放大")按钮打开配置界面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/nCX9ibHIQOiVv1ziNkWU-A/zh-cn_image_0000002792000888.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=E0058BF24558EFA7DF0C21DD5D47AA0AC2112A22E019E980E92EC07EE5D5B691)
  2. 在配置界面点击**故障分析**，勾选**增强错误信息**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/2kb7pnzoQZe6MclauMAK_g/zh-cn_image_0000002820720859.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=402A56F72B300351DAF03B259669230137C6621A7DEE7553166A1F4700B83016)

* 方式二

  通过命令行开启。

  ```screen
  hdc shell aa start {abilityName} {bundleName} -E
  ```

### 使用方舟native模块加载异常信息增强

1. 运行或调试当前应用。
2. 当程序出现因native模块加载导致的报错信息时，会显示更详细准确的错误信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/19hWjjLURaqoIK5wQE0yLQ/zh-cn_image_0000002792000894.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=66A7F8F901D33E12C5C3DCAB4C4812848100DF48C17FB696080CDA5F29335194)
