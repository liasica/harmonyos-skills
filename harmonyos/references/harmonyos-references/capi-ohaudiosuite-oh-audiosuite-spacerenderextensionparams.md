---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-audiosuite-spacerenderextensionparams
title: OH_AudioSuite_SpaceRenderExtensionParams
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioSuite_SpaceRenderExtensionParams
category: harmonyos-references
scraped_at: 2026-09-02T15:02:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8d264fcaa2b4b409aef6580517e4024f18df7e93e31f1760ad4986e5d9c55f1d
---

```c
struct OH_AudioSuite_SpaceRenderExtensionParams {...}
```

## 概述

定义空间渲染效果节点扩展模式配置参数。

**起始版本：** 23

**相关模块：** [OHAudioSuite](capi-ohaudiosuite.md)

**所在头文件：** [native\_audio\_suite\_base.h](capi-native-audio-suite-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float extRadius | 扩展半径，表示声音源的空间扩散范围。取值越大，声音的空间扩散范围越宽广。取值范围为[1.0, 5.0]，单位为米（m）。 |
| int32\_t extAngle | 扩展角度，表示声音源在水平面上的扩散角度范围。取值越大，声音的扩散角度越宽。取值范围为(0, 360)，单位为度（°）。 |
