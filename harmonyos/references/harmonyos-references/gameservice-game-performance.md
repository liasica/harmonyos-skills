---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-game-performance
title: GamePerformance
breadcrumb: API参考 > 应用服务 > Game Service Kit（游戏服务） > C API > 模块 > GamePerformance
category: harmonyos-references
scraped_at: 2026-04-28T08:16:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:44d9bc20c1f820ae960d704b5dabad71d56308529b1f9bccb81c836f1e9ad520
---

## 概述

PhonePC/2in1Tablet

为游戏场景感知模块提供C接口的定义。

**系统能力：** SystemCapability.GameService.GamePerformance

**起始版本：** 5.0.2(14)

## 汇总

PhonePC/2in1Tablet

### 文件

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [game\_performance.h](gameservice-game-performance-h.md) | 声明游戏场景感知的基本概念。 |

### 类型定义

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| typedef struct [GamePerformance\_DeviceInfo](gameservice-game-performance.md#gameperformance_deviceinfo) [GamePerformance\_DeviceInfo](gameservice-game-performance.md#gameperformance_deviceinfo) | 定义设备性能信息。 |
| typedef struct [GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo) [GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo) | 定义GPU性能信息。 |
| typedef struct [GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo) [GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo) | 定义CPU性能信息。 |
| typedef struct [GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo) [GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo) | 定义温度信息。 |
| typedef struct [GamePerformance\_ThermalInfoQueryParameters](gameservice-game-performance.md#gameperformance_thermalinfoqueryparameters) [GamePerformance\_ThermalInfoQueryParameters](gameservice-game-performance.md#gameperformance_thermalinfoqueryparameters) | 定义温度信息的查询参数。 |
| typedef struct [GamePerformance\_InitParameters](gameservice-game-performance.md#gameperformance_initparameters) [GamePerformance\_InitParameters](gameservice-game-performance.md#gameperformance_initparameters) | 定义初始化参数。 |
| typedef struct [GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo) [GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo) | 定义游戏包信息。 |
| typedef struct [GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo) [GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo) | 定义游戏配置信息。 |
| typedef struct [GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) [GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) | 定义游戏场景信息。 |
| typedef struct [GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo) [GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo) | 定义游戏网络信息。 |
| typedef struct [GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo) [GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo) | 定义游戏玩家信息。 |
| typedef enum [GamePerformance\_EngineType](gameservice-game-performance.md#gameperformance_enginetype-1) [GamePerformance\_EngineType](gameservice-game-performance.md#gameperformance_enginetype) | 定义游戏引擎类型。 |
| typedef enum [GamePerformance\_GameType](gameservice-game-performance.md#gameperformance_gametype-1) [GamePerformance\_GameType](gameservice-game-performance.md#gameperformance_gametype) | 定义游戏类型。 |
| typedef enum [GamePerformance\_PictureQualityLevel](gameservice-game-performance.md#gameperformance_picturequalitylevel-1) [GamePerformance\_PictureQualityLevel](gameservice-game-performance.md#gameperformance_picturequalitylevel) | 定义画质等级。 |
| typedef enum [GamePerformance\_SceneImportanceLevel](gameservice-game-performance.md#gameperformance_sceneimportancelevel-1) [GamePerformance\_SceneImportanceLevel](gameservice-game-performance.md#gameperformance_sceneimportancelevel) | 定义游戏场景重要程度。 |
| typedef enum [GamePerformance\_CpuLevel](gameservice-game-performance.md#gameperformance_cpulevel-1) [GamePerformance\_CpuLevel](gameservice-game-performance.md#gameperformance_cpulevel) | 定义CPU等级。 |
| typedef enum [GamePerformance\_GpuLevel](gameservice-game-performance.md#gameperformance_gpulevel-1) [GamePerformance\_GpuLevel](gameservice-game-performance.md#gameperformance_gpulevel) | 定义GPU等级。 |
| typedef enum [GamePerformance\_DdrLevel](gameservice-game-performance.md#gameperformance_ddrlevel-1) [GamePerformance\_DdrLevel](gameservice-game-performance.md#gameperformance_ddrlevel) | 定义DDR等级。 |
| typedef enum [GamePerformance\_NetLoad](gameservice-game-performance.md#gameperformance_netload-1) [GamePerformance\_NetLoad](gameservice-game-performance.md#gameperformance_netload) | 定义网络负载等级。 |
| typedef enum [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode) | 定义错误码。 |
| typedef enum [GamePerformance\_DeviceInfoType](gameservice-game-performance.md#gameperformance_deviceinfotype-1) [GamePerformance\_DeviceInfoType](gameservice-game-performance.md#gameperformance_deviceinfotype) | 定义设备性能信息类型。 |
| typedef void(\*[GamePerformance\_ThermalLevelChangedCallback](gameservice-game-performance.md#gameperformance_thermallevelchangedcallback)) ([GamePerformance\_DeviceInfo](gameservice-game-performance.md#gameperformance_deviceinfo) \*deviceInfo, void \*userData) | [HMS\_GamePerformance\_RegisterThermalLevelChangedCallback](gameservice-game-performance.md#hms_gameperformance_registerthermallevelchangedcallback)中使用的回调函数。当温度等级改变并且温度等级小于3档时，该函数将被调用一次。当温度等级大于或等于3档时，该函数将每10秒调用一次。 |

### 枚举

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [GamePerformance\_EngineType](gameservice-game-performance.md#gameperformance_enginetype-1) {  GAME\_PERFORMANCE\_ENGINE\_TYPE\_UNITY = 1,  GAME\_PERFORMANCE\_ENGINE\_TYPE\_UNREAL = 2,  GAME\_PERFORMANCE\_ENGINE\_TYPE\_MESSIAH = 3,  GAME\_PERFORMANCE\_ENGINE\_TYPE\_COCOS = 4,  GAME\_PERFORMANCE\_ENGINE\_TYPE\_OTHERS = 200  } | 此枚举描述引擎类型。 |
| [GamePerformance\_GameType](gameservice-game-performance.md#gameperformance_gametype-1) {  GAME\_PERFORMANCE\_GAME\_TYPE\_MOBA = 1,  GAME\_PERFORMANCE\_GAME\_TYPE\_RPG = 2,  GAME\_PERFORMANCE\_GAME\_TYPE\_FPS = 3,  GAME\_PERFORMANCE\_GAME\_TYPE\_FTG = 4,  GAME\_PERFORMANCE\_GAME\_TYPE\_RAC = 5,  GAME\_PERFORMANCE\_GAME\_TYPE\_OTHERS = 200  } | 此枚举描述游戏类型。 |
| [GamePerformance\_PictureQualityLevel](gameservice-game-performance.md#gameperformance_picturequalitylevel-1) {  GAME\_PERFORMANCE\_PQL\_SMOOTH = 1,  GAME\_PERFORMANCE\_PQL\_BALANCED = 2,  GAME\_PERFORMANCE\_PQL\_HD = 3,  GAME\_PERFORMANCE\_PQL\_HDR = 4,  GAME\_PERFORMANCE\_PQL\_UHD = 5  } | 此枚举描述画质等级。 |
| [GamePerformance\_SceneImportanceLevel](gameservice-game-performance.md#gameperformance_sceneimportancelevel-1) {  GAME\_PERFORMANCE\_SIL\_LEVEL1 = 1,  GAME\_PERFORMANCE\_SIL\_LEVEL2 = 2,  GAME\_PERFORMANCE\_SIL\_LEVEL3 = 3,  GAME\_PERFORMANCE\_SIL\_LEVEL4 = 4,  GAME\_PERFORMANCE\_SIL\_LEVEL5 = 5  } | 此枚举描述场景重要程度。 |
| [GamePerformance\_CpuLevel](gameservice-game-performance.md#gameperformance_cpulevel-1) {  GAME\_PERFORMANCE\_CPU\_LEVEL\_LOW = 1,  GAME\_PERFORMANCE\_CPU\_LEVEL\_MIDDLE = 2,  GAME\_PERFORMANCE\_CPU\_LEVEL\_HIGH = 3  } | 此枚举描述CPU等级。 |
| [GamePerformance\_GpuLevel](gameservice-game-performance.md#gameperformance_gpulevel-1) {  GAME\_PERFORMANCE\_GPU\_LEVEL\_LOW = 1,  GAME\_PERFORMANCE\_GPU\_LEVEL\_MIDDLE = 2,  GAME\_PERFORMANCE\_GPU\_LEVEL\_HIGH = 3  } | 此枚举描述GPU等级。 |
| [GamePerformance\_DdrLevel](gameservice-game-performance.md#gameperformance_ddrlevel-1) {  GAME\_PERFORMANCE\_DDR\_LEVEL\_LOW = 1,  GAME\_PERFORMANCE\_DDR\_LEVEL\_MIDDLE = 2,  GAME\_PERFORMANCE\_DDR\_LEVEL\_HIGH = 3  } | 此枚举描述DDR等级。 |
| [GamePerformance\_NetLoad](gameservice-game-performance.md#gameperformance_netload-1) {  GAME\_PERFORMANCE\_NET\_LOAD\_LIGHT = 1,  GAME\_PERFORMANCE\_NET\_LOAD\_MODERATE = 2,  GAME\_PERFORMANCE\_NET\_LOAD\_HEAVY = 3  } | 此枚举描述网络负载等级。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) {  GAME\_PERFORMANCE\_SUCCESS = 0,  GAME\_PERFORMANCE\_PARAM\_INVALID = 401,  GAME\_PERFORMANCE\_INTERNAL\_ERROR = 1010300001,  GAME\_PERFORMANCE\_AUTH\_FAILED = 1010300002,  GAME\_PERFORMANCE\_INVALID\_REQUEST = 1010300003,  GAME\_PERFORMANCE\_PARAM\_ERROR = 1010300004  } | 此枚举描述错误码。  GAME\_PERFORMANCE\_PARAM\_ERROR 从6.0.2(22)开始支持。 |
| [GamePerformance\_DeviceInfoType](gameservice-game-performance.md#gameperformance_deviceinfotype-1) {  GAME\_PERFORMANCE\_DEVICEINFO\_TYPE\_THERMAL = 0,  GAME\_PERFORMANCE\_DEVICEINFO\_TYPE\_GPU = 1,  GAME\_PERFORMANCE\_DEVICEINFO\_TYPE\_CPU = 2  } | 此枚举描述设备性能信息类型。  GAME\_PERFORMANCE\_DEVICEINFO\_TYPE\_CPU 从6.0.2(22)开始支持。 |

### 函数

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_CreateInitParameters](gameservice-game-performance.md#hms_gameperformance_createinitparameters) ([GamePerformance\_InitParameters](gameservice-game-performance.md#gameperformance_initparameters) \*\*initParameters) | 创建[GamePerformance\_InitParameters](gameservice-game-performance.md#gameperformance_initparameters)实例，该实例在[HMS\_GamePerformance\_Init](gameservice-game-performance.md#hms_gameperformance_init)方法中使用。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_DestroyInitParameters](gameservice-game-performance.md#hms_gameperformance_destroyinitparameters) ([GamePerformance\_InitParameters](gameservice-game-performance.md#gameperformance_initparameters) \*\*initParameters) | 当[GamePerformance\_InitParameters](gameservice-game-performance.md#gameperformance_initparameters)实例不再使用，销毁该实例。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_InitParameters\_SetBundleName](gameservice-game-performance.md#hms_gameperformance_initparameters_setbundlename) ([GamePerformance\_InitParameters](gameservice-game-performance.md#gameperformance_initparameters) \*initParameters, const char \*bundleName) | 为[GamePerformance\_InitParameters](gameservice-game-performance.md#gameperformance_initparameters)实例设置包名。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_InitParameters\_SetAppVersion](gameservice-game-performance.md#hms_gameperformance_initparameters_setappversion) ([GamePerformance\_InitParameters](gameservice-game-performance.md#gameperformance_initparameters) \*initParameters, const char \*appVersion) | 为[GamePerformance\_InitParameters](gameservice-game-performance.md#gameperformance_initparameters)实例设置版本号。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_Init](gameservice-game-performance.md#hms_gameperformance_init) ([GamePerformance\_InitParameters](gameservice-game-performance.md#gameperformance_initparameters) \*initParameters) | 初始化游戏场景感知。  **说明**：调用HMS\_GamePerformance\_Init前，必须已设置bundleName，appVersion。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_CreatePackageInfo](gameservice-game-performance.md#hms_gameperformance_createpackageinfo) ([GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo) \*\*packageInfo) | 创建[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例，该实例在[HMS\_GamePerformance\_UpdatePackageInfo](gameservice-game-performance.md#hms_gameperformance_updatepackageinfo)方法中使用。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_DestroyPackageInfo](gameservice-game-performance.md#hms_gameperformance_destroypackageinfo) ([GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo) \*\*packageInfo) | 当[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例不再使用，销毁该实例。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_PackageInfo\_SetBundleName](gameservice-game-performance.md#hms_gameperformance_packageinfo_setbundlename) ([GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo) \*packageInfo, const char \*bundleName) | 为[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例设置包名。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_PackageInfo\_SetAppVersion](gameservice-game-performance.md#hms_gameperformance_packageinfo_setappversion) ([GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo) \*packageInfo, const char \*appVersion) | 为[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例设置版本号。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_PackageInfo\_SetEngineType](gameservice-game-performance.md#hms_gameperformance_packageinfo_setenginetype) ([GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo) \*packageInfo, const [GamePerformance\_EngineType](gameservice-game-performance.md#gameperformance_enginetype-1) engineType) | 为[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例设置引擎类型。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_PackageInfo\_SetEngineVersion](gameservice-game-performance.md#hms_gameperformance_packageinfo_setengineversion) ([GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo) \*packageInfo, const char \*engineVersion) | 为[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例设置引擎版本号。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_PackageInfo\_SetGameType](gameservice-game-performance.md#hms_gameperformance_packageinfo_setgametype) ([GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo) \*packageInfo, const [GamePerformance\_GameType](gameservice-game-performance.md#gameperformance_gametype-1) gameType) | 为[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例设置游戏类型。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_PackageInfo\_SetVulkanSupported](gameservice-game-performance.md#hms_gameperformance_packageinfo_setvulkansupported) ([GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo) \*packageInfo, const bool vulkanSupported) | 为[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例设置是否支持vulkan。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_UpdatePackageInfo](gameservice-game-performance.md#hms_gameperformance_updatepackageinfo) ([GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo) \*packageInfo) | 更新游戏包信息。  **说明**：调用HMS\_GamePerformance\_UpdatePackageInfo前，必须已设置bundleName，appVersion。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_CreateConfigInfo](gameservice-game-performance.md#hms_gameperformance_createconfiginfo) ([GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo) \*\*configInfo) | 创建[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例，该实例在[HMS\_GamePerformance\_UpdateConfigInfo](gameservice-game-performance.md#hms_gameperformance_updateconfiginfo)方法中使用。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_DestroyConfigInfo](gameservice-game-performance.md#hms_gameperformance_destroyconfiginfo) ([GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo) \*\*configInfo) | 当[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例不再使用，销毁该实例。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_ConfigInfo\_SetMaxPictureQualityLevel](gameservice-game-performance.md#hms_gameperformance_configinfo_setmaxpicturequalitylevel) ([GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo) \*configInfo, const [GamePerformance\_PictureQualityLevel](gameservice-game-performance.md#gameperformance_picturequalitylevel-1) maxPictureQualityLevel) | 为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置最大画质等级。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_ConfigInfo\_SetCurrentPictureQualityLevel](gameservice-game-performance.md#hms_gameperformance_configinfo_setcurrentpicturequalitylevel) ([GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo) \*configInfo, const [GamePerformance\_PictureQualityLevel](gameservice-game-performance.md#gameperformance_picturequalitylevel-1) currentPictureQualityLevel) | 为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置当前画质等级。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_ConfigInfo\_SetMaxFrameRate](gameservice-game-performance.md#hms_gameperformance_configinfo_setmaxframerate) ([GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo) \*configInfo, const int64\_t maxFrameRate) | 为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置最大帧率。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_ConfigInfo\_SetCurrentFrameRate](gameservice-game-performance.md#hms_gameperformance_configinfo_setcurrentframerate) ([GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo) \*configInfo, const int64\_t currentFrameRate) | 为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置当前帧率。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_ConfigInfo\_SetMaxResolution](gameservice-game-performance.md#hms_gameperformance_configinfo_setmaxresolution) ([GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo) \*configInfo, const char \*maxResolution) | 为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置最大分辨率。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_ConfigInfo\_SetCurrentResolution](gameservice-game-performance.md#hms_gameperformance_configinfo_setcurrentresolution) ([GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo) \*configInfo, const char \*currentResolution) | 为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置当前分辨率。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_ConfigInfo\_SetAntiAliasingEnabled](gameservice-game-performance.md#hms_gameperformance_configinfo_setantialiasingenabled) ([GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo) \*configInfo, const bool antiAliasingEnabled) | 为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置是否开启抗锯齿。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_ConfigInfo\_SetShadowEnabled](gameservice-game-performance.md#hms_gameperformance_configinfo_setshadowenabled) ([GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo) \*configInfo, const bool shadowEnabled) | 为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置是否开启阴影。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_ConfigInfo\_SetMultithreadingEnabled](gameservice-game-performance.md#hms_gameperformance_configinfo_setmultithreadingenabled) ([GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo) \*configInfo, const bool multithreadingEnabled) | 为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置开启多线程。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_ConfigInfo\_SetParticleEnabled](gameservice-game-performance.md#hms_gameperformance_configinfo_setparticleenabled) ([GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo) \*configInfo, const bool particleEnabled) | 为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置粒子效果。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_ConfigInfo\_SetHdModeEnabled](gameservice-game-performance.md#hms_gameperformance_configinfo_sethdmodeenabled) ([GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo) \*configInfo, const bool hdModeEnabled) | 为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置开启高清模式。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_UpdateConfigInfo](gameservice-game-performance.md#hms_gameperformance_updateconfiginfo) ([GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo) \*configInfo) | 更新游戏配置信息。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_CreateSceneInfo](gameservice-game-performance.md#hms_gameperformance_createsceneinfo) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*\*sceneInfo) | 创建[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例，该实例在[HMS\_GamePerformance\_UpdateSceneInfo](gameservice-game-performance.md#hms_gameperformance_updatesceneinfo)方法中使用。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_DestroySceneInfo](gameservice-game-performance.md#hms_gameperformance_destroysceneinfo) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*\*sceneInfo) | 当[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例不再使用，销毁该实例。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_SceneInfo\_SetSceneID](gameservice-game-performance.md#hms_gameperformance_sceneinfo_setsceneid) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo, const int64\_t sceneID) | 为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置场景ID。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_SceneInfo\_SetDescription](gameservice-game-performance.md#hms_gameperformance_sceneinfo_setdescription) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo, const char \*description) | 为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置场景描述。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_SceneInfo\_SetSubSceneID](gameservice-game-performance.md#hms_gameperformance_sceneinfo_setsubsceneid) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo, const char \*subSceneID) | 为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置子场景ID。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_SceneInfo\_SetSubDescription](gameservice-game-performance.md#hms_gameperformance_sceneinfo_setsubdescription) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo, const char \*subDescription) | 为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置子场景描述。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_SceneInfo\_SetImportanceLevel](gameservice-game-performance.md#hms_gameperformance_sceneinfo_setimportancelevel) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo, const [GamePerformance\_SceneImportanceLevel](gameservice-game-performance.md#gameperformance_sceneimportancelevel-1) importanceLevel) | 为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置场景重要程度。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_SceneInfo\_SetSceneFrequency](gameservice-game-performance.md#hms_gameperformance_sceneinfo_setscenefrequency) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo, const int64\_t sceneFrequency) | 为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置该场景在一局游戏中出现的次数。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_SceneInfo\_SetSceneTime](gameservice-game-performance.md#hms_gameperformance_sceneinfo_setscenetime) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo, const int64\_t sceneTime) | 为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置场景持续时间。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_SceneInfo\_SetRecommendedCpuLevel](gameservice-game-performance.md#hms_gameperformance_sceneinfo_setrecommendedcpulevel) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo, const [GamePerformance\_CpuLevel](gameservice-game-performance.md#gameperformance_cpulevel-1) recommendedCpuLevel) | 为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置推荐的CPU等级。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_SceneInfo\_SetRecommendedGpuLevel](gameservice-game-performance.md#hms_gameperformance_sceneinfo_setrecommendedgpulevel) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo, const [GamePerformance\_GpuLevel](gameservice-game-performance.md#gameperformance_gpulevel-1) recommendedGpuLevel) | 为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置推荐的GPU等级。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_SceneInfo\_SetRecommendedDdrLevel](gameservice-game-performance.md#hms_gameperformance_sceneinfo_setrecommendedddrlevel) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo, const [GamePerformance\_DdrLevel](gameservice-game-performance.md#gameperformance_ddrlevel-1) recommendedDdrLevel) | 为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置推荐的DDR等级。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_SceneInfo\_SetMaxFrameRate](gameservice-game-performance.md#hms_gameperformance_sceneinfo_setmaxframerate) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo, const int64\_t maxFrameRate) | 为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置场景最大帧率。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_SceneInfo\_SetCurrentFrameRate](gameservice-game-performance.md#hms_gameperformance_sceneinfo_setcurrentframerate) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo, const int64\_t currentFrameRate) | 为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置场景当前帧率。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_SceneInfo\_SetKeyThread](gameservice-game-performance.md#hms_gameperformance_sceneinfo_setkeythread) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo, const char \*keyThread) | 为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置关键线程。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_SceneInfo\_SetDrawCallCount](gameservice-game-performance.md#hms_gameperformance_sceneinfo_setdrawcallcount) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo, const int64\_t drawCallCount) | 为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置每帧的平均Drawcall数。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_SceneInfo\_SetVertexCount](gameservice-game-performance.md#hms_gameperformance_sceneinfo_setvertexcount) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo, const int64\_t vertexCount) | 为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置每帧的平均模型顶点数。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_SceneInfo\_SetTriangleCount](gameservice-game-performance.md#hms_gameperformance_sceneinfo_settrianglecount) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo, const int64\_t triangleCount) | 为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置每帧的平均模型三角形数。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_SceneInfo\_SetShaderCount](gameservice-game-performance.md#hms_gameperformance_sceneinfo_setshadercount) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo, const int64\_t shaderCount) | 为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置每帧的平均shader数量。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_SceneInfo\_SetTextureCount](gameservice-game-performance.md#hms_gameperformance_sceneinfo_settexturecount) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo, const int64\_t textureCount) | 为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置每帧的平均纹理数量。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_SceneInfo\_SetMeshCount](gameservice-game-performance.md#hms_gameperformance_sceneinfo_setmeshcount) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo, const int64\_t meshCount) | 为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置每帧的平均mesh数量。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_SceneInfo\_SetChannelCount](gameservice-game-performance.md#hms_gameperformance_sceneinfo_setchannelcount) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo, const int64\_t channelCount) | 为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置每帧渲染的通道数。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_SceneInfo\_SetParticipantCount](gameservice-game-performance.md#hms_gameperformance_sceneinfo_setparticipantcount) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo, const int64\_t participantCount) | 为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置场景下的同屏人数。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_UpdateSceneInfo](gameservice-game-performance.md#hms_gameperformance_updatesceneinfo) ([GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo) \*sceneInfo) | 更新游戏场景信息。  **说明**：调用HMS\_GamePerformance\_UpdateSceneInfo前，必须已设置sceneID，importanceLevel。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_CreateNetInfo](gameservice-game-performance.md#hms_gameperformance_createnetinfo) ([GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo) \*\*netInfo) | 创建[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例，该实例在[HMS\_GamePerformance\_UpdateNetInfo](gameservice-game-performance.md#hms_gameperformance_updatenetinfo)方法中使用。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_DestroyNetInfo](gameservice-game-performance.md#hms_gameperformance_destroynetinfo) ([GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo) \*\*netInfo) | 当[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例不再使用，销毁该实例。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_NetInfo\_SetTotalLatency](gameservice-game-performance.md#hms_gameperformance_netinfo_settotallatency) ([GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo) \*netInfo, const int64\_t total) | 为[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例设置总网络时延。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_NetInfo\_SetUplinkLatency](gameservice-game-performance.md#hms_gameperformance_netinfo_setuplinklatency) ([GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo) \*netInfo, const int64\_t up) | 为[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例设置上行网络时延。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_NetInfo\_SetDownlinkLatency](gameservice-game-performance.md#hms_gameperformance_netinfo_setdownlinklatency) ([GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo) \*netInfo, const int64\_t down) | 为[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例设置下行网络时延。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_NetInfo\_SetServerLatency](gameservice-game-performance.md#hms_gameperformance_netinfo_setserverlatency) ([GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo) \*netInfo, const int64\_t server) | 为[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例设置服务器网络时延。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_NetInfo\_SetNetLoad](gameservice-game-performance.md#hms_gameperformance_netinfo_setnetload) ([GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo) \*netInfo, const [GamePerformance\_NetLoad](gameservice-game-performance.md#gameperformance_netload-1) netLoad) | 为[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例设置网络负载。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_UpdateNetInfo](gameservice-game-performance.md#hms_gameperformance_updatenetinfo) ([GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo) \*netInfo) | 更新游戏网络信息。  **说明**：调用HMS\_GamePerformance\_UpdateNetInfo前必须已设置totalLatency。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_CreatePlayerInfo](gameservice-game-performance.md#hms_gameperformance_createplayerinfo) ([GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo) \*\*playerInfo) | 创建[GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo)实例，该实例在[HMS\_GamePerformance\_UpdatePlayerInfo](gameservice-game-performance.md#hms_gameperformance_updateplayerinfo)方法中使用。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_DestroyPlayerInfo](gameservice-game-performance.md#hms_gameperformance_destroyplayerinfo) ([GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo) \*\*playerInfo) | 当[GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo)实例不再使用，销毁该实例。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_PlayerInfo\_SetGamePlayerId](gameservice-game-performance.md#hms_gameperformance_playerinfo_setgameplayerid) ([GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo) \*playerInfo, const char \*gamePlayerId) | 为[GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo)实例设置游戏玩家ID。  **说明**：gamePlayerId、teamPlayerId和thirdOpenId不能同时为空。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_PlayerInfo\_SetTeamPlayerId](gameservice-game-performance.md#hms_gameperformance_playerinfo_setteamplayerid) ([GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo) \*playerInfo, const char \*teamPlayerId) | 为[GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo)实例设置团队玩家ID。  **说明**：gamePlayerId、teamPlayerId和thirdOpenId不能同时为空。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_PlayerInfo\_SetThirdOpenId](gameservice-game-performance.md#hms_gameperformance_playerinfo_setthirdopenid) ([GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo) \*playerInfo, const char \*thirdOpenId) | 为[GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo)实例设置游戏官方账号。  **说明**：gamePlayerId、teamPlayerId和thirdOpenId不能同时为空。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_UpdatePlayerInfo](gameservice-game-performance.md#hms_gameperformance_updateplayerinfo) ([GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo) \*playerInfo) | 更新游戏玩家信息。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_RegisterThermalLevelChangedCallback](gameservice-game-performance.md#hms_gameperformance_registerthermallevelchangedcallback) ([GamePerformance\_DeviceInfoType](gameservice-game-performance.md#gameperformance_deviceinfotype-1) \*types[], size\_t size, [GamePerformance\_ThermalLevelChangedCallback](gameservice-game-performance.md#gameperformance_thermallevelchangedcallback) callback, void \*userData) | 订阅温度变化事件，注册温度变化回调，当达到触发点时，将调用回调函数。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_UnregisterThermalLevelChangedCallback](gameservice-game-performance.md#hms_gameperformance_unregisterthermallevelchangedcallback) ([GamePerformance\_ThermalLevelChangedCallback](gameservice-game-performance.md#gameperformance_thermallevelchangedcallback) callback) | 取消注册指定温度变化回调。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_UnregisterAllThermalLevelChangedCallbacks](gameservice-game-performance.md#hms_gameperformance_unregisterallthermallevelchangedcallbacks) (void) | 取消注册所有温度变化回调。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_CreateThermalInfoQueryParameters](gameservice-game-performance.md#hms_gameperformance_createthermalinfoqueryparameters) ([GamePerformance\_ThermalInfoQueryParameters](gameservice-game-performance.md#gameperformance_thermalinfoqueryparameters) \*\*parameters) | 创建[GamePerformance\_ThermalInfoQueryParameters](gameservice-game-performance.md#gameperformance_thermalinfoqueryparameters)实例，该实例在[HMS\_GamePerformance\_QueryThermalInfo](gameservice-game-performance.md#hms_gameperformance_querythermalinfo)方法中使用。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_DestroyThermalInfoQueryParameters](gameservice-game-performance.md#hms_gameperformance_destroythermalinfoqueryparameters) ([GamePerformance\_ThermalInfoQueryParameters](gameservice-game-performance.md#gameperformance_thermalinfoqueryparameters) \*\*parameters) | 当[GamePerformance\_ThermalInfoQueryParameters](gameservice-game-performance.md#gameperformance_thermalinfoqueryparameters)实例不再使用，销毁该实例。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_ThermalInfoQueryParameters\_SetNeedsPrediction](gameservice-game-performance.md#hms_gameperformance_thermalinfoqueryparameters_setneedsprediction) ([GamePerformance\_ThermalInfoQueryParameters](gameservice-game-performance.md#gameperformance_thermalinfoqueryparameters) \*parameters, const bool needsPrediction) | 为[GamePerformance\_ThermalInfoQueryParameters](gameservice-game-performance.md#gameperformance_thermalinfoqueryparameters)实例设置是否需要预测温升趋势。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_ThermalInfoQueryParameters\_SetTargetThermalLevel](gameservice-game-performance.md#hms_gameperformance_thermalinfoqueryparameters_settargetthermallevel) ([GamePerformance\_ThermalInfoQueryParameters](gameservice-game-performance.md#gameperformance_thermalinfoqueryparameters) \*parameters, const int32\_t targetThermalLevel) | 为[GamePerformance\_ThermalInfoQueryParameters](gameservice-game-performance.md#gameperformance_thermalinfoqueryparameters)实例设置预测温升趋势的目标温度等级。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_QueryThermalInfo](gameservice-game-performance.md#hms_gameperformance_querythermalinfo) ([GamePerformance\_ThermalInfoQueryParameters](gameservice-game-performance.md#gameperformance_thermalinfoqueryparameters) \*parameters，[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo) \*\*thermalInfo) | 查询温度信息。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_DestroyThermalInfo](gameservice-game-performance.md#hms_gameperformance_destroythermalinfo) ([GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo) \*\*thermalInfo) | 当[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)实例不再使用，销毁该实例。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_QueryGpuInfo](gameservice-game-performance.md#hms_gameperformance_querygpuinfo) ([GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo) \*\*gpuInfo) | 查询GPU性能信息。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_DestroyGpuInfo](gameservice-game-performance.md#hms_gameperformance_destroygpuinfo) ([GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo) \*\*gpuInfo) | 当[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)实例不再使用，销毁该实例。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_QueryCpuInfo](gameservice-game-performance.md#hms_gameperformance_querycpuinfo) ([GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo) \*\*cpuInfo) | 查询CPU性能信息。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_DestroyCpuInfo](gameservice-game-performance.md#hms_gameperformance_destroycpuinfo) ([GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo) \*\*cpuInfo) | 当[GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo)实例不再使用，销毁该实例。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_DeviceInfo\_GetThermalInfo](gameservice-game-performance.md#hms_gameperformance_deviceinfo_getthermalinfo) ([GamePerformance\_DeviceInfo](gameservice-game-performance.md#gameperformance_deviceinfo) \*deviceInfo, [GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo) \*\*thermalInfo) | 从设备性能信息[GamePerformance\_DeviceInfo](gameservice-game-performance.md#gameperformance_deviceinfo)中获取温度信息[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_ThermalInfo\_GetThermalMargin](gameservice-game-performance.md#hms_gameperformance_thermalinfo_getthermalmargin) ([GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo) \*thermalInfo, int32\_t \*thermalMargin) | 从温度信息[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)中获取温度时间裕量。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_ThermalInfo\_GetThermalTrend](gameservice-game-performance.md#hms_gameperformance_thermalinfo_getthermaltrend) ([GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo) \*thermalInfo, int32\_t \*thermalTrend) | 从[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)中获取温升趋势。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_ThermalInfo\_GetThermalLevel](gameservice-game-performance.md#hms_gameperformance_thermalinfo_getthermallevel) ([GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo) \*thermalInfo, int32\_t \*thermalLevel) | 从[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)中获取温度等级。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_ThermalInfo\_GetRecommendNormalizedCurrent](gameservice-game-performance.md#hms_gameperformance_thermalinfo_getrecommendnormalizedcurrent) ([GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo) \*thermalInfo, int32\_t \*recommendCurrent) | 从[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)中获取系统建议的工作电流。若当前的工作电流高于此值，温升趋势thermalTrend会大于0，设备有发烫风险。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_ThermalInfo\_GetNowNormalizedCurrent](gameservice-game-performance.md#hms_gameperformance_thermalinfo_getnownormalizedcurrent) ([GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo) \*thermalInfo, int32\_t \*nowCurrent) | 从[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)中获取当前的工作电流。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_ThermalInfo\_GetRecommendMaxNormalizedCurrent](gameservice-game-performance.md#hms_gameperformance_thermalinfo_getrecommendmaxnormalizedcurrent) ([GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo) \*thermalInfo, int32\_t \*recommendMaxCurrent) | 从[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)中获取系统建议的最大工作电流。若当前的工作电流高于此值，设备会立即发烫。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_DeviceInfo\_GetGpuInfo](gameservice-game-performance.md#hms_gameperformance_deviceinfo_getgpuinfo) ([GamePerformance\_DeviceInfo](gameservice-game-performance.md#gameperformance_deviceinfo) \*deviceInfo, [GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo) \*\*gpuInfo) | 从设备性能信息[GamePerformance\_DeviceInfo](gameservice-game-performance.md#gameperformance_deviceinfo)中获取GPU性能信息[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_GpuInfo\_GetGpuLoadLevel](gameservice-game-performance.md#hms_gameperformance_gpuinfo_getgpuloadlevel) ([GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo) \*gpuInfo, int32\_t \*gpuLoadLevel) | 从[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)中获取GPU负载信息。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_GpuInfo\_GetVertexLoadLevel](gameservice-game-performance.md#hms_gameperformance_gpuinfo_getvertexloadlevel) ([GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo) \*gpuInfo, int32\_t \*vertexLoadLevel) | 从[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)中获取GPU顶点处理负载等级。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_GpuInfo\_GetFragmentLoadLevel](gameservice-game-performance.md#hms_gameperformance_gpuinfo_getfragmentloadlevel) ([GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo) \*gpuInfo, int32\_t \*fragmentLoadLevel) | 从[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)中获取GPU片元处理负载等级。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_GpuInfo\_GetTextureLoadLevel](gameservice-game-performance.md#hms_gameperformance_gpuinfo_gettextureloadlevel) ([GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo) \*gpuInfo, int32\_t \*textureLoadLevel) | 从[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)中获取GPU纹理处理负载等级。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_GpuInfo\_GetBandwidthLoadLevel](gameservice-game-performance.md#hms_gameperformance_gpuinfo_getbandwidthloadlevel) ([GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo) \*gpuInfo, int32\_t \*bandwidthLoadLevel) | 从[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)中获取GPU带宽负载等级。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_GpuInfo\_GetCurrentFrequency](gameservice-game-performance.md#hms_gameperformance_gpuinfo_getcurrentfrequency) ([GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo) \*gpuInfo, int32\_t \*currentFrequency) | 从[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)中获取GPU频点信息。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_DeviceInfo\_GetCpuInfo](gameservice-game-performance.md#hms_gameperformance_deviceinfo_getcpuinfo) ([GamePerformance\_DeviceInfo](gameservice-game-performance.md#gameperformance_deviceinfo) \*deviceInfo, [GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo) \*\*cpuInfo) | 从设备性能信息[GamePerformance\_DeviceInfo](gameservice-game-performance.md#gameperformance_deviceinfo)中获取CPU性能信息[GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo)。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_CpuInfo\_GetCpuLoadLevel](gameservice-game-performance.md#hms_gameperformance_cpuinfo_getcpuloadlevel) ([GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo) \*cpuInfo, int32\_t \*cpuLoadLevel) | 从[GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo)中获取CPU负载整体等级。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_CpuInfo\_GetSingleThreadLoadLevel](gameservice-game-performance.md#hms_gameperformance_cpuinfo_getsinglethreadloadlevel) ([GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo) \*cpuInfo, int32\_t \*singleThreadLoadLevel) | 从[GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo)中获取游戏最重线程的负载整体等级。 |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) [HMS\_GamePerformance\_DestroyDeviceInfo](gameservice-game-performance.md#hms_gameperformance_destroydeviceinfo) ([GamePerformance\_DeviceInfo](gameservice-game-performance.md#gameperformance_deviceinfo) \*\*deviceInfo) | 当[GamePerformance\_DeviceInfo](gameservice-game-performance.md#gameperformance_deviceinfo)实例不再使用，销毁该实例。 |

## 类型定义说明

PhonePC/2in1Tablet

### GamePerformance\_ConfigInfo

PhonePC/2in1Tablet

```
1. typedef struct GamePerformance_ConfigInfo GamePerformance_ConfigInfo
```

**描述**

定义游戏配置信息。

**起始版本：** 5.0.2(14)

### GamePerformance\_CpuInfo

PhonePC/2in1Tablet

```
1. typedef struct GamePerformance_CpuInfo GamePerformance_CpuInfo
```

**描述**

定义CPU性能信息。

**起始版本：** 6.0.2(22)

### GamePerformance\_CpuLevel

PhonePC/2in1Tablet

```
1. typedef enum GamePerformance_CpuLevel GamePerformance_CpuLevel
```

**描述**

定义CPU等级。

**起始版本：** 5.0.2(14)

### GamePerformance\_DdrLevel

PhonePC/2in1Tablet

```
1. typedef enum GamePerformance_DdrLevel GamePerformance_DdrLevel
```

**描述**

定义DDR等级。

**起始版本：** 5.0.2(14)

### GamePerformance\_DeviceInfo

PhonePC/2in1Tablet

```
1. typedef struct GamePerformance_DeviceInfo GamePerformance_DeviceInfo
```

**描述**

定义设备性能信息。

**起始版本：** 5.0.2(14)

### GamePerformance\_DeviceInfoType

PhonePC/2in1Tablet

```
1. typedef enum GamePerformance_DeviceInfoType GamePerformance_DeviceInfoType
```

**描述**

定义设备性能信息类型。

**起始版本：** 5.0.2(14)

### GamePerformance\_EngineType

PhonePC/2in1Tablet

```
1. typedef enum GamePerformance_EngineType GamePerformance_EngineType
```

**描述**

定义游戏引擎类型。

**起始版本：** 5.0.2(14)

### GamePerformance\_ErrorCode

PhonePC/2in1Tablet

```
1. typedef enum GamePerformance_ErrorCode GamePerformance_ErrorCode
```

**描述**

定义错误码。

**起始版本：** 5.0.2(14)

### GamePerformance\_GameType

PhonePC/2in1Tablet

```
1. typedef enum GamePerformance_GameType GamePerformance_GameType
```

**描述**

定义游戏类型。

**起始版本：** 5.0.2(14)

### GamePerformance\_GpuInfo

PhonePC/2in1Tablet

```
1. typedef struct GamePerformance_GpuInfo GamePerformance_GpuInfo
```

**描述**

定义GPU性能信息。

**起始版本：** 5.0.2(14)

### GamePerformance\_GpuLevel

PhonePC/2in1Tablet

```
1. typedef enum GamePerformance_GpuLevel GamePerformance_GpuLevel
```

**描述**

定义GPU等级。

**起始版本：** 5.0.2(14)

### GamePerformance\_InitParameters

PhonePC/2in1Tablet

```
1. typedef struct GamePerformance_InitParameters GamePerformance_InitParameters
```

**描述**

定义初始化参数。

**起始版本：** 5.0.2(14)

### GamePerformance\_NetInfo

PhonePC/2in1Tablet

```
1. typedef struct GamePerformance_NetInfo GamePerformance_NetInfo
```

**描述**

定义游戏网络信息。

**起始版本：** 5.0.2(14)

### GamePerformance\_NetLoad

PhonePC/2in1Tablet

```
1. typedef enum GamePerformance_NetLoad GamePerformance_NetLoad
```

**描述**

定义网络负载等级。

**起始版本：** 5.0.2(14)

### GamePerformance\_PackageInfo

PhonePC/2in1Tablet

```
1. typedef struct GamePerformance_PackageInfo GamePerformance_PackageInfo
```

**描述**

定义包信息。

**起始版本：** 5.0.2(14)

### GamePerformance\_PictureQualityLevel

PhonePC/2in1Tablet

```
1. typedef enum GamePerformance_PictureQualityLevel GamePerformance_PictureQualityLevel
```

**描述**

定义画质等级。

**起始版本：** 5.0.2(14)

### GamePerformance\_PlayerInfo

PhonePC/2in1Tablet

```
1. typedef struct GamePerformance_PlayerInfo GamePerformance_PlayerInfo
```

**描述**

定义游戏玩家信息。

**起始版本：** 5.0.2(14)

### GamePerformance\_SceneImportanceLevel

PhonePC/2in1Tablet

```
1. typedef enum GamePerformance_SceneImportanceLevel GamePerformance_SceneImportanceLevel
```

**描述**

定义场景重要程度。

**起始版本：** 5.0.2(14)

### GamePerformance\_SceneInfo

PhonePC/2in1Tablet

```
1. typedef struct GamePerformance_SceneInfo GamePerformance_SceneInfo
```

**描述**

定义游戏场景信息。

**起始版本：** 5.0.2(14)

### GamePerformance\_ThermalInfo

PhonePC/2in1Tablet

```
1. typedef struct GamePerformance_ThermalInfo GamePerformance_ThermalInfo
```

**描述**

定义温度信息。

**起始版本：** 5.0.2(14)

### GamePerformance\_ThermalInfoQueryParameters

PhonePC/2in1Tablet

```
1. typedef struct GamePerformance_ThermalInfoQueryParameters GamePerformance_ThermalInfoQueryParameters
```

**描述**

定义温度信息的查询参数。

**起始版本：** 5.0.2(14)

### GamePerformance\_ThermalLevelChangedCallback

PhonePC/2in1Tablet

```
1. typedef void(*GamePerformance_ThermalLevelChangedCallback) (GamePerformance_DeviceInfo *deviceInfo, void *userData)
```

**描述**

[HMS\_GamePerformance\_RegisterThermalLevelChangedCallback](gameservice-game-performance.md#hms_gameperformance_registerthermallevelchangedcallback)中使用的回调函数。当温度等级改变并且温度等级小于3时，该函数将被调用一次。当温度等级大于或等于3级时，该函数将每10秒调用一次。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 设备详细信息[GamePerformance\_DeviceInfo](gameservice-game-performance.md#gameperformance_deviceinfo)。 |
| userData | 用户指定的数据。用户自定义传参。 |

## 枚举类型说明

PhonePC/2in1Tablet

### GamePerformance\_CpuLevel

PhonePC/2in1Tablet

```
1. enum GamePerformance_CpuLevel
```

**描述**

定义CPU等级。

**起始版本：** 5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| GAME\_PERFORMANCE\_CPU\_LEVEL\_LOW | 低。 |
| GAME\_PERFORMANCE\_CPU\_LEVEL\_MIDDLE | 中。 |
| GAME\_PERFORMANCE\_CPU\_LEVEL\_HIGH | 高。 |

### GamePerformance\_DdrLevel

PhonePC/2in1Tablet

```
1. enum GamePerformance_DdrLevel
```

**描述**

定义DDR等级。

**起始版本：** 5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| GAME\_PERFORMANCE\_DDR\_LEVEL\_LOW | 低。 |
| GAME\_PERFORMANCE\_DDR\_LEVEL\_MIDDLE | 中。 |
| GAME\_PERFORMANCE\_DDR\_LEVEL\_HIGH | 高。 |

### GamePerformance\_DeviceInfoType

PhonePC/2in1Tablet

```
1. enum GamePerformance_DeviceInfoType
```

**描述**

定义回调返回的设备性能信息类型。

**起始版本：** 5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| GAME\_PERFORMANCE\_DEVICEINFO\_TYPE\_THERMAL | 温度信息。 |
| GAME\_PERFORMANCE\_DEVICEINFO\_TYPE\_GPU | GPU性能信息。 |
| GAME\_PERFORMANCE\_DEVICEINFO\_TYPE\_CPU | CPU性能信息。  **起始版本：** 6.0.2(22) |

### GamePerformance\_EngineType

PhonePC/2in1Tablet

```
1. enum GamePerformance_EngineType
```

**描述**

定义游戏引擎类型。

**起始版本：** 5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| GAME\_PERFORMANCE\_ENGINE\_TYPE\_UNITY | UNITY。 |
| GAME\_PERFORMANCE\_ENGINE\_TYPE\_UNREAL | UNREAL。 |
| GAME\_PERFORMANCE\_ENGINE\_TYPE\_MESSIAH | MESSIAH。 |
| GAME\_PERFORMANCE\_ENGINE\_TYPE\_COCOS | COCOS。 |
| GAME\_PERFORMANCE\_ENGINE\_TYPE\_OTHERS | 其他引擎类型。 |

### GamePerformance\_ErrorCode

PhonePC/2in1Tablet

```
1. enum GamePerformance_ErrorCode
```

**描述**

定义错误码。

**起始版本：** 5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| GAME\_PERFORMANCE\_SUCCESS | 成功。 |
| GAME\_PERFORMANCE\_PARAM\_INVALID | 无效参数。 |
| GAME\_PERFORMANCE\_INTERNAL\_ERROR | 系统内部错误。 |
| GAME\_PERFORMANCE\_AUTH\_FAILED | 鉴权失败。 |
| GAME\_PERFORMANCE\_INVALID\_REQUEST | 非法请求。 |
| GAME\_PERFORMANCE\_PARAM\_ERROR | 参数错误。  起始版本：6.0.2(22) |

### GamePerformance\_GameType

PhonePC/2in1Tablet

```
1. enum GamePerformance_GameType
```

**描述**

定义游戏类型。

**起始版本：** 5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| GAME\_PERFORMANCE\_GAME\_TYPE\_MOBA | 多人在线战术竞技。 |
| GAME\_PERFORMANCE\_GAME\_TYPE\_RPG | 角色扮演。 |
| GAME\_PERFORMANCE\_GAME\_TYPE\_FPS | 第一人称射击类。 |
| GAME\_PERFORMANCE\_GAME\_TYPE\_FTG | 格斗游戏。 |
| GAME\_PERFORMANCE\_GAME\_TYPE\_RAC | 竞速游戏。 |
| GAME\_PERFORMANCE\_GAME\_TYPE\_OTHERS | 其他游戏类型。 |

### GamePerformance\_GpuLevel

PhonePC/2in1Tablet

```
1. enum GamePerformance_GpuLevel
```

**描述**

定义GPU等级。

**起始版本：** 5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| GAME\_PERFORMANCE\_GPU\_LEVEL\_LOW | 低。 |
| GAME\_PERFORMANCE\_GPU\_LEVEL\_MIDDLE | 中。 |
| GAME\_PERFORMANCE\_GPU\_LEVEL\_HIGH | 高。 |

### GamePerformance\_NetLoad

PhonePC/2in1Tablet

```
1. enum GamePerformance_NetLoad
```

**描述**

定义网络负载等级。

**起始版本：** 5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| GAME\_PERFORMANCE\_NET\_LOAD\_LIGHT | 轻度负载。 |
| GAME\_PERFORMANCE\_NET\_LOAD\_MODERATE | 中度负载。 |
| GAME\_PERFORMANCE\_NET\_LOAD\_HEAVY | 重度负载。 |

### GamePerformance\_PictureQualityLevel

PhonePC/2in1Tablet

```
1. enum GamePerformance_PictureQualityLevel
```

**描述**

定义画质等级。

**起始版本：** 5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| GAME\_PERFORMANCE\_PQL\_SMOOTH | 流畅。 |
| GAME\_PERFORMANCE\_PQL\_BALANCED | 均衡。 |
| GAME\_PERFORMANCE\_PQL\_HD | 高清。 |
| GAME\_PERFORMANCE\_PQL\_HDR | HDR高清。 |
| GAME\_PERFORMANCE\_PQL\_UHD | 超高清。 |

### GamePerformance\_SceneImportanceLevel

PhonePC/2in1Tablet

```
1. enum GamePerformance_SceneImportanceLevel
```

**描述**

定义游戏场景重要程度，5个等级，重要程度从1到5递增。

**起始版本：** 5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| GAME\_PERFORMANCE\_SIL\_LEVEL1 | 等级1。 |
| GAME\_PERFORMANCE\_SIL\_LEVEL2 | 等级2。 |
| GAME\_PERFORMANCE\_SIL\_LEVEL3 | 等级3。 |
| GAME\_PERFORMANCE\_SIL\_LEVEL4 | 等级4。 |
| GAME\_PERFORMANCE\_SIL\_LEVEL5 | 等级5。 |

## 函数说明

PhonePC/2in1Tablet

### HMS\_GamePerformance\_ConfigInfo\_SetAntiAliasingEnabled()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetAntiAliasingEnabled (GamePerformance_ConfigInfo *configInfo, const bool antiAliasingEnabled)
```

**描述**

为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置是否开启抗锯齿。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例。该值不可以为空，否则将返回错误码401。 |
| antiAliasingEnabled | 是否开启抗锯齿。  - true：开启  - false：不开启  默认为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_ConfigInfo\_SetCurrentFrameRate()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetCurrentFrameRate (GamePerformance_ConfigInfo *configInfo, const int64_t currentFrameRate)
```

**描述**

为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置当前帧率。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例。该值不可以为空，否则将返回错误码401。 |
| currentFrameRate | 当前帧率。取值范围为[1, 144]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_ConfigInfo\_SetCurrentPictureQualityLevel()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetCurrentPictureQualityLevel (GamePerformance_ConfigInfo *configInfo, const GamePerformance_PictureQualityLevel currentPictureQualityLevel)
```

**描述**

为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置当前画质等级。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例。该值不可以为空，否则将返回错误码401。 |
| currentPictureQualityLevel | 当前画质等级[GamePerformance\_PictureQualityLevel](gameservice-game-performance.md#gameperformance_picturequalitylevel-1)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_ConfigInfo\_SetCurrentResolution()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetCurrentResolution (GamePerformance_ConfigInfo *configInfo, const char *currentResolution)
```

**描述**

为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置当前分辨率。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例。该值不可以为空，否则将返回错误码401。 |
| currentResolution | 当前分辨率。格式AxB（如1260x1980），字符长度范围：[1, 32]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_ConfigInfo\_SetHdModeEnabled()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetHdModeEnabled (GamePerformance_ConfigInfo *configInfo, const bool hdModeEnabled)
```

**描述**

为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置开启高清模式。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例。该值不可以为空，否则将返回错误码401。 |
| hdModeEnabled | 是否开启高清模式。  - true：开启  - false：不开启  默认为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_ConfigInfo\_SetMaxFrameRate()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetMaxFrameRate (GamePerformance_ConfigInfo *configInfo, const int64_t maxFrameRate)
```

**描述**

为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置最大帧率。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例。该值不可以为空，否则将返回错误码401。 |
| maxFrameRate | 最大帧率。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_ConfigInfo\_SetMaxPictureQualityLevel()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetMaxPictureQualityLevel (GamePerformance_ConfigInfo *configInfo, const GamePerformance_PictureQualityLevel maxPictureQualityLevel)
```

**描述**

为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置最大画质等级。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例。该值不可以为空，否则将返回错误码401。 |
| maxPictureQualityLevel | 支持的画质最高等级[GamePerformance\_PictureQualityLevel](gameservice-game-performance.md#gameperformance_picturequalitylevel-1)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_ConfigInfo\_SetMaxResolution()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetMaxResolution (GamePerformance_ConfigInfo *configInfo, const char *maxResolution)
```

**描述**

为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置最大分辨率。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例。该值不可以为空，否则将返回错误码401。 |
| maxResolution | 最大分辨率。格式AxB（如1260x1980），字符长度范围：[1, 32]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_ConfigInfo\_SetMultithreadingEnabled()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetMultithreadingEnabled (GamePerformance_ConfigInfo *configInfo, const bool multithreadingEnabled)
```

**描述**

为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置开启多线程。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例。该值不可以为空，否则将返回错误码401。 |
| multithreadingEnabled | 是否开启多线程。  - true：开启  - false：不开启  默认为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_ConfigInfo\_SetParticleEnabled()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetParticleEnabled (GamePerformance_ConfigInfo *configInfo, const bool particleEnabled)
```

**描述**

为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置粒子效果。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例。该值不可以为空，否则将返回错误码401。 |
| particleEnabled | 是否开启粒子效果。  - true：开启  - false：不开启  默认为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_ConfigInfo\_SetShadowEnabled()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetShadowEnabled (GamePerformance_ConfigInfo *configInfo, const bool shadowEnabled)
```

**描述**

为[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例设置是否开启阴影。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例。该值不可以为空，否则将返回错误码401。 |
| shadowEnabled | 是否开启阴影。  - true：开启  - false：不开启  默认为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_CpuInfo\_GetCpuLoadLevel()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_CpuInfo_GetCpuLoadLevel (GamePerformance_CpuInfo *cpuInfo, int32_t *cpuLoadLevel)
```

**描述**

从[GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo)中获取CPU负载整体等级。

**起始版本：** 6.0.2(22)

**参数:**

| 名称 | 描述 |
| --- | --- |
| cpuInfo | 指向[GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo)实例的指针。该值不可以为空，否则将返回错误码1010300004。 |
| cpuLoadLevel | CPU负载整体等级，取值范围为[1, 10]区间的整数。值越大表示负载越高。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_ERROR：参数错误。参数不能为空指针。 |

### HMS\_GamePerformance\_CpuInfo\_GetSingleThreadLoadLevel()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_CpuInfo_GetSingleThreadLoadLevel (GamePerformance_CpuInfo *cpuInfo, int32_t *singleThreadLoadLevel)
```

**描述**

从[GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo)中获取游戏最重线程的负载整体等级。

**起始版本：** 6.0.2(22)

**参数:**

| 名称 | 描述 |
| --- | --- |
| cpuInfo | 指针指向[GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo)实例。该值不可以为空，否则将返回错误码1010300004。 |
| singleThreadLoadLevel | 游戏最重线程的负载整体等级，取值范围为[1, 10]区间的整数。值越大表示负载越高。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_ERROR：参数错误。参数不能为空指针。 |

### HMS\_GamePerformance\_CreateConfigInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_CreateConfigInfo (GamePerformance_ConfigInfo **configInfo)
```

**描述**

创建[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例，该实例在[HMS\_GamePerformance\_UpdateConfigInfo](gameservice-game-performance.md#hms_gameperformance_updateconfiginfo)方法中使用。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 二级指针指向[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。 |

### HMS\_GamePerformance\_CreateInitParameters()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_CreateInitParameters (GamePerformance_InitParameters **initParameters)
```

**描述**

创建[GamePerformance\_InitParameters](gameservice-game-performance.md#gameperformance_initparameters)实例，该实例在[HMS\_GamePerformance\_Init](gameservice-game-performance.md#hms_gameperformance_init)方法中使用。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| initParameters | 二级指针指向[GamePerformance\_InitParameters](gameservice-game-performance.md#gameperformance_initparameters)初始化参数实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。 |

### HMS\_GamePerformance\_CreateNetInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_CreateNetInfo (GamePerformance_NetInfo **netInfo)
```

**描述**

创建[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例，该实例在[HMS\_GamePerformance\_UpdateNetInfo](gameservice-game-performance.md#hms_gameperformance_updatenetinfo)方法中使用。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| netInfo | 二级指针指向[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。 |

### HMS\_GamePerformance\_CreatePackageInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_CreatePackageInfo (GamePerformance_PackageInfo **packageInfo)
```

**描述**

创建[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例，该实例在[HMS\_GamePerformance\_UpdatePackageInfo](gameservice-game-performance.md#hms_gameperformance_updatepackageinfo)方法中使用。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| packageInfo | 二级指针指向[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。 |

### HMS\_GamePerformance\_CreatePlayerInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_CreatePlayerInfo (GamePerformance_PlayerInfo **playerInfo)
```

**描述**

创建[GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo)实例，该实例在[HMS\_GamePerformance\_UpdatePlayerInfo](gameservice-game-performance.md#hms_gameperformance_updateplayerinfo)方法中使用。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| playerInfo | 二级指针指向[GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。 |

### HMS\_GamePerformance\_CreateSceneInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_CreateSceneInfo (GamePerformance_SceneInfo **sceneInfo)
```

**描述**

创建[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例，该实例在[HMS\_GamePerformance\_UpdateSceneInfo](gameservice-game-performance.md#hms_gameperformance_updatesceneinfo)方法中使用。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 二级指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。 |

### HMS\_GamePerformance\_CreateThermalInfoQueryParameters()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_CreateThermalInfoQueryParameters (GamePerformance_ThermalInfoQueryParameters **parameters)
```

**描述**

创建[GamePerformance\_ThermalInfoQueryParameters](gameservice-game-performance.md#gameperformance_thermalinfoqueryparameters)实例，该实例在[HMS\_GamePerformance\_QueryThermalInfo](gameservice-game-performance.md#hms_gameperformance_querythermalinfo)方法中使用。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| parameters | 二级指针指向[GamePerformance\_ThermalInfoQueryParameters](gameservice-game-performance.md#gameperformance_thermalinfoqueryparameters)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。 |

### HMS\_GamePerformance\_DestroyConfigInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_DestroyConfigInfo (GamePerformance_ConfigInfo **configInfo)
```

**描述**

当[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例不再使用，销毁该实例。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 二级指针指向[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_DestroyCpuInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_DestroyCpuInfo (GamePerformance_CpuInfo **cpuInfo)
```

**描述**

当[GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo)实例不再使用，销毁该实例。

**起始版本：** 6.0.2(22)

**参数:**

| 名称 | 描述 |
| --- | --- |
| cpuInfo | 二级指针指向[GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo)实例。该值不可以为空，否则将返回错误码1010300004。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_ERROR：参数错误。参数不能为空指针。 |

### HMS\_GamePerformance\_DestroyDeviceInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_DestroyDeviceInfo (GamePerformance_DeviceInfo **deviceInfo)
```

**描述**

当[GamePerformance\_DeviceInfo](gameservice-game-performance.md#gameperformance_deviceinfo)实例不再使用，销毁该实例。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 二级指针指向[GamePerformance\_DeviceInfo](gameservice-game-performance.md#gameperformance_deviceinfo)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_DestroyGpuInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_DestroyGpuInfo (GamePerformance_GpuInfo **gpuInfo)
```

**描述**

当[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)实例不再使用，销毁该实例。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| gpuInfo | 二级指针指向[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_DestroyInitParameters()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_DestroyInitParameters (GamePerformance_InitParameters **initParameters)
```

**描述**

当[GamePerformance\_InitParameters](gameservice-game-performance.md#gameperformance_initparameters)实例不再使用，销毁该实例。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| initParameters | 二级指针指向[GamePerformance\_InitParameters](gameservice-game-performance.md#gameperformance_initparameters)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_DestroyNetInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_DestroyNetInfo (GamePerformance_NetInfo **netInfo)
```

**描述**

当[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例不再使用，销毁该实例。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| netInfo | 二级指针指向[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_DestroyPackageInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_DestroyPackageInfo (GamePerformance_PackageInfo **packageInfo)
```

**描述**

当[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例不再使用，销毁该实例。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| packageInfo | 二级指针指向[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_DestroyPlayerInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_DestroyPlayerInfo (GamePerformance_PlayerInfo **playerInfo)
```

**描述**

当[GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo)实例不再使用，销毁该实例。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| playerInfo | 二级指针指向[GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_DestroySceneInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_DestroySceneInfo (GamePerformance_SceneInfo **sceneInfo)
```

**描述**

当[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例不再使用，销毁该实例。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 二级指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_DestroyThermalInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_DestroyThermalInfo (GamePerformance_ThermalInfo **thermalInfo)
```

**描述**

当[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)实例不再使用，销毁该实例。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| thermalInfo | 二级指针指向[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_DestroyThermalInfoQueryParameters()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_DestroyThermalInfoQueryParameters (GamePerformance_ThermalInfoQueryParameters **parameters)
```

**描述**

当[GamePerformance\_ThermalInfoQueryParameters](gameservice-game-performance.md#gameperformance_thermalinfoqueryparameters)实例不再使用，销毁该实例。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| parameters | 二级指针指向[GamePerformance\_ThermalInfoQueryParameters](gameservice-game-performance.md#gameperformance_thermalinfoqueryparameters)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_DeviceInfo\_GetCpuInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_DeviceInfo_GetCpuInfo (GamePerformance_DeviceInfo *deviceInfo, GamePerformance_CpuInfo **cpuInfo)
```

**描述**

从设备性能信息[GamePerformance\_DeviceInfo](gameservice-game-performance.md#gameperformance_deviceinfo)中获取CPU性能信息[GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo)。当[GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo)实例不再使用，必须调用[HMS\_GamePerformance\_DestroyCpuInfo](gameservice-game-performance.md#hms_gameperformance_destroycpuinfo)销毁该实例。

**起始版本：** 6.0.2(22)

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 指针指向[GamePerformance\_DeviceInfo](gameservice-game-performance.md#gameperformance_deviceinfo)实例。该值不可以为空，否则将返回错误码1010300004。 |
| cpuInfo | 二级指针指向[GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_ERROR：参数错误。参数不能为空指针。 |

### HMS\_GamePerformance\_DeviceInfo\_GetGpuInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_DeviceInfo_GetGpuInfo (GamePerformance_DeviceInfo *deviceInfo, GamePerformance_GpuInfo **gpuInfo)
```

**描述**

从设备性能信息[GamePerformance\_DeviceInfo](gameservice-game-performance.md#gameperformance_deviceinfo)中获取GPU性能信息[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)。当[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)实例不再使用，必须调用[HMS\_GamePerformance\_DestroyGpuInfo](gameservice-game-performance.md#hms_gameperformance_destroygpuinfo)销毁该实例。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 指针指向[GamePerformance\_DeviceInfo](gameservice-game-performance.md#gameperformance_deviceinfo)实例。该值不可以为空，否则将返回错误码401。 |
| gpuInfo | 二级指针指向[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_DeviceInfo\_GetThermalInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_DeviceInfo_GetThermalInfo (GamePerformance_DeviceInfo *deviceInfo, GamePerformance_ThermalInfo **thermalInfo)
```

**描述**

从设备性能信息[GamePerformance\_DeviceInfo](gameservice-game-performance.md#gameperformance_deviceinfo)中获取温度信息[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)。当[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)实例不再使用，必须调用[HMS\_GamePerformance\_DestroyThermalInfo](gameservice-game-performance.md#hms_gameperformance_destroythermalinfo)销毁该实例。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 指针指向[GamePerformance\_DeviceInfo](gameservice-game-performance.md#gameperformance_deviceinfo)实例。该值不可以为空，否则将返回错误码401。 |
| thermalInfo | 二级指针指向[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_GpuInfo\_GetBandwidthLoadLevel()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetBandwidthLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *bandwidthLoadLevel)
```

**描述**

从[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)中获取GPU带宽负载等级。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| gpuInfo | 指针指向[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)实例。该值不可以为空，否则将返回错误码401。 |
| bandwidthLoadLevel | GPU带宽负载等级，取值范围为[1, 10]区间的整数。值越大表示负载越高。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_GpuInfo\_GetCurrentFrequency()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetCurrentFrequency (GamePerformance_GpuInfo *gpuInfo, int32_t *currentFrequency)
```

**描述**

从[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)中获取GPU频点信息。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| gpuInfo | 指针指向[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)实例。该值不可以为空，否则将返回错误码401。 |
| currentFrequency | GPU频点信息，单位：KHz。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_GpuInfo\_GetFragmentLoadLevel()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetFragmentLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *fragmentLoadLevel)
```

**描述**

从[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)中获取GPU片元处理负载等级。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| gpuInfo | 指针指向[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)实例。该值不可以为空，否则将返回错误码401。 |
| fragmentLoadLevel | GPU片元处理负载等级，取值范围为[1, 10]区间的整数。值越大表示负载越高。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_GpuInfo\_GetGpuLoadLevel()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetGpuLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *gpuLoadLevel)
```

**描述**

从[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)中获取GPU负载信息。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| gpuInfo | 指针指向[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)实例。该值不可以为空，否则将返回错误码401。 |
| gpuLoadLevel | GPU负载信息，取值范围为[1, 10]区间的整数。值越大表示负载越高。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_GpuInfo\_GetTextureLoadLevel()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetTextureLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *textureLoadLevel)
```

**描述**

从[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)中获取GPU纹理处理负载等级。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| gpuInfo | 指针指向[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)实例。该值不可以为空，否则将返回错误码401。 |
| textureLoadLevel | GPU纹理处理负载等级，取值范围为[1, 10]区间的整数。值越高表示负载越高。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_GpuInfo\_GetVertexLoadLevel()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetVertexLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *vertexLoadLevel)
```

**描述**

从[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)中获取GPU顶点处理负载等级。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| gpuInfo | 指针指向[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)实例。该值不可以为空，否则将返回错误码401。 |
| vertexLoadLevel | GPU顶点处理负载等级，取值范围为[1, 10]区间的整数。值越大表示负载越高。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_Init()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_Init (GamePerformance_InitParameters *initParameters)
```

**描述**

初始化游戏场景感知。

说明

调用HMS\_GamePerformance\_Init前，必须已调用[HMS\_GamePerformance\_InitParameters\_SetBundleName](gameservice-game-performance.md#hms_gameperformance_initparameters_setbundlename)接口和[HMS\_GamePerformance\_InitParameters\_SetAppVersion](gameservice-game-performance.md#hms_gameperformance_initparameters_setappversion)接口，分别设置bundleName和appVersion。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| initParameters | 指针指向[GamePerformance\_InitParameters](gameservice-game-performance.md#gameperformance_initparameters)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。  GAME\_PERFORMANCE\_INTERNAL\_ERROR：系统内部错误。  GAME\_PERFORMANCE\_AUTH\_FAILED：认证失败。 |

### HMS\_GamePerformance\_InitParameters\_SetAppVersion()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_InitParameters_SetAppVersion (GamePerformance_InitParameters *initParameters,const char *appVersion)
```

**描述**

为[GamePerformance\_InitParameters](gameservice-game-performance.md#gameperformance_initparameters)实例设置版本号。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| initParameters | 指针指向[GamePerformance\_InitParameters](gameservice-game-performance.md#gameperformance_initparameters)实例。该值不可以为空，否则将返回错误码401。 |
| appVersion | 游戏版本号。字符长度范围：[1, 64]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_InitParameters\_SetBundleName()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_InitParameters_SetBundleName (GamePerformance_InitParameters *initParameters, const char *bundleName)
```

**描述**

为[GamePerformance\_InitParameters](gameservice-game-performance.md#gameperformance_initparameters)实例设置包名。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| initParameters | 指针指向[GamePerformance\_InitParameters](gameservice-game-performance.md#gameperformance_initparameters)实例。该值不可以为空，否则将返回错误码401。 |
| bundleName | 游戏包名。字符长度范围：[1, 128]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_NetInfo\_SetDownlinkLatency()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetDownlinkLatency (GamePerformance_NetInfo *netInfo, const int64_t down)
```

**描述**

为[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例设置下行网络时延。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| netInfo | 指针指向[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例。该值不可以为空，否则将返回错误码401。 |
| down | 下行网络时延，单位：毫秒（ms）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_NetInfo\_SetNetLoad()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetNetLoad (GamePerformance_NetInfo *netInfo, const GamePerformance_NetLoad netLoad)
```

**描述**

为[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例设置网络负载。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| netInfo | 指针指向[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例。该值不可以为空，否则将返回错误码401。 |
| netLoad | 网络负载[GamePerformance\_NetLoad](gameservice-game-performance.md#gameperformance_netload)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_NetInfo\_SetServerLatency()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetServerLatency (GamePerformance_NetInfo *netInfo, const int64_t server)
```

**描述**

为[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例设置服务器网络时延。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| netInfo | 指针指向[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例。该值不可以为空，否则将返回错误码401。 |
| server | 服务器网络时延，单位：毫秒（ms）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_NetInfo\_SetTotalLatency()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetTotalLatency (GamePerformance_NetInfo *netInfo, const int64_t total)
```

**描述**

为[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例设置总网络时延。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| netInfo | 指针指向[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例。该值不可以为空，否则将返回错误码401。 |
| total | 总网络时延，单位：毫秒（ms）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_NetInfo\_SetUplinkLatency()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetUplinkLatency (GamePerformance_NetInfo *netInfo, const int64_t up)
```

**描述**

为[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例设置上行网络时延。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| netInfo | 指针指向[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例。该值不可以为空，否则将返回错误码401。 |
| up | 上行网络时延，单位：毫秒（ms）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_PackageInfo\_SetAppVersion()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetAppVersion (GamePerformance_PackageInfo *packageInfo, const char *appVersion)
```

**描述**

为[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例设置游戏版本号。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| packageInfo | 指针指向[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例。该值不可以为空，否则将返回错误码401。 |
| appVersion | 游戏版本号。字符长度范围：[1, 64]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_PackageInfo\_SetBundleName()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetBundleName (GamePerformance_PackageInfo *packageInfo, const char *bundleName)
```

**描述**

为[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例设置包名。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| packageInfo | 指针指向[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例。该值不可以为空，否则将返回错误码401。 |
| bundleName | 游戏包名。字符长度范围：[1, 128]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_PackageInfo\_SetEngineType()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetEngineType (GamePerformance_PackageInfo *packageInfo, const GamePerformance_EngineType engineType)
```

**描述**

为[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例设置引擎类型。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| packageInfo | 指针指向[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例。该值不可以为空，否则将返回错误码401。 |
| engineType | 引擎类型[GamePerformance\_EngineType](gameservice-game-performance.md#gameperformance_enginetype)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_PackageInfo\_SetEngineVersion()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetEngineVersion (GamePerformance_PackageInfo *packageInfo, const char *engineVersion)
```

**描述**

为[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例设置引擎版本号。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| packageInfo | 指针指向[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例。该值不可以为空，否则将返回错误码401。 |
| engineVersion | 游戏引擎版本号。字符长度范围：[0, 64]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_PackageInfo\_SetGameType()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetGameType (GamePerformance_PackageInfo *packageInfo, const GamePerformance_GameType gameType)
```

**描述**

为[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例设置游戏类型。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| packageInfo | 指针指向[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例。该值不可以为空，否则将返回错误码401。 |
| gameType | 游戏类型[GamePerformance\_GameType](gameservice-game-performance.md#gameperformance_gametype)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_PackageInfo\_SetVulkanSupported()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetVulkanSupported (GamePerformance_PackageInfo *packageInfo, const bool vulkanSupported)
```

**描述**

为[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例设置是否支持vulkan。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| packageInfo | 指针指向[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例。该值不可以为空，否则将返回错误码401。 |
| vulkanSupported | 是否支持vulkan。  - true：支持  - false：不支持  默认为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_PlayerInfo\_SetGamePlayerId()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_PlayerInfo_SetGamePlayerId (GamePerformance_PlayerInfo *playerInfo, const char *gamePlayerId)
```

**描述**

为[GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo)实例设置游戏玩家ID。

说明

调用[HMS\_GamePerformance\_PlayerInfo\_SetGamePlayerId](gameservice-game-performance.md#hms_gameperformance_playerinfo_setgameplayerid)设置的gamePlayerId、[HMS\_GamePerformance\_PlayerInfo\_SetTeamPlayerId](gameservice-game-performance.md#hms_gameperformance_playerinfo_setteamplayerid)设置的teamPlayerId和[HMS\_GamePerformance\_PlayerInfo\_SetThirdOpenId](gameservice-game-performance.md#hms_gameperformance_playerinfo_setthirdopenid)设置的thirdOpenId不能同时为空。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| playerInfo | 指针指向[GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo)实例。该值不可以为空，否则将返回错误码401。 |
| gamePlayerId | 游戏玩家ID。字符长度范围：[0, 256]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_PlayerInfo\_SetTeamPlayerId()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_PlayerInfo_SetTeamPlayerId (GamePerformance_PlayerInfo *playerInfo, const char *teamPlayerId)
```

**描述**

为[GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo)实例设置团队玩家ID。

说明

调用[HMS\_GamePerformance\_PlayerInfo\_SetGamePlayerId](gameservice-game-performance.md#hms_gameperformance_playerinfo_setgameplayerid)设置的gamePlayerId、[HMS\_GamePerformance\_PlayerInfo\_SetTeamPlayerId](gameservice-game-performance.md#hms_gameperformance_playerinfo_setteamplayerid)设置的teamPlayerId和[HMS\_GamePerformance\_PlayerInfo\_SetThirdOpenId](gameservice-game-performance.md#hms_gameperformance_playerinfo_setthirdopenid)设置的thirdOpenId不能同时为空。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| playerInfo | 指针指向[GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo)实例。该值不可以为空，否则将返回错误码401。 |
| teamPlayerId | 团队玩家ID。字符长度范围：[0, 256]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_PlayerInfo\_SetThirdOpenId()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_PlayerInfo_SetThirdOpenId (GamePerformance_PlayerInfo *playerInfo, const char *thirdOpenId)
```

**描述**

为[GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo)实例设置游戏官方账号。

说明

调用[HMS\_GamePerformance\_PlayerInfo\_SetGamePlayerId](gameservice-game-performance.md#hms_gameperformance_playerinfo_setgameplayerid)设置的gamePlayerId、[HMS\_GamePerformance\_PlayerInfo\_SetTeamPlayerId](gameservice-game-performance.md#hms_gameperformance_playerinfo_setteamplayerid)设置的teamPlayerId和[HMS\_GamePerformance\_PlayerInfo\_SetThirdOpenId](gameservice-game-performance.md#hms_gameperformance_playerinfo_setthirdopenid)设置的thirdOpenId不能同时为空。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| playerInfo | 指针指向[GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo)实例。该值不可以为空，否则将返回错误码401。 |
| thirdOpenId | 游戏官方账号。字符长度范围：[0, 128]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_QueryCpuInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_QueryCpuInfo (GamePerformance_CpuInfo **cpuInfo)
```

**描述**

查询CPU性能信息。当[GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo)实例不再使用，必须调用[HMS\_GamePerformance\_DestroyCpuInfo](gameservice-game-performance.md#hms_gameperformance_destroycpuinfo)销毁该实例。

**起始版本：** 6.0.2(22)

**参数:**

| 名称 | 描述 |
| --- | --- |
| cpuInfo | 二级指针指向[GamePerformance\_CpuInfo](gameservice-game-performance.md#gameperformance_cpuinfo)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_INTERNAL\_ERROR：系统内部错误。请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101704354579010004&keyWord=Game Service Kit)系统提交此问题。  GAME\_PERFORMANCE\_INVALID\_REQUEST：无效请求。请先调用[HMS\_GamePerformance\_Init](gameservice-game-performance.md#hms_gameperformance_init)接口。  GAME\_PERFORMANCE\_PARAM\_ERROR：参数错误。参数不能为空指针。 |

### HMS\_GamePerformance\_QueryGpuInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_QueryGpuInfo (GamePerformance_GpuInfo **gpuInfo)
```

**描述**

查询GPU性能信息。当[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)实例不再使用，必须调用[HMS\_GamePerformance\_DestroyGpuInfo](gameservice-game-performance.md#hms_gameperformance_destroygpuinfo)销毁该实例。

说明

Mali系列GPU不支持采集GPU性能信息，无法获取设备GPU性能信息。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| gpuInfo | 二级指针指向[GamePerformance\_GpuInfo](gameservice-game-performance.md#gameperformance_gpuinfo)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。  GAME\_PERFORMANCE\_INTERNAL\_ERROR：系统内部错误。  GAME\_PERFORMANCE\_INVALID\_REQUEST：无效请求。 |

### HMS\_GamePerformance\_QueryThermalInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_QueryThermalInfo (GamePerformance_ThermalInfoQueryParameters *parameters, GamePerformance_ThermalInfo **thermalInfo)
```

**描述**

查询温度信息。当[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)实例不再使用，必须调用[HMS\_GamePerformance\_DestroyThermalInfo](gameservice-game-performance.md#hms_gameperformance_destroythermalinfo)销毁该实例。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| parameters | 指针指向[GamePerformance\_ThermalInfoQueryParameters](gameservice-game-performance.md#gameperformance_thermalinfoqueryparameters)实例。该值不可以为空，否则将返回错误码401。 |
| thermalInfo | 二级指针指向[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。  GAME\_PERFORMANCE\_INTERNAL\_ERROR：系统内部错误。  GAME\_PERFORMANCE\_INVALID\_REQUEST：无效请求。 |

### HMS\_GamePerformance\_RegisterThermalLevelChangedCallback()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_RegisterThermalLevelChangedCallback (GamePerformance_DeviceInfoType *types[], size_t size, GamePerformance_ThermalLevelChangedCallback callback, void *userData)
```

**描述**

订阅温度变化事件，注册温度变化回调，当达到触发点时，将调用回调函数。

当温度等级改变并且温度等级小于3档时，该函数将被调用一次。当温度等级大于或等于3档时，该函数将每10秒调用一次。

说明

Mali系列GPU不支持采集GPU性能信息，无法获取设备GPU性能信息。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| types[] | 注册回调的设备性能信息类型[GamePerformance\_DeviceInfoType](gameservice-game-performance.md#gameperformance_deviceinfotype-1)。 |
| size | types数组的长度。 |
| callback | 回调函数[GamePerformance\_ThermalLevelChangedCallback](gameservice-game-performance.md#gameperformance_thermallevelchangedcallback)。 |
| userData | 用户指定数据。用户自定义任意类型，callback透传返回。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。  GAME\_PERFORMANCE\_INTERNAL\_ERROR：系统内部错误。  GAME\_PERFORMANCE\_INVALID\_REQUEST：无效请求。 |

### HMS\_GamePerformance\_SceneInfo\_SetChannelCount()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetChannelCount (GamePerformance_SceneInfo *sceneInfo, const int64_t channelCount)
```

**描述**

为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置每帧渲染的通道数。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |
| channelCount | 每帧渲染的通道数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_SceneInfo\_SetCurrentFrameRate()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetCurrentFrameRate (GamePerformance_SceneInfo *sceneInfo, const int64_t currentFrameRate)
```

**描述**

为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置场景当前帧率。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |
| currentFrameRate | 场景当前帧率。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_SceneInfo\_SetDescription()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetDescription (GamePerformance_SceneInfo *sceneInfo, const char *description)
```

**描述**

为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置场景描述。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |
| description | 游戏场景描述（自定义描述）。字符长度范围：[0, 128]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_SceneInfo\_SetDrawCallCount()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetDrawCallCount (GamePerformance_SceneInfo *sceneInfo, const int64_t drawCallCount)
```

**描述**

为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置每帧的平均Drawcall数。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |
| drawCallCount | 每帧的平均Drawcall数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_SceneInfo\_SetImportanceLevel()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetImportanceLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_SceneImportanceLevel importanceLevel)
```

**描述**

为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置场景重要程度。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |
| importanceLevel | 场景重要程度[GamePerformance\_SceneImportanceLevel](gameservice-game-performance.md#gameperformance_sceneimportancelevel)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_SceneInfo\_SetKeyThread()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetKeyThread (GamePerformance_SceneInfo *sceneInfo, const char *keyThread)
```

**描述**

为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置关键线程。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |
| keyThread | 该场景下的关键线程。  - render：渲染线程  - logic：逻辑线程  - net：网络线程  按照 render|xxx|logic|xxx 格式传入。字符长度范围：[0, 32]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_SceneInfo\_SetMaxFrameRate()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetMaxFrameRate (GamePerformance_SceneInfo *sceneInfo, const int64_t maxFrameRate)
```

**描述**

为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置场景最大帧率。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |
| maxFrameRate | 场景最大帧率。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_SceneInfo\_SetMeshCount()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetMeshCount (GamePerformance_SceneInfo *sceneInfo, const int64_t meshCount)
```

**描述**

为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置每帧的平均mesh数量。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |
| meshCount | 每帧的平均mesh数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_SceneInfo\_SetParticipantCount()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetParticipantCount (GamePerformance_SceneInfo *sceneInfo, const int64_t participantCount)
```

**描述**

为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置场景下的同屏人数。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |
| participantCount | 场景下的同屏人数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_SceneInfo\_SetRecommendedCpuLevel()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetRecommendedCpuLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_CpuLevel recommendedCpuLevel)
```

**描述**

为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置推荐的CPU等级。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |
| recommendedCpuLevel | 推荐的CPU等级[GamePerformance\_CpuLevel](gameservice-game-performance.md#gameperformance_cpulevel)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_SceneInfo\_SetRecommendedDdrLevel()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetRecommendedDdrLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_DdrLevel recommendedDdrLevel)
```

**描述**

为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置推荐的DDR等级。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |
| recommendedDdrLevel | 推荐的DDR等级[GamePerformance\_DdrLevel](gameservice-game-performance.md#gameperformance_ddrlevel)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_SceneInfo\_SetRecommendedGpuLevel()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetRecommendedGpuLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_GpuLevel recommendedGpuLevel)
```

**描述**

为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置推荐的GPU等级。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |
| recommendedGpuLevel | 推荐的GPU等级[GamePerformance\_GpuLevel](gameservice-game-performance.md#gameperformance_gpulevel)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_SceneInfo\_SetSceneFrequency()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSceneFrequency (GamePerformance_SceneInfo *sceneInfo, const int64_t sceneFrequency)
```

**描述**

为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置该场景在一局游戏中出现的次数。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |
| sceneFrequency | 该场景在一局游戏中出现的次数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_SceneInfo\_SetSceneID()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSceneID (GamePerformance_SceneInfo *sceneInfo, const int64_t sceneID)
```

**描述**

为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置场景ID。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |
| sceneID | 场景ID。  0：回切场景标识结束  1：游戏启动  2：游戏内更新  3：登录过程  4：主界面  5：加载一局游戏（自己加载）  6：加载一局游戏（自己加载完毕，等待其他玩家）  7：游戏中  8：观战模式 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_SceneInfo\_SetSceneTime()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSceneTime (GamePerformance_SceneInfo *sceneInfo, const int64_t sceneTime)
```

**描述**

为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置场景持续时间。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |
| sceneTime | 场景持续时间，单位：毫秒（ms）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_SceneInfo\_SetShaderCount()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetShaderCount (GamePerformance_SceneInfo *sceneInfo, const int64_t shaderCount)
```

**描述**

为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置每帧的平均shader数量。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |
| shaderCount | 每帧的平均shader数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_SceneInfo\_SetSubDescription()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSubDescription (GamePerformance_SceneInfo *sceneInfo, const char *subDescription)
```

**描述**

为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置子场景描述。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |
| subDescription | 游戏子场景描述（自定义描述）。字符长度范围：[0, 128]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_SceneInfo\_SetSubSceneID()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSubSceneID (GamePerformance_SceneInfo *sceneInfo, const char *subSceneID)
```

**描述**

为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置子场景ID。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |
| subSceneID | 游戏子场景ID。字符长度范围：[0, 128]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_SceneInfo\_SetTextureCount()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetTextureCount (GamePerformance_SceneInfo *sceneInfo, const int64_t textureCount)
```

**描述**

为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置每帧的平均纹理数量。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |
| textureCount | 每帧的平均纹理数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_SceneInfo\_SetTriangleCount()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetTriangleCount (GamePerformance_SceneInfo *sceneInfo, const int64_t triangleCount)
```

**描述**

为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置每帧的平均模型三角形数。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |
| triangleCount | 每帧的平均模型三角形数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_SceneInfo\_SetVertexCount()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetVertexCount (GamePerformance_SceneInfo *sceneInfo, const int64_t vertexCount)
```

**描述**

为[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例设置每帧的平均模型顶点数。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |
| vertexCount | 每帧的平均模型顶点数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_ThermalInfo\_GetNowNormalizedCurrent()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetNowNormalizedCurrent (GamePerformance_ThermalInfo *thermalInfo, int32_t *nowCurrent)
```

**描述**

从[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)中获取当前的工作电流。

**起始版本：** 6.0.2(22)

**设备行为差异：** 该接口在Phone中可正常调用，在其他设备类型中无返回值。

**参数:**

| 名称 | 描述 |
| --- | --- |
| thermalInfo | 指针指向[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)实例。该值不可以为空，否则将返回错误码1010300004。 |
| nowCurrent | 当前的工作电流，单位：mA。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_ERROR：参数错误。参数不能为空指针。 |

### HMS\_GamePerformance\_ThermalInfo\_GetRecommendMaxNormalizedCurrent()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetRecommendMaxNormalizedCurrent (GamePerformance_ThermalInfo *thermalInfo, int32_t *recommendMaxCurrent)
```

**描述**

从[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)中获取系统建议的最大工作电流。

**起始版本：** 6.0.2(22)

**设备行为差异：** 该接口在Phone中可正常调用，在其他设备类型中无返回值。

**参数:**

| 名称 | 描述 |
| --- | --- |
| thermalInfo | 指针指向[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)实例。该值不可以为空，否则将返回错误码1010300004。 |
| recommendMaxCurrent | 系统建议的最大工作电流，单位：mA。  若当前的工作电流高于此值，设备会立即发烫。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_ERROR：参数错误。参数不能为空指针。 |

### HMS\_GamePerformance\_ThermalInfo\_GetRecommendNormalizedCurrent()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetRecommendNormalizedCurrent (GamePerformance_ThermalInfo *thermalInfo, int32_t *recommendCurrent)
```

**描述**

从[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)中获取系统建议的工作电流。

**起始版本：** 6.0.2(22)

**设备行为差异：** 该接口在Phone中可正常调用，在其他设备类型中无返回值。

**参数:**

| 名称 | 描述 |
| --- | --- |
| thermalInfo | 指针指向[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)实例。该值不可以为空，否则将返回错误码1010300004。 |
| recommendCurrent | 系统建议的工作电流，单位：mA。  若当前的工作电流高于此值，温升趋势thermalTrend会大于0，设备有发烫风险。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_ERROR：参数错误。参数不能为空指针。 |

### HMS\_GamePerformance\_ThermalInfo\_GetThermalLevel()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetThermalLevel (GamePerformance_ThermalInfo *thermalInfo, int32_t *thermalLevel)
```

**描述**

从[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)中获取温度等级。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| thermalInfo | 指针指向[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)实例。该值不可以为空，否则将返回错误码401。 |
| thermalLevel | 温度等级，即温控档位，档位越高表示温度越高。不同档位及其建议如下：  1：无需处理。  2：建议降低无感知业务规格，例如后台更新降速或延迟运行。  3：建议暂停无感知业务，降低游戏非核心业务的规格，例如前台更新降速。  4：建议减少游戏特效，降低分辨率，画质。  5：建议降低全场景规格，进一步降低分辨率、画质等。  6：建议游戏降至最低规格。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_ThermalInfo\_GetThermalMargin()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetThermalMargin (GamePerformance_ThermalInfo *thermalInfo, int32_t *thermalMargin)
```

**描述**

从温度信息[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)中获取温度时间裕量。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| thermalInfo | 指针指向[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)实例。该值不可以为空，否则将返回错误码401。 |
| thermalMargin | 时间裕量，温控到达指定档位的时间，负值表示系统无法预测。单位：秒（s）。  **说明**：  - 该数值超过60时，可信度降低。  - 值为0：表示已达到查询的温控档位。  - 值为-1：表示不能到达。  - 值为-2：表示查询的档位低于当前档位。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_ThermalInfo\_GetThermalTrend()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetThermalTrend (GamePerformance_ThermalInfo *thermalInfo, int32_t *thermalTrend)
```

**描述**

从温度信息[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)中获取温升趋势。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| thermalInfo | 指针指向[GamePerformance\_ThermalInfo](gameservice-game-performance.md#gameperformance_thermalinfo)实例。该值不可以为空，否则将返回错误码401。 |
| thermalTrend | 温升趋势，取值范围为[-100, 100]，负号代表降温，数值越大说明当前温度变化越快。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_ThermalInfoQueryParameters\_SetNeedsPrediction()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfoQueryParameters_SetNeedsPrediction (GamePerformance_ThermalInfoQueryParameters *parameters, const bool needsPrediction)
```

**描述**

为[GamePerformance\_ThermalInfoQueryParameters](gameservice-game-performance.md#gameperformance_thermalinfoqueryparameters)实例设置是否需要预测温升趋势。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| parameters | 指针指向[GamePerformance\_ThermalInfoQueryParameters](gameservice-game-performance.md#gameperformance_thermalinfoqueryparameters)实例。该值不可以为空，否则将返回错误码401。 |
| needsPrediction | 是否需要预测温升趋势。如果需要预测温升趋势，将返回温度时间裕量和温升趋势。  - true：需要  - false：不需要  默认为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_ThermalInfoQueryParameters\_SetTargetThermalLevel()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfoQueryParameters_SetTargetThermalLevel (GamePerformance_ThermalInfoQueryParameters *parameters, const int32_t targetThermalLevel)
```

**描述**

为[GamePerformance\_ThermalInfoQueryParameters](gameservice-game-performance.md#gameperformance_thermalinfoqueryparameters)实例设置预测温升趋势的目标温度等级。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| parameters | 指针指向[GamePerformance\_ThermalInfoQueryParameters](gameservice-game-performance.md#gameperformance_thermalinfoqueryparameters)实例。该值不可以为空，否则将返回错误码401。 |
| targetThermalLevel | 预测温升趋势的目标温度等级。如果需要预测温升趋势，将根据该目标温度等级计算返回温度时间裕量和温度趋势。取值请参见[温度等级](gameservice-game-performance.md#hms_gameperformance_thermalinfo_getthermallevel)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。 |

### HMS\_GamePerformance\_UnregisterAllThermalLevelChangedCallbacks()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_UnregisterAllThermalLevelChangedCallbacks (void)
```

**描述**

取消注册所有温度变化回调。

**起始版本：** 5.0.2(14)

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_INTERNAL\_ERROR：系统内部错误。  GAME\_PERFORMANCE\_INVALID\_REQUEST：无效请求。 |

### HMS\_GamePerformance\_UnregisterThermalLevelChangedCallback()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_UnregisterThermalLevelChangedCallback (GamePerformance_ThermalLevelChangedCallback callback)
```

**描述**

取消注册指定温度变化回调。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| callback | 回调函数[GamePerformance\_ThermalLevelChangedCallback](gameservice-game-performance.md#gameperformance_thermallevelchangedcallback)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。  GAME\_PERFORMANCE\_INTERNAL\_ERROR：系统内部错误。  GAME\_PERFORMANCE\_INVALID\_REQUEST：无效请求。 |

### HMS\_GamePerformance\_UpdateConfigInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_UpdateConfigInfo (GamePerformance_ConfigInfo *configInfo)
```

**描述**

更新游戏配置信息。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向[GamePerformance\_ConfigInfo](gameservice-game-performance.md#gameperformance_configinfo)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。  GAME\_PERFORMANCE\_INTERNAL\_ERROR：系统内部错误。  GAME\_PERFORMANCE\_INVALID\_REQUEST：无效请求。 |

### HMS\_GamePerformance\_UpdateNetInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_UpdateNetInfo (GamePerformance_NetInfo *netInfo)
```

**描述**

更新游戏网络信息。

说明

调用HMS\_GamePerformance\_UpdateNetInfo前，必须已调用[HMS\_GamePerformance\_NetInfo\_SetTotalLatency](gameservice-game-performance.md#hms_gameperformance_netinfo_settotallatency)设置totalLatency。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| netInfo | 指针指向[GamePerformance\_NetInfo](gameservice-game-performance.md#gameperformance_netinfo)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。  GAME\_PERFORMANCE\_INTERNAL\_ERROR：系统内部错误。  GAME\_PERFORMANCE\_INVALID\_REQUEST：无效请求。 |

### HMS\_GamePerformance\_UpdatePackageInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_UpdatePackageInfo (GamePerformance_PackageInfo *packageInfo)
```

**描述**

更新游戏包信息。

说明

调用HMS\_GamePerformance\_UpdatePackageInfo前，必须已调用[HMS\_GamePerformance\_InitParameters\_SetBundleName](gameservice-game-performance.md#hms_gameperformance_initparameters_setbundlename)接口和[HMS\_GamePerformance\_InitParameters\_SetAppVersion](gameservice-game-performance.md#hms_gameperformance_initparameters_setappversion)接口，分别设置bundleName和appVersion。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| packageInfo | 指针指向[GamePerformance\_PackageInfo](gameservice-game-performance.md#gameperformance_packageinfo)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。  GAME\_PERFORMANCE\_INTERNAL\_ERROR：系统内部错误。  GAME\_PERFORMANCE\_INVALID\_REQUEST：无效请求。 |

### HMS\_GamePerformance\_UpdatePlayerInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_UpdatePlayerInfo (GamePerformance_PlayerInfo *playerInfo)
```

**描述**

更新游戏玩家信息。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| playerInfo | 指针指向[GamePerformance\_PlayerInfo](gameservice-game-performance.md#gameperformance_playerinfo)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。  GAME\_PERFORMANCE\_INTERNAL\_ERROR：系统内部错误。  GAME\_PERFORMANCE\_INVALID\_REQUEST：无效请求。 |

### HMS\_GamePerformance\_UpdateSceneInfo()

PhonePC/2in1Tablet

```
1. GamePerformance_ErrorCode HMS_GamePerformance_UpdateSceneInfo (GamePerformance_SceneInfo *sceneInfo)
```

**描述**

更新游戏场景信息。

说明

调用HMS\_GamePerformance\_UpdateSceneInfo前，必须已调用[HMS\_GamePerformance\_SceneInfo\_SetSceneID](gameservice-game-performance.md#hms_gameperformance_sceneinfo_setsceneid)接口和[HMS\_GamePerformance\_SceneInfo\_SetImportanceLevel](gameservice-game-performance.md#hms_gameperformance_sceneinfo_setimportancelevel)接口，分别设置sceneID和importanceLevel。

**起始版本：** 5.0.2(14)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向[GamePerformance\_SceneInfo](gameservice-game-performance.md#gameperformance_sceneinfo)实例。该值不可以为空，否则将返回错误码401。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GamePerformance\_ErrorCode](gameservice-game-performance.md#gameperformance_errorcode-1) | GAME\_PERFORMANCE\_SUCCESS：成功。  GAME\_PERFORMANCE\_PARAM\_INVALID：无效参数。  GAME\_PERFORMANCE\_INTERNAL\_ERROR：系统内部错误。  GAME\_PERFORMANCE\_INVALID\_REQUEST：无效请求。 |
