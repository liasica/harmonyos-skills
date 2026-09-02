---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-aip-error-code
title: aip_error_code.h
breadcrumb: API参考 > 应用框架 > Data Augmentation Kit（数据增强服务） > C API > 头文件 > aip_error_code.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:33+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:4d8aab9618d075d6376d82c8babb0f182a9b14d88e204e299bcbf8e266b7424d
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
| OH\_Aip\_ErrCode {  AIP\_OK = 0,  AIP\_E\_EXEC\_ERR = 1021200005,  AIP\_E\_OUT\_OF\_RANGE = 1021200006,  AIP\_E\_NO\_SUCH\_FIELD = 1021200007,  AIP\_E\_OVER\_LIMIT = 1021200008,  AIP\_E\_CONDITION\_OVER\_LIMIT = 1021200009,  AIP\_E\_INVALID\_ARGS = 1021200010,  AIP\_E\_EMBEDDING\_ERR = 1021200012  } | 错误码信息。各错误码含义如下：  - AIP\_OK：操作成功完成。  - AIP\_E\_EXEC\_ERR：执行过程中发生错误，可能是内部运行异常导致。  - AIP\_E\_OUT\_OF\_RANGE：输入参数超出允许范围，例如索引越界。  - AIP\_E\_NO\_SUCH\_FIELD：请求的字段不存在，指定的字段名在当前记录中未找到。  - AIP\_E\_OVER\_LIMIT：数组超过最大长度限制（512字节）。  - AIP\_E\_CONDITION\_OVER\_LIMIT：检索条件数量超过上限（1个）。  - AIP\_E\_INVALID\_ARGS：传入的参数无效，例如空指针或参数类型不匹配。  - AIP\_E\_EMBEDDING\_ERR：无法生成嵌入向量，可能是模型加载失败或输入内容不支持向量化。 |

```c
// 示例：处理AIP接口错误码
int ret = OH_Retrieval_Retrieve(retriever, query, condition, NULL, &record);
if (ret != AIP_OK) {
    switch (ret) {
        case AIP_E_INVALID_ARGS:
            printf("参数无效，请检查输入参数。\n");
            break;
        case AIP_E_OUT_OF_RANGE:
            printf("参数超出范围，请检查索引值。\n");
            break;
        case AIP_E_EMBEDDING_ERR:
            printf("嵌入向量生成失败，请检查模型是否正常加载。\n");
            break;
        default:
            printf("操作失败，错误码：%d\n", ret);
            break;
    }
}
```
