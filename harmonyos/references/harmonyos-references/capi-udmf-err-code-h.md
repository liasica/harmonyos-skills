---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-err-code-h
title: udmf_err_code.h
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 头文件 > udmf_err_code.h
category: harmonyos-references
scraped_at: 2026-04-28T07:59:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:91cde7c695e2c048f1655eb9532f7558e369159b2c2e0f67b453f433335f7479
---

## 概述

PhonePC/2in1TabletTV

声明统一数据管理框架错误码信息。

**引用文件：** <database/udmf/udmf\_err\_code.h>

**库：** libudmf.so

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 12

**相关模块：** [UDMF](capi-udmf.md)

## 汇总

PhonePC/2in1TabletTV

### 枚举

PhonePC/2in1TabletTV

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode) | Udmf\_ErrCode | 错误码信息。 |
| [Udmf\_ListenerStatus](capi-udmf-err-code-h.md#udmf_listenerstatus) | Udmf\_ListenerStatus | 异步获取数据时的状态码枚举。 |

## 枚举类型说明

PhonePC/2in1TabletTV

### Udmf\_ErrCode

PhonePC/2in1TabletTV

```
1. enum Udmf_ErrCode
```

**描述**

错误码信息。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| UDMF\_E\_OK = 0 | 执行成功。 |
| UDMF\_ERR = 20400000 | 通用错误码。 |
| UDMF\_E\_INVALID\_PARAM = (UDMF\_ERR + 1) | 非法参数。 |

### Udmf\_ListenerStatus

PhonePC/2in1TabletTV

```
1. enum Udmf_ListenerStatus
```

**描述**

异步获取数据时的状态码枚举。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| UDMF\_FINISHED = 0 | 表示获取数据成功。 |
| UDMF\_PROCESSING | 表示正在处理中。 |
| UDMF\_CANCELED | 表示本次任务已被取消。 |
| UDMF\_INNER\_ERROR = 200 | 表示有内部错误发生。 |
| UDMF\_INVALID\_PARAMETERS | 表示包含无效参数。 |
| UDMF\_DATA\_NOT\_FOUND | 表示没有获取到数据。 |
| UDMF\_SYNC\_FAILED | 表示同步数据过程中出现错误。 |
| UDMF\_COPY\_FILE\_FAILED | 表示文件拷贝过程中出现错误。 |
