---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-audiodataarray
title: OH_AudioDataArray
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioDataArray
category: harmonyos-references
scraped_at: 2026-04-28T08:11:55+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:30a930e436edb43f969bad62f0834ff618f8b729300d1f464b48cc52da4b7d14
---

```
1. typedef struct {...} OH_AudioDataArray
```

## 概述

PhonePC/2in1Tablet

定义多路输出渲染接口的输入数据描述。当管线中存在多输出效果节点时，通过多输出渲染接口获取处理过后的音频数据。

**起始版本：** 22

**相关模块：** [OHAudioSuite](capi-ohaudiosuite.md)

**所在头文件：** [native\_audio\_suite\_base.h](capi-native-audio-suite-base-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| void \*\*audioDataArray | 需要输出的音频数据地址。 |
| int32\_t arraySize | 音频数组大小。 |
| int32\_t requestFrameSize | audioDataArray数组中地址的内存大小（单位为字节），应确保每个地址均具有requestFrameSize字节个大小。 |
