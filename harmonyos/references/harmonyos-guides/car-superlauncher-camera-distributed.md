---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/car-superlauncher-camera-distributed
title: 超级桌面应用接入分布式相机
breadcrumb: 指南 > 系统 > 硬件 > Car Kit（车服务） > 超级桌面应用接入分布式相机
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bc971362c510824bcfb50c605ace9c427fff82f60391364541e614f9feaf80b8
---

## 场景介绍

超级桌面是一种手机、车机互联的特性，车主可以通过超级桌面，将华为手机上的应用共享至中控屏，在中控屏上使用丰富的手机应用。

手机和车机通过超级桌面连接后，当在车机上使用超级桌面应用需要调用车机摄像头（例如视频通话/会议场景）时，可选择接入远端分布式相机能力，在本端设备（手机）获取并展示远端设备（车机）相机画面，最终共享在车机中控屏上显示。

## 环境准备

手机和车机之间需要超级桌面建连成功并且待接入分布式相机的应用在超级桌面已打开。

## 开发指导

应用如需在超级桌面场景中使用车机摄像头实现视频通话/会议等功能，详细开发指导请参见[相机服务](camera-kit.md)。
