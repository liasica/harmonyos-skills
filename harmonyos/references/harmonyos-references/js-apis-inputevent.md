---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputevent
title: "@ohos.multimodalInput.inputEvent (输入事件)"
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > ArkTS API > @ohos.multimodalInput.inputEvent (输入事件)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:11a5a9b5a48d4666c7d5ec01201053011e918e10b3e1b8fe2097ed64cfede976
---

设备上报的基本事件。

**说明** 

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```js
import { InputEvent } from '@kit.InputKit';
```

## InputEvent

输入事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 否 | 否 | 事件ID。 |
| deviceId | number | 否 | 否 | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |
| actionTime | number | 否 | 否 | 上报输入事件的时间，表示系统启动运行至今逝去的微秒数，单位为微秒（μs）。 |
| screenId | number | 否 | 否 | 目标屏幕ID。 |
| windowId | number | 否 | 否 | 目标窗口ID。 |
