---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-overview
title: 业务概述
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > 业务概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6109f5f2a56ffff602887dd0243d9a06f9660373b237901872d3c448e83d7b7d
---

## 约束与限制

游戏渲染加速服务支持Phone、Tablet设备，并且从6.1.0(23)版本开始，新增支持TV设备。

## 亮点/特征

* **稳定帧率，减少卡顿、掉帧现象**

  游戏应用集成超帧、ABR后，在无画质损耗的基础上，可有效稳定或提升游戏运行帧率，减少卡顿和掉帧现象，使游戏运行更加稳定、流畅。集成OpenGTX后，通过感知游戏场景、设备状态等关键信息，动态调整游戏的帧率/刷新率以及设备的SOC/DDR频率，从而做到稳定帧率，保障游戏在终端设备上流畅运行。
* **降低功耗和发热，延长续航时间**

  游戏应用集成超帧、ABR后，在GPU重负载游戏场景，单帧功耗可降低10%及以上，可有效降低GPU负载和系统功耗，减轻手机发热现象，延长续航时间。集成OpenGTX后，通过对游戏的帧率控制以及设备的SOC/DDR频率控制，在满足用户游戏体验的前提下，最大限度的降低设备的性能开销，从而做到降低功耗减少发热，提升设备的续航时间。

## 场景介绍

* 超帧

  为满足不同游戏场景的使用需求，我们为开发者提供了两种超帧模式供选择，分别是内插模式和外插模式。具体适用场景参见下方表格。

  | 超帧模式 | 适用场景 |
  | --- | --- |
  | [内插模式](graphics-accelerate-fg-interpolation.md) | 适用于对渲染画质和运行流畅度要求高的游戏，如角色扮演游戏、竞速类游戏等。 |
  | [外插模式](graphics-accelerate-fg-extrapolation.md) | 适用于对响应时延和操作跟手性要求高的游戏，如动作类游戏、射击类游戏等。 |
* ABR

  | ABR策略 | 适用场景 |
  | --- | --- |
  | [基于相机运动的感知策略](graphics-accelerate-abr.md) | 适用于竞速类游戏、角色扮演类游戏、射击类游戏等，在加速、奔跑、视角旋转等场景自适应调整Buffer分辨率，在用户对画质影响感知不明显的前提下，帮助游戏应用实现更稳定的帧率、更低的功耗。 |
* OpenGTX

  针对高帧率重负载游戏场景，OpenGTX LTPO方案提供了三种动态帧率/刷新率控制模式，分别是SCENE\_MODE、TOUCH\_MODE、ADAPTIVE\_MODE，具体使用场景参见下方表格。

  | LTPO模式 | 适用场景 |
  | --- | --- |
  | [SCENE\_MODE](../harmonyos-references/_graphics_accelerate.md#opengtx_ltpo_mode-1) | 根据场景设置不同的游戏帧率，如游戏场景120fps。 |
  | [TOUCH\_MODE](../harmonyos-references/_graphics_accelerate.md#opengtx_ltpo_mode-1) | 根据触控频率设置游戏帧率。 |
  | [ADAPTIVE\_MODE](../harmonyos-references/_graphics_accelerate.md#opengtx_ltpo_mode-1) | 根据场景、相机、触控等自适应控制游戏帧率，包含SCENE\_MODE和TOUCH\_MODE。 |

## 场景约束

* 超帧

  + 超帧适用于GPU重负载的高目标帧率游戏场景：在负载较轻的游戏场景开启超帧可能存在功耗负收益，在目标帧率低于60fps游戏场景开启超帧可能引入拖影现象。
  + 超帧运动估计模式分为“基础模式”和“增强模式”，下表说明两种模式的使用约束。

    | 运动估计模式 | 开发准备 | 场景约束 |
    | --- | --- | --- |
    | 基础模式 | - | 适用于相机或场景中物体静止以及慢速运动的游戏场景。在高速运动目标场景及复杂粒子特效场景可能引入拖影和鬼影。 |
    | 增强模式 | 需要开发者对绘制顶点的draw call进行标记。相比基础模式，增强模式利用三维场景中的顶点信息进行更精准的运动估计，超帧效果更优。 | 对于相机或物体慢速和快速运动场景均具有较好超帧效果，较基础模式能有效优化运动拖影现象。但在复杂粒子特效场景可能引入鬼影。 |
  + 超帧API不支持并发调用。
* ABR

  + ABR目前只支持对一个Buffer进行自适应分辨率调整，请结合游戏渲染管线各Pass（通道）的GPU负载情况，选择GPU重负载Pass对应的Buffer使能ABR。
  + ABR API不支持并发调用。
* OpenGTX

  设备规格：设备需要支持LTPO（Low Temperature Polycrystalline Oxide）屏幕。
