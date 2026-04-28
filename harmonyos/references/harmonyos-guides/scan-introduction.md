---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-introduction
title: Scan Kit简介
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7147585040d7c8907dcfcccc704045011c381a0c88820221c6df8f745f6e8003
---

Scan Kit（统一扫码服务）作为软硬协同的系统级扫码服务，创新性地推出了更简单的“扫码直达”接入能力。只需少量的接入工作，无需在应用中开发专门的扫码模块，即可通过系统级扫码入口实现扫码到应用的跳转。同时还为开发者提供了面向各种场景的码图识别和生成能力。

Scan Kit应用了多项计算机视觉技术和AI算法技术，不仅实现了远距离自动扫码，同时还针对多种复杂扫码场景（如暗光、污损、模糊、小角度、曲面码等）做了识别优化，提升扫码成功率与用户体验。

为了方便开发者接入，我们提供了详细的样例工程供参考，推荐参考[示例工程](https://gitcode.com/HarmonyOS_Samples/scankit-samplecode-clientdemo-arkts)接入。

## 场景介绍

Scan Kit提供了系统“扫码直达”、开发者应用内扫码等多种能力。优先接入“扫码直达”能力，通过少量的接入工作即可实现开发者应用服务的一步直达。

* 扫码直达（推荐）：用户可通过控制中心等系统级的常驻入口，扫描开发者应用的二维码、条形码并跳转到开发者应用对应服务页，实现一步直达的体验。
* 默认界面扫码：提供系统级体验一致的扫码界面，包含相机预览流，相册扫码入口，暗光环境闪光灯开启提示，具备相机预授权，集成简单，适用于通用扫码场景。
* 自定义界面扫码：提供扫码能力并支持在指定控件上渲染相机预览流，需要开发者实现扫码界面，申请相机权限，适用于对扫码界面有个性化定制的场景。
* 图像识码：对图库中的码图或图像数据进行扫描识别。
* 码图生成：通过文本或字节数组生成码图。

说明

Scan Kit支持十三种全球主流的码制式的识别和生成以及MULTIFUNCTIONAL CODE的识别。目前已支持的码制式包括QR Code、Data Matrix、PDF417、Aztec、EAN-8、EAN-13、UPC-A、UPC-E、Codabar、Code 39、Code 93、Code 128、 ITF-14。

## 约束与限制

### 支持的设备

* 扫码直达能力仅支持Phone、Tablet。
* 默认界面扫码能力和自定义界面扫码能力仅支持Phone、Tablet、Wearable（从6.1.0(23)版本开始支持带后置相机的Wearable，可以通过[cameraManager.getSupportedCameras](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机）。
* 图像识码能力仅支持Phone、Tablet、Wearable（从6.1.0(23)版本开始支持Wearable）。
* 码图生成能力支持Phone、Tablet、Wearable、2in1、TV（从5.1.0(18)版本开始支持Wearable、从5.1.1(19)版本开始支持2in1、TV）。

### 功能使用限制

| 能力 | 限制条件 |
| --- | --- |
| 扫码直达能力 | 1. 当前只支持开发者配置HTTPS架构的网页链接接入扫码直达。其他方式接入如HTTP配置可以通过[工单](https://developer.huawei.com/consumer/cn/support/feedback/#/)联系我们。  2. 当前仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）接入使用。 |
| 默认界面扫码能力 | 从6.1.0(23)版本开始，标题支持根据[ScanOptions](../harmonyos-references/scan-scanbarcode-api.md#scanoptions)的scanTypes进行动态显示；从6.0.0(20)版本开始，支持悬浮屏、分屏场景；相册扫码只支持单码识别；不支持界面UX添加自定义设置。 |
| 自定义界面扫码能力 | 需要授权使用相机权限；需要开发者自行实现扫码的人机交互界面。 |
| 码图生成能力 | 通过字节数组生成码图时，若Scan Kit识别某码图内容显示内容为乱码，则该码图的字节数组需要通过专门的解码器解析，例如地铁闸机。 |

## 模拟器支持情况

本Kit支持模拟器开发，但与真机存在部分能力差异，具体差异如下：

* 通用差异：请参见“[模拟器与真机的差异](ide-emulator-specification.md#section1227613205203)”。
* 从6.0.0(20)版本开始，模拟器支持默认界面扫码能力开发，模拟器中默认界面扫码的相机流存在镜像问题，且由于仅支持固定分辨率比例，画面会出现上下黑边。
* 模拟器部分支持自定义界面扫码能力。

  + 从6.0.0(20)版本开始，模拟器支持部分自定义界面扫码接口开发（支持的接口包括[init](../harmonyos-references/scan-customscan-api.md#customscaninit)、[start](../harmonyos-references/scan-customscan-api.md#customscanstart)、[stop](../harmonyos-references/scan-customscan-api.md#customscanstop)、[release](../harmonyos-references/scan-customscan-api.md#customscanrelease)、[rescan](../harmonyos-references/scan-customscan-api.md#customscanrescan)），可实现自定义界面扫码能力的基本功能验证。
  + 模拟器自定义界面扫码能力仅支持1280\*720分辨率，开发者传入其他分辨率会统一转换成1280\*720。
* 模拟器不支持图像数据识别能力、码图生成能力。

## 示例代码

Scan Kit提供的[示例工程](https://gitcode.com/HarmonyOS_Samples/scankit-samplecode-clientdemo-arkts)体现了Scan Kit的默认界面扫码、自定义界面扫码、图像识码、码图生成等特性，可参考该工程进行应用的相关内容开发。
