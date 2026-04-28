---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-effect-errors-h
title: image_effect_errors.h
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 头文件 > image_effect_errors.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6dd18bee7784ac93d45fb172783d115a9ab62ebc17f5b085ec40f67da9f42f07
---

## 概述

PhonePC/2in1TabletTV

声明图片效果器错误码。

**库：** libimage\_effect.so

**引用文件：** <multimedia/image\_effect/image\_effect\_errors.h>

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**相关模块：** [ImageEffect](capi-imageeffect.md)

## 汇总

PhonePC/2in1TabletTV

### 枚举

PhonePC/2in1TabletTV

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | ImageEffect\_ErrorCode | 效果器错误码。 |

## 枚举类型说明

PhonePC/2in1TabletTV

### ImageEffect\_ErrorCode

PhonePC/2in1TabletTV

```
1. enum ImageEffect_ErrorCode
```

**描述**

效果器错误码。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| EFFECT\_SUCCESS = 0 | 操作成功。 |
| EFFECT\_ERROR\_PERMISSION\_DENIED = 201 | 权限校验失败。 |
| EFFECT\_ERROR\_PARAM\_INVALID = 401 | 参数检查失败。 |
| EFFECT\_BUFFER\_SIZE\_NOT\_MATCH = 29000001 | 输出buffer尺寸不匹配。 |
| EFFECT\_COLOR\_SPACE\_NOT\_MATCH = 29000002 | 输入输出色彩空间不匹配。 |
| EFFECT\_INPUT\_OUTPUT\_NOT\_MATCH = 29000101 | 输入输出配置不一致。比如：输入Surface，输出Pixelmap。 |
| EFFECT\_EFFECT\_NUMBER\_LIMITED = 29000102 | 超出管线最大规格。 |
| EFFECT\_INPUT\_OUTPUT\_NOT\_SUPPORTED = 29000103 | 输入、输出配置不支持。 |
| EFFECT\_ALLOCATE\_MEMORY\_FAILED = 29000104 | 申请内存失败。 |
| EFFECT\_PARAM\_ERROR = 29000121 | 参数值错误。 例如：滤镜无效的参数值。 |
| EFFECT\_KEY\_ERROR = 29000122 | 参数错误。例如：滤镜无效的参数。 |
| EFFECT\_UNKNOWN = 29000199 | 未定义错误。 |
