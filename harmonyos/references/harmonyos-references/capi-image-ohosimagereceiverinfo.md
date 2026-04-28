---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagereceiverinfo
title: OhosImageReceiverInfo
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageReceiverInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:13:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b76c087860c53ce47522adcfdf24252167f16b7d7050d1634a6c150c04872be6
---

```
1. struct OhosImageReceiverInfo {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义ImageReceiver的相关信息。

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_receiver\_mdk.h](capi-image-receiver-mdk-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t width | 消费端接收图片时的默认图像宽度，用pixels表示。 |
| int32\_t height | 消费端接收图片时的默认图像高度，用pixels表示。 |
| int32\_t format | 通过接收器创建图像格式OHOS\_IMAGE\_FORMAT\_JPEG。 |
| int32\_t capicity | 图片缓存数量的最大值。该参数仅作为期望值，实际capacity由设备硬件决定。 |
