---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/location-guidelines-capi
title: 获取设备的位置信息开发指导(C/C++)
breadcrumb: 指南 > 应用服务 > Location Kit（位置服务） > 获取设备的位置信息开发指导 > 获取设备的位置信息开发指导(C/C++)
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:4b21d338538f142e304ac4b3a463d5fbde0ec7b4be624f3fd1bb69b2a9d37d6c
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/7S9Qg60kTwuavx9ErwIMOg/zh-cn_image_0000002815559817.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=FB4363987E4EE2F9C3861841605717CB9B5D0D68B3B4DD8B5E5FD2A7D6A61D8C)
2. 获取设备的位置信息，需要有位置权限，位置权限申请的方法和步骤见[申请位置权限开发指导](location-permission-guidelines.md)。
3. CMakeLists.txt文件中引入动态依赖库。

   ```c
   target_link_libraries(entry PUBLIC libace_napi.z.so)
   target_link_libraries(entry PUBLIC libhilog_ndk.z.so)
   target_link_libraries(entry PUBLIC liblocation_ndk.so)
   ```
4. 在napi\_init.cpp文件中编码，首先导入模块。

   ```c
   #include "napi/native_api.h"
   #include "LocationKit/oh_location.h"
   #include "LocationKit/oh_location_type.h"
   #include "hilog/log.h"
   #include <stdlib.h>
   #include <string>
   ```
5. 调用获取位置接口之前需要先判断位置开关是否打开。

   查询当前位置开关状态，返回结果为布尔值，true代表位置开关开启，false代表位置开关关闭，示例代码如下：

   ```c
    std::string GetErrorMsgFromErrorCode(int errorCode)
    {
        switch(errorCode) {
           case LOCATION_PERMISSION_DENIED:
              return "Permission verification failed. The application does not have the permission required to call the API.";
           case LOCATION_INVALID_PARAM:
              return "Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.";
           case LOCATION_NOT_SUPPORTED:
              return "Capability not supported. Failed to call this API due to limited device capabilities.";
           case LOCATION_SERVICE_UNAVAILABLE:
              return "The location service is unavailable.";
           case LOCATION_SWITCH_OFF:
              return "The location switch is off.";
           default:
              return "Unknown error. error code: " + std::to_string(errorCode);
        }
    }

    static napi_value OhLocationIsEnabled(napi_env env, napi_callback_info info)
    {
        bool isEnabled = false;
        int resultCode = OH_Location_IsLocatingEnabled(&isEnabled);
        napi_value result = NULL;
        if (resultCode != LOCATION_SUCCESS) {
           std::string errorMsg = GetErrorMsgFromErrorCode(resultCode);
           napi_throw_error(env, std::to_string(resultCode).c_str(), errorMsg.c_str());
           napi_get_undefined(env, &result);
           return result;
        }
        napi_get_boolean(env, isEnabled, &result);
        return result;
    }
    // 在Init函数中补充接口。
    EXTERN_C_START
    static napi_value Init(napi_env env, napi_value exports)
    {
        napi_property_descriptor desc[] = {
            {"ohLocationIsEnabled", NULL, OhLocationIsEnabled, NULL, NULL, NULL, napi_default, NULL},
        };
        napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
        return exports;
    }
    EXTERN_C_END
   ```
6. 定位位置变化。

   ```c
   // 定义一个请求参数
   struct Location_RequestConfig *g_requestConfig = NULL;
   void *mydata = NULL;

   // 定义一个回调函数用来接收位置信息
   void reportLocation(Location_Info* location, void* userData)
   {
       Location_BasicInfo baseInfo = OH_LocationInfo_GetBasicInfo(location);
       char additionalInfo[1024] = "";
       Location_ResultCode result = OH_LocationInfo_GetAdditionalInfo(location, additionalInfo, sizeof(additionalInfo));
       // 此处接收传回的userData与mydata做对比，判断是否为携带mydata字段的位置请求回调
       if (mydata == userData) {
           OH_LOG_INFO(LOG_APP, "userData is mydata");
       }
       return;
   }

   // 订阅位置信息
   static napi_value OhLocationStartLocating(napi_env env, napi_callback_info info)
   {
       if (g_requestConfig == NULL) {
          g_requestConfig = OH_Location_CreateRequestConfig();
       }
       OH_LocationRequestConfig_SetUseScene(g_requestConfig, LOCATION_USE_SCENE_NAVIGATION);
       OH_LocationRequestConfig_SetInterval(g_requestConfig, 1);
       // mydata:用户自定义任意类型，触发reportLocation回调时会传回该字段，用于区分是否为携带mydata字段的位置请求回调
       mydata = (void *)malloc(sizeof("mydata"));
       napi_value result = NULL;
       if (mydata == NULL) {
          int errCode = LOCATION_INVALID_PARAM;
          std::string errorMsg = GetErrorMsgFromErrorCode(errCode);
          napi_throw_error(env, std::to_string(errCode).c_str(), errorMsg.c_str());
          napi_get_undefined(env, &result);
          return result;
       }

       OH_LocationRequestConfig_SetCallback(g_requestConfig, reportLocation, mydata);
       int resultCode = OH_Location_StartLocating(g_requestConfig);
       if (resultCode != LOCATION_SUCCESS) {
           std::string errorMsg = GetErrorMsgFromErrorCode(resultCode);
           napi_throw_error(env, std::to_string(resultCode).c_str(), errorMsg.c_str());
           napi_get_undefined(env, &result);
           return result;
       }
       napi_create_int32(env, resultCode, &result);
       return result;
   }

   // 取消订阅位置信息， g_requestConfig要和订阅时传入的对象保持一致
   static napi_value OhLocationStopLocating(napi_env env, napi_callback_info info)
   {
       int32_t resultCode = OH_Location_StopLocating(g_requestConfig);
       if (g_requestConfig != NULL) {
           OH_Location_DestroyRequestConfig(g_requestConfig);
           g_requestConfig = NULL;
       }
       if (mydata != NULL) {
           free(mydata);
           mydata = NULL;
       }
       napi_value result = NULL;
       if (resultCode != LOCATION_SUCCESS) {
           std::string errorMsg = GetErrorMsgFromErrorCode(resultCode);
           napi_throw_error(env, std::to_string(resultCode).c_str(), errorMsg.c_str());
           napi_get_undefined(env, &result);
           return result;
       }
       napi_create_int32(env, resultCode, &result);
       return result;
   }

   // 在Init函数中补充接口。
   EXTERN_C_START
   static napi_value Init(napi_env env, napi_value exports)
   {
       napi_property_descriptor desc[] = {
           {"ohLocationStartLocating", NULL, OhLocationStartLocating, NULL, NULL, NULL, napi_default, NULL},
           {"ohLocationStopLocating", NULL, OhLocationStopLocating, NULL, NULL, NULL, napi_default, NULL},
       };
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
       return exports;
   }
   EXTERN_C_END
   ```
7. 在types/libentry路径下index.d.ts文件中引入Napi接口。

   ```c
   export const ohLocationIsEnabled: () => boolean;
   export const ohLocationStartLocating: () => number;
   export const ohLocationStopLocating: () => number;
   ```
8. 删除Index.ets中的已废弃函数。

   ```js
   .onClick(() => {
       hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(2, 3));
   })
   ```
