---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-struct-araugmentedimagesource
title: AREngine_ARAugmentedImageSource
breadcrumb: API参考 > 图形 > AR Engine（AR引擎服务） > C API > 头文件和结构体 > 结构体 > AREngine_ARAugmentedImageSource
category: harmonyos-references
scraped_at: 2026-09-02T15:02:40+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:99cc973da27c5d00761f99c7f5e4e07947a9cb3926e036d7a95ca9986c7f1d23
---

## 概述

图像数据。

**起始版本：** 5.1.0(18)

**相关模块：** [AR Engine](arengine-capi-arengine.md)

**所在头文件：** [ar\_engine\_core.h](arengine-header-file.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char \*[imageName](arengine-struct-araugmentedimagesource.md#imagename) | 图像名，不允许为空，255个字符以内，超过255个字符的部分将被自动截断。 |
| const uint8\_t \*[imageData](arengine-struct-araugmentedimagesource.md#imagedata) | 灰度图像元素数组地址。 |
| int32\_t [pixelWidth](arengine-struct-araugmentedimagesource.md#pixelwidth) | 图像像素宽度。 |
| int32\_t [pixelHeight](arengine-struct-araugmentedimagesource.md#pixelheight) | 图像像素高度。 |
| int32\_t [stride](arengine-struct-araugmentedimagesource.md#stride) | 图像步幅。 |
| float [realWidthInMeters](arengine-struct-araugmentedimagesource.md#realwidthinmeters) | 图像中对象的实际物理宽度。无限制，默认值为A4纸张尺寸。 |

## 结构体成员变量说明

### imageName

```cpp
const char* AREngine_ARAugmentedImageSource::imageName
```

**描述**

图像名，不允许为空，255个字符以内，超过255个字符的部分将被自动截断。

### imageData

```cpp
const uint8_t* AREngine_ARAugmentedImageSource::imageData
```

**描述**

灰度图像元素数组地址。

### pixelWidth

```cpp
int32_t AREngine_ARAugmentedImageSource::pixelWidth
```

**描述**

图像像素宽度。

### pixelHeight

```cpp
int32_t AREngine_ARAugmentedImageSource::pixelHeight
```

**描述**

图像像素高度。

### stride

```cpp
int32_t AREngine_ARAugmentedImageSource::stride
```

**描述**

图像步幅。

### realWidthInMeters

```cpp
float AREngine_ARAugmentedImageSource::realWidthInMeters
```

**描述**

图像中对象的实际物理宽度。无限制，默认值为291mm。
