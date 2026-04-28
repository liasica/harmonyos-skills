---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameperformance-access-procedure-c
title: 开发指导(C/C++)
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 游戏场景感知（可选） > 开发指导(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:569b63df0b597e63c9bc51a8cafbdc40052f281a68d964550a7d16ad3c22cd86
---

游戏场景感知包括：

* Game Service Kit通过游戏提供的精细化场景信息、配置信息和网络信息等数据，以及当前负载情况使用不同策略优化系统资源调度。
* Game Service Kit通过感知游戏设备的系统状态信息（包括温度变化趋势数据、GPU性能信息和CPU性能信息等），并将其反馈给游戏应用，游戏应用可以基于当前设备状态自行调整游戏设置等内容，在系统资源有限的情况下优化玩家的游戏体验。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/7shs4IWoQMK6uB5Z66LxhA/zh-cn_image_0000002552958900.png?HW-CC-KV=V1&HW-CC-Date=20260427T234904Z&HW-CC-Expire=86400&HW-CC-Sign=814F81C2932D5E89D6899864DFA6967E88B7C945A97E702D55FD3E424133F021)

1. 游戏启动后调用[HMS\_GamePerformance\_Init](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_init)接口对游戏场景感知进行初始化。
2. 初始化成功后，游戏调用[HMS\_GamePerformance\_RegisterThermalLevelChangedCallback](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_registerthermallevelchangedcallback)接口注册设备状态变化事件监听，订阅设备状态变化通知。
3. 游戏调用以下接口向游戏场景感知上报各种游戏信息。

   * 包信息：[HMS\_GamePerformance\_UpdatePackageInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_updatepackageinfo)
   * 配置信息：[HMS\_GamePerformance\_UpdateConfigInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_updateconfiginfo)
   * 场景信息：[HMS\_GamePerformance\_UpdateSceneInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_updatesceneinfo)
   * 网络信息：[HMS\_GamePerformance\_UpdateNetInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_updatenetinfo)
   * 玩家信息：[HMS\_GamePerformance\_UpdatePlayerInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_updateplayerinfo)
4. 游戏场景感知广播游戏信息给终端系统。
5. 终端系统根据游戏信息进行系统资源调度。
6. 终端系统会将设备状态变化通知游戏场景感知。
7. 游戏场景感知向游戏客户端反馈设备状态变化。
8. 如不再需要订阅，游戏可调用[HMS\_GamePerformance\_UnregisterThermalLevelChangedCallback](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_unregisterthermallevelchangedcallback)接口或[HMS\_GamePerformance\_UnregisterAllThermalLevelChangedCallbacks](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_unregisterallthermallevelchangedcallbacks)接口取消设备状态变化事件监听。
9. 游戏调用以下接口向游戏场景感知主动查询设备状态信息。

   * 设备GPU性能信息：[HMS\_GamePerformance\_QueryGpuInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_querygpuinfo)
   * 设备CPU性能信息：[HMS\_GamePerformance\_QueryCpuInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_querycpuinfo)
   * 设备温度相关信息：[HMS\_GamePerformance\_QueryThermalInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_querythermalinfo)

说明

Mali系列GPU不支持采集GPU性能信息，调用订阅和查询设备状态信息接口时无法获取设备GPU性能信息。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/gameservice-game-performance.md)。

| 接口名 | 描述 |
| --- | --- |
| [GamePerformance\_ErrorCode](../harmonyos-references/gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_Init](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_init) ([GamePerformance\_InitParameters](../harmonyos-references/gameservice-game-performance.md#gameperformance_initparameters) \*initParameters) | 游戏初始化接口，对游戏场景感知进行初始化。 |
| [GamePerformance\_ErrorCode](../harmonyos-references/gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_RegisterThermalLevelChangedCallback](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_registerthermallevelchangedcallback) ([GamePerformance\_DeviceInfoType](../harmonyos-references/gameservice-game-performance.md#gameperformance_deviceinfotype-1) \*types[], size\_t size, [GamePerformance\_ThermalLevelChangedCallback](../harmonyos-references/gameservice-game-performance.md#gameperformance_thermallevelchangedcallback) callback, void \*userData) | 注册温度变化回调接口，当达到触发点时，将调用回调函数。 |
| [GamePerformance\_ErrorCode](../harmonyos-references/gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_UpdatePackageInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_updatepackageinfo) ([GamePerformance\_PackageInfo](../harmonyos-references/gameservice-game-performance.md#gameperformance_packageinfo) \*packageInfo) | 更新游戏包信息接口，用于上报游戏包信息。 |
| [GamePerformance\_ErrorCode](../harmonyos-references/gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_UpdateConfigInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_updateconfiginfo) ([GamePerformance\_ConfigInfo](../harmonyos-references/gameservice-game-performance.md#gameperformance_configinfo) \*configInfo) | 更新游戏配置信息接口，用于上报游戏配置信息。 |
| [GamePerformance\_ErrorCode](../harmonyos-references/gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_UpdateSceneInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_updatesceneinfo) ([GamePerformance\_SceneInfo](../harmonyos-references/gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo) | 更新游戏场景信息接口，用于上报游戏场景信息。 |
| [GamePerformance\_ErrorCode](../harmonyos-references/gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_UpdateNetInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_updatenetinfo) ([GamePerformance\_NetInfo](../harmonyos-references/gameservice-game-performance.md#gameperformance_netinfo) \*netInfo) | 更新游戏网络信息接口，用于上报游戏网络信息。 |
| [GamePerformance\_ErrorCode](../harmonyos-references/gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_UpdatePlayerInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_updateplayerinfo) ([GamePerformance\_PlayerInfo](../harmonyos-references/gameservice-game-performance.md#gameperformance_playerinfo) \*playerInfo) | 更新游戏玩家信息接口，用于上报游戏玩家信息。 |
| [GamePerformance\_ErrorCode](../harmonyos-references/gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_UnregisterThermalLevelChangedCallback](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_unregisterthermallevelchangedcallback) ([GamePerformance\_ThermalLevelChangedCallback](../harmonyos-references/gameservice-game-performance.md#gameperformance_thermallevelchangedcallback) callback) | 取消注册指定温度变化回调接口。 |
| [GamePerformance\_ErrorCode](../harmonyos-references/gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_UnregisterAllThermalLevelChangedCallbacks](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_unregisterallthermallevelchangedcallbacks) (void) | 取消注册所有温度变化回调接口。 |
| [GamePerformance\_ErrorCode](../harmonyos-references/gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_QueryThermalInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_querythermalinfo) ([GamePerformance\_ThermalInfoQueryParameters](../harmonyos-references/gameservice-game-performance.md#gameperformance_thermalinfoqueryparameters) \*parameters, [GamePerformance\_ThermalInfo](../harmonyos-references/gameservice-game-performance.md#gameperformance_thermalinfo) \*\*thermalInfo) | 查询温度信息接口。 |
| [GamePerformance\_ErrorCode](../harmonyos-references/gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_QueryGpuInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_querygpuinfo) ([GamePerformance\_GpuInfo](../harmonyos-references/gameservice-game-performance.md#gameperformance_gpuinfo) \*\*gpuInfo) | 查询GPU性能信息接口。 |
| [GamePerformance\_ErrorCode](../harmonyos-references/gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_QueryCpuInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_querycpuinfo) ([GamePerformance\_CpuInfo](../harmonyos-references/gameservice-game-performance.md#gameperformance_cpuinfo) \*\*cpuInfo) | 查询CPU性能信息接口。 |

## 接入步骤

### 在 CMake 脚本中链接动态库

```
1. target_include_directories(entry PUBLIC ${HMOS_SDK_NATIVE}/sysroot/usr/include)
2. target_link_directories(entry PUBLIC ${HMOS_SDK_NATIVE}/sysroot/usr/lib/aarch64-linux-ohos)
3. target_link_libraries(entry PUBLIC libgame_performance.z.so)
```

### 导入模块

导入Game Service Kit。

```
1. #include <GameServiceKit/game_performance.h>
2. #include <cstdlib>
```

### 初始化

导入相关模块后，需先调用[HMS\_GamePerformance\_Init](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_init)接口对游戏场景感知进行初始化。

说明

HMS\_GamePerformance\_Init接口是调用其他接口的前提，如果未初始化或初始化失败，将无法调用其他接口。

```
1. // 创建初始化参数
2. GamePerformance_InitParameters *initParameters = NULL;
3. HMS_GamePerformance_CreateInitParameters(&initParameters);

5. // 设置参数，所有SetXXX接口的第二个参数均为示例，请替换成实际参数
6. GamePerformance_ErrorCode appVersionSetCode = HMS_GamePerformance_InitParameters_SetAppVersion(initParameters, "1.0");

8. // 所有SetXXX接口，如果参数设置错误，将会返回错误码401；为确保参数设置无误，建议接收返回值并判断错误码
9. if (appVersionSetCode != GAME_PERFORMANCE_SUCCESS) {
10. // 异常处理
11. }
12. HMS_GamePerformance_InitParameters_SetBundleName(initParameters, "com.example.demo");

14. // 初始化
15. GamePerformance_ErrorCode ret = HMS_GamePerformance_Init(initParameters);
16. if (ret != GAME_PERFORMANCE_SUCCESS) {
17. // 异常处理
18. }

20. // 使用完释放内存
21. HMS_GamePerformance_DestroyInitParameters(&initParameters);
```

### 注册温度变化回调

调用[HMS\_GamePerformance\_RegisterThermalLevelChangedCallback](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_registerthermallevelchangedcallback)接口可以注册温度变化回调，获取设备状态信息的通知，包括温度相关信息、GPU负载和CPU负载信息。

```
1. // 定义回调函数
2. static void onThermalLevelChanged(GamePerformance_DeviceInfo *deviceInfo, void *userData) {
3. // 获取GPU负载等级（须订阅设备信息类型：GAME_PERFORMANCE_DEVICEINFO_TYPE_GPU）
4. (void) userData;
5. GamePerformance_GpuInfo *gpuInfo = NULL;
6. HMS_GamePerformance_DeviceInfo_GetGpuInfo(deviceInfo, &gpuInfo);
7. int32_t gpuloadLevel = -1;
8. int32_t vertexLevel = -1;
9. int32_t fragmentLoadLevel = -1;
10. int32_t bandwidthLoadLevel = -1;
11. int32_t textureLoadLevel = -1;
12. int32_t currentFrequency = -1;
13. HMS_GamePerformance_GpuInfo_GetGpuLoadLevel(gpuInfo, &gpuloadLevel);
14. HMS_GamePerformance_GpuInfo_GetVertexLoadLevel(gpuInfo, &vertexLevel);
15. HMS_GamePerformance_GpuInfo_GetFragmentLoadLevel(gpuInfo, &fragmentLoadLevel);
16. HMS_GamePerformance_GpuInfo_GetBandwidthLoadLevel(gpuInfo, &bandwidthLoadLevel);
17. HMS_GamePerformance_GpuInfo_GetTextureLoadLevel(gpuInfo, &textureLoadLevel);
18. HMS_GamePerformance_GpuInfo_GetCurrentFrequency(gpuInfo, &currentFrequency);

20. // 获取温度相关信息（须订阅设备信息类型：GAME_PERFORMANCE_DEVICEINFO_TYPE_THERMAL）
21. GamePerformance_ThermalInfo *thermalInfo = NULL;
22. HMS_GamePerformance_DeviceInfo_GetThermalInfo(deviceInfo, &thermalInfo);
23. int32_t margin = INT32_MIN;
24. int32_t trend = INT32_MIN;
25. int32_t level = -1;
26. int32_t recommendNormalizedCurrent = 0;
27. int32_t nowNormalizedCurrent = 0;
28. int32_t recommendMaxNormalizedCurrent = 0;
29. HMS_GamePerformance_ThermalInfo_GetThermalMargin(thermalInfo, &margin);
30. HMS_GamePerformance_ThermalInfo_GetThermalTrend(thermalInfo, &trend);
31. HMS_GamePerformance_ThermalInfo_GetThermalLevel(thermalInfo, &level);
32. HMS_GamePerformance_ThermalInfo_GetRecommendNormalizedCurrent(thermalInfo, &recommendNormalizedCurrent);
33. HMS_GamePerformance_ThermalInfo_GetNowNormalizedCurrent(thermalInfo, &nowNormalizedCurrent);
34. HMS_GamePerformance_ThermalInfo_GetRecommendMaxNormalizedCurrent(thermalInfo, &recommendMaxNormalizedCurrent);

36. // 获取CPU使用率（须订阅设备信息类型：GAME_PERFORMANCE_DEVICEINFO_TYPE_CPU）
37. GamePerformance_CpuInfo *cpuInfo = NULL;
38. HMS_GamePerformance_DeviceInfo_GetCpuInfo(deviceInfo, &cpuInfo);
39. int32_t cpuLoadLevel = 0;
40. int32_t singleThreadLoadLevel = 0;
41. HMS_GamePerformance_CpuInfo_GetCpuLoadLevel(cpuInfo, &cpuLoadLevel);
42. HMS_GamePerformance_CpuInfo_GetSingleThreadLoadLevel(cpuInfo, &singleThreadLoadLevel);

44. // 使用完释放内存
45. HMS_GamePerformance_DestroyGpuInfo(&gpuInfo);
46. HMS_GamePerformance_DestroyThermalInfo(&thermalInfo);
47. HMS_GamePerformance_DestroyCpuInfo(&cpuInfo);
48. }

50. // 注册回调
51. void registerCallback() {
52. // 按需订阅设备信息类型
53. int size = 2; // 订阅的设备信息类型的数量，即下文array数组的长度
54. GamePerformance_DeviceInfoType **array = (GamePerformance_DeviceInfoType **)malloc(sizeof(GamePerformance_DeviceInfoType *) * size);
55. if (array == NULL) {
56. // 异常处理
57. }
58. array[0] = (GamePerformance_DeviceInfoType *)malloc(sizeof(GamePerformance_DeviceInfoType));
59. array[1] = (GamePerformance_DeviceInfoType *)malloc(sizeof(GamePerformance_DeviceInfoType));
60. if (!array[0] || !array[1]) {
61. // 异常处理
62. }
63. *(array[0]) = GAME_PERFORMANCE_DEVICEINFO_TYPE_GPU;
64. *(array[1]) = GAME_PERFORMANCE_DEVICEINFO_TYPE_THERMAL;
65. void *userData = (void *)"mydata"; // 用户自定义任意类型，callback透传返回
66. GamePerformance_ErrorCode ret =
67. HMS_GamePerformance_RegisterThermalLevelChangedCallback(array, size, onThermalLevelChanged, userData);
68. free(array);
69. if (ret != GAME_PERFORMANCE_SUCCESS) {
70. // 异常处理
71. }
72. }
```

### 取消注册指定温度变化回调

调用[HMS\_GamePerformance\_UnregisterThermalLevelChangedCallback](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_unregisterthermallevelchangedcallback)接口可以取消注册指定温度变化回调。

```
1. // 取消注册
2. GamePerformance_ErrorCode ret = HMS_GamePerformance_UnregisterThermalLevelChangedCallback(onThermalLevelChanged);
3. if (ret != GAME_PERFORMANCE_SUCCESS) {
4. // 异常处理
5. }
```

### 取消注册所有温度变化回调

可以通过调用[HMS\_GamePerformance\_UnregisterAllThermalLevelChangedCallbacks](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_unregisterallthermallevelchangedcallbacks)接口可以取消注册所有温度变化回调。

```
1. // 取消所有注册的函数
2. GamePerformance_ErrorCode ret = HMS_GamePerformance_UnregisterAllThermalLevelChangedCallbacks();
3. if (ret != GAME_PERFORMANCE_SUCCESS) {
4. // 异常处理
5. }
```

### 上报游戏包信息

初始化成功后，可以通过调用[HMS\_GamePerformance\_UpdatePackageInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_updatepackageinfo)接口上报游戏包信息。

```
1. GamePerformance_PackageInfo *packageInfo = NULL;
2. HMS_GamePerformance_CreatePackageInfo(&packageInfo);

4. // SetXXX接口的第二个参数均为示例，请替换成实际参数
5. // 设置必选参数
6. HMS_GamePerformance_PackageInfo_SetBundleName(packageInfo, "com.example.demo");
7. HMS_GamePerformance_PackageInfo_SetAppVersion(packageInfo, "1.0");

9. // 按需设置可选参数
10. HMS_GamePerformance_PackageInfo_SetEngineType(packageInfo, GAME_PERFORMANCE_ENGINE_TYPE_COCOS);
11. HMS_GamePerformance_PackageInfo_SetEngineVersion(packageInfo, "2.0");
12. HMS_GamePerformance_PackageInfo_SetGameType(packageInfo, GAME_PERFORMANCE_GAME_TYPE_FPS);

14. // 上报游戏包信息
15. GamePerformance_ErrorCode ret = HMS_GamePerformance_UpdatePackageInfo(packageInfo);
16. if (ret != GAME_PERFORMANCE_SUCCESS) {
17. // 异常处理
18. }

20. // 使用完释放内存
21. HMS_GamePerformance_DestroyPackageInfo(&packageInfo);
```

### 上报游戏配置信息

初始化成功后，可以通过调用[HMS\_GamePerformance\_UpdateConfigInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_updateconfiginfo)接口上报游戏配置信息。

```
1. GamePerformance_ConfigInfo *configInfo = NULL;
2. HMS_GamePerformance_CreateConfigInfo(&configInfo);

4. // 如需多次上报，若使用同一个实例上报，只需通过set方法更新参数即可（同一个实例将保留上一次设置的数据）
5. // SetXXX接口的第二个参数均为示例，请替换成实际参数
6. // 按需设置下列可选字段
7. HMS_GamePerformance_ConfigInfo_SetMaxPictureQualityLevel(configInfo, GAME_PERFORMANCE_PQL_BALANCED);
8. HMS_GamePerformance_ConfigInfo_SetCurrentPictureQualityLevel(configInfo, GAME_PERFORMANCE_PQL_HD);
9. HMS_GamePerformance_ConfigInfo_SetMaxFrameRate(configInfo, 120);
10. HMS_GamePerformance_ConfigInfo_SetCurrentFrameRate(configInfo, 60);
11. HMS_GamePerformance_ConfigInfo_SetMaxResolution(configInfo, "1260*2720");
12. HMS_GamePerformance_ConfigInfo_SetCurrentResolution(configInfo, "1260*2720");
13. HMS_GamePerformance_ConfigInfo_SetAntiAliasingEnabled(configInfo, true);
14. HMS_GamePerformance_ConfigInfo_SetShadowEnabled(configInfo, true);
15. HMS_GamePerformance_ConfigInfo_SetMultithreadingEnabled(configInfo, true);
16. HMS_GamePerformance_ConfigInfo_SetParticleEnabled(configInfo, true);
17. HMS_GamePerformance_ConfigInfo_SetHdModeEnabled(configInfo, true);

19. // 上报游戏配置信息
20. GamePerformance_ErrorCode ret = HMS_GamePerformance_UpdateConfigInfo(configInfo);
21. if (ret != GAME_PERFORMANCE_SUCCESS) {
22. // 异常处理
23. }

25. // 使用完释放内存
26. HMS_GamePerformance_DestroyConfigInfo(&configInfo);
```

### 上报游戏场景信息

初始化成功后，可以通过调用[HMS\_GamePerformance\_UpdateSceneInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_updatesceneinfo)接口上报游戏场景信息。

```
1. // SetXXX接口的第二个参数均为示例，请替换成实际参数
2. GamePerformance_SceneInfo *sceneInfo = NULL;
3. HMS_GamePerformance_CreateSceneInfo(&sceneInfo);

5. // 如需多次上报，若使用同一个实例上报，只需通过set方法更新参数即可（同一个实例将保留上一次设置的数据）
6. // 设置必选字段
7. HMS_GamePerformance_SceneInfo_SetSceneID(sceneInfo, 1);
8. HMS_GamePerformance_SceneInfo_SetImportanceLevel(sceneInfo, GAME_PERFORMANCE_SIL_LEVEL1);

10. // 按需设置下列可选字段
11. HMS_GamePerformance_SceneInfo_SetDescription(sceneInfo, "this is description of scene");
12. HMS_GamePerformance_SceneInfo_SetSubSceneID(sceneInfo, "20101020304");
13. HMS_GamePerformance_SceneInfo_SetSubDescription(sceneInfo, "this is description of subScene");
14. HMS_GamePerformance_SceneInfo_SetSceneFrequency(sceneInfo, 2);
15. HMS_GamePerformance_SceneInfo_SetSceneTime(sceneInfo, 15);
16. HMS_GamePerformance_SceneInfo_SetRecommendedCpuLevel(sceneInfo, GAME_PERFORMANCE_CPU_LEVEL_HIGH);
17. HMS_GamePerformance_SceneInfo_SetRecommendedGpuLevel(sceneInfo, GAME_PERFORMANCE_GPU_LEVEL_HIGH);
18. HMS_GamePerformance_SceneInfo_SetRecommendedDdrLevel(sceneInfo, GAME_PERFORMANCE_DDR_LEVEL_HIGH);
19. HMS_GamePerformance_SceneInfo_SetKeyThread(sceneInfo, "render");
20. HMS_GamePerformance_SceneInfo_SetDrawCallCount(sceneInfo, 100);
21. HMS_GamePerformance_SceneInfo_SetVertexCount(sceneInfo, 100);
22. HMS_GamePerformance_SceneInfo_SetTriangleCount(sceneInfo, 100);
23. HMS_GamePerformance_SceneInfo_SetShaderCount(sceneInfo, 100);
24. HMS_GamePerformance_SceneInfo_SetTextureCount(sceneInfo, 100);
25. HMS_GamePerformance_SceneInfo_SetMeshCount(sceneInfo, 100);
26. HMS_GamePerformance_SceneInfo_SetChannelCount(sceneInfo, 100);
27. HMS_GamePerformance_SceneInfo_SetParticipantCount(sceneInfo, 5);

29. // 上报游戏场景信息
30. GamePerformance_ErrorCode ret = HMS_GamePerformance_UpdateSceneInfo(sceneInfo);
31. if (ret != GAME_PERFORMANCE_SUCCESS) {
32. // 异常处理
33. }

35. // 使用完释放内存
36. HMS_GamePerformance_DestroySceneInfo(&sceneInfo);
```

### 上报游戏网络信息

初始化成功后，可以通过调用[HMS\_GamePerformance\_UpdateNetInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_updatenetinfo)接口上报游戏网络信息。

```
1. // SetXXX接口的第二个参数均为示例，请替换成实际参数
2. GamePerformance_NetInfo *netInfo = NULL;
3. HMS_GamePerformance_CreateNetInfo(&netInfo);

5. // 如需多次上报，若使用同一个实例上报，只需通过set方法更新参数即可（同一个实例将保留上一次设置的数据）
6. // 设置必选字段
7. HMS_GamePerformance_NetInfo_SetTotalLatency(netInfo, 60);

9. // 按需设置下列可选字段
10. HMS_GamePerformance_NetInfo_SetNetLoad(netInfo, GAME_PERFORMANCE_NET_LOAD_HEAVY);
11. HMS_GamePerformance_NetInfo_SetUplinkLatency(netInfo, 10);
12. HMS_GamePerformance_NetInfo_SetDownlinkLatency(netInfo, 20);
13. HMS_GamePerformance_NetInfo_SetServerLatency(netInfo, 30);

15. // 上报游戏网络信息
16. GamePerformance_ErrorCode ret = HMS_GamePerformance_UpdateNetInfo(netInfo);
17. if (ret != GAME_PERFORMANCE_SUCCESS) {
18. // 异常处理
19. }

21. // 使用完释放内存
22. HMS_GamePerformance_DestroyNetInfo(&netInfo);
```

### 上报游戏玩家信息

初始化成功后，可以通过调用[HMS\_GamePerformance\_UpdatePlayerInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_updateplayerinfo)接口上报游戏玩家信息。

```
1. // SetXXX接口的第二个参数均为示例，请替换成实际参数
2. GamePerformance_PlayerInfo *playerInfo = NULL;
3. HMS_GamePerformance_CreatePlayerInfo(&playerInfo);

5. // 下列三个参数至少设置一个
6. HMS_GamePerformance_PlayerInfo_SetGamePlayerId(playerInfo, "43JIOdok74***3980sd9453");
7. HMS_GamePerformance_PlayerInfo_SetTeamPlayerId(playerInfo, "s2546dgs38***374dgwa5g3");
8. HMS_GamePerformance_PlayerInfo_SetThirdOpenId(playerInfo, "k854Cs367***937efwhi03");

10. // 上报游戏玩家信息
11. GamePerformance_ErrorCode ret = HMS_GamePerformance_UpdatePlayerInfo(playerInfo);
12. if (ret != GAME_PERFORMANCE_SUCCESS) {
13. // 异常处理
14. }

16. // 使用完释放内存
17. HMS_GamePerformance_DestroyPlayerInfo(&playerInfo);
```

### 查询GPU性能信息

除订阅设备状态变化的方式外，也可以通过调用[HMS\_GamePerformance\_QueryGpuInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_querygpuinfo)接口主动查询设备GPU性能信息。

```
1. // 查询GPU性能信息
2. GamePerformance_GpuInfo *gpuInfo = NULL;
3. GamePerformance_ErrorCode ret = HMS_GamePerformance_QueryGpuInfo(&gpuInfo);
4. if (ret != GAME_PERFORMANCE_SUCCESS) {
5. // 异常处理
6. }

8. // 获取指标数据值
9. int32_t gpuloadLevel = -1;
10. int32_t bandwidth = -1;
11. int32_t currentFrequency = -1;
12. int32_t fragmentLoadLevel = -1;
13. int32_t textureLoadLevel = -1;
14. int32_t vertexLoadLevel = -1;
15. HMS_GamePerformance_GpuInfo_GetGpuLoadLevel(gpuInfo, &gpuloadLevel);
16. HMS_GamePerformance_GpuInfo_GetBandwidthLoadLevel(gpuInfo, &bandwidth);
17. HMS_GamePerformance_GpuInfo_GetCurrentFrequency(gpuInfo, &currentFrequency);
18. HMS_GamePerformance_GpuInfo_GetFragmentLoadLevel(gpuInfo, &fragmentLoadLevel);
19. HMS_GamePerformance_GpuInfo_GetTextureLoadLevel(gpuInfo, &textureLoadLevel);
20. HMS_GamePerformance_GpuInfo_GetVertexLoadLevel(gpuInfo, &vertexLoadLevel);

22. // 使用完释放内存
23. HMS_GamePerformance_DestroyGpuInfo(&gpuInfo);
```

### 查询CPU性能信息

除订阅设备状态变化的方式外，也可以通过调用[HMS\_GamePerformance\_QueryCpuInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_querycpuinfo)接口主动查询设备CPU性能信息。

```
1. // 查询CPU性能信息
2. GamePerformance_CpuInfo *cpuInfo = NULL;
3. GamePerformance_ErrorCode ret = HMS_GamePerformance_QueryCpuInfo(&cpuInfo);
4. if (ret != GAME_PERFORMANCE_SUCCESS) {
5. // 异常处理
6. }

8. int32_t cpuLoadLevel = 0;
9. int32_t singleThreadLoadLevel = 0;
10. HMS_GamePerformance_CpuInfo_GetCpuLoadLevel(cpuInfo, &cpuLoadLevel);
11. HMS_GamePerformance_CpuInfo_GetSingleThreadLoadLevel(cpuInfo, &singleThreadLoadLevel);

13. // 使用完释放内存
14. HMS_GamePerformance_DestroyCpuInfo(&cpuInfo);
```

### 查询温度相关信息

除订阅设备状态变化的方式外，也可以通过调用[HMS\_GamePerformance\_QueryThermalInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_querythermalinfo)接口主动查询设备温控档位、温升趋势、当前的工作电流、系统建议的工作电流和系统建议的最大工作电流。

```
1. // 查询温度和温升趋势
2. GamePerformance_ThermalInfo *thermalInfo = NULL;
3. GamePerformance_ThermalInfoQueryParameters *parameters = NULL;

5. // 创建查询参数
6. HMS_GamePerformance_CreateThermalInfoQueryParameters(&parameters);

8. // 设置是否预测温升趋势。true：将查询温升趋势预测信息，false:不会查询温升趋势预测信息，默认为false。
9. HMS_GamePerformance_ThermalInfoQueryParameters_SetNeedsPrediction(parameters, true);

11. // needsPrediction=true时可选设置该参数。设置预测温升趋势的目标温度等级，设置后将以该温度等级作为目标温度等级进行温升趋势预测，若不设置，将使用系统默认档位进行预测。
12. HMS_GamePerformance_ThermalInfoQueryParameters_SetTargetThermalLevel(parameters, 4);

14. // 查询温度信息
15. GamePerformance_ErrorCode ret = HMS_GamePerformance_QueryThermalInfo(parameters, &thermalInfo);
16. if (ret != GAME_PERFORMANCE_SUCCESS) {
17. // 异常处理
18. }
19. int32_t margin = INT32_MIN;
20. int32_t trend = INT32_MIN;
21. int32_t level = -1;
22. int32_t recommendNormalizedCurrent = 0;
23. int32_t nowNormalizedCurrent = 0;
24. int32_t recommendMaxNormalizedCurrent = 0;
25. HMS_GamePerformance_ThermalInfo_GetThermalLevel(thermalInfo, &level);
26. HMS_GamePerformance_ThermalInfo_GetThermalMargin(thermalInfo, &margin); // needsPrediction=true时,返回有效值
27. HMS_GamePerformance_ThermalInfo_GetThermalTrend(thermalInfo, &trend); // needsPrediction=true时,返回有效值
28. HMS_GamePerformance_ThermalInfo_GetRecommendNormalizedCurrent(thermalInfo, &recommendNormalizedCurrent);
29. HMS_GamePerformance_ThermalInfo_GetNowNormalizedCurrent(thermalInfo, &nowNormalizedCurrent);
30. HMS_GamePerformance_ThermalInfo_GetRecommendMaxNormalizedCurrent(thermalInfo, &recommendMaxNormalizedCurrent);

32. // 使用完释放内存
33. HMS_GamePerformance_DestroyThermalInfo(&thermalInfo);
34. HMS_GamePerformance_DestroyThermalInfoQueryParameters(&parameters);
```

说明

查询温度变化趋势需要历史数据作为计算依据，调用[HMS\_GamePerformance\_QueryThermalInfo](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_querythermalinfo)接口时请保证设备已启动至少一分钟，否则会返回1010300001错误。
