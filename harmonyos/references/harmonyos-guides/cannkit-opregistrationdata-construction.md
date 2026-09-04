---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-opregistrationdata-construction
title: 构造函数和析构函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > 构造函数和析构函数
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2dd36e198e47236acfaf9921be0b92dd28b9a7e4c4a3e0b0f7f3376d007be8ef
---

## 函数功能

OpRegistrationData构造函数和析构函数。

## 函数原型

![](https://media:401788444104128885) 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
OpRegistrationData(const std::string &om_optype);
OpRegistrationData(const char_t *om_optype);
~OpRegistrationData();
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| om\_optype | 输入 | 指定适配AI处理器的模型支持的算子类型。 |

## 返回值

OpRegistrationData构造函数返回OpRegistrationData类型的对象。

## 异常处理

无

## 约束说明

无
