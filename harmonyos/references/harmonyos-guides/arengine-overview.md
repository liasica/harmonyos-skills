---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-overview
title: AR Engine简介
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > AR Engine简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:47+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:d81c871aedc7b5fc9da75a8165f3cf372b139831f69c091c3a062c276a7fe433
---

AR Engine（AR引擎服务）是一个用于在HarmonyOS上构建增强现实应用的引擎，提供了运动跟踪、环境跟踪等空间计算能力。

## 能力介绍

AR Engine主要包含运动跟踪与平面识别特性、平面语义及物体语义特性、环境Mesh识别特性、深度估计特性、图像跟踪特性、高精几何重建特性、人脸识别与跟踪特性、人体骨骼点识别与跟踪特性。

通过这些能力，应用可以实现虚拟世界与现实世界的融合，给用户提供全新的视觉体验和交互方式。

### 环境识别与运动跟踪能力

* [运动跟踪](arengine-get-pose-conversion.md)：实时获取设备位置和姿态
* [平面识别](arengine-get-plane-conversion.md)：识别环境中的平面
* [命中检测](arengine-arworld-conversion.md)：获取碰撞检测结果后可以在识别的平面上放置虚拟物体
* [平面语义](arengine-get-semantics-conversion.md)：识别环境中的平面类型
* [物体语义](arengine-get-plane-shape-conversion.md)：识别平面上的物体形状
* [环境Mesh识别](arengine-get-mesh-conversion.md)：获取环境Mesh数据
* [深度估计](arengine-get-depth-conversion.md)：获取环境的深度信息
* [高精几何重建](arengine-get-volume-measurement-conversion.md)：输出环境中的稠密点云，识别立方体、嵌入式立方体空间

### 人体骨骼识别与跟踪能力

* [人体骨骼点识别与跟踪](arengine-body-conversion.md)：识别环境中的人体骨骼点信息

### 人脸识别与跟踪能力

* [人脸识别与跟踪](arengine-face-conversion.md)：识别环境中的人脸信息

### 图像识别与跟踪能力

* [图像跟踪](arengine-get-image-track-conversion.md)：识别环境中已预置在AR Engine中的图像并输出图像位置和姿态

## 坐标系说明

### AR Engine重力对齐世界坐标系

* 以相机启动时相机中心为坐标原点；
* 重力方向为Y轴，向上+Y，向下-Y；
* 设备水平前后移动为X轴，由近及远+X，由远及近-X；
* 设备水平左右移动为Z轴，向右+Z，向左-Z。

**图12** 重力对齐世界坐标系示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/Q2AhFUjPSVqqPALD3J41Iw/zh-cn_image_0000002552958616.png?HW-CC-KV=V1&HW-CC-Date=20260427T234646Z&HW-CC-Expire=86400&HW-CC-Sign=D66ED4E8A2A24441588A23A3F5AD2F437BCD5C6408782351F17A97AB6FD6539E)

### AR Engine重力对齐北向坐标系

* 以相机启动时相机中心为坐标原点；
* 重力方向为Y轴，向上+Y，向下-Y；
* 指南针北向为+X轴，南向为-X轴；
* 指南针东向为+Z轴，西向为-Z轴；
* 重力对齐北向坐标系为固定坐标系，不受设备位姿变化影响。

**图13** 重力对齐北向坐标系示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/7WvK5xWURw2HxA5TxT2KYQ/zh-cn_image_0000002583478617.png?HW-CC-KV=V1&HW-CC-Date=20260427T234646Z&HW-CC-Expire=86400&HW-CC-Sign=4856F52817E5B5C85482A5266DE6FE7121EC19F60D9384AE6CE9DAF8CE0028FE)

### AGP世界坐标系

* 以相机启动时相机中心为坐标原点；
* 设备垂直方向为Y轴，向上+Y，向下-Y；
* 设备水平前后移动为Z轴，向前+Z，向后-Z；
* 设备水平左右移动为X轴，向左+X，向右-X。

**图14** AGP世界坐标系示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/nzS4Rx0vQgyP5X7sLh9InA/zh-cn_image_0000002552958616.png?HW-CC-KV=V1&HW-CC-Date=20260427T234646Z&HW-CC-Expire=86400&HW-CC-Sign=3F0714F54696F87E13262EC11F953ECD9AA3F901C07BEFD73DA0F5F25F8C2C15)

## 约束与限制

* 在调用AR Engine能力前，需要先通过[Syscap](../harmonyos-references/syscap.md#判断-api-是否可以使用)查询您的目标设备是否支持SystemCapability.AREngine.Core系统能力。
* 支持的设备类型：Phone、Tablet。从6.1.0(23)版本开始，新增支持TV。
* 不同设备支持的特性范围有所差异，可以通过以下方式查询设备是否支持对应的特性：

  + 对于C API，使用[HMS\_AREngine\_CheckSupported](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_checksupported)拓展特性查询接口进行查询。
  + 对于ArkTS API，使用[arViewController.isARTypeSupported](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)拓展特性查询接口进行查询。

  两种方式均返回对应的特性是否支持，具体使用方式参考各个特性的示例代码。

## 支持的国家/地区

本Kit当前仅支持在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）接入使用。

## 模拟器支持情况

本Kit暂不支持模拟器。
