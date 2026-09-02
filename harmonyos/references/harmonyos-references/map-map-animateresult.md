---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-animateresult
title: Interface (AnimateResult)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Interface (AnimateResult)
category: harmonyos-references
scraped_at: 2026-09-02T14:53:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f99c68f917998197e460ab88d4afc951f4e212b2a6a61c83e36f8d5ebc936fef
---

## AnimateResult

动画结果类。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| isFinished | boolean | 否 | 是 | 动画是否结束。  - true：已结束  - false：未结束 |
| isCanceled | boolean | 否 | 是 | 动画是否取消。  - true：已取消  - false：未取消 |
