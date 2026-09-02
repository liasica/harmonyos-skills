---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-semantics
title: 识别平面语义（C/C++）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 平面语义 > 识别平面语义（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:19+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:30d4a76780312342a885bccd6f5b25b1ab30a445e88c174aaae3dd0088961e40
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/harmonyos_samples/arengine_-sample-code_-clientdemo_cpp)。

## 约束与限制

从5.0.0(12)开始，识别平面语义能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持平面语义及物体语义特性（[ARENGINE\_FEATURE\_TYPE\_SEMANTIC](../harmonyos-references/arengine-capi-arengine.md#arengine_featuretype)）。

## 引入AR Engine

开发者可参考管理AR会话章节的[引入AR Engine](arengine-c-arsession.md#引入ar-engine)。

## 创建AR会话

创建AR会话并配置为平面语义识别模式。

```
CHECK(HMS_AREngine_ARSession_Create(nullptr, nullptr, &mArSession));

AREngine_ARConfig *arConfig = nullptr;
CHECK(HMS_AREngine_ARConfig_Create(mArSession, &arConfig));
// ...
SetSemanticDenseMode(params.semanticDenseMode, mArSession, arConfig);
AREngine_ARSemanticDenseMode outSemanticDenseMode = ARENGINE_SEMANTIC_DENSE_MODE_DISABLED;
HMS_AREngine_ARConfig_GetSemanticDenseMode(mArSession, arConfig, &outSemanticDenseMode);
CHECK(HMS_AREngine_ARSession_Configure(mArSession, arConfig));
```

## 检测环境中的平面

进行平面语义识别之前，需要先检测环境中的平面。开发者可以参考[检测环境中的平面](arengine-c-get-plane.md)完成平面检测过程，并获取环境中的平面数量。当存在平面时，就可以继续下面的步骤。

## 初始化平面语义标签

创建并初始化平面语义标签label，用于描述平面的语义。

```cpp
AREngine_ARSemanticPlaneLabel planeLabel = ARENGINE_PLANE_UNKNOWN;
```

平面语义标签定义为枚举类型，包括12种枚举值（1种未知类型+11种平面类型）。 参考[AREngine\_ARSemanticPlaneLabel](../harmonyos-references/arengine-capi-arengine.md#arengine_arsemanticplanelabel)

## 识别平面类型

调用[HMS\_AREngine\_ARPlane\_GetLabel](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arplane_getlabel)函数，获取平面类型，结果存放在label中。平面的获取可以参考[获取平面实例](arengine-c-get-plane.md#获取平面实例)。

```cpp
HMS_AREngine_ARPlane_GetLabel(arSession, arPlane, &planeLabel);
```
