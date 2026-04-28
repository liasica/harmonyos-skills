---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-dynamicinputregister
title: DynamicInputRegister
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > DynamicInputRegister
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d0c01a5ba9f7c76bbb273eb7dc065a60575e341ec1260d08d81c5d772cd81460
---

## 函数功能

算子动态输入注册。

## 函数原型

```
1. void DynamicInputRegister(const char_t *name, const uint32_t num, bool is_push_back = true);
2. void DynamicInputRegister(const char_t *name, const uint32_t num, const char_t *datatype_symbol, bool is_push_back = true);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 算子的动态输入名。 |
| num | 输入 | 添加的动态输入个数。 |
| datatype\_symbol | 输入 | 动态输入的数据类型。 |
| is\_push\_back | 输入 | - true表示在尾部追加动态输入。  - false表示在头部追加动态输入。 |

## 返回值

无

## 异常处理

无

## 约束说明

无
