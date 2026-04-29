---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/car-introduction
title: Car Kit简介
breadcrumb: 指南 > 系统 > 硬件 > Car Kit（车服务） > Car Kit简介
category: harmonyos-guides
scraped_at: 2026-04-29T13:33:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c540215de46f01c8ad6d7c0c43d908e5d4c81146003b565c7bc858a6e980453c
---

Car Kit（车服务）为开发者提供一套便捷接入出行服务的能力，开发者通过集成Car Kit，可以轻松实现在手机与鸿蒙智行车机之间无缝传递导航信息、通过超级桌面在鸿蒙智行车机上使用手机上的应用、通过HiCar在认证车机上使用手机上的应用等功能，为用户提供更加良好的出行体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/aZFDfC-AQEaw4hr7LuGFWw/zh-cn_image_0000002558605308.png?HW-CC-KV=V1&HW-CC-Date=20260429T053327Z&HW-CC-Expire=86400&HW-CC-Sign=466A5DEA0E01000546268DF414D315C8E26F8FC73FC51123B6F860E4EA1D929B)

## 场景介绍

Car Kit为华为手机用户提供驾驶鸿蒙智行车辆的出行场景和驾驶HiCar认证车辆的出行场景两类解决方案。

### 驾驶鸿蒙智行车辆的出行场景

如果用户驾驶鸿蒙智行车辆（包括仪表/HUD显示）出行，华为提供了导航流转和超级桌面解决方案：

导航流转：

* 是华为为用户提供的手机与车机之间无缝传递导航信息的解决方案，涵盖多种使用场景，如导航信息流转至车机、地址流转至车机，以及下车后地图导航自动流转回手机，实现步行导航接续等。
* 应用通过接入 Car Kit 的导航类接口，提供导航信息，响应系统流转事件，从而完成手机与车机之间的导航流转业务。

超级桌面：

* 是华为为用户提供手机应用在鸿蒙座舱车机操作系统上使用，丰富鸿蒙智行生态的解决方案。
* 应用接入Car Kit出行互联类接口，可根据超级桌面连接状态，获取车机的屏幕信息用于UI呈现，或使用车机摄像头优化业务交互等。

### 驾驶HiCar认证车辆的出行场景

如果用户驾驶HUAWEI HiCar（以下简称HiCar ）认证车辆出行，华为提供了HiCar互联解决方案：

* HiCar将移动设备和HiCar认证车辆连接起来，利用车辆和移动设备各自的软硬件以及多设备互联能力，给用户创造智慧出行体验。
* 应用接入Car Kit出行互联类接口，可根据HiCar连接状态，获取HiCar认证车辆的屏幕信息用于用户UI呈现，或使用HiCar认证车辆摄像头优化业务交互等。

## 实现原理

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/27qhfet-SHCV4N_1K81UZw/zh-cn_image_0000002589324833.png?HW-CC-KV=V1&HW-CC-Date=20260429T053327Z&HW-CC-Expire=86400&HW-CC-Sign=D8C4D03268B706358DD9BDBE564A0803AF9142B743628AD21296E5C20C47BBD3)

Car Kit处于HarmonyOS的框架层，作为生态应用和系统应用之间的桥梁。

1. 系统应用向Car Kit订阅导航数据的变化：当生态应用导航数据发生变化时通知到Car Kit，Car Kit会将导航数据的变化转发给系统应用。
2. 生态应用向Car Kit订阅系统事件：当系统应用希望生态应用执行任务时通知到Car Kit，Car Kit会将系统事件转发给生态应用。
3. 生态应用向Car Kit订阅智慧出行连接状态的变化：当智慧出行连接状态发生变化时，Car Kit会将当前智慧出行连接状态转发给生态应用。

## 约束和限制

### 支持的国家/地区

当前仅在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）提供服务。

### 支持的设备

本Kit从4.1.0(11)开始支持Phone设备，并且从6.1.0(23)版本开始，新增支持Tablet设备。

## 模拟器支持情况

本Kit暂不支持模拟器。
