---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-semantics
title: 识别平面语义（C/C++）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 平面语义 > 识别平面语义（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:52+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:0286b5c26ff6562b0c4ad9142da4305ef4f1a4b19bbabde9329f3f9993afc9c2
---

## 约束与限制

识别平面语义能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_SEMANTIC](../harmonyos-references/arengine-capi-arengine.md#arengine_featuretype)）。

## 引入AR Engine

开发者可参考管理AR会话章节的[引入AR Engine](arengine-c-arsession.md#引入ar-engine)。

## 创建AR会话

创建AR会话并配置为平面语义识别模式。

```
1. AREngine_ARSession *arSession = nullptr;
2. // 创建AR会话。
3. HMS_AREngine_ARSession_Create(nullptr, nullptr, &arSession);
4. AREngine_ARConfig *arConfig = nullptr;
5. // 创建AR会话配置器。
6. HMS_AREngine_ARConfig_Create(arSession, &arConfig);
7. // 设置语义识别模式为平面语义识别。
8. HMS_AREngine_ARConfig_SetSemanticMode(arSession, arConfig, ARENGINE_SEMANTIC_MODE_PLANE);
9. // 配置器设置给AR会话。
10. HMS_AREngine_ARSession_Configure(arSession, arConfig);
```

## 检测环境中的平面

进行平面语义识别之前，需要先检测环境中的平面。开发者可以参考[检测环境中的平面](arengine-c-get-plane.md)完成平面检测过程，并获取环境中的平面数量。当存在平面时，就可以继续下面的步骤。

## 初始化平面语义标签

创建并初始化平面语义标签label，用于描述平面的语义。

```
1. AREngine_ARSemanticPlaneLabel label = ARENGINE_PLANE_UNKNOWN;
```

平面语义标签定义为枚举类型，包括12种枚举值（1种未知类型+11种平面类型）。

```
1. typedef enum {
2. /** Unknown type. */
3. ARENGINE_PLANE_UNKNOWN = 0,
4. /** Wall. */
5. ARENGINE_PLANE_WALL = 1,
6. /** Floor. */
7. ARENGINE_PLANE_FLOOR = 2,
8. /** Seat. */
9. ARENGINE_PLANE_SEAT = 3,
10. /** Table. */
11. ARENGINE_PLANE_TABLE = 4,
12. /** Ceiling. */
13. ARENGINE_PLANE_CEILING = 5,
14. /** Door. */
15. ARENGINE_PLANE_DOOR = 6,
16. /** Window. */
17. ARENGINE_PLANE_WINDOW = 7,
18. /** Bed. */
19. ARENGINE_PLANE_BED = 8,
20. /** Plane Space. */
21. ARENGINE_PLANE_SPACE = 9,
22. /** Cube Volume. */
23. ARENGINE_CUBE_VOLUME = 10,
24. /** Cube Space. */
25. ARENGINE_CUBE_SPACE = 11,
26. } AREngine_ARSemanticPlaneLabel;
```

## 识别平面类型

调用[HMS\_AREngine\_ARPlane\_GetLabel](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arplane_getlabel)函数，获取平面类型，结果存放在label中。平面的获取可以参考[获取平面实例](arengine-c-get-plane.md#获取平面实例)。

```
1. HMS_AREngine_ARPlane_GetLabel(arSession, arPlane, &label);
```
