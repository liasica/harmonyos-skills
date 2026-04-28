---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-faq-1
title: 获取检测平面的二维顶点数组时报错：“plane is nullptr!”，返回错误码：401
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > AR Engine常见问题 > 获取检测平面的二维顶点数组时报错：“plane is nullptr!”，返回错误码：401
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:73d2ddf8b1263dcd150258635edbdfaeea8e6bb71e72fc2dc4fa9cdbe83814e6
---

## 现象描述

调用[HMS\_AREngine\_ARPlane\_GetPolygonSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arplane_getpolygonsize)获取检测到平面的二维顶点数组大小时报错：“plane is nullptr!”，返回错误码：401。

## 可能原因

初次打开应用还未识别到平面，调用[HMS\_AREngine\_ARSession\_GetAllTrackables](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_getalltrackables)获取的可跟踪对象列表为空，导致后续[HMS\_AREngine\_ARTrackableList\_AcquireItem](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_artrackablelist_acquireitem)获取对应索引的对象也为空，使用前未做有效性判断，使用时出现无效参数错误。

## 处理步骤

开发者从AR Engine获取平面之后需判断其有效性后使用，例如，进行非空判断。
