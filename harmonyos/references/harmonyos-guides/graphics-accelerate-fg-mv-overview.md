---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-fg-mv-overview
title: 概述
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > 超帧功能开发 > 顶点标记 > 概述
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:50+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:5f5e2188e12a5fe004e4df9c016cd315f7af8cc435c4406b3ecee2d807a0b4ec
---

从6.0.0(20)版本开始，新增支持顶点标记的Vulkan平台能力。

超帧提供两种运动估计模式供开发者选择：分别为基础模式和增强模式。其中增强模式需要对绘制顶点的Draw Call命令进行额外的标记，在相机和物体快速运动的游戏场景超帧效果较基础模式更优，能够有效改善拖影问题。本章主要介绍增强模式的运动估计原理及顶点标记方法。

**说明** 

Draw Call：指图形驱动库（OpenGL ES、Vulkan）中进行绘制的命令，例如glDrawElements、glDrawArrays、glDrawElementsInstanced、vkCmdDraw等。

| 运动估计模式 | 描述 |
| --- | --- |
| 基础模式 | 利用历史帧颜色信息、深度信息及相机矩阵信息进行运动估计。 |
| 增强模式 | 利用历史帧中的几何顶点信息进行更精准的运动估计，绘制的预测帧质量更高。 但该模式需要开发者对绘制顶点的Draw Call命令进行额外的标记，且仅支持马良910 GPU及以上的Phone、Tablet设备，在不支持的平台上会切换成默认模式。 |
