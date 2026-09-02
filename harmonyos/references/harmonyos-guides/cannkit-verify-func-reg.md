---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-verify-func-reg
title: VERIFY_FUNC_REG
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > VERIFY_FUNC_REG
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:44f1a724ba621764dff6fe97ddf8d70fa1621d6ee9a59e6c1bf90b5ed80751d5
---

## 函数功能

注册算子的Verify函数。

## 函数原型

```cpp
VERIFY_FUNC_REG(op_name, x)
```

## 约束说明

无

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| op\_name | 输入 | 算子类型。 |
| x | 输入 | Verify函数名，和[IMPLEMT\_VERIFIER](cannkit-implemt-verifier.md)的Verify函数名保持一致。 |

## 返回值

无
