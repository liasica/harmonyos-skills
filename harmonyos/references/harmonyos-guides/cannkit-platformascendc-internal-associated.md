---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-platformascendc-internal-associated
title: 内部关联接口
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 内部关联接口
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:228fe9948d49cbc310681672db2f966feb03934b9f0a242fe9fbd23d1402863f
---

在进行算子原型注册、Tiling实现、shape推导过程中，使用到的外部开放接口中会调用到一些辅助数据结构和接口，称之为**内部关联接口**。开发者不会直接调用内部关联接口，此处仅作简单介绍。

## CTilingDataClassFactory

CTilingDataClassFactory类用于注册AscendC高阶API和开发者自定义tiling结构，通过单例实现的工厂类，在[TilingData结构注册](cannkit-tilingdata-structure-registration.md)中REGISTER\_TILING\_DATA\_CLASS中使用。

**表1** CTilingDataClassFactory成员函数

| 函数名称 | 含义 |
| --- | --- |
| GetInstance | 获取CTilingDataClassFactory类的单例。 |
| RegisterTilingData | 注册op\_type的tiling结构constructor至CTilingDataClassFactory工厂类。 |
| CreateTilingDataInstance | 根据算子名获取tiling结构。 |

## OpDef相关接口

原型注册相关类的一些非对外开放接口，包括OpDef、OpParamDef、OpAICoreConfig等，下述接口均为框架生成相关工程所需，开发者无需关心。

**表2** OpDef相关类及其成员函数

| 类名 | 接口名 | 接口功能 |
| --- | --- | --- |
| OpAICoreDef | GetTiling | 获取Tiling信息。 |
| OpDef | GetInferShape | 获取Shape推导函数。 |
| OpDef | GetInferDataType | 获取DataType推导函数。 |
| OpDefFactory | OpDefRegister | 注册算子。 |

## Tiling定义辅助接口

以下接口为Tiling定义辅助接口。AscendC提供了一系列Tiling类型定义宏，包含BEGIN\_TILING\_DATA\_DEF、TILING\_DATA\_FIELD\_DEF、TILING\_DATA\_FIELD\_DEF\_ARR、TILING\_DATA\_FIELD\_DEF\_STRUCT、REGISTER\_TILING\_DATA\_CLASS。开发者调用该系列宏会调用以下接口对tiling信息进一步处理，包含结构信息保留、字节对齐等。

```
1. // TilingDef类
2. void SaveToBuffer(void *pdata, size_t capacity);
3. std::vector<FieldInfo> GetFieldInfo() const;
4. const char *GetTilingClassName() const;
5. size_t GetDataSize() const;
6. void SetDataPtr(void *dataPtr);
7. void CheckAlignAndGenPlaceHolder(const char *name, size_t typeSize);
8. // FieldInfo类
9. FieldInfo(const char *dtype, const char *name)
10. FieldInfo(const char *dtype, const char *name, size_t arrSize)
11. FieldInfo(const char *dtype, const char *name, const char *structType,size_t structSize)
```
