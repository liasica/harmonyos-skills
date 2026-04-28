---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pasteboard-time-lapse-copy-and-paste
title: 使用剪贴板进行延迟复制粘贴
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 剪贴板服务 > 使用剪贴板进行延迟复制粘贴
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:43940c084b087206db13a2d45f4a6c40595912e95ec7efee61596065953e0072
---

## 场景介绍

[@ohos.pasteboard](../harmonyos-references/js-apis-pasteboard.md)主要提供管理系统剪贴板的能力，为系统复制、粘贴功能提供支持。

反复执行复制操作时，剪贴板缓存中会存储多余数据从而导致内存增加，为了优化内存以及后续支持指定数据类型粘贴，剪贴板提供了延迟复制粘贴的功能。

用户复制使用延迟复制技术的应用内的数据时，该条真实数据不会立即写入剪贴板服务的缓存中，而是等需要粘贴时，再从应用获取数据。

## 约束限制

* 剪贴板内容包含剪贴板系统服务元数据和应用设置的数据，总大小上限默认为128MB，PC/2in1设备可通过系统配置修改上限，有效范围为128MB~2GB。
* NDK接口仅支持Record级别的延迟复制粘贴。
* 当复制的数据量较小且准备数据所需时间不会影响用户体验时，不建议应用程序使用延迟复制功能，推荐将数据直接写入剪贴板。

## 使用基于Record级别的延迟复制粘贴

本方案可以在粘贴前查询数据type信息，应用可以据此决定是否向剪贴板请求数据，因此建议使用本方案实现延迟复制功能。

从API version 21开始，应用退出不仅可以调用延迟复制接口[OH\_Pasteboard\_SetData](../harmonyos-references/capi-oh-pasteboard-h.md#oh_pasteboard_setdata)主动提交所有复制数据，还可以使用同步延迟数据接口[OH\_Pasteboard\_SyncDelayedDataAsync](../harmonyos-references/capi-oh-pasteboard-h.md#oh_pasteboard_syncdelayeddataasync)通知剪贴板获取全量数据。

1. 当应用使用延迟复制功能复制时，仅将应用支持的数据类型写入剪贴板。应用应在退出时，重新调用[OH\_Pasteboard\_SetData](../harmonyos-references/capi-oh-pasteboard-h.md#oh_pasteboard_setdata)接口主动提交所有复制数据或调用[OH\_Pasteboard\_SyncDelayedDataAsync](../harmonyos-references/capi-oh-pasteboard-h.md#oh_pasteboard_syncdelayeddataasync)接口通知剪贴板获取全量数据，等待数据同步完成再继续退出，否则可能导致其他应用粘贴获取不到数据。
2. 调用[OH\_Pasteboard\_SyncDelayedDataAsync](../harmonyos-references/capi-oh-pasteboard-h.md#oh_pasteboard_syncdelayeddataasync)接口会延长退出过程，建议应用在复制数据时直接设置数据到剪贴板，而不是调用延迟复制接口[OH\_UdmfRecordProvider\_SetData](../harmonyos-references/capi-udmf-h.md#oh_udmfrecordprovider_setdata)和同步延迟数据接口[OH\_Pasteboard\_SyncDelayedDataAsync](../harmonyos-references/capi-oh-pasteboard-h.md#oh_pasteboard_syncdelayeddataasync)。
3. 延迟复制场景应用异常退出时，无法触发应用退出延迟数据同步流程，会导致其他应用粘贴时获取不到数据。

### 接口说明

详细接口见[Pasteboard文档](../harmonyos-references/capi-pasteboard.md)和[UDMF接口文档](../harmonyos-references/capi-udmf.md)。

| 名称 | 说明 |
| --- | --- |
| OH\_UdmfRecordProvider\* OH\_UdmfRecordProvider\_Create() | 创建一个指向统一数据提供者的指针。 |
| int OH\_UdmfRecordProvider\_SetData(OH\_UdmfRecordProvider\* provider, void\* context, const OH\_UdmfRecordProvider\_GetData callback, const UdmfData\_Finalize finalize) | 设置统一数据提供者的回调函数。 |
| int OH\_UdmfRecord\_SetProvider(OH\_UdmfRecord\* pThis, const char\* const\* types, unsigned int count, OH\_UdmfRecordProvider\* provider) | 将统一数据提供者配置到OH\_UdmfRecord中。 |
| int OH\_Pasteboard\_SetData(OH\_Pasteboard\* pasteboard, OH\_UdmfData\* data) | 向剪贴板中写入数据。 |
| OH\_UdmfData \* OH\_Pasteboard\_GetData(OH\_Pasteboard\* pasteboard, int\* status) | 获取剪贴板中的数据。 |
| OH\_UdmfRecord\*\* OH\_UdmfData\_GetRecords(OH\_UdmfData\* pThis, unsigned int\* count) | 获取OH\_UdmfData中全部的数据记录。 |
| void OH\_Pasteboard\_SyncDelayedDataAsync(OH\_Pasteboard\* pasteboard, void (\*callback)(int errorCode)) | 通知剪贴板从应用同步所有延迟数据。 当应用使用延迟复制功能复制时，仅将应用支持的数据类型写入剪贴板。应用应在退出时，重新调用[OH\_Pasteboard\_SetData](../harmonyos-references/capi-oh-pasteboard-h.md#oh_pasteboard_setdata)接口主动提交所有复制数据或调用[OH\_Pasteboard\_SyncDelayedDataAsync](../harmonyos-references/capi-oh-pasteboard-h.md#oh_pasteboard_syncdelayeddataasync)接口通知剪贴板获取全量数据，等待数据同步完成再继续退出，否则可能导致其他应用粘贴获取不到数据。 |

### 开发步骤

下面以纯文本类型和HTML类型数据为例，说明如何向剪贴板服务设置延迟复制数据。

为了代码可读性，代码中省略了各个步骤操作结果的校验，实际开发中需要确认每次调用的成功。

1. 引用头文件。

   ```
   1. #include <cstring>
   2. #include <hilog/log.h>
   3. #include <database/pasteboard/oh_pasteboard.h>
   4. #include <database/udmf/udmf.h>
   5. #include <database/udmf/uds.h>
   6. #include <database/udmf/udmf_meta.h>
   7. #include <accesstoken/ability_access_control.h>
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/pasteboard/pasteboard_NDK_sample/entry/src/main/cpp/napi_init.cpp#L20-L29)
2. 定义OH\_UdmfRecordProvider的数据提供函数和实例注销回调函数。

   ```
   1. // 1. 获取数据时触发的提供剪贴板数据的回调函数。
   2. void* GetDataCallback(void* context, const char* type)
   3. {
   4. // 纯文本类型
   5. if (memcmp(type, UDMF_META_PLAIN_TEXT, sizeof(UDMF_META_PLAIN_TEXT) - 1) == 0) {
   6. // 创建纯文本类型的Uds对象。
   7. OH_UdsPlainText* udsText = OH_UdsPlainText_Create();
   8. // 设置纯文本内容。
   9. OH_UdsPlainText_SetContent(udsText, "hello world");
   10. return udsText;
   11. } else if (strcmp(type, UDMF_META_HTML) == 0) {
   12. // 创建HTML类型的Uds对象。
   13. OH_UdsHtml* udsHtml = OH_UdsHtml_Create();
   14. // 设置HTML内容。
   15. OH_UdsHtml_SetContent(udsHtml, "<div>hello world</div>");
   16. return udsHtml;
   17. }
   18. return nullptr;
   19. }
   20. // 2. OH_UdmfRecordProvider销毁时触发的回调函数。
   21. void ProviderFinalizeCallback(void* context)
   22. {
   23. OH_LOG_INFO(LOG_APP, "OH_UdmfRecordProvider finalize.");
   24. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/pasteboard/pasteboard_NDK_sample/entry/src/main/cpp/napi_init.cpp#L142-L167)
3. 定义OH\_Pasteboard\_SyncDelayedDataAsync的回调函数。

   ```
   1. // 3. 定义应用退出时调用延迟同步接口触发的回调函数。
   2. void SyncCallback(int errorCode)
   3. {
   4. // 继续退出
   5. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/pasteboard/pasteboard_NDK_sample/entry/src/main/cpp/napi_init.cpp#L168-L174)
4. 在剪贴板中准备延迟复制数据。此步骤完成后纯文本类型数据与HTML类型数据并未真正写入剪贴板服务，只有当数据使用者从OH\_UdmfRecord中获取OH\_UdsPlainText或OH\_UdsHtml时，才会触发上文定义的GetDataCallback数据提供函数，从中得到数据。

   ```
   1. OH_Pasteboard* CreateAndSetPasteboardData()
   2. {
   3. // 4. 创建OH_UdmfRecord对象。
   4. OH_UdmfRecord* record = OH_UdmfRecord_Create();
   5. // 5. 创建OH_UdmfRecordProvider对象，并设置用于提供延迟数据、析构的两个回调函数。
   6. OH_UdmfRecordProvider* provider = OH_UdmfRecordProvider_Create();
   7. OH_UdmfRecordProvider_SetData(provider, (void *)record, GetDataCallback, ProviderFinalizeCallback);
   8. // 6. 将provider绑定到record，并设置支持的数据类型。
   9. #define TYPE_COUNT 2
   10. const char* types[TYPE_COUNT] = {UDMF_META_PLAIN_TEXT, UDMF_META_HTML};
   11. OH_UdmfRecord_SetProvider(record, types, TYPE_COUNT, provider);
   12. // 7. 创建OH_UdmfData对象，并向OH_UdmfData中添加OH_UdmfRecord。
   13. OH_UdmfData* setData = OH_UdmfData_Create();
   14. if (setData != nullptr) {
   15. OH_UdmfData_AddRecord(setData, record);
   16. }
   17. // 8. 创建OH_Pasteboard对象，将数据写入剪贴板中。
   18. OH_Pasteboard* pasteboard = OH_Pasteboard_Create();
   19. if (setData != nullptr) {
   20. OH_Pasteboard_SetData(pasteboard, setData);
   21. }
   22. OH_UdmfRecordProvider_Destroy(provider);
   23. OH_UdmfRecord_Destroy(record);
   24. OH_UdmfData_Destroy(setData);
   25. return pasteboard;
   26. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/pasteboard/pasteboard_NDK_sample/entry/src/main/cpp/napi_init.cpp#L175-L202)
5. 从剪贴板获取延迟复制数据。

   ```
   1. void ProcessRecordType(OH_UdmfRecord* record, const char* recordType)
   2. {
   3. OH_UdsPlainText* udsText = nullptr;
   4. OH_UdsHtml* udsHtml = nullptr;
   5. if (strcmp(recordType, UDMF_META_PLAIN_TEXT) == 0) {
   6. // 创建纯文本类型的Uds对象
   7. udsText = OH_UdsPlainText_Create();
   8. if (udsText != nullptr) {
   9. // 从record中获取纯文本类型的Uds对象
   10. OH_UdmfRecord_GetPlainText(record, udsText);
   11. // 从Uds对象中获取内容
   12. const char* content = OH_UdsPlainText_GetContent(udsText);
   13. } else if (strcmp(recordType, UDMF_META_HTML) == 0) {
   14. // 创建HTML类型的Uds对象
   15. udsHtml = OH_UdsHtml_Create();
   16. if (udsHtml != nullptr) {
   17. // 从record中获取HTML类型的Uds对象
   18. OH_UdmfRecord_GetHtml(record, udsHtml);
   19. // 从Uds对象中获取内容
   20. const char* content = OH_UdsHtml_GetContent(udsHtml);
   21. }
   22. }
   23. }
   24. }
   25. void ProcessRecord(OH_UdmfRecord* record)
   26. {
   27. // 13. 查询OH_UdmfRecord中的数据类型。
   28. unsigned typeCount = 0;
   29. char** recordTypes = OH_UdmfRecord_GetTypes(record, &typeCount);
   30. // 14. 遍历数据类型。
   31. for (unsigned int typeIndex = 0; typeIndex < typeCount; ++typeIndex) {
   32. const char* recordType = recordTypes[typeIndex];
   33. ProcessRecordType(record, recordType);
   34. }
   35. }

   37. static napi_value NAPI_Pasteboard_time(napi_env env, napi_callback_info info)
   38. {
   39. OH_Pasteboard* pasteboard = CreateAndSetPasteboardData();
   40. // 9. 记录当前的剪贴板数据变化次数。
   41. uint32_t changeCount = OH_Pasteboard_GetChangeCount(pasteboard);
   42. // 10. 从剪贴板获取OH_UdmfData。
   43. int status = -1;
   44. bool hasPermission = OH_AT_CheckSelfPermission("ohos.permission.READ_PASTEBOARD");
   45. if (!hasPermission) {
   46. OH_LOG_ERROR(LOG_APP, "No Permission READ_PASTEBOARD");
   47. };
   48. OH_UdmfData* getData = OH_Pasteboard_GetData(pasteboard, &status);
   49. if (getData == nullptr) {
   50. // 处理错误情况，清理资源
   51. OH_LOG_ERROR(LOG_APP, "Failed to get data from pasteboard, status: %d\n", status);
   52. }
   53. // 11. 获取OH_UdmfData中的所有OH_UdmfRecord。
   54. unsigned int recordCount = 0;
   55. OH_UdmfRecord** getRecords = OH_UdmfData_GetRecords(getData, &recordCount);
   56. OH_UdsPlainText* udsText = nullptr;
   57. OH_UdsHtml* udsHtml = nullptr;
   58. // 12. 遍历OH_UdmfRecord。
   59. for (unsigned int recordIndex = 0; recordIndex < recordCount; ++recordIndex) {
   60. OH_UdmfRecord* record = getRecords[recordIndex];
   61. ProcessRecord(record);
   62. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/pasteboard/pasteboard_NDK_sample/entry/src/main/cpp/napi_init.cpp#L203-L266)
6. 应用退出时，如果剪贴板内的数据没有变化，则通知剪贴板获取全量数据，等待回调完成再继续退出，否则可能导致其他应用粘贴获取不到数据。

   ```
   1. // 15. 查询剪贴板内的数据是否变化。
   2. uint32_t newChangeCount = OH_Pasteboard_GetChangeCount(pasteboard);
   3. if (newChangeCount == changeCount) {
   4. // 16. 通知剪贴板获取全量数据。
   5. OH_Pasteboard_SyncDelayedDataAsync(pasteboard, SyncCallback);
   6. // 需要等待SyncCallback回调完成再继续退出
   7. } else {
   8. // 继续退出
   9. OH_LOG_INFO(LOG_APP, "No newChangeCount in pasteboard.");
   10. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/pasteboard/pasteboard_NDK_sample/entry/src/main/cpp/napi_init.cpp#L267-L278)
7. 使用完毕后需要及时释放相关对象的内存。

   ```
   1. OH_UdsPlainText_Destroy(udsText);
   2. OH_UdsHtml_Destroy(udsHtml);
   3. OH_UdmfData_Destroy(getData);
   4. OH_Pasteboard_Destroy(pasteboard);
   5. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/pasteboard/pasteboard_NDK_sample/entry/src/main/cpp/napi_init.cpp#L280-L286)
