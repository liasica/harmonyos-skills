---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-free
title: Free
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TensorData > Free
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8addd2b50ba027d2ce318e7f5f8b2564d106b2d5624cd12915ba744dfb0df583
---

## 函数功能

释放tensor。

## 函数原型

```
1. ge::graphStatus Free()
```

## 参数说明

无

## 返回值

成功时返回：ge::GRAPH\_SUCCESS。

失败时返回manager函数返回的状态码。

关于ge::graphStatus类型的定义，请参见[ge::graphStatus](cannkit-gegraphstatus.md)。

## 约束说明

无

## 调用示例

```
1. std::vector<int> a = {10};
2. auto addr = reinterpret_cast<void *>(a.data());
3. TensorData td(addr, nullptr);
4. td.Free();
```
