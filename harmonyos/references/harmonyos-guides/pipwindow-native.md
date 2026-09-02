---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pipwindow-native
title: 使用NDK接口实现画中画功能开发 (C/C++)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口类型 > 画中画开发指导 > 使用NDK接口实现画中画功能开发 (C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:22+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:355eed9e24324beb475d6436bfd278a0c1b7f8d7892f4c6bef9b1888f305f1f2
---

本文以视频播放为例，介绍通过NDK接口实现画中画功能的基本开发步骤。

**说明** 

* 从API version 20开始，支持使用NDK接口实现画中画功能开发。
* 支持在Phone、PC/2in1、Tablet设备使用NDK接口实现画中画功能开发。

## 约束与限制

* 画中画窗口中画面的呈现不通过传入XComponent Controller实现，而是通过渲染surfaceId（在开启画中画回调中获取）对应的组件实现。
* 与typeNode实现方式相同，系统不缓存页面。如需进行页面操作，应用需要开启画中画生命周期监听，在对应周期内进行对应操作。
* 不支持设置自动拉起画中画。

## 开发步骤

示例中的视频播放器简易实现逻辑如下：

1. 通过OH\_PictureInPicture\_CreatePipConfig创建画中画参数配置器，并通过OH\_PictureInPicture\_SetPipMainWindowId、OH\_PictureInPicture\_SetPipTemplateType、OH\_PictureInPicture\_SetPipRect、OH\_PictureInPicture\_SetPipControlGroup、OH\_PictureInPicture\_SetPipNapiEnv接口在画中画参数配置器中设置初始配置信息。
2. 创建画中画控制器，后续可根据返回的控制器标识controllerId注册生命周期事件以及控制事件回调。通过OH\_PictureInPicture\_CreatePip接口创建画中画控制器实例，并缓存对应的控制器标识。建议在创建完成后立即调用OH\_PictureInPicture\_DestroyPipConfig销毁画中画参数配置器，以免发生内存泄漏。
3. 通过OH\_PictureInPicture\_RegisterStartPipCallback接口注册启动画中画回调，并根据返回的surfaceId渲染视频画面。同时应用可以按需注册其他需要监听的事件回调。
4. 通过OH\_PictureInPicture\_StartPip启动画中画。
5. 通过OH\_PictureInPicture\_UpdatePipContentSize更新媒体源尺寸信息。
6. 通过OH\_PictureInPicture\_StopPip关闭画中画。
7. 通过OH\_PictureInPicture\_UnregisterStartPipCallback解注册画中画启动回调，避免内存泄漏。同时应用可以按需解注册其他已注册的事件回调。

以上步骤涉及的各文件及示例可见下文。

Node-API模块注册，具体使用请参考[Native API在应用工程中的使用指导](napi-guidelines.md)。

本文件仅作为参考示例，异常处理及错误码打印由开发者按需处理。

```
// napi_init.cpp
#include "napi/native_api.h"
#include <cstddef>
#include <cstdint>
#include <cstdio>
#include <string>
#include "window_manager/oh_window_pip.h"
#include "hilog/log.h"
#include "js_native_api.h"
#include "napi/native_api.h"
#include <cstdio>
#include "rawfile/raw_file_manager.h"

#define LOG_MSG_TAG "PiPMain"
#define LOG(format, ...) ((void)OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00, LOG_MSG_TAG, format, ##__VA_ARGS__))
napi_ref jsCallback;
napi_env env_;

napi_ref jsLifecycleCallback;
napi_env lifeEnv_;
int32_t g_minValue = 0;
int32_t g_maxValue = 255;

inline bool ConvertFromJsNumber(napi_env env, napi_value jsValue, int32_t& value)
{
    return napi_get_value_int32(env, jsValue, &value) == napi_ok;
}

inline bool ConvertFromJsNumber(napi_env env, napi_value jsValue, uint32_t& value)
{
    return napi_get_value_uint32(env, jsValue, &value) == napi_ok;
}

inline bool ConvertFromJsNumber(napi_env env, napi_value jsValue, int64_t& value)
{
    return napi_get_value_int64(env, jsValue, &value) == napi_ok;
}

inline bool ConvertFromJsNumber(napi_env env, napi_value jsValue, uint64_t& value)
{
    int64_t num;
    auto res = napi_get_value_int64(env, jsValue, &num);
    if (res == napi_ok) {
        value = static_cast<uint64_t>(num);
    }
    return res == napi_ok;
}

inline bool ConvertFromJsNumber(napi_env env, napi_value jsValue, double& value)
{
    return napi_get_value_double(env, jsValue, &value) == napi_ok;
}

inline bool ConvertFromJsNumber(napi_env env, napi_value jsValue, bool& value)
{
    return napi_get_value_bool(env, jsValue, &value) == napi_ok;
}

inline bool ConvertFromJsNumber(napi_env env, napi_value jsValue, unsigned char& value)
{
    int32_t num;
    if (napi_get_value_int32(env, jsValue, &num) != napi_ok) {
        return false;
    }
    if (num < g_minValue || num > g_maxValue) {
        return false; // 越界无效
    }
    value = static_cast<unsigned char>(num);
    return true;
}

template<class T>
bool ConvertFromJsValue(napi_env env, napi_value jsValue, T& value)
{
    if (jsValue == nullptr) {
        return false;
    }
    using ValueType = std::remove_cv_t<std::remove_reference_t<T>>;
    if constexpr (std::is_same_v<ValueType, bool>) {
        return napi_get_value_bool(env, jsValue, &value) == napi_ok;
    } else if constexpr (std::is_arithmetic_v<ValueType>) {
        return ConvertFromJsNumber(env, jsValue, value);
    } else if constexpr (std::is_same_v<ValueType, std::string>) {
        size_t len = 0;
        if (napi_get_value_string_utf8(env, jsValue, nullptr, 0, &len) != napi_ok) {
            return false;
        }
        auto buffer = std::make_unique<char[]>(len + 1);
        size_t strLength = 0;
        if (napi_get_value_string_utf8(env, jsValue, buffer.get(), len + 1, &strLength) == napi_ok) {
            value = buffer.get();
            return true;
        }
        return false;
    } else if constexpr (std::is_enum_v<ValueType>) {
        std::make_signed_t<ValueType> numberValue = 0;
        if (!ConvertFromJsNumber(env, jsValue, numberValue)) {
            return false;
        }
        value = static_cast<ValueType>(numberValue);
        return true;
    }
    return false;
}

void PipStartPipCallback(uint32_t controllerId, uint8_t requestId, uint64_t surfaceId)
{
    if (jsCallback) {
        napi_value global = nullptr;
        napi_get_global(env_, &global);
        size_t argc = 1;
        std::string tStr = std::to_string(surfaceId);
        const char* cStr = tStr.c_str();
        size_t length = strlen(cStr);
        napi_value str;
        napi_status status = napi_create_string_utf8(env_, cStr, length, &str);
        napi_value argv[1] = {str};
        napi_value jsCallbackValue;
        
        napi_value result = nullptr;
        if (!jsCallback) {
            LOG("js callback is invalid");
        }
        napi_get_reference_value(env_, jsCallback, &jsCallbackValue);
        napi_call_function(env_, global, jsCallbackValue, argc, argv, &result);
    }
}

void LifecycleCallback(uint32_t controllerId, PictureInPicture_PipState state, int32_t errcode)
{
    if (jsLifecycleCallback) {
        napi_value global = nullptr;
        napi_get_global(lifeEnv_, &global);
        size_t argc = 1;
        napi_value pipState = nullptr;
        napi_create_int32(lifeEnv_, static_cast<int32_t> (state), &pipState);
        napi_value argv[1] = {pipState};
        napi_value jsCallbackValue;
        
        napi_value result = nullptr;
        if (!jsCallback) {
            LOG("js callback is invalid");
        }
        napi_get_reference_value(lifeEnv_, jsLifecycleCallback, &jsCallbackValue);
        napi_call_function(lifeEnv_, global, jsCallbackValue, argc, argv, &result);
    }
}

class PiPManager {
public:
    static napi_value CreatePip(napi_env env, napi_callback_info info);
    static napi_value StartPip(napi_env env, napi_callback_info info);
    static napi_value RegisterStartPip(napi_env env, napi_callback_info info);
    static napi_value DeletePip(napi_env env, napi_callback_info info);
    static napi_value StopPip(napi_env env, napi_callback_info info);
    static napi_value RegisterLifecycleListener(napi_env env, napi_callback_info info);
    static void getElement(napi_env &env, uint32_t size, napi_value &controlGroupValue,
                PictureInPicture_PipControlGroup controlGroup[]);
};

napi_value PiPManager::CreatePip(napi_env env, napi_callback_info info)
{
    size_t argc = 1;
    napi_value argv[1] = {nullptr};
    napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
    napi_value config = argv[0];

    napi_value mainWindowIdValue = nullptr;
    napi_value pipTemplateTypeValue = nullptr;
    napi_value widthValue = nullptr;
    napi_value heightValue = nullptr;
    napi_value controlGroupValue = nullptr;
    napi_value pipControllerIdValue = nullptr;
    
    uint32_t controllerId = -1;
    uint32_t mainWindowId = -1;
    PictureInPicture_PipTemplateType pipTemplateType = PictureInPicture_PipTemplateType::VIDEO_PLAY;
    uint32_t width = -1;
    uint32_t height = -1;
    
    napi_get_named_property(env, config, "mainWindowId", &mainWindowIdValue);
    napi_get_named_property(env, config, "pipTemplateType", &pipTemplateTypeValue);
    napi_get_named_property(env, config, "width", &widthValue);
    napi_get_named_property(env, config, "height", &heightValue);
    napi_get_named_property(env, config, "controlGroup", &controlGroupValue);
    napi_get_named_property(env, config, "pipControllerId", &pipControllerIdValue);
    
    ConvertFromJsValue(env, mainWindowIdValue, mainWindowId);
    ConvertFromJsValue(env, pipTemplateTypeValue, pipTemplateType);
    ConvertFromJsValue(env, widthValue, width);
    ConvertFromJsValue(env, heightValue, height);
    ConvertFromJsValue(env, pipControllerIdValue, controllerId);
    
    uint32_t size = 0;
    napi_get_array_length(env, controlGroupValue, &size);
    PictureInPicture_PipControlGroup controlGroup[size];

    PiPManager::getElement(env, size, controlGroupValue, controlGroup);
    
    napi_value result = nullptr;
    PictureInPicture_PipConfig pipConfig;
    OH_PictureInPicture_CreatePipConfig(&pipConfig);
    OH_PictureInPicture_SetPipMainWindowId(pipConfig, mainWindowId);
    OH_PictureInPicture_SetPipTemplateType(pipConfig, pipTemplateType);
    OH_PictureInPicture_SetPipRect(pipConfig, width, height);
    OH_PictureInPicture_SetPipControlGroup(pipConfig, controlGroup, size);
    OH_PictureInPicture_SetPipNapiEnv(pipConfig, env);
    int32_t res = OH_PictureInPicture_CreatePip(pipConfig, &controllerId);
    OH_PictureInPicture_DestroyPipConfig(&pipConfig);
    napi_create_uint32(env, controllerId, &result);
    return result;
}

void PiPManager::getElement(napi_env &env, uint32_t size, napi_value &controlGroupValue,
    PictureInPicture_PipControlGroup controlGroup[])
{
    for (uint32_t i = 0; i < size; i++) {
        napi_value getElementValue = nullptr;
        napi_get_element(env, controlGroupValue, i, &getElementValue);
        PictureInPicture_PipControlGroup controlType;
        if (ConvertFromJsValue(env, getElementValue, controlType)) {
            controlGroup[i] = controlType;
        }
        LOG("controlType: %{public}d", controlType);
    }
}

napi_value PiPManager::StartPip(napi_env env, napi_callback_info info)
{
    size_t argc = 1;
    napi_value argv[1] = {nullptr};
    napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
    napi_value controlIdValue = argv[0];
    uint32_t controlId = -1;
    ConvertFromJsValue(env, controlIdValue, controlId);
    napi_value resultValue = nullptr;
    int32_t result = OH_PictureInPicture_StartPip(controlId);
    napi_create_uint32(env, result, &resultValue);
    return resultValue;
}

napi_value PiPManager::RegisterStartPip(napi_env env, napi_callback_info info)
{
    size_t argc = 2;
    napi_value argv[2] = {nullptr};
    napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
    napi_value controllerIdValue = argv[0];
    uint32_t controlId = -1;
    napi_status status = napi_create_reference(env, argv[1], 1, &jsCallback);
    env_ = env;
    ConvertFromJsValue(env, controllerIdValue, controlId);
    napi_value resultValue = nullptr;
    int32_t result = OH_PictureInPicture_RegisterStartPipCallback(controlId, PipStartPipCallback);
    napi_create_uint32(env, result, &resultValue);
    return resultValue;
}

napi_value PiPManager::DeletePip(napi_env env, napi_callback_info info)
{
    size_t argc = 1;
    napi_value argv[1] = {nullptr};
    napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
    uint32_t controlId = -1;
    ConvertFromJsValue(env, argv[0], controlId);
    napi_value resultValue = nullptr;
    int32_t result = OH_PictureInPicture_DeletePip(controlId);
    napi_create_uint32(env, result, &resultValue);
    return resultValue;
}

napi_value PiPManager::StopPip(napi_env env, napi_callback_info info)
{
    size_t argc = 1;
    napi_value argv[1] = {nullptr};
    napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
    uint32_t controlId = -1;
    napi_value resultValue = nullptr;

    ConvertFromJsValue(env, argv[0], controlId);
    uint32_t result = OH_PictureInPicture_StopPip(controlId);
    napi_create_uint32(env, result, &resultValue);
    return resultValue;
}

napi_value PiPManager::RegisterLifecycleListener(napi_env env, napi_callback_info info)
{
    size_t argc = 2;
    napi_value argv[2] = {nullptr};
    napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
    uint32_t controlId = -1;
    napi_status status = napi_create_reference(env, argv[1], 1, &jsLifecycleCallback);
    lifeEnv_ = env;
    if (status != napi_ok) {
        LOG("register failed %{public}d", status);
    }
    ConvertFromJsValue(env, argv[0], controlId);
    
    napi_value resultValue = nullptr;
    int32_t result = OH_PictureInPicture_RegisterLifecycleListener(controlId, LifecycleCallback);
    napi_create_uint32(env, result, &resultValue);
    return resultValue;
}

EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports)
{
    napi_property_descriptor desc[] = {
        {"createPip", nullptr, PiPManager::CreatePip, nullptr, nullptr, nullptr, napi_default, nullptr},
        {"startPip", nullptr, PiPManager::StartPip, nullptr, nullptr, nullptr, napi_default, nullptr},
        {"registerStartPip", nullptr, PiPManager::RegisterStartPip, nullptr, nullptr, nullptr, napi_default, nullptr},
        {"deletePip", nullptr, PiPManager::DeletePip, nullptr, nullptr, nullptr, napi_default, nullptr},
        {"stopPip", nullptr, PiPManager::StopPip, nullptr, nullptr, nullptr, napi_default, nullptr},
        {"registerLifecycleListener", nullptr, PiPManager::RegisterLifecycleListener,
            nullptr, nullptr, nullptr, napi_default, nullptr},
    };
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
    return exports;
}
EXTERN_C_END

static napi_module demoModule = {
    .nm_version = 1,
    .nm_flags = 0,
    .nm_filename = nullptr,
    .nm_register_func = Init,
    .nm_modname = "entry",
    .nm_priv = ((void*)0),
    .reserved = { 0 },
};
extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
{
    napi_module_register(&demoModule);
}
```

Node-API接口声明。

```ts
// Index.d.ts
export enum PiPControlGroup {
  VIDEO_PLAY_VIDEO_PREVIOUS_NEXT = 101,
  VIDEO_PLAY_FAST_FORWARD_BACKWARD = 102,
  VIDEO_CALL_MICROPHONE_SWITCH = 201,
  VIDEO_CALL_HANG_UP_BUTTON = 202,
  VIDEO_CALL_CAMERA_SWITCH = 203,
  VIDEO_CALL_MUTE_SWITCH = 204,
  VIDEO_MEETING_HANG_UP_BUTTON = 301,
  VIDEO_MEETING_CAMERA_SWITCH = 302,
  VIDEO_MEETING_MUTE_SWITCH = 303,
  VIDEO_MEETING_MICROPHONE_SWITCH = 304,
  VIDEO_LIVE_VIDEO_PLAY_PAUSE = 401,
  VIDEO_LIVE_MUTE_SWITCH = 402,
}
export interface PiPConfig {
  mainWindowId: number;
  pipTemplateType: number;
  width: number;
  height: number;
  controlGroup: Array<PiPControlGroup>;
}
export declare const createPip: (config: PiPConfig) => number;
export declare const startPip: (controllerId: number) => number;
export declare const registerStartPip: (controllerId: number, jsCallback: Function) => number;
export declare const deletePip: (controllerId: number) => number;
export declare const stopPip: (controllerId: number) => number;
export declare const registerLifecycleListener: (controllerId: number, jsCallback: Function) => number;
```

CMakeLists.txt文件，用于生成对应的库文件。

```txt
# CMakeLists.txt
# the minimum version of CMake.
cmake_minimum_required(VERSION 3.5.0)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
project(MyApplication)
set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})
if(DEFINED PACKAGE_FIND_FILE)
    include(${PACKAGE_FIND_FILE})
endif()
include_directories(${NATIVERENDER_ROOT_PATH}
                    ${NATIVERENDER_ROOT_PATH}/include)
add_library(entry SHARED napi_init.cpp)
target_link_libraries(entry PUBLIC libace_napi.z.so libace_ndk.z.so libnative_window_manager.so libhilog_ndk.z.so)
```

EntryAbility文件示例。

```typescript
// entryability/EntryAbility.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { PipManager } from '../nodefree/PipManager';
import { Logger } from '../util/LogUtil';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    AppStorage.setOrCreate('UIAbilityContext', this.context);
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (err) {
      Logger.error('testTag', 'Failed to set color mode: %{public}s', JSON.stringify(err));
    }
  }

  onDestroy(): void {
    Logger.info('testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    Logger.info('testTag', '%{public}s', 'Ability onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    let windowClassId: number = -1;

    windowStage.getMainWindow().then((window) => {
      if (window == null) {
        Logger.error('Failed to obtaining the window. Cause: The data is empty');
        return;
      }
      windowClass = window;
      windowClass.setUIContent('pages/Index');
      windowClassId = windowClass.getWindowProperties().id;
      AppStorage.setOrCreate('windowId', windowClassId);
      Logger.info('Succeeded in obtaining the window')

      let ctx = window.getUIContext();
      AppStorage.setOrCreate('UIContext', ctx);
      // 通过主窗口UIContext创建typeNode节点
      PipManager.getInstance().makeTypeNode(ctx);
    }).catch((err: BusinessError) => {
      Logger.error(`Failed to obtaining the window. Cause code: ${err.code}, message: ${err.message}`);
    });
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        Logger.error('testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      Logger.info('testTag', 'Succeeded in loading the content.');
    });
  }
  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    Logger.info('testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    Logger.info('testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    Logger.info('testTag', '%{public}s', 'Ability onBackground');
  }
}
```

示例中的视频播放需要使用AVPlayer，具体实现可参考[视频播放](video-playback.md)。

```typescript
// model/AVPlayer.ets
// 视频播放器简单实现
import media from '@ohos.multimedia.media';
import common from '@ohos.app.ability.common';
import { BusinessError } from '@ohos.base';
import resourceManager from '@ohos.resourceManager';
import { Logger } from '../util/LogUtil';

export class AVPlayer {
  public avPlayer?: media.AVPlayer;
  private count: number = 0;
  private surfaceID: string; // surfaceID用于播放画面显示，具体的值需要通过Xcomponent接口获取，相关文档链接见上面Xcomponent创建方法
  public jumpNext: boolean = false;
  public type: number = 0; // 用于区分主界面的player还是pip界面的player
  public state_: string = ''
  public playStatus: boolean = true;

  constructor(surfaceID: string, type: number) {
    this.surfaceID = surfaceID;
    this.type = type
  }

  setSurfaceId(id: string) {
    if (this.avPlayer) {
      this.surfaceID = id;
      this.avPlayer.surfaceId = id;
    }
  }

  updatePlayStatus(status: boolean) {
    this.playStatus = status;
  }
  // 注册avplayer回调函数
  setAVPlayerCallback() {
    // seek操作结果回调函数
    this.avPlayer?.on('seekDone', (seekDoneTime: number) => {
      Logger.info(`PipMain AVPlayer seek succeeded, seek time is ${seekDoneTime}`);
    })
    // error回调监听函数,当avPlayer在操作过程中出现错误时调用reset接口触发重置流程
    this.avPlayer?.on('error', (err: BusinessError) => {
      Logger.error(`PipMain Invoke avPlayer failed, code is ${err.code}, message is ${err.message}`);
      this.avPlayer?.reset(); // 调用reset重置资源，触发idle状态
    })
    // 状态机变化回调函数
    this.avPlayer?.on('stateChange', async (state, reason) => {
      if (!this.avPlayer) {
        return;
      }
      this.state_ = state;
      switch (state) {
        case 'idle': // 成功调用reset接口后触发该状态机上报
          Logger.info('AVPlayer state idle called.');
          if (!this.jumpNext) {
            this.avPlayer.release(); // 调用release接口销毁实例对象
          } else {
            let uiContext: UIContext = AppStorage.get('UIAbilityContext') as UIContext;
            let context = uiContext.getHostContext() as common.UIAbilityContext;
            let fileDescriptor: resourceManager.RawFileDescriptor;
            fileDescriptor = await context.resourceManager.getRawFd('640x360.mp4');
            // 为fdSrc赋值触发initialized状态机上报
            this.avPlayer.fdSrc = fileDescriptor;
          }
          break;
        case 'initialized': // avplayer 设置播放源后触发该状态上报
          Logger.info('initialized called.');
          this.avPlayer.surfaceId = this.surfaceID; // 设置显示画面，当播放的资源为纯音频时无需设置
          this.avPlayer.prepare().then(() => {
            Logger.info('AVPlayer prepare succeeded.');
          }, (err: BusinessError) => {
            Logger.error(`Invoke prepare failed, code is ${err.code}, message is ${err.message}`);
          });
          break;
        case 'prepared': // prepare调用成功后上报该状态机
          Logger.info('AVPlayer state prepared called.');
          this.avPlayer.play(); // 调用播放接口开始播放
          break;
        case 'playing': // play成功调用后触发该状态机上报
          Logger.info('AVPlayer state playing called.');
          this.jumpNext = false;
          this.count++;
          break;
        case 'paused': // pause成功调用后触发该状态机上报
          Logger.info('AVPlayer state paused called.');
          // this.avPlayer.play(); // 再次播放接口开始播放
          break;
        case 'completed': // 播放结束后触发该状态机上报
          Logger.info('AVPlayer state completed called.');
          this.playNext();
          ; // 调用播放结束接口
          break;
        case 'stopped': // stop接口成功调用后触发该状态机上报
          Logger.info('AVPlayer state stopped called.');
          this.avPlayer.reset(); // 调用reset接口初始化avplayer状态
          break;
        case 'released':
          Logger.info('AVPlayer state released called.');
          break;
        default:
          Logger.info('AVPlayer state unknown called.');
          break;
      }
    })
    this.avPlayer?.on('videoSizeChange', (width: number, height: number) => {
      Logger.info('videoSizeChange width:' + width + ' height:' + height);
      let context = AppStorage.get('UIAbilityContext') as common.UIAbilityContext;
    })
  }

  // 以下demo为使用资源管理接口获取打包在HAP内的媒体资源文件并通过fdSrc属性进行播放示例
  async avPlayerFdSrc() {
    Logger.info('avPlayerFdSrc');
    try {
      // 创建avPlayer实例对象
      this.avPlayer = await media.createAVPlayer();
    } catch (err) {
      let error = err as BusinessError;
      Logger.error(`createAVPlayer failed, code: ${error.code}, msg: ${error.message}`);
      return;
    }

    // 创建状态机变化回调函数
    this.setAVPlayerCallback();
    // 通过UIAbilityContext的resourceManager成员的getRawFd接口获取媒体资源播放地址
    // 返回类型为{fd,offset,length},fd为HAP包fd地址，offset为媒体资源偏移量，length为播放长度

    try {
      let context = AppStorage.get('UIAbilityContext') as common.UIAbilityContext;
      let fileDescriptor = await context.resourceManager.getRawFd('640x360.mp4');
      Logger.info('getRawFd');
      // 为fdSrc赋值触发initialized状态机上报
      this.avPlayer.fdSrc = fileDescriptor;
    } catch (err) {
      let error = err as BusinessError;
      Logger.error(`getRawFd failed, code=${error.code}, msg=${error.message}`);
    }
  }

  async playNext() {
    if (this.avPlayer === null) {
      return;
    }
    this.jumpNext = true;
    this.avPlayer?.stop()
    .then(() => {
      Logger.info(`Succeeded to stop avPlayer`);
    }).catch((err: BusinessError) => {
      Logger.error(`Failed to stop avPlayer, Cause:${err.code}, message:${err.message}`);
    });
  }

  play() {
    if (this.state_ === 'paused') {
      this.avPlayer?.play()
        .then(() => {
          Logger.info(`Succeeded to play avPlayer`);
        }).catch((err: BusinessError) => {
          Logger.error(`Failed to play avPlayer, Cause:${err.code}, message:${err.message}`);
      });
    }
  }

  pause() {
    if (this.state_ === 'playing') {
      this.avPlayer?.pause()
        .then(() => {
          Logger.info(`Succeeded to pause avPlayer`);
        }).catch((err: BusinessError) => {
          Logger.error(`Failed to pause avPlayer, Cause:${err.code}, message:${err.message}`);
      });
    }
  }

  stopAvPlayer() {
    Logger.info('stopAvPlayer>>>')
    if (!this.avPlayer) {
      return;
    }
    this.avPlayer.stop()
      .then(() => {
        Logger.info(`Succeeded to stop avPlayer`);
      }).catch((err: BusinessError) => {
        Logger.error(`Failed to stop avPlayer, Cause:${err.code}, message:${err.message}`);
    });
    Logger.info('stopping>>>');
    this.avPlayer.reset()
      .then(() => {
        Logger.info(`Succeeded to reset avPlayer`);
      }).catch((err: BusinessError) => {
        Logger.error(`Failed to reset avPlayer, Cause:${err.code}, message:${err.message}`);
    });
  }
}
```

应用界面布局文件，用于演示画中画基本功能。

```ts
// pages/Index.ets
// 应用首页
import { router } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  pathStack: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.pathStack) {
      Scroll() {
        Flex({ direction: FlexDirection.Column }) {
          // ...
          this.featureButton('使用NDK接口实现画中画（C++）', this.ndkImplement);
        }
      }
    }
    .hideBackButton(true)
    .titleMode(NavigationTitleMode.Mini)
    .backgroundColor('#FFF1F3F5')
    .mode(NavigationMode.Stack)
    .title('画中画SampleCode')
  }

  @Builder
  featureButton(buttonText: string, callbackOnClick: () => void) {
    Button({ type: ButtonType.Normal }) {
      Row() {
        Column() {
          Text(buttonText)
            .fontSize(24)
            .fontWeight(FontWeight.Bold)
            .fontColor('#000000')
          Rect()
            .radius(1)
            .fill('#0A59F7')
            .height(2)
            .width(30)
        }
        .width('100%')
        .alignItems(HorizontalAlign.Start)
      }
      .width('100%')
    }
    .width('90%')
    .padding('5%')
    .margin({ top: '3%', bottom: '2%', right: '3%' })
    .backgroundColor('#FFFFFF')
    .borderRadius(20)
    .onClick(callbackOnClick)
  }

  // ...
  private ndkImplement = () => {
    this.getUIContext().getRouter().pushUrl({ url: 'pages/NDKImplementPage' }, router.RouterMode.Standard)
  }
}
```

```ts
// pages/NDKImplementIndexPage.ets
// 画中画功能演示界面
import testNapi, {PiPConfig} from 'libentry.so';
import { PiPWindow } from '@kit.ArkUI';
import { AVPlayer } from '../model/NDKAVPlayer';
import { Logger } from '../util/LogUtil';

const TAG = 'PipMain';
export enum PiPControlGroup {
  VIDEO_PLAY_VIDEO_PREVIOUS_NEXT = 101,
  VIDEO_PLAY_FAST_FORWARD_BACKWARD = 102,
  VIDEO_CALL_MICROPHONE_SWITCH = 201,
  VIDEO_CALL_HANG_UP_BUTTON = 202,
  VIDEO_CALL_CAMERA_SWITCH = 203,
  VIDEO_CALL_MUTE_SWITCH = 204,
  VIDEO_MEETING_HANG_UP_BUTTON = 301,
  VIDEO_MEETING_CAMERA_SWITCH = 302,
  VIDEO_MEETING_MUTE_SWITCH = 303,
  VIDEO_MEETING_MICROPHONE_SWITCH = 304,
  VIDEO_LIVE_VIDEO_PLAY_PAUSE = 401,
  VIDEO_LIVE_MUTE_SWITCH = 402,
}

@Entry
@Component
struct NDKImplementIndexPage {
  @State message: string = 'Hello World';
  mXComponentController: XComponentController | null = new XComponentController();
  private controllerId: number = -1;
  private contentWidth: number = 1920;
  private contentHeight: number = 1080;
  private pipType: PiPWindow.PiPTemplateType = PiPWindow.PiPTemplateType.VIDEO_PLAY;
  private pipControlGroups: Array<PiPControlGroup> = [];
  player?: AVPlayer;
  surfaceId = '';

  changeSurface = (surfaceId: string) => {
    if(this.player) {
      this.player.setSurfaceId(surfaceId);
      return;
    }
    Logger.info(`[${TAG}] change surface failed`);
  }

  private onStateChange = (state: PiPWindow.PiPState) => {
    switch(state) {
      case PiPWindow.PiPState.ABOUT_TO_START:
        Logger.info(`[${TAG}] ABOUT_TO_START`);
        break;
      case PiPWindow.PiPState.STARTED:
        Logger.info(`[${TAG}] STARTED`);
        break;
      case PiPWindow.PiPState.ABOUT_TO_STOP:
        Logger.info(`[${TAG}] ABOUT_TO_STOP`);
        break;
      case PiPWindow.PiPState.STOPPED:
        if (this.mXComponentController) {
          this.changeSurface(this.mXComponentController?.getXComponentSurfaceId());
        }
        Logger.info(`[${TAG}] STOPPED`);
        break;
      case PiPWindow.PiPState.ABOUT_TO_RESTORE:
        this.changeSurface(this.surfaceId);
        Logger.info(`[${TAG}] ABOUT_TO_RESTORE`);
        break;
      case PiPWindow.PiPState.ERROR:
        Logger.info(`[${TAG}] ERROR`);
        break;
      default:
        break;
    }
  }

  build() {
    RelativeContainer() {
      Row({ space: 20 }) {

        Button('更换模板')
          .bindMenu([
            {
              value: '视频',
              action: () => {
                this.pipType = PiPWindow.PiPTemplateType.VIDEO_PLAY;
                this.pipControlGroups = [PiPControlGroup.VIDEO_PLAY_VIDEO_PREVIOUS_NEXT];
              }
            },
            {
              value: '通话',
              action: () => {
                this.pipType = PiPWindow.PiPTemplateType.VIDEO_CALL;
                this.pipControlGroups = [PiPControlGroup.VIDEO_CALL_HANG_UP_BUTTON,
                  PiPControlGroup.VIDEO_CALL_CAMERA_SWITCH, PiPControlGroup.VIDEO_CALL_MICROPHONE_SWITCH];
              }
            },
            {
              value: '会议',
              action: () => {
                this.pipType = PiPWindow.PiPTemplateType.VIDEO_MEETING;
                this.pipControlGroups = [PiPControlGroup.VIDEO_MEETING_MICROPHONE_SWITCH,
                  PiPControlGroup.VIDEO_MEETING_HANG_UP_BUTTON,
                  PiPControlGroup.VIDEO_MEETING_CAMERA_SWITCH];
              }
            },
            {
              value: '直播',
              action: () => {
                this.pipType = PiPWindow.PiPTemplateType.VIDEO_LIVE;
                this.pipControlGroups = [PiPControlGroup.VIDEO_LIVE_VIDEO_PLAY_PAUSE,
                  PiPControlGroup.VIDEO_LIVE_MUTE_SWITCH];
              }
            }
          ])
      }
      .size({ width: '100%', height: 60 })
      .backgroundColor('#DDDDDD')
      .justifyContent(FlexAlign.SpaceAround)
      .alignRules({
        top: { anchor: '__container__', align: VerticalAlign.Top },
        middle: { anchor: '__container__', align: HorizontalAlign.Center }
      })
      .id('pip_type_control')
      XComponent({
        type: XComponentType.SURFACE,
        controller: this.mXComponentController
      })
        .onLoad(() => {
          if (this.mXComponentController) {
            this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
          }
          this.player = new AVPlayer(this.surfaceId, 1);
          this.player.avPlayerFdSrc();
        })
        .onDestroy(() => {
          Logger.info(`[${TAG}] XComponent onDestroy`);
        })
        .size({ width: '100%', height: '800px' })
        .margin({ top: 10 })
        .backgroundColor('#888888')
        .alignRules({
          bottom: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .id('x_component')
        .size({ width: '100%', height: '800px' })
      Row({ space: 0 }) {
        Button('创建画中画')
          .onClick(() => {
            let windowId: number | undefined = AppStorage.get('windowId');
            let config: PiPConfig = {
              mainWindowId: windowId as number,
              pipTemplateType: this.pipType,
              width: this.contentWidth,
              height: this.contentHeight,
              controlGroup: this.pipControlGroups
            }
            this.controllerId = testNapi.createPip(config);
            testNapi.registerStartPip(this.controllerId, this.changeSurface);
            testNapi.registerLifecycleListener(this.controllerId, this.onStateChange);
          })
        Button('开启画中画')
          .onClick(() => {
            testNapi.startPip(this.controllerId);
          })
      }
      .size({ width: '100%', height: 60 })
      .alignRules({
        top: { anchor: 'x_component', align: VerticalAlign.Bottom },
        left: { anchor: '__container__', align: HorizontalAlign.Start }
      })
      .id('pip_control')
      Row({ space: 0 }) {
        Button('关闭画中画')
          .onClick(() => {
            testNapi.stopPip(this.controllerId);
          })
        Button('删除控制器')
          .onClick(() => {
            testNapi.deletePip(this.controllerId);
          })
      }
      .size({ width: '100%', height: 60 })
      .alignRules({
        top: { anchor: 'pip_control', align: VerticalAlign.Bottom },
        left: { anchor: '__container__', align: HorizontalAlign.Start }
      })
    }
    .size({ width: '100%', height: '100%' })
  }
}
```

以上示例代码对应的示意图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/qiRu5IVIRe-BvvDtWahU4Q/zh-cn_image_0000002736313123.gif)
