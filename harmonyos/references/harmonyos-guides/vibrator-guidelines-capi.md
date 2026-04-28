---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/vibrator-guidelines-capi
title: 振动开发指导(C/C++)
breadcrumb: 指南 > 系统 > 硬件 > Sensor Service Kit（传感器服务） > 振动 > 振动开发指导(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ae0dea6e30aa72e133efe29ce73dd00cb7cf072e58fc4b341658ef455fbb6e03
---

## 场景介绍

当设备需要设置不同的振动效果时，可以调用Vibrator模块，例如：设备的按键可以设置不同强度和不同时长的振动，闹钟和来电可以设置不同强度和时长的单次或周期振动。

详细的接口介绍请参考[Vibrator](../harmonyos-references/capi-vibrator.md)。

## 函数说明

| 名称 | 描述 |
| --- | --- |
| OHOS::Sensors::OH\_Vibrator\_PlayVibration(int32\_t duration, Vibrator\_Attribute attribute) | 控制马达在指定时间内持续振动。 |
| OHOS::Sensors::OH\_Vibrator\_PlayVibrationCustom(Vibrator\_FileDescription fileDescription, Vibrator\_Attribute vibrateAttribute) | 播放自定义振动序列。 |
| OHOS::Sensors::OH\_Vibrator\_Cancel() | 停止马达振动。 |

## 振动效果说明

目前支持两类振动效果，如下所示。

### 固定时长振动

传入一个固定时长，马达按照默认强度和频率触发振动。

### 自定义振动

自定义振动提供给用户设计自己所需振动效果的能力，用户可通过自定义振动配置文件，并遵循相应规则编排所需振动形式，使能更加开放的振感交互体验。

## 开发步骤

1. 新建一个Native C++工程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/tcbxM7igR6C_uYgbe5KYgw/zh-cn_image_0000002583478483.png?HW-CC-KV=V1&HW-CC-Date=20260427T234447Z&HW-CC-Expire=86400&HW-CC-Sign=0AA0BEF0B754439ABB7E0017661D19C76442D4E8CE0DFFCBE277EDFC7DBD1C08)
2. 控制设备上的振动器，需要申请权限ohos.permission.VIBRATE。具体配置方式请参考[声明权限](declare-permissions.md)。

   ```
   1. "requestPermissions": [
   2. {
   3. "name": "ohos.permission.VIBRATE"
   4. }
   5. ]
   ```
3. CMakeLists.txt文件中引入动态依赖库。

   ```
   1. target_link_libraries(entry PUBLIC libace_napi.z.so)
   2. target_link_libraries(entry PUBLIC libhilog_ndk.z.so)
   3. target_link_libraries(entry PUBLIC libohvibrator.z.so)
   4. target_link_libraries(entry PUBLIC librawfile.z.so)
   ```
4. 导入模块。

   ```
   1. #include <sensors/vibrator.h>
   2. #include "napi/native_api.h"
   3. #include "hilog/log.h"
   4. #include <thread>
   5. #include <fcntl.h>
   6. #include <unistd.h>
   7. #include <sys/stat.h>
   8. #include <rawfile/raw_file_manager.h>
   ```
5. 定义常量。

   ```
   1. const int VIBRATOR_LOG_DOMAIN = 0xD002701;
   2. const char *TAG = "[NativeVibratorTest]";
   3. constexpr int32_t TIME_WAIT_FOR_OP = 2;
   ```
6. 控制马达在指定时间内持续振动和停止马达振动。

   ```
   1. static napi_value PlayVibrationInDuration(napi_env env, napi_callback_info info)
   2. {
   3. Vibrator_Attribute vibrateAttribute;
   4. vibrateAttribute.usage = VIBRATOR_USAGE_ALARM;
   5. // 控制马达在指定时间内持续振动。
   6. int32_t ret = OH_Vibrator_PlayVibration(2000, vibrateAttribute);
   7. if (ret != 0) {
   8. OH_LOG_Print(LOG_APP, LOG_ERROR, VIBRATOR_LOG_DOMAIN, TAG, "vibration fail");
   9. return nullptr;
   10. }
   11. OH_LOG_Print(LOG_APP, LOG_INFO, VIBRATOR_LOG_DOMAIN, TAG, "vibration successful");
   12. std::this_thread::sleep_for(std::chrono::milliseconds(TIME_WAIT_FOR_OP));
   13. // 停止马达振动。
   14. ret = OH_Vibrator_Cancel();
   15. if (ret != 0) {
   16. OH_LOG_Print(LOG_APP, LOG_ERROR, VIBRATOR_LOG_DOMAIN, TAG, "cancel vibration fail");
   17. return nullptr;
   18. }
   19. return nullptr;
   20. }
   ```
7. 播放自定义振动序列。

   ```
   1. static napi_value PlayVibrationCustom(napi_env env, napi_callback_info info)
   2. {
   3. size_t argc = 1;
   4. napi_value argv[1] = { nullptr };
   5. // 获取参数信息
   6. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

   8. // argv[0]即为函数第一个参数Js资源对象，OH_ResourceManager_InitNativeResourceManager转为Native对象
   9. NativeResourceManager *mNativeResMgr = OH_ResourceManager_InitNativeResourceManager(env, argv[0]);
   10. if (mNativeResMgr == nullptr) {
   11. OH_LOG_Print(LOG_APP, LOG_ERROR, VIBRATOR_LOG_DOMAIN, TAG, "Get native resource manager failed");
   12. return nullptr;
   13. }
   14. // 获取rawfile指针对象
   15. std::string fileName = "coin_drop.json";
   16. RawFile *rawFile = OH_ResourceManager_OpenRawFile(mNativeResMgr, fileName.c_str());
   17. if (rawFile == nullptr) {
   18. OH_ResourceManager_ReleaseNativeResourceManager(mNativeResMgr);
   19. OH_LOG_Print(LOG_APP, LOG_ERROR, VIBRATOR_LOG_DOMAIN, TAG, "Get native rawFile failed");
   20. return nullptr;
   21. }
   22. // 获取rawfile的描述符RawFileDescriptor {fd, offset, length}
   23. RawFileDescriptor descriptor;
   24. OH_ResourceManager_GetRawFileDescriptor(rawFile, descriptor);
   25. Vibrator_FileDescription fileDescription = {
   26. .fd = descriptor.fd,
   27. .offset = descriptor.start,
   28. .length = descriptor.length
   29. };
   30. Vibrator_Attribute vibrateAttribute = {
   31. .usage = VIBRATOR_USAGE_RING
   32. };
   33. // 播放自定义振动序列。
   34. int32_t ret = OH_Vibrator_PlayVibrationCustom(fileDescription, vibrateAttribute);
   35. bool isSuccess = ((ret == 0) || (ret == UNSUPPORTED));
   36. if (!isSuccess) {
   37. OH_LOG_Print(LOG_APP, LOG_INFO, VIBRATOR_LOG_DOMAIN, TAG, "Vibratecustom fail");
   38. } else {
   39. OH_LOG_Print(LOG_APP, LOG_INFO, VIBRATOR_LOG_DOMAIN, TAG, "Vibratecustom successful");
   40. }
   41. std::this_thread::sleep_for(std::chrono::milliseconds(TIME_WAIT_FOR_OP));
   42. // 停止马达振动。
   43. OH_Vibrator_Cancel();
   44. // 关闭打开的指针对象
   45. OH_ResourceManager_CloseRawFile(rawFile);
   46. OH_ResourceManager_ReleaseNativeResourceManager(mNativeResMgr);
   47. return nullptr;
   48. }
   ```
8. 在Init函数中补充接口。

   ```
   1. EXTERN_C_START
   2. static napi_value Init(napi_env env, napi_value exports)
   3. {
   4. napi_property_descriptor desc[] = {
   5. {"playVibrationInDuration", nullptr, PlayVibrationInDuration, nullptr, nullptr, nullptr, napi_default, nullptr},
   6. {"playVibrationCustom", nullptr, PlayVibrationCustom, nullptr, nullptr, nullptr, napi_default, nullptr}
   7. };
   8. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   9. return exports;
   10. }
   11. EXTERN_C_END
   ```
9. 在types/libentry路径下index.d.ts文件中引入Napi接口。

   ```
   1. export const playVibrationInDuration: () => object;
   2. export const playVibrationCustom: (resmgr: object) => object;
   ```
10. 编写程序入口调用代码。

    ```
    1. import { BusinessError } from '@kit.BasicServicesKit';
    2. import { hilog } from '@kit.PerformanceAnalysisKit';
    3. import { resourceManager } from '@kit.LocalizationKit';
    4. import vibratorCapi from 'libentry.so';

    6. const DOMAIN = 0xD002701;
    7. // ...
    8. try {
    9. vibratorCapi.playVibrationInDuration();
    10. // ...
    11. } catch (error) {
    12. let e: BusinessError = error as BusinessError;
    13. hilog.error(DOMAIN, 'testTag', `Failed to invoke playVibrationInDuration. Code: ${e.code}, message: ${e.message}`);
    14. }
    15. // ...
    16. try {
    17. vibratorCapi.playVibrationCustom(this.getUIContext().getHostContext()?.resourceManager);
    18. // ...
    19. } catch (error) {
    20. let e: BusinessError = error as BusinessError;
    21. hilog.error(DOMAIN, 'testTag', `Failed to invoke playVibrationCustom. Code: ${e.code}, message: ${e.message}`);
    22. }
    ```
