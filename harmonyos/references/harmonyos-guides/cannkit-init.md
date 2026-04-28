---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-init
title: Init
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingData > Init
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b4790fbd4f3b5f4ebf585368cbbfb391cce84f3223f96c567b6582a87d3346bc
---

## 函数功能

初始化TilingData。

## 函数原型

```
1. void Init(const size_t cap_size, void *const data);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| cap\_size | 输入 | 最大容量，单位为字节。 |
| data | 输入 | tiling data的地址。 |

## 返回值

无

## 约束说明

无

## 调用示例

```
1. size_t cap_size = 100U;
2. size_t total_size = cap_size + sizeof(TilingData);
3. auto td_buf = std::unique_ptr<uint8_t[]>(new (std::nothrow) uint8_t[total_size]());
4. auto td = reinterpret_cast<TilingData *>(td_buf.get());
5. td->Init(cap_size, td_buf.get() + sizeof(TilingData)); // 内存平铺
```
