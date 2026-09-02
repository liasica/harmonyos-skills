---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-introduction
title: Graphics Accelerate Kit简介
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:50+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bf41da86f0a1b68ba730fa7204df065a96d21ac107574021c4fc202fd98b9179
---

Graphics Accelerate Kit（图形加速服务）是集成了先进的图形渲染加速和资源管理优化的综合解决方案，旨在通过软硬件协同优化，全面提升图形处理相关应用的性能和用户体验。该服务的应用场景包括游戏、AR、VR、UI交互渲染、3D动效等。其中，游戏作为端侧典型的重负载GPU渲染场景。本Kit已构建四大核心服务：游戏渲染加速服务、游戏资源加速服务、游戏启动加速服务、游戏伴随服务。

## 业务介绍

* 游戏渲染加速服务

  游戏渲染加速服务作为软硬件协同的系统级图形加速解决方案，帮助游戏应用快速构建超帧、ABR（自适应稳态渲染）、OpenGTX（Open GPU Turbo X）等游戏渲染加速能力，解决游戏运行不流畅、卡顿掉帧、长时间运行造成发热发烫等痛点体验问题。

  | 功能模块 | 描述 |
  | --- | --- |
  | [超帧](graphics-accelerate-fg.md) | 针对GPU重负载的高目标帧率游戏场景，超帧利用渲染管线中的时域和空域信息，通过软硬件结合的MEMC（运动估计、运动补偿）技术，在游戏真实渲染帧间高效插入预测帧。在最大程度保持原始渲染画质前提下，有效提升游戏帧率和运行流畅度，降低系统负载和功耗，延长手机的续航时间。 |
  | [ABR](graphics-accelerate-abr.md) | 针对GPU重负载游戏场景，通过感知游戏、设备状态，自适应决策分辨率缩放因子，并基于FrameBuffer（帧缓冲，下文简称Buffer）调整分辨率，帮助游戏应用实现更稳定的帧率、更低的功耗。 |
  | [OpenGTX](graphics-accelerate-opengtx.md) | 针对高帧率重负载游戏场景，LTPO（动态帧率/刷新率）等方案通过动态感知游戏渲染状态、游戏场景、设备状态等信息，自适应调整游戏的帧率、设备的SOC/DDR频率，在不影响用户游戏体验的前提下，有效降低系统负载和功耗。 |
* 游戏资源加速服务

  游戏资源加速服务旨在利用后台任务调度、预加载等技术手段，实现资源包的高效后台更新和管理，降低游戏启动的等待时间，避免由于游戏内的资源包更新导致玩家流失。

  | 功能模块 | 描述 |
  | --- | --- |
  | [资源包后台下载](graphics-accelerate-assetdownload-introduction.md) | 将资源文件（例如关卡包、3D角色模型、纹理等）静默下载到用户设备中，减少游戏启动后等待资源包下载的时间，解决游戏启动慢的问题，为用户提供即开即玩的游戏体验。 |
* 游戏启动加速服务

  游戏启动加速服务作为系统级启动优化方案，通过引入秒级启动与预启动两种机制，帮助游戏全面提升启动性能，减少启动等待时间，带来更加流畅、顺滑的启动体验。

  | 功能模块 | 描述 |
  | --- | --- |
  | [秒级启动](graphics-accelerate-launch-introduction.md) | 在游戏退出时，系统自动为游戏制作内存镜像，在该游戏下一次冷启动时，可通过加载内存镜像实现游戏的秒开秒进，无需再经过漫长的加载过程，大大提升了游戏操控体验。 |
  | [游戏预启动](graphics-accelerate-preload-introduction.md) | 系统根据用户的使用习惯，在资源充足时提前加载游戏进行部分初始化和资源加载，从而在用户触发启动时显著缩短游戏启动时间，提升用户体验。 |
* 游戏伴随服务

  游戏伴随服务为游戏陪玩类的应用提供游戏状态感知、游戏截图等基础能力。

  | 功能模块 | 描述 |
  | --- | --- |
  | [游戏状态感知](graphics-accelerate-gamebuddyservice-development.md) | 接收游戏前后台状态变化通知，游戏伴随服务可持续监听游戏状态变化，当游戏状态变化时，通知已注册的客户端应用。 |
  | [游戏截图](graphics-accelerate-gamebuddyservice-development.md) | 获取游戏当前画面截图，支持文件描述符方式获取截图数据。 |

## 约束和限制

### 支持的国家/地区

本Kit仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

### 支持的设备

| 核心服务 | 支持的设备 |
| --- | --- |
| 游戏渲染加速服务 | Phone、Tablet、TV |
| 游戏资源加速服务 | Phone、Tablet、PC/2in1 |
| 游戏启动加速服务 | Phone、Tablet、PC/2in1 |
| 游戏伴随服务 | Phone |

## 模拟器支持情况

本Kit暂不支持模拟器。
