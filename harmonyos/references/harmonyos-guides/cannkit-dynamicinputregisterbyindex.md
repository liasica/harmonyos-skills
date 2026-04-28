---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-dynamicinputregisterbyindex
title: DynamicInputRegisterByIndex
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > DynamicInputRegisterByIndex
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2b5e49ff041d9464daf85c7d0a1060ee702f1922998725ce3d377e44941b659f
---

## 函数功能

指定位置进行算子动态输入注册。

## 函数原型

```
1. void DynamicInputRegisterByIndex(const char_t *name, const uint32_t num, size_t index);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 算子的动态Input名。 |
| num | 输入 | 添加的动态Input个数。 |
| index | 输入 | 从index位置添加动态输入。 |

## 返回值

无

## 异常处理

无

## 约束说明

无
