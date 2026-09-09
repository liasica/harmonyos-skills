---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-audiodataarray
title: OH_AudioDataArray
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioDataArray
category: harmonyos-references
scraped_at: 2026-09-10T06:28:06+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:9a187211f5e0f9c10f4d8cd7bd9a224a39cc2e2b170e22d83cfadde1a8b2861f
---

```c
typedef struct OH_AudioDataArray {...} OH_AudioDataArray
```

## 概述

定义多路输出渲染接口的输出数据描述。当管线中存在多输出效果节点时，通过多输出渲染接口获取处理过后的音频数据。

**起始版本：** 22

**相关模块：** [OHAudioSuite](capi-ohaudiosuite.md)

**所在头文件：** [native\_audio\_suite\_base.h](capi-native-audio-suite-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| void \*\*audioDataArray | 输出的音频数据地址。 |
| int32\_t arraySize | 音频数据audioDataArray数组的元素个数。 |
| int32\_t requestFrameSize | audioDataArray数组中每个地址指向的内存大小，单位为字节（Byte）。应确保每个地址指向的内存大小均符合requestFrameSize字段定义。 |
