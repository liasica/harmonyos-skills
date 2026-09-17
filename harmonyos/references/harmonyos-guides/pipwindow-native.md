---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pipwindow-native
title: 使用NDK接口实现画中画功能开发 (C/C++)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口类型 > 画中画开发指导 > 使用NDK接口实现画中画功能开发 (C/C++)
category: harmonyos-guides
scraped_at: 2026-09-18T06:45:13+08:00
doc_updated_at: 2026-09-17
content_hash: sha256:cdb77d3cd0c6cf18a26fd68aa80ac28d105a03fbee2d2d4a3730abe14c798cb4
---

本文以视频播放场景为例，介绍通过NDK接口实现画中画功能的基本开发步骤。

**说明** 

* 从API version 20开始，支持使用NDK接口实现画中画功能开发。
* 支持在Phone、PC/2in1、Tablet设备使用NDK接口实现画中画功能开发。

## 约束与限制

* 画中画窗口中画面的呈现不通过传入XComponent Controller实现，而是通过渲染surfaceId（在开启画中画回调中获取）对应的组件实现。
* 与typeNode实现方式相同，系统不缓存页面。如需进行页面操作，应用需要开启画中画生命周期监听，在对应生命周期内进行相应操作。

## 开发步骤

### Node-API层实现示例

Node-API模块注册方法，具体使用请参考[Native API在应用工程中的使用指导](napi-guidelines.md)。

1. 通过[OH\_PictureInPicture\_CreatePipConfig](../harmonyos-references/capi-oh-window-pip-h.md#oh_pictureinpicture_createpipconfig)创建画中画参数配置器，并通过[OH\_PictureInPicture\_SetPipMainWindowId](../harmonyos-references/capi-oh-window-pip-h.md#oh_pictureinpicture_setpipmainwindowid)、[OH\_PictureInPicture\_SetPipTemplateType](../harmonyos-references/capi-oh-window-pip-h.md#oh_pictureinpicture_setpiptemplatetype)、[OH\_PictureInPicture\_SetPipRect](../harmonyos-references/capi-oh-window-pip-h.md#oh_pictureinpicture_setpiprect)、[OH\_PictureInPicture\_SetPipControlGroup](../harmonyos-references/capi-oh-window-pip-h.md#oh_pictureinpicture_setpipcontrolgroup)、[OH\_PictureInPicture\_SetPipNapiEnv](../harmonyos-references/capi-oh-window-pip-h.md#oh_pictureinpicture_setpipnapienv)接口在画中画参数配置器中设置初始配置信息。

   ```
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
       // ...
   }
   ```
2. 创建画中画控制器。后续可根据返回的controllerId注册生命周期事件以及控制事件回调。通过[OH\_PictureInPicture\_CreatePip](../harmonyos-references/capi-oh-window-pip-h.md#oh_pictureinpicture_createpip)接口创建画中画控制器实例，并缓存对应的控制器标识。建议在创建完成后立即调用[OH\_PictureInPicture\_DestroyPipConfig](../harmonyos-references/capi-oh-window-pip-h.md#oh_pictureinpicture_destroypipconfig)销毁画中画参数配置器，以免发生内存泄漏。

   ```
   napi_value PiPManager::CreatePip(napi_env env, napi_callback_info info)
   {
       // ...
       int32_t res = OH_PictureInPicture_CreatePip(pipConfig, &controllerId);
       OH_PictureInPicture_DestroyPipConfig(&pipConfig);
       napi_create_uint32(env, controllerId, &result);
       return result;
   }
   ```
3. 通过[OH\_PictureInPicture\_RegisterStartPipCallback](../harmonyos-references/capi-oh-window-pip-h.md#oh_pictureinpicture_registerstartpipcallback)接口注册启动画中画回调，并根据返回的surfaceId渲染视频画面。同时应用可以按需注册其他需要监听的事件回调。

   ```
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
   ```
4. 通过[OH\_PictureInPicture\_StartPip](../harmonyos-references/capi-oh-window-pip-h.md#oh_pictureinpicture_startpip)启动画中画。

   ```
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
   ```

   从API版本26.0.0开始，还可以通过[OH\_PictureInPicture\_SetAutoStartEnabled](../harmonyos-references/capi-oh-window-pip-h.md#oh_pictureinpicture_setautostartenabled)接口设置在应用主窗退后台时是否自动启动画中画。

   ```
   napi_value PiPManager::SetAutoStart(napi_env env, napi_callback_info info)
   {
       size_t argc = 2;
       napi_value argv[2] = {nullptr};
       napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
       uint32_t controllerId = -1;
       ConvertFromJsValue(env, argv[0], controllerId);
       bool enabled;
       ConvertFromJsValue(env, argv[1], enabled);
       napi_value resultValue = nullptr;
       LOG("set auto start enable: %{public}d", enabled);
       int32_t result = OH_PictureInPicture_SetAutoStartEnabled(controllerId, enabled);
       napi_create_uint32(env, result, &resultValue);
       return resultValue;
   }
   ```
5. 通过[OH\_PictureInPicture\_UpdatePipContentSize](../harmonyos-references/capi-oh-window-pip-h.md#oh_pictureinpicture_updatepipcontentsize)更新媒体源尺寸信息。

   ```
   napi_value PiPManager::UpdatePipContentSize(napi_env env, napi_callback_info info)
   {
       size_t argc = 3;
       napi_value argv[3] = {nullptr};
       napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
       uint32_t controlId = -1;
       uint32_t width = -1;
       uint32_t height = -1;
       uint32_t index = 0;

       ConvertFromJsValue(env, argv[index++], controlId);
       ConvertFromJsValue(env, argv[index++], width);
       ConvertFromJsValue(env, argv[index], height);
       
       napi_value resultValue = nullptr;
       int32_t result = OH_PictureInPicture_UpdatePipContentSize(controlId, width, height);
       napi_create_uint32(env, result, &resultValue);
       return resultValue;
   }
   ```
6. 通过[OH\_PictureInPicture\_StopPip](../harmonyos-references/capi-oh-window-pip-h.md#oh_pictureinpicture_stoppip)关闭画中画。

   ```
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
   ```
7. 通过[OH\_PictureInPicture\_UnregisterStartPipCallback](../harmonyos-references/capi-oh-window-pip-h.md#oh_pictureinpicture_unregisterstartpipcallback)解注册画中画启动回调，避免内存泄漏。同时应用可以按需解注册其他已注册的事件回调。

   ```
   napi_value PiPManager::UnregisterStartPip(napi_env env, napi_callback_info info)
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
       int32_t result = OH_PictureInPicture_UnregisterStartPipCallback(controlId, PipStartPipCallback);
       napi_create_uint32(env, result, &resultValue);
       return resultValue;
   }
   ```
8. 以上对NDK接口进行的包装还不能使用，需要通过[模块加载](use-napi-about-extension.md#模块加载)的napi\_module\_register函数将方法对外暴露。

   ```
   EXTERN_C_START
   static napi_value Init(napi_env env, napi_value exports) {
       napi_property_descriptor desc[] = {
           {"createPip", nullptr, PiPManager::CreatePip, nullptr, nullptr, nullptr, napi_default, nullptr},
           {"startPip", nullptr, PiPManager::StartPip, nullptr, nullptr, nullptr, napi_default, nullptr},
           {"registerStartPip", nullptr, PiPManager::RegisterStartPip, nullptr, nullptr, nullptr, napi_default, nullptr},
           {"deletePip", nullptr, PiPManager::DeletePip, nullptr, nullptr, nullptr, napi_default, nullptr},
           {"stopPip", nullptr, PiPManager::StopPip, nullptr, nullptr, nullptr, napi_default, nullptr},
           {"updatePipContentSize", nullptr, PiPManager::UpdatePipContentSize, nullptr, nullptr, nullptr,
            napi_default, nullptr},
           {"registerLifecycleListener", nullptr, PiPManager::RegisterLifecycleListener, nullptr, nullptr, nullptr,
            napi_default, nullptr},
           {"unregisterStartPip", nullptr, PiPManager::UnregisterStartPip, nullptr, nullptr, nullptr, napi_default,
            nullptr},
           {"unregisterLifecycleListener", nullptr, PiPManager::UnregisterLifecycleListener, nullptr, nullptr, nullptr,
            napi_default, nullptr },
           {"setAutoStart", nullptr, PiPManager::SetAutoStart, nullptr, nullptr, nullptr, napi_default, nullptr},
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
9. 对外暴露的接口，其中接口实现必须与第8步中声明的函数一致。这些接口将是后续被实际调用的接口。

   ```typescript
   // ...
   export declare const createPip: (config: PiPConfig) => number;
   export declare const startPip: (controllerId: number) => number;
   export declare const registerStartPip: (controllerId: number, jsCallback: Function) => number;
   export declare const unregisterStartPip: (controllerId: number, jsCallback: Function) => number;
   export declare const deletePip: (controllerId: number) => number;
   export declare const stopPip: (controllerId: number) => number;
   export declare const updatePipContentSize: (controllerId: number, width: number, height: number) => number;
   export declare const registerLifecycleListener: (controllerId: number, jsCallback: Function) => number;
   export declare const unregisterLifecycleListener: (controllerId: number, jsCallback: Function) => number;
   export declare const setAutoStart: (controllerId: number, enabled: boolean) => number;
   ```
10. 编写[CMakeLists.txt](build-with-ndk-ide.md#cmakeliststxt)文件，用于生成对应的库文件。

    ```text
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

### 应用层实现示例

1. 应用启动时，需要在UIAbility创建时保存窗口ID，用于绑定主窗和画中画的关系。

   ```typescript
   export default class EntryAbility extends UIAbility {
   // ...
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
         // ...
   }
   ```
2. 使用保存的窗口ID创建控制器。在成功创建画中画控制器后，需要通过获取到的控制器ID注册画中画启动的回调函数以切换需要渲染的surfaceId，除此之外应用可以选择注册画中画生命周期回调函数以满足业务需求。

   ```typescript
   import testNapi, {PiPConfig} from 'libentry.so';
   // ...
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
     // ...
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
               // ...
   ```
3. 使用获取到的控制器ID，启动画中画。

   ```typescript
   testNapi.startPip(this.controllerId);
   ```
4. 使用获取到的控制器ID，开启自动拉起画中画。当启动该画中画的主窗退后台后，会自动拉起画中画。

   ```typescript
   let ret: number = testNapi.setAutoStart(this.controllerId, true);
   Logger.info(`set auto start enabled result: ${ret}`);
   ```
5. 使用获取到的控制器ID，调整画中画尺寸。

   ```typescript
   testNapi.updatePipContentSize(this.controllerId, 900, 1600);
   ```
6. 使用获取到的控制器ID，关闭画中画。

   ```typescript
   testNapi.stopPip(this.controllerId);
   ```
7. 当画中画控制器不再使用时，需要使用获取到的控制器ID解除回调注册并删除画中画控制器，以防止内存泄漏。

   ```typescript
   testNapi.unregisterStartPip(this.controllerId, this.changeSurface);
   testNapi.unregisterLifecycleListener(this.controllerId, this.onStateChange);
   testNapi.deletePip(this.controllerId);
   ```
