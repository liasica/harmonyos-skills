---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-addcontrolinput
title: AddControlInput
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > AddControlInput
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5feb4b8a61cd4007c2ecc40138a6a88f2a22ee9d47c88328c467063b6ea1aa4f
---

## 函数功能

添加算子的控制边，控制边目前只是控制算子的执行顺序。

## 函数原型

```cpp
Operator &AddControlInput(const Operator &src_oprt);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| src\_oprt | 输入 | 控制边对应的源算子。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| Operator& | 算子对象本身。 |

## 异常处理

无

## 约束说明

无
