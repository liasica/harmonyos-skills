---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getplatforminfo
title: GetPlatformInfo
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingContext > GetPlatformInfo
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:22bb6bc142be95970650ded1826b884f136a0a9dbe6318c83bec6af4c54f0aa5
---

## 函数功能

获取fe::PlatFormInfos指针。

## 函数原型

```cpp
fe::PlatFormInfos *GetPlatformInfo() const
```

## 参数说明

无

## 返回值

fe::PlatFormInfos指针。

## 约束说明

无

## 调用示例

```cpp
ge::graphStatus Tiling4XXX(TilingContext* context) {
  auto platform_info = context->GetPlatformInfo();
  // ...
}
```
