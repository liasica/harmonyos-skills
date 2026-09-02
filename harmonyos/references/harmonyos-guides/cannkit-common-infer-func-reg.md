---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-common-infer-func-reg
title: COMMON_INFER_FUNC_REG
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > COMMON_INFER_FUNC_REG
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:38c3fdea60bb4b7a9d4866f0b1b1a8dca06c1ab49919e94e1e55db6075fc1cfc
---

## 函数功能

注册算子的InferShape函数。

与[INFER\_FUNC\_REG](cannkit-infer-func-reg.md)的区别是，此函数注册的InferShape函数入参为operator基类而非子类，此接口支持多算子共用同一个InferShape函数。

## 函数原型

```cpp
COMMON_INFER_FUNC_REG(op_name, x)
```

该函数内部会自动调用COMMON\_INFER\_VERIFY\_FUNC(x)，COMMON\_INFER\_VERIFY\_FUNC(x)函数中的x为指向COMMON\_INFER\_FUNC\_REG(op\_name, x)中“x”的指针。

## 约束说明

无

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| op\_name | 输入 | 算子类型。 |
| x | 输入 | InferShape函数名，和[IMPLEMT\_COMMON\_INFERFUNC](cannkit-implemt-common-inferfunc.md)的InferShape函数名保持一致。 |

## 返回值

无
