---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-display-manager
title: 使用OH_DisplayManager实现屏幕基础信息查询和状态监听 (C/C++)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 屏幕管理 > 使用OH_DisplayManager实现屏幕基础信息查询和状态监听 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:34c3cccf952b29d4ab45e5d08c42bd9a077f4e176a259aeef6060ac8f749a749
---

## 场景介绍

[OH\_DisplayManager](../harmonyos-references/capi-oh-displaymanager.md)屏幕管理模块用于提供屏幕的信息查询、屏幕状态变化监听、折叠设备的折叠状态变化监听等能力，应用可根据对应的屏幕信息、屏幕状态变化、屏幕折叠状态适配不同的UI界面显示。

* 支持查询的屏幕信息，包括屏幕的分辨率、物理像素密度、逻辑像素密度、刷新率、屏幕尺寸、屏幕旋转方向、屏幕旋转角度等。
* 支持屏幕状态变化的监听，包括屏幕旋转变化，屏幕分辨率变化、屏幕刷新率变化等。
* 支持查询当前设备是否为可折叠设备，同时支持折叠状态（展开/折叠）变化的监听。

## 基本概念

* 屏幕的物理像素密度(densityDPI)：代表每英寸屏幕所拥有的物理像素点数。
* 屏幕的逻辑像素的密度(densityPixels)：代表物理像素与逻辑像素的缩放系数比，计算方法为物理像素密度除以160。

## 接口说明

常用接口如下表所示。更多API说明请参考[OH\_DisplayManager](../harmonyos-references/capi-oh-displaymanager.md)。

| 接口名 | 描述 |
| --- | --- |
| OH\_NativeDisplayManager\_GetDefaultDisplayRotation(NativeDisplayManager\_Rotation \*displayRotation) | 获取默认屏幕的旋转角度。 |
| OH\_NativeDisplayManager\_CreateDefaultDisplayCutoutInfo(NativeDisplayManager\_CutoutInfo \*\*cutoutInfo) | 获取挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。 |
| OH\_NativeDisplayManager\_DestroyDefaultDisplayCutoutInfo(NativeDisplayManager\_CutoutInfo \*cutoutInfo) | 销毁挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。 |
| OH\_NativeDisplayManager\_IsFoldable() | 查询设备是否可折叠。 |
| OH\_NativeDisplayManager\_RegisterDisplayChangeListener( OH\_NativeDisplayManager\_DisplayChangeCallback displayChangeCallback, uint32\_t \*listenerIndex) | 注册屏幕状态变化监听（如旋转变化、刷新率、DPI、分辨率等）。 |
| OH\_NativeDisplayManager\_UnregisterDisplayChangeListener(uint32\_t listenerIndex) | 取消屏幕状态变化监听。 |
| OH\_NativeDisplayManager\_RegisterFoldDisplayModeChangeListener( OH\_NativeDisplayManager\_FoldDisplayModeChangeCallback displayModeChangeCallback, uint32\_t \*listenerIndex) | 注册屏幕展开、折叠状态变化监听。 |
| OH\_NativeDisplayManager\_UnregisterFoldDisplayModeChangeListener(uint32\_t listenerIndex) | 取消屏幕展开、折叠状态变化监听。 |

## 在CMake脚本中链接动态库

```
1. target_link_libraries(entry PUBLIC libhilog_ndk.z.so)
2. target_link_libraries(entry PUBLIC libnative_display_manager.so )
```

## 添加头文件

```
1. #include <window_manager/oh_display_info.h>
2. #include <window_manager/oh_display_manager.h>
3. #include <hilog/log.h>
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDisplayBasicSample/entry/src/main/cpp/napi_init.cpp#L17-L21)

## 获取屏幕状态

1. 可以通过OH\_NativeDisplayManager\_GetDefaultDisplayRotation获取默认屏幕的旋转角度。

   ```
   1. static napi_value GetDefaultDisplayRotation(napi_env env, napi_callback_info info)
   2. {
   3. NativeDisplayManager_Rotation displayRotation;
   4. NativeDisplayManager_ErrorCode errCode = OH_NativeDisplayManager_GetDefaultDisplayRotation(&displayRotation);
   5. if (errCode == NativeDisplayManager_ErrorCode::DISPLAY_MANAGER_OK) {
   6. napi_value rotation;
   7. napi_create_int32(env, displayRotation, &rotation);
   8. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "DMSTest", "rotation=%{public}d", displayRotation);
   9. return rotation;
   10. } else {
   11. napi_value errorCode;
   12. napi_create_int32(env, errCode, &errorCode);
   13. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "DMSTest",
   14. "GetDefaultDisplayRotation errCode=%{public}d", errCode);
   15. return errorCode;
   16. }
   17. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDisplayBasicSample/entry/src/main/cpp/napi_init.cpp#L25-L43)
2. 可以通过OH\_NativeDisplayManager\_CreateDefaultDisplayCutoutInfo获取挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。 可通过OH\_NativeDisplayManager\_DestroyDefaultDisplayCutoutInfo销毁挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。

   ```
   1. static napi_value CreateDefaultDisplayCutoutInfo(napi_env env, napi_callback_info info)
   2. {
   3. NativeDisplayManager_CutoutInfo *cutOutInfo = NULL;
   4. NativeDisplayManager_ErrorCode errCode = OH_NativeDisplayManager_CreateDefaultDisplayCutoutInfo(&cutOutInfo);
   5. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "DMSTest", "GetDefaultCutoutInfo errCode=%{public}d", errCode);
   6. if (errCode == NativeDisplayManager_ErrorCode::DISPLAY_MANAGER_OK) {
   7. if (cutOutInfo != NULL && cutOutInfo->boundingRectsLength != 0) {
   8. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "DMSTest",
   9. "GetDefaultCutoutInfo cutOutInfo length=%{public}d", cutOutInfo->boundingRectsLength);
   10. for (int i = 0; i < cutOutInfo->boundingRectsLength; i++) {
   11. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "DMSTest",
   12. "cutOutInfo[%{public}d]=[%{public}d %{public}d %{public}d %{public}d]",
   13. i, cutOutInfo->boundingRects[i].left, cutOutInfo->boundingRects[i].top,
   14. cutOutInfo->boundingRects[i].width, cutOutInfo->boundingRects[i].height);
   15. }
   16. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "DMSTest",
   17. "cutOutInfo waterfall left rect=[%{public}d %{public}d %{public}d %{public}d]",
   18. cutOutInfo->waterfallDisplayAreaRects.left.left, cutOutInfo->waterfallDisplayAreaRects.left.top,
   19. cutOutInfo->waterfallDisplayAreaRects.left.width, cutOutInfo->waterfallDisplayAreaRects.left.height);
   20. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "DMSTest",
   21. "cutOutInfo waterfall top rect=[%{public}d %{public}d %{public}d %{public}d]",
   22. cutOutInfo->waterfallDisplayAreaRects.top.left, cutOutInfo->waterfallDisplayAreaRects.top.top,
   23. cutOutInfo->waterfallDisplayAreaRects.top.width, cutOutInfo->waterfallDisplayAreaRects.top.height);
   24. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "DMSTest",
   25. "cutOutInfo waterfall right rect=[%{public}d %{public}d %{public}d %{public}d]",
   26. cutOutInfo->waterfallDisplayAreaRects.right.left, cutOutInfo->waterfallDisplayAreaRects.right.top,
   27. cutOutInfo->waterfallDisplayAreaRects.right.width, cutOutInfo->waterfallDisplayAreaRects.right.height);
   28. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "DMSTest",
   29. "cutOutInfo waterfall bottom rect=[%{public}d %{public}d %{public}d %{public}d]",
   30. cutOutInfo->waterfallDisplayAreaRects.bottom.left,
   31. cutOutInfo->waterfallDisplayAreaRects.bottom.top,
   32. cutOutInfo->waterfallDisplayAreaRects.bottom.width,
   33. cutOutInfo->waterfallDisplayAreaRects.bottom.height);
   34. }
   35. napi_value boundingRectsLength;
   36. napi_create_int32(env, cutOutInfo->boundingRectsLength, &boundingRectsLength);
   37. OH_NativeDisplayManager_DestroyDefaultDisplayCutoutInfo(cutOutInfo);
   38. return boundingRectsLength;
   39. } else {
   40. napi_value errorCode;
   41. napi_create_int32(env, errCode, &errorCode);
   42. return errorCode;
   43. }
   44. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDisplayBasicSample/entry/src/main/cpp/napi_init.cpp#L45-L90)

## 监听屏幕状态变化

可以通过OH\_NativeDisplayManager\_RegisterDisplayChangeListener接口注册屏幕变化的监听，包括屏幕旋转、分辨率变化、刷新率变化、DPI变化等。 通过OH\_NativeDisplayManager\_UnregisterDisplayChangeListener接口取消屏幕状态变化的监听。

```
1. void DisplayChangeCallback(uint64_t displayId)
2. {
3. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "DMSTest",
4. "DisplayChangeCallback displayId=%{public}lu.", displayId);
5. }

7. static napi_value RegisterDisplayChangeListener(napi_env env, napi_callback_info info)
8. {
9. uint32_t listenerIndex;
10. NativeDisplayManager_ErrorCode errCode = OH_NativeDisplayManager_RegisterDisplayChangeListener(
11. DisplayChangeCallback, &listenerIndex);
12. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "DMSTest",
13. "RegisterDisplayChangeListener listenerIndex =%{public}d errCode=%{public}d.", listenerIndex, errCode);
14. if (errCode == NativeDisplayManager_ErrorCode::DISPLAY_MANAGER_OK) {
15. napi_value registerIndex;
16. napi_create_int32(env, listenerIndex, &registerIndex);
17. return registerIndex;
18. } else {
19. napi_value errorCode;
20. napi_create_int32(env, errCode, &errorCode);
21. return errorCode;
22. }
23. }

25. static napi_value UnregisterDisplayChangeListener(napi_env env, napi_callback_info info)
26. {
27. size_t argc = 1;
28. napi_value args[1] = { nullptr };

30. uint32_t listenerIndex;
31. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
32. napi_get_value_uint32(env, args[0], &listenerIndex);
33. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "DMSTest",
34. "UnregisterDisplayChangeListener listenerIndex =%{public}d.", listenerIndex);
35. NativeDisplayManager_ErrorCode errCode = OH_NativeDisplayManager_UnregisterDisplayChangeListener(listenerIndex);
36. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "DMSTest",
37. "UnregisterDisplayChangeListener errCode=%{public}d.", errCode);
38. napi_value errorCode;
39. napi_create_int32(env, errCode, &errorCode);
40. return errorCode;
41. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDisplayBasicSample/entry/src/main/cpp/napi_init.cpp#L92-L134)

## 监听折叠设备状态变化

1. 可以通过OH\_NativeDisplayManager\_IsFoldable接口查询设备是不是折叠设备。

   ```
   1. static napi_value IsFoldable(napi_env env, napi_callback_info info)
   2. {
   3. bool isFoldDevice = OH_NativeDisplayManager_IsFoldable();
   4. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "DMSTest", "IsFoldable isFoldDevice =%{public}d.", isFoldDevice);
   5. napi_value isFold;
   6. napi_get_boolean(env, isFoldDevice, &isFold);
   7. return isFold;
   8. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDisplayBasicSample/entry/src/main/cpp/napi_init.cpp#L136-L145)
2. 可以通过OH\_NativeDisplayManager\_RegisterFoldDisplayModeChangeListener注册屏幕展开/折叠状态变化的监听。 通过OH\_NativeDisplayManager\_UnregisterFoldDisplayModeChangeListener接口取消屏幕展开/折叠状态变化的监听。

   ```
   1. void FoldDisplayModeChangeCallback(NativeDisplayManager_FoldDisplayMode displayMode)
   2. {
   3. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "DMSTest", "displayMode=%{public}d.", displayMode);
   4. }

   6. static napi_value RegisterFoldDisplayModeChangeListener(napi_env env, napi_callback_info info)
   7. {
   8. uint32_t listenerIndex = 0;
   9. NativeDisplayManager_ErrorCode errCode = OH_NativeDisplayManager_RegisterFoldDisplayModeChangeListener(
   10. FoldDisplayModeChangeCallback, &listenerIndex);
   11. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "DMSTest", "listenerIndex =%{public}d errCode=%{public}d.",
   12. listenerIndex, errCode);
   13. if (errCode == NativeDisplayManager_ErrorCode::DISPLAY_MANAGER_OK) {
   14. napi_value registerIndex;
   15. napi_create_int32(env, listenerIndex, &registerIndex);
   16. return registerIndex;
   17. } else {
   18. napi_value errorCode;
   19. napi_create_int32(env, errCode, &errorCode);
   20. return errorCode;
   21. }
   22. }

   24. static napi_value UnregisterFoldDisplayModeChangeListener(napi_env env, napi_callback_info info)
   25. {
   26. size_t argc = 1;
   27. napi_value args[1] = { nullptr };
   28. uint32_t listenerIndex;
   29. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   30. napi_get_value_uint32(env, args[0], &listenerIndex);
   31. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "DMSTest", "listenerIndex =%{public}d.", listenerIndex);
   32. NativeDisplayManager_ErrorCode errCode =
   33. OH_NativeDisplayManager_UnregisterFoldDisplayModeChangeListener(listenerIndex);
   34. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "DMSTest", "errorCode=%{public}d", errCode);
   35. napi_value errorCode;
   36. napi_create_int32(env, errCode, &errorCode);
   37. return errorCode;
   38. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDisplayBasicSample/entry/src/main/cpp/napi_init.cpp#L147-L186)

## 注册函数

```
1. EXTERN_C_START
2. static napi_value Init(napi_env env, napi_value exports)
3. {
4. napi_property_descriptor desc[] = {
5. {"getDisplayRotation", nullptr, GetDefaultDisplayRotation, nullptr, nullptr, nullptr, napi_default, nullptr},
6. {"getCutoutInfo", nullptr, CreateDefaultDisplayCutoutInfo, nullptr, nullptr, nullptr, napi_default, nullptr},
7. {"registerDisplayChange", nullptr, RegisterDisplayChangeListener,
8. nullptr, nullptr, nullptr, napi_default, nullptr},
9. {"unregisterDisplayChange", nullptr, UnregisterDisplayChangeListener,
10. nullptr, nullptr, nullptr, napi_default, nullptr},
11. {"checkIsFoldDevice", nullptr, IsFoldable, nullptr, nullptr, nullptr, napi_default, nullptr},
12. {"registerFoldDisplayModeChange", nullptr, RegisterFoldDisplayModeChangeListener,
13. nullptr, nullptr, nullptr, napi_default, nullptr},
14. {"unregisterFoldDisplayModeChange", nullptr, UnregisterFoldDisplayModeChangeListener,
15. nullptr, nullptr, nullptr, napi_default, nullptr},
16. };
17. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
18. return exports;
19. }
20. EXTERN_C_END
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDisplayBasicSample/entry/src/main/cpp/napi_init.cpp#L188-L209)

## 注册模块

```
1. static napi_module displayModule = {
2. .nm_version = 1,
3. .nm_flags = 0,
4. .nm_filename = nullptr,
5. .nm_register_func = Init,
6. .nm_modname = "nativedisplay",
7. .nm_priv = ((void*)0),
8. .reserved = { 0 },
9. };

11. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
12. {
13. napi_module_register(&displayModule);
14. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDisplayBasicSample/entry/src/main/cpp/napi_init.cpp#L211-L226)

```
1. static napi_module displayModule = {
2. .nm_version = 1,
3. .nm_flags = 0,
4. .nm_filename = nullptr,
5. .nm_register_func = Init,
6. .nm_modname = "nativedisplay",
7. .nm_priv = ((void*)0),
8. .reserved = { 0 },
9. };

11. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
12. {
13. napi_module_register(&displayModule);
14. }
```

## 在Index.ets文件中调用函数

```
1. private callGetDisplayRotation(): void {
2. this.promptAction.openToast({ message: '调用getDisplayRotation方法' }).catch((error: Error) => {
3. console.error(`callGetDisplayRotation error ${JSON.stringify(error)}`);
4. }).then(() => {
5. console.info(`get rotation value is: ${displayNapi.getDisplayRotation()}`);
6. });
7. }

9. private callFoldableCallback(): void {
10. this.promptAction.openToast({ message: '调用register displayMode方法' }).catch((error: Error) => {
11. console.error(`callFoldableCallback error ${JSON.stringify(error)}`);
12. }).then(() => {
13. let registerIndex = displayNapi.registerFoldDisplayModeChange();
14. console.info(`register foldable value is: ${registerIndex}`);
15. console.info(`unregister foldable value is: ${displayNapi.unregisterFoldDisplayModeChange(registerIndex)}`);
16. });
17. }

19. private callGetCutoutInfo(): void {
20. this.promptAction.openToast({ message: '调用getCutoutInfo方法' }).catch((error: Error) => {
21. console.error(`callGetCutoutInfo error ${JSON.stringify(error)}`);
22. }).then(() => {
23. console.info(`cutoutInfo length is: ${displayNapi.getCutoutInfo()}`);
24. });
25. }

27. private callDealListenCallback(): void {
28. this.promptAction.openToast({ message: '调用register change方法' }).catch((error: Error) => {
29. console.error(`callDealListenCallback error ${JSON.stringify(error)}`);
30. }).then(() => {
31. let registerIndex = displayNapi.registerDisplayChange();
32. console.info(`register display change value is: ${registerIndex}`);
33. console.info(`unregister display change value is: ${displayNapi.unregisterDisplayChange(registerIndex)}`);
34. });
35. }

37. private callDealFoldableDevice(): void {
38. this.promptAction.openToast({ message: '调用dealFoldableDevice方法' }).catch((error: Error) => {
39. console.error(`callDealFoldableDevice error ${JSON.stringify(error)}`);
40. }).then(() => {
41. console.info(`fold device is: ${displayNapi.checkIsFoldDevice()}`);
42. });
43. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDisplayBasicSample/entry/src/main/ets/pages/Index.ets#L53-L97)
