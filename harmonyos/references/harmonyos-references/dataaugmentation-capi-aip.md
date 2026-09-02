---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip
title: AIP
breadcrumb: API参考 > 应用框架 > Data Augmentation Kit（数据增强服务） > C API > 模块 > AIP
category: harmonyos-references
scraped_at: 2026-09-02T15:01:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d05bd0740d76bd78e7a48ea92fe553442e030735354bcb158a3499306da62d6d
---

## 概述

智慧化数据平台（AIP）为应用提供构建端侧智慧化解决方案，提供向量化、知识检索和知识问答的能力。

**起始版本：** 6.0.0(20)

**使用前提：** 使用该模块前，需确认设备系统版本不低于6.0.0(20)，并确保设备支持端侧AI计算能力。

## 汇总

### 文件

| 名称 | 描述 |
| --- | --- |
| [aip\_error\_code.h](dataaugmentation-aip-error-code.md) | 描述错误码信息。 |

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef enum [OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1) [OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1) | 错误码。 |

### 枚举

| 名称 | 描述 |
| --- | --- |
| [OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1) {  AIP\_OK = 0,  AIP\_E\_EXEC\_ERR = 1021200005,  AIP\_E\_OUT\_OF\_RANGE = 1021200006,  AIP\_E\_NO\_SUCH\_FIELD = 1021200007,  AIP\_E\_OVER\_LIMIT = 1021200008,  AIP\_E\_CONDITION\_OVER\_LIMIT = 1021200009,  AIP\_E\_INVALID\_ARGS = 1021200010,  AIP\_E\_EMBEDDING\_ERR = 1021200012  } | 错误码信息。 |

## 类型定义说明

### OH\_Aip\_ErrCode

```c
typedef enum OH_Aip_ErrCode OH_Aip_ErrCode;
```

**描述**

错误码信息。

**起始版本：** 6.0.0(20)

## 枚举类型说明

### OH\_Aip\_ErrCode

```c
enum OH_Aip_ErrCode;
```

**描述**

错误码信息。

**起始版本：** 6.0.0(20)

| 枚举项 | 描述 |
| --- | --- |
| AIP\_OK = 0 | 操作成功。 |
| AIP\_E\_EXEC\_ERR = 1021200005 | 执行报错。执行过程中发生内部运行异常时返回。 |
| AIP\_E\_OUT\_OF\_RANGE = 1021200006 | 下标越界。输入参数超出允许范围时返回，例如索引超出数组长度。 |
| AIP\_E\_NO\_SUCH\_FIELD = 1021200007 | 不存在该字段。请求的字段名在当前记录中未找到时返回。 |
| AIP\_E\_OVER\_LIMIT = 1021200008 | 数组超过最大长度512字节。数组长度超出限制时返回。 |
| AIP\_E\_CONDITION\_OVER\_LIMIT = 1021200009 | 条件数量超过上限1。检索条件数量超过上限时返回。 |
| AIP\_E\_INVALID\_ARGS = 1021200010 | 无效参数。传入空指针或参数类型不匹配时返回。 |
| AIP\_E\_EMBEDDING\_ERR = 1021200012 | 无法生成嵌入向量。模型加载失败或输入内容不支持向量化时返回。 |
