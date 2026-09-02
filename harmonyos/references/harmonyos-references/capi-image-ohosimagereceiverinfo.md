---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagereceiverinfo
title: OhosImageReceiverInfo
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageReceiverInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:af84060bd702cfef3d3125ea155d0cc2cce7ba4fe44b39da775bd4efab68f1c3
---

```c
struct OhosImageReceiverInfo {...}
```

## 概述

定义ImageReceiver的相关信息。

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_receiver\_mdk.h](capi-image-receiver-mdk-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t width | 消费端接收图片时的默认图像宽度，用pixels表示。 |
| int32\_t height | 消费端接收图片时的默认图像高度，用pixels表示。 |
| int32\_t format | 通过接收器创建图像格式OHOS\_IMAGE\_FORMAT\_JPEG。 |
| int32\_t capicity | 图片缓存数量的最大值。该参数仅作为期望值，实际capacity由设备硬件决定。 |
