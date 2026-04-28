---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-plane-shape
title: 识别目标形状（C/C++）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 物体语义 > 识别目标形状（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:53+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:a7e985335f6e8bf664f281b027facab7d6d127a8790cb53ecd05b58c6de04d32
---

## 约束与限制

识别目标形状能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_SEMANTIC](../harmonyos-references/arengine-capi-arengine.md#arengine_featuretype)）。

## 引入AR Engine

开发者可参考管理AR会话章节的[引入AR Engine](arengine-c-arsession.md#引入ar-engine)。

## 创建AR会话

创建AR会话并配置为目标形状识别模式。

```
1. AREngine_ARSession *arSession = nullptr;
2. // 创建AR会话。
3. HMS_AREngine_ARSession_Create(nullptr, nullptr, &arSession);
4. AREngine_ARConfig *arConfig = nullptr;
5. // 创建AR会话配置器。
6. HMS_AREngine_ARConfig_Create(arSession, &arConfig);
7. // 设置语义识别模式为目标形状识别。
8. HMS_AREngine_ARConfig_SetSemanticMode(arSession, arConfig, ARENGINE_SEMANTIC_MODE_TARGET);
9. // 配置器设置给AR会话。
10. HMS_AREngine_ARSession_Configure(arSession, arConfig);
```

## 创建可跟踪对象列表

创建一个可跟踪对象列表targetList，用于存放AR Engine运行过程中检测到的所有可跟踪对象。

```
1. AREngine_ARTrackableList *targetList = nullptr;
2. HMS_AREngine_ARTrackableList_Create(arSession, &targetList);
```

## 获取当前环境中的可跟踪对象

调用[HMS\_AREngine\_ARSession\_GetAllTrackables](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_getalltrackables)函数，检测当前环境中的所有可跟踪对象，并将结果存放在targetList中。

```
1. HMS_AREngine_ARSession_GetAllTrackables(arSession, ARENGINE_TRACKABLE_TARGET, targetList);
```

## 获取可跟踪对象数量

调用[HMS\_AREngine\_ARTrackableList\_GetSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_artrackablelist_getsize)函数获取当前可跟踪对象数量，结果存放在targetSize中。

```
1. int32_t targetSize = 0;
2. HMS_AREngine_ARTrackableList_GetSize(arSession, targetList, &targetSize);
```

当targetSize等于0时，代表当前环境中无可跟踪对象。

当targetSize等于1时，代表当前环境中仅存在1个可跟踪对象。

当targetSize大于1时，代表当前环境中存在多个可跟踪对象。

## 遍历并识别物体形状

1. 当环境中存在一个或多个可跟踪对象时，依次遍历targetList中所有可跟踪对象进行目标形状识别。

   ```
   1. for (int i = 0; i < targetSize; ++i) {
   2. // 遍历可跟踪对象，进行形状识别。
   3. }
   ```
2. 对于第i个对象，创建并获取对象实例。

   ```
   1. AREngine_ARTrackable *target = nullptr;
   2. HMS_AREngine_ARTrackableList_AcquireItem(arSession, targetList, i, &target);
   ```
3. 获取该实例跟踪状态，仅当跟踪状态为[ARENGINE\_TRACKING\_STATE\_TRACKING](../harmonyos-references/arengine-capi-arengine.md#arengine_artrackingstate)时，才可进行形状识别。

   ```
   1. AREngine_ARTrackingState outTrackingState;
   2. HMS_AREngine_ARTrackable_GetTrackingState(arSession, target, &outTrackingState);

   4. if (AREngine_ARTrackingState::ARENGINE_TRACKING_STATE_TRACKING != outTrackingState) {
   5. continue;
   6. }
   ```
4. 获取该实例目标形状，识别结果存放在label中。

   ```
   1. AREngine_ARTargetShapeLabel label = ARENGINE_TARGET_SHAPE_UNKNOWN;
   2. HMS_AREngine_ARTarget_GetShapeType(arSession, reinterpret_cast<AREngine_ARTarget *>(target), &label);
   ```

   其中，[AREngine\_ARTargetShapeLabel](../harmonyos-references/arengine-capi-arengine.md#arengine_artargetshapelabel)为枚举类型，描述了目标物体形状。

## 销毁可跟踪对象列表

```
1. HMS_AREngine_ARTrackableList_Destroy(targetList);
```
