---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tilingdata-structure-registration
title: TilingData结构注册
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > Tiling数据结构注册 > TilingData结构注册
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e50baafca67c1e0b8e0c14253eeb66ddcc7ac77b603f2ec3ddc5e5cddd8589dc
---

## 函数功能

注册定义的TilingData结构体并和自定义算子绑定。具体使用说明请参考[调用示例](cannkit-tilingdata-structure-registration.md#调用示例)。

## 函数原型

```
1. REGISTER_TILING_DATA_CLASS(op_type, class_name)
2. #define REGISTER_TILING_DATA_CLASS(op_type, class_name)
3. class op_type##class_name##Helper {
4. public:
5. op_type##class_name##Helper() {
6. CTilingDataClassFactory::RegisterTilingData(#op_type, op_type##class_name##Helper::CreateTilingDataInstance);
7. }
8. static std::shared_ptr<TilingDef> CreateTilingDataInstance() {
9. return std::make_shared<class_name>();
10. }
11. };
12. op_type##class_name##Helper g_tilingdata_##op_type##class_name##helper;
```

## 参数说明

**表1** 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| op\_type | 输入 | 注册的算子名。 |
| class\_name | 输入 | tiling结构体名，与c++变量命名要求一致。 |

## 约束说明

* 使用时需要包含头文件register/tilingdata\_base.h。
* 中间结构体和定制tilingkey结构体需注意op\_type命名规则，具体见[调用示例](cannkit-tilingdata-structure-registration.md#调用示例)。
* 算子定制tilingkey结构体需保证必须注册op\_type默认结构体。
* tiling结构体是全局属性，需注意应通过结构体名作为全局唯一标记，不同算子若注册同名不同结构tiling结构体则会发生未定义行为。

## 调用示例

* 注册算子Tiling结构体

  ```
  1. #include "register/tilingdata_base.h"

  3. // 定义tilingdata类
  4. namespace optiling {
  5. BEGIN_TILING_DATA_DEF(AddCustomTilingData)    // 注册一个tiling的类，以tiling的名字作为入参
  6. TILING_DATA_FIELD_DEF(uint32_t, blkDim);    // 添加tiling字段，参与计算核数
  7. TILING_DATA_FIELD_DEF(uint32_t, totalSize); // 添加tiling字段，总计算数据量-输入shape大小
  8. TILING_DATA_FIELD_DEF(uint32_t, splitTile); // 添加tiling字段，每个core处理的数据分块计算
  9. END_TILING_DATA_DEF;                          // 定义结束
  10. // 注册算子tilingdata类到对应的AddCustom算子
  11. REGISTER_TILING_DATA_CLASS(AddCustom, AddCustomTilingData)
  12. }
  ```
* 注册中间结构体。当开发者有结构体嵌套场景时，嵌套的结构体称为中间结构体。因为一个算子名只能注册一个Tiling结构体，为使得框架能够检测中间结构体信息，需要构造"虚拟算子名"（结构体名+Op）并通过REGISTER\_TILING\_DATA\_CLASS接口注册中间结构体，注册方式如下。

  ```
  1. BEGIN_TILING_DATA_DEF(Matmul)
  2. TILING_DATA_FIELD_DEF(uint16_t, mmVar);
  3. TILING_DATA_FIELD_DEF_ARR(uint16_t, 3, mmArr);
  4. END_TILING_DATA_DEF;
  5. // 注册中间结构体，第一个参数固定为struct_name#Op，第二个参数即struct_name, 如struct_name为Matmul，第一参数为MatmulOp，第二个参数为Matmul
  6. REGISTER_TILING_DATA_CLASS(MatmulOp, Matmul)      // 注册中间结构体
  ```
* 定制tiling\_key注册不同Tiling结构体

  ```
  1. // REGISTER_TILING_DATA_CLASS中第一个参数为${op_type} + ‘_’ + tiling_key。若tiling_key未注册匹配的tiling结构体，则会使用默认的结构体。如下面两种方式，tiling_key不指定或者非1情况，tiling结构体为AddStruct；tiling_key等于1的时候，tiling结构体为AddStructSample1

  3. // 以op_type为Add为例，默认tiling结构体注册如下
  4. BEGIN_TILING_DATA_DEF(AddStruct)
  5. TILING_DATA_FIELD_DEF(uint16_t, mmVar);
  6. TILING_DATA_FIELD_DEF_ARR(uint16_t, 3, mmArr);
  7. END_TILING_DATA_DEF;
  8. REGISTER_TILING_DATA_CLASS(Add, AddStruct)

  10. // TilingKey等于1时注册结构体如下
  11. BEGIN_TILING_DATA_DEF(AddStructSample1)
  12. TILING_DATA_FIELD_DEF(uint16_t, mmVar);
  13. TILING_DATA_FIELD_DEF_ARR(uint16_t, 3, mmArr);
  14. END_TILING_DATA_DEF;
  15. REGISTER_TILING_DATA_CLASS(Add_1, AddStructSample1)
  ```
