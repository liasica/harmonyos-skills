---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/unified-data-channels-c
title: 通过标准化数据通路实现数据共享 (C/C++)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 跨应用数据共享 > 多对多跨应用数据共享 > 通过标准化数据通路实现数据共享 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c26a3990979a0c34d2e04efe4fb0073fe872e3519e5fb5ce457ee750005db17e
---

## 场景介绍

在多对多跨应用数据共享的场景下，需要提供一条数据通路，能够写入多个不同应用的数据，并共享给其他应用进行读取。

UDMF针对多对多跨应用数据共享的不同业务场景，提供了标准化的数据通路和数据写入与读取接口。

## 标准化数据通路的定义和实现

标准化数据通路是为各种业务场景提供的跨应用数据写入与读取通路。它能够暂存应用需要共享的、符合标准化数据定义的统一数据对象，并提供给其他应用访问。同时，它按照一定策略对暂存数据的修改、删除权限及生命周期进行管理。

标准化数据通路通过UDMF提供的系统服务实现。应用（数据提供方）需要共享公共数据时，可以通过UDMF提供的插入接口将数据写入UDMF的数据通路中，并且可以通过UDMF提供的更新和删除接口对已存入的数据进行更新和删除操作。目标应用（数据访问方）可以通过UDMF提供的读取接口访问数据。

标准化数据通路相关接口应不推荐多线程调用。

统一数据对象UnifiedData在UDMF数据通路中具有全局唯一URI标识，其定义为udmf://intention/bundleName/groupId，其中各组成部分的含义分别为：

* **udmf:** 协议名，表示使用UDMF提供的数据通路。
* **intention:** UDMF已经支持的数据通路类型枚举值，对应不同的业务场景。
* **bundleName:** 数据来源应用的包名称。
* **groupId:** 分组名称，支持批量数据分组管理。

当前UDMF中的跨应用数据共享通路有：**公共数据通路**

**公共数据通路**：应用共享的公用数据通路，所有应用均可向通路中写入数据。写入方可以根据写入数据时生成的数据唯一标识符进行数据的更新、删除、查询指定数据标识符或全量查询。数据读取方可以通过唯一标识符读取指定数据，也可以设置Intention枚举类型为DATA\_HUB来读取当前数据通路中的全量数据。公共数据通路仅用于传输应用间的过程数据，不能用于传输沙箱目录下文件等有权限管控的数据。UDMF会统一对数据的生命周期进行管理，每小时定期清理存入时长超过一小时的数据。

## 接口说明

详细的接口说明请参考[UDMF接口文档](../harmonyos-references/capi-udmf-h.md)。

| 接口名称 | 描述 |
| --- | --- |
| OH\_UdsHyperlink\* OH\_UdsHyperlink\_Create() | 创建超链接类型对象的指针。 |
| int OH\_UdsHyperlink\_SetDescription(OH\_UdsHyperlink\* pThis, const char\* description) | 设置超链接类型实例中的描述参数。 |
| OH\_UdmfRecord\* OH\_UdmfRecord\_Create() | 创建一个指向统一数据记录OH\_UdmfRecord的指针。 |
| int OH\_UdmfRecord\_AddHyperlink(OH\_UdmfRecord\* pThis, OH\_UdsHyperlink\* hyperlink) | 向OH\_UdmfRecord添加超链接类型数据。 |
| OH\_UdmfData\* OH\_UdmfData\_Create() | 创建一个指向统一数据对象OH\_UdmfData的指针。 |
| int OH\_UdmfData\_AddRecord(OH\_UdmfData\* pThis, OH\_UdmfRecord\* record) | 向OH\_UdmfData中增加一条OH\_UdmfRecord数据记录。 |
| int OH\_Udmf\_SetUnifiedDataByOptions(OH\_UdmfOptions\* options, OH\_UdmfData \*unifiedData, char \*key, unsigned int keyLen) | 从统一数据管理框架数据库中写入统一数据对象OH\_UdmfData数据。 |
| void OH\_UdsHyperlink\_Destroy(OH\_UdsHyperlink\* pThis) | 销毁超链接类型指针指向的实例对象。 |
| void OH\_UdmfRecord\_Destroy(OH\_UdmfRecord\* pThis) | 销毁指向统一数据记录OH\_UdmfRecord的指针。 |
| void OH\_UdmfData\_Destroy(OH\_UdmfData\* pThis) | 销毁指向统一数据对象OH\_UdmfData的指针。 |
| char\*\* OH\_UdmfRecord\_GetTypes(OH\_UdmfRecord\* pThis, unsigned int\* count) | 获取OH\_UdmfRecord中全部的数据类型。 |
| int OH\_UdmfRecord\_GetHyperlink(OH\_UdmfRecord\* pThis, OH\_UdsHyperlink\* hyperlink) | 获取OH\_UdmfRecord中超链接类型数据。 |
| int OH\_Udmf\_GetUnifiedDataByOptions(OH\_UdmfOptions\* options, OH\_UdmfData\*\* dataArray, unsigned int\* dataSize) | 通过数据通路类型从统一数据管理框架数据库中获取统一数据对象数据。 |
| int OH\_Udmf\_UpdateUnifiedData(OH\_UdmfOptions\* options, OH\_UdmfData\* unifiedData) | 对统一数据管理框架数据库中的统一数据对象数据进行数据更改。 |
| int OH\_Udmf\_DeleteUnifiedData(OH\_UdmfOptions\* options, OH\_UdmfData\*\* dataArray, unsigned int\* dataSize) | 删除统一数据管理框架数据库中的统一数据对象数据。 |
| bool OH\_UdmfData\_HasType(OH\_UdmfData\* pThis, const char\* type) | 判断统一数据对象OH\_UdmfData是否存在指定类型。 |
| OH\_UdmfRecord\*\* OH\_UdmfData\_GetRecords(OH\_UdmfData\* pThis, unsigned int\* count) | 获取OH\_UdmfData中全部的数据记录。 |
| OH\_UdmfRecordProvider\* OH\_UdmfRecordProvider\_Create() | 创建一个指向统一数据提供者的指针。 |
| int OH\_UdmfRecordProvider\_SetData(OH\_UdmfRecordProvider\* provider, void\* context, const OH\_UdmfRecordProvider\_GetData callback, const UdmfData\_Finalize finalize) | 设置统一数据提供者的回调函数。 |
| int OH\_UdmfRecord\_SetProvider(OH\_UdmfRecord\* pThis, const char\* const\* types, unsigned int count, OH\_UdmfRecordProvider\* provider) | 将统一数据提供者配置到OH\_UdmfRecord中。 |
| OH\_UdmfOptions\* OH\_UdmfOptions\_Create() | 创建一个指向数据操作选项的指针。 |
| void OH\_UdmfOptions\_Destroy(OH\_UdmfOptions\* pThis) | 销毁指向数据操作选项的指针。 |

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

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/UnifiedDataChannels_C/entry/src/main/cpp/napi_init.cpp#L16-L28)

## 使用UDMF写入UDS数据

下面以写入超链接OH\_UdsHyperlink类型数据场景为例，说明如何使用UDS与UDMF。

1. 创建hyperlink的UDS数据结构。
2. 设置hyperlink中的URL和描述信息。
3. 创建OH\_UdmfRecord对象，并向OH\_UdmfRecord中添加超链接类型数据。
4. 创建OH\_UdmfData对象，并向OH\_UdmfData中添加OH\_UdmfRecord。
5. 构建数据操作选项。
6. 构建数据，将数据写入数据库中，得到返回的key值。
7. 使用完成后销毁指针。

```
1. int32_t SetHyperlinkData(OH_UdsHyperlink* hyperlink, OH_UdmfRecord* record, OH_UdmfData* data)
2. {
3. // 2.设置hyperlink中的URL和描述信息。
4. int ret = OH_UdsHyperlink_SetUrl(hyperlink, "www.demo.com");
5. if (ret != Udmf_ErrCode::UDMF_E_OK) {
6. OH_LOG_ERROR(LOG_APP, "Hyperlink set url error!");
7. return ret;
8. }
9. ret = OH_UdsHyperlink_SetDescription(hyperlink, "This is the description.");
10. if (ret != Udmf_ErrCode::UDMF_E_OK) {
11. OH_LOG_ERROR(LOG_APP, "Hyperlink set description error!");
12. return ret;
13. }
14. // 3. 向OH_UdmfRecord中添加超链接类型数据。
15. ret = OH_UdmfRecord_AddHyperlink(record, hyperlink);
16. if (ret != Udmf_ErrCode::UDMF_E_OK) {
17. OH_LOG_ERROR(LOG_APP, "Add hyperlink to record error!");
18. return ret;
19. }
20. // 4. 并向OH_UdmfData中添加OH_UdmfRecord。
21. ret = OH_UdmfData_AddRecord(data, record);
22. if (ret != Udmf_ErrCode::UDMF_E_OK) {
23. OH_LOG_ERROR(LOG_APP, "Add record to data error!");
24. return ret;
25. }
26. return UDMF_E_OK;
27. }

29. int32_t CreateDataTest()
30. {
31. // 1.创建hyperlink的UDS数据结构、OH_UdmfRecord对象及OH_UdmfData对象。
32. OH_UdsHyperlink* hyperlink = OH_UdsHyperlink_Create();
33. OH_UdmfRecord* record = OH_UdmfRecord_Create();
34. OH_UdmfData* data = OH_UdmfData_Create();
35. int32_t ret = SetHyperlinkData(hyperlink, record, data);
36. if (ret != UDMF_E_OK) {
37. OH_LOG_ERROR(LOG_APP, "Create data error!");
38. OH_UdsHyperlink_Destroy(hyperlink);
39. OH_UdmfRecord_Destroy(record);
40. OH_UdmfData_Destroy(data);
41. return ret;
42. }
43. // 构建数据操作选项。
44. OH_UdmfOptions* options = OH_UdmfOptions_Create();
45. ret = OH_UdmfOptions_SetIntention(options, Udmf_Intention::UDMF_INTENTION_DATA_HUB);
46. if (ret != Udmf_ErrCode::UDMF_E_OK) {
47. OH_LOG_ERROR(LOG_APP, "Set option error!");
48. OH_UdsHyperlink_Destroy(hyperlink);
49. OH_UdmfRecord_Destroy(record);
50. OH_UdmfData_Destroy(data);
51. OH_UdmfOptions_Destroy(options);
52. return ret;
53. }
54. // 6. 构建数据，将数据写入数据库中，得到返回的key值。
55. char key[UDMF_KEY_BUFFER_LEN] = {0};
56. ret = OH_Udmf_SetUnifiedDataByOptions(options, data, key, sizeof(key));
57. if (ret != Udmf_ErrCode::UDMF_E_OK) {
58. OH_LOG_ERROR(LOG_APP, "Set data error!");
59. OH_UdsHyperlink_Destroy(hyperlink);
60. OH_UdmfRecord_Destroy(record);
61. OH_UdmfData_Destroy(data);
62. OH_UdmfOptions_Destroy(options);
63. return ret;
64. }
65. OH_LOG_INFO(LOG_APP, "key = %{public}s", key);
66. // 7. 使用完成后销毁指针。
67. OH_UdsHyperlink_Destroy(hyperlink);
68. OH_UdmfRecord_Destroy(record);
69. OH_UdmfData_Destroy(data);
70. OH_UdmfOptions_Destroy(options);
71. return UDMF_E_OK;
72. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/UnifiedDataChannels_C/entry/src/main/cpp/napi_init.cpp#L30-L103)

## 使用UDMF获取UDS数据

下面继续以获取超链接OH\_UdsHyperlink类型数据场景为例，说明如何使用UDS与UDMF。

1. 构建数据操作选项。
2. 通过数据操作选项获取数据。
3. 判断OH\_UdmfData是否有对应的类型。
4. 获取数据记录和hyperlink数据。
5. 销毁指针。

```
1. int32_t ProcessHyperlinks(OH_UdmfRecord* record, unsigned int recordTypeIdCount, char** typeIdsFromRecord)
2. {
3. for (unsigned int k = 0; k < recordTypeIdCount; k++) {
4. // 从OH_UdmfRecord中获取超链接类型数据。
5. if (strcmp(typeIdsFromRecord[k], UDMF_META_HYPERLINK) == 0) {
6. // 创建hyperlink的UDS，用来承载record中读取出来的hyperlink数据。
7. OH_UdsHyperlink* hyperlink = OH_UdsHyperlink_Create();
8. int32_t ret = OH_UdmfRecord_GetHyperlink(record, hyperlink);
9. if (ret != Udmf_ErrCode::UDMF_E_OK) {
10. OH_LOG_ERROR(LOG_APP, "Fail get hyperlink from record!");
11. return ret;
12. }
13. // 读取OH_UdsHyperlink中的各项信息。
14. OH_LOG_INFO(LOG_APP, "The hyperlink type id is : %{public}s", OH_UdsHyperlink_GetType(hyperlink));
15. OH_LOG_INFO(LOG_APP, "The hyperlink url is : %{public}s", OH_UdsHyperlink_GetUrl(hyperlink));
16. OH_LOG_INFO(LOG_APP, "The hyperlink description is : %{public}s",
17. OH_UdsHyperlink_GetDescription(hyperlink));
18. OH_UdsHyperlink_Destroy(hyperlink);
19. }
20. }
21. return UDMF_E_OK;
22. }

24. int32_t ProcessData(OH_UdmfData* data)
25. {
26. unsigned int recordsCount = 0;
27. OH_UdmfRecord** records = OH_UdmfData_GetRecords(data, &recordsCount);
28. OH_LOG_INFO(LOG_APP, "the count of records count is %{public}u", recordsCount);
29. for (unsigned int j = 0; j < recordsCount; j++) {
30. // 获取OH_UdmfRecord类型列表。
31. unsigned int recordTypeIdCount = 0;
32. char** typeIdsFromRecord = OH_UdmfRecord_GetTypes(records[j], &recordTypeIdCount);
33. int32_t ret = ProcessHyperlinks(records[j], recordTypeIdCount, typeIdsFromRecord);
34. if (ret != Udmf_ErrCode::UDMF_E_OK) {
35. OH_LOG_ERROR(LOG_APP, "ProcessRecordHyperlinks error!");
36. return ret;
37. }
38. }
39. return UDMF_E_OK;
40. }

42. int32_t HandleUdmfHyperlinkData(OH_UdmfData* readData, unsigned int dataSize, OH_UdmfData** dataArray)
43. {
44. for (unsigned int i = 0; i < dataSize; i++) {
45. OH_UdmfData* data = OH_UDMF_GetDataElementAt(dataArray, i);
46. // 3. 判断OH_UdmfData是否有对应的类型。
47. if (!OH_UdmfData_HasType(data, UDMF_META_HYPERLINK)) {
48. OH_LOG_INFO(LOG_APP, "There is no hyperlink type in data[%{public}u].", i);
49. continue;
50. }
51. // 4. 获取数据记录和hyperlink数据。
52. int32_t ret = ProcessData(data);
53. if (ret != Udmf_ErrCode::UDMF_E_OK) {
54. OH_LOG_ERROR(LOG_APP, "Process data error!");
55. return ret;
56. }
57. }
58. return UDMF_E_OK;
59. }

61. int32_t GetDataTest()
62. {
63. // 1. 构建数据操作选项。
64. OH_UdmfOptions* options = OH_UdmfOptions_Create();
65. int32_t ret = OH_UdmfOptions_SetIntention(options, Udmf_Intention::UDMF_INTENTION_DATA_HUB);
66. if (ret != Udmf_ErrCode::UDMF_E_OK) {
67. OH_LOG_ERROR(LOG_APP, "Set option error!");
68. OH_UdmfOptions_Destroy(options);
69. return ret;
70. }
71. // 2. 通过数据操作选项获取数据。
72. unsigned int dataSize = 0;
73. OH_UdmfData* readData = nullptr;
74. ret = OH_Udmf_GetUnifiedDataByOptions(options, &readData, &dataSize);
75. if (ret != Udmf_ErrCode::UDMF_E_OK) {
76. OH_LOG_ERROR(LOG_APP, "Get Data error!");
77. OH_UdmfOptions_Destroy(options);
78. return ret;
79. }
80. OH_UdmfOptions_Destroy(options);
81. OH_LOG_INFO(LOG_APP, "the size of data is %{public}u", dataSize);
82. OH_UdmfData** dataArray = &readData;
83. ret = HandleUdmfHyperlinkData(readData, dataSize, dataArray);
84. if (ret != Udmf_ErrCode::UDMF_E_OK) {
85. OH_LOG_ERROR(LOG_APP, "Get Data error!");
86. return ret;
87. }
88. // 5.销毁指针。
89. OH_Udmf_DestroyDataArray(dataArray, dataSize);
90. return UDMF_E_OK;
91. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/UnifiedDataChannels_C/entry/src/main/cpp/napi_init.cpp#L105-L198)

## 使用UDMF更新UDS数据

下面以更新超链接OH\_UdsHyperlink类型数据场景为例，说明如何使用UDS与UDMF。

1. 创建hyperlink的UDS数据结构。
2. 设置hyperlink中的URL和描述信息。
3. 创建OH\_UdmfRecord对象，并向OH\_UdmfRecord中添加超链接类型数据。
4. 创建OH\_UdmfData对象，并向OH\_UdmfData中添加OH\_UdmfRecord。
5. 构建数据操作选项。
6. 更新数据，将数据写入数据库中。
7. 使用完成后销毁指针。

```
1. int32_t AddHyperlinkToUdmfRecord(OH_UdsHyperlink* hyperlink, OH_UdmfRecord* record, OH_UdmfData* data)
2. {
3. // 2. 设置hyperlink中的URL和描述信息。
4. int32_t ret = OH_UdsHyperlink_SetUrl(hyperlink, "www.demo2.com");
5. if (ret != Udmf_ErrCode::UDMF_E_OK) {
6. OH_LOG_ERROR(LOG_APP, "Hyperlink set url error!");
7. return ret;
8. }
9. ret = OH_UdsHyperlink_SetDescription(hyperlink, "This is the new description.");
10. if (ret != Udmf_ErrCode::UDMF_E_OK) {
11. OH_LOG_ERROR(LOG_APP, "Hyperlink set description error!");
12. return ret;
13. }
14. // 3. 向OH_UdmfRecord中添加超链接类型数据。
15. ret = OH_UdmfRecord_AddHyperlink(record, hyperlink);
16. if (ret != Udmf_ErrCode::UDMF_E_OK) {
17. OH_LOG_ERROR(LOG_APP, "Add hyperlink to record error!");
18. return ret;
19. }
20. // 4. 向OH_UdmfData中添加OH_UdmfRecord。
21. ret = OH_UdmfData_AddRecord(data, record);
22. if (ret != Udmf_ErrCode::UDMF_E_OK) {
23. OH_LOG_ERROR(LOG_APP, "Add record to data error!");
24. return ret;
25. }
26. return UDMF_E_OK;
27. }

29. int32_t UpdateDataTest()
30. {
31. // 1.创建hyperlink的UDS数据结构、OH_UdmfRecord对象及OH_UdmfData对象。
32. OH_UdsHyperlink* hyperlink = OH_UdsHyperlink_Create();
33. OH_UdmfRecord* record = OH_UdmfRecord_Create();
34. OH_UdmfData* data = OH_UdmfData_Create();
35. int32_t ret = AddHyperlinkToUdmfRecord(hyperlink, record, data);
36. if (ret != UDMF_E_OK) {
37. OH_LOG_ERROR(LOG_APP, "Fail to create hyperlink!");
38. OH_UdsHyperlink_Destroy(hyperlink);
39. OH_UdmfRecord_Destroy(record);
40. OH_UdmfData_Destroy(data);
41. return ret;
42. }
43. // 5. 构建数据操作选项。
44. OH_UdmfOptions* options = OH_UdmfOptions_Create();
45. // 此处key为示例，不可直接使用，其值应与OH_Udmf_SetUnifiedDataByOptions接口中获取到的key值保持一致。
46. char key[] = "udmf://DataHub/com.ohos.test/0123456789";
47. ret = OH_UdmfOptions_SetIntention(options, Udmf_Intention::UDMF_INTENTION_DATA_HUB);
48. if (ret != Udmf_ErrCode::UDMF_E_OK
49. || OH_UdmfOptions_SetKey(options, key) != Udmf_ErrCode::UDMF_E_OK) {
50. OH_LOG_ERROR(LOG_APP, "Set option error!");
51. OH_UdsHyperlink_Destroy(hyperlink);
52. OH_UdmfRecord_Destroy(record);
53. OH_UdmfData_Destroy(data);
54. OH_UdmfOptions_Destroy(options);
55. return ret;
56. }
57. // 6. 更新数据，将数据写入数据库中。
58. ret = OH_Udmf_UpdateUnifiedData(options, data);
59. if (ret != Udmf_ErrCode::UDMF_E_OK) {
60. OH_LOG_ERROR(LOG_APP, "Update data error!");
61. OH_UdsHyperlink_Destroy(hyperlink);
62. OH_UdmfRecord_Destroy(record);
63. OH_UdmfData_Destroy(data);
64. OH_UdmfOptions_Destroy(options);
65. return ret;
66. }
67. OH_LOG_INFO(LOG_APP, "update data success");
68. // 7. 使用完成后销毁指针。
69. OH_UdsHyperlink_Destroy(hyperlink);
70. OH_UdmfRecord_Destroy(record);
71. OH_UdmfData_Destroy(data);
72. OH_UdmfOptions_Destroy(options);
73. return UDMF_E_OK;
74. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/UnifiedDataChannels_C/entry/src/main/cpp/napi_init.cpp#L200-L275)

## 使用UDMF删除UDS数据

下面继续以获取超链接OH\_UdsHyperlink类型数据场景为例，说明如何使用UDS与UDMF。

1. 构建数据操作选项。
2. 通过数据操作选项删除数据。
3. 判断OH\_UdmfData是否有对应的类型。
4. 获取数据记录和hyperlink数据。
5. 获取数据记录中的元素。
6. 销毁指针。

```
1. int32_t ProcessRecordHyperlinks(OH_UdmfRecord* record, unsigned int recordTypeIdCount, char** typeIdsFromRecord)
2. {
3. for (unsigned int k = 0; k < recordTypeIdCount; k++) {
4. // 从OH_UdmfRecord中获取超链接类型数据。
5. if (strcmp(typeIdsFromRecord[k], UDMF_META_HYPERLINK) == 0) {
6. // 创建hyperlink的UDS，用来承载record中读取出来的hyperlink数据。
7. OH_UdsHyperlink* hyperlink = OH_UdsHyperlink_Create();
8. int32_t ret = OH_UdmfRecord_GetHyperlink(record, hyperlink);
9. if (ret != Udmf_ErrCode::UDMF_E_OK) {
10. OH_LOG_ERROR(LOG_APP, "Fail get hyperlink from record!");
11. OH_UdsHyperlink_Destroy(hyperlink);
12. return ret;
13. }
14. // 读取OH_UdsHyperlink中的各项信息。
15. OH_LOG_INFO(LOG_APP, "The hyperlink type id is : %{public}s", OH_UdsHyperlink_GetType(hyperlink));
16. OH_LOG_INFO(LOG_APP, "The hyperlink url is : %{public}s", OH_UdsHyperlink_GetUrl(hyperlink));
17. OH_LOG_INFO(LOG_APP, "The hyperlink description is : %{public}s",
18. OH_UdsHyperlink_GetDescription(hyperlink));
19. OH_UdsHyperlink_Destroy(hyperlink);
20. }
21. }
22. return UDMF_E_OK;
23. }

25. int32_t ProcessDataElement(OH_UdmfData* data)
26. {
27. unsigned int recordsCount = 0;
28. OH_UdmfRecord** records = OH_UdmfData_GetRecords(data, &recordsCount);
29. OH_LOG_INFO(LOG_APP, "the count of records count is %{public}u", recordsCount);
30. // 5. 获取数据记录中的元素。
31. for (unsigned int j = 0; j < recordsCount; j++) {
32. // 获取OH_UdmfRecord类型列表。
33. unsigned int recordTypeIdCount = 0;
34. char** typeIdsFromRecord = OH_UdmfRecord_GetTypes(records[j], &recordTypeIdCount);
35. int32_t ret = ProcessRecordHyperlinks(records[j], recordTypeIdCount, typeIdsFromRecord);
36. if (ret != Udmf_ErrCode::UDMF_E_OK) {
37. OH_LOG_ERROR(LOG_APP, "ProcessRecordHyperlinks error!");
38. return ret;
39. }
40. }
41. return UDMF_E_OK;
42. }

44. int32_t ProcessHyperlinkDataFromArray(OH_UdmfData* readData, unsigned int dataSize, OH_UdmfData** dataArray)
45. {
46. for (unsigned int i = 0; i < dataSize - 1; i++) {
47. OH_UdmfData* data = OH_UDMF_GetDataElementAt(dataArray, i);
48. // 3. 判断OH_UdmfData是否有对应的类型。
49. if (!OH_UdmfData_HasType(data, UDMF_META_HYPERLINK)) {
50. OH_LOG_INFO(LOG_APP, "There is no hyperlink type in data[%{public}u].", i);
51. continue;
52. }
53. // 4. 获取数据记录和hyperlink数据。
54. int32_t ret = ProcessDataElement(data);
55. if (ret != UDMF_E_OK) {
56. OH_LOG_ERROR(LOG_APP, "processDataElement data error!");
57. return ret;
58. }
59. }
60. return UDMF_E_OK;
61. }

63. int32_t DeleteDataTest()
64. {
65. // 1. 构建数据操作选项。
66. OH_UdmfOptions* options = OH_UdmfOptions_Create();
67. int32_t ret = OH_UdmfOptions_SetIntention(options, Udmf_Intention::UDMF_INTENTION_DATA_HUB);
68. if (ret != Udmf_ErrCode::UDMF_E_OK) {
69. OH_LOG_ERROR(LOG_APP, "Set option error!");
70. OH_UdmfOptions_Destroy(options);
71. return ret;
72. }
73. // 2. 通过数据操作选项删除数据。
74. unsigned int dataSize = 0;
75. OH_UdmfData* readData = nullptr;
76. ret = OH_Udmf_DeleteUnifiedData(options, &readData, &dataSize);
77. if (ret != Udmf_ErrCode::UDMF_E_OK) {
78. OH_LOG_ERROR(LOG_APP, "Delete Data error!");
79. OH_UdmfOptions_Destroy(options);
80. return ret;
81. }
82. OH_UdmfOptions_Destroy(options);
83. if (dataSize == 0) {
84. OH_LOG_INFO(LOG_APP, "the size of data is %{public}u", dataSize);
85. return UDMF_E_OK;
86. }
87. OH_LOG_INFO(LOG_APP, "the size of data is %{public}u", dataSize);
88. OH_UdmfData** dataArray = &readData;
89. ret = ProcessHyperlinkDataFromArray(readData, dataSize, dataArray);
90. if (ret != UDMF_E_OK) {
91. OH_LOG_ERROR(LOG_APP, "Process hyperlink data error!");
92. return ret;
93. }
94. // 6. 销毁指针。
95. OH_Udmf_DestroyDataArray(dataArray, dataSize);
96. return UDMF_E_OK;
97. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/UnifiedDataChannels_C/entry/src/main/cpp/napi_init.cpp#L277-L375)

## 使用UDMF延迟写入UDS数据

### 定义UDS数据提供函数

下面以超链接hyperlink类型数据场景为例，说明如何定义一个提供UDS数据的回调函数。

1. 定义OH\_UdmfRecordProvider的数据提供函数。
2. 在数据提供函数中，创建hyperlink类型的UDS数据结构。
3. 设置hyperlink的URL和描述信息。
4. 定义OH\_UdmfRecordProvider销毁时触发的回调函数。

```
1. // 为了代码可读性，代码中省略了各个步骤操作结果的校验，实际开发中需要确认每次调用的成功。
2. // 1. 获取数据时触发的提供UDS数据的回调函数。
3. static void* GetDataCallback(void* context, const char* type)
4. {
5. if (strcmp(type, UDMF_META_HYPERLINK) == 0) {
6. // 2. 创建超链接hyperlink数据的UDS数据结构。
7. OH_UdsHyperlink* hyperlink = OH_UdsHyperlink_Create();
8. // 3. 设置hyperlink中的URL和描述信息。
9. OH_UdsHyperlink_SetUrl(hyperlink, "www.demo.com");
10. OH_UdsHyperlink_SetDescription(hyperlink, "This is the description.");
11. return hyperlink;
12. }
13. return nullptr;
14. }
15. // 4. OH_UdmfRecordProvider销毁时触发的回调函数。
16. static void ProviderFinalizeCallback(void* context) { OH_LOG_INFO(LOG_APP, "OH_UdmfRecordProvider finalize."); }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/UnifiedDataChannels_C/entry/src/main/cpp/napi_init.cpp#L377-L394)

### 延迟写入UDS数据

下面以延迟写入超链接类型数据为例，说明如何使用OH\_UdmfRecordProvider与UDMF。此步骤完成后，超链接类型数据并未真正写入数据库。只有当数据使用者从OH\_UdmfRecord中获取OH\_UdsHyperlink时，才会触发上文定义的GetDataCallback数据提供函数，从中获取数据。

1. 创建OH\_UdmfRecordProvider对象，设置它的数据提供函数和销毁回调函数。
2. 创建OH\_UdmfRecord对象，并配置OH\_UdmfRecordProvider。
3. 创建OH\_UdmfData对象，并向OH\_UdmfData中添加OH\_UdmfRecord。
4. 构建数据并写入数据库中，获取返回的Key值。
5. 使用完成后销毁指针。

```
1. int32_t ProviderSetDataTest()
2. {
3. // 为了代码可读性，代码中省略了各个步骤操作结果的校验，实际开发中需要确认每次调用的成功。
4. // 1. 创建一个OH_UdmfRecordProvider，设置它的数据提供函数和销毁回调函数。
5. OH_UdmfRecordProvider* provider = OH_UdmfRecordProvider_Create();
6. OH_UdmfRecordProvider_SetData(provider, (void*)provider, GetDataCallback, ProviderFinalizeCallback);

8. // 2. 创建OH_UdmfRecord对象，并配置OH_UdmfRecordProvider。
9. OH_UdmfRecord* record = OH_UdmfRecord_Create();
10. const char* types[1] = {UDMF_META_HYPERLINK};
11. OH_UdmfRecord_SetProvider(record, types, 1, provider);

13. // 3. 创建OH_UdmfData对象，并向OH_UdmfData中添加OH_UdmfRecord。
14. OH_UdmfData* data = OH_UdmfData_Create();
15. OH_UdmfData_AddRecord(data, record);

17. // 4. 构建数据并写入数据库中，获取返回的Key值。
18. OH_UdmfOptions* options = OH_UdmfOptions_Create();
19. if (OH_UdmfOptions_SetIntention(options, Udmf_Intention::UDMF_INTENTION_DATA_HUB) != Udmf_ErrCode::UDMF_E_OK) {
20. OH_LOG_ERROR(LOG_APP, "Set option error!");
21. OH_UdmfOptions_Destroy(options);
22. return UDMF_ERR;
23. }
24. char key[UDMF_KEY_BUFFER_LEN] = {0};
25. if (OH_Udmf_SetUnifiedDataByOptions(options, data, key, sizeof(key)) != Udmf_ErrCode::UDMF_E_OK) {
26. OH_LOG_ERROR(LOG_APP, "Set data error!");
27. }
28. OH_LOG_INFO(LOG_APP, "key = %{public}s", key);

30. // 5. 使用完成后销毁指针。
31. OH_UdmfRecord_Destroy(record);
32. OH_UdmfData_Destroy(data);
33. OH_UdmfOptions_Destroy(options);
34. return UDMF_E_OK;
35. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/UnifiedDataChannels_C/entry/src/main/cpp/napi_init.cpp#L396-L432)
