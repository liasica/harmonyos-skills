---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-bundle-guidelines
title: NativeBundle开发指导
breadcrumb: 指南 > NDK开发 > 代码开发 > 包管理 > NativeBundle开发指导
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0539596f180a2e53193fa4414dba34b9c06002c809c0ae098b95a4cc36f41d01
---

## 场景介绍

开发者可以通过本指导了解在HarmonyOS应用中，如何使用Native Bundle接口获取应用自身相关信息。

## 接口说明

常用接口如下表所示，具体API说明详见[Native\_Bundle](../harmonyos-references/capi-native-bundle.md)。

| 接口名 | 描述 |
| --- | --- |
| [OH\_NativeBundle\_GetCurrentApplicationInfo](../harmonyos-references/capi-native-interface-bundle-h.md#oh_nativebundle_getcurrentapplicationinfo) | 获取应用自身相关信息。 |
| [OH\_NativeBundle\_GetAppId](../harmonyos-references/capi-native-interface-bundle-h.md#oh_nativebundle_getappid) | 获取自身应用的appId信息。 |
| [OH\_NativeBundle\_GetAppIdentifier](../harmonyos-references/capi-native-interface-bundle-h.md#oh_nativebundle_getappidentifier) | 获取自身应用的appIdentifier信息。 |
| [OH\_NativeBundle\_GetMainElementName](../harmonyos-references/capi-native-interface-bundle-h.md#oh_nativebundle_getmainelementname) | 获取自身应用入口的信息。 |
| [OH\_NativeBundle\_GetCompatibleDeviceType](../harmonyos-references/capi-native-interface-bundle-h.md#oh_nativebundle_getcompatibledevicetype) | 获取自身应用适用的设备类型。 |
| [OH\_NativeBundle\_IsDebugMode](../harmonyos-references/capi-native-interface-bundle-h.md#oh_nativebundle_isdebugmode) | 查询当前应用的调试模式。从API version 20开始支持。 |
| [OH\_NativeBundle\_GetModuleMetadata](../harmonyos-references/capi-native-interface-bundle-h.md#oh_nativebundle_getmodulemetadata) | 获取当前应用的元数据信息。从API version 20开始支持。 |
| [OH\_NativeBundle\_GetAbilityResourceInfo](../harmonyos-references/capi-native-interface-bundle-h.md#oh_nativebundle_getabilityresourceinfo) | 获取支持打开特定文件类型的组件资源信息列表。从API version 21开始支持。 |

## 开发步骤

**1. 创建工程**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/_PJUGgegSxCWJEZByGkpFw/zh-cn_image_0000002558606232.png?HW-CC-KV=V1&HW-CC-Date=20260429T054427Z&HW-CC-Expire=86400&HW-CC-Sign=41AF3BC845AD71A591501683AE089D63DCDD5A8491248CCFEB8CD5A60BCDA70B)

**2. 添加依赖**

创建完成后，DevEco Studio会在工程生成cpp目录，目录中包含types/libentry/index.d.ts、napi\_init.cpp、CMakeLists.txt等文件。

1. 打开src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加包管理的libbundle\_ndk.so。

   ```
   1. target_link_libraries(entry PUBLIC libace_napi.z.so libbundle_ndk.so)
   ```
2. 打开src/main/cpp/napi\_init.cpp文件，添加头文件。

   ```
   1. // napi依赖头文件
   2. #include "napi/native_api.h"
   3. // native接口依赖头文件
   4. #include "bundle/ability_resource_info.h"
   5. #include "bundle/native_interface_bundle.h"
   6. // free()函数依赖的基础库
   7. #include <cstdlib>
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/NativeBundleGuidelines/entry/src/main/cpp/napi_init.cpp#L16-L24)

**3. 修改源文件**

1. 打开src/main/cpp/napi\_init.cpp文件，文件Init会对当前方法进行初始化映射，这里定义对外的接口。

   ```
   1. EXTERN_C_START
   2. static napi_value Init(napi_env env, napi_value exports)
   3. {
   4. napi_property_descriptor desc[] = {
   5. { "add", nullptr, Add, nullptr, nullptr, nullptr, napi_default, nullptr },
   6. // 新增方法getCurrentApplicationInfo
   7. { "getCurrentApplicationInfo", nullptr, GetCurrentApplicationInfo, nullptr,
   8. nullptr, nullptr, napi_default, nullptr},
   9. // 新增方法getAppId
   10. { "getAppId", nullptr, GetAppId, nullptr, nullptr, nullptr, napi_default, nullptr},
   11. // 新增方法getAppIdentifier
   12. { "getAppIdentifier", nullptr, GetAppIdentifier, nullptr, nullptr, nullptr, napi_default, nullptr},
   13. // 新增方法getMainElementName
   14. { "getMainElementName", nullptr, GetMainElementName, nullptr, nullptr, nullptr, napi_default, nullptr},
   15. // 新增方法getCompatibleDeviceType
   16. { "getCompatibleDeviceType", nullptr, GetCompatibleDeviceType, nullptr,
   17. nullptr, nullptr, napi_default, nullptr},
   18. // 新增方法isDebugMode
   19. { "isDebugMode", nullptr, IsDebugMode, nullptr, nullptr, nullptr, napi_default, nullptr},
   20. // 新增方法getModuleMetadata
   21. { "getModuleMetadata", nullptr, GetModuleMetadata, nullptr, nullptr, nullptr, napi_default, nullptr},
   22. // 新增方法getAbilityResourceInfo
   23. { "getAbilityResourceInfo", nullptr, GetAbilityResourceInfo, nullptr, nullptr, nullptr, napi_default, nullptr}
   24. };
   25. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   26. return exports;
   27. }
   28. EXTERN_C_END
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/NativeBundleGuidelines/entry/src/main/cpp/napi_init.cpp#L381-L410)
2. 在src/main/cpp/napi\_init.cpp文件中获取Native的包信息对象，并转为js的包信息对象，即可在js侧获取应用的信息：

   ```
   1. static napi_value GetCurrentApplicationInfo(napi_env env, napi_callback_info info)
   2. {
   3. // 调用Native接口获取应用信息
   4. OH_NativeBundle_ApplicationInfo nativeApplicationInfo = OH_NativeBundle_GetCurrentApplicationInfo();
   5. napi_value result = nullptr;
   6. napi_create_object(env, &result);
   7. // Native接口获取的应用包名转为js对象里的bundleName属性
   8. napi_value bundleName;
   9. napi_create_string_utf8(env, nativeApplicationInfo.bundleName, NAPI_AUTO_LENGTH, &bundleName);
   10. napi_set_named_property(env, result, "bundleName", bundleName);
   11. // Native接口获取的指纹信息转为js对象里的fingerprint属性
   12. napi_value fingerprint;
   13. napi_create_string_utf8(env, nativeApplicationInfo.fingerprint, NAPI_AUTO_LENGTH, &fingerprint);
   14. napi_set_named_property(env, result, "fingerprint", fingerprint);
   15. // 最后为了防止内存泄漏，手动释放
   16. free(nativeApplicationInfo.bundleName);
   17. free(nativeApplicationInfo.fingerprint);
   18. return result;
   19. }

   21. static napi_value GetAppId(napi_env env, napi_callback_info info)
   22. {
   23. // 调用Native接口获取应用appId
   24. char* appId = OH_NativeBundle_GetAppId();
   25. // Native接口转成nAppId返回
   26. napi_value nAppId;
   27. napi_create_string_utf8(env, appId, NAPI_AUTO_LENGTH, &nAppId);
   28. // 最后为了防止内存泄漏，手动释放
   29. free(appId);
   30. return nAppId;
   31. }

   33. static napi_value GetAppIdentifier(napi_env env, napi_callback_info info)
   34. {
   35. // 调用Native接口获取应用appIdentifier
   36. char* appIdentifier = OH_NativeBundle_GetAppIdentifier();
   37. // Native接口转成nAppIdentifier返回
   38. napi_value nAppIdentifier;
   39. napi_create_string_utf8(env, appIdentifier, NAPI_AUTO_LENGTH, &nAppIdentifier);
   40. // 最后为了防止内存泄漏，手动释放
   41. free(appIdentifier);
   42. return nAppIdentifier;
   43. }

   45. static napi_value GetMainElementName(napi_env env, napi_callback_info info)
   46. {
   47. // 调用Native接口获取应用入口的信息
   48. OH_NativeBundle_ElementName elementName = OH_NativeBundle_GetMainElementName();
   49. napi_value result = nullptr;
   50. napi_create_object(env, &result);
   51. // Native接口获取的应用包名转为js对象里的bundleName属性
   52. napi_value bundleName;
   53. napi_create_string_utf8(env, elementName.bundleName, NAPI_AUTO_LENGTH, &bundleName);
   54. napi_set_named_property(env, result, "bundleName", bundleName);
   55. // Native接口获取的模块名称转为js对象里的moduleName属性
   56. napi_value moduleName;
   57. napi_create_string_utf8(env, elementName.moduleName, NAPI_AUTO_LENGTH, &moduleName);
   58. napi_set_named_property(env, result, "moduleName", moduleName);
   59. // Native接口获取的ability名称转为js对象里的abilityName属性
   60. napi_value abilityName;
   61. napi_create_string_utf8(env, elementName.abilityName, NAPI_AUTO_LENGTH, &abilityName);
   62. napi_set_named_property(env, result, "abilityName", abilityName);
   63. // 最后为了防止内存泄漏，手动释放
   64. free(elementName.bundleName);
   65. free(elementName.moduleName);
   66. free(elementName.abilityName);
   67. return result;
   68. }

   70. static napi_value GetCompatibleDeviceType(napi_env env, napi_callback_info info)
   71. {
   72. // 调用Native接口获取应用deviceType
   73. char* deviceType = OH_NativeBundle_GetCompatibleDeviceType();
   74. // Native接口转成nDeviceType返回
   75. napi_value nDeviceType;
   76. napi_create_string_utf8(env, deviceType, NAPI_AUTO_LENGTH, &nDeviceType);
   77. // 最后为了防止内存泄漏，手动释放
   78. free(deviceType);
   79. return nDeviceType;
   80. }

   82. static napi_value IsDebugMode(napi_env env, napi_callback_info info)
   83. {
   84. bool isDebug = false;
   85. // 调用Native接口获取应用DebugMode的信息，该接口从API version 20开始支持
   86. bool isSuccess = OH_NativeBundle_IsDebugMode(&isDebug);
   87. // 调用Native接口失败抛出异常
   88. if (isSuccess == false) {
   89. napi_throw_error(env, nullptr, "call failed");
   90. return nullptr;
   91. }
   92. // Native接口转成debug返回
   93. napi_value debug;
   94. napi_get_boolean(env, isDebug, &debug);
   95. return debug;
   96. }

   98. static napi_value GetModuleMetadata(napi_env env, napi_callback_info info)
   99. {
   100. size_t moduleCount = 0;
   101. // 调用Native接口获取应用元数据的信息，该接口从API version 20开始支持
   102. OH_NativeBundle_ModuleMetadata* modules = OH_NativeBundle_GetModuleMetadata(&moduleCount);
   103. if (modules == nullptr || moduleCount == 0) {
   104. napi_throw_error(env, nullptr, "no metadata found");
   105. return nullptr;
   106. }
   107. napi_value result;
   108. napi_create_array(env, &result);
   109. for (size_t i = 0; i < moduleCount; i++) {
   110. napi_value moduleObj;
   111. napi_create_object(env, &moduleObj);
   112. // Native接口获取的模块名转为js对象里的moduleName属性
   113. napi_value moduleName;
   114. napi_create_string_utf8(env, modules[i].moduleName, NAPI_AUTO_LENGTH, &moduleName);
   115. napi_set_named_property(env, moduleObj, "moduleName", moduleName);
   116. napi_value metadataArray;
   117. napi_create_array(env, &metadataArray);
   118. for (size_t j = 0; j < modules[i].metadataArraySize; j++) {
   119. napi_value metadataObj;
   120. napi_create_object(env, &metadataObj);
   121. napi_value name;
   122. napi_value value;
   123. napi_value resource;
   124. napi_create_string_utf8(env, modules[i].metadataArray[j].name, NAPI_AUTO_LENGTH, &name);
   125. napi_create_string_utf8(env, modules[i].metadataArray[j].value, NAPI_AUTO_LENGTH, &value);
   126. napi_create_string_utf8(env, modules[i].metadataArray[j].resource, NAPI_AUTO_LENGTH, &resource);
   127. // Native接口获取的元数据名称转为js对象里的name属性
   128. napi_set_named_property(env, metadataObj, "name", name);
   129. // Native接口获取的元数据值名称转为js对象里的value属性
   130. napi_set_named_property(env, metadataObj, "value", value);
   131. // Native接口获取的元数据资源转为js对象里的resource属性
   132. napi_set_named_property(env, metadataObj, "resource", resource);
   133. napi_set_element(env, metadataArray, j, metadataObj);
   134. }
   135. napi_set_named_property(env, moduleObj, "metadata", metadataArray);
   136. napi_set_element(env, result, i, moduleObj);
   137. }
   138. // 最后为了防止内存泄漏，手动释放
   139. for (size_t i = 0; i < moduleCount; i++) {
   140. free(modules[i].moduleName);
   141. for (size_t j = 0; j < modules[i].metadataArraySize; j++) {
   142. free(modules[i].metadataArray[j].name);
   143. free(modules[i].metadataArray[j].value);
   144. free(modules[i].metadataArray[j].resource);
   145. }
   146. free(modules[i].metadataArray);
   147. }
   148. free(modules);
   149. return result;
   150. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/NativeBundleGuidelines/entry/src/main/cpp/napi_init.cpp#L51-L202)

   ```
   1. static void AddDefaultApp(napi_env env,
   2. napi_value &infoObj,
   3. OH_NativeBundle_AbilityResourceInfo* temp)
   4. {
   5. bool isDefaultApp = true;
   6. // 该接口从API version 21开始支持
   7. OH_NativeBundle_CheckDefaultApp(temp, &isDefaultApp);
   8. napi_value defaultAppValue;
   9. napi_get_boolean(env, isDefaultApp, &defaultAppValue);
   10. napi_set_named_property(env, infoObj, "isDefaultApp", defaultAppValue);
   11. }

   13. static void AddAppIndex(napi_env env,
   14. napi_value &infoObj,
   15. OH_NativeBundle_AbilityResourceInfo* temp)
   16. {
   17. int appIndex = -1;
   18. // 该接口从API version 21开始支持
   19. OH_NativeBundle_GetAppIndex(temp, &appIndex);
   20. napi_value appIndexValue;
   21. napi_create_int32(env, appIndex, &appIndexValue);
   22. napi_set_named_property(env, infoObj, "appIndex", appIndexValue);
   23. }

   25. static void AddLabel(napi_env env,
   26. napi_value &infoObj,
   27. OH_NativeBundle_AbilityResourceInfo* temp)
   28. {
   29. char *label = nullptr;
   30. // 该接口从API version 21开始支持
   31. OH_NativeBundle_GetLabel(temp, &label);
   32. napi_value labelValue;
   33. if (label) {
   34. napi_create_string_utf8(env, label, NAPI_AUTO_LENGTH, &labelValue);
   35. free(label);
   36. } else {
   37. napi_get_null(env, &labelValue);
   38. }
   39. napi_set_named_property(env, infoObj, "label", labelValue);
   40. }

   42. static void AddBundleName(napi_env env,
   43. napi_value &infoObj,
   44. OH_NativeBundle_AbilityResourceInfo* temp)
   45. {
   46. char *bundleName = nullptr;
   47. // 该接口从API version 21开始支持
   48. OH_NativeBundle_GetBundleName(temp, &bundleName);
   49. napi_value bundleNameValue;
   50. if (bundleName) {
   51. napi_create_string_utf8(env, bundleName, NAPI_AUTO_LENGTH, &bundleNameValue);
   52. free(bundleName);
   53. } else {
   54. napi_get_null(env, &bundleNameValue);
   55. }
   56. napi_set_named_property(env, infoObj, "bundleName", bundleNameValue);
   57. }

   59. static void AddModuleName(napi_env env,
   60. napi_value &infoObj,
   61. OH_NativeBundle_AbilityResourceInfo* temp)
   62. {
   63. char *moduleName = nullptr;
   64. // 该接口从API version 21开始支持
   65. OH_NativeBundle_GetModuleName(temp, &moduleName);
   66. napi_value moduleNameValue;
   67. if (moduleName) {
   68. napi_create_string_utf8(env, moduleName, NAPI_AUTO_LENGTH, &moduleNameValue);
   69. free(moduleName);
   70. } else {
   71. napi_get_null(env, &moduleNameValue);
   72. }
   73. napi_set_named_property(env, infoObj, "moduleName", moduleNameValue);
   74. }

   76. static void AddAbilityName(napi_env env,
   77. napi_value &infoObj,
   78. OH_NativeBundle_AbilityResourceInfo* temp)
   79. {
   80. char *abilityName = nullptr;
   81. // 该接口从API version 21开始支持
   82. OH_NativeBundle_GetAbilityName(temp, &abilityName);
   83. napi_value abilityNameValue;
   84. if (abilityName) {
   85. napi_create_string_utf8(env, abilityName, NAPI_AUTO_LENGTH, &abilityNameValue);
   86. free(abilityName);
   87. } else {
   88. napi_get_null(env, &abilityNameValue);
   89. }
   90. napi_set_named_property(env, infoObj, "abilityName", abilityNameValue);
   91. }

   93. static void GetDrawableDescriptor(
   94. OH_NativeBundle_AbilityResourceInfo* temp)
   95. {
   96. ArkUI_DrawableDescriptor *rawDrawable = nullptr;
   97. // 该接口从API version 21开始支持
   98. OH_NativeBundle_GetDrawableDescriptor(temp, &rawDrawable);
   99. if (rawDrawable) {
   100. // 使用ArkUI_DrawableDescriptor对象绘制图标
   101. }
   102. }

   104. static void AssemblyAbilityResourceInfo(napi_env env,
   105. napi_value &infoObj,
   106. OH_NativeBundle_AbilityResourceInfo* temp)
   107. {
   108. // 1. 添加Default App
   109. AddDefaultApp(env, infoObj, temp);
   110. // 2. 添加App Index
   111. AddAppIndex(env, infoObj, temp);
   112. // 3. 添加Label
   113. AddLabel(env, infoObj, temp);
   114. // 4. 添加Bundle Name
   115. AddBundleName(env, infoObj, temp);
   116. // 5. 添加Module Name
   117. AddModuleName(env, infoObj, temp);
   118. // 6. 添加Ability Name
   119. AddAbilityName(env, infoObj, temp);
   120. // 7. 获取ArkUI_DrawableDescriptor对象
   121. GetDrawableDescriptor(temp);
   122. }

   124. static napi_value GetAbilityResourceInfo(napi_env env, napi_callback_info info)
   125. {
   126. size_t argc = 1;
   127. napi_value args[1];
   128. napi_status status;
   129. // 获取传入的参数
   130. status = napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   131. if (status != napi_ok || argc < 1) {
   132. napi_throw_error(env, nullptr, "Invalid arguments. Expected fileType string.");
   133. return nullptr;
   134. }
   135. // 检查参数类型是否为字符串
   136. napi_valuetype valuetype;
   137. status = napi_typeof(env, args[0], &valuetype);
   138. if (status != napi_ok || valuetype != napi_string) {
   139. napi_throw_error(env, nullptr, "Argument must be a string");
   140. return nullptr;
   141. }
   142. // 获取字符串参数
   143. char fileType[256] = {0}; // 假设文件类型不会超过255个字符
   144. size_t strLen;
   145. status = napi_get_value_string_utf8(env, args[0], fileType, sizeof(fileType) - 1, &strLen);
   146. if (status != napi_ok) {
   147. napi_throw_error(env, nullptr, "Failed to get fileType string");
   148. return nullptr;
   149. }
   150. size_t infosCount = 0;
   151. OH_NativeBundle_AbilityResourceInfo *infos = nullptr;
   152. // 调用Native接口获取组件资源信息，使用传入的fileType，该接口从API version 21开始支持
   153. BundleManager_ErrorCode ret = OH_NativeBundle_GetAbilityResourceInfo(fileType, &infos, &infosCount);
   154. if (ret == BUNDLE_MANAGER_ERROR_CODE_PERMISSION_DENIED) {
   155. napi_throw_error(env, nullptr, "BUNDLE_MANAGER_ERROR_CODE_PERMISSION_DENIED");
   156. return nullptr;
   157. }
   158. if (infos == nullptr || infosCount == 0) {
   159. napi_throw_error(env, nullptr, "no metadata found");
   160. return nullptr;
   161. }
   162. napi_value result;
   163. napi_create_array(env, &result);
   164. for (size_t i = 0; i < infosCount; i++) {
   165. auto temp = (OH_NativeBundle_AbilityResourceInfo *)((char *)infos + OH_NativeBundle_GetSize() * i);
   166. napi_value infoObj;
   167. napi_create_object(env, &infoObj);
   168. AssemblyAbilityResourceInfo(env, infoObj, temp);
   169. napi_set_element(env, result, i, infoObj);
   170. }
   171. // 释放内存，该接口从API version 21开始支持
   172. OH_AbilityResourceInfo_Destroy(infos, infosCount);
   173. return result;
   174. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/NativeBundleGuidelines/entry/src/main/cpp/napi_init.cpp#L204-L379)

**4. 接口暴露**

1. 在src/main/cpp/types/libentry/Index.d.ts文件中，声明暴露接口。

   ```
   1. export const add: (a: number, b: number) => number;
   2. export const getCurrentApplicationInfo: () => object;   // 新增暴露方法 getCurrentApplicationInfo
   3. export const getAppId: () => string;                    // 新增暴露方法 getAppId
   4. export const getAppIdentifier: () => string;            // 新增暴露方法 getAppIdentifier
   5. export const getMainElementName: () => object;          // 新增暴露方法 getMainElementName
   6. export const getCompatibleDeviceType: () => string;     // 新增暴露方法 getCompatibleDeviceType
   7. export const isDebugMode: () => boolean;                // 新增暴露方法 isDebugMode
   8. export const getModuleMetadata: () => object;           // 新增暴露方法 getModuleMetadata
   9. export const getAbilityResourceInfo: (fileType: string) => object;      // 新增暴露方法 getAbilityResourceInfo
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/NativeBundleGuidelines/entry/src/main/cpp/types/libentry/Index.d.ts#L15-L25)

**5. js侧调用**

1. 打开src/main/ets/pages/Index.ets，导入"libentry.so"，调用Native接口打印出获取的信息内容。示例如下：

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';
   2. import testNapi from 'libentry.so';

   4. const DOMAIN = 0x0000;

   6. @Entry
   7. @Component
   8. struct Index {
   9. @State message: string = 'Hello World';

   11. build() {
   12. Row() {
   13. Column() {
   14. Text(this.message)
   15. .fontSize($r('app.float.page_text_font_size'))
   16. .fontWeight(FontWeight.Bold)
   17. .onClick(() => {
   18. this.message = 'Welcome';
   19. hilog.info(DOMAIN, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(2, 3));
   20. let appInfo = testNapi.getCurrentApplicationInfo();
   21. console.info("bundleNative getCurrentApplicationInfo success, data is " + JSON.stringify(appInfo));
   22. let appId = testNapi.getAppId();
   23. console.info("bundleNative getAppId success, appId is " + appId);
   24. let appIdentifier = testNapi.getAppIdentifier();
   25. console.info("bundleNative getAppIdentifier success, appIdentifier is " + appIdentifier);
   26. let mainElement = testNapi.getMainElementName();
   27. console.info("bundleNative getMainElementName success, data is " + JSON.stringify(mainElement));
   28. let deviceType = testNapi.getCompatibleDeviceType();
   29. console.info("bundleNative getCompatibleDeviceType success, deviceType is " + deviceType);
   30. let isDebugMode = testNapi.isDebugMode();
   31. console.info("bundleNative isDebugMode success, isDebugMode is " + isDebugMode);
   32. let moduleMetadata = testNapi.getModuleMetadata();
   33. console.info("bundleNative getModuleMetadata success, data is " + JSON.stringify(moduleMetadata));
   34. let fileType: string = '.png';
   35. let abilityResourceInfo = testNapi.getAbilityResourceInfo(fileType);
   36. console.info("bundleNative getAbilityResourceInfo success, data is " + JSON.stringify(abilityResourceInfo));
   37. })
   38. }
   39. .width('100%')
   40. }
   41. .height('100%')
   42. }
   43. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/NativeBundleGuidelines/entry/src/main/ets/pages/Index.ets#L16-L60)

关于包管理NDK接口说明，可参考[Native\_Bundle模块介绍](../harmonyos-references/capi-native-bundle.md)。
