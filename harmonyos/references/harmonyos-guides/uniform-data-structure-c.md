---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uniform-data-structure-c
title: 标准化数据结构 (C/C++)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 标准化数据定义 > 标准化数据结构 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f07c725c488e4cde7c65dd6e259f368e3768254a7725ed1497c074d86710301f
---

## 场景介绍

针对[UTD标准化数据类型](../harmonyos-references/capi-utd-h.md)中的部分常见类型，为了方便业务使用，提供了标准化数据结构。例如，系统定义的桌面图标类型（标准化数据类型标识为'OH\_UdsAppItem'）明确定义了相关描述信息。

某些业务场景下应用可以直接使用我们具体定义的UTD标准化数据结构，例如跨应用拖拽场景。拖出方应用可以按照标准化数据结构将拖拽数据写入[拖拽事件](ndk-drag-event.md)，拖入方应用从拖拽事件中读取拖拽数据并按照标准化数据结构进行数据的解析。这使得不同应用间的数据交互遵从相同的标准定义，有效减少了跨应用数据交互的开发工作量。

## 基本概念

* **标准化数据结构**：Unified Data Structure，简称UDS。主要针对部分标准化数据类型定义了统一的数据内容结构，并明确了对应的描述信息。应用间使用标准化数据结构进行数据交互后，将遵从统一的解析标准，可有效减少适配相关的工作量。一般用于跨应用跨设备间的数据交互，比如拖拽。

## 接口说明

详细的接口说明请参考[标准化数据结构相关接口](../harmonyos-references/capi-uds-h.md)。

| 接口名称 | 描述 |
| --- | --- |
| OH\_UdmfData\* OH\_UdmfData\_Create() | 创建统一数据对象指针及实例对象 |
| OH\_UdmfRecord\* OH\_UdmfRecord\_Create() | 创建统一数据记录指针及实例对象 |
| OH\_UdsPlainText\* OH\_UdsPlainText\_Create() | 创建纯文本类型指针及实例对象 |
| int OH\_UdmfRecord\_GetPlainText(OH\_UdmfRecord\* pThis, OH\_UdsPlainText\* plainText) | 从统一数据记录中获取纯文本类型 |
| int OH\_UdsPlainText\_SetContent(OH\_UdsPlainText\* pThis, const char\* content) | 设置纯文本类型中的纯文本内容参数 |
| int OH\_UdmfRecord\_AddPlainText(OH\_UdmfRecord\* pThis, OH\_UdsPlainText\* plainText) | 添加纯文本类型数据至统一数据记录中 |
| int OH\_UdmfData\_AddRecord(OH\_UdmfData\* pThis, OH\_UdmfRecord\* record) | 添加一个数据记录到统一数据对象中 |
| OH\_UdsFileUri\* OH\_UdsFileUri\_Create() | 创建文件Uri类型指针及实例对象 |
| int OH\_UdsFileUri\_SetFileUri(OH\_UdsFileUri\* pThis, const char\* fileUri) | 设置文件Uri类型对象的Uri信息 |
| int OH\_UdsFileUri\_SetFileType(OH\_UdsFileUri\* pThis, const char\* fileType) | 设置文件Uri类型对象的文件类型 |
| int OH\_UdmfRecord\_AddFileUri(OH\_UdmfRecord\* pThis, OH\_UdsFileUri\* fileUri) | 增加文件Uri类型数据至统一数据记录中 |
| int OH\_Udmf\_SetUnifiedData(Udmf\_Intention intention, OH\_UdmfData\* unifiedData,char\* key, unsigned int keyLen) | 从统一数据管理框架数据库中写入统一数据对象数据 |
| void OH\_UdsPlainText\_Destroy(OH\_UdsPlainText\* pThis) | 销毁纯文本类型数据指针指向的实例对象 |
| void OH\_UdmfData\_Destroy(OH\_UdmfData\* pThis) | 销毁统一数据对象指针指向的实例对象 |
| void OH\_UdsFileUri\_Destroy(OH\_UdsFileUri\* pThis) | 销毁文件Uri类型的实例对象 |

## 添加动态链接库

CMakeLists.txt中添加以下库。

```
1. libudmf.so, libhilog_ndk.z.so
```

## 引用头文件

```
1. #include <database/udmf/uds.h>
2. #include <database/udmf/udmf.h>
3. #include <database/udmf/udmf_meta.h>
4. #include <hilog/log.h>

6. #undef LOG_TAG
7. #define LOG_TAG "MY_LOG"
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/UniformDataStructure_C/entry/src/main/cpp/napi_init.cpp#L18-L26)

## 纯文本类型数据结构的使用

1. 创建PlainText对象指针。
2. 添加PlainText内容。
3. 获取数据。
4. 使用完成后销毁指针。

```
1. // 1.创建PlainText对象指针
2. OH_UdmfRecord *plainTextRecord = OH_UdmfRecord_Create();
3. OH_UdsPlainText *plainText = OH_UdsPlainText_Create();
4. char content[] = "hello world";

6. // 2.添加PlainText内容
7. OH_UdsPlainText_SetContent(plainText, content);
8. OH_UdmfRecord_AddPlainText(plainTextRecord, plainText);

10. // 3.获取PlainText数据
11. OH_UdsPlainText *plainText2 = OH_UdsPlainText_Create();
12. OH_UdmfRecord_GetPlainText(plainTextRecord, plainText2);
13. const char *content2 = OH_UdsPlainText_GetContent(plainText2);

15. OH_LOG_INFO(LOG_APP, "content = %{public}s.", content2);
16. // 4.使用完成后销毁指针。
17. OH_UdsPlainText_Destroy(plainText);
18. OH_UdmfRecord_Destroy(plainTextRecord);
19. OH_UdsPlainText_Destroy(plainText2);
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/UniformDataStructure_C/entry/src/main/cpp/napi_init.cpp#L30-L50)

## fileUri类型的数据结构的使用

1. 创建fileUri类型的数据结构。
2. 设置fileUri中的URL和描述信息。
3. 创建OH\_UdmfRecord对象，并向OH\_UdmfRecord中添加fileUri类型数据。
4. 获取fileUri数据。
5. 使用完成后销毁指针。

```
1. // 1.创建fileUri类型的数据结构
2. const char *uri = "https://xxx/xx/xx.jpg";
3. OH_UdsFileUri *fileUri = OH_UdsFileUri_Create();
4. // 2. 设置fileUri中的URL和描述信息。
5. OH_UdsFileUri_SetFileUri(fileUri, uri);
6. OH_UdsFileUri_SetFileType(fileUri, UDMF_META_IMAGE);
7. // 3. 创建OH_UdmfRecord对象，并向OH_UdmfRecord中添加fileUri类型数据。
8. OH_UdmfRecord *record = OH_UdmfRecord_Create();
9. OH_UdmfRecord_AddFileUri(record, fileUri);
10. // 4. 获取fileUri数据。
11. OH_UdsFileUri *fileUri1 = OH_UdsFileUri_Create();
12. OH_UdmfRecord_GetFileUri(record, fileUri1);
13. const char *fileUriStr = OH_UdsFileUri_GetFileUri(fileUri1);
14. OH_LOG_INFO(LOG_APP, "fileUri1 = %{public}s.", fileUriStr);
15. // 5. 使用完成后销毁指针。
16. OH_UdsFileUri_Destroy(fileUri);
17. OH_UdmfRecord_Destroy(record);
18. OH_UdsFileUri_Destroy(fileUri1);
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/UniformDataStructure_C/entry/src/main/cpp/napi_init.cpp#L58-L77)
