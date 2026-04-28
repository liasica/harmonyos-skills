---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourcedelaytimelist
title: OhosImageSourceDelayTimeList
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageSourceDelayTimeList
category: harmonyos-references
scraped_at: 2026-04-28T08:13:36+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:74614caba17d9e5b7b13a8183276d716fc185e8dadedd84a93f9460e4b309365
---

```
1. struct OhosImageSourceDelayTimeList {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义图像源延迟时间列表。由[OH\_ImageSource\_GetDelayTime](capi-image-source-mdk-h.md#oh_imagesource_getdelaytime)获取。

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_source\_mdk.h](capi-image-source-mdk-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t\* delayTimeList | 图像源延迟时间列表头地址。 |
| size\_t size = 0 | 图像源延迟时间列表大小。 |
