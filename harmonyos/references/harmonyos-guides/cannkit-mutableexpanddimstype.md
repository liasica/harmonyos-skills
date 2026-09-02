---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-mutableexpanddimstype
title: MutableExpandDimsType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageFormat > MutableExpandDimsType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d1c942609a35d219d2d1fd15cbfb548bb2bbb970e6d0662a57f105fa07f4e1cb
---

## 函数功能

获取可写的补维规则。

## 函数原型

```cpp
ExpandDimsType &MutableExpandDimsType()
```

## 参数说明

无

## 返回值

补维规则引用。

## 约束说明

无

## 调用示例

```cpp
ExpandDimsType dim_type("1100");
StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
ExpandDimsType new_dim_type("1010");
format.SetExpandDimsType(new_dim_type);
auto &fmt_dim_type = format.MutableExpandDimsType();
```
