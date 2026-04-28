---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip
title: AIP
breadcrumb: API参考 > 应用框架 > Data Augmentation Kit（数据增强服务） > C API > 模块 > AIP
category: harmonyos-references
scraped_at: 2026-04-28T08:05:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:593299b2d7420996c2c550496d2258fc7751b9816a49633bc498ed4ed493c7b6
---

## 概述

PhonePC/2in1Tablet

智慧化数据平台（AIP）为应用提供构建端侧智慧化解决方案，提供向量化、知识检索和知识问答的能力。

**起始版本：** 6.0.0(20)

## 汇总

PhonePC/2in1Tablet

### 文件

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [aip\_error\_code.h](dataaugmentation-aip-error-code.md) | 描述错误码信息。 |

### 类型定义

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| typedef enum [OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1) [OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1) | 错误码。 |

### 枚举

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1) {  AIP\_OK = 0,  AIP\_E\_EXEC\_ERR = 1021200005,  AIP\_E\_OUT\_OF\_RANGE = 1021200006,  AIP\_E\_NO\_SUCH\_FIELD = 1021200007,  AIP\_E\_OVER\_LIMIT = 1021200008,  AIP\_E\_CONDITION\_OVER\_LIMIT = 1021200009,  AIP\_E\_INVALID\_ARGS = 1021200010,  AIP\_E\_EMBEDDING\_ERR = 1021200012  } | 错误码信息。 |

## 类型定义说明

PhonePC/2in1Tablet

### OH\_Aip\_ErrCode

PhonePC/2in1Tablet

```
1. typedef enum OH_Aip_ErrCode OH_Aip_ErrCode;
```

**描述**

错误码信息。

**起始版本：** 6.0.0(20)

## 枚举类型说明

PhonePC/2in1Tablet

### OH\_Aip\_ErrCode

PhonePC/2in1Tablet

```
1. enum OH_Aip_ErrCode;
```

**描述**

错误码信息。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| AIP\_OK | 操作成功。 |
| AIP\_E\_EXEC\_ERR | 执行报错。 |
| AIP\_E\_OUT\_OF\_RANGE | 下标越界。 |
| AIP\_E\_NO\_SUCH\_FIELD | 不存在该字段。 |
| AIP\_E\_OVER\_LIMIT | 数组超过最大长度512字节。 |
| AIP\_E\_CONDITION\_OVER\_LIMIT | 条件数量超过上限1。 |
| AIP\_E\_INVALID\_ARGS | 无效参数。 |
| AIP\_E\_EMBEDDING\_ERR | 无法生成嵌入向量。 |
