---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi-oh-midiclientstruct
title: OH_MIDIClientStruct
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_MIDIClientStruct
category: harmonyos-references
scraped_at: 2026-09-02T14:52:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d0cfbf51396aaf020acf1f9607b17963286ba2e186cc620e40ec5e7219854ad6
---

```c
typedef struct OH_MIDIClientStruct OH_MIDIClient
```

## 概述

声明MIDI客户端。OH\_MIDIClient用于建立与MIDI服务的连接，是开发者进行MIDI数据收发和设备管理等操作的基础句柄，适用于音乐播放器、MIDI控制器接入、数字音乐创作等需要与MIDI设备通信的场景。

**起始版本：** 24

**相关模块：** [OHMIDI](capi-ohmidi.md)

**所在头文件：** [native\_midi\_base.h](capi-native-midi-base-h.md)
