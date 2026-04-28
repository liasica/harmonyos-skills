---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-common-event-publish
title: 发布公共事件（C/C++）
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 进程线程通信 > 使用公共事件进行进程间通信 > 发布公共事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f06db559c5f9a66ccd1501917eb1a5f0e26d25d5168c26e31e1dd28d5a752eb3
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

   ```
   1. #include <cstdint>
   2. #include <cstring>
   3. #include "hilog/log.h"
   4. #include "BasicServicesKit/oh_commonevent.h"

   6. const long PARAM_LONG_VALUE1 = 2147483646;
   7. const long PARAM_LONG_VALUE2 = 2147483645;
   8. const long PARAM_LONG_VALUE3 = 555;
   9. const double PARAM_DOUBLE_VALUE1 = 11.22;
   10. const double PARAM_DOUBLE_VALUE2 = 33.44;
   11. const double PARAM_DOUBLE_VALUE3 = 55.66;
   12. const int PARAM_INT_VALUE1 = 10;
   13. const int PARAM_INT_VALUE2 = 123;
   14. const int PARAM_INT_VALUE3 = 234;
   15. const int PARAM_INT_VALUE4 = 567;
   ```

   [common\_event\_publish.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/common_event/NativeCommonEvent/entry/src/main/cpp/common_event_publish.h#L19-L35)
2. 在CMake脚本中添加动态链接库。

   ```
   1. target_link_libraries(entry PUBLIC
   2. libace_napi.z.so
   3. libhilog_ndk.z.so
   4. libohcommonevent.so
   5. )
   ```
3. （可选）创建公共事件属性对象。

   发布携带数据的公共事件时，需要通过[OH\_CommonEvent\_CreatePublishInfo](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_createpublishinfo)创建公共事件属性对象，并通过以下接口设置公共事件属性。

   ```
   1. // 创建并添加公共事件属性附加信息
   2. CommonEvent_Parameters *CreateParameters()
   3. {
   4. int32_t ret = -1;
   5. // 创建公共事件附加信息
   6. CommonEvent_Parameters *param = OH_CommonEvent_CreateParameters();

   8. // 设置int类型附加信息和key
   9. ret = OH_CommonEvent_SetIntToParameters(param, "intKey", PARAM_INT_VALUE1);
   10. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetIntToParameters ret <%{public}d>.", ret);

   12. // 设置int数组类型附加信息和key
   13. int intArray[] = {PARAM_INT_VALUE2, PARAM_INT_VALUE3, PARAM_INT_VALUE4};
   14. size_t arraySize = sizeof(intArray) / sizeof(intArray[0]);
   15. ret = OH_CommonEvent_SetIntArrayToParameters(param, "intArrayKey", intArray, arraySize);
   16. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetIntArrayToParameters ret <%{public}d>.", ret);

   18. // 设置long类型附加信息和key
   19. ret = OH_CommonEvent_SetLongToParameters(param, "longKey", PARAM_LONG_VALUE1);
   20. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetLongToParameters ret <%{public}d>.", ret);

   22. // 设置long数组类型附加信息和key
   23. long longArray[] = {PARAM_LONG_VALUE1, PARAM_LONG_VALUE3, PARAM_LONG_VALUE2};
   24. ret = OH_CommonEvent_SetLongArrayToParameters(param, "longArrayKey", longArray, arraySize);
   25. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetLongArrayToParameters ret <%{public}d>.", ret);

   27. // 设置double类型附加信息和key
   28. ret = OH_CommonEvent_SetDoubleToParameters(param, "doubleKey", PARAM_DOUBLE_VALUE1);
   29. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetDoubleToParameters ret <%{public}d>.", ret);

   31. // 设置double数组类型附加信息和key
   32. double doubleArray[] = {PARAM_DOUBLE_VALUE1, PARAM_DOUBLE_VALUE2, PARAM_DOUBLE_VALUE3};
   33. ret = OH_CommonEvent_SetDoubleArrayToParameters(param, "doubleArrayKey", doubleArray, arraySize);
   34. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetDoubleArrayToParameters ret <%{public}d>.", ret);

   36. // 设置boolean类型附加信息和key
   37. ret = OH_CommonEvent_SetBoolToParameters(param, "boolKey", true);
   38. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetBoolToParameters ret <%{public}d>.", ret);

   40. // 设置boolean数组类型附加信息和key
   41. bool boolArray[] = {true, false, true};
   42. ret = OH_CommonEvent_SetBoolArrayToParameters(param, "boolArrayKey", boolArray, arraySize);
   43. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetBoolArrayToParameters ret <%{public}d>.", ret);

   45. // 设置char类型附加信息和key
   46. ret = OH_CommonEvent_SetCharToParameters(param, "charKey", 'A');
   47. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetCharToParameters ret <%{public}d>.", ret);

   49. // 设置char数组类型附加信息和key
   50. const char *value = "Char Array";
   51. size_t valueLength = strlen(value);
   52. ret = OH_CommonEvent_SetCharArrayToParameters(param, "charArrayKey", value, valueLength);
   53. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetCharArrayToParameters ret <%{public}d>.", ret);
   54. return param;
   55. }

   57. // 设置公共事件属性
   58. void SetPublishInfo(const char *bundleName, const char *permissions[], int32_t num, const int32_t code,
   59. const char *data)
   60. {
   61. int32_t ret = -1;
   62. // 创建publishInfo，设置是否为有序公共事件，取值为true，表示有序公共事件；取值为false，表示无序公共事件
   63. CommonEvent_PublishInfo *info = OH_CommonEvent_CreatePublishInfo(true);

   65. // 设置公共事件包名称
   66. ret = OH_CommonEvent_SetPublishInfoBundleName(info, bundleName);
   67. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetPublishInfoBundleName ret <%{public}d>.", ret);

   69. // 设置公共事件权限，参数为权限数组和权限的数量
   70. ret = OH_CommonEvent_SetPublishInfoPermissions(info, permissions, num);
   71. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetPublishInfoPermissions ret <%{public}d>.", ret);

   73. // 设置公共事件结果码
   74. ret = OH_CommonEvent_SetPublishInfoCode(info, code);
   75. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetPublishInfoCode ret <%{public}d>.", ret);

   77. // 设置公共事件结果数据
   78. size_t dataLength = strlen(data);
   79. ret = OH_CommonEvent_SetPublishInfoData(info, data, dataLength);
   80. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetPublishInfoData ret <%{public}d>.", ret);

   82. // 设置公共事件附加信息
   83. CommonEvent_Parameters *param = CreateParameters();
   84. ret = OH_CommonEvent_SetPublishInfoParameters(info, param);
   85. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_SetPublishInfoParameters ret <%{public}d>.", ret);
   86. }
   ```

   [common\_event\_publish.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/common_event/NativeCommonEvent/entry/src/main/cpp/common_event_publish.cpp#L35-L122)
4. 发布公共事件。

   * 通过[OH\_CommonEvent\_Publish](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_publish)发布不携带信息的公共事件。

     说明

     不携带信息的公共事件，只能发布为无序公共事件。

     ```
     1. void Publish(const char *event)
     2. {
     3. int32_t ret = OH_CommonEvent_Publish(event);
     4. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_Publish ret <%{public}d>.", ret);
     5. }
     ```

     [common\_event\_publish.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/common_event/NativeCommonEvent/entry/src/main/cpp/common_event_publish.cpp#L18-L24)
   * 通过[OH\_CommonEvent\_PublishWithInfo](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_publishwithinfo)发布携带信息的公共事件。

     ```
     1. void PublishWithInfo(const char *event, CommonEvent_PublishInfo *info)
     2. {
     3. // 创建时带入公共事件属性对象
     4. int32_t ret = OH_CommonEvent_PublishWithInfo(event, info);
     5. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_PublishWithInfo ret <%{public}d>.", ret);
     6. }
     ```

     [common\_event\_publish.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/common_event/NativeCommonEvent/entry/src/main/cpp/common_event_publish.cpp#L26-L33)
5. 销毁公共事件对象。

   如果后续无需使用已创建的公共事件对象来发布公共事件，需要先通过[OH\_CommonEvent\_DestroyParameters](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_destroyparameters)销毁CommonEvent\_Parameters对象，然后再通过[OH\_CommonEvent\_DestroyPublishInfo](../harmonyos-references/capi-oh-commonevent-h.md#oh_commonevent_destroypublishinfo)销毁公共事件对象。

   ```
   1. void DestroyPublishInfo(CommonEvent_Parameters *param, CommonEvent_PublishInfo *info)
   2. {
   3. // 先销毁Parameters
   4. OH_CommonEvent_DestroyParameters(param);
   5. param = nullptr;
   6. // 销毁PublishInfo
   7. OH_CommonEvent_DestroyPublishInfo(info);
   8. info = nullptr;
   9. }
   ```

   [common\_event\_publish.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/common_event/NativeCommonEvent/entry/src/main/cpp/common_event_publish.cpp#L124-L134)
