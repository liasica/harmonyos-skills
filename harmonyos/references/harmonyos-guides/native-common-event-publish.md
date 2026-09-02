---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-common-event-publish
title: 发布公共事件（C/C++）
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 进程线程通信 > 使用公共事件进行进程间通信 > 发布公共事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:35+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:94923c09b54497e342fbb63da6af808b787c138d5ab0edb0203b2ef323905824
---

## 场景介绍

当需要发布某个公共事件时，可以通过[OH\_CommonEvent\_Publish](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_publish)和[OH\_CommonEvent\_PublishWithInfo](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_publishwithinfo)方法发布事件。发布的公共事件可以携带数据，供订阅者解析并进行下一步处理。

## 接口说明

详细的API说明请参考[oh\_commonevent.h](../harmonyos-references/capi-oh-commonevent-h.md)。

| 接口名 | 描述 |
| --- | --- |
| [struct CommonEvent\_PublishInfo](../harmonyos-references/capi-oh-commonevent-commonevent-publishinfo.md) | 发布公共事件时使用的公共事件属性对象。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_Publish(const char\* event)](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_publish) | 发布公共事件。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_PublishWithInfo(const char\* event, const CommonEvent\_PublishInfo\* info)](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_publishwithinfo) | 发布带有指定属性的公共事件。 |
| [CommonEvent\_PublishInfo\* OH\_CommonEvent\_CreatePublishInfo(bool ordered)](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_createpublishinfo) | 创建公共事件属性对象。 |
| [void OH\_CommonEvent\_DestroyPublishInfo(CommonEvent\_PublishInfo\* info)](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_destroypublishinfo) | 销毁公共事件属性对象。 |
| [CommonEvent\_Parameters\* OH\_CommonEvent\_CreateParameters()](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_createparameters) | 创建公共事件附加信息对象。 |
| [void OH\_CommonEvent\_DestroyParameters(CommonEvent\_Parameters\* param)](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_destroyparameters) | 销毁公共事件附加信息对象。 |

## 开发步骤

1. 引用头文件。

   ```c
   #include <cstdint>
   #include <cstring>
   #include "hilog/log.h"
   #include "BasicServicesKit/oh_commonevent.h"

   const long PARAM_LONG_VALUE1 = 2147483646;
   const long PARAM_LONG_VALUE2 = 2147483645;
   const long PARAM_LONG_VALUE3 = 555;
   const double PARAM_DOUBLE_VALUE1 = 11.22;
   const double PARAM_DOUBLE_VALUE2 = 33.44;
   const double PARAM_DOUBLE_VALUE3 = 55.66;
   const int PARAM_INT_VALUE1 = 10;
   const int PARAM_INT_VALUE2 = 123;
   const int PARAM_INT_VALUE3 = 234;
   const int PARAM_INT_VALUE4 = 567;
   ```
2. 在CMake脚本中添加动态链接库。

   ```txt
   target_link_libraries(entry PUBLIC
       libace_napi.z.so
       libhilog_ndk.z.so
       libohcommonevent.so
   )
   ```
3. （可选）创建公共事件属性对象。

   发布携带数据的公共事件时，需要通过[OH\_CommonEvent\_CreatePublishInfo](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_createpublishinfo)创建公共事件属性对象，并通过以下接口设置公共事件属性。

   ```
   // 创建并添加公共事件属性附加信息
   CommonEvent_Parameters *CreateParameters()
   {
       int32_t ret = -1;
       // 创建公共事件附加信息
       CommonEvent_Parameters *param = OH_CommonEvent_CreateParameters();

       // 设置int类型附加信息和key
       ret = OH_CommonEvent_SetIntToParameters(param, "intKey", PARAM_INT_VALUE1);
       OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetIntToParameters ret <%{public}d>.", ret);

       // 设置int数组类型附加信息和key
       int intArray[] = {PARAM_INT_VALUE2, PARAM_INT_VALUE3, PARAM_INT_VALUE4};
       size_t arraySize = sizeof(intArray) / sizeof(intArray[0]);
       ret = OH_CommonEvent_SetIntArrayToParameters(param, "intArrayKey", intArray, arraySize);
       OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetIntArrayToParameters ret <%{public}d>.", ret);

       // 设置long类型附加信息和key
       ret = OH_CommonEvent_SetLongToParameters(param, "longKey", PARAM_LONG_VALUE1);
       OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetLongToParameters ret <%{public}d>.", ret);

       // 设置long数组类型附加信息和key
       long longArray[] = {PARAM_LONG_VALUE1, PARAM_LONG_VALUE3, PARAM_LONG_VALUE2};
       ret = OH_CommonEvent_SetLongArrayToParameters(param, "longArrayKey", longArray, arraySize);
       OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetLongArrayToParameters ret <%{public}d>.", ret);

       // 设置double类型附加信息和key
       ret = OH_CommonEvent_SetDoubleToParameters(param, "doubleKey", PARAM_DOUBLE_VALUE1);
       OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetDoubleToParameters ret <%{public}d>.", ret);

       // 设置double数组类型附加信息和key
       double doubleArray[] = {PARAM_DOUBLE_VALUE1, PARAM_DOUBLE_VALUE2, PARAM_DOUBLE_VALUE3};
       ret = OH_CommonEvent_SetDoubleArrayToParameters(param, "doubleArrayKey", doubleArray, arraySize);
       OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetDoubleArrayToParameters ret <%{public}d>.", ret);

       // 设置boolean类型附加信息和key
       ret = OH_CommonEvent_SetBoolToParameters(param, "boolKey", true);
       OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetBoolToParameters ret <%{public}d>.", ret);

       // 设置boolean数组类型附加信息和key
       bool boolArray[] = {true, false, true};
       ret = OH_CommonEvent_SetBoolArrayToParameters(param, "boolArrayKey", boolArray, arraySize);
       OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetBoolArrayToParameters ret <%{public}d>.", ret);

       // 设置char类型附加信息和key
       ret = OH_CommonEvent_SetCharToParameters(param, "charKey", 'A');
       OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetCharToParameters ret <%{public}d>.", ret);

       // 设置char数组类型附加信息和key
       const char *value = "Char Array";
       size_t valueLength = strlen(value);
       ret = OH_CommonEvent_SetCharArrayToParameters(param, "charArrayKey", value, valueLength);
       OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetCharArrayToParameters ret <%{public}d>.", ret);
       return param;
   }

   // 设置公共事件属性
   void SetPublishInfo(const char *bundleName, const char *permissions[], int32_t num, const int32_t code,
                       const char *data)
   {
       int32_t ret = -1;
       // 创建publishInfo，设置是否为有序公共事件，取值为true，表示有序公共事件；取值为false，表示无序公共事件
       CommonEvent_PublishInfo *info = OH_CommonEvent_CreatePublishInfo(true);

       // 设置公共事件包名称
       ret = OH_CommonEvent_SetPublishInfoBundleName(info, bundleName);
       OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetPublishInfoBundleName ret <%{public}d>.", ret);

       // 设置公共事件权限，参数为权限数组和权限的数量
       ret = OH_CommonEvent_SetPublishInfoPermissions(info, permissions, num);
       OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetPublishInfoPermissions ret <%{public}d>.", ret);

       // 设置公共事件结果码
       ret = OH_CommonEvent_SetPublishInfoCode(info, code);
       OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetPublishInfoCode ret <%{public}d>.", ret);

       // 设置公共事件结果数据
       size_t dataLength = strlen(data);
       ret = OH_CommonEvent_SetPublishInfoData(info, data, dataLength);
       OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetPublishInfoData ret <%{public}d>.", ret);

       // 设置公共事件附加信息
       CommonEvent_Parameters *param = CreateParameters();
       ret = OH_CommonEvent_SetPublishInfoParameters(info, param);
       OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetPublishInfoParameters ret <%{public}d>.", ret);
   }
   ```
4. 发布公共事件。

   * 通过[OH\_CommonEvent\_Publish](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_publish)发布不携带信息的公共事件。

     **说明** 

     不携带信息的公共事件，只能发布为无序公共事件。

     ```
     void Publish(const char *event)
     {
         int32_t ret = OH_CommonEvent_Publish(event);
         OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_Publish ret <%{public}d>.", ret);
     }
     ```
   * 通过[OH\_CommonEvent\_PublishWithInfo](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_publishwithinfo)发布携带信息的公共事件。

     ```
     void PublishWithInfo(const char *event, CommonEvent_PublishInfo *info)
     {
         // 创建时带入公共事件属性对象
         int32_t ret = OH_CommonEvent_PublishWithInfo(event, info);
         OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_PublishWithInfo ret <%{public}d>.", ret);
     }
     ```
5. 销毁公共事件对象。

   如果后续无需使用已创建的公共事件对象来发布公共事件，需要先通过[OH\_CommonEvent\_DestroyParameters](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_destroyparameters)销毁CommonEvent\_Parameters对象，然后再通过[OH\_CommonEvent\_DestroyPublishInfo](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_destroypublishinfo)销毁公共事件对象。

   ```
   void DestroyPublishInfo(CommonEvent_Parameters *param, CommonEvent_PublishInfo *info)
   {
       // 先销毁Parameters
       OH_CommonEvent_DestroyParameters(param);
       param = nullptr;
       // 销毁PublishInfo
       OH_CommonEvent_DestroyPublishInfo(info);
       info = nullptr;
   }
   ```
