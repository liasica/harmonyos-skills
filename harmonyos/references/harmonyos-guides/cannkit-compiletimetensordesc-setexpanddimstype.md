---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-compiletimetensordesc-setexpanddimstype
title: SetExpandDimsType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > CompileTimeTensorDesc > SetExpandDimsType
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dbcd9125703b017d32127c00c57db919e2920304ca1bcea33b108bf5999fd321
---

## 函数功能

设置原始Format向运行时Format转换时的补维规则。

## 函数原型

```
1. void SetExpandDimsType(const ExpandDimsType &expand_dims_type)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| expand\_dims\_type | 输入 | 需要设置的补维规则。  关于ExpandDimsType的说明，请参见[ExpandDimsType](cannkit-expanddimstype-introduction.md)。 |

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
11. td.SetExpandDimsType(type_);
12. auto type = td.GetExpandDimsType(); // type_("1001")
```
