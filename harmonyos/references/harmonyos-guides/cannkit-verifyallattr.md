---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-verifyallattr
title: VerifyAllAttr
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > VerifyAllAttr
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3a448d6d8c51d1f32f019b984e16186ab532a23aa455763e5cc6daba4b7d40c8
---

## 函数功能

根据disableCommonVerifier值，校验Operator中的属性是否有效，校验Operator的输入输出是否有效。

## 函数原型

```
1. graphStatus VerifyAllAttr(bool disable_common_verifier = false);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| disable\_common\_verifier | 输入 | 当false时，只校验属性有效性，当true时，增加校验Operator所有输入输出有效性。  默认值为false。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 推导成功，返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
