---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-calctotalsize
title: CalcTotalSize
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingData > CalcTotalSize
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:13c667fca2fd2605263ad2deae058343b7a92f8211ad4a0f3ddb39e93c55d2b8
---

## 函数功能

通过最大容量计算TilingData实例所占用的内存空间。

## 函数原型

```
1. static ge::graphStatus CalcTotalSize(const size_t cap_size, size_t &total_size);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| cap\_size | 输入 | 最大容量，单位为字节。 |
| total\_size | 输出 | 内存空间，单位为字节。 |

## 返回值

* 成功返回：ge::GRAPH\_SUCCESS。
* 失败返回：ge::GRAPH\_FAILED。

## 约束说明

无

## 调用示例

```
1. auto td_buf = TilingData::CreateCap(100U);
2. auto td = reinterpret_cast<TilingData *>(td_buf.get());
3. size_t total_size = 0U;
4. auto ret = td->CalcTotalSize(td->GetCapacity, total_size); // total_size = 100 + sizeof(TilingData)
```
