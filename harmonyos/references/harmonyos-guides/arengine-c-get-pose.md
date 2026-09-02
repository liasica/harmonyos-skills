---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-pose
title: 获取设备位姿（C/C++）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 运动跟踪 > 获取设备位姿（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:19+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:848f8aa9fd2cb649ba2f360975f6f00b454fa147ca8cb84d15c6ebbbe99e46bf
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/harmonyos_samples/arengine_-sample-code_-clientdemo_cpp)。

## 约束与限制

从5.0.0(12)开始，获取设备位姿能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_SLAM](../harmonyos-references/arengine-capi-arengine.md#arengine_featuretype)）。

## 创建ARSession

开发者可以参考[管理AR会话](arengine-c-arsession.md)创建ARSession。

## 获取设备当前位姿

1. 创建一个空位姿变量cameraPose。

   ```
   AREngine_ARPose *cameraPose = nullptr;
   CHECK(HMS_AREngine_ARPose_Create(arSession, nullptr, 0, &cameraPose));
   ```
2. 获取当前时刻相机位姿信息，并存储在cameraPose变量中。

   ```
   CHECK(HMS_AREngine_ARCamera_GetPose(arSession, arCamera, cameraPose));
   ```
3. 从cameraPose中获取相机位姿的不同分量，包括平移分量和旋转分量。

   ```cpp
   float poseRaw[7] = { 0.0f };
   HMS_AREngine_ARPose_GetPoseRaw(arSession, cameraPose, poseRaw, 7);
   ```
