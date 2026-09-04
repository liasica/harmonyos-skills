---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getname
title: GetName
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetName
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6f52aa874d99cf8a9fe2a95457c4de5731f49f3e396c8d7f972a1857bb5b2559
---

## 函数功能

获取算子名称。

## 函数原型

![](https://media:401788444113840927) 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
std::string GetName() const;
graphStatus GetName(AscendString &name) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输出 | 算子名称。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | GRAPH\_FAILED：失败。  GRAPH\_SUCCESS：成功。 |

## 异常处理

无

## 约束说明

无
