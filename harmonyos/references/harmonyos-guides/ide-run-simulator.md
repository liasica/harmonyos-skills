---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-simulator
title: 使用仿真器运行轻量级智能穿戴应用
breadcrumb: 指南 > 编写与调试应用 > 使用仿真器运行轻量级智能穿戴应用
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:38134026e78a5bb4099a2c18b363c94e0b1b770207b13d044135f51c333e781c
---

DevEco Studio提供的**Simulator**可以运行和调试Lite Wearable设备上的HarmonyOS应用，兼容签名与不签名两种类型的HAP。

## 操作步骤

1. 在DevEco Studio右上角的设备框中选择**Huawei Lite Wearable Simulator。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/ziVANliZQ2C7FvP3ZivcHQ/zh-cn_image_0000002701662834.png)
2. 点击**Run** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/6g4_h7CzTCqpxKjnrqKeNg/zh-cn_image_0000002731542047.png)或**Debug** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/pUMLTZ6NR92rf9rOn3q8rQ/zh-cn_image_0000002731382063.png)按钮，在弹框中选择设备形状和分辨率，点击**OK**按钮，开始运行或调试应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/Vlx2uR5OSsKyM9XX7LxfzA/zh-cn_image_0000002701822756.png "点击放大")
3. DevEco Studio会启动编译构建和安装，完成后应用即可运行在Simulator上。

## 功能介绍

在Simulator界面中，点击设备上方的**More**可展开更多功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/0zm8FUD1S2y50kRtotLG7g/zh-cn_image_0000002731542033.png)

### 屏幕

* **Turn screen on：**控制屏幕开关。
* **Keep screen on：**控制屏幕是否保持常亮状态。关闭开关时，息屏计时结束后，屏幕自动关闭，同时**Turn screen on**开关自动关闭。开启屏幕后，打开**Keep screen on**开关才能使屏幕常亮。
* **Brightness adjustment mode：**调节屏幕亮度。
  + **Manual：**手动调节，可拖动滑动条，或直接输入亮度。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/VMRhPJmvTSONR-e3deZ5nA/zh-cn_image_0000002701662848.png)
  + **Automatic：**自动调节。
* **Resolution：**运行/调试模式下暂不支持调整分辨率，如需调整，请停止运行后，按照[操作步骤](ide-run-simulator.md#section1332819367496)选择分辨率。

### 传感器

仿真器提供了虚拟传感器来模拟硬件传感器的能力。在该界面，您可以调节不同的传感器来测试您的应用，使用[@system.sensor](../harmonyos-references/js-apis-system-sensor.md)模块监听传感器值的变化，使用[@system.geolocation](../harmonyos-references/js-apis-system-location.md)模块监听地理位置的变化。仿真器提供以下虚拟传感器：

* **On-body status**：传感器所在设备穿戴状态，包括已穿戴和未穿戴。
* **Barometer：**气压传感器用于测量环境气压，单位为Pa。
* **Heart rate：**心率传感器用于测量心率数值，拖动滑动条，或直接输入心率大小。
* **Step count：**计步传感器用于统计行走步数，拖动滑动条，或直接输入步数。
* **Geographic location：**输入经度、纬度，模拟设备所处的地理位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/4enKm2hMS_W7IvrPsuCSFw/zh-cn_image_0000002701822766.png)

### 电池

您可以通过仿真器模拟不同的电池状态，包括以下三种充电状态，也可以手动输入或拖动滑动条来改变电量大小。在应用中，您可以通过[@system.battery](../harmonyos-references/js-apis-system-battery.md)模块查询仿真器的剩余电量以及充电状态。

* Not charging：未充电。
* Charging：正在充电。
* Wireless charging：无线充电。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/_PNtba-vQ36UxKmVn16FtQ/zh-cn_image_0000002701662838.png)

### 设备设置

您可以更改设备的语言和地区，当前仅运行模式可以更改，调试模式暂不支持。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/Gs5OkdBJRUmiOvNdYSO4dg/zh-cn_image_0000002701822760.png)

### 调试

* **Screen coordinate system****：**开启屏幕坐标系后，将光标移动到表盘上时，会显示屏幕坐标。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/vynhDSIsSSCkCo9rCAIJKg/zh-cn_image_0000002731382069.gif "点击放大")
* **Show device mask****：**关闭开关后，表盘周围的表冠颜色淡化。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/wJvNWfN9ShGKaMz0bASG3w/zh-cn_image_0000002731542037.gif "点击放大")
