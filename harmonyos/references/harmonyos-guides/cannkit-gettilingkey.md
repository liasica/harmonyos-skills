---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gettilingkey
title: GetTilingKey
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingContext > GetTilingKey
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:28503fe7cae51ee997d5d77892a3b2368b3c2ad6d4994b02d1df0d6295b34624
---

## 函数功能

获取tiling key。

## 函数原型

```cpp
uint64_t GetTilingKey() const;
```

## 参数说明

无

## 返回值

返回tiling key。

## 约束说明

无

## 调用示例

```cpp
ge::graphStatus Tiling4XXX(TilingContext* context) {
  auto tiling_key = context->GetTilingKey();
  // ...
}
```
