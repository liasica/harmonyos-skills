---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/location-guidelines-capi
title: 获取设备的位置信息开发指导(C/C++)
breadcrumb: 指南 > 应用服务 > Location Kit（位置服务） > 获取设备的位置信息开发指导 > 获取设备的位置信息开发指导(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-29T13:38:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:802569679d6b737a4e3bfb65093188c734b4c59916205bae814845f9ec93ab5e
---

## 场景介绍

开发者可以调用HarmonyOS位置相关接口，监听设备的位置变化。

## 函数说明

| 名称 | 描述 |
| --- | --- |
| OH\_Location\_IsLocatingEnabled(bool\* enabled) | 查询位置开关是否开启。 |
| OH\_Location\_StartLocating(const Location\_RequestConfig\* requestConfig) | 启动定位并订阅位置变化。 |
| Location\_ResultCode OH\_Location\_StopLocating(const Location\_RequestConfig\* requestConfig) | 停止定位并取消订阅位置变化。 |
| OH\_LocationInfo\_GetBasicInfo(Location\_Info\* location) | 从定位结果中获取基本信息，如经纬度、海拔、速度等信息。 |
| OH\_LocationInfo\_GetAdditionalInfo(Location\_Info\* location, char\* additionalInfo, uint32\_t length) | 从定位结果中获取附加信息。附加信息是一个JSON格式的字符串。 |
| OH\_Location\_CreateRequestConfig(void) | 创建一个位置请求参数结构体实例。 |
| OH\_Location\_DestroyRequestConfig(Location\_RequestConfig\* requestConfig) | 销毁位置请求参数实例并回收内存。 |
| OH\_LocationRequestConfig\_SetUseScene(Location\_RequestConfig\* requestConfig, Location\_UseScene useScene) | 设置发起定位时的用户活动场景。  如果设置了useScene，则powerConsumptionScene无效。  如果未设置useScene，且设置了powerConsumptionScene，则该参数生效。  如果两个参数都不设置，则默认useScene为LOCATION\_USE\_SCENE\_DAILY\_LIFE\_SERVICE,powerConsumptionScene参数无效。 |
| OH\_LocationRequestConfig\_SetPowerConsumptionScene(Location\_RequestConfig\* requestConfig, Location\_PowerConsumptionScene powerConsumptionScene) | 设置发起定位时的功耗场景。 |
| OH\_LocationRequestConfig\_SetInterval(Location\_RequestConfig\* requestConfig, int interval) | 设置定位结果上报时间间隔。 |
| OH\_LocationRequestConfig\_SetCallback(Location\_RequestConfig\* requestConfig, Location\_InfoCallback callback, void\* userData) | 设置用于接收位置上报的回调函数。 |

## 开发步骤

1. 新建一个Native C++工程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/Jjbm2fYuSVu0YA_l_aXnfg/zh-cn_image_0000002558605840.png?HW-CC-KV=V1&HW-CC-Date=20260429T053856Z&HW-CC-Expire=86400&HW-CC-Sign=6016D60939A948CA4AE1E74F6CD673E30CCB65C9C432B21710D40F3486074B34)
2. 获取设备的位置信息，需要有位置权限，位置权限申请的方法和步骤见[申请位置权限开发指导](location-permission-guidelines.md)。
3. CMakeLists.txt文件中引入动态依赖库。

   ```
   1. target_link_libraries(entry PUBLIC libace_napi.z.so)
   2. target_link_libraries(entry PUBLIC libhilog_ndk.z.so)
   3. target_link_libraries(entry PUBLIC liblocation_ndk.so)
   ```
4. 在napi\_init.cpp文件中编码，首先导入模块。

   ```
   1. #include "napi/native_api.h"
   2. #include "LocationKit/oh_location.h"
   3. #include "LocationKit/oh_location_type.h"
   4. #include "hilog/log.h"
   5. #include <stdlib.h>
   ```
5. 调用获取位置接口之前需要先判断位置开关是否打开。

   查询当前位置开关状态，返回结果为布尔值，true代表位置开关开启，false代表位置开关关闭，示例代码如下：

   ```
   1. static napi_value OhLocationIsEnabled(napi_env env, napi_callback_info info)
   2. {
   3. bool isEnabled = false;
   4. int resultCode = OH_Location_IsLocatingEnabled(&isEnabled);
   5. napi_value result = NULL;
   6. napi_get_boolean(env, isEnabled, &result);
   7. return result;
   8. }
   9. // 在Init函数中补充接口。
   10. EXTERN_C_START
   11. static napi_value Init(napi_env env, napi_value exports)
   12. {
   13. napi_property_descriptor desc[] = {
   14. {"ohLocationIsEnabled", NULL, OhLocationIsEnabled, NULL, NULL, NULL, napi_default, NULL},
   15. };
   16. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   17. return exports;
   18. }
   19. EXTERN_C_END
   ```
6. 定位位置变化。

   ```
   1. // 定义一个请求参数
   2. struct Location_RequestConfig *g_requestConfig = NULL;
   3. void *mydata = NULL;

   5. // 定义一个回调函数用来接收位置信息
   6. void reportLocation(Location_Info* location, void* userData)
   7. {
   8. Location_BasicInfo baseInfo = OH_LocationInfo_GetBasicInfo(location);
   9. char additionalInfo[1024] = "";
   10. Location_ResultCode result = OH_LocationInfo_GetAdditionalInfo(location, additionalInfo, sizeof(additionalInfo));
   11. if (mydata == userData) {
   12. OH_LOG_INFO(LOG_APP, "userData is mydata");
   13. }
   14. return;
   15. }

   17. // 订阅位置信息
   18. static napi_value OhLocationStartLocating(napi_env env, napi_callback_info info)
   19. {
   20. if (g_requestConfig == NULL) {
   21. g_requestConfig = OH_Location_CreateRequestConfig();
   22. }
   23. OH_LocationRequestConfig_SetUseScene(g_requestConfig, LOCATION_USE_SCENE_NAVIGATION);
   24. OH_LocationRequestConfig_SetInterval(g_requestConfig, 1);
   25. mydata = (void *)malloc(sizeof("mydata")); // 用户自定义任意类型，callback 透传返回
   26. OH_LocationRequestConfig_SetCallback(g_requestConfig, reportLocation, mydata);
   27. OH_Location_StartLocating(g_requestConfig);
   28. int32_t ret = 0;
   29. napi_value result = NULL;
   30. napi_create_int32(env, ret, &result);
   31. return result;
   32. }

   34. // 取消订阅位置信息， g_requestConfig要和订阅时传入的对象保持一致
   35. static napi_value OhLocationStopLocating(napi_env env, napi_callback_info info)
   36. {
   37. OH_Location_StopLocating(g_requestConfig);
   38. if (g_requestConfig != NULL) {
   39. OH_Location_DestroyRequestConfig(g_requestConfig);
   40. g_requestConfig = NULL;
   41. }
   42. free(mydata);
   43. mydata = NULL;
   44. int32_t ret = 0;
   45. napi_value result = NULL;
   46. napi_create_int32(env, ret, &result);
   47. return result;
   48. }

   50. // 在Init函数中补充接口。
   51. EXTERN_C_START
   52. static napi_value Init(napi_env env, napi_value exports)
   53. {
   54. napi_property_descriptor desc[] = {
   55. {"ohLocationStartLocating", NULL, OhLocationStartLocating, NULL, NULL, NULL, napi_default, NULL},
   56. {"ohLocationStopLocating", NULL, OhLocationStopLocating, NULL, NULL, NULL, napi_default, NULL},
   57. };
   58. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   59. return exports;
   60. }
   61. EXTERN_C_END
   ```
7. 在types/libentry路径下index.d.ts文件中引入Napi接口。

   ```
   1. export const ohLocationIsEnabled: () => boolean;
   2. export const ohLocationStartLocating: () => number;
   3. export const ohLocationStopLocating: () => number;
   ```
8. 删除Index.ets中的已废弃函数。

   ```
   1. .onClick(() => {
   2. hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(2, 3));
   3. })
   ```
