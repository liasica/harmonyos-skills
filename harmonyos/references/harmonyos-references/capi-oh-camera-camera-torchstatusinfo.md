---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-torchstatusinfo
title: Camera_TorchStatusInfo
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_TorchStatusInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:12:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0a7f7ee77e0515850956aa15c787c8aad979c4e7b95e5f6ea2a62b17660bcc72
---

```
1. typedef struct Camera_TorchStatusInfo {...} Camera_TorchStatusInfo
```

## 概述

PhonePC/2in1TabletTVWearable

手电筒状态信息。

**起始版本：** 12

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| bool isTorchAvailable | 手电筒是否可用，true表示可用，false表示不可用。 |
| bool isTorchActive | 手电筒是否激活，true表示激活，false表示未激活。 |
| float torchLevel | 手电筒亮度等级。取值范围为[0,1]，越靠近1，亮度越大。 |
