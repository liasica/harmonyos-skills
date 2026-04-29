---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-blanklessinfo
title: ArkWeb_BlanklessInfo
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_BlanklessInfo
category: harmonyos-references
scraped_at: 2026-04-29T13:55:56+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:ae35279b208d00d4096624c4340f0c77c7f3fcb00bad0f0e29774a9a6a6598f9
---

```
1. typedef struct {...} ArkWeb_BlanklessInfo
```

## 概述

PhonePC/2in1TabletTVWearable

页面首屏加载预测信息，主要包括首屏相似度预测值，首屏加载耗时预测值，错误码，应用需根据此信息来决策是否启用无白屏加载插帧方案。

**起始版本：** 20

**相关模块：** [Web](capi-web.md)

**所在头文件：** [native\_interface\_arkweb.h](capi-native-interface-arkweb-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| ArkWeb\_BlanklessErrorCode errCode | 无白屏加载的错误码，见[ArkWeb\_BlanklessErrorCode](capi-arkweb-error-code-h.md#arkweb_blanklesserrorcode)定义。 |
| double similarity | 首屏相似度，根据历史加载首屏内容计算相似度，范围为0~1.0，1.0表示完全一致，数值越接近1，相似度越高。该值存在滞后性，本地加载的相似度将在下次加载时才可反映。建议当相似度较低时，应用不启用无白屏加载插帧方案。 |
| int32\_t loadingTime | 根据历史加载首屏耗时预测本次加载耗时，单位ms，取值范围需大于0。 |
