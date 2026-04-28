---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcapacity
title: GetCapacity
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingData > GetCapacity
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:12087ca20cadb28189a5b6ff9a8c1d7ee4d758ce2051df60db06155b6871b3d4
---

## 函数功能

获取本实例可容纳的最大tiling data长度。

## 函数原型

```
1. size_t GetCapacity() const;
```

## 参数说明

无

## 返回值

最大tiling data长度。

## 约束说明

无

## 调用示例

```
1. auto td_buf = TilingData::CreateCap(100U);
2. auto td = reinterpret_cast<TilingData *>(td_buf.get());
3. size_t cap = td->GetCapacity(); // 100U
```
