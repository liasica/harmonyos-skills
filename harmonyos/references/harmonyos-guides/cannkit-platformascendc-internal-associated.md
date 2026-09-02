---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-platformascendc-internal-associated
title: 内部关联接口
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 内部关联接口
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d8a5ccb4961360ca7e133e81ba266e1303047f559e40631f6c6b5caac3c3e2c1
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

```cpp
// TilingDef类
void SaveToBuffer(void *pdata, size_t capacity);
std::vector<FieldInfo> GetFieldInfo() const;
const char *GetTilingClassName() const;
size_t GetDataSize() const;
void SetDataPtr(void *dataPtr);
void CheckAlignAndGenPlaceHolder(const char *name, size_t typeSize);
// FieldInfo类
FieldInfo(const char *dtype, const char *name)
FieldInfo(const char *dtype, const char *name, size_t arrSize)
FieldInfo(const char *dtype, const char *name, const char *structType,size_t structSize)
```
