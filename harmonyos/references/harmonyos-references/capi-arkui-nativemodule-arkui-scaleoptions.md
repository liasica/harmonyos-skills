---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-scaleoptions
title: ArkUI_ScaleOptions
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_ScaleOptions
category: harmonyos-references
scraped_at: 2026-04-28T08:04:24+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:e55a1d332b6a4e50b7ad7e9e202b06c8d3a74631e992aa98d0a5f13f0c3929ac
---

```
1. typedef struct {...} ArkUI_ScaleOptions
```

## 概述

PhonePC/2in1TabletTVWearable

定义组件转场时的缩放效果对象。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_type.h](capi-native-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| float x | x轴的缩放倍数。x>1时以x轴方向放大，0<x<1时以x轴方向缩小，x=0时表示在x轴方向缩小成0，x=1时表示在x轴方向缩放倍数是1，x<0时沿x轴反向并缩放。 |
| float y | y轴的缩放倍数。y>1时以y轴方向放大，0<y<1时以y轴方向缩小，y=0时表示在y轴方向缩小成0，y=1时表示在y轴方向缩放倍数是1，y<0时沿y轴反向并缩放。 |
| float z | 当前为二维显示，该参数无效。 |
| float centerX | 变换中心点x轴坐标。表示组件变换中心点（即锚点）的x方向坐标，单位为vp。 |
| float centerY | 变换中心点y轴坐标。表示组件变换中心点（即锚点）的y方向坐标，单位为vp。 |
