---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-use-pasteboard
title: 使用剪贴板进行复制粘贴 (C/C++)
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 剪贴板服务 > 使用剪贴板进行复制粘贴 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c68999846d1e8621e4b373d04fd4551218ddd0a7ebd40625148463fa829f4b61
---

## 场景介绍

剪贴板为开发者提供数据的复制粘贴能力。支持对纯文本、超文本、URI等内容的操作。

## 基本概念

* [**OH\_PasteboardObserver**](../harmonyos-references/capi-pasteboard-oh-pasteboardobserver.md)：剪贴板数据变更观察者对象，用以监听剪贴板数据变更事件。
* [**OH\_Pasteboard**](../harmonyos-references/capi-pasteboard-oh-pasteboard.md)：剪贴板对象，用来进行查询、写入等操作。
* [**OH\_UdmfData**](../harmonyos-references/capi-udmf-oh-udmfdata.md)：统一数据对象。

## 约束限制

* 剪贴板内容包含剪贴板系统服务元数据和应用设置的数据，总大小上限默认为128MB，PC/2in1设备可通过系统配置修改上限，有效范围为128MB~2GB。
* 为保证剪贴板数据的准确性，同一时间只能支持一个复制操作。
* 当前支持的数据类型：纯文本类型(OH\_UdsPlainText)、超文本标记语言类型(OH\_UdsHtml)、文件Uri类型(OH\_UdsFileUri)、像素图片类型(OH\_UdsPixelMap)、超链接类型(OH\_UdsHyperlink)、桌面图标类型(OH\_UdsAppItem)、自定义类型。ArkTS接口与NDK接口支持数据类型不完全一致，使用时须匹配接口支持类型，详情见[ArkTS接口与NDK接口数据类型对应关系](use-pasteboard-to-copy-and-paste.md#arkts接口与ndk接口数据类型对应关系)。
* 自定义类型数据在复制粘贴时，指定的类型名称不能和已有的类型名称重复。
* API version 12及之后，系统为提升用户隐私安全保护能力，剪贴板读取接口增加[权限管控](get-pastedata-permission-guidelines.md)。
* API version 12中新增的复制、粘贴接口[setUnifiedData](../harmonyos-references/js-apis-pasteboard.md#setunifieddata12)/[getUnifiedData](../harmonyos-references/js-apis-pasteboard.md#getunifieddata12)与本文档中的复制、粘贴接口[OH\_Pasteboard\_SetData](../harmonyos-references/capi-oh-pasteboard-h.md#oh_pasteboard_setdata)/[OH\_Pasteboard\_GetData](../harmonyos-references/capi-oh-pasteboard-h.md#oh_pasteboard_getdata)当前相互独立，进行写入、读取操作时请使用对应配套接口。

## 接口说明

详细接口见[Pasteboard文档](../harmonyos-references/capi-pasteboard.md)。

| 接口名称 | 描述 |
| --- | --- |
| OH\_PasteboardObserver\* OH\_PasteboardObserver\_Create() | 创建一个剪贴板数据变更观察者对象。 |
| OH\_PasteboardObserver\_Destroy(OH\_PasteboardObserver\* observer) | 销毁剪贴板数据变更观察者对象。 |
| int OH\_PasteboardObserver\_SetData(OH\_PasteboardObserver\* observer, void\* context, const Pasteboard\_Notify callback, const Pasteboard\_Finalize finalize) | 将剪贴板变更回调函数设置到剪贴板数据变更观察者对象中。 |
| OH\_Pasteboard\* OH\_Pasteboard\_Create() | 创建一个剪贴板实例。 |
| void OH\_Pasteboard\_Destroy(OH\_Pasteboard\* pasteboard) | 销毁剪贴板实例。 |
| int OH\_Pasteboard\_Subscribe(OH\_Pasteboard\* pasteboard, int type, const OH\_PasteboardObserver\* observer) | 订阅剪贴板的数据变更。 |
| int OH\_Pasteboard\_Unsubscribe(OH\_Pasteboard\* pasteboard, int type, const OH\_PasteboardObserver\* observer) | 取消对剪贴板数据变更的订阅。 |
| bool OH\_Pasteboard\_IsRemoteData(OH\_Pasteboard\* pasteboard) | 判断剪贴板中的数据是否来自远端设备。 |
| int OH\_Pasteboard\_GetDataSource(OH\_Pasteboard\* pasteboard, char\* source, unsigned int len) | 获取剪贴板中数据的数据源。 |
| bool OH\_Pasteboard\_HasType(OH\_Pasteboard\* pasteboard, const char\* type) | 判断剪贴板中是否有指定类型的数据。 |
| bool OH\_Pasteboard\_HasData(OH\_Pasteboard\* pasteboard) | 检查剪贴板中是否有数据。 |
| OH\_UdmfData\* OH\_Pasteboard\_GetData(OH\_Pasteboard\* pasteboard, int\* status) | 获取剪贴板中的数据。 |
| int OH\_Pasteboard\_SetData(OH\_Pasteboard\* pasteboard, OH\_UdmfData\* data) | 向剪贴板中写入数据。 |
| int OH\_Pasteboard\_ClearData(OH\_Pasteboard\* pasteboard) | 清空剪贴板中的数据。 |
| void (\*Pasteboard\_Notify)(void\* context, Pasteboard\_NotifyType type) | 剪贴板中数据变更回调函数。 |
| void (\*Pasteboard\_Finalize)(void\* context) | 剪贴板数据变更观察者对象销毁时，释放context上下文资源。 |

## 开发步骤

1. 添加动态链接库。

   ```
   1. # CMakeLists.txt中添加以下lib
   2. libudmf.so
   3. libpasteboard.so
   ```
2. 引用头文件。

   ```
   1. #include <cstdio>
   2. #include <cstring>
   3. #include <hilog/log.h>
   4. #include <database/pasteboard/oh_pasteboard.h>
   5. #include <database/udmf/udmf.h>
   6. #include <database/udmf/uds.h>
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/pasteboard/pasteboard_NDK_sample/entry/src/main/cpp/napi_init.cpp#L18-L26)
3. 定义剪贴板变化监听的回调函数。

   ```
   1. // 定义剪贴板数据内容变更时的通知回调函数
   2. static void PasteboardNotifyImpl2(void* context, Pasteboard_NotifyType type)
   3. {
   4. OH_LOG_INFO(LOG_APP, "Pasteboard_NotifyType, type: %d", type);
   5. }
   6. // 定义剪贴板数据变更观察者对象销毁时的通知回调函数
   7. static void PasteboardFinalizeImpl2(void* context)
   8. {
   9. OH_LOG_INFO(LOG_APP, "callback: Pasteboard_Finalize");
   10. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/pasteboard/pasteboard_NDK_sample/entry/src/main/cpp/napi_init.cpp#L32-L43)
4. 订阅剪贴板变化。

   ```
   1. static void PasteboardTestObserver()
   2. {
   3. // 1. 创建一个剪贴板实例
   4. OH_Pasteboard* pasteboard = OH_Pasteboard_Create();
   5. // 2. 创建一个剪贴板数据变更观察者实例
   6. OH_PasteboardObserver* observer = OH_PasteboardObserver_Create();
   7. // 3. 将两个回调函数设置到观察者实例
   8. OH_PasteboardObserver_SetData(observer, (void*)pasteboard, PasteboardNotifyImpl2, PasteboardFinalizeImpl2);
   9. // 4. 设置对剪贴板本端数据变化的订阅
   10. OH_Pasteboard_Subscribe(pasteboard, NOTIFY_LOCAL_DATA_CHANGE, observer);
   11. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/pasteboard/pasteboard_NDK_sample/entry/src/main/cpp/napi_init.cpp#L44-L56)
5. 向剪贴板写入数据。

   ```
   1. static napi_value NAPI_Pasteboard_set(napi_env env, napi_callback_info info)
   2. {
   3. napi_value args[1];
   4. size_t argc = 1;
   5. napi_status status = napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   6. char text[256];
   7. size_t value0Size;
   8. status = napi_get_value_string_utf8(env, args[0], text, sizeof(text), &value0Size);

   10. // 1. 创建一个剪贴板实例
   11. OH_Pasteboard* pasteboard = OH_Pasteboard_Create();
   12. if (pasteboard == nullptr) {
   13. OH_LOG_INFO(LOG_APP, "Failed to create pasteboard instance.");
   14. };
   15. // 2. 创建OH_UdmfRecord对象，并向OH_UdmfRecord中添加文本类型数据
   16. OH_UdsPlainText* udsPlainText = OH_UdsPlainText_Create();
   17. OH_UdsPlainText_SetContent(udsPlainText, text);
   18. OH_UdsHtml* udsHtml = OH_UdsHtml_Create();
   19. OH_UdsHtml_SetContent(udsHtml, "hello world");
   20. OH_UdmfRecord* record = OH_UdmfRecord_Create();
   21. OH_UdmfRecord_AddPlainText(record, udsPlainText);
   22. OH_UdmfRecord_AddHtml(record, udsHtml);
   23. // 3. 创建OH_UdmfData对象，并向OH_UdmfData中添加OH_UdmfRecord
   24. OH_UdmfData* data = OH_UdmfData_Create();
   25. OH_UdmfData_AddRecord(data, record);
   26. // 4. 将数据写入剪贴板
   27. OH_Pasteboard_SetData(pasteboard, data);
   28. // 5. 使用完销毁指针
   29. OH_UdsPlainText_Destroy(udsPlainText);
   30. OH_UdsHtml_Destroy(udsHtml);
   31. OH_UdmfRecord_Destroy(record);
   32. OH_UdmfData_Destroy(data);
   33. OH_Pasteboard_Destroy(pasteboard);
   34. // ...
   35. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/pasteboard/pasteboard_NDK_sample/entry/src/main/cpp/napi_init.cpp#L57-L97)
6. 从剪贴板读取数据。

   ```
   1. static napi_value NAPI_Pasteboard_get(napi_env env, napi_callback_info info)
   2. {
   3. // 1. 创建一个剪贴板实例
   4. OH_Pasteboard* pasteboard = OH_Pasteboard_Create();
   5. if (pasteboard == nullptr) {
   6. OH_LOG_INFO(LOG_APP, "Failed to create pasteboard instance.");
   7. };
   8. // 2. 判断剪贴板中是否有文本类型数据
   9. bool hasPlainTextData = OH_Pasteboard_HasType(pasteboard, "text/plain");
   10. if (hasPlainTextData) {
   11. // 3. 从剪贴板中获取统一类型数据OH_UdmfData
   12. int ret = 0;
   13. OH_UdmfData* udmfData = OH_Pasteboard_GetData(pasteboard, &ret);
   14. if (udmfData == nullptr) {
   15. OH_LOG_INFO(LOG_APP, "Failed to get data from pasteboard.");
   16. };
   17. // 4. 从OH_UdmfData中获取第一个数据记录
   18. OH_UdmfRecord* record = OH_UdmfData_GetRecord(udmfData, 0);
   19. if (record == nullptr) {
   20. OH_LOG_INFO(LOG_APP, "Failed to get record from udmfData.");
   21. };
   22. // 5. 从数据记录中获取文本数据内容
   23. OH_UdsPlainText* plainText = OH_UdsPlainText_Create();
   24. if (plainText == nullptr) {
   25. OH_LOG_INFO(LOG_APP, "Failed to create plain text object.");
   26. };
   27. OH_UdmfRecord_GetPlainText(record, plainText);
   28. const char* content = OH_UdsPlainText_GetContent(plainText);
   29. if (content == nullptr) {
   30. OH_LOG_INFO(LOG_APP, "Failed to get content from plain text.");
   31. }
   32. napi_value result;
   33. napi_create_string_utf8(env, content, strlen(content), &result);
   34. // 6. 使用完销毁指针
   35. OH_UdsPlainText_Destroy(plainText);
   36. OH_UdmfRecord_Destroy(record);
   37. return result;
   38. } else {
   39. OH_LOG_INFO(LOG_APP, "No plain text data in pasteboard.");
   40. }
   41. OH_Pasteboard_Destroy(pasteboard);
   42. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/pasteboard/pasteboard_NDK_sample/entry/src/main/cpp/napi_init.cpp#L98-L141)
