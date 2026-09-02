---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-preferences-err-code-h
title: oh_preferences_err_code.h
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 头文件 > oh_preferences_err_code.h
category: harmonyos-references
scraped_at: 2026-09-02T15:00:42+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c3f4b2a9e207375d6744da3b40c576c6e55cfc708fbef0b68fe75bec21daf35b
---

## 概述

声明首选项模块统一使用的错误码信息。

**引用文件：** <database/preferences/oh\_preferences\_err\_code.h>

**库：** libohpreferences.so

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 13

**相关模块：** [Preferences](capi-preferences.md)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Preferences\_ErrCode](capi-oh-preferences-err-code-h.md#oh_preferences_errcode) | OH\_Preferences\_ErrCode | 错误码信息。 |

## 枚举类型说明

### OH\_Preferences\_ErrCode

```c
enum OH_Preferences_ErrCode
```

**描述**

错误码信息。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| PREFERENCES\_OK = 0 | 操作执行成功。 |
| PREFERENCES\_ERROR\_INVALID\_PARAM = 401 | 参数不合法。 |
| PREFERENCES\_ERROR\_NOT\_SUPPORTED = 801 | 系统能力不支持。 |
| PREFERENCES\_ERROR\_BASE = 15500000 | 基准错误码。 |
| PREFERENCES\_ERROR\_DELETE\_FILE = 15500010 | 删除文件失败。 |
| PREFERENCES\_ERROR\_STORAGE = 15500011 | 存储异常。 |
| PREFERENCES\_ERROR\_MALLOC = 15500012 | 申请内存失败。 |
| PREFERENCES\_ERROR\_KEY\_NOT\_FOUND = 15500013 | Key不存在。 |
| PREFERENCES\_ERROR\_GET\_DATAOBSMGRCLIENT = 15500019 | 获取数据变更订阅服务失败。 |
