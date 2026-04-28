---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-createcap
title: CreateCap
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingData > CreateCap
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9a7d97eed0095897837c5f8a33c6c82cd8dbbea1012e3d66e171f10ce8af6483
---

## 函数功能

根据指定的最大容量创建一个TilingData类实例。

## 函数原型

```
1. static std::unique_ptr<uint8_t[]> CreateCap(const size_t cap_size);
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

```
1. auto td_buf = TilingData::CreateCap(100U);
2. auto td = reinterpret_cast<TilingData *>(td_buf.get());
```
