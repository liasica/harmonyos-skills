---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/servicecollaboration-servicendk-guide
title: 跨设备互通NDK开发指导
breadcrumb: 指南 > 系统 > 网络 > Service Collaboration Kit（协同服务） > 跨设备互通NDK（C） > 跨设备互通NDK开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d10c7f8ec97256865adf687d31de074a7bc4d9c1cec754368856b0866fdfc246
---

跨设备互通提供相机、扫描以及图库（图片和视频）的跨设备调用能力，TV、平板或2in1设备可以调用手机的相机、扫描、图库等功能，并且在6.1.0(23)之后支持TV、手机、平板或2in1设备调用支持拍照、扫描、选择图库中图片与视频能力的手机，支持拍照、扫描、选择图库中图片与视频能力的平板，以及支持选择图库中图片与视频能力的2in1设备。

## 场景介绍

您通过此能力实现跨设备交互，可以使用其他设备的相机、扫描和图库功能。

## 约束与限制

需同时满足以下条件，才能使用该功能：

* **设备限制**

  + 本端设备：HarmonyOS版本为HarmonyOS NEXT及以上的TV、平板或2in1设备。
  + 远端设备：HarmonyOS版本为HarmonyOS NEXT及以上、具有相机能力的手机或平板设备。
* **使用限制**

  + 双端设备需要登录同一华为账号。
  + 跨设备互通API支持根据特定调用策略调用设备。调用策略：TV、2in1设备可以调用平板和手机，平板可以调用手机，并且在6.1.0(23)之后支持TV、手机、平板或2in1设备调用支持拍照、扫描、选择图库中图片与视频能力的手机，支持拍照、扫描、选择图库中图片与视频能力的平板，以及支持选择图库中图片与视频能力的2in1设备。
  + 双端设备需要打开WLAN和蓝牙开关。

    条件允许时，建议双端设备接入同一个局域网，可提升唤醒相机的速度。

## 业务流程

1. 通过[HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](../harmonyos-references/servicecollaboration-capi-module.md#hms_servicecollaboration_getcollaborationdeviceinfos)接口获取设备能力列表。
2. 通过[HMS\_ServiceCollaboration\_StartCollaboration](../harmonyos-references/servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaboration)接口拉起跨设备互通能力。
3. 对端设备确定回传后，本端处理对端回传的图片。

## 接口说明

在开发具体功能前，请先查阅[参考文档](../harmonyos-references/servicecollaboration-capi-module.md)。

| 接口名 | 描述 |
| --- | --- |
| [HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](../harmonyos-references/servicecollaboration-capi-module.md#hms_servicecollaboration_getcollaborationdeviceinfos) | 获取跨设备互通可用的设备信息。 |
| [HMS\_ServiceCollaboration\_StartCollaboration](../harmonyos-references/servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaboration) | 拉起跨设备互通能力，回传图片。 |
| [HMS\_ServiceCollaboration\_StopCollaboration](../harmonyos-references/servicecollaboration-capi-module.md#hms_servicecollaboration_stopcollaboration) | 取消跨设备互通能力。 |
| [HMS\_ServiceCollaboration\_StartCollaborationV2](../harmonyos-references/servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaborationv2) | 拉起跨设备互通能力, 回传图片和视频 |

## 开发步骤

1. 引入头文件。

   ```
   1. #include "service_collaboration/service_collaboration_api.h"
   ```
2. 编写CMakeLists.txt。

   ```
   1. find_library(
   2. # Sets the name of the path variable.
   3. service_collaboration-lib
   4. # Specifies the name of the NDK library that
   5. # you want CMake to locate.
   6. libservice_collaboration_ndk.z.so
   7. )
   8. target_link_libraries(entry PUBLIC
   9. ${service_collaboration-lib}
   10. )
   ```
3. 实例代码调用接口，分为以下三步。

   1. 通过调用HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos接口获取设备列表信息，传入需要的ServiceCollaborationFilterType能力数组，接口会返回支持对应能力设备。每个设备中包含所支持的能力类型ServiceCollaborationFilterTypes和设备类型deviceType信息。
   2. 创建回调ServiceCollaborationCallback，其中包括事件回调OnEventProc和图片数据回调OnDataCallbackProc；创建ServiceCollaboration\_SelectInfo，示例中传入了TAKE\_PHOTO能力，并选择了列表的第一个设备。
   3. HMS\_ServiceCollaboration\_StartCollaboration入参传入第二步构造的ServiceCollaborationCallback和ServiceCollaboration\_SelectInfo，此时被调用的设备会拉起相机，操作被拉起相机的设备进行拍照。事件和图片数据会通过第二步构造的回调通知给应用。

   ```
   1. #include "service_collaboration/service_collaboration_api.h"
   2. #include <thread>

   4. static int32_t OnEventProc(ServiceCollaborationEventCode code, uint32_t extraCode)
   5. {
   6. return 0;
   7. }
   8. static int32_t OnDataCallbackProc(
   9. ServiceCollaborationEventCode code, ServiceCollaborationDataType dataType, uint32_t dataSize, char* data)
   10. {
   11. return 0;
   12. }
   13. int main(int argc, char* argv[])
   14. {
   15. int two = 2;
   16. int three = 3;
   17. int filter = 1;
   18. const int size = 3;
   19. int shouldCancel = 0;

   21. // 构建所需跨设备互通能力，并调用HMS_ServiceCollaboration_GetCollaborationDeviceInfos接口获取设备信息
   22. ServiceCollaborationFilterType serviceFilterTypes[size] = {TAKE_PHOTO, SCAN_DOCUMENT, IMAGE_PICKER};
   23. ServiceCollaboration_CollaborationDeviceInfoSets* info = HMS_ServiceCollaboration_GetCollaborationDeviceInfos(3, serviceFilterTypes);
   24. // 构建callback回调
   25. ServiceCollaboration_SelectInfo taskInfo = { TAKE_PHOTO, { 0 } };
   26. for (uint32_t i = 0; i < info->size; i++) {
   27. ServiceCollaboration_CollaborationDeviceInfo *deviceInfo =
   28. (ServiceCollaboration_CollaborationDeviceInfo *)&(info->deviceInfoSets[i]);
   29. if (filter == 1) {
   30. taskInfo.serviceFilterType = TAKE_PHOTO;
   31. }
   32. if (filter == two) {
   33. taskInfo.serviceFilterType = SCAN_DOCUMENT;
   34. }
   35. if (filter == three) {
   36. taskInfo.serviceFilterType = IMAGE_PICKER;
   37. }
   38. std::memcpy(taskInfo.deviceNetworkId, deviceInfo->deviceNetworkId, COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH-1);
   39. }
   40. ServiceCollaborationCallback callback = {.OnEvent = OnEventProc, .OnDataCallback = OnDataCallbackProc};
   41. // 传入拍照参数、callback回调并调用HMS_ServiceCollaboration_StartCollaboration接口
   42. uint32_t id = HMS_ServiceCollaboration_StartCollaboration(&taskInfo, &callback);
   43. std::this_thread::sleep_for(std::chrono::seconds(three));
   44. if (shouldCancel) {
   45. // 三秒后主动调用HMS_ServiceCollaboration_StopCollaboration关闭跨设备互通
   46. int32_t ret = HMS_ServiceCollaboration_StopCollaboration(id);
   47. }
   48. }
   ```
