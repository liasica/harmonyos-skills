---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-enums
title: Enums
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Enums
category: harmonyos-references
scraped_at: 2026-09-02T14:53:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e8301adc22a6ed7f4d206205b092374b76d97cad963c44f86bd4b20d3e2e6d23
---

## AnimationFillMode

动画执行完成后的状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FORWARDS | 0 | 动画执行后保持在最后一帧。 |
| BACKWARDS | 1 | 动画执行后保持在第一帧。 |

## AnimationRepeatMode

重复执行的模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RESTART | 0 | 动画结束后从头播放，适用于需要循环播放动画的场景。 |
| REVERSE | 1 | 动画结束后从尾倒放，适用于需要反向播放动画的场景。 |
