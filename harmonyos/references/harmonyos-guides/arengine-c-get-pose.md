---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-pose
title: 获取设备位姿（C/C++）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 运动跟踪 > 获取设备位姿（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:50+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:8e61cec35ca2276a90304c4ef3337ff08e6c941daba0134aca480247004914e1
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/harmonyos_samples/arengine_-sample-code_-clientdemo_cpp)。

## 约束与限制

获取设备位姿能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_SLAM](../harmonyos-references/arengine-capi-arengine.md#arengine_featuretype)）。

## 创建ARSession

开发者可以参考[管理AR会话](arengine-c-arsession.md)创建ARSession。

## 获取设备当前位姿

1. 创建一个空位姿变量cameraPose。

   ```
   1. AREngine_ARPose *cameraPose = nullptr;
   2. HMS_AREngine_ARPose_Create(arSession, nullptr, 0, &cameraPose);
   ```
2. 获取当前时刻相机位姿信息，并存储在cameraPose变量中。

   ```
   1. // 创建一个新的AREngine_ARFrame对象。
   2. AREngine_ARFrame *arFrame = nullptr;
   3. HMS_AREngine_ARFrame_Create(arSession, &arFrame);
   4. // 更新当前帧的结果到arFrame。
   5. HMS_AREngine_ARSession_Update(arSession, arFrame);
   6. // 获取当前帧的相机参数对象。
   7. AREngine_ARCamera *arCamera = nullptr;
   8. HMS_AREngine_ARFrame_AcquireCamera(arSession, arFrame, &arCamera);
   9. // 获取当前时刻相机位姿信息。
   10. HMS_AREngine_ARCamera_GetPose(arSession, arCamera, cameraPose);
   ```
3. 从cameraPose中获取相机位姿的不同分量，包括平移分量和旋转分量。

   ```
   1. float poseRaw[7] = { 0.0f };
   2. HMS_AREngine_ARPose_GetPoseRaw(arSession, cameraPose, poseRaw, 7);
   ```
