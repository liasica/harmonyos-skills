---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-compiletimetensordesc-getstorageformat
title: GetStorageFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > CompileTimeTensorDesc > GetStorageFormat
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:32069131eea913bdd20a755d654a68b29e3f412ae58d116ffa542684bf00a054
---

## 函数功能

获取运行时Tensor中存储数据的实际排布格式。

## 函数原型

```
1. ge::Format GetStorageFormat() const
```

## 参数说明

无

## 返回值

运行时数据的实际排布格式。

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
