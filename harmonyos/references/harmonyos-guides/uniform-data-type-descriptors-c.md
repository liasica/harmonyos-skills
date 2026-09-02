---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uniform-data-type-descriptors-c
title: 标准化数据类型 (C/C++)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 标准化数据定义 > 标准化数据类型 (C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b181c9faf77a85a498323a8bf87562a5ca473e83e211b7d11afb147079756031
---

## 场景介绍

统一数据管理框架（UDMF）提供数据跨应用、跨设备交互标准，定义数据交互过程中的数据语言，提升数据交互效率。它提供安全、标准化的数据流通路径，支持不同级别的数据访问权限和生命周期管理策略，实现高效的数据共享。

## 基本概念

* **标准化数据类型**：Uniform Type Descriptor，简称UTD。主要针对同一种数据类型，提供统一定义，即标准数据类型描述符，定义了包括标识数据类型的ID、类型归属关系等相关信息，用于解决HarmonyOS系统中的类型模糊问题。一般用于过滤或者识别某一种数据类型的场景，比如文件预览、文件分享等。

## 接口说明

详细的接口说明请参考UTD接口文档[utd.h](../harmonyos-references/capi-utd-h.md)。

| 接口名称 | 描述 |
| --- | --- |
| OH\_Utd\* OH\_Utd\_Create(const char\* typeId) | 创建一个指向统一数据类型描述符OH\_Utd的指针。 |
| void OH\_Utd\_Destroy(OH\_Utd\* pThis) | 销毁指向统一数据类型描述符OH\_Utd的指针。 |
| const char\*\* OH\_Utd\_GetTypesByFilenameExtension(const char\* extension, unsigned int\* count) | 通过文件后缀名获取标准化数据类型ID。 |
| const char\*\* OH\_Utd\_GetTypesByMimeType(const char\* mimeType, unsigned int\* count) | 通过MIME类型获取标准化数据类型ID。 |
| bool OH\_Utd\_Equals(OH\_Utd\* utd1, OH\_Utd\* utd2) | 判断两个标准化数据类型是否相等。 |
| void OH\_Utd\_DestroyStringList(const char\*\* list, unsigned int count) | 销毁字符串列表数据。 |
| bool OH\_Utd\_BelongsTo (const char \*srcTypeId, const char \*destTypeId) | 判断两个标准化数据类型是否存在归属关系。 |
| bool OH\_Utd\_IsLower (const char\* srcTypeId, const char\* destTypeId ) | 判断原标准化数据类型是否是目标标准化数据类型的低层级类型。 例如TYPE\_SCRIPT为SOURCE\_CODE的低层级类型，TYPE\_SCRIPT和SOURCE\_CODE为PLAIN\_TEXT的低层级类型。 |
| bool OH\_Utd\_IsHigher (const char\* srcTypeId, const char\* destTypeId ) | 判断原标准化数据类型是否是目标标准化数据类型的高层级类型。 例如SOURCE\_CODE为TYPE\_SCRIPT的高层级类型，PLAIN\_TEXT为SOURCE\_CODE和TYPE\_SCRIPT的高层级类型。 |

## 添加动态链接库

CMakeLists.txt中添加以下库。

```txt
libudmf.so, libhilog_ndk.z.so
```

## 引用头文件

```
#include <cstdio>
#include <cstring>
#include <database/udmf/utd.h>
#include <database/udmf/uds.h>
#include <database/udmf/udmf.h>
#include <database/udmf/udmf_meta.h>
#include <database/udmf/udmf_err_code.h>
#include <hilog/log.h>

#undef LOG_TAG
#define LOG_TAG "MY_LOG"
```

## 通过不同方式获取不同类型数据并且比较它们之间的关系

下面以获取纯文本数据的查询场景为例，说明如何使用UTD。

1. 通过后缀名“.txt”获取UTD的typeId。
2. 通过MIME类型“text/plain”获取UTD的typeId。
3. 使用以上两个步骤获取到的typeId创建UTD实例对象。
4. 比较UTD实例对象是否相等。
5. 比较两种方式获取到的typeId是否存在归属关系。
6. 比较两种方式获取到的typeIds1[0]是否是typeIds2[0]的低层级类型。
7. 比较两种方式获取到的typeIds1[0]是否是typeIds2[0]的高层级类型。
8. 使用结束后，删除上述步骤中产生的指针。

```
// 1. 通过文件后缀名获取纯文本类型的UTD的typeId
unsigned int typeIds1Count = 0;
const char **typeIds1 = OH_Utd_GetTypesByFilenameExtension(".txt", &typeIds1Count);
OH_LOG_INFO(LOG_APP, "the count of typeIds1 is %{public}u", typeIds1Count);
// 2. 通过MIME类型获取typeId
unsigned int typeIds2Count = 0;
const char **typeIds2 = OH_Utd_GetTypesByMimeType("text/plain", &typeIds2Count);
OH_LOG_INFO(LOG_APP, "the count of typeIds2 is %{public}u", typeIds2Count);
// 3. 使用以上两个步骤获取到的typeId创建UTD实例对象。
OH_Utd *utd1 = OH_Utd_Create(typeIds1[0]);
OH_Utd *utd2 = OH_Utd_Create(typeIds2[0]);
// 4. 比较两种方式获取到的typeId对应的UTD是否相同
bool isEquals = OH_Utd_Equals(utd1, utd2);
if (isEquals) {
    OH_LOG_INFO(LOG_APP, "utd1 == utd2");
} else {
    OH_LOG_INFO(LOG_APP, "utd1 != utd2");
}
// 5. 比较两种方式获取到的typeId是否存在归属关系
bool isBelongsTo = OH_Utd_BelongsTo(typeIds1[0], typeIds2[0]);
if (isBelongsTo) {
    OH_LOG_INFO(LOG_APP, "typeIds1[0] belongs to typeIds2[0]");
} else {
    OH_LOG_INFO(LOG_APP, "typeIds1[0] doesn't belong to typeIds2[0]");
}
// 6. 比较两种方式获取到的typeIds1[0]是否是typeIds2[0]的低层级类型
bool isLower = OH_Utd_IsLower(typeIds1[0], typeIds2[0]);
if (isLower) {
    OH_LOG_INFO(LOG_APP, "typeIds1[0] is lower typeIds2[0]");
} else {
    OH_LOG_INFO(LOG_APP, "typeIds1[0] is not lower typeIds2[0]");
}
// 7. 比较两种方式获取到的typeIds1[0]是否是typeIds2[0]的高层级类型
bool isHigher = OH_Utd_IsHigher(typeIds1[0], typeIds2[0]);
if (isHigher) {
    OH_LOG_INFO(LOG_APP, "typeIds1[0] is higher typeIds2[0]");
} else {
    OH_LOG_INFO(LOG_APP, "typeIds1[0] is not higher typeIds2[0]");
}
// 8. 销毁OH_Utd_GetTypesByFilenameExtension与OH_Utd_GetTypesByMimeType函数获取到的指针，同时销毁UTD指针
OH_Utd_DestroyStringList(typeIds1, typeIds1Count);
OH_Utd_DestroyStringList(typeIds2, typeIds2Count);
OH_Utd_Destroy(utd1);
OH_Utd_Destroy(utd2);
```
