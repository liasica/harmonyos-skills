---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-simulator
title: 使用仿真器运行轻量级穿戴应用
breadcrumb: 指南 > 编写与调试应用 > 使用仿真器运行轻量级穿戴应用
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:34+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:499594649ceac7cb34bcf2298d88d3ccf4059427de494d90a5cad48c32da2d30
---

DevEco Studio提供的**Simulator**可以运行和调试Lite Wearable设备上的HarmonyOS应用，兼容签名与不签名两种类型的HAP。

## 操作步骤

1. 在DevEco Studio右上角的设备框中选择**Huawei Lite Wearable Simulator。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/sG5Rw-isQcGeaDcojUYrAw/zh-cn_image_0000002561752733.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=1E10025B37F00CF7A6BD259705FDDA3821BB71DF393D4F3408FFBB7B8154D498)
2. 点击**Run** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/VMSKUf8tRBK-Ifc9VBI4vw/zh-cn_image_0000002530752814.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=A68955C1E8FE6302BE7C729F7C95694B9A327EB322223761A953EFE3DA416D03)或**Debug** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/47UziQbdSsqYoum-JVZ_MA/zh-cn_image_0000002530752808.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=E39C22F2A854795898F7579BD529BEBBF4AA2016E15752A5A0BDA2D00E232606)按钮，在弹框中选择设备形状和分辨率，点击**OK**按钮，开始运行或调试应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/3-asny3_Q8OG3Grt04Pn1Q/zh-cn_image_0000002561752739.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=3DF0A2F19FEB7881AEB2FF5804C1F03B085BCA15C01193CAB1B2D4518806A590 "点击放大")
3. DevEco Studio会启动编译构建和安装，完成后应用即可运行在Simulator上。

## 功能介绍

在Simulator界面中，点击设备上方的**More**可展开更多功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/taB-x0wqS8WPoJTtaBdKVA/zh-cn_image_0000002530752812.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=DEEA8ADB81F58548981980CDF9B81F835C41BD5337358A2EA64BC751EE529C06)

### 屏幕

* **Turn screen on：**控制屏幕开关。
* **Keep screen on：**控制屏幕是否保持常亮状态。关闭开关时，息屏计时结束后，屏幕自动关闭，同时**Turn screen on**开关自动关闭。开启屏幕后，打开**Keep screen on**开关才能使屏幕常亮。
* **Brightness adjustment mode：**调节屏幕亮度。
  + **Manual：**手动调节，可拖动滑动条，或直接输入亮度。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/zPyCTnddQ3eK_BuiIxPWSQ/zh-cn_image_0000002530752794.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=85BF75E2EA78F794837A522B384D2290A85891901D95FB75ACAB9E0CB4D8CA15)
  + **Automatic：**自动调节。
* **Resolution：**运行/调试模式下暂不支持调整分辨率，如需调整，请停止运行后，按照[操作步骤](ide-run-simulator.md#section1332819367496)选择分辨率。

### 传感器

仿真器提供了虚拟传感器来模拟硬件传感器的能力。在该界面，您可以调节不同的传感器来测试您的应用，使用[@system.sensor](../harmonyos-references/js-apis-system-sensor.md)模块监听传感器值的变化，使用[@system.geolocation](../harmonyos-references/js-apis-system-location.md)模块监听地理位置的变化。仿真器提供以下虚拟传感器：

* **On-body status**：传感器所在设备穿戴状态，包括已穿戴和未穿戴。
* **Barometer：**气压传感器用于测量环境气压，单位为Pa。
* **Heart rate：**心率传感器用于测量心率数值，拖动滑动条，或直接输入心率大小。
* **Step count：**计步传感器用于统计行走步数，拖动滑动条，或直接输入步数。
* **Geographic location：**输入经度、纬度，模拟设备所处的地理位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/L4mP6mgDSeOIxMka4Nny4Q/zh-cn_image_0000002530912796.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=F2144F28B91E512DB8F35489D01859BC2B88BF52F90AED5C51328FE8F4B7FC56)

### 电池

您可以通过仿真器模拟不同的电池状态，包括以下三种充电状态，也可以手动输入或拖动滑动条来改变电量大小。在应用中，您可以通过[@system.battery](../harmonyos-references/js-apis-system-battery.md)模块查询仿真器的剩余电量以及充电状态。

* Not charging：未充电。
* Charging：正在充电。
* Wireless charging：无线充电。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/b7q-t0Z9RMuYna0K5d7_pQ/zh-cn_image_0000002530752798.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=0C5B18AA0DABDAFBD7AC4D409D968801F790F79BCF9B3880443FFFC357D43459)

### 设备设置

您可以更改设备的语言和地区，当前仅运行模式可以更改，调试模式暂不支持。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/oT4WctSpQaW1reAvX7f2HQ/zh-cn_image_0000002530912800.png?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=384FAFBE52B02F8CC98D1E95916F3028566177028EC1A0B2480A5ED652935D7E)

### 调试

* **Screen coordinate system****：**开启屏幕坐标系后，将光标移动到表盘上时，会显示屏幕坐标。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/aSOD6vKlTyyABgoX6qWEag/zh-cn_image_0000002530752806.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=A19E118D6E1260ED66C43C8417D8327590094BA09D720F010B8D8D731673DDD7 "点击放大")
* **Show device mask****：**关闭开关后，表盘周围的表冠颜色淡化。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/iOH0cgJVS1OUjjeE6dIpNg/zh-cn_image_0000002561752735.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054633Z&HW-CC-Expire=86400&HW-CC-Sign=0CEC430D05B924062189BC365785B2E1AAA0741DD1E1C5F9BEBA7B42ECAB2B77 "点击放大")
