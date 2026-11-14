---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-simulator
title: 使用仿真器运行轻量级智能穿戴应用
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 使用仿真器运行轻量级智能穿戴应用
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:b22568d6f5be4b27e37e11671b45c556d3c3b5d4e64da4e6b4b87421a5cdb14c
---

DevEco Studio提供的**Simulator**可以运行和调试Lite Wearable设备上的HarmonyOS应用，兼容签名与不签名两种类型的HAP。

## 操作步骤

1. 在DevEco Studio右上角的设备框中选择**Huawei Lite Wearable Simulator。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/vgebrISfTOCyYY9oair8aw/zh-cn_image_0000002779406648.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=4215F1A9BDE19E93A2A50BEE52BA2746B536B91296B3BE5EB214EE36F4860C32)
2. 点击**Run** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/MCBKJW4gQ3y-eN0eZ6XonA/zh-cn_image_0000002779566642.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=F4529E6DD8D3D7B58D4D41F85408C74B73973D18AED3A6FEEB5D9EBF26A80829)或**Debug** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/RAsAqb-wQfyRY9S9pCEuZg/zh-cn_image_0000002779406660.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=D8B10B7065CC5A74058747FD0FC3B96BF348EC8BFBF81AED88BE0AD6E56CA667)按钮，在弹框中选择设备形状和分辨率，点击**OK**按钮，开始运行或调试应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/QUzDzpQlSVGDv_EPT9w6wA/zh-cn_image_0000002779406654.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=5D2AB3B1DE5F47A52A82FC875C25324D1F0317C768F71DF42903EF01807245CA "点击放大")
3. DevEco Studio会启动编译构建和安装，完成后应用即可运行在Simulator上。

## 功能介绍

在Simulator界面中，点击设备上方的**More**可展开更多功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/8ILnEbUqSt-7r47f6Z62oA/zh-cn_image_0000002779406662.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=F3AD1E4CB737DD633BD809242EAF61AB9EA93E7F4C1AB35394AC473503A76213)

### 屏幕

* **Turn screen on：**控制屏幕开关。
* **Keep screen on：**控制屏幕是否保持常亮状态。关闭开关时，息屏计时结束后，屏幕自动关闭，同时**Turn screen on**开关自动关闭。开启屏幕后，打开**Keep screen on**开关才能使屏幕常亮。
* **Brightness adjustment mode：**调节屏幕亮度。
  + **Manual：**手动调节，可拖动滑动条，或直接输入亮度。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/G54rHSFhRbuOCLOIESV5Dg/zh-cn_image_0000002808886289.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=74091E905B6ED21C17FB08E0A914177BE44157BD5923DAB492113AB1BD3C4832)
  + **Automatic：**自动调节。
* **Resolution：**运行/调试模式下暂不支持调整分辨率，如需调整，请停止运行后，按照[操作步骤](ide-run-simulator.md#section1332819367496)选择分辨率。

### 传感器

仿真器提供了虚拟传感器来模拟硬件传感器的能力。在该界面，您可以调节不同的传感器来测试您的应用，使用[@system.sensor](../harmonyos-references/js-apis-system-sensor.md)模块监听传感器值的变化，使用[@system.geolocation](../harmonyos-references/js-apis-system-location.md)模块监听地理位置的变化。仿真器提供以下虚拟传感器：

* **On-body status**：传感器所在设备穿戴状态，包括已穿戴和未穿戴。
* **Barometer：**气压传感器用于测量环境气压，单位为Pa。
* **Heart rate：**心率传感器用于测量心率数值，拖动滑动条，或直接输入心率大小。
* **Step count：**计步传感器用于统计行走步数，拖动滑动条，或直接输入步数。
* **Geographic location：**输入经度、纬度，模拟设备所处的地理位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/ZHkQLbzCTOqJcAIhqGaVSw/zh-cn_image_0000002779566632.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=9CEFEAD82B93E0A84486DB3181ED640ADB8079DF02839EE887EB17CCBCCD5EF3)

### 电池

您可以通过仿真器模拟不同的电池状态，包括以下三种充电状态，也可以手动输入或拖动滑动条来改变电量大小。在应用中，您可以通过[@system.battery](../harmonyos-references/js-apis-system-battery.md)模块查询仿真器的剩余电量以及充电状态。

* Not charging：未充电。
* Charging：正在充电。
* Wireless charging：无线充电。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/kdMLRq62Q06J11E7mK7JEg/zh-cn_image_0000002808766211.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=D9A02551CB530B24D0F0C3CF5BC3D04F712E8D0C0CD144B480277B3A3350ADAE)

### 设备设置

您可以更改设备的语言和地区，当前仅运行模式可以更改，调试模式暂不支持。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/8Ir_7GprRmuMcVkGKvlY5Q/zh-cn_image_0000002779406656.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6660C467B18EDA462EF30B5A0F12D34248760A8E95643ACED1BB6113D694120)

### 调试

* **Screen coordinate system****：**开启屏幕坐标系后，将光标移动到表盘上时，会显示屏幕坐标。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/KfiPWmkNQO63m4I1gjyT8Q/zh-cn_image_0000002779566636.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=ADB8769FD610655D997557641D728AAA4964F53160087639FBDA7D906F25BA1C "点击放大")
* **Show device mask****：**关闭开关后，表盘周围的表冠颜色淡化。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/KmIl1JK8SaGn5Ta3qHkokw/zh-cn_image_0000002779566628.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=A738080EE1B68606DF3D01103CFF00D8758A8D69AFCB3DA3CEF642138D61807B "点击放大")
