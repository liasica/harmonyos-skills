---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getworkspacenum
title: GetWorkspaceNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingContext > GetWorkspaceNum
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c0cfe4e27d41ae1dd4eaa16a225d8a0fecd3bce3453ccd365cf932d4bd04ca9f
---

## 函数功能

获取workspace个数。

## 函数原型

```
1. size_t GetWorkspaceNum() const;
```

## 参数说明

无

## 返回值

workspace的个数。

## 约束说明

无

## 调用示例

```
1. ge::graphStatus Tiling4XXX(TilingContext* context) {
2. auto ws_num = context->GetWorkspaceNum();
3. // ...
4. }
```
