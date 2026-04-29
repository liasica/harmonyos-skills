---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sensor-guidelines-capi
title: 传感器开发指导(C/C++)
breadcrumb: 指南 > 系统 > 硬件 > Sensor Service Kit（传感器服务） > 传感器 > 传感器开发指导(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-29T13:33:41+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:d210692d1ed876ca1ff97e5b88fba406f3e73f3f07b9f47efa3d1811b5a84dac
---

## 场景介绍

当设备需要获取传感器数据时，可以使用sensor模块，例如：通过订阅方向传感器数据感知用户设备当前的朝向，通过订阅计步传感器数据统计用户的步数等。

详细的接口介绍请参考[Sensor](../harmonyos-references/capi-sensor.md)。

## 函数说明

| 名称 | 描述 |
| --- | --- |
| OH\_Sensor\_GetInfos(Sensor\_Info \*\*infos, uint32\_t \*count) | 获取设备上所有传感器的信息。 |
| OH\_Sensor\_Subscribe(const Sensor\_SubscriptionId \*id, const Sensor\_SubscriptionAttribute \*attribute, const Sensor\_Subscriber \*subscriber) | 订阅传感器数据。系统将以指定的频率向用户上报传感器数据。  订阅加速度传感器，需要申请ohos.permission.ACCELEROMETER权限；  订阅陀螺仪传感器，需要申请ohos.permission.GYROSCOPE权限；  订阅计步器相关传感器时，需要申请ohos.permission.ACTIVITY\_MOTION权限；  订阅与健康相关的传感器时，比如心率传感器需要申请ohos.permission.READ\_HEALTH\_DATA权限，否则订阅失败;  订阅其余传感器不需要申请权限。 |
| OH\_Sensor\_Unsubscribe(const Sensor\_SubscriptionId \*id, const Sensor\_Subscriber \*subscriber) | 取消订阅传感器数据。  取消订阅加速度传感器，需要申请ohos.permission.ACCELEROMETER权限；  取消订阅陀螺仪传感器，需要申请ohos.permission.GYROSCOPE权限；  取消订阅计步器相关传感器时，需要申请ohos.permission.ACTIVITY\_MOTION权限；  取消订阅与健康相关的传感器时，需要申请ohos.permission.READ\_HEALTH\_DATA权限，否则取消订阅失败。  取消订阅其余传感器不需要申请权限。 |
| OH\_Sensor\_CreateInfos(uint32\_t count) | 用给定的数字创建一个实例数组，请参考[Sensor\_Info](../harmonyos-references/capi-sensor-sensor-info.md)。 |
| OH\_Sensor\_DestroyInfos(Sensor\_Info \*\*sensors, uint32\_t count) | 销毁实例数组并回收内存，请参考[Sensor\_Info](../harmonyos-references/capi-sensor-sensor-info.md)。 |
| OH\_SensorInfo\_GetName(Sensor\_Info \*sensor, char \*sensorName, uint32\_t \*length) | 获取传感器名称。 |
| OH\_SensorInfo\_GetVendorName(Sensor\_Info\* sensor, char \*vendorName, uint32\_t \*length) | 获取传感器的厂商名称。 |
| OH\_SensorInfo\_GetType(Sensor\_Info\* sensor, Sensor\_Type \*sensorType) | 获取传感器类型。 |
| OH\_SensorInfo\_GetResolution(Sensor\_Info\* sensor, float \*resolution) | 获取传感器分辨率。 |
| OH\_SensorInfo\_GetMinSamplingInterval(Sensor\_Info\* sensor, int64\_t \*minSamplingInterval) | 获取传感器的最小数据上报间隔。 |
| OH\_SensorInfo\_GetMaxSamplingInterval(Sensor\_Info\* sensor, int64\_t \*maxSamplingInterval) | 获取传感器的最大数据上报间隔时间。 |
| OH\_SensorEvent\_GetType(Sensor\_Event\* sensorEvent, Sensor\_Type \*sensorType) | 获取传感器类型。 |
| OH\_SensorEvent\_GetTimestamp(Sensor\_Event\* sensorEvent, int64\_t \*timestamp) | 获取传感器数据的时间戳。 |
| OH\_SensorEvent\_GetAccuracy(Sensor\_Event\* sensorEvent, Sensor\_Accuracy \*accuracy) | 获取传感器数据的精度。 |
| OH\_SensorEvent\_GetData(Sensor\_Event\* sensorEvent, float \*\*data, uint32\_t \*length) | 获取传感器数据。  数据的长度和内容依赖于监听的传感器类型，传感器上报的数据格式如下：  1.SENSOR\_TYPE\_ACCELEROMETER:data[0]、data[1]、data[2]分别表示设备x、y、z轴的加速度分量，单位m/s²；  2.SENSOR\_TYPE\_GYROSCOPE:data[0]、data[1]、data[2]分别表示设备x、y、z轴的旋转角速度，单位弧度/s；  3.SENSOR\_TYPE\_AMBIENT\_LIGHT:data[0]表示环境光强度，单位lux；从API Version 12开始，将返回两个额外的数据，其中data[1]表示色温，单位kelvin；data[2]表示红外亮度，单位cd/m²；  4.SENSOR\_TYPE\_MAGNETIC\_FIELD:data[0]、data[1]、data[2]分别表示设备x、y、z轴的地磁分量，单位微特斯拉；  5.SENSOR\_TYPE\_BAROMETER:data[0]表示气压值，单位hPa；  6.SENSOR\_TYPE\_HALL:data[0]表示皮套吸合状态，0表示打开，大于0表示吸附；  7.SENSOR\_TYPE\_PROXIMITY:data[0]表示接近状态，0表示接近，大于0表示远离；  8.SENSOR\_TYPE\_ORIENTATION:data[0]、data[1]、data[2]分别表示设备绕z、x、y轴的角度，单位度；  9.SENSOR\_TYPE\_GRAVITY:data[0]、data[1]、data[2]分别表示设备x、y、z轴的重力加速度分量，单位m/s²；  10.SENSOR\_TYPE\_ROTATION\_VECTOR:data[0]、data[1]、data[2]分别表示设备x、y、z轴的旋转角度，单位度，data[3]表示旋转向量元素；  11.SENSOR\_TYPE\_PEDOMETER\_DETECTION:data[0]表示计步检测状态，1表示检测到了步数变化；  12.SENSOR\_TYPE\_PEDOMETER:data[0]表示步数；  13.SENSOR\_TYPE\_HEART\_RATE:data[0]表示心率数值。 |
| OH\_Sensor\_CreateSubscriptionId(void) | 创建一个Sensor\_SubscriptionId 实例。 |
| OH\_Sensor\_DestroySubscriptionId(Sensor\_SubscriptionId \*id) | 销毁Sensor\_SubscriptionId 实例并回收内存。 |
| OH\_SensorSubscriptionId\_SetType(Sensor\_SubscriptionId\* id, const Sensor\_Type sensorType) | 设置传感器类型。 |
| OH\_Sensor\_CreateSubscriptionAttribute(void) | 创建Sensor\_SubscriptionAttribute实例。 |
| OH\_Sensor\_DestroySubscriptionAttribute(Sensor\_SubscriptionAttribute \*attribute) | 销毁Sensor\_SubscriptionAttribute实例并回收内存。 |
| OH\_SensorSubscriptionAttribute\_SetSamplingInterval(Sensor\_SubscriptionAttribute\* attribute, const int64\_t samplingInterval) | 设置传感器数据上报间隔。 |
| OH\_Sensor\_CreateSubscriber(void) | 创建一个Sensor\_Subscriber实例。 |
| OH\_Sensor\_DestroySubscriber(Sensor\_Subscriber \*subscriber) | 销毁Sensor\_Subscriber实例并回收内存。 |
| OH\_SensorSubscriber\_SetCallback(Sensor\_Subscriber\* subscriber, const Sensor\_EventCallback callback) | 设置一个回调函数来上报传感器数据。 |

## 开发步骤

开发步骤以加速度传感器为例。

1. 新建一个Native C++工程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/rdQ5iTntTp-eAE_DPpXBeg/zh-cn_image_0000002589324849.png?HW-CC-KV=V1&HW-CC-Date=20260429T053339Z&HW-CC-Expire=86400&HW-CC-Sign=FE2AD5DAAA8057F15DEF2721B16D5629A814246BCD36392A283FEC23D8F43C26)
2. 配置加速度传感器权限，具体配置方式请参考[声明权限](declare-permissions.md)。

   ```
   1. "requestPermissions": [
   2. {
   3. "name": "ohos.permission.ACCELEROMETER"
   4. }
   5. ]
   ```
3. CMakeLists.txt文件中引入动态依赖库。

   ```
   1. target_link_libraries(entry PUBLIC libace_napi.z.so)
   2. target_link_libraries(entry PUBLIC libhilog_ndk.z.so)
   3. target_link_libraries(entry PUBLIC libohsensor.so)
   ```
4. 在oh\_sensor\_capi.cpp文件中编码，首先导入模块。

   ```
   1. #include "sensors/oh_sensor.h"
   2. #include "napi/native_api.h"
   3. #include "hilog/log.h"
   4. #include <thread>
   ```
5. 定义常量。

   ```
   1. const int SENSOR_LOG_DOMAIN = 0xD002700;
   2. const char *TAG = "[Sensor]";
   3. constexpr Sensor_Type SENSOR_ID { SENSOR_TYPE_ACCELEROMETER };
   4. constexpr uint32_t SENSOR_NAME_LENGTH_MAX = 64;
   5. constexpr int64_t SENSOR_SAMPLE_PERIOD = 200000000;
   6. constexpr int32_t SLEEP_TIME_MS = 1000;
   7. constexpr int64_t INVALID_VALUE = -1;
   8. constexpr float INVALID_RESOLUTION = -1.0F;
   9. Sensor_Subscriber *g_user = nullptr;
   ```
6. 定义一个回调函数用来接收传感器数据。

   ```
   1. // 定义回调函数
   2. void SensorDataCallbackImpl(Sensor_Event *event)
   3. {
   4. if (event == nullptr) {
   5. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG, "event is null");
   6. return;
   7. }
   8. int64_t timestamp = INVALID_VALUE;
   9. // 获取传感器数据的时间戳。
   10. int32_t ret = OH_SensorEvent_GetTimestamp(event, &timestamp);
   11. if (ret != SENSOR_SUCCESS) {
   12. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG, "get timestamp failed");
   13. return;
   14. }
   15. Sensor_Type sensorType;
   16. // 获取传感器类型。
   17. ret = OH_SensorEvent_GetType(event, &sensorType);
   18. if (ret != SENSOR_SUCCESS) {
   19. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG, "get sensor type failed");
   20. return;
   21. }
   22. Sensor_Accuracy accuracy = SENSOR_ACCURACY_UNRELIABLE;
   23. // 获取传感器数据的精度。
   24. ret = OH_SensorEvent_GetAccuracy(event, &accuracy);
   25. if (ret != SENSOR_SUCCESS) {
   26. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG, "get sensor accuracy failed");
   27. return;
   28. }
   29. float *data = nullptr;
   30. uint32_t length = 0;
   31. // 获取传感器数据。
   32. ret = OH_SensorEvent_GetData(event, &data, &length);
   33. if (ret != SENSOR_SUCCESS) {
   34. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG, "get sensor data failed");
   35. return;
   36. }
   37. if (data == nullptr) {
   38. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG, "sensor data is null");
   39. return;
   40. }
   41. OH_LOG_Print(LOG_APP, LOG_INFO, SENSOR_LOG_DOMAIN, TAG,
   42. "sensorType:%{public}d, dataLen:%{public}d, accuracy:%{public}d", sensorType, length, accuracy);
   43. for (uint32_t i = 0; i < length; ++i) {
   44. OH_LOG_Print(LOG_APP, LOG_INFO, SENSOR_LOG_DOMAIN, TAG, "data[%{public}d]:%{public}f", i, data[i]);
   45. }
   46. }
   ```
7. 获取设备上所有传感器的信息。

   ```
   1. static int32_t GetSensorInfo(Sensor_Info *sensorInfoTemp)
   2. {
   3. char sensorName[SENSOR_NAME_LENGTH_MAX] = {};
   4. uint32_t length = SENSOR_NAME_LENGTH_MAX;
   5. // 获取传感器名称。
   6. int32_t ret = OH_SensorInfo_GetName(sensorInfoTemp, sensorName, &length);
   7. if (ret != SENSOR_SUCCESS) {
   8. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG, "get sensor name failed");
   9. return ret;
   10. }
   11. char vendorName[SENSOR_NAME_LENGTH_MAX] = {};
   12. length = SENSOR_NAME_LENGTH_MAX;
   13. // 获取传感器的厂商名称。
   14. ret = OH_SensorInfo_GetVendorName(sensorInfoTemp, vendorName, &length);
   15. if (ret != SENSOR_SUCCESS) {
   16. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG, "get sensor vendor name failed");
   17. return ret;
   18. }
   19. Sensor_Type sensorType;
   20. // 获取传感器类型。
   21. ret = OH_SensorInfo_GetType(sensorInfoTemp, &sensorType);
   22. if (ret != SENSOR_SUCCESS) {
   23. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG, "get sensor type failed");
   24. return ret;
   25. }
   26. float resolution = INVALID_RESOLUTION;
   27. // 获取传感器分辨率。
   28. ret = OH_SensorInfo_GetResolution(sensorInfoTemp, &resolution);
   29. if (ret != SENSOR_SUCCESS) {
   30. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG, "get sensor resolution failed");
   31. return ret;
   32. }
   33. int64_t minSamplePeriod = INVALID_VALUE;
   34. // 获取传感器的最小数据上报间隔。
   35. ret = OH_SensorInfo_GetMinSamplingInterval(sensorInfoTemp, &minSamplePeriod);
   36. if (ret != SENSOR_SUCCESS) {
   37. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG, "get sensor min sampling interval failed");
   38. return ret;
   39. }
   40. int64_t maxSamplePeriod = INVALID_VALUE;
   41. // 获取传感器的最大数据上报间隔时间。
   42. ret = OH_SensorInfo_GetMaxSamplingInterval(sensorInfoTemp, &maxSamplePeriod);
   43. if (ret != SENSOR_SUCCESS) {
   44. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG, "get sensor max sampling interval failed");
   45. }
   46. return ret;
   47. }

   49. static napi_value GetSensorInfos(napi_env env, napi_callback_info info)
   50. {
   51. uint32_t count = 0;
   52. // 获取设备上所有传感器的个数。
   53. int32_t ret = OH_Sensor_GetInfos(nullptr, &count);
   54. if (ret != SENSOR_SUCCESS) {
   55. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG, "get sensor count failed");
   56. return nullptr;
   57. }
   58. // 用给定的数字创建一个实例数组。
   59. Sensor_Info **sensors = OH_Sensor_CreateInfos(count);
   60. if (sensors == nullptr) {
   61. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG, "create sensorInfo array failed");
   62. return nullptr;
   63. }
   64. // 获取设备上所有传感器的信息。
   65. ret = OH_Sensor_GetInfos(sensors, &count);
   66. if (ret != SENSOR_SUCCESS) {
   67. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG, "get all sensor info failed");
   68. return nullptr;
   69. }
   70. for (uint32_t i = 0; i < count; ++i) {
   71. Sensor_Info *sensorInfoTemp = sensors[i];
   72. ret = GetSensorInfo(sensorInfoTemp);
   73. if (ret != SENSOR_SUCCESS) {
   74. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG, "get sensor info failed");
   75. return nullptr;
   76. }
   77. }
   78. OH_LOG_Print(LOG_APP, LOG_INFO, SENSOR_LOG_DOMAIN, TAG, "GetSensorInfos successful");
   79. // 销毁实例数组并回收内存。
   80. ret = OH_Sensor_DestroyInfos(sensors, count);
   81. if (ret != SENSOR_SUCCESS) {
   82. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG, "destroy sensor info failed");
   83. return nullptr;
   84. }
   85. return nullptr;
   86. }
   ```
8. 订阅和取消订阅传感器数据。

   ```
   1. static napi_value Subscriber(napi_env env, napi_callback_info info)
   2. {
   3. // 创建Sensor_Subscriber实例。
   4. g_user = OH_Sensor_CreateSubscriber();
   5. // 设置回调函数来报告传感器数据。
   6. int32_t ret = OH_SensorSubscriber_SetCallback(g_user, SensorDataCallbackImpl);
   7. if (ret != SENSOR_SUCCESS) {
   8. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG, "OH_SensorSubscriber_SetCallback failed");
   9. return nullptr;
   10. }
   11. // 创建Sensor_SubscriptionId实例。
   12. Sensor_SubscriptionId *id = OH_Sensor_CreateSubscriptionId();
   13. // 设置传感器类型,示例中设置的是SENSOR_TYPE_ACCELEROMETER类型，需开通ohos.permission.ACCELEROMETER权限
   14. // 参考传感器开发指导中 开发步骤第2点配置加速度传感器权限。
   15. ret = OH_SensorSubscriptionId_SetType(id, SENSOR_ID);
   16. if (ret != SENSOR_SUCCESS) {
   17. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG, "OH_SensorSubscriptionId_SetType failed");
   18. return nullptr;
   19. }
   20. // 创建Sensor_SubscriptionAttribute实例。
   21. Sensor_SubscriptionAttribute *attr = OH_Sensor_CreateSubscriptionAttribute();
   22. // 设置传感器数据报告间隔。
   23. ret = OH_SensorSubscriptionAttribute_SetSamplingInterval(attr, SENSOR_SAMPLE_PERIOD);
   24. if (ret != SENSOR_SUCCESS) {
   25. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG,
   26. "OH_SensorSubscriptionAttribute_SetSamplingInterval failed");
   27. return nullptr;
   28. }
   29. // 订阅传感器数据。
   30. ret = OH_Sensor_Subscribe(id, attr, g_user);
   31. if (ret != SENSOR_SUCCESS) {
   32. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG, "OH_Sensor_Subscribe failed");
   33. return nullptr;
   34. }
   35. OH_LOG_Print(LOG_APP, LOG_INFO, SENSOR_LOG_DOMAIN, TAG, "OH_Sensor_Subscribe successful");
   36. std::this_thread::sleep_for(std::chrono::milliseconds(SLEEP_TIME_MS));
   37. // 取消订阅传感器数据。
   38. ret = OH_Sensor_Unsubscribe(id, g_user);
   39. if (ret != SENSOR_SUCCESS) {
   40. OH_LOG_Print(LOG_APP, LOG_ERROR, SENSOR_LOG_DOMAIN, TAG, "OH_Sensor_Unsubscribe failed");
   41. return nullptr;
   42. }
   43. OH_LOG_Print(LOG_APP, LOG_INFO, SENSOR_LOG_DOMAIN, TAG, "OH_Sensor_Unsubscribe successful");
   44. if (id != nullptr) {
   45. // 销毁Sensor_SubscriptionId实例。
   46. OH_Sensor_DestroySubscriptionId(id);
   47. }
   48. if (attr != nullptr) {
   49. // 销毁Sensor_SubscriptionAttribute实例。
   50. OH_Sensor_DestroySubscriptionAttribute(attr);
   51. }
   52. if (g_user != nullptr) {
   53. // 销毁Sensor_Subscriber实例并回收内存。
   54. OH_Sensor_DestroySubscriber(g_user);
   55. g_user = nullptr;
   56. }
   57. return nullptr;
   58. }
   ```
9. 在Init函数中补充接口。

   ```
   1. EXTERN_C_START
   2. static napi_value Init(napi_env env, napi_value exports)
   3. {
   4. napi_property_descriptor desc[] = {
   5. {"getSensorInfos", nullptr, GetSensorInfos, nullptr, nullptr, nullptr, napi_default, nullptr},
   6. {"subscriber", nullptr, Subscriber, nullptr, nullptr, nullptr, napi_default, nullptr}
   7. };
   8. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   9. return exports;
   10. }
   11. EXTERN_C_END
   ```
10. 在types/libentry路径下index.d.ts文件中引入Napi接口。

    ```
    1. export const getSensorInfos: () => object;
    2. export const subscriber: () => object;
    ```
11. 编写程序入口调用代码。

    ```
    1. import { BusinessError } from '@kit.BasicServicesKit';
    2. import { hilog } from '@kit.PerformanceAnalysisKit';
    3. import sensorCapi from 'libentry.so';

    5. const DOMAIN = 0xD002700;
    6. // ...
    7. try {
    8. sensorCapi.getSensorInfos();
    9. // ...
    10. } catch (error) {
    11. let e: BusinessError = error as BusinessError;
    12. hilog.error(DOMAIN, 'testTag', `Failed to invoke getSensorInfos. Code: ${e.code}, message: ${e.message}`);
    13. }
    14. // ...
    15. try {
    16. sensorCapi.subscriber();
    17. // ...
    18. } catch (error) {
    19. let e: BusinessError = error as BusinessError;
    20. hilog.error(DOMAIN, 'testTag', `Failed to invoke subscriber. Code: ${e.code}, message: ${e.message}`);
    21. }
    ```
