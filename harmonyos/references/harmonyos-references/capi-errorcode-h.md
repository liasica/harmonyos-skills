---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-errorcode-h
title: errorcode.h
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 头文件 > errorcode.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:33+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8abc84e4b23fb5e59581787f2d8289464c49aa96c74bcd5912d8177f813603a6
---

## 概述

PhonePC/2in1TabletTVWearable

提供国际化接口返回的错误码。

**引用文件：** <i18n/errorcode.h>

**库：** libohi18n.so

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**相关模块：** [i18n](capi-i18n.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [I18n\_ErrorCode](capi-errorcode-h.md#i18n_errorcode) | I18n\_ErrorCode | 国际化错误码。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### I18n\_ErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum I18n_ErrorCode
```

**描述**

国际化错误码。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| SUCCESS = 0 | 成功。 |
| ERROR\_INVALID\_PARAMETER = 8900001 | 传入参数无效。 |
| UNEXPECTED\_ERROR = 8900050 | 预期之外的错误，例如内存错误。 |
