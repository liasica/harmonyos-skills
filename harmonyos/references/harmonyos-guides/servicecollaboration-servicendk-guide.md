---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/servicecollaboration-servicendk-guide
title: 跨设备互通NDK开发指导
breadcrumb: 指南 > 系统 > 网络 > Service Collaboration Kit（协同服务） > 跨设备互通NDK（C） > 跨设备互通NDK开发指导
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:06+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:8ea70f9b1f751f73c1df02b8cc8168d5ba5b1248dd39f1cbacc965d202390709
---

跨设备互通提供相机、扫描以及图库（图片和视频）的跨设备调用能力，TV、Tablet或PC/2in1设备可以调用Phone的相机、扫描、图库等功能，并且从API 6.1.0(23)开始支持TV、Phone、Tablet或PC/2in1设备调用支持拍照、扫描、选择图库中图片与视频能力的Phone，支持拍照、扫描、选择图库中图片与视频能力的Tablet，以及支持选择图库中图片与视频能力的PC/2in1设备。

## 场景介绍

您通过此能力实现跨设备交互，可以使用其他设备的相机、扫描和图库功能。

## 约束与限制

需同时满足以下条件，才能使用该功能：

* **设备限制**

  + 本端设备：HarmonyOS版本为HarmonyOS 5及以上的TV、Tablet或PC/2in1设备，从API 6.1.0(23)开始，支持HarmonyOS版本为HarmonyOS 5及以上的TV、Phone、Tablet或PC/2in1设备。
  + 远端设备：HarmonyOS版本为HarmonyOS 5及以上、具有相机能力的Phone或Tablet设备，从API 6.1.0(23)开始，支持HarmonyOS版本为HarmonyOS 5及以上的Phone、Tablet或PC/2in1设备。
* **使用限制**

  + 双端设备需要登录同一华为账号。
  + 跨设备互通API支持根据特定调用策略调用设备。调用策略：TV、PC/2in1设备可以调用Tablet和Phone，Tablet可以调用Phone，并且在6.1.0(23)之后支持TV、Phone、Tablet或PC/2in1设备调用支持拍照、扫描、选择图库中图片与视频能力的Phone，支持拍照、扫描、选择图库中图片与视频能力的Tablet，以及支持选择图库中图片与视频能力的PC/2in1设备。
  + 双端设备需要打开WLAN和蓝牙开关。条件允许时，建议双端设备接入同一个局域网，可提升唤醒相机的速度。

## 业务流程

1. 通过[HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](../harmonyos-references/servicecollaboration-capi-module.md#hms_servicecollaboration_getcollaborationdeviceinfos)接口获取支持相关能力的设备列表。
2. 通过[HMS\_ServiceCollaboration\_StartCollaboration](../harmonyos-references/servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaboration)接口拉起跨设备互通能力。
3. 对端设备确定回传后，本端处理对端回传的图片。

## 接口说明

在开发具体功能前，请先查阅[参考文档](../harmonyos-references/servicecollaboration-capi-module.md)。

| 接口名 | 描述 |
| --- | --- |
| [HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](../harmonyos-references/servicecollaboration-capi-module.md#hms_servicecollaboration_getcollaborationdeviceinfos) | 获取支持相关能力的设备列表。 |
| [HMS\_ServiceCollaboration\_StartCollaboration](../harmonyos-references/servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaboration) | 拉起跨设备互通能力，回传图片。 |
| [HMS\_ServiceCollaboration\_StopCollaboration](../harmonyos-references/servicecollaboration-capi-module.md#hms_servicecollaboration_stopcollaboration) | 取消跨设备互通能力。 |
| [HMS\_ServiceCollaboration\_StartCollaborationV2](../harmonyos-references/servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaborationv2) | 拉起跨设备互通能力，回传图片和视频。 |

## 开发步骤

1. 引入头文件。

   ```
   #include "service_collaboration/service_collaboration_api.h"
   ```
2. 编写CMakeLists.txt。

   ```text
   cmake_minimum_required(VERSION 3.4.1)
   project(MyApplication)

   set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   if(DEFINED PACKAGE_FIND_FILE)
       include(${PACKAGE_FIND_FILE})
   endif()

   include_directories(${NATIVERENDER_ROOT_PATH}
                       ${NATIVERENDER_ROOT_PATH}/include)
   link_directories(${HMOS_SDK_NATIVE}/sysroot/usr/lib/aarch64-linux-ohos)
   link_directories(${HMOS_SDK_NATIVE}/sysroot/usr/lib/aarch64-linux-ohos)

   add_library(entry SHARED napi_init.cpp)
   target_link_libraries(entry PUBLIC libservice_collaboration_ndk.z.so
   libace_napi.z.so)
   ```
3. 实例代码调用接口，分为以下三步。

   1. 通过调用HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos接口获取设备列表信息，传入需要的ServiceCollaborationFilterType能力数组，接口会返回支持对应能力设备。每个设备中包含所支持的能力类型ServiceCollaborationFilterTypes和设备类型deviceType信息。
   2. 创建回调ServiceCollaborationCallback，其中包括事件回调OnEventProc和图片数据回调OnDataCallbackProc；创建ServiceCollaboration\_SelectInfo，示例中传入了TAKE\_PHOTO能力，并选择了列表的第一个设备。
   3. HMS\_ServiceCollaboration\_StartCollaboration入参传入第二步构造的ServiceCollaborationCallback和ServiceCollaboration\_SelectInfo，此时被调用的设备会拉起相机，操作被拉起相机的设备进行拍照。事件和图片数据会通过第二步构造的回调通知给应用。

   ```
   static int32_t OnEventProc(ServiceCollaborationEventCode code, uint32_t extraCode)
   {
       return 0;
   }

   static int32_t OnDataCallbackProc(ServiceCollaborationEventCode code, ServiceCollaborationDataType dataType,
       uint32_t dataSize, char *data)
   {
       return 0;
   }

   static napi_value HCTS_HMS_ServiceCollaboration_TestDemo(napi_env env, napi_callback_info info)
   {
       int two = 2;
       int three = 3;
       int filter = 1;
       const int size = 3;
       int shouldCancel = 0;

       // 构建所需跨设备互通能力，并调用HMS_ServiceCollaboration_GetCollaborationDeviceInfos接口获取设备信息
       ServiceCollaborationFilterType serviceFilterTypes[size] = {TAKE_PHOTO, SCAN_DOCUMENT, IMAGE_PICKER};
       ServiceCollaboration_CollaborationDeviceInfoSets* sets = HMS_ServiceCollaboration_GetCollaborationDeviceInfos(
           3, serviceFilterTypes);
       // 构建callback回调
       ServiceCollaboration_SelectInfo taskInfo = { TAKE_PHOTO, { 0 } };
       for (uint32_t i = 0; i < sets->size; i++) {
           ServiceCollaboration_CollaborationDeviceInfo *deviceInfo =
               (ServiceCollaboration_CollaborationDeviceInfo *)&(sets->deviceInfoSets[i]);
           if (filter == 1) {
               taskInfo.serviceFilterType = TAKE_PHOTO;
           }
           if (filter == two) {
               taskInfo.serviceFilterType = SCAN_DOCUMENT;
           }
           if (filter == three) {
               taskInfo.serviceFilterType = IMAGE_PICKER;
           }
           std::memcpy(taskInfo.deviceNetworkId, deviceInfo->deviceNetworkId,
               COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH-1);
       }
       ServiceCollaborationCallback callback = {.OnEvent = OnEventProc, .OnDataCallback = OnDataCallbackProc};
       // 传入拍照参数、callback回调并调用HMS_ServiceCollaboration_StartCollaboration接口
       uint32_t id = HMS_ServiceCollaboration_StartCollaboration(&taskInfo, &callback);
       std::this_thread::sleep_for(std::chrono::seconds(three));
       int32_t ret = 0;
       if (shouldCancel) {
           // 三秒后主动调用HMS_ServiceCollaboration_StopCollaboration关闭跨设备互通
           ret = HMS_ServiceCollaboration_StopCollaboration(id);
       }
       napi_value code_napi_value;
       napi_create_double(env, ret, &code_napi_value);
       return code_napi_value;
   }
   ```
