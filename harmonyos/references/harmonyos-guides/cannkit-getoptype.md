---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoptype
title: GetOpType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetOpType
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:56233830b18f4514d572a7b8f9dfd0b848b3a9ccb3822cb3aaed27e38118607d
---

## 函数功能

获取算子类型。

## 函数原型

![](https://media:401788444114642932) 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
std::string GetOpType() const;
graphStatus GetOpType(AscendString &type) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| type | 输出 | 算子类型。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | GRAPH\_FAILED：失败。  GRAPH\_SUCCESS：成功。 |

## 异常处理

无

## 约束说明

无
