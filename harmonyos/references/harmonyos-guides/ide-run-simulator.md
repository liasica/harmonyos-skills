---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-simulator
title: 使用仿真器运行轻量级穿戴应用
breadcrumb: 指南 > 编写与调试应用 > 使用仿真器运行轻量级穿戴应用
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:39+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:90cf2e97de475e13c2ceb0b349d9be51ce881601952028fc2b3b073f7bf1bd41
---

DevEco Studio提供的**Simulator**可以运行和调试Lite Wearable设备上的HarmonyOS应用，兼容签名与不签名两种类型的HAP。

## 操作步骤

1. 在DevEco Studio右上角的设备框中选择**Huawei Lite Wearable Simulator。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/2VvfUVljR7-cbazxzFQJyQ/zh-cn_image_0000002561752733.png?HW-CC-KV=V1&HW-CC-Date=20260427T235638Z&HW-CC-Expire=86400&HW-CC-Sign=A9149E0C5E0BFE51D1B86EF1CB1D70AF74C4503D0F1B93A84384B852673F69FE)
2. 点击**Run** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/y6jydcdKRniILEjnLq4eVw/zh-cn_image_0000002530752814.png?HW-CC-KV=V1&HW-CC-Date=20260427T235638Z&HW-CC-Expire=86400&HW-CC-Sign=C4F812D260140BCE6FCDECBD1E0FECDC960DC373E937C7EF0EDDD524C4015EF3)或**Debug** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/ahoOV2H_RNmBJBZ4slZpwg/zh-cn_image_0000002530752808.png?HW-CC-KV=V1&HW-CC-Date=20260427T235638Z&HW-CC-Expire=86400&HW-CC-Sign=5639D73455CCA73240BA5D273EB78DD5DBC814E6BEB1C8D8A2691ED3AD1B3161)按钮，在弹框中选择设备形状和分辨率，点击**OK**按钮，开始运行或调试应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/PrZxyhFnT2mNoCSee-6MTA/zh-cn_image_0000002561752739.png?HW-CC-KV=V1&HW-CC-Date=20260427T235638Z&HW-CC-Expire=86400&HW-CC-Sign=67312EFA40BF72B9E6E67A27C99E550AE88B659B8282BBAF972C402706B2AD8F "点击放大")
3. DevEco Studio会启动编译构建和安装，完成后应用即可运行在Simulator上。

## 功能介绍

在Simulator界面中，点击设备上方的**More**可展开更多功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/A7Gkg09ASmaqok7Ft60XKg/zh-cn_image_0000002530752812.png?HW-CC-KV=V1&HW-CC-Date=20260427T235638Z&HW-CC-Expire=86400&HW-CC-Sign=CD9366C3652BF806B8956F7BE5C30F16602DDFB685B528555C0FEAEBC108F1E8)

### 屏幕

* **Turn screen on：**控制屏幕开关。
* **Keep screen on：**控制屏幕是否保持常亮状态。关闭开关时，息屏计时结束后，屏幕自动关闭，同时**Turn screen on**开关自动关闭。开启屏幕后，打开**Keep screen on**开关才能使屏幕常亮。
* **Brightness adjustment mode：**调节屏幕亮度。
  + **Manual：**手动调节，可拖动滑动条，或直接输入亮度。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/uvLNE6jkQe6gwzMlJXh4PA/zh-cn_image_0000002530752794.png?HW-CC-KV=V1&HW-CC-Date=20260427T235638Z&HW-CC-Expire=86400&HW-CC-Sign=C3B24331122A91600DCF3E44C4DDFA2D4A816DFB29487742B58130F265D8F87D)
  + **Automatic：**自动调节。
* **Resolution：**运行/调试模式下暂不支持调整分辨率，如需调整，请停止运行后，按照[操作步骤](ide-run-simulator.md#section1332819367496)选择分辨率。

### 传感器

仿真器提供了虚拟传感器来模拟硬件传感器的能力。在该界面，您可以调节不同的传感器来测试您的应用，使用[@system.sensor](../harmonyos-references/js-apis-system-sensor.md)模块监听传感器值的变化，使用[@system.geolocation](../harmonyos-references/js-apis-system-location.md)模块监听地理位置的变化。仿真器提供以下虚拟传感器：

* **On-body status**：传感器所在设备穿戴状态，包括已穿戴和未穿戴。
* **Barometer：**气压传感器用于测量环境气压，单位为Pa。
* **Heart rate：**心率传感器用于测量心率数值，拖动滑动条，或直接输入心率大小。
* **Step count：**计步传感器用于统计行走步数，拖动滑动条，或直接输入步数。
* **Geographic location：**输入经度、纬度，模拟设备所处的地理位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/zeJ8XDv8TAOU9M8f_fJBrQ/zh-cn_image_0000002530912796.png?HW-CC-KV=V1&HW-CC-Date=20260427T235638Z&HW-CC-Expire=86400&HW-CC-Sign=0877BEC5B171C2AC24C1DDAB847313C18E701EC6A3385E478EC42CC61312E6E1)

### 电池

您可以通过仿真器模拟不同的电池状态，包括以下三种充电状态，也可以手动输入或拖动滑动条来改变电量大小。在应用中，您可以通过[@system.battery](../harmonyos-references/js-apis-system-battery.md)模块查询仿真器的剩余电量以及充电状态。

* Not charging：未充电。
* Charging：正在充电。
* Wireless charging：无线充电。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/YorunbqWSeKzHajBAk4Baw/zh-cn_image_0000002530752798.png?HW-CC-KV=V1&HW-CC-Date=20260427T235638Z&HW-CC-Expire=86400&HW-CC-Sign=FD03432B42C6058A2F917198A0313CDD4B8FF3A957228A14A943565FB8000E72)

### 设备设置

您可以更改设备的语言和地区，当前仅运行模式可以更改，调试模式暂不支持。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/ht93TlWJRXGsVgFQRf1EpA/zh-cn_image_0000002530912800.png?HW-CC-KV=V1&HW-CC-Date=20260427T235638Z&HW-CC-Expire=86400&HW-CC-Sign=68C7A42F1EAD2C8DCB24F1309AF5D52C483FB31C32036D7565AA84254B832D1F)

### 调试

* **Screen coordinate system****：**开启屏幕坐标系后，将光标移动到表盘上时，会显示屏幕坐标。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/ERFg3YgxQ3SsYPVf8nPdgQ/zh-cn_image_0000002530752806.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235638Z&HW-CC-Expire=86400&HW-CC-Sign=8FC427A3667BCD89D383D82ED499FE8396E9E9577A2B22428ABD81F9C54A195C "点击放大")
* **Show device mask****：**关闭开关后，表盘周围的表冠颜色淡化。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/pVM5hVxvSe2agN4rp_eB9A/zh-cn_image_0000002561752735.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235638Z&HW-CC-Expire=86400&HW-CC-Sign=F910702F29255F8223ED44F6F14A2C80991A41B7B35084BBB53B4C56BCB8769F "点击放大")
