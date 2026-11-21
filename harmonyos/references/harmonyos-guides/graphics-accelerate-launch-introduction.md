---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-introduction
title: 业务概述
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏启动加速服务 > 秒级启动 > 业务概述
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:aa19d9caa3dad5d49aa3a01a413ab0a021ce6e0b1dd52c78da2d9c7b17146811
---

秒级启动是在游戏退出时，开发者先切换场景，系统再自动为该场景制作内存镜像。在该游戏下一次无资源更新冷启动时，可以直接进入内存镜像界面，实现游戏的秒开秒进，无需再经过漫长的加载过程。

## 约束与限制

秒级启动自6.0.0(20)版本起支持Phone、Tablet设备，并在6.1.0(23) 版本中新增对PC/2in1设备的支持。

## 基本概念

| 概念 | 说明 |
| --- | --- |
| 切换场景 | 游戏退出时，开发者需要先切换游戏场景，系统再根据该场景自动制作内存镜像。等到下一次游戏无资源包更新冷启动时，游戏直接到达该游戏场景。  因为游戏登录界面具备内存占用率低、处于相对稳定的运行状态等优势，建议开发者在游戏退出时将**游戏登录界面**保存为内存镜像，大幅降低切换场景过程中的适配问题。 |

## 用户体验

打开游戏时，自动跳过游戏开头动画，直达游戏界面。

* 加载内存镜像

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/BEkFaq5wT5O0fSnivwxZBQ/zh-cn_image_0000002821757735.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011046Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D4AC0A755D1197AF6C35C20193EF1CA90F2C19B58A9AFD3C031B5458E7D7312)
* 未加载内存镜像

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/H6jE9ku_TFi-rIlvxzPJ3Q/zh-cn_image_0000002793037798.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011046Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E50585B46954281D503864E023EBA2E43B305588484B0FD9C78D3EA3030F7FE)

## 快速上手体验

在正式开发之前，开发者可以通过[Codelab](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_LaunchAcceleration-ArkTS)快速体验秒级启动的开发过程。
