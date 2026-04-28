---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-plane
title: 检测环境中的平面（C/C++）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 平面识别 > 检测环境中的平面（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:50+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:3cc7f7614386a349330493a8ca6c3c2c1c4947fb56048d8c8c46ad03d945dd66
---

## 概要

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/harmonyos_samples/arengine_-sample-code_-clientdemo_cpp)。

## 约束与限制

检测环境平面能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_SLAM](../harmonyos-references/arengine-capi-arengine.md#arengine_featuretype)）。

## 引入AR Engine

开发者可参考管理AR会话章节的[引入AR Engine](arengine-c-arsession.md#引入ar-engine)。

## 创建ARSession

开发者可以参考[管理AR会话](arengine-c-arsession.md)创建ARSession。

## 创建平面对象列表

1. 创建一个平面对象列表planeList，用于存放AR Engine运行过程中检测到的所有平面。

   ```
   1. AREngine_ARTrackableList *planeList = nullptr;
   2. HMS_AREngine_ARTrackableList_Create(arSession, &planeList);
   ```
2. 设置可跟踪对象类型为ARENGINE\_TRACKABLE\_PLANE。

   ```
   1. AREngine_ARTrackableType planeTrackedType = ARENGINE_TRACKABLE_PLANE;
   ```

## 识别当前环境中的平面

调用[HMS\_AREngine\_ARSession\_GetAllTrackables](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_getalltrackables)函数，检测当前环境中的所有平面，并将结果存放在planeList中。

```
1. HMS_AREngine_ARSession_GetAllTrackables(arSession, planeTrackedType, planeList);
```

## 获取平面数量

调用[HMS\_AREngine\_ARTrackableList\_GetSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_artrackablelist_getsize)函数获取平面数量，结果存放在planeListSize中。

```
1. int32_t planeListSize = 0;
2. HMS_AREngine_ARTrackableList_GetSize(arSession, planeList, &planeListSize);
```

在应用环境中，可能存在0个、1个或多个平面。

当planeListSize等于0时，表示当前环境中不存在平面。

当planeListSize等于1时，表示当前环境中仅存在1个平面。

当planeListSize大于1时，表示当前环境中存在多个平面。

## 获取平面实例

当存在1个或多个平面时，可以依次遍历planeList获取所有平面对象。

```
1. for (int i = 0; i < planeListSize; ++i) {
2. // 遍历所有平面对象，根据您的应用进行处理。
3. }
```

对于第i个平面，创建并获取可跟踪对象，并将其转化为平面对象[AREngine\_ARPlane](../harmonyos-references/arengine-capi-arengine.md#arengine_arplane)。

```
1. AREngine_ARTrackable *arTrackable = nullptr;
2. HMS_AREngine_ARTrackableList_AcquireItem(arSession, planeList, i, &arTrackable);
3. AREngine_ARPlane *arPlane = reinterpret_cast<AREngine_ARPlane*>(arTrackable);
```

说明

AR Engine中，任何物体都被定义为可跟踪对象[AREngine\_ARTrackable](../harmonyos-references/arengine-capi-arengine.md#arengine_artrackable)。平面也是一种可跟踪对象，开发者可以通过类型转换reinterpret\_cast将可跟踪对象[AREngine\_ARTrackable](../harmonyos-references/arengine-capi-arengine.md#arengine_artrackable)转化为平面对象[AREngine\_ARPlane](../harmonyos-references/arengine-capi-arengine.md#arengine_arplane)。

## 销毁平面对象列表

```
1. HMS_AREngine_ARTrackableList_Destroy(planeList);
```
