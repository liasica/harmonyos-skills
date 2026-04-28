---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tilingdata-operator
title: operator
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingData > operator
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0d1c4228345bbc82f89b389c86e860f63cdd5c9001e39e3b9cb038ebbae81501
---

## 函数功能

向后添加tiling data，若添加超过可容纳的最大长度，则忽略本次操作。

## 函数原型

```
1. template<typename T>
2. TilingData &operator<<(TilingData &out, const T &data);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| T | 输入 | 添加的tiling data的类型。 |
| out | 输出 | TilingData类实例。 |
| data | 输入 | 添加的tiling data的实例。 |

## 返回值

追加完data的TilingData对象。

## 约束说明

无

## 调用示例

```
1. auto td_buf = TilingData::CreateCap(100U);
2. auto td = reinterpret_cast<TilingData *>(td_buf.get());

4. struct AppendData{
5. int a = 10;
6. int b = 100;
7. };
8. AppendData ad;
9. td << ad;
10. auto data_size = td.GetDataSize(); // 2 * sizeof(int)
```
