---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-avplayercallback
title: AVPlayerCallback
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > AVPlayerCallback
category: harmonyos-references
scraped_at: 2026-04-28T08:13:59+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:14cd04bbb456324bfcdc4366d1d45829cbb2e3b4af352b06f81224e91d44529d
---

```
1. typedef struct AVPlayerCallback {...} AVPlayerCallback
```

## 概述

PhonePC/2in1TabletTVWearable

包含了OH\_AVPlayerOnInfo和OH\_AVPlayerOnError回调函数指针的集合。应用需注册此实例结构体到OH\_AVPlayer实例中，并对回调上报的信息进行处理，保证AVPlayer的正常运行。

**起始版本：** 11

**废弃版本：** 12

**替代接口：** [OH\_AVPlayerOnInfoCallback](capi-avplayer-base-h.md#oh_avplayeroninfocallback) [OH\_AVPlayerOnErrorCallback](capi-avplayer-base-h.md#oh_avplayeronerrorcallback)

**相关模块：** [AVPlayer](capi-avplayer.md)

**所在头文件：** [avplayer\_base.h](capi-avplayer-base-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| OH\_AVPlayerOnInfo onInfo | 监控AVPlayer过程信息，参考[OH\_AVPlayerOnInfo](capi-avplayer-base-h.md#oh_avplayeroninfo)。  **起始版本：** 11  **废弃版本：** 12  **替代接口：** [OH\_AVPlayerOnInfoCallback](capi-avplayer-base-h.md#oh_avplayeroninfocallback) |
| OH\_AVPlayerOnError onError | 监控AVPlayer操作错误，参考[OH\_AVPlayerOnError](capi-avplayer-base-h.md#oh_avplayeronerror)。  **起始版本：** 11  **废弃版本：** 12  **替代接口：** [OH\_AVPlayerOnErrorCallback](capi-avplayer-base-h.md#oh_avplayeronerrorcallback) |
