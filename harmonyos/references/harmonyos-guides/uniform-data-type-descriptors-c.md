---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uniform-data-type-descriptors-c
title: 标准化数据类型 (C/C++)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 标准化数据定义 > 标准化数据类型 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e0994bbc04f379976ee9f4059a2968751cdca94cdb41440d9686ca1d1ab3da5a
---

## 场景介绍

统一数据管理框架（UDMF）提供数据跨应用、跨设备交互标准，定义数据交互过程中的数据语言，提升数据交互效率。它提供安全、标准化的数据流通路径，支持不同级别的数据访问权限和生命周期管理策略，实现高效的数据共享。

## 基本概念

* **标准化数据类型**：Uniform Type Descriptor，简称UTD。主要针对同一种数据类型，提供统一定义，即标准数据类型描述符，定义了包括标识数据类型的ID、类型归属关系等相关信息，用于解决HarmonyOS系统中的类型模糊问题。一般用于过滤或者识别某一种数据类型的场景，比如文件预览、文件分享等。

## 接口说明

详细的接口说明请参考[UTD接口文档](../harmonyos-references/capi-utd-h.md)。

| 接口名称 | 描述 |
| --- | --- |
| OH\_Utd\* OH\_Utd\_Create(const char\* typeId) | 创建一个指向统一数据类型描述符OH\_Utd的指针。 |
| void OH\_Utd\_Destroy(OH\_Utd\* pThis) | 销毁指向统一数据类型描述符OH\_Utd的指针。 |
| const char\*\* OH\_Utd\_GetTypesByFilenameExtension(const char\* extension, unsigned int\* count) | 通过文件后缀名获取标准化数据类型ID。 |
| const char\*\* OH\_Utd\_GetTypesByMimeType(const char\* mimeType, unsigned int\* count) | 通过MIME类型获取标准化数据类型ID。 |
| bool OH\_Utd\_Equals(OH\_Utd\* utd1, OH\_Utd\* utd2) | 判断两种标准化数据类型是否相等。 |
| void OH\_Utd\_DestroyStringList(const char\*\* list, unsigned int count) | 销毁字符串列表数据。 |
| bool OH\_Utd\_BelongsTo (const char \*srcTypeId, const char \*destTypeId) | 判断两个标准化数据描述类型是否存在归属关系。 |
| bool OH\_Utd\_IsLower (const char\* srcTypeId, const char\* destTypeId ) | 判断原标准化数据类型是否是目标标准化数据类型的低层级类型。 例如TYPE\_SCRIPT为SOURCE\_CODE的低层级类型，TYPE\_SCRIPT和SOURCE\_CODE为PLAIN\_TEXT的低层级类型。 |
| bool OH\_Utd\_IsHigher (const char\* srcTypeId, const char\* destTypeId ) | 判断原标准化数据类型是否是目标标准化数据类型的高层级类型。 例如SOURCE\_CODE为TYPE\_SCRIPT的高层级类型，PLAIN\_TEXT为SOURCE\_CODE和TYPE\_SCRIPT的高层级类型。 |

## 添加动态链接库

CMakeLists.txt中添加以下库。

```
1. libudmf.so, libhilog_ndk.z.so
```

## 引用头文件

```
1. #include <cstdio>
2. #include <cstring>
3. #include <database/udmf/utd.h>
4. #include <database/udmf/uds.h>
5. #include <database/udmf/udmf.h>
6. #include <database/udmf/udmf_meta.h>
7. #include <database/udmf/udmf_err_code.h>
8. #include <hilog/log.h>

10. #undef LOG_TAG
11. #define LOG_TAG "MY_LOG"
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/UniformDataTypeDescriptors_C/entry/src/main/cpp/napi_init.cpp#L16-L28)

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
1. // 1. 通过文件后缀名获取纯文本类型的UTD的typeId
2. unsigned int typeIds1Count = 0;
3. const char **typeIds1 = OH_Utd_GetTypesByFilenameExtension(".txt", &typeIds1Count);
4. OH_LOG_INFO(LOG_APP, "the count of typeIds1 is %{public}u", typeIds1Count);
5. // 2. 通过MIME类型获取typeId
6. unsigned int typeIds2Count = 0;
7. const char **typeIds2 = OH_Utd_GetTypesByMimeType("text/plain", &typeIds2Count);
8. OH_LOG_INFO(LOG_APP, "the count of typeIds2 is %{public}u", typeIds2Count);
9. // 3. 使用以上两个步骤获取到的typeId创建UTD实例对象。
10. OH_Utd *utd1 = OH_Utd_Create(typeIds1[0]);
11. OH_Utd *utd2 = OH_Utd_Create(typeIds2[0]);
12. // 4. 比较两种方式获取到的typeId对应的UTD是否相同
13. bool isEquals = OH_Utd_Equals(utd1, utd2);
14. if (isEquals) {
15. OH_LOG_INFO(LOG_APP, "utd1 == utd2");
16. } else {
17. OH_LOG_INFO(LOG_APP, "utd1 != utd2");
18. }
19. // 5. 比较两种方式获取到的typeId是否存在归属关系
20. bool isBelongsTo = OH_Utd_BelongsTo(typeIds1[0], typeIds2[0]);
21. if (isBelongsTo) {
22. OH_LOG_INFO(LOG_APP, "typeIds1[0] belongs to typeIds2[0]");
23. } else {
24. OH_LOG_INFO(LOG_APP, "typeIds1[0] doesn't belong to typeIds2[0]");
25. }
26. // 6. 比较两种方式获取到的typeIds1[0]是否是typeIds2[0]的低层级类型
27. bool isLower = OH_Utd_IsLower(typeIds1[0], typeIds2[0]);
28. if (isLower) {
29. OH_LOG_INFO(LOG_APP, "typeIds1[0] is lower typeIds2[0]");
30. } else {
31. OH_LOG_INFO(LOG_APP, "typeIds1[0] is not lower typeIds2[0]");
32. }
33. // 7. 比较两种方式获取到的typeIds1[0]是否是typeIds2[0]的高层级类型
34. bool isHigher = OH_Utd_IsHigher(typeIds1[0], typeIds2[0]);
35. if (isHigher) {
36. OH_LOG_INFO(LOG_APP, "typeIds1[0] is higher typeIds2[0]");
37. } else {
38. OH_LOG_INFO(LOG_APP, "typeIds1[0] is not higher typeIds2[0]");
39. }
40. // 8. 销毁OH_Utd_GetTypesByFilenameExtension与OH_Utd_GetTypesByMimeType函数获取到的指针，同时销毁UTD指针
41. OH_Utd_DestroyStringList(typeIds1, typeIds1Count);
42. OH_Utd_DestroyStringList(typeIds2, typeIds2Count);
43. OH_Utd_Destroy(utd1);
44. OH_Utd_Destroy(utd2);
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/UniformDataTypeDescriptors_C/entry/src/main/cpp/napi_init.cpp#L32-L77)
