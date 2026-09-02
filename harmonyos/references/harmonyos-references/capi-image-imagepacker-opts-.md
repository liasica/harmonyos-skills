---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagepacker-opts-
title: ImagePacker_Opts_
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > ImagePacker_Opts_
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bcb8c0b016d5f03b6108ef2d0f7a65f06d298be67afe5941b3a40f68c94463ff
---

```c
struct ImagePacker_Opts_ {...}
```

## 概述

定义图像编码选项信息。

**起始版本：** 11

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_packer\_mdk.h](capi-image-packer-mdk-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char\* format | 编码格式。 |
| int quality | 编码质量。 |
