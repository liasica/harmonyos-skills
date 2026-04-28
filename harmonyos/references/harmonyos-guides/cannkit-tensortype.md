---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensortype
title: TensorType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorType
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bee6d29e4912a01c2f56327e478c84e6e6eda22ed0a77a1ee29c8d5218c7257b
---

TensorType类用以定义输入或者输出支持的数据类型，TensorType提供以下接口指定支持的数据类型：

```
1. struct TensorType {
2. explicit TensorType(DataType dt);

4. TensorType(const std::initializer_list<DataType> &initial_types);

6. static TensorType ALL() {
7. return TensorType{DT_BOOL,   DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT,  DT_FLOAT16, DT_INT16,
8. DT_INT32,  DT_INT64,      DT_INT8,      DT_QINT16, DT_QINT32, DT_QINT8,   DT_QUINT16,
9. DT_QUINT8, DT_RESOURCE,   DT_STRING,    DT_UINT16, DT_UINT32, DT_UINT64,  DT_UINT8,
10. DT_BF16, DT_COMPLEX32};
11. }

13. static TensorType QuantifiedType() { return TensorType{DT_QINT16, DT_QINT32, DT_QINT8, DT_QUINT16, DT_QUINT8}; }

15. static TensorType OrdinaryType() {
16. return TensorType{DT_BOOL,  DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT,  DT_FLOAT16, DT_INT16,
17. DT_INT32, DT_INT64,      DT_INT8,      DT_UINT16, DT_UINT32, DT_UINT64,  DT_UINT8,
18. DT_BF16, DT_COMPLEX32};
19. }

21. static TensorType BasicType() {
22. return TensorType{DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT,  DT_FLOAT16, DT_INT16,
23. DT_INT32,      DT_INT64,     DT_INT8,   DT_QINT16, DT_QINT32,  DT_QINT8,
24. DT_QUINT16,    DT_QUINT8,    DT_UINT16, DT_UINT32, DT_UINT64,  DT_UINT8,
25. DT_BF16, DT_COMPLEX32};
26. }

28. static TensorType NumberType() {
29. return TensorType{DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT,  DT_FLOAT16, DT_INT16,  DT_INT32,  DT_INT64,
30. DT_INT8,       DT_QINT32,    DT_QINT8,  DT_QUINT8, DT_UINT16,  DT_UINT32, DT_UINT64, DT_UINT8,
31. DT_BF16, DT_COMPLEX32};
32. }

34. static TensorType RealNumberType() {
35. return TensorType{DT_DOUBLE, DT_FLOAT,  DT_FLOAT16, DT_INT16,  DT_INT32, DT_INT64,
36. DT_INT8,   DT_UINT16, DT_UINT32,  DT_UINT64, DT_UINT8, DT_BF16};
37. }

39. static TensorType ComplexDataType() { return TensorType{DT_COMPLEX128, DT_COMPLEX64, DT_COMPLEX32}; }

41. static TensorType IntegerDataType() {
42. return TensorType{DT_INT16, DT_INT32, DT_INT64, DT_INT8, DT_UINT16, DT_UINT32, DT_UINT64, DT_UINT8};
43. }

45. static TensorType SignedDataType() { return TensorType{DT_INT16, DT_INT32, DT_INT64, DT_INT8}; }

47. static TensorType UnsignedDataType() { return TensorType{DT_UINT16, DT_UINT32, DT_UINT64, DT_UINT8}; }

49. static TensorType FloatingDataType() { return TensorType{DT_DOUBLE, DT_FLOAT, DT_FLOAT16}; }

51. static TensorType IndexNumberType() { return TensorType{DT_INT32, DT_INT64}; }

53. static TensorType UnaryDataType() {
54. return TensorType{DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16, DT_BF16, DT_COMPLEX32};
55. }

57. static TensorType FLOAT() { return TensorType{DT_FLOAT, DT_FLOAT16, DT_BF16}; }

59. std::shared_ptr<TensorTypeImpl> tensor_type_impl_;
60. };
```
