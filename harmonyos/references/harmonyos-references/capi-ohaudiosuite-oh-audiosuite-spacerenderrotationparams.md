---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-audiosuite-spacerenderrotationparams
title: OH_AudioSuite_SpaceRenderRotationParams
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioSuite_SpaceRenderRotationParams
category: harmonyos-references
scraped_at: 2026-09-02T15:02:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f96a0f7b72d6686600ecbd25ffc2aa91eb43d5031ad6e28683008355539df11f
---

```c
typedef struct {...} OH_AudioSuite_SpaceRenderRotationParams
```

## 概述

定义空间渲染效果节点旋转模式配置参数。

**起始版本：** 23

**相关模块：** [OHAudioSuite](capi-ohaudiosuite.md)

**所在头文件：** [native\_audio\_suite\_base.h](capi-native-audio-suite-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float x | 空间中的X坐标。取值范围为[-5.0, 5.0]，单位为米。 |
| float y | 空间中的Y坐标。取值范围为[-5.0, 5.0]，单位为米。 |
| float z | 空间中的Z坐标。取值范围为[-5.0, 5.0]，单位为米。 |
| int32\_t surroundTime | 单周环绕时间。取值范围为[2, 40]，单位为秒。 |
| [OH\_AudioSuite\_SurroundDirection](capi-native-audio-suite-base-h.md#oh_audiosuite_surrounddirection) surroundDirection | 环绕方向。0表示逆时针旋转，1表示顺时针旋转。 |
