---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-avplayercallback
title: AVPlayerCallback
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > AVPlayerCallback
category: harmonyos-references
scraped_at: 2026-09-02T15:02:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6d9607d73c1369f830e0964898aeb1a780d1d67b80dbb803842950d693ee100c
---

```c
typedef struct AVPlayerCallback {...} AVPlayerCallback
```

## 概述

AVPlayerCallback是AVPlayer的回调管理结构体，包含了播放过程信息OH\_AVPlayerOnInfo和错误信息OH\_AVPlayerOnError的回调函数指针。应用需注册此实例结构体到OH\_AVPlayer实例中，并对回调上报的信息进行处理，保证AVPlayer的正常运行。通过注册这些回调，开发者可以实时监控AVPlayer的播放状态、获取播放过程信息（如缓冲进度、播放位置等）和错误事件，及时响应和处理播放过程中的各种事件，适用于需要对播放流程进行细粒度控制（Fine-grained Control）和监控的场景。

**起始版本：** 11

**废弃版本：** 12

**替代接口：** [OH\_AVPlayerOnInfoCallback](capi-avplayer-base-h.md#oh_avplayeroninfocallback)或[OH\_AVPlayerOnErrorCallback](capi-avplayer-base-h.md#oh_avplayeronerrorcallback)。

**相关模块：** [AVPlayer](capi-avplayer.md)

**所在头文件：** [avplayer\_base.h](capi-avplayer-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| OH\_AVPlayerOnInfo onInfo | 监控AVPlayer过程信息，需注册此回调到AVPlayer实例中使用，详细内容参考[OH\_AVPlayerOnInfo](capi-avplayer-base-h.md#oh_avplayeroninfo)。  **起始版本：** 11  **废弃版本：** 12  **替代接口：** [OH\_AVPlayerOnInfoCallback](capi-avplayer-base-h.md#oh_avplayeroninfocallback) |
| OH\_AVPlayerOnError onError | 监控AVPlayer操作错误，需注册此回调到AVPlayer实例中使用。回调签名为OH\_AVPlayerOnError。回调参数信息请参考[OH\_AVPlayerOnError](capi-avplayer-base-h.md#oh_avplayeronerror)。  **起始版本：** 11  **废弃版本：** 12  **替代接口：** [OH\_AVPlayerOnErrorCallback](capi-avplayer-base-h.md#oh_avplayeronerrorcallback) |
