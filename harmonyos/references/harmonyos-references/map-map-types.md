---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-types
title: Types
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Types
category: harmonyos-references
scraped_at: 2026-09-02T14:53:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7916141fcec49a93d7f6909a0a1cec951db7877ecb00b6c8b54f496b1f6fecbe
---

## MassPointOverlayCallback

type MassPointOverlayCallback = (massPointOverlay: MassPointOverlay, massPointItem: mapCommon.MassPointItem) => void

回调函数，无返回结果。用于监听海量点图层的点击事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数**：

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| massPointOverlay | [MassPointOverlay](map-map-masspointoverlay.md) | 是 | 海量点管理对象。 |
| massPointItem | [mapCommon.MassPointItem](map-common.md#masspointitem) | 是 | 海量点项。 |
