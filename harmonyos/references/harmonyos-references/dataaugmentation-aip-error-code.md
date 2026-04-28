---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-aip-error-code
title: aip_error_code.h
breadcrumb: API参考 > 应用框架 > Data Augmentation Kit（数据增强服务） > C API > 头文件和结构体 > aip_error_code.h
category: harmonyos-references
scraped_at: 2026-04-28T08:05:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6dbe8cbb77375144773eb038911ae81155b41fe13464e46b18623216ecc7c78b
---

## 概述

提供与错误代码相关的接口。

**引用文件：** #include "dataaugmentation/aip\_error\_code.h"

**库：** libretrieval\_ndk.so

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

**相关模块：** [AIP](dataaugmentation-capi-aip.md)

## 汇总

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef enum [OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1) [OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1) | 错误码信息。 |

### 枚举

| 名称 | 描述 |
| --- | --- |
| OH\_Aip\_ErrCode {  AIP\_OK = 0,  AIP\_E\_EXEC\_ERR = 1021200005,  AIP\_E\_OUT\_OF\_RANGE = 1021200006,  AIP\_E\_NO\_SUCH\_FIELD = 1021200007,  AIP\_E\_OVER\_LIMIT = 1021200008,  AIP\_E\_CONDITION\_OVER\_LIMIT = 1021200009,  AIP\_E\_INVALID\_ARGS = 1021200010,  AIP\_E\_EMBEDDING\_ERR = 1021200012  } | 错误码信息。 |
