---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gettilingcond
title: GetTilingCond
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingContext > GetTilingCond
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5dd4d629bfa2cfc2242ffd5be98b9ad3e2c8ccb799e473b2978562b80d36d714
---

## 函数功能

获取tiling cond。

## 函数原型

```cpp
int32_t GetTilingCond() const;
```

## 参数说明

无

## 返回值

tiling cond:

若返回值大于等于0，代表此tiling cond为有效的tiling cond。

若返回值为-1，代表此tiling cond为无效的tiling cond。

## 约束说明

无

## 调用示例

```cpp
ge::graphStatus Tiling4XXX(TilingContext* context) {
  auto tiling_cond = context->GetTilingCond();
  // ...
}
```
