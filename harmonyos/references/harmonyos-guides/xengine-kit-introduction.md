---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xengine-kit-introduction
title: XEngine Kit简介
breadcrumb: 指南 > 图形 > XEngine Kit（GPU加速引擎服务） > XEngine Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a966e57ae4511496b67196e93aff4fde1fbfc6d0cff690b086deefc7b22b378f
---

XEngine Kit（GPU加速引擎服务）提供基于马良GPU的性能提升方案，包括GPU/AI超分能力、自适应VRS（Variable Rate Shading，可变速率着色）、Subpass Shading、光线追踪技术（包括反射、阴影、环境光遮蔽和全局光照，Ray-Traced Reflection, Shadow, Ambient Occlusion and Global Illumination）和高性能着色器（High performance shaders，简称HPS）等，通过图形算法以及软硬件优化，让用户拥有更高画质、更高性能、更低功耗的3D游戏/应用、AR/VR体验。

## 基本概念

在进行XEngine Kit开发前，建议开发者提前了解以下基本概念：

* [XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件：是一种绘制组件，通常用于满足开发者较为复杂的自定义绘制需求，例如相机预览流的显示和游戏画面的绘制。
* 可变速率着色（Variable Rate Shading，简称VRS）：是一种图形功能，允许应用程序独立于渲染目标的分辨率来控制像素着色器调用的频率。自适应可变速率着色（Adaptive VRS）在VRS的基础上，添加了可动态调整的着色率，能够大幅提升渲染性能。
* 基于瓦片的延迟渲染（Tile-Based Deferred Rendering，TBDR）：是一种渲染技术，它结合了即时渲染（Immediate Mode Rendering, IMR）和延迟渲染（Deferred Rendering）的优点，旨在提高渲染效率和减少内存访问。
* 动态漫反射全局光照（Dynamic Diffuse Global Illumination，简称DDGI）：是一种实时渲染技术，旨在模拟光线在场景中经多次漫反射后的全局光照效果，以提升画面真实感。

## 场景介绍

### 优化细节画质，降低能耗

当GPU性能不足以支持渲染高分辨率场景时，为了提高用户体验，可以使用超分能力，将较低分辨率图像通过超分重建为高分辨率图像。相较于直接渲染高分辨率图像，使用超分能力能够降低GPU渲染负载，降低功耗。目前支持以下3种超分能力：

* 空域GPU超分：基于单帧图像的空域超采样，开销最低。
* 空域AI超分：GPU/NPU协同空域超采样，效果更好。
* 时域AI超分：GPU/NPU协同时域超采样，抗锯齿效果明显，画质更优，倍率更高。

### 画质视觉无损，智能降低渲染开销

当GPU性能限制，不能持续为输出图像的每个像素提供相同质量级别的渲染结果时，可使用自适应VRS功能，其通过合理分配画面的计算资源，视觉无损降低渲染频次，使不同的渲染图像使用不同的渲染速率，能够有效提高渲染性能。

### 降低带宽开销，提升性能

对于TBDR（Tile-Based Deferred Rendering，基于瓦片的延迟渲染）和Forward+管线，Subpass Shading能力可以有效降低带宽开销，提升性能。

### 光线追踪加速技术，高效利用硬件光追能力

当GPU支持硬件光线追踪能力时，可以使用光线追踪渲染技术，提升场景的光影效果和画面质量。

* **反射、阴影和环境光遮蔽**

  XEngine Kit提供开箱即用的光线追踪渲染技术，包括反射（Reflection）、阴影（Shadow）和环境光遮蔽（Ambient Occlusion，AO）效果的相关API。相比于这些效果的传统光线追踪实现方式，XEngine Kit可以在较少光线数的情况下达成较高的画质表现，实现同等画质GPU负载更轻，同等负载下画质更好。
* **全局光照**

  XEngine Kit全局光照解决方案，基于硬件光线追踪、AI渲染和端云结合渲染等技术，实现移动端的实时全局光照，包括动态漫反射全局光照（Dynamic Diffuse Global Illumination，DDGI）和神经网络全局光照（Neural Network Global Illumination，NNGI）两种技术。DDGI更轻量级，配合端云渲染能效更佳，而NNGI则能够提供移动端更好的动态GI画质。

### 高性能GPU排序

高性能GPU排序可以帮助我们更快地将乱序信息进行整齐排列，降低排序时延，提升性能。

## 约束与限制

* 在调用XEngine Kit能力前，需要先通过[Syscap](../harmonyos-references/syscap.md#判断-api-是否可以使用)查询您的目标设备是否支持SystemCapability.Graphic.XEngine系统能力。
* 支持的设备类型：Phone、Tablet、PC/2in1、TV。
* XEngine Kit特性仅在使用马良GPU芯片的设备上受支持。不同设备支持的特性范围有所差异，可以通过以下方式查询设备支持的特性列表：

  + 对于OpenGL ES，使用[HMS\_XEG\_GetString](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_getstring)扩展特性查询接口进行查询。
  + 对于Vulkan，使用[HMS\_XEG\_EnumerateDeviceExtensionProperties](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)扩展特性查询接口进行查询。

  两种方式均返回所支持的特性列表，具体使用方式参考各个特性的示例代码。

## 模拟器支持情况

本Kit暂不支持模拟器。
