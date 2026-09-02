---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-init
title: Init
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingData > Init
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f0bc9ef732902f8075f2f9f458c555b7c1da877531e49e0263cfec35419e7e50
---

## 函数功能

初始化TilingData。

## 函数原型

```cpp
void Init(const size_t cap_size, void *const data);
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

```cpp
size_t cap_size = 100U;
size_t total_size = cap_size + sizeof(TilingData);
auto td_buf = std::unique_ptr<uint8_t[]>(new (std::nothrow) uint8_t[total_size]());
auto td = reinterpret_cast<TilingData *>(td_buf.get());
td->Init(cap_size, td_buf.get() + sizeof(TilingData)); // 内存平铺
```
