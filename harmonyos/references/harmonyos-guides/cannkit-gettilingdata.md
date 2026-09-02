---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gettilingdata
title: GetTilingData
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingContext > GetTilingData
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:48c53e4c65c2b55335e139b6327036cb08d128594f7737edfa3ca18589e942fe
---

## 函数功能

获取有类型的tiling data指针。

## 函数原型

```cpp
template<typename T>  T *GetTilingData();
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| T | 输出 | tiling data类型，sizeof(T)不可以大于编译结果中指定的最大tiling data长度。 |

## 返回值

tiling data指针，失败时返回空指针。

## 约束说明

sizeof(T)不可以大于编译结果中指定的最大tiling data长度。

## 调用示例

```cpp
ge::graphStatus Tiling4XXX(TilingContext* context) {
  auto tiling_data = context->GetTilingData<int64_t>();
  // ...
}
```
