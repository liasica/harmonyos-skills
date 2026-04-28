---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourceupdatedata
title: OhosImageSourceUpdateData
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageSourceUpdateData
category: harmonyos-references
scraped_at: 2026-04-28T08:13:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:619f7911932e6678a74085ae76a1f1d571d0df2c6dbc05789c9d2b8562f39bd2
---

```
1. struct OhosImageSourceUpdateData {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义图像源更新数据选项，由[OH\_ImageSource\_UpdateData](capi-image-source-mdk-h.md#oh_imagesource_updatedata)获取。

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_source\_mdk.h](capi-image-source-mdk-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint8\_t\* buffer = nullptr | 图像源更新数据缓冲区。 |
| size\_t bufferSize = 0 | 图像源更新数据缓冲区大小。 |
| uint32\_t offset = 0 | 图像源更新数据缓冲区的开端。 |
| uint32\_t updateLength = 0 | 图像源更新数据缓冲区的更新数据长度。 |
| int8\_t isCompleted = 0 | 图像源更新数据在此节中完成。 |
