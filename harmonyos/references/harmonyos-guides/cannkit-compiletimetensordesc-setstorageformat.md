---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-compiletimetensordesc-setstorageformat
title: SetStorageFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > CompileTimeTensorDesc > SetStorageFormat
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3be27dc5dd19674c8415b6f954aa1e9954e22fa45d9bdafdff944edde35dfcf9
---

## 函数功能

向CompileTimeTensorDesc中设置运行时Tensor的数据排布格式。

## 函数原型

```cpp
void SetStorageFormat(const ge::Format format)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| format | 输入 | 需要设置的运行时数据排布格式信息。  关于ge::Format的定义，请参见[Format](cannkit-ge-format.md)。 |

## 返回值

无

## 约束说明

无

## 调用示例

```cpp
auto dtype_ = ge::DataType::DT_INT32;
StorageFormat fmt_(ge::Format::FORMAT_NC, ge::FORMAT_NCHW, {});
ExpandDimsType type_("1001");
gert::CompileTimeTensorDesc td;
td.SetDataType(dtype_);
auto dtype = td.GetDataType(); // ge::DataType::DT_INT32;
td.SetStorageFormat(fmt_.GetStorageFormat());
auto storage_fmt = td.GetStorageFormat(); // ge::FORMAT_NCHW
td.SetOriginFormat(fmt_.GetOriginFormat());
auto origin_fmt = td.GetOriginFormat(); // ge::Format::FORMAT_NC
td.SetExpandDimsType(type_);auto type = td.GetExpandDimsType(); // type_("1001")
```
