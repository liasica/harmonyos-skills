---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-dynamicoutputregister
title: DynamicOutputRegister
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > DynamicOutputRegister
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:041aaa2ea7b3ff72a3685563b1bd69d81d4b410076212bf5d30b7d1842b16256
---

## 函数功能

算子动态输出注册。

## 函数原型

```
1. void DynamicOutputRegister(const char_t *name, const uint32_t num, bool is_push_back = true);
2. void DynamicOutputRegister(const char_t *name, const uint32_t num, const char_t *datatype_symbol, bool is_push_back = true);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 算子的动态输出名。 |
| num | 输入 | 添加的动态输出个数。 |
| datatype\_symbol | 输入 | 动态输出的数据类型。 |
| is\_push\_back | 输入 | - true表示在尾部追加动态输出。  - false表示在头部追加动态输出。 |

## 返回值

无

## 异常处理

无

## 约束说明

无
