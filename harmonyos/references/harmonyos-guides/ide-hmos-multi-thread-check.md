---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-multi-thread-check
title: 方舟运行时检测
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 方舟运行时检测
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:b98886924d327cdc9883ef6c0091c63756e175d0920648f77a668cd2a8443dd4
---

## 方舟多线程检测

在JS运行时环境中，多线程的安全问题是一个重要的考虑因素。由于JavaScript主线程是单线程的，在主线程中创建的JS对象（尤其是DOM相关对象）只能在主线程上进行操作。如果违反了这一规则，就会导致多线程安全问题。针对该场景，鸿蒙电脑DevEco Studio集成多线程检测能力，并通过FaultLog展示错误的堆栈详情及导致错误的代码行。关于多线程检测的原理请参考[原理介绍](../best-practices/bpta-stability-ark-runtime-detection.md#section18515155816101)。

开启多线程检测会有较大性能损耗，请开发者按需开启。

### 开启方舟多线程检测

可通过以下方式开启方舟多线程检测。

* **方式一**
  1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/2M6fz__UQbCMk1Wg3YUA5A/zh-cn_image_0000002781471294.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C8D3536FAEA8EF030D1BD70FC81A4383FCB06B3CF0382DB6E5933DE4504F9430)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/SCw9SsWnQ8Gb8kl-w45EnQ/zh-cn_image_0000002781471296.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A3FF3D80D0427980CCD66499201EA5E18AB1F7C062C69FB979F43F0C3D52F5C3 "点击放大")按钮打开配置界面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/Hb7pOW9mRDa2qkv9esbMVw/zh-cn_image_0000002781311362.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=01053D353BA8218A856F57B4E634C6994FF6027BEFB55711F74804CEB87D80FA)
  2. 在配置界面点击**故障分析**，勾选**多线程检测**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/UemSUeisQoC-o-tir9Ochw/zh-cn_image_0000002810630845.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=869CF7BFD9CD7068E05285451FA15800F2E176BB9EBE4BDEFCE2E7B5985C7104)

* **方式二**

  通过命令行开启。

  ```screen
  hdc shell aa start -a {abilityName} -b {bundleName} -R
  ```

### 使用方舟多线程检测

1. 运行或调试当前应用。
2. 当程序出现多线程安全问题时，会弹出Crash log信息，点击信息中的链接即可跳转至引起多线程安全问题的代码处。关于多线程安全问题的分析方法请参考[使用Node-API接口产生的异常日志/崩溃分析](use-napi-about-crash.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/SCULMN4xRViqMKZgRaEYWQ/zh-cn_image_0000002810630847.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=7D67AF13CFD66A3BB8082534B8A99A9AA8D5C5329D94218470470174A785E609)

## 方舟native模块加载异常信息增强

在进行ArkTS项目开发中可能存在需要加载native模块的场景，开启方舟native模块加载异常信息增强功能后，可以丰富ArkTS项目中因加载native模块导致的报错信息，以便更准确地进行native问题定位。

### 开启方舟native模块加载异常信息增强

可以通过以下两种方式开启方舟native模块加载异常信息增强。

* 方式一
  1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/mMbedNaaS_Cj_M2jTfu7pw/zh-cn_image_0000002810630849.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA593E73223C771744478C30D7AE531F349B8A83363D9CF2B1A5AAA2C9A517C3)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/yVfEnAnkSoWgk1ZtvH44Kw/zh-cn_image_0000002810750953.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=B6C7B6E5E97C0D5FB63D3D8F74412BE2E9827986AE201D591739B406C0D829A3 "点击放大")按钮打开配置界面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/vjTfY_1hSZSiuMgUTxBOMQ/zh-cn_image_0000002810750957.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=31902D6165C47F19B940FD4B62413F839707CBFE1FB41B5B0C6541CBD586576E)
  2. 在配置界面点击**故障分析**，勾选**增强错误信息**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/wSSMVLr-Q7uPM7wSuXfOWQ/zh-cn_image_0000002810630843.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC9702E2F18FFF6BAFD9D20E7BE060F74225720550587598005114AC9A1DE203)

* 方式二

  通过命令行开启。

  ```screen
  hdc shell aa start {abilityName} {bundleName} -E
  ```

### 使用方舟native模块加载异常信息增强

1. 运行或调试当前应用。
2. 当程序出现因native模块加载导致的报错信息时，会显示更详细准确的错误信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/1RJhwDThTZG-peBroWH95g/zh-cn_image_0000002781311360.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=34E9148DAFA75EDA26531A0BFF4925351EF4DA816CA7A07A448B58AFC1BBEC9B)
