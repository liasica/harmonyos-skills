---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-developer-mode
title: 开发者选项
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 开发者模式 > 开发者选项
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f00ab8e3e89803f8d5de3f7476d4fbae86258bd3800c141101f21d2367482261
---

HarmonyOS系统上的“设置”包含开发者选项的界面，用于辅助HarmonyOS应用程序开发、测试及优化，面向开发人员提供商业发行版之外的功能（如API能力），提供更多的调试选项及能力；您可在该界面中通过配置选项来帮助您分析和调试应用，例如，您可以通过启用USB/无线调试进行应用调试、开启DFX稳定性相关选项获取更多应用的故障及性能信息、开启过度绘制等选项快速发现性能问题等等。

## 启用开发者选项

在Phone或Tablet上查看**设置 > 系统**中**开发者选项**是否存在，如果不存在，可在**设置 > *具体的设备名称***中，连续点击**软件版本**七次，直到提示“开启开发者选项”，点击**确认开启**后输入PIN码（如果已设置），设备将自动重启，请等待设备完成重启。

## 禁用开发者选项

在Phone或Tablet上点击**设置 > 系统** **> 开发者选项**，关闭开发者选项开关，弹出提示框后点击确认关闭，设备会自动重启。

## 常规选项

* **充电温度限制**：防止手机充电时过热，用于对充电温度进行严格控制。
* **系统回退**：支持开发者将终端设备从HarmonyOS NEXT回退到HarmonyOS。

## 调试

* **USB调试**：如果开发者希望通过计算机侧命令对移动设备进行调测，需要启用USB调试，同时通过设备授权确认。开启并授权后，HarmonyOS设备才能连接到计算机进行调试，可用于在计算机和设备之间复制数据、在设备上安装或卸载调试应用、以及读取日志数据等。

* **无线调试**：通过Wi-Fi进行设备连接从而实现设备的调测，在开启无线调试后，可以查看设备的IP地址和端口，通过[DevEco Studio或hdc命令](ide-run-device.md#section9315596477)进行设备连接。使用过程中需要确保您的设备与计算机在同一个Wi-Fi网络中，初次连接需要进行设备授权确认。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/SucR8lzdS7eSsJnbUEqC-Q/zh-cn_image_0000002561753121.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=84AF3BDE9819E3195B335BEE37E748882D22FA36AB0B9E04345A54EBD1E437D5 "点击放大")
* 清除受信任设备：针对之前授权过的所有计算机，撤销USB/无线调试的访问权限。

DFX稳定性配置选项包括：

* **系统trace跟踪**：可以将系统采集的trace落盘到本地文件，便于本地问题定位及故障上报。
* **冻屏信息日志**：稳定性在故障时会生成稳定性日志，提供更详细的日志信息。
* **系统资源泄漏日志**：稳定性在故障时会生成内存相关日志，用于定位资源泄漏问题，提供更详细的日志信息。

其他调试选项包括：

* **意图框架调试**：方便开发者在设备上验证意图框架，可以关闭部分校验机制并直接显示最近使用的意图。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/L7cypcqXRW287YcDPAkJNA/zh-cn_image_0000002530753188.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=964E651B6C5B67BD20A41B89CE0FB98C794EB9AD273CEEA80E1F2BFF46C47AB8 "点击放大")
* **显示刷新频率**：刷新频率是指显示器每秒钟更新画面的次数，可在屏幕左上方显示刷新率档位和RenderService实时帧率，更好地了解设备性能和屏幕表现，从而进行针对性的优化或调整。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/D8IkieilRf--8AzKelzgzg/zh-cn_image_0000002530753194.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=35117AED21ED66FF48F353666840A5754CFF300F4539122C8E0ACE0551A68858 "点击放大")
* **关闭充电**：连接USB后默认充电，如果开发者希望不充电，需手动打开开关，插拔USB后可恢复默认充电状态。

## 网络

* **网络领航员**：开启网络领航员后，开发者可以选择预置的网络模拟场景或者自定义网络模拟场景进行网络验证，提升APP体验的测试及验证效率，具体使用方式请参考[网络领航员](network-navigator.md)。

## 输入

* **显示触摸操作：**开启开关后，当用户触摸屏幕时, 会有一个小圆点跟随手指移动，显示用户的触摸动作。
* **指针位置：**开启指针位置后，屏幕上会出现十字准线，可以显示指针（点按）位置。屏幕上方会显示一个条形，用于跟踪十字准线的坐标。移动指针时，该条形中的坐标会跟踪十字准线位置，且屏幕上会绘制出指针路径。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/LCkHB6VuRoaUPRKz9y8N5A/zh-cn_image_0000002561753113.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=49F7BB431C41D197244350C2753C02A59AC0B09C683EB2461D4C497932EB7D71 "点击放大")

## 绘图

* **显示布局边界**：开启后可以显示应用的裁剪边界、外边距和设备上的其他界面结构，方便开发者查看控件布局、空白空隙及控件重叠等问题。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/5pIAVk_TT4Ks8HhFEKgJug/zh-cn_image_0000002561753115.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=A555A536D745B9002FA402F353EC063F4D9FC3CF5EC3763A218317AF17B60A63)

* **显示重绘刷新区域**：当点击、滚动屏幕或者系统自动刷新使得屏幕上的某块区域重新绘制时，该区域突出显示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/HqbSo3PeRe6lAxjZEc7j0Q/zh-cn_image_0000002561753117.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=08141CA50E80BACC957987F26F92E598EA7180BBD03D913E1F5F2692CA158AF1)
* **缓存是否命中检测**：在一些属性动画的场景下，您可以使用renderGroup缓存提升属性动画性能；开启选项后，检测缓存未命中的场景，通过颜色标识。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/0RHyt82hRryBOQ9Mlmfxrw/zh-cn_image_0000002561833101.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=13BB8A36D065E4FC3F4410F6489AD792106EE254AE7D76462A166E7821ED8947 "点击放大")
* **过度绘制检测**：显示设备上的颜色编码，以便可视化相同像素在同一帧中绘制的次数，可视化会显示应用可能在哪里进行了不必要的渲染。过度绘制的程度可以通过颜色来表示。
* **过渡动画缩放**：设置过渡动画播放速度，便于开发者查看不同速度下的性能。缩放越小，速度越快。

## 应用

* **开发中元服务豁免管控**：嵌入式运行元服务能力默认是受限的，需要开发者申请权限才能使用。如果在申请权限之前的开发调试阶段想临时开启权限，可以通过开启本选项获取调试嵌入式元服务的权限。
