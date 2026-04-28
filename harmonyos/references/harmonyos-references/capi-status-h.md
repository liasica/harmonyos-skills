---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-status-h
title: status.h
breadcrumb: API参考 > AI > MindSpore Lite Kit（昇思推理框架服务） > C API > 头文件 > status.h
category: harmonyos-references
scraped_at: 2026-04-28T08:19:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5076bfde33aefa0307c065f26888b6bebb45aa6823a2ffaf1d3ac4464a29f10b
---

## 概述

PhonePC/2in1TabletTVWearable

提供了MindSpore Lite运行时的状态码。

**引用文件：** <mindspore/status.h>

**库：** libmindspore\_lite\_ndk.so

**系统能力：** SystemCapability.Ai.MindSpore

**起始版本：** 9

**相关模块：** [MindSpore](capi-mindspore.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AI\_CompCode](capi-status-h.md#oh_ai_compcode) | - | MindSpore不同组件的代码。 |
| [OH\_AI\_Status](capi-status-h.md#oh_ai_status) | OH\_AI\_Status | MindSpore的状态码。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_AI\_CompCode

PhonePC/2in1TabletTVWearable

```
1. enum OH_AI_CompCode
```

**描述**

MindSpore不同组件的代码。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_AI\_COMPCODE\_CORE = 0x00000000u | MindSpore Core的代码。 |
| OH\_AI\_COMPCODE\_MD = 0x10000000u | MindSpore MindData的代码。 |
| OH\_AI\_COMPCODE\_ME = 0x20000000u | MindSpore MindExpression的代码。 |
| OH\_AI\_COMPCODE\_MC = 0x30000000u | MindSpore的代码。 |
| OH\_AI\_COMPCODE\_LITE = 0xF0000000u | MindSpore Lite的代码。 |

### OH\_AI\_Status

PhonePC/2in1TabletTVWearable

```
1. enum OH_AI_Status
```

**描述**

MindSpore的状态码。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_AI\_STATUS\_SUCCESS = 0 | 执行成功。 |
| OH\_AI\_STATUS\_CORE\_FAILED = OH\_AI\_COMPCODE\_CORE | 0x1 | MindSpore Core执行失败。 |
| OH\_AI\_STATUS\_LITE\_ERROR = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -1) | MindSpore Lite执行异常。 |
| OH\_AI\_STATUS\_LITE\_NULLPTR = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -2) | MindSpore Lite空指针异常。 |
| OH\_AI\_STATUS\_LITE\_PARAM\_INVALID = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -3) | MindSpore Lite参数异常。 |
| OH\_AI\_STATUS\_LITE\_NO\_CHANGE = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -4) | MindSpore Lite未改变。 |
| OH\_AI\_STATUS\_LITE\_SUCCESS\_EXIT = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -5) | MindSpore Lite没有错误但是退出。 |
| OH\_AI\_STATUS\_LITE\_MEMORY\_FAILED = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -6) | MindSpore Lite分配内存失败。 |
| OH\_AI\_STATUS\_LITE\_NOT\_SUPPORT = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -7) | MindSpore Lite未支持的功能。 |
| OH\_AI\_STATUS\_LITE\_THREADPOOL\_ERROR = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -8) | MindSpore Lite线程池异常。 |
| OH\_AI\_STATUS\_LITE\_UNINITIALIZED\_OBJ = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -9) | MindSpore Lite 未初始化状态码。 |
| OH\_AI\_STATUS\_LITE\_OUT\_OF\_TENSOR\_RANGE = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -100) | 执行器相关的错误码，范围 (-200, -100]。  MindSpore Lite张量溢出错误。 |
| OH\_AI\_STATUS\_LITE\_INPUT\_TENSOR\_ERROR = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -101) | 执行器相关的错误码，范围 (-200, -100]。  MindSpore Lite张量输入异常。 |
| OH\_AI\_STATUS\_LITE\_REENTRANT\_ERROR = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -102) | 执行器相关的错误码，范围 (-200, -100]。  MindSpore Lite函数重入异常。 |
| OH\_AI\_STATUS\_LITE\_GRAPH\_FILE\_ERROR = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -200) | 图相关的错误码，范围 (-300, -200]。  MindSpore Lite图文件异常。 |
| OH\_AI\_STATUS\_LITE\_NOT\_FIND\_OP = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -300) | 算子相关的错误码，范围 (-400, -300]。  MindSpore Lite未找到算子。 |
| OH\_AI\_STATUS\_LITE\_INVALID\_OP\_NAME = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -301) | 算子相关的错误码，范围 (-400, -300]。  MindSpore Lite算子无效。 |
| OH\_AI\_STATUS\_LITE\_INVALID\_OP\_ATTR = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -302) | 算子相关的错误码，范围 (-400, -300]。  MindSpore Lite算子超参数无效。 |
| OH\_AI\_STATUS\_LITE\_OP\_EXECUTE\_FAILURE = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -303) | 算子相关的错误码，范围 (-400, -300]。  MindSpore Lite算子执行失败。 |
| OH\_AI\_STATUS\_LITE\_FORMAT\_ERROR = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -400) | 张量相关的错误码，范围 (-500, -400]。  MindSpore Lite张量格式异常。 |
| OH\_AI\_STATUS\_LITE\_INFER\_ERROR = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -500) | 形状推理相关的错误码，范围 (-600, -500]。  MindSpore Lite形状推理异常。 |
| OH\_AI\_STATUS\_LITE\_INFER\_INVALID = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -501) | 形状推理相关的错误码，范围 (-600, -500]。  MindSpore Lite形状推理无效。 |
| OH\_AI\_STATUS\_LITE\_INPUT\_PARAM\_INVALID = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -600) | 用户输入相关的错误码，范围 (-700, -600]。  用户输入的参数无效。 |
| OH\_AI\_STATUS\_LITE\_AIPP\_NOT\_SUPPORTED = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -700) | AIPP（AI Pre-Process，针对AI推理的输入数据进行前处理）相关的错误码，范围 (-800, -700]。  MindSpore Lite不支持AIPP。  **起始版本：** 23 |
| OH\_AI\_STATUS\_LITE\_AIPP\_INFER\_ERROR = OH\_AI\_COMPCODE\_LITE | (0x0FFFFFFF & -701) | AIPP（AI Pre-Process，针对AI推理的输入数据进行前处理）相关的错误码，范围 (-800, -700]。  MindSpore Lite使用AIPP推理失败。  **起始版本：** 23 |
