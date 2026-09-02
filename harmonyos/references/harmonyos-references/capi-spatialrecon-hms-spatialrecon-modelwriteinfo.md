---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-spatialrecon-hms-spatialrecon-modelwriteinfo
title: HMS_SpatialRecon_ModelWriteInfo
breadcrumb: API参考 > 图形 > Spatial Recon Kit（空间建模服务） > C API > 头文件和结构体 > 结构体 > HMS_SpatialRecon_ModelWriteInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:af026300e6cc7197153fad48da542edf11d55d1b63ae393a177b3cd935e57e82
---

```c
typedef struct HMS_SpatialRecon_ModelWriteInfo {...} HMS_SpatialRecon_ModelWriteInfo
```

## 概述

空间重建模型写入的结构体。

**起始版本：** 6.1.0(23)

**相关模块：** [SpatialRecon](capi-spatialrecon.md)

**所在头文件：** [spatial\_recon\_interface.h](capi-spatial-recon-interface-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float longitude = 0.0 | 用于地理定位参考的经度坐标（十进制度）。正值表示东经，负值表示西经。取值范围：[-180, 180]。 |
| float latitude = 0.0 | 用于地理定位参考的纬度坐标（十进制度）。正值表示北纬，负值表示南纬。取值范围：[-90, 90]。 |
| const char \*audioFile = nullptr | 与空间重建关联的可选音频文件路径，需要以.mp3 结尾。如果没有可用的音频数据或不需要音频数据，可以为nullptr。 |
| const char\* modelFile | 存储空间重建模型的输出文件名。为必填字段。必须是应用文件目录的子目录。 |
| HMS\_SpatialReconOutputFormat modelFormat | 空间重建模型的输出格式。指定生成模型的文件格式和结构。 |
