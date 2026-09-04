---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setname
title: SetName
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > SetName
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:617f8350924d0b34a8724bb67293fda242bb6bbfb1a835775227db01cb54792c
---

## 函数功能

向TensorDesc中设置Tensor的名称。

## 函数原型

![](https://media:401788444113719926) 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
void SetName(const std::string &name);
void SetName(const char_t *name);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 需设置的Tensor的名称。 |

## 返回值

无

## 异常处理

无

## 约束说明

无
