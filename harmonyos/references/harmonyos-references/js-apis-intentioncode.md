---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-intentioncode
title: "@ohos.multimodalInput.intentionCode (意图事件)"
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > ArkTS API > @ohos.multimodalInput.intentionCode (意图事件)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:08+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2658e3fe627ce96c7fe729c7815e023f03b86a2ad65baf2fa6e713b5099a14f1
---

将键盘输入设备的原始事件映射为归一化交互的意图事件，如键盘上空格键映射后的事件为INTENTION\_SELECT，意图为选中。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```js
import { IntentionCode } from '@kit.InputKit';
```

## IntentionCode

意图事件枚举值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INTENTION\_UNKNOWN | -1 | 未知意图 |
| INTENTION\_UP | 1 | 上 |
| INTENTION\_DOWN | 2 | 下 |
| INTENTION\_LEFT | 3 | 左 |
| INTENTION\_RIGHT | 4 | 右 |
| INTENTION\_SELECT | 5 | 选中 |
| INTENTION\_ESCAPE | 6 | 退出 |
| INTENTION\_BACK | 7 | 返回 |
| INTENTION\_FORWARD | 8 | 前进 |
| INTENTION\_MENU | 9 | 菜单 |
| INTENTION\_PAGE\_UP | 11 | 上一页 |
| INTENTION\_PAGE\_DOWN | 12 | 下一页 |
| INTENTION\_ZOOM\_OUT | 13 | 缩小键 |
| INTENTION\_ZOOM\_IN | 14 | 放大键 |
