---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-image-string
title: Image_String
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > Image_String
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d2bdc71c593af99a09cfa7878646f3eda47bf769d12f1f1d388738e5ac4793b8
---

```c
struct Image_String {...}
typedef struct Image_String Image_MimeType
typedef struct Image_String Image_String
```

## 概述

字符串结构，用于描述字符串数据地址和数据长度。Image\_MimeType是Image\_String的别名，用于表示MIME类型。

作为输入参数使用时，调用方负责保证data和size有效；作为输出参数使用时，data的分配和释放方式以具体接口说明为准。

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_common.h](capi-image-common-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \*data = nullptr | 指向字符串数据首地址的指针。 |
| size\_t size = 0 | 字符串数据长度。 |
