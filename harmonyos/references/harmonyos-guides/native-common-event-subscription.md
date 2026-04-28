---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-common-event-subscription
title: 订阅公共事件（C/C++）
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 进程线程通信 > 使用公共事件进行进程间通信 > 订阅公共事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:88d59443d3c4b87ff2cc4f61223f9da964f094d16bebf744bd801f717eb4eb94
---

## 场景介绍

通过[OH\_CommonEvent\_CreateSubscriber](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_createsubscriber)创建的订阅者可以对某个公共事件进行订阅，如果有订阅的事件发布那么订阅了这个事件的订阅者将会收到该事件及其传递的参数，也可以通过订阅者对象进一步处理有序公共事件。

## 接口说明

详细的API说明请参考[oh\_commonevent.h](../harmonyos-references/capi-oh-commonevent-h.md)。

| 接口名 | 描述 |
| --- | --- |
| [CommonEvent\_SubscribeInfo\* OH\_CommonEvent\_CreateSubscribeInfo(const char\* events[], int32\_t eventsNum)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_createsubscribeinfo) | 创建订阅者信息。 |
| [void OH\_CommonEvent\_DestroySubscribeInfo(CommonEvent\_SubscribeInfo\* info)](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_destroysubscribeinfo) | 销毁订阅者信息。 |
| [CommonEvent\_Subscriber\* OH\_CommonEvent\_CreateSubscriber(const CommonEvent\_SubscribeInfo\* info, CommonEvent\_ReceiveCallback callback)](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_createsubscriber) | 创建订阅者。 |
| [void OH\_CommonEvent\_DestroySubscriber(CommonEvent\_Subscriber\* subscriber)](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_destroysubscriber) | 销毁订阅者。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_Subscribe(const CommonEvent\_Subscriber\* subscriber)](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_subscribe) | 订阅事件。 |
| [bool OH\_CommonEvent\_AbortCommonEvent(CommonEvent\_Subscriber\* subscriber)](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_abortcommonevent) | 中止当前的有序公共事件。 |
| [bool OH\_CommonEvent\_ClearAbortCommonEvent(CommonEvent\_Subscriber\* subscriber)](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_clearabortcommonevent) | 取消当前有序公共事件的中止状态。 |
| [bool OH\_CommonEvent\_FinishCommonEvent(CommonEvent\_Subscriber\* subscriber)](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_finishcommonevent) | 结束对当前有序公共事件的处理。 |

## 开发步骤

1. 引用头文件。

   ```
   1. #include <cstdint>
   2. #include <cstring>
   3. #include "hilog/log.h"
   4. #include "BasicServicesKit/oh_commonevent.h"
   ```

   [common\_event\_subscribe.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/common_event/NativeCommonEvent/entry/src/main/cpp/common_event_subscribe.h#L19-L24)
2. 在CMake脚本中添加动态链接库。

   ```
   1. target_link_libraries(entry PUBLIC
   2. libace_napi.z.so
   3. libhilog_ndk.z.so
   4. libohcommonevent.so
   5. )
   ```
3. 创建订阅者信息。

   通过[OH\_CommonEvent\_CreateSubscribeInfo](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_createsubscribeinfo)创建订阅者信息。

   ```
   1. CommonEvent_SubscribeInfo *CreateSubscribeInfo(const char *events[], int32_t eventsNum, const char *permission,
   2. const char *bundleName)
   3. {
   4. int32_t ret = -1;
   5. // 创建订阅者信息
   6. CommonEvent_SubscribeInfo *info = OH_CommonEvent_CreateSubscribeInfo(events, eventsNum);

   8. // 设置发布者权限
   9. ret = OH_CommonEvent_SetPublisherPermission(info, permission);
   10. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetPublisherPermission ret <%{public}d>.", ret);

   12. // 设置发布者包名称
   13. ret = OH_CommonEvent_SetPublisherBundleName(info, bundleName);
   14. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetPublisherBundleName ret <%{public}d>.", ret);
   15. return info;
   16. }

   18. // 销毁订阅者信息
   19. void DestroySubscribeInfo(CommonEvent_SubscribeInfo *info)
   20. {
   21. OH_CommonEvent_DestroySubscribeInfo(info);
   22. info = nullptr;
   23. }
   ```

   [common\_event\_subscribe.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/common_event/NativeCommonEvent/entry/src/main/cpp/common_event_subscribe.cpp#L17-L42)
4. 创建订阅者。

   创建订阅者时需传入公共事件的回调函数[CommonEvent\_ReceiveCallback](../harmonyos-references/capi-oh-commonevent-h.md#commonevent_receivecallback)。待事件发布时，订阅者会接收到回调数据[CommonEvent\_RcvData](../harmonyos-references/capi-oh-commonevent-h.md#结构体)。

   ```
   1. // 公共事件回调函数
   2. void OnReceive(const CommonEvent_RcvData *data)
   3. {
   4. // 获取回调公共事件名称
   5. const char *event = OH_CommonEvent_GetEventFromRcvData(data);

   7. // 获取回调公共事件结果代码
   8. int code = OH_CommonEvent_GetCodeFromRcvData(data);

   10. // 获取回调公共事件自定义结果数据
   11. const char *retData = OH_CommonEvent_GetDataStrFromRcvData(data);

   13. // 获取回调公共事件包名称
   14. const char *bundle = OH_CommonEvent_GetBundleNameFromRcvData(data);
   15. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST",
   16. "event: %{public}s, code: %{public}d, data: %{public}s, bundle: %{public}s", event, code, retData,
   17. bundle);
   18. }
   ```

   [common\_event\_subscribe.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/common_event/NativeCommonEvent/entry/src/main/cpp/common_event_subscribe.cpp#L44-L63)

   通过[CommonEvent\_Parameters](../harmonyos-references/capi-oh-commonevent-h.md#变量)传入key来获取附加信息内容。

   ```
   1. void GetParameters(const CommonEvent_RcvData *data)
   2. {
   3. // 获取回调公共事件附件信息
   4. bool exists = false;
   5. const CommonEvent_Parameters *parameters = OH_CommonEvent_GetParametersFromRcvData(data);

   7. // 检查公共事件附加信息中是否包含某个键值对信息
   8. exists = OH_CommonEvent_HasKeyInParameters(parameters, "intKey");
   9. // 获取公共事件附加信息中int数据信息
   10. int intValue = OH_CommonEvent_GetIntFromParameters(parameters, "intKey", 10);
   11. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "exists = %{public}d, intValue = %{public}d", exists, intValue);

   13. // 补充说明：除int类型外，还支持获取以下多种类型的公共事件附加信息，调用对应鸿蒙API即可：
   14. // - 基础数据类型：bool（OH_CommonEvent_GetBoolFromParameters）、long（OH_CommonEvent_GetLongFromParameters）、
   15. // double（OH_CommonEvent_GetDoubleFromParameters）、char（OH_CommonEvent_GetCharFromParameters）
   16. // -
   17. // 数组数据类型：int数组（OH_CommonEvent_GetIntArrayFromParameters）、long数组（OH_CommonEvent_GetLongArrayFromParameters）、
   18. // double数组（OH_CommonEvent_GetDoubleArrayFromParameters）、char数组（OH_CommonEvent_GetCharArrayFromParameters）、
   19. // bool数组（OH_CommonEvent_GetBoolArrayFromParameters）
   20. // 所有类型均支持通过OH_CommonEvent_HasKeyInParameters先校验键是否存在，避免获取失败
   21. }
   ```

   [common\_event\_subscribe.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/common_event/NativeCommonEvent/entry/src/main/cpp/common_event_subscribe.cpp#L65-L87)

   通过[OH\_CommonEvent\_CreateSubscriber](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_createsubscriber)创建订阅者，传入订阅者信息[CommonEvent\_SubscribeInfo](../harmonyos-references/capi-oh-commonevent-h.md#结构体)和步骤4公共事件回调函数OnReceive。

   ```
   1. // 创建订阅者
   2. CommonEvent_Subscriber *CreateSubscriber(CommonEvent_SubscribeInfo *info)
   3. {
   4. return OH_CommonEvent_CreateSubscriber(info, OnReceive);
   5. }

   7. // 销毁订阅者
   8. void DestroySubscriber(CommonEvent_Subscriber *Subscriber)
   9. {
   10. OH_CommonEvent_DestroySubscriber(Subscriber);
   11. Subscriber = nullptr;
   12. }
   ```

   [common\_event\_subscribe.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/common_event/NativeCommonEvent/entry/src/main/cpp/common_event_subscribe.cpp#L228-L241)
5. 订阅事件。

   通过[OH\_CommonEvent\_Subscribe](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_subscribe)订阅事件。

   ```
   1. void Subscribe(CommonEvent_Subscriber *subscriber)
   2. {
   3. // 通过传入订阅者来订阅事件
   4. int32_t ret = OH_CommonEvent_Subscribe(subscriber);
   5. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_Subscribe ret <%{public}d>.", ret);
   6. }
   ```

   [common\_event\_subscribe.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/common_event/NativeCommonEvent/entry/src/main/cpp/common_event_subscribe.cpp#L243-L250)
6. （可选）当订阅的事件为有序公共事件时，可以选择进一步处理有序公共事件。

   根据订阅者设置的优先级等级，优先将公共事件发送给优先级较高的订阅者，等待其成功接收该公共事件之后再将事件发送给优先级较低的订阅者。如果有多个订阅者具有相同的优先级，则他们将随机接收到公共事件。

   注意

   在订阅者收到公共事件之后，才能通过以下接口进一步处理有序公共事件。

   * 中止当前的有序公共事件。

     通过[OH\_CommonEvent\_AbortCommonEvent](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_abortcommonevent)与[OH\_CommonEvent\_FinishCommonEvent](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_finishcommonevent)配合使用，可以中止当前的有序公共事件，使该公共事件不再向下一个订阅者传递。

     ```
     1. void AbortCommonEvent(CommonEvent_Subscriber *subscriber)
     2. {
     3. // 判断是否为有序公共事件
     4. if (!OH_CommonEvent_IsOrderedCommonEvent(subscriber)) {
     5. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "Not ordered common event.");
     6. return;
     7. }
     8. // 中止有序事件
     9. if (OH_CommonEvent_AbortCommonEvent(subscriber)) {
     10. if (OH_CommonEvent_FinishCommonEvent(subscriber)) {
     11. // 获取当前有序公共事件是否处于中止状态
     12. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "Abort common event success, Get abort <%{public}d>.",
     13. OH_CommonEvent_GetAbortCommonEvent(subscriber));
     14. }
     15. } else {
     16. OH_LOG_Print(LOG_APP, LOG_ERROR, 1, "CES_TEST", "Abort common event failed.");
     17. }
     18. }
     ```

     [common\_event\_subscribe.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/common_event/NativeCommonEvent/entry/src/main/cpp/common_event_subscribe.cpp#L252-L271)
   * 取消当前有序公共事件的中止状态。

     通过[OH\_CommonEvent\_ClearAbortCommonEvent](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_clearabortcommonevent)与[OH\_CommonEvent\_FinishCommonEvent](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_finishcommonevent)配合使用，可以取消当前有序公共事件的中止状态，使该公共事件继续向下一个订阅者传递。

     ```
     1. void ClearAbortCommonEvent(CommonEvent_Subscriber *subscriber)
     2. {
     3. // 判断是否为有序公共事件
     4. if (!OH_CommonEvent_IsOrderedCommonEvent(subscriber)) {
     5. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "Not ordered common event.");
     6. return;
     7. }
     8. // 中止有序事件
     9. if (!OH_CommonEvent_AbortCommonEvent(subscriber)) {
     10. OH_LOG_Print(LOG_APP, LOG_ERROR, 1, "CES_TEST", "Abort common event failed.");
     11. return;
     12. }
     13. // 取消中止有序事件
     14. if (OH_CommonEvent_ClearAbortCommonEvent(subscriber)) {
     15. if (OH_CommonEvent_FinishCommonEvent(subscriber)) {
     16. // 获取当前有序公共事件是否处于中止状态
     17. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "Clear abort common event success, Get abort <%{public}d>.",
     18. OH_CommonEvent_GetAbortCommonEvent(subscriber));
     19. }
     20. } else {
     21. OH_LOG_Print(LOG_APP, LOG_ERROR, 1, "CES_TEST", "Clear abort common event failed.");
     22. }
     23. }
     ```

     [common\_event\_subscribe.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/common_event/NativeCommonEvent/entry/src/main/cpp/common_event_subscribe.cpp#L273-L297)
   * 修改有序公共事件的内容。

     通过[OH\_CommonEvent\_SetCodeToSubscriber](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_setcodetosubscriber)与[OH\_CommonEvent\_SetDataToSubscriber](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_setdatatosubscriber)设置有序公共事件的代码和数据。

     ```
     1. void SetToSubscriber(CommonEvent_Subscriber *subscriber, const int32_t code, const char *data)
     2. {
     3. // 设置有序公共事件的代码
     4. if (!OH_CommonEvent_SetCodeToSubscriber(subscriber, code)) {
     5. OH_LOG_Print(LOG_APP, LOG_ERROR, 1, "CES_TEST", "OH_CommonEvent_SetCodeToSubscriber failed.");
     6. return;
     7. }
     8. // 设置有序公共事件的数据
     9. size_t dataLength = strlen(data);
     10. if (!OH_CommonEvent_SetDataToSubscriber(subscriber, data, dataLength)) {
     11. OH_LOG_Print(LOG_APP, LOG_ERROR, 1, "CES_TEST", "OH_CommonEvent_SetDataToSubscriber failed.");
     12. return;
     13. }
     14. }

     16. void GetFromSubscriber(CommonEvent_Subscriber *subscriber)
     17. {
     18. // 获取有序公共事件的数据和代码
     19. const char *data = OH_CommonEvent_GetDataFromSubscriber(subscriber);
     20. int32_t code = OH_CommonEvent_GetCodeFromSubscriber(subscriber);
     21. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "Subscriber data <%{public}s>, code <%{public}d>.", data, code);
     22. }
     ```

     [common\_event\_subscribe.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/common_event/NativeCommonEvent/entry/src/main/cpp/common_event_subscribe.cpp#L299-L322)
