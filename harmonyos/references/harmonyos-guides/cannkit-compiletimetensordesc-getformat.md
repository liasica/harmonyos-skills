---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-compiletimetensordesc-getformat
title: GetFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > CompileTimeTensorDesc > GetFormat
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6da2ffa083d510103452840b1372e00b6b955d6bea695bbdfd5fd846332268ae
---

## 函数功能

获取CompileTimeTensorDesc所描述的Tensor的数据排布格式。

## 函数原型

```
1. const StorageFormat &GetFormat() const
```

## 参数说明

无

## 返回值

返回数据排布格式。

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
7. td.SetStorageFormat(fmt_.GetFormat());
8. auto storage_fmt = td.GetFormat(); // ge::FORMAT_NCHW
9. td.SetOriginFormat(fmt_.GetOriginFormat());
10. auto origin_fmt = td.GetOriginFormat(); // ge::Format::FORMAT_NC
11. td.SetExpandDimsType(type_);
12. auto type = td.GetExpandDimsType(); // type_("1001")
```
