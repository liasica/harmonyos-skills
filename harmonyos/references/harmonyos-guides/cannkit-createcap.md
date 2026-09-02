---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-createcap
title: CreateCap
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingData > CreateCap
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dcb60c9f3b3320d6953cc6a998236269c6b43b20481f43da2719896f6edb7e11
---

## 函数功能

根据指定的最大容量创建一个TilingData类实例。

## 函数原型

```cpp
static std::unique_ptr<uint8_t[]> CreateCap(const size_t cap_size);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| cap\_size | 输入 | 最大容量，单位为字节。 |

## 返回值

TilingData的实例指针。

## 约束说明

无

## 调用示例

```cpp
auto td_buf = TilingData::CreateCap(100U);
auto td = reinterpret_cast<TilingData *>(td_buf.get());
```
