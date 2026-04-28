---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-readstatecode
title: ReadStateCode（播报状态）
breadcrumb: API参考 > AI > Speech Kit（场景化语音服务） > ArkTS API > ReadStateCode（播报状态）
category: harmonyos-references
scraped_at: 2026-04-28T08:19:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:817fe65fb15ab82b8dcbbcb9c07b7d234839bc12cf1b09c39f00aa9bfc9f89cb
---

朗读控件的播报状态枚举类。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { ReadStateCode } from '@kit.SpeechKit';
```

## ReadStateCode

PhonePC/2in1Tablet

播报状态枚举类。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PLAYING | 1 | 播放。 |
| PAUSED | 2 | 暂停。 |
| COMPLETED | 3 | 播放完成。 |
| WAITING | 4 | 未播放/停止。 |
| NOT\_IN\_READ\_LIST | 5 | 未在播放列表。 |
