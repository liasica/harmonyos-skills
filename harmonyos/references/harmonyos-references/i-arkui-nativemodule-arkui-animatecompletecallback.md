---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-nativemodule-arkui-animatecompletecallback
title: ArkUI_AnimateCompleteCallback
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_AnimateCompleteCallback
category: harmonyos-references
scraped_at: 2026-04-28T08:04:02+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:84ec7c2ef208a9e2b2ba3f20cc0baa9088b92d84008b200753a3359469319691
---

```
1. typedef struct {...} ArkUI_AnimateCompleteCallback
```

## 概述

PhonePC/2in1TabletTVWearable

动画播放结束回调类型。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_animate.h](capi-native-animate-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_FinishCallbackType](capi-native-type-h.md#arkui_finishcallbacktype) type | 在动画中定义结束回调的类型。 |
| void\* userData | 用于动画结束回调，传递用户自定义数据。 |

### 成员函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [void (\*callback)(void\* userData)](i-arkui-nativemodule-arkui-animatecompletecallback.md#callback) | 动画播放结束回调。 |

## 成员函数说明

PhonePC/2in1TabletTVWearable

### callback()

PhonePC/2in1TabletTVWearable

```
1. void (*callback)(void* userData)
```

**描述：**

动画播放结束回调。
