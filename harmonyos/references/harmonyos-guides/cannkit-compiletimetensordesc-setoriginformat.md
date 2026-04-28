---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-compiletimetensordesc-setoriginformat
title: SetOriginFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > CompileTimeTensorDesc > SetOriginFormat
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fb234674c22fadd4917aabda231109b7f0ee95e39d9e401cb57fcc71962572ca
---

## 函数功能

向CompileTimeTensorDesc中设置Tensor的原始数据排布格式。

## 函数原型

```
1. void SetOriginFormat(const ge::Format format)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| format | 输入 | 需要设置的原始数据排布格式信息。  关于ge::Format的定义，请参见[Format](cannkit-ge-format.md)。 |

## 返回值

无

## 约束说明

无

## 调用示例

```
1. auto dtype_ = ge::DataType::DT_INT32;
2. StorageFormat fmt_(ge::Format::FORMAT_NC, ge::FORMAT_NCHW, {});
3. ExpandDimsType type_("1001");
4. gert::CompileTimeTensorDesc td;
5. td.SetDataType(dtype_);
6. auto dtype = td.GetDataType(); // ge::DataType::DT_INT32;
7. td.SetStorageFormat(fmt_.GetStorageFormat());
8. auto storage_fmt = td.GetStorageFormat(); // ge::FORMAT_NCHW
9. td.SetOriginFormat(fmt_.GetOriginFormat());
10. auto origin_fmt = td.GetOriginFormat(); // ge::Format::FORMAT_NC
11. td.SetExpandDimsType(type_);auto type = td.GetExpandDimsType(); // type_("1001")
```
