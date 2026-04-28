---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/audiosuite-oh-audiosuite-spacerenderrotationparams
title: OH_AudioSuite_SpaceRenderRotationParams
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioSuite_SpaceRenderRotationParams
category: harmonyos-references
scraped_at: 2026-04-28T08:11:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:104dec0450fe11ed4e898ed7b6e1c2caa663581fd6c1e1ced84995316e109bdb
---

```
1. typedef struct {...} OH_AudioSuite_SpaceRenderRotationParams
```

## 概述

PhonePC/2in1Tablet

定义空间渲染效果节点旋转模式配置参数。

**起始版本：** 23

**相关模块：** [OHAudioSuite](capi-ohaudiosuite.md)

**所在头文件：** [native\_audio\_suite\_base.h](capi-native-audio-suite-base-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| float x | 空间中的X坐标。取值范围为[-5.0, 5.0]，单位为米。 |
| float y | 空间中的Y坐标。取值范围为[-5.0, 5.0]，单位为米。 |
| float z | 空间中的Z坐标。取值范围为[-5.0, 5.0]，单位为米。 |
| int32\_t surroundTime | 单周环绕时间。取值范围为[2, 40]，单位为秒。 |
| [OH\_AudioSuite\_SurroundDirection](capi-native-audio-suite-base-h.md#oh_audiosuite_surrounddirection) surroundDirection | 单周环绕方向。取值范围为[0, 1]。 |
