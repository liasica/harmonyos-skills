---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-simulator
title: 使用仿真器运行轻量级智能穿戴应用
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 使用仿真器运行轻量级智能穿戴应用
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:c6501faed09ba6cc19e625beafb0bef1d0934596527c2688908d0d31ed7af953
---

DevEco Studio提供的**Simulator**可以运行和调试Lite Wearable设备上的HarmonyOS应用，兼容签名与不签名两种类型的HAP。

## 操作步骤

1. 在DevEco Studio右上角的设备框中选择**Huawei Lite Wearable Simulator。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/j9THIApjRaeXYUWqcpSHvg/zh-cn_image_0000002779406648.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=B472582F93FA9C4914E0C8945007E77D0627586B7815EABD320B0B7A5C501B5A)
2. 点击**Run** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/BkSrd2eRQLSDFMMI21-m5w/zh-cn_image_0000002779566642.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=3459D13CBB5C58334B6231619CF8E7AFE0DA1D28D5B15D6AF7FABDCE09496B97)或**Debug** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/u1sTPID3Sn-ukhLEjgJcTQ/zh-cn_image_0000002779406660.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=126759A9296B7CA0C8827E3B96F97229DA43FD9AD1771855E268908CAF0D4091)按钮，在弹框中选择设备形状和分辨率，点击**OK**按钮，开始运行或调试应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/yq-TIGLzRGeU2uoCPbsmgg/zh-cn_image_0000002779406654.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=9998CC96D3C6679BC7F07A87DF4DC80CF4F75F18ADAE563436C58E0071368D31 "点击放大")
3. DevEco Studio会启动编译构建和安装，完成后应用即可运行在Simulator上。

## 功能介绍

在Simulator界面中，点击设备上方的**More**可展开更多功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/hY5dGsxgSGG7ta6_231NxA/zh-cn_image_0000002779406662.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=FDBBD7AE7386234550A68D1CDCDD05FC3BEF4759887B71E34FB96CF21F15CB2D)

### 屏幕

* **Turn screen on：**控制屏幕开关。
* **Keep screen on：**控制屏幕是否保持常亮状态。关闭开关时，息屏计时结束后，屏幕自动关闭，同时**Turn screen on**开关自动关闭。开启屏幕后，打开**Keep screen on**开关才能使屏幕常亮。
* **Brightness adjustment mode：**调节屏幕亮度。
  + **Manual：**手动调节，可拖动滑动条，或直接输入亮度。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/MmyVMh3vQ0mpuhP90K7aFQ/zh-cn_image_0000002808886289.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=FCA9D6AD15E32E1C5AF34250D81C0B48C29EE75AA933FA29AC4BA5D97C2D707B)
  + **Automatic：**自动调节。
* **Resolution：**运行/调试模式下暂不支持调整分辨率，如需调整，请停止运行后，按照[操作步骤](ide-run-simulator.md#section1332819367496)选择分辨率。

### 传感器

仿真器提供了虚拟传感器来模拟硬件传感器的能力。在该界面，您可以调节不同的传感器来测试您的应用，使用[@system.sensor](../harmonyos-references/js-apis-system-sensor.md)模块监听传感器值的变化，使用[@system.geolocation](../harmonyos-references/js-apis-system-location.md)模块监听地理位置的变化。仿真器提供以下虚拟传感器：

* **On-body status**：传感器所在设备穿戴状态，包括已穿戴和未穿戴。
* **Barometer：**气压传感器用于测量环境气压，单位为Pa。
* **Heart rate：**心率传感器用于测量心率数值，拖动滑动条，或直接输入心率大小。
* **Step count：**计步传感器用于统计行走步数，拖动滑动条，或直接输入步数。
* **Geographic location：**输入经度、纬度，模拟设备所处的地理位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/KXflwLSVTCeDFl6Bf45iwQ/zh-cn_image_0000002779566632.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=24CFB1B7783B2BC15E3A7665E65303216170C69DAA8DFA96CCABD8EBE65CEC0D)

### 电池

您可以通过仿真器模拟不同的电池状态，包括以下三种充电状态，也可以手动输入或拖动滑动条来改变电量大小。在应用中，您可以通过[@system.battery](../harmonyos-references/js-apis-system-battery.md)模块查询仿真器的剩余电量以及充电状态。

* Not charging：未充电。
* Charging：正在充电。
* Wireless charging：无线充电。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/A7f8idQuRPqxxsY37vW6sg/zh-cn_image_0000002808766211.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B84DD7306C0A859F07B24A54CB0334B75E67EB8B948782385BA6B71E9F58126)

### 设备设置

您可以更改设备的语言和地区，当前仅运行模式可以更改，调试模式暂不支持。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/LSerflEgQTawHjS2jVWjJg/zh-cn_image_0000002779406656.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=D790A6F47C6A61E4C8327D76F36CC71A87893D78C70DA5771BC8AA3C3CD905B4)

### 调试

* **Screen coordinate system****：**开启屏幕坐标系后，将光标移动到表盘上时，会显示屏幕坐标。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/FlwuSh7ER1ms8Ewj6bugVw/zh-cn_image_0000002779566636.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=14AF4F132918E9F6B32B47E862D6907F20E9685396ED1A8049BDACBAF14C9167 "点击放大")
* **Show device mask****：**关闭开关后，表盘周围的表冠颜色淡化。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/mv23dFdMSROkoJGd7Qt33w/zh-cn_image_0000002779566628.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=086D5D7E3C5C477F70690CFDBF2808A5EAF5B264EBFD92B2646931A5A77CF5D0 "点击放大")
