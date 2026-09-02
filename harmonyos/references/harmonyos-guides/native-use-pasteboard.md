---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-use-pasteboard
title: 使用剪贴板进行复制粘贴（C/C++）
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 剪贴板服务 > 使用剪贴板进行复制粘贴（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:08+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f101cd1285b1be8b1d2f39af4766789b01570d9831aea2d5644073a35bc5301e
---

## 场景介绍

剪贴板为开发者提供数据的复制粘贴能力。支持对纯文本、超文本、URI等内容的操作。

## 基本概念

* [**OH\_PasteboardObserver**](../harmonyos-references/capi-pasteboard-oh-pasteboardobserver.md)：剪贴板数据变更观察者对象，用以监听剪贴板数据变更事件。
* [**OH\_Pasteboard**](../harmonyos-references/capi-pasteboard-oh-pasteboard.md)：剪贴板对象，用来进行查询、写入等操作。
* [**OH\_UdmfData**](../harmonyos-references/capi-udmf-oh-udmfdata.md)：统一数据对象。

## 约束限制

* 剪贴板内容包含剪贴板系统服务元数据和应用设置的数据，总大小上限默认为128MB，PC/2in1设备可通过系统配置修改上限，有效范围为1MB~2GB。
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

   ```cmake
   # CMakeLists.txt中添加以下lib
   libudmf.so
   libpasteboard.so
   ```
2. 引用头文件。

   ```
   #include <cstdio>
   #include <cstring>
   #include <hilog/log.h>
   #include <database/pasteboard/oh_pasteboard.h>
   #include <database/udmf/udmf.h>
   #include <database/udmf/uds.h>
   ```
3. 定义剪贴板变化监听的回调函数。

   ```
   // 定义剪贴板数据内容变更时的通知回调函数
   static void PasteboardNotifyImpl2(void* context, Pasteboard_NotifyType type)
   {
       OH_LOG_INFO(LOG_APP, "Pasteboard_NotifyType, type: %d", type);
   }
   // 定义剪贴板数据变更观察者对象销毁时的通知回调函数
   static void PasteboardFinalizeImpl2(void* context)
   {
       OH_LOG_INFO(LOG_APP, "callback: Pasteboard_Finalize");
   }
   ```
4. 订阅剪贴板变化。

   ```
   static void PasteboardTestObserver()
   {
       // 1. 创建一个剪贴板实例
       OH_Pasteboard* pasteboard = OH_Pasteboard_Create();
       // 2. 创建一个剪贴板数据变更观察者实例
       OH_PasteboardObserver* observer = OH_PasteboardObserver_Create();
       // 3. 将两个回调函数设置到观察者实例
       OH_PasteboardObserver_SetData(observer, (void*)pasteboard, PasteboardNotifyImpl2, PasteboardFinalizeImpl2);
       // 4. 设置对剪贴板本端数据变化的订阅
       OH_Pasteboard_Subscribe(pasteboard, NOTIFY_LOCAL_DATA_CHANGE, observer);
   }
   ```
5. 向剪贴板写入数据。

   ```
   static napi_value NAPI_Pasteboard_set(napi_env env, napi_callback_info info)
   {
       napi_value args[1];
       size_t argc = 1;
       napi_status status = napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
       char text[256];
       size_t value0Size;
       status = napi_get_value_string_utf8(env, args[0], text, sizeof(text), &value0Size);

       // 1. 创建一个剪贴板实例
       OH_Pasteboard* pasteboard = OH_Pasteboard_Create();
       if (pasteboard == nullptr) {
           OH_LOG_INFO(LOG_APP, "Failed to create pasteboard instance.");
       };
       // 2. 创建OH_UdmfRecord对象，并向OH_UdmfRecord中添加文本类型数据
       OH_UdsPlainText* udsPlainText = OH_UdsPlainText_Create();
       OH_UdsPlainText_SetContent(udsPlainText, text);
       OH_UdsHtml* udsHtml = OH_UdsHtml_Create();
       OH_UdsHtml_SetContent(udsHtml, "hello world");
       OH_UdmfRecord* record = OH_UdmfRecord_Create();
       OH_UdmfRecord_AddPlainText(record, udsPlainText);
       OH_UdmfRecord_AddHtml(record, udsHtml);
       // 3. 创建OH_UdmfData对象，并向OH_UdmfData中添加OH_UdmfRecord
       OH_UdmfData* data = OH_UdmfData_Create();
       OH_UdmfData_AddRecord(data, record);
       // 4. 将数据写入剪贴板
       OH_Pasteboard_SetData(pasteboard, data);
       // 5. 使用完销毁指针
       OH_UdsPlainText_Destroy(udsPlainText);
       OH_UdsHtml_Destroy(udsHtml);
       OH_UdmfRecord_Destroy(record);
       OH_UdmfData_Destroy(data);
       OH_Pasteboard_Destroy(pasteboard);
       // ...
   }
   ```
6. 从剪贴板读取数据。

   ```
   static napi_value NAPI_Pasteboard_get(napi_env env, napi_callback_info info)
   {
       // 1. 创建一个剪贴板实例
       OH_Pasteboard* pasteboard = OH_Pasteboard_Create();
       if (pasteboard == nullptr) {
           OH_LOG_INFO(LOG_APP, "Failed to create pasteboard instance.");
       };
       // 2. 判断剪贴板中是否有文本类型数据
       bool hasPlainTextData = OH_Pasteboard_HasType(pasteboard, "text/plain");
       if (hasPlainTextData) {
           // 3. 从剪贴板中获取统一类型数据OH_UdmfData
           int ret = 0;
           OH_UdmfData* udmfData = OH_Pasteboard_GetData(pasteboard, &ret);
           if (udmfData == nullptr) {
               OH_LOG_INFO(LOG_APP, "Failed to get data from pasteboard.");
           };
           // 4. 从OH_UdmfData中获取第一个数据记录
           OH_UdmfRecord* record = OH_UdmfData_GetRecord(udmfData, 0);
           if (record == nullptr) {
               OH_LOG_INFO(LOG_APP, "Failed to get record from udmfData.");
           };
           // 5. 从数据记录中获取文本数据内容
           OH_UdsPlainText* plainText = OH_UdsPlainText_Create();
           if (plainText == nullptr) {
               OH_LOG_INFO(LOG_APP, "Failed to create plain text object.");
           };
           OH_UdmfRecord_GetPlainText(record, plainText);
           const char* content = OH_UdsPlainText_GetContent(plainText);
           if (content == nullptr) {
               OH_LOG_INFO(LOG_APP, "Failed to get content from plain text.");
           }
           napi_value result;
           napi_create_string_utf8(env, content, strlen(content), &result);
           // 6. 使用完销毁指针
           OH_UdsPlainText_Destroy(plainText);
           OH_UdmfRecord_Destroy(record);
           return result;
       } else {
           OH_LOG_INFO(LOG_APP, "No plain text data in pasteboard.");
       }
       OH_Pasteboard_Destroy(pasteboard);
   }
   ```
