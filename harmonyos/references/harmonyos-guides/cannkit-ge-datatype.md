---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-datatype
title: DataType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > DataType
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d652332780834b166a150e2ebb5ccca1cad96fb3b52799c4952e676eaadcff13
---

DataType枚举值定义如下。

```
1. enum DataType {
2. DT_FLOAT = 0,            // float type
3. DT_FLOAT16 = 1,          // fp16 type
4. DT_INT8 = 2,             // int8 type
5. DT_INT32 = 3,            // int32 type
6. DT_UINT8 = 4,            // uint8 type
7. // reserved
8. DT_INT16 = 6,            // int16 type
9. DT_UINT16 = 7,           // uint16 type
10. DT_UINT32 = 8,           // unsigned int32
11. DT_INT64 = 9,            // int64 type
12. DT_UINT64 = 10,          // unsigned int64
13. DT_DOUBLE = 11,          // double type
14. DT_BOOL = 12,            // bool type
15. DT_STRING = 13,          // string type
16. DT_DUAL_SUB_INT8 = 14,   // dual output int8 type
17. DT_DUAL_SUB_UINT8 = 15,  // dual output uint8 type
18. DT_COMPLEX64 = 16,       // complex64 type
19. DT_COMPLEX128 = 17,      // complex128 type
20. DT_QINT8 = 18,           // qint8 type
21. DT_QINT16 = 19,          // qint16 type
22. DT_QINT32 = 20,          // qint32 type
23. DT_QUINT8 = 21,          // quint8 type
24. DT_QUINT16 = 22,         // quint16 type
25. DT_RESOURCE = 23,        // resource type
26. DT_STRING_REF = 24,      // string ref type
27. DT_DUAL = 25,            // dual output type
28. DT_VARIANT = 26,         // dt_variant type
29. DT_BF16 = 27,            // bf16 type
30. DT_UNDEFINED = 28,       // Used to indicate a DataType field has not been set.
31. DT_INT4 = 29,            // int4 type
32. DT_UINT1 = 30,           // uint1 type
33. DT_INT2 = 31,            // int2 type
34. DT_UINT2 = 32,           // uint2 type
35. DT_COMPLEX32 = 33,       // complex32 type
36. DT_MAX                   // Mark the boundaries of data types
37. };
```
