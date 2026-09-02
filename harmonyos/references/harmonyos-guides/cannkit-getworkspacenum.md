---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getworkspacenum
title: GetWorkspaceNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingContext > GetWorkspaceNum
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:42d743d71041dd07a37bad4c04a78318cbe140d1d28c0ef42fd18d8c9a642d50
---

## 函数功能

获取workspace个数。

## 函数原型

```cpp
size_t GetWorkspaceNum() const;
```

## 参数说明

无

## 返回值

workspace的个数。

## 约束说明

无

## 调用示例

```cpp
ge::graphStatus Tiling4XXX(TilingContext* context) {
  auto ws_num = context->GetWorkspaceNum();
  // ...
}
```
