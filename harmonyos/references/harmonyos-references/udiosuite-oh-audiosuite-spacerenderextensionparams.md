---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/udiosuite-oh-audiosuite-spacerenderextensionparams
title: OH_AudioSuite_SpaceRenderExtensionParams
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioSuite_SpaceRenderExtensionParams
category: harmonyos-references
scraped_at: 2026-04-28T08:11:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7e0c38bbc385dcf6be68d5008aa10d9d94da17cbb2fb438d779934e4388e3c65
---

```
1. struct OH_AudioSuite_SpaceRenderExtensionParams {...}
```

## 概述

PhonePC/2in1Tablet

定义空间渲染效果节点扩展模式配置参数。

**起始版本：** 23

**相关模块：** [OHAudioSuite](capi-ohaudiosuite.md)

**所在头文件：** [native\_audio\_suite\_base.h](capi-native-audio-suite-base-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| float extRadius | 扩展半径。取值范围为[1.0, 5.0]，单位为米。 |
| int32\_t extAngle | 扩展角度。取值范围为(0, 360)，单位为度。 |
