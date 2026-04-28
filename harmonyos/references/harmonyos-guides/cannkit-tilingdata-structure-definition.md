---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tilingdata-structure-definition
title: TilingData结构定义
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > Tiling数据结构注册 > TilingData结构定义
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:750f006c6a95ccc85a0062d9bfa7916f5fba8cef23abd2809615916d33475af6
---

## 函数功能

定义一个TilingData的类，添加所需的成员变量（TilingData字段），用于保存所需TilingData参数。完成该TilingData类的定义后，该类通过继承TilingDef类（用来存放、处理开发者自定义Tiling结构体成员变量的基类）提供以下接口：

* set\_+field\_name接口：用于设置TilingData类的字段值，field\_name为定义TilingData类时添加的字段名。
* SaveToBuffer接口：完成TilingData的序列化和保存。
* GetDataSize接口：获取TilingData的长度。

## 函数原型

* 定义一个TilingData类

  ```
  1. BEGIN_TILING_DATA_DEF(class_name)
  ```
* 添加通用数据类型的TilingData字段

  ```
  1. TILING_DATA_FIELD_DEF(data_type, field_name)
  ```
* 添加数组类型的TilingData字段，数组的元素数据类型为通用数据类型

  ```
  1. TILING_DATA_FIELD_DEF_ARR(arr_type, arr_size, field_name)
  ```
* 添加结构体类型的TilingData字段

  ```
  1. TILING_DATA_FIELD_DEF_STRUCT(struct_type, field_name)
  ```
* 定义结束

  ```
  1. END_TILING_DATA_DEF
  ```

## 参数说明

**表1** BEGIN\_TILING\_DATA\_DEF参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| class\_name | 输入 | 开发者定义tiling结构体名，与c++变量命名要求一致。 |

**表2** TILING\_DATA\_FIELD\_DEF参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| data\_type | 输入 | 字段的数据类型。 |
| field\_name | 输入 | 字段名，与c++变量命名要求一致。 |

**表3** TILING\_DATA\_FIELD\_DEF\_ARR参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| arr\_type | 输入 | 数组元素数据类型。 |
| arr\_size | 输入 | 数组元素个数。 |
| field\_name | 输入 | 字段名，与c++变量命名要求一致。 |

**表4** TILING\_DATA\_FIELD\_DEF\_STRUCT参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| struct\_type | 输入 | 结构体类型。 |
| field\_name | 输入 | 字段名，与c++变量命名要求一致。 |

## 约束说明

* 使用SaveToBuffer接口时必须在set\_+\_field\_name\_接口后调用。
* 使用时需要包含头文件register/tilingdata\_base.h。
* TILING\_DATA\_FIELD\_DEF和TILING\_DATA\_FIELD\_DEF\_ARR中定义的变量，仅支持int8\_t, uint8\_t, int16\_t, uint16\_t, int32\_t, uint32\_t, int64\_t, uint64\_t, float数据类型。
* TILING\_DATA\_FIELD\_DEF\_STRUCT中struct\_type仅支持用BEGIN\_TILING\_DATA\_DEF等定义的tiling结构体，不支持直接使用c++语法定义的结构体类型。
* 开发者在host侧设置参数值和使用tiling数据需要使用set\_xxx和get\_xxx接口（xxx请替换为字段名），具体使用方法见调用示例。
* tiling数据成员需要满足字节对齐要求，即：当前数据成员dataVar位于结构体的偏移offset满足， offset % sizeof(dataVar) == 0。
* tiling结构体是全局属性，需注意应通过结构体名作为全局唯一标记，不同算子若注册同名不同结构tiling结构体则会发生未定义行为。

## 调用示例

```
1. #include "register/tilingdata_base.h"

3. // 定义tilingdata类
4. namespace optiling {
5. BEGIN_TILING_DATA_DEF(Matmul)
6. TILING_DATA_FIELD_DEF(uint16_t, mmVar);
7. TILING_DATA_FIELD_DEF_ARR(uint16_t, 3, mmArr);
8. END_TILING_DATA_DEF;
9. // 注册中间结构体，第一个参数固定为struct_name#Op，第二个参数即struct_name, 如struct_name为Matmul，第一参数为MatmulOp，第二个参数为Matmul
10. REGISTER_TILING_DATA_CLASS(MatmulOp, Matmul)      // 注册中间结构体

12. BEGIN_TILING_DATA_DEF(AddCustomTilingData)        // 注册一个tiling类，以tiling的名字作为入参
13. TILING_DATA_FIELD_DEF(uint32_t, blkDim);        // 添加tiling变量类型字段，参与计算核数
14. TILING_DATA_FIELD_DEF(uint32_t, totalSize);     // 添加tiling变量类型字段，总计算数据量
15. TILING_DATA_FIELD_DEF(uint32_t, splitTile);     // 添加tiling变量类型字段，每个core处理的数据分块计算
16. TILING_DATA_FIELD_DEF_ARR(uint16_t, 3, arrSample);    // 添加tiling数组类型字段
17. TILING_DATA_FIELD_DEF_STRUCT(Matmul, mm);             // 添加tiling结构体类型字段
18. END_TILING_DATA_DEF;                                    // 定义结束
19. // 注册算子tilingdata类到对应的AddCustom算子
20. REGISTER_TILING_DATA_CLASS(AddCustom, AddCustomTilingData)
21. }

23. // host侧设置参数值和使用tiling参数
24. static void TilingAddInit(AddCustomTilingData *tiling, uint32_t blockDim)
25. {
26. // 设置参数值
27. tiling->set_blkDim(blockDim);                  // 置值通用数据类型变量blockDim
28. uint16_t arr[] = {10,2,8,2,3,4,5,2,1,2,4,4,5,};
29. tiling->set_arrSample(arr);                    // 置值通用数据类型数组变量arrSample，仅会复制arr数据的前三个数据，与TILING_DATA_FIELD_DEF_ARR中arr_size一致
30. tiling->mm.set_mmVar(1);                       // 置值嵌套结构体通用数据类型变量mmVar
31. tiling->mm.set_mmArr(arr);                     // 置值嵌套结构体通用数据类型数组mmArr

33. // 使用参数值
34. uint32_t useBlockDim = tiling->get_blkDim();    // 获取通用数据类型变量blockDim
35. uint32_t* arrPoint = tiling->get_arrSample();   // 获取通用数据类型数组变量arrSample
36. useBlockDim = tiling->mm.get_mmVar();           // 获取嵌套结构体通用数据类型变量mmVar
37. arrPoint = tiling->mm.get_mmArr();              // 获取嵌套结构体通用数据类型数组mmArr
38. }
```
