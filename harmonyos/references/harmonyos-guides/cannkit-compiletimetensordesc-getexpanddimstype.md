---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-compiletimetensordesc-getexpanddimstype
title: GetExpandDimsType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > CompileTimeTensorDesc > GetExpandDimsType
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4d1c9793449c91da0634c8ccc48557b672c104e96a4b8fe1c32d6cefdd5d95be
---

## 函数功能

获取原始Format向运行时Format转换时的补维规则。

## 函数原型

```
1. ExpandDimsType GetExpandDimsType() const
```

## 参数说明

无

## 返回值

补维规则，请参考[ExpandDimsType](cannkit-expanddimstype-introduction.md)。

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
