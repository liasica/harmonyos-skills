---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkweb-ndk-jsbridge
title: 应用侧与前端页面的相互调用(C/C++)
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 在应用中使用前端页面JavaScript > 应用侧与前端页面的相互调用(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:add98b7db6a57a16560e306d3cdc44f98ab670609da3b588a841e0ae2d2e9f65
---

本指导适用于ArkWeb应用侧与前端网页通信场景，开发者可根据应用架构选择使用ArkWeb Native接口完成业务通信机制（以下简称Native JSBridge）。

针对JSBridge进行性能优化可参考[JSBridge优化解决方案](../best-practices/bpta-web-develop-optimization.md#section58781855115017)

## 适用的应用架构

应用使用ArkTS、C++语言混合开发，或本身应用架构较贴近于小程序架构，自带C++侧环境，推荐使用ArkWeb在Native侧提供的[ArkWeb\_ControllerAPI](../harmonyos-references/capi-web-arkweb-controllerapi.md)、[ArkWeb\_ComponentAPI](../harmonyos-references/capi-web-arkweb-componentapi.md)实现JSBridge功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/Uo-ZZQhGQ1eNT9buxd9QFw/zh-cn_image_0000002558764704.png?HW-CC-KV=V1&HW-CC-Date=20260429T052916Z&HW-CC-Expire=86400&HW-CC-Sign=0ED2DE6B92D281CFE737B5DA2D596B87E2C28A940458CC48C6C8E1DE64FB54F5)

上图展示了具有普遍适用性的小程序的通用架构。在这一架构中，逻辑层依赖于应用程序自带的JavaScript运行时，该运行时在一个已有的C++环境中运行。通过Native接口，逻辑层能够直接在C++环境中与视图层（其中ArkWeb充当渲染器）进行通信，无需回退至ArkTS环境使用ArkTS JSBridge接口。

左图是使用ArkTS JSBridge接口构建小程序的方案，如红框所示，应用需要先调用到ArkTS环境，再调用到C++环境。右图是使用Native JSBridge接口构建小程序的方案，不需要ArkTS环境和C++环境的切换，执行效率更高。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/GOE7WJtcS8KDcZAigeHrWg/zh-cn_image_0000002558605050.png?HW-CC-KV=V1&HW-CC-Date=20260429T052916Z&HW-CC-Expire=86400&HW-CC-Sign=9CA85FC360A007E6764FB96664EFB44A98C4784838BABA0BA669A677062D0765)

Native JSBridge方案解决了ArkTS环境的冗余切换，同时允许回调在非UI线程上运行，避免造成UI阻塞。

## 使用Native接口实现JSBridge通信（推荐）

原先，Native同步接口不支持返回值，其返回类型固定为void。然而，为满足业务扩展需求，自API version 18起，引入了替代接口，支持bool、string类型的返回值。

另外针对同步接口[registerJavaScriptProxyEx](../harmonyos-references/capi-web-arkweb-controllerapi.md#registerjavascriptproxyex)和异步接口[registerAsyncJavaScriptProxyEx](../harmonyos-references/capi-web-arkweb-controllerapi.md#registerasyncjavascriptproxyex)，新增了参数[permission](arkweb-ndk-jsbridge.md#前端页面调用应用侧函数)字段，用于调用权限控制。

### 接口替代关系

| 不推荐的接口 | 替代接口 | 说明 |
| --- | --- | --- |
| ArkWeb\_OnJavaScriptProxyCallback | ArkWeb\_OnJavaScriptProxyCallbackWithResult | Proxy方法被执行的回调。 |
| ArkWeb\_ProxyMethod | ArkWeb\_ProxyMethodWithResult | 注入的Proxy方法通用结构体。 |
| ArkWeb\_ProxyObject | ArkWeb\_ProxyObjectWithResult | 注入的Proxy对象通用结构体。 |
| registerJavaScriptProxy | registerJavaScriptProxyEx | 注入JavaScript对象到window对象中，并在window对象中调用该对象的同步方法。 |
| registerAsyncJavaScriptProxy | registerAsyncJavaScriptProxyEx | 注入JavaScript对象到window对象中，并在window对象中调用该对象的异步方法。 |

### 使用Native接口绑定ArkWeb

* ArkWeb组件声明在ArkTS侧，需要用户自定义一个标识webTag，并将webTag通过Node-API传至应用Native侧，后续ArkWeb Native接口使用，均需webTag作为对应组件的唯一标识。
* ArkTS侧

  ```
  1. // 自定义webTag，在WebviewController创建时作为入参传入，建立controller与webTag的映射关系
  2. webTag: string = 'ArkWeb1';
  3. controller: webview.WebviewController = new webview.WebviewController(this.webTag);
  4. // ...
  5. // 在aboutToAppear方法中，通过Node-API接口将webTag传入C++侧，C++侧使用webTag作为ArkWeb组件的唯一标识
  6. aboutToAppear() {
  7. console.info('aboutToAppear');
  8. //初始化web Native Development Kit
  9. testNapi.nativeWebInit(this.webTag);
  10. }
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseFrontendJSApp/entry4/src/main/ets/pages/Index.ets#L39-L52)
* C++侧

  ```
  1. // 解析存储webTag
  2. static napi_value NativeWebInit(napi_env env, napi_callback_info info)
  3. {
  4. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "Native Development Kit NativeWebInit start");
  5. size_t argc = 1;
  6. napi_value args[1] = {nullptr};
  7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
  8. // 获取第一个参数webTag
  9. size_t webTagSize = 0;
  10. napi_get_value_string_utf8(env, args[0], nullptr, 0, &webTagSize);
  11. char *webTagValue = new (std::nothrow) char[webTagSize + 1];
  12. size_t webTagLength = 0;
  13. napi_get_value_string_utf8(env, args[0], webTagValue, webTagSize + 1, &webTagLength);
  14. OH_LOG_Print(
  15. LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb",
  16. "Native Development Kit NativeWebInit webTag:%{public}s", webTagValue);

  18. // 将webTag保存在实例对象中
  19. jsbridge_object_ptr = std::make_shared<JSBridgeObject>(webTagValue);
  20. // ...
  21. }
  ```

  [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseFrontendJSApp/entry4/src/main/cpp/hello.cpp#L247-L296)

### 使用Native接口获取API结构体

在ArkWeb Native侧，需要先获取API结构体，才能调用结构体里的Native API。ArkWeb Native侧API通过函数[OH\_ArkWeb\_GetNativeAPI](../harmonyos-references/capi-arkweb-interface-h.md#oh_arkweb_getnativeapi)获取，根据入参type不同，可分别获取[ArkWeb\_ControllerAPI](../harmonyos-references/capi-web-arkweb-controllerapi.md)、[ArkWeb\_ComponentAPI](../harmonyos-references/capi-web-arkweb-componentapi.md)结构体。其中，[ArkWeb\_ControllerAPI](../harmonyos-references/capi-web-arkweb-controllerapi.md)对应ArkTS侧[web\_webview.WebviewController API](../harmonyos-references/arkts-apis-webview-webviewcontroller.md)，[ArkWeb\_ComponentAPI](../harmonyos-references/capi-web-arkweb-componentapi.md)对应ArkTS侧[ArkWeb组件API](../harmonyos-references/arkts-basic-components-web.md)。

```
1. static ArkWeb_ControllerAPI *controller = nullptr;
2. static ArkWeb_ComponentAPI *component = nullptr;
3. // ...
4. controller = reinterpret_cast<ArkWeb_ControllerAPI *>(OH_ArkWeb_GetNativeAPI(ARKWEB_NATIVE_CONTROLLER));
5. component = reinterpret_cast<ArkWeb_ComponentAPI *>(OH_ArkWeb_GetNativeAPI(ARKWEB_NATIVE_COMPONENT));
```

### Native侧注册组件生命周期回调

通过[ArkWeb\_ComponentAPI](../harmonyos-references/capi-web-arkweb-componentapi.md)注册组件生命周期回调，调用接口前，建议通过[ARKWEB\_MEMBER\_MISSING](../harmonyos-references/capi-arkweb-type-h.md#宏定义)校验该函数结构体中是否存在对应函数指针，以避免SDK与设备ROM不匹配导致crash问题。

```
1. if (!ARKWEB_MEMBER_MISSING(component, onControllerAttached)) {
2. component->onControllerAttached(
3. webTagValue, ValidCallback, static_cast<void *>(jsbridge_object_ptr->GetWeakPtr()));
4. } else {
5. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "component onControllerAttached func not exist");
6. }

8. if (!ARKWEB_MEMBER_MISSING(component, onPageBegin)) {
9. component->onPageBegin(webTagValue, LoadStartCallback, static_cast<void *>(jsbridge_object_ptr->GetWeakPtr()));
10. } else {
11. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "component onPageBegin func not exist");
12. }

14. if (!ARKWEB_MEMBER_MISSING(component, onPageEnd)) {
15. component->onPageEnd(webTagValue, LoadEndCallback, static_cast<void *>(jsbridge_object_ptr->GetWeakPtr()));
16. } else {
17. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "component onPageEnd func not exist");
18. }

20. if (!ARKWEB_MEMBER_MISSING(component, onDestroy)) {
21. component->onDestroy(webTagValue, DestroyCallback, static_cast<void *>(jsbridge_object_ptr->GetWeakPtr()));
22. } else {
23. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "component onDestroy func not exist");
24. }
```

[hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseFrontendJSApp/entry4/src/main/cpp/hello.cpp#L219-L244)

### 前端页面调用应用侧函数

通过[registerJavaScriptProxyEx](../harmonyos-references/capi-web-arkweb-controllerapi.md#registerjavascriptproxyex)将应用侧函数注册至前端页面，注册后在下次加载或者重新加载后生效。

```
1. // 注册对象
2. OH_LOG_Print(
3. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "Native Development Kit RegisterJavaScriptProxy begin");
4. ArkWeb_ProxyMethodWithResult method1 = {
5. "method1", ProxyMethod1, static_cast<void *>(jsbridge_object_ptr->GetWeakPtr())};
6. ArkWeb_ProxyMethodWithResult method2 = {
7. "method2", ProxyMethod2, static_cast<void *>(jsbridge_object_ptr->GetWeakPtr())};
8. ArkWeb_ProxyMethodWithResult methodList[2] = {method1, method2};
9. // 调用Native Development Kit接口注册对象
10. // 如此注册的情况下，在H5页面就可以使用proxy.method1、proxy.method1调用此文件下的ProxyMethod1和ProxyMethod2方法了
11. ArkWeb_ProxyObjectWithResult proxyObject = {"ndkProxy", methodList, 2};
12. controller->registerJavaScriptProxyEx(webTag, &proxyObject, "");
```

[hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseFrontendJSApp/entry4/src/main/cpp/hello.cpp#L135-L149)

* 参数permission是一个JSON字符串，示例如下：

```
1. {
2. "javascriptProxyPermission": {
3. "urlPermissionList": [       // Object级权限，如果匹配，所有Method都授权
4. {
5. "scheme": "resource",    // 精确匹配，不能为空
6. "host": "rawfile",       // 精确匹配，不能为空
7. "port": "",              // 精确匹配，为空不检查
8. "path": ""               // 前缀匹配，为空不检查
9. },
10. {
11. "scheme": "https",       // 精确匹配，不能为空
12. "host": "xxx.com",       // 精确匹配，不能为空
13. "port": "8080",          // 精确匹配，为空不检查
14. "path": "a/b/c"          // 前缀匹配，为空不检查
15. }
16. ],
17. "methodList": [
18. {
19. "methodName": "test",
20. "urlPermissionList": [   // Method级权限
21. {
22. "scheme": "https",   // 精确匹配，不能为空
23. "host": "xxx.com",   // 精确匹配，不能为空
24. "port": "",          // 精确匹配，为空不检查
25. "path": ""           // 前缀匹配，为空不检查
26. },
27. {
28. "scheme": "resource",// 精确匹配，不能为空
29. "host": "rawfile",   // 精确匹配，不能为空
30. "port": "",          // 精确匹配，为空不检查
31. "path": ""           // 前缀匹配，为空不检查
32. }
33. ]
34. },
35. {
36. "methodName": "test11",
37. "urlPermissionList": [   // Method级权限
38. {
39. "scheme": "q",       // 精确匹配，不能为空
40. "host": "r",         // 精确匹配，不能为空
41. "port": "",          // 精确匹配，为空不检查
42. "path": "t"          // 前缀匹配，为空不检查
43. },
44. {
45. "scheme": "u",       // 精确匹配，不能为空
46. "host": "v",         // 精确匹配，不能为空
47. "port": "",          // 精确匹配，为空不检查
48. "path": ""           // 前缀匹配，为空不检查
49. }
50. ]
51. }
52. ]
53. }
54. }
```

### 应用侧调用前端页面函数

使用[runJavaScript](../harmonyos-references/capi-web-arkweb-controllerapi.md#runjavascript)调用前端页面函数。

```
1. // 构造runJS执行的结构体
2. char* jsCode = "runJSRetStr()";
3. ArkWeb_JavaScriptObject object = {(uint8_t *)jsCode, bufferSize, &JSBridgeObject::StaticRunJavaScriptCallback,
4. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr())};
5. // 调用前端页面runJSRetStr()函数
6. controller->runJavaScript(webTagValue, &object);
```

### 完整示例

* 前端页面代码

  ```
  1. <!-- entry/src/main/resources/rawfile/runJS.html -->
  2. <!-- runJS.html -->
  3. <!DOCTYPE html>
  4. <html lang="en-gb">
  5. <head>
  6. <meta name="viewport" content="width=device-width, initial-scale=1.0">
  7. <title>run javascript demo</title>
  8. </head>
  9. <body>
  10. <h1>run JavaScript Ext demo</h1>
  11. <p id="webDemo"></p>
  12. <br>
  13. <button type="button" style="height:30px;width:200px" onclick="testNdkProxyObjMethod1()">test ndk method1 ! </button>
  14. <br>
  15. <br>
  16. <button type="button" style="height:30px;width:200px" onclick="testNdkProxyObjMethod2()">test ndk method2 ! </button>
  17. <br>

  19. </body>
  20. <script type="text/javascript">

  22. function testNdkProxyObjMethod1() {
  23. if (window.ndkProxy == undefined) {
  24. document.getElementById("webDemo").innerHTML = "ndkProxy undefined"
  25. return "objName undefined"
  26. }

  28. if (window.ndkProxy.method1 == undefined) {
  29. document.getElementById("webDemo").innerHTML = "ndkProxy method1 undefined"
  30. return "objName  test undefined"
  31. }

  33. let retStr = window.ndkProxy.method1("hello", "world", [1.2, -3.4, 123.456], ["Saab", "Volvo", "BMW", undefined], 1.23456, 123789, true, false, 0,  undefined);
  34. console.info("ndkProxy and method1 is ok, " + retStr + ", type:" + typeof(retStr));
  35. }

  37. function testNdkProxyObjMethod2() {
  38. if (window.ndkProxy == undefined) {
  39. document.getElementById("webDemo").innerHTML = "ndkProxy undefined"
  40. return "objName undefined"
  41. }

  43. if (window.ndkProxy.method2 == undefined) {
  44. document.getElementById("webDemo").innerHTML = "ndkProxy method2 undefined"
  45. return "objName  test undefined"
  46. }

  48. var student = {
  49. name:"zhang",
  50. sex:"man",
  51. age:25
  52. };
  53. var cars = [student, 456, false, 4.567];
  54. let params = "[\"{\\\"scope\\\"]";

  56. let retStr = window.ndkProxy.method2("hello", "world", false, cars, params);
  57. console.info("ndkProxy and method2 is ok, " + retStr + ", type:" + typeof(retStr));
  58. }

  60. function runJSRetStr(data) {
  61. const d = new Date();
  62. let time = d.getTime();
  63. return JSON.stringify(time)
  64. }
  65. </script>
  66. </html>
  ```
* ArkTS侧代码

  ```
  1. // entry/src/main/ets/pages/Index.ets
  2. import testNapi from 'libentry.so';
  3. import { webview } from '@kit.ArkWeb';

  5. class testObj {
  6. constructor() {
  7. }

  9. test(): string {
  10. console.info('ArkUI Web Component');
  11. return "ArkUI Web Component";
  12. }

  14. toString(): void {
  15. console.info('Web Component toString');
  16. }
  17. }

  19. @Entry
  20. @Component
  21. struct Index {
  22. webTag: string = 'ArkWeb1';
  23. controller: webview.WebviewController = new webview.WebviewController(this.webTag);
  24. @State testObjtest: testObj = new testObj();

  26. aboutToAppear() {
  27. console.info("aboutToAppear")
  28. //初始化web ndk
  29. testNapi.nativeWebInit(this.webTag);
  30. }

  32. build() {
  33. Column() {
  34. Row() {
  35. Button('runJS hello')
  36. .fontSize(12)
  37. .onClick(() => {
  38. testNapi.runJavaScript(this.webTag, "runJSRetStr(\"" + "hello" + "\")");
  39. })
  40. }.height('20%')

  42. Row() {
  43. Web({ src: $rawfile('runJS.html'), controller: this.controller })
  44. .javaScriptAccess(true)
  45. .fileAccess(true)
  46. .onControllerAttached(() => {
  47. console.error("ndk onControllerAttached webId: " + this.controller.getWebId());
  48. })
  49. }.height('80%')
  50. }
  51. }
  52. }
  ```
* Node-API侧暴露ArkTS接口

  ```
  1. export const nativeWebInit: (webName: string) => void;
  2. export const runJavaScript: (webName: string, jsCode: string) => void;
  ```

  [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseFrontendJSApp/entry4/src/main/cpp/types/libentry4/Index.d.ts#L16-L20)
* Node-API侧编译配置entry/src/main/cpp/CMakeLists.txt

  ```
  1. # the minimum version of CMake.
  2. cmake_minimum_required(VERSION 3.4.1)
  3. project(NDKJSBridge)

  5. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

  7. if(DEFINED PACKAGE_FIND_FILE)
  8. include(${PACKAGE_FIND_FILE})
  9. endif()

  11. include_directories(${NATIVERENDER_ROOT_PATH}
  12. ${NATIVERENDER_ROOT_PATH}/include)

  14. add_library(entry SHARED hello.cpp jsbridge_object.cpp)

  16. find_library(
  17. # Sets the name of the path variable.
  18. hilog-lib
  19. # Specifies the name of the NDK library that
  20. # you want CMake to locate.
  21. hilog_ndk.z
  22. )

  24. target_link_libraries(entry PUBLIC libace_napi.z.so ${hilog-lib} libohweb.so)
  ```
* Node-API层代码

  ```
  1. // entry/src/main/cpp/hello.cpp
  2. #include "napi/native_api.h"
  3. #include <bits/alltypes.h>
  4. #include <memory>
  5. #include <string>
  6. #include <sys/types.h>
  7. #include <thread>

  9. #include "hilog/log.h"
  10. #include "web/arkweb_interface.h"
  11. #include "jsbridge_object.h"

  13. constexpr unsigned int LOG_PRINT_DOMAIN = 0xFF00;
  14. std::shared_ptr<JSBridgeObject> jsbridge_object_ptr = nullptr;
  15. static ArkWeb_ControllerAPI *controller = nullptr;
  16. static ArkWeb_ComponentAPI *component = nullptr;
  17. ArkWeb_JavaScriptValueAPI *javaScriptValueApi = nullptr;

  19. // 发送JS脚本到H5侧执行，该方法为执行结果的回调。
  20. static void RunJavaScriptCallback(const char *webTag, const char *result, void *userData) {
  21. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk RunJavaScriptCallback webTag:%{public}s", webTag);
  22. if (!userData) {
  23. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk RunJavaScriptCallback userData is nullptr");
  24. return;
  25. }
  26. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);
  27. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
  28. jsb_ptr->RunJavaScriptCallback(result);
  29. } else {
  30. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  31. "ndk RunJavaScriptCallback jsb_weak_ptr lock failed");
  32. }
  33. }

  35. // 示例代码 ，注册了1个对象，2个方法
  36. static ArkWeb_JavaScriptValuePtr ProxyMethod1(const char *webTag, const ArkWeb_JavaScriptBridgeData *dataArray, size_t arraySize, void *userData) {
  37. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ProxyMethod1 webTag:%{public}s", webTag);
  38. if (!userData) {
  39. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ProxyMethod1 userData is nullptr");
  40. return nullptr;
  41. }
  42. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);
  43. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
  44. jsb_ptr->ProxyMethod1(dataArray, arraySize);
  45. } else {
  46. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ProxyMethod1 jsb_weak_ptr lock failed");
  47. }

  49. bool boolValue = true;
  50. return javaScriptValueApi->createJavaScriptValue(ArkWeb_JavaScriptValueType::ARKWEB_JAVASCRIPT_BOOL, (void*)(&boolValue), 1);
  51. }

  53. static ArkWeb_JavaScriptValuePtr ProxyMethod2(const char *webTag, const ArkWeb_JavaScriptBridgeData *dataArray, size_t arraySize, void *userData) {
  54. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ProxyMethod2 webTag:%{public}s", webTag);
  55. if (!userData) {
  56. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ProxyMethod2 userData is nullptr");
  57. return nullptr;
  58. }
  59. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);

  61. std::string jsCode = "runJSRetStr()";
  62. ArkWeb_JavaScriptObject object = {(uint8_t *)jsCode.c_str(), jsCode.size(),
  63. &JSBridgeObject::StaticRunJavaScriptCallback,
  64. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr())};
  65. controller->runJavaScript(webTag, &object);

  67. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
  68. jsb_ptr->ProxyMethod2(dataArray, arraySize);
  69. } else {
  70. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ProxyMethod2 jsb_weak_ptr lock failed");
  71. }

  73. std::string str = "this is a string";
  74. return javaScriptValueApi->createJavaScriptValue(ArkWeb_JavaScriptValueType::ARKWEB_JAVASCRIPT_STRING, (void*)str.c_str(), str.length() + 1);
  75. }

  77. void ValidCallback(const char *webTag, void *userData) {
  78. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ValidCallback webTag: %{public}s", webTag);
  79. if (!userData) {
  80. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ValidCallback userData is nullptr");
  81. return;
  82. }
  83. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);
  84. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
  85. jsb_ptr->SaySomething("ValidCallback");
  86. } else {
  87. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ValidCallback jsb_weak_ptr lock failed");
  88. }

  90. // 注册对象
  91. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk registerJavaScriptProxyEx begin");
  92. ArkWeb_ProxyMethodWithResult method1 = {"method1", ProxyMethod1, static_cast<void *>(jsbridge_object_ptr->GetWeakPtr())};
  93. ArkWeb_ProxyMethodWithResult method2 = {"method2", ProxyMethod2, static_cast<void *>(jsbridge_object_ptr->GetWeakPtr())};
  94. ArkWeb_ProxyMethodWithResult methodList[2] = {method1, method2};
  95. // 调用ndk接口注册对象
  96. // 如此注册的情况下，在H5页面就可以使用proxy.method1、proxy.method2调用此文件下的ProxyMethod1和ProxyMethod2方法了
  97. ArkWeb_ProxyObjectWithResult proxyObject = {"ndkProxy", methodList, 2};
  98. controller->registerJavaScriptProxyEx(webTag, &proxyObject, "");

  100. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk registerJavaScriptProxyEx end");
  101. }

  103. void LoadStartCallback(const char *webTag, void *userData) {
  104. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk LoadStartCallback webTag: %{public}s", webTag);
  105. if (!userData) {
  106. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk LoadStartCallback userData is nullptr");
  107. return;
  108. }
  109. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);
  110. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
  111. jsb_ptr->SaySomething("LoadStartCallback");
  112. } else {
  113. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk LoadStartCallback jsb_weak_ptr lock failed");
  114. }
  115. }

  117. void LoadEndCallback(const char *webTag, void *userData) {
  118. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk LoadEndCallback webTag: %{public}s", webTag);
  119. if (!userData) {
  120. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk LoadEndCallback userData is nullptr");
  121. return;
  122. }
  123. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);
  124. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
  125. jsb_ptr->SaySomething("LoadEndCallback");
  126. } else {
  127. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk LoadEndCallback jsb_weak_ptr lock failed");
  128. }
  129. }

  131. void DestroyCallback(const char *webTag, void *userData) {
  132. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk DestroyCallback webTag: %{public}s", webTag);
  133. if (!userData) {
  134. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk DestroyCallback userData is nullptr");
  135. return;
  136. }
  137. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);
  138. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
  139. jsb_ptr->SaySomething("DestroyCallback");
  140. } else {
  141. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk DestroyCallback jsb_weak_ptr lock failed");
  142. }
  143. }

  145. void SetComponentCallback(ArkWeb_ComponentAPI * component, const char* webTagValue) {
  146. if (!ARKWEB_MEMBER_MISSING(component, onControllerAttached)) {
  147. component->onControllerAttached(webTagValue, ValidCallback,
  148. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr()));
  149. } else {
  150. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "component onControllerAttached func not exist");
  151. }

  153. if (!ARKWEB_MEMBER_MISSING(component, onPageBegin)) {
  154. component->onPageBegin(webTagValue, LoadStartCallback,
  155. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr()));
  156. } else {
  157. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "component onPageBegin func not exist");
  158. }

  160. if (!ARKWEB_MEMBER_MISSING(component, onPageEnd)) {
  161. component->onPageEnd(webTagValue, LoadEndCallback,
  162. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr()));
  163. } else {
  164. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "component onPageEnd func not exist");
  165. }

  167. if (!ARKWEB_MEMBER_MISSING(component, onDestroy)) {
  168. component->onDestroy(webTagValue, DestroyCallback,
  169. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr()));
  170. } else {
  171. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "component onDestroy func not exist");
  172. }
  173. }

  175. // 解析存储webTag
  176. static napi_value NativeWebInit(napi_env env, napi_callback_info info) {
  177. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk NativeWebInit start");
  178. size_t argc = 1;
  179. napi_value args[1] = {nullptr};
  180. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
  181. // 获取第一个参数 webTag
  182. size_t webTagSize = 0;
  183. napi_get_value_string_utf8(env, args[0], nullptr, 0, &webTagSize);
  184. char *webTagValue = new (std::nothrow) char[webTagSize + 1];
  185. size_t webTagLength = 0;
  186. napi_get_value_string_utf8(env, args[0], webTagValue, webTagSize + 1, &webTagLength);
  187. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "ndk NativeWebInit webTag:%{public}s", webTagValue);

  189. jsbridge_object_ptr = std::make_shared<JSBridgeObject>(webTagValue);
  190. if (jsbridge_object_ptr)
  191. jsbridge_object_ptr->Init();

  193. controller = reinterpret_cast<ArkWeb_ControllerAPI *>(OH_ArkWeb_GetNativeAPI(ARKWEB_NATIVE_CONTROLLER));
  194. if (controller)
  195. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "get ArkWeb_ControllerAPI success");

  197. component = reinterpret_cast<ArkWeb_ComponentAPI *>(OH_ArkWeb_GetNativeAPI(ARKWEB_NATIVE_COMPONENT));
  198. if (component)
  199. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "get ArkWeb_ComponentAPI success");

  201. javaScriptValueApi =
  202. reinterpret_cast<ArkWeb_JavaScriptValueAPI *>(OH_ArkWeb_GetNativeAPI(ARKWEB_NATIVE_JAVASCRIPT_VALUE));
  203. if (javaScriptValueApi)
  204. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "get ArkWeb_JavaScriptValueAPI success");
  205. else
  206. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "get ArkWeb_JavaScriptValueAPI failed");

  208. SetComponentCallback(component, webTagValue);

  210. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk NativeWebInit end");

  212. delete[] webTagValue;

  214. return nullptr;
  215. }

  217. // 发送JS脚本到H5侧执行
  218. static napi_value RunJavaScript(napi_env env, napi_callback_info info) {
  219. size_t argc = 2;
  220. napi_value args[2] = {nullptr};
  221. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

  223. // 获取第一个参数webTag
  224. size_t webTagSize = 0;
  225. napi_get_value_string_utf8(env, args[0], nullptr, 0, &webTagSize);
  226. char *webTagValue = new (std::nothrow) char[webTagSize + 1];
  227. size_t webTagLength = 0;
  228. napi_get_value_string_utf8(env, args[0], webTagValue, webTagSize + 1, &webTagLength);
  229. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk OH_NativeArkWeb_RunJavaScript webTag:%{public}s",
  230. webTagValue);

  232. // 获取第二个参数 jsCode
  233. size_t bufferSize = 0;
  234. napi_get_value_string_utf8(env, args[1], nullptr, 0, &bufferSize);
  235. char *jsCode = new (std::nothrow) char[bufferSize + 1];
  236. size_t byteLength = 0;
  237. napi_get_value_string_utf8(env, args[1], jsCode, bufferSize + 1, &byteLength);

  239. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  240. "ndk OH_NativeArkWeb_RunJavaScript jsCode len:%{public}zu", strlen(jsCode));

  242. // 构造runJS执行的结构体
  243. ArkWeb_JavaScriptObject object = {(uint8_t *)jsCode, bufferSize, &JSBridgeObject::StaticRunJavaScriptCallback,
  244. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr())};
  245. controller->runJavaScript(webTagValue, &object);

  247. delete[] webTagValue;

  249. delete[] jsCode;

  251. return nullptr;
  252. }

  254. EXTERN_C_START
  255. static napi_value Init(napi_env env, napi_value exports) {
  256. napi_property_descriptor desc[] = {
  257. {"nativeWebInit", nullptr, NativeWebInit, nullptr, nullptr, nullptr, napi_default, nullptr},
  258. {"runJavaScript", nullptr, RunJavaScript, nullptr, nullptr, nullptr, napi_default, nullptr},
  259. };
  260. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
  261. return exports;
  262. }
  263. EXTERN_C_END

  265. static napi_module demoModule = {
  266. .nm_version = 1,
  267. .nm_flags = 0,
  268. .nm_filename = nullptr,
  269. .nm_register_func = Init,
  270. .nm_modname = "entry",
  271. .nm_priv = ((void *)0),
  272. .reserved = {0},
  273. };

  275. extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
  ```
* Native侧业务代码

  ```
  1. // entry/src/main/cpp/jsbridge_object.h
  2. #include "web/arkweb_type.h"
  3. #include <string>

  5. class JSBridgeObject : public std::enable_shared_from_this<JSBridgeObject> {
  6. public:
  7. JSBridgeObject(const char* webTag);
  8. ~JSBridgeObject() = default;
  9. void Init();
  10. std::weak_ptr<JSBridgeObject>* GetWeakPtr();
  11. static void StaticRunJavaScriptCallback(const char *webTag, const ArkWeb_JavaScriptBridgeData *data, void *userData);
  12. void RunJavaScriptCallback(const char *result);
  13. void ProxyMethod1(const ArkWeb_JavaScriptBridgeData *dataArray, int32_t arraySize);
  14. void ProxyMethod2(const ArkWeb_JavaScriptBridgeData *dataArray, int32_t arraySize);
  15. void SaySomething(const char* say);

  17. private:
  18. std::string webTag_;
  19. std::weak_ptr<JSBridgeObject> weak_ptr_;
  20. };
  ```

  ```
  1. // entry/src/main/cpp/jsbridge_object.cpp
  2. #include "jsbridge_object.h"

  4. #include "hilog/log.h"

  6. constexpr unsigned int LOG_PRINT_DOMAIN = 0xFF00;

  8. JSBridgeObject::JSBridgeObject(const char *webTag) : webTag_(webTag) {}

  10. void JSBridgeObject::Init() { weak_ptr_ = shared_from_this(); }

  12. std::weak_ptr<JSBridgeObject> *JSBridgeObject::GetWeakPtr() { return &weak_ptr_; }

  14. void JSBridgeObject::StaticRunJavaScriptCallback(const char *webTag, const ArkWeb_JavaScriptBridgeData *data,
  15. void *userData) {
  16. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  17. "JSBridgeObject StaticRunJavaScriptCallback webTag:%{public}s", webTag);
  18. if (!userData) {
  19. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  20. "JSBridgeObject StaticRunJavaScriptCallback userData is nullptr");
  21. return;
  22. }
  23. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);
  24. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
  25. std::string result((char *)data->buffer, data->size);
  26. jsb_ptr->RunJavaScriptCallback(result.c_str());
  27. } else {
  28. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  29. "JSBridgeObject StaticRunJavaScriptCallback jsb_weak_ptr lock failed");
  30. }
  31. }

  33. void JSBridgeObject::RunJavaScriptCallback(const char *result) {
  34. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  35. "JSBridgeObject OH_NativeArkWeb_RunJavaScript result:%{public}s", result);
  36. }

  38. void JSBridgeObject::ProxyMethod1(const ArkWeb_JavaScriptBridgeData *dataArray, int32_t arraySize) {
  39. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "JSBridgeObject ProxyMethod1 argc:%{public}d",
  40. arraySize);
  41. for (int i = 0; i < arraySize; i++) {
  42. std::string result((char *)dataArray[i].buffer, dataArray[i].size);
  43. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  44. "JSBridgeObject ProxyMethod1 argv[%{public}d]:%{public}s, size:%{public}d", i, result.c_str(),
  45. dataArray[i].size);
  46. }
  47. }

  49. void JSBridgeObject::ProxyMethod2(const ArkWeb_JavaScriptBridgeData *dataArray, int32_t arraySize) {
  50. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "JSBridgeObject ProxyMethod2 argc:%{public}d",
  51. arraySize);
  52. for (int i = 0; i < arraySize; i++) {
  53. std::string result((char *)dataArray[i].buffer, dataArray[i].size);
  54. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  55. "JSBridgeObject ProxyMethod2 argv[%{public}d]:%{public}s, size:%{public}d", i, result.c_str(),
  56. dataArray[i].size);
  57. }
  58. }

  60. void JSBridgeObject::SaySomething(const char *say) {
  61. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "JSBridgeObject SaySomething argc:%{public}s", say);
  62. }
  ```

## 使用Native接口实现JSBridge通信

### 使用Native接口绑定ArkWeb

* ArkWeb组件声明在ArkTS侧，需要用户自定义一个标识webTag，并将webTag通过Node-API传至应用Native侧，后续ArkWeb Native接口使用，均需webTag作为对应组件的唯一标识。
* ArkTS侧

  ```
  1. // 自定义webTag，在WebviewController创建时作为入参传入，建立controller与webTag的映射关系
  2. webTag: string = 'ArkWeb1';
  3. controller: webview.WebviewController = new webview.WebviewController(this.webTag);
  4. // ...
  5. // aboutToAppear中将webTag通过Node-API接口传入C++侧，作为C++侧ArkWeb组件的唯一标识
  6. aboutToAppear() {
  7. console.info("aboutToAppear")
  8. //初始化web ndk
  9. testNapi.nativeWebInit(this.webTag);
  10. }
  11. // ...
  ```
* C++侧

  ```
  1. // 解析存储webTag
  2. static napi_value NativeWebInit(napi_env env, napi_callback_info info) {
  3. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk NativeWebInit start");
  4. size_t argc = 1;
  5. napi_value args[1] = {nullptr};
  6. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
  7. // 获取第一个参数webTag
  8. size_t webTagSize = 0;
  9. napi_get_value_string_utf8(env, args[0], nullptr, 0, &webTagSize);
  10. char *webTagValue = new (std::nothrow) char[webTagSize + 1];
  11. size_t webTagLength = 0;
  12. napi_get_value_string_utf8(env, args[0], webTagValue, webTagSize + 1, &webTagLength);
  13. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "ndk NativeWebInit webTag:%{public}s", webTagValue);

  15. // 将webTag保存在实例对象中
  16. jsbridge_object_ptr = std::make_shared<JSBridgeObject>(webTagValue);
  17. // ...
  18. }
  ```

### 使用Native接口获取API结构体

ArkWeb Native侧需要先获取API结构体，才能调用结构体里的Native API。ArkWeb Native侧API通过函数[OH\_ArkWeb\_GetNativeAPI](../harmonyos-references/capi-arkweb-interface-h.md#oh_arkweb_getnativeapi)获取，根据入参type不同，可分别获取[ArkWeb\_ControllerAPI](../harmonyos-references/capi-web-arkweb-controllerapi.md)、[ArkWeb\_ComponentAPI](../harmonyos-references/capi-web-arkweb-componentapi.md)函数指针结构体。其中，[ArkWeb\_ControllerAPI](../harmonyos-references/capi-web-arkweb-controllerapi.md)对应ArkTS侧[web\_webview.WebviewController API](../harmonyos-references/arkts-apis-webview-webviewcontroller.md)，[ArkWeb\_ComponentAPI](../harmonyos-references/capi-web-arkweb-componentapi.md)对应ArkTS侧[ArkWeb组件API](../harmonyos-references/arkts-basic-components-web.md)。

```
1. static ArkWeb_ControllerAPI *controller = nullptr;
2. static ArkWeb_ComponentAPI *component = nullptr;
3. // ...
4. controller = reinterpret_cast<ArkWeb_ControllerAPI *>(OH_ArkWeb_GetNativeAPI(ARKWEB_NATIVE_CONTROLLER));
5. component = reinterpret_cast<ArkWeb_ComponentAPI *>(OH_ArkWeb_GetNativeAPI(ARKWEB_NATIVE_COMPONENT));
```

### Native侧注册组件生命周期回调

通过[ArkWeb\_ComponentAPI](../harmonyos-references/capi-web-arkweb-componentapi.md)注册组件生命周期回调，在调用接口前建议通过[ARKWEB\_MEMBER\_MISSING](../harmonyos-references/capi-arkweb-type-h.md#宏定义)校验该函数结构体是否有对应函数指针，避免SDK与设备ROM不匹配导致crash问题。

```
1. if (!ARKWEB_MEMBER_MISSING(component, onControllerAttached)) {
2. component->onControllerAttached(webTagValue, ValidCallback,
3. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr()));
4. } else {
5. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "component onControllerAttached func not exist");
6. }

8. if (!ARKWEB_MEMBER_MISSING(component, onPageBegin)) {
9. component->onPageBegin(webTagValue, LoadStartCallback,
10. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr()));
11. } else {
12. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "component onPageBegin func not exist");
13. }

15. if (!ARKWEB_MEMBER_MISSING(component, onPageEnd)) {
16. component->onPageEnd(webTagValue, LoadEndCallback,
17. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr()));
18. } else {
19. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "component onPageEnd func not exist");
20. }

22. if (!ARKWEB_MEMBER_MISSING(component, onDestroy)) {
23. component->onDestroy(webTagValue, DestroyCallback,
24. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr()));
25. } else {
26. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "component onDestroy func not exist");
27. }
```

### 前端页面调用应用侧函数

通过[registerJavaScriptProxy](../harmonyos-references/capi-web-arkweb-controllerapi.md#registerjavascriptproxy)将应用侧函数注册至前端页面，注册后在下次加载或者重新加载后生效。

```
1. // 注册对象
2. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk RegisterJavaScriptProxy begin");
3. ArkWeb_ProxyMethod method1 = {"method1", ProxyMethod1, static_cast<void *>(jsbridge_object_ptr->GetWeakPtr())};
4. ArkWeb_ProxyMethod method2 = {"method2", ProxyMethod2, static_cast<void *>(jsbridge_object_ptr->GetWeakPtr())};
5. ArkWeb_ProxyMethod methodList[2] = {method1, method2};
6. // 调用ndk接口注册对象
7. // 如此注册的情况下，在H5页面就可以使用proxy.method1、proxy.method2调用此文件下的ProxyMethod1和ProxyMethod2方法了
8. ArkWeb_ProxyObject proxyObject = {"ndkProxy", methodList, 2};
9. controller->registerJavaScriptProxy(webTag, &proxyObject);
```

### 应用侧调用前端页面函数

通过[runJavaScript](../harmonyos-references/capi-web-arkweb-controllerapi.md#runjavascript)调用前端页面函数。

```
1. // 构造runJS执行的结构体
2. const char* jsCode = "runJSRetStr()";
3. ArkWeb_JavaScriptObject object = {(uint8_t *)jsCode, bufferSize, &JSBridgeObject::StaticRunJavaScriptCallback,
4. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr())};
5. // 调用前端页面runJSRetStr()函数
6. controller->runJavaScript(webTagValue, &object);
```

### 完整示例

* 前端页面代码

  ```
  1. <!-- entry/src/main/resources/rawfile/runJS.html -->
  2. <!-- runJS.html -->
  3. <!DOCTYPE html>
  4. <html lang="en-gb">
  5. <head>
  6. <meta name="viewport" content="width=device-width, initial-scale=1.0">
  7. <title>run javascript demo</title>
  8. </head>
  9. <body>
  10. <h1>run JavaScript Ext demo</h1>
  11. <p id="webDemo"></p>
  12. <br>
  13. <button type="button" style="height:30px;width:200px" onclick="testNdkProxyObjMethod1()">test ndk method1 ! </button>
  14. <br>
  15. <br>
  16. <button type="button" style="height:30px;width:200px" onclick="testNdkProxyObjMethod2()">test ndk method2 ! </button>
  17. <br>

  19. </body>
  20. <script type="text/javascript">

  22. function testNdkProxyObjMethod1() {
  23. if (window.ndkProxy == undefined) {
  24. document.getElementById("webDemo").innerHTML = "ndkProxy undefined"
  25. return "objName undefined"
  26. }

  28. if (window.ndkProxy.method1 == undefined) {
  29. document.getElementById("webDemo").innerHTML = "ndkProxy method1 undefined"
  30. return "objName  test undefined"
  31. }

  33. window.ndkProxy.method1("hello", "world", [1.2, -3.4, 123.456], ["Saab", "Volvo", "BMW", undefined], 1.23456, 123789, true, false, 0,  undefined);
  34. }

  36. function testNdkProxyObjMethod2() {
  37. if (window.ndkProxy == undefined) {
  38. document.getElementById("webDemo").innerHTML = "ndkProxy undefined"
  39. return "objName undefined"
  40. }

  42. if (window.ndkProxy.method2 == undefined) {
  43. document.getElementById("webDemo").innerHTML = "ndkProxy method2 undefined"
  44. return "objName  test undefined"
  45. }

  47. var student = {
  48. name:"zhang",
  49. sex:"man",
  50. age:25
  51. };
  52. var cars = [student, 456, false, 4.567];
  53. let params = "[\"{\\\"scope\\\"]";

  55. window.ndkProxy.method2("hello", "world", false, cars, params);
  56. }

  58. function runJSRetStr(data) {
  59. const d = new Date();
  60. let time = d.getTime();
  61. return JSON.stringify(time)
  62. }
  63. </script>
  64. </html>
  ```
* ArkTS侧代码

  ```
  1. // entry/src/main/ets/pages/Index.ets
  2. import testNapi from 'libentry.so';
  3. import { webview } from '@kit.ArkWeb';

  5. class testObj {
  6. constructor() {
  7. }

  9. test(): string {
  10. console.info('ArkUI Web Component');
  11. return "ArkUI Web Component";
  12. }

  14. toString(): void {
  15. console.info('Web Component toString');
  16. }
  17. }

  19. @Entry
  20. @Component
  21. struct Index {
  22. webTag: string = 'ArkWeb1';
  23. controller: webview.WebviewController = new webview.WebviewController(this.webTag);
  24. @State testObjtest: testObj = new testObj();

  26. aboutToAppear() {
  27. console.info("aboutToAppear")
  28. //初始化web ndk
  29. testNapi.nativeWebInit(this.webTag);
  30. }

  32. build() {
  33. Column() {
  34. Row() {
  35. Button('runJS hello')
  36. .fontSize(12)
  37. .onClick(() => {
  38. testNapi.runJavaScript(this.webTag, "runJSRetStr(\"" + "hello" + "\")");
  39. })
  40. }.height('20%')

  42. Row() {
  43. Web({ src: $rawfile('runJS.html'), controller: this.controller })
  44. .javaScriptAccess(true)
  45. .fileAccess(true)
  46. .onControllerAttached(() => {
  47. console.error("ndk onControllerAttached webId: " + this.controller.getWebId());
  48. })
  49. }.height('80%')
  50. }
  51. }
  52. }
  ```
* Node-API侧暴露ArkTS接口

  ```
  1. // entry/src/main/cpp/types/libentry/index.d.ts
  2. export const nativeWebInit: (webName: string) => void;
  3. export const runJavaScript: (webName: string, jsCode: string) => void;
  ```
* Node-API侧编译配置entry/src/main/cpp/CMakeLists.txt

  ```
  1. # the minimum version of CMake.
  2. cmake_minimum_required(VERSION 3.4.1)
  3. project(NDKJSBridge)

  5. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

  7. if(DEFINED PACKAGE_FIND_FILE)
  8. include(${PACKAGE_FIND_FILE})
  9. endif()

  11. include_directories(${NATIVERENDER_ROOT_PATH}
  12. ${NATIVERENDER_ROOT_PATH}/include)

  14. add_library(entry SHARED hello.cpp jsbridge_object.cpp)

  16. find_library(
  17. # Sets the name of the path variable.
  18. hilog-lib
  19. # Specifies the name of the NDK library that
  20. # you want CMake to locate.
  21. hilog_ndk.z
  22. )

  24. target_link_libraries(entry PUBLIC libace_napi.z.so ${hilog-lib} libohweb.so)
  ```
* Node-API层代码

  ```
  1. // entry/src/main/cpp/hello.cpp
  2. #include "napi/native_api.h"
  3. #include <bits/alltypes.h>
  4. #include <memory>
  5. #include <string>
  6. #include <sys/types.h>
  7. #include <thread>

  9. #include "hilog/log.h"
  10. #include "web/arkweb_interface.h"
  11. #include "jsbridge_object.h"

  13. constexpr unsigned int LOG_PRINT_DOMAIN = 0xFF00;
  14. std::shared_ptr<JSBridgeObject> jsbridge_object_ptr = nullptr;
  15. static ArkWeb_ControllerAPI *controller = nullptr;
  16. static ArkWeb_ComponentAPI *component = nullptr;

  18. // 发送JS脚本到H5侧执行，该方法为执行结果的回调。
  19. static void RunJavaScriptCallback(const char *webTag, const char *result, void *userData) {
  20. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk RunJavaScriptCallback webTag:%{public}s", webTag);
  21. if (!userData) {
  22. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk RunJavaScriptCallback userData is nullptr");
  23. return;
  24. }
  25. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);
  26. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
  27. jsb_ptr->RunJavaScriptCallback(result);
  28. } else {
  29. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  30. "ndk RunJavaScriptCallback jsb_weak_ptr lock failed");
  31. }
  32. }

  34. // 示例代码 ，注册了1个对象，2个方法
  35. static void ProxyMethod1(const char *webTag, const ArkWeb_JavaScriptBridgeData *dataArray, size_t arraySize, void *userData) {
  36. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ProxyMethod1 webTag:%{public}s", webTag);
  37. if (!userData) {
  38. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ProxyMethod1 userData is nullptr");
  39. return;
  40. }
  41. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);
  42. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
  43. jsb_ptr->ProxyMethod1(dataArray, arraySize);
  44. } else {
  45. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ProxyMethod1 jsb_weak_ptr lock failed");
  46. }
  47. }

  49. static void ProxyMethod2(const char *webTag, const ArkWeb_JavaScriptBridgeData *dataArray, size_t arraySize, void *userData) {
  50. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ProxyMethod2 webTag:%{public}s", webTag);
  51. if (!userData) {
  52. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ProxyMethod2 userData is nullptr");
  53. return;
  54. }
  55. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);

  57. std::string jsCode = "runJSRetStr()";
  58. ArkWeb_JavaScriptObject object = {(uint8_t *)jsCode.c_str(), jsCode.size(),
  59. &JSBridgeObject::StaticRunJavaScriptCallback,
  60. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr())};
  61. controller->runJavaScript(webTag, &object);

  63. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
  64. jsb_ptr->ProxyMethod2(dataArray, arraySize);
  65. } else {
  66. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ProxyMethod2 jsb_weak_ptr lock failed");
  67. }
  68. }

  70. void ValidCallback(const char *webTag, void *userData) {
  71. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ValidCallback webTag: %{public}s", webTag);
  72. if (!userData) {
  73. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ValidCallback userData is nullptr");
  74. return;
  75. }
  76. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);
  77. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
  78. jsb_ptr->SaySomething("ValidCallback");
  79. } else {
  80. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ValidCallback jsb_weak_ptr lock failed");
  81. }

  83. // 注册对象
  84. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk RegisterJavaScriptProxy begin");
  85. ArkWeb_ProxyMethod method1 = {"method1", ProxyMethod1, static_cast<void *>(jsbridge_object_ptr->GetWeakPtr())};
  86. ArkWeb_ProxyMethod method2 = {"method2", ProxyMethod2, static_cast<void *>(jsbridge_object_ptr->GetWeakPtr())};
  87. ArkWeb_ProxyMethod methodList[2] = {method1, method2};
  88. // 调用ndk接口注册对象
  89. // 如此注册的情况下，在H5页面就可以使用proxy.method1、proxy.method2调用此文件下的ProxyMethod1和ProxyMethod2方法了
  90. ArkWeb_ProxyObject proxyObject = {"ndkProxy", methodList, 2};
  91. controller->registerJavaScriptProxy(webTag, &proxyObject);

  93. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk RegisterJavaScriptProxy end");
  94. }

  96. void LoadStartCallback(const char *webTag, void *userData) {
  97. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk LoadStartCallback webTag: %{public}s", webTag);
  98. if (!userData) {
  99. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk LoadStartCallback userData is nullptr");
  100. return;
  101. }
  102. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);
  103. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
  104. jsb_ptr->SaySomething("LoadStartCallback");
  105. } else {
  106. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk LoadStartCallback jsb_weak_ptr lock failed");
  107. }
  108. }

  110. void LoadEndCallback(const char *webTag, void *userData) {
  111. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk LoadEndCallback webTag: %{public}s", webTag);
  112. if (!userData) {
  113. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk LoadEndCallback userData is nullptr");
  114. return;
  115. }
  116. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);
  117. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
  118. jsb_ptr->SaySomething("LoadEndCallback");
  119. } else {
  120. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk LoadEndCallback jsb_weak_ptr lock failed");
  121. }
  122. }

  124. void DestroyCallback(const char *webTag, void *userData) {
  125. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk DestroyCallback webTag: %{public}s", webTag);
  126. if (!userData) {
  127. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk DestroyCallback userData is nullptr");
  128. return;
  129. }
  130. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);
  131. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
  132. jsb_ptr->SaySomething("DestroyCallback");
  133. } else {
  134. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk DestroyCallback jsb_weak_ptr lock failed");
  135. }
  136. }

  138. void SetComponentCallback(ArkWeb_ComponentAPI * component, const char* webTagValue) {
  139. if (!ARKWEB_MEMBER_MISSING(component, onControllerAttached)) {
  140. component->onControllerAttached(webTagValue, ValidCallback,
  141. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr()));
  142. } else {
  143. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "component onControllerAttached func not exist");
  144. }

  146. if (!ARKWEB_MEMBER_MISSING(component, onPageBegin)) {
  147. component->onPageBegin(webTagValue, LoadStartCallback,
  148. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr()));
  149. } else {
  150. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "component onPageBegin func not exist");
  151. }

  153. if (!ARKWEB_MEMBER_MISSING(component, onPageEnd)) {
  154. component->onPageEnd(webTagValue, LoadEndCallback,
  155. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr()));
  156. } else {
  157. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "component onPageEnd func not exist");
  158. }

  160. if (!ARKWEB_MEMBER_MISSING(component, onDestroy)) {
  161. component->onDestroy(webTagValue, DestroyCallback,
  162. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr()));
  163. } else {
  164. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "component onDestroy func not exist");
  165. }
  166. }

  168. // 解析存储webTag
  169. static napi_value NativeWebInit(napi_env env, napi_callback_info info) {
  170. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk NativeWebInit start");
  171. size_t argc = 1;
  172. napi_value args[1] = {nullptr};
  173. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
  174. // 获取第一个参数webTag
  175. size_t webTagSize = 0;
  176. napi_get_value_string_utf8(env, args[0], nullptr, 0, &webTagSize);
  177. char *webTagValue = new (std::nothrow) char[webTagSize + 1];
  178. size_t webTagLength = 0;
  179. napi_get_value_string_utf8(env, args[0], webTagValue, webTagSize + 1, &webTagLength);
  180. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "ndk NativeWebInit webTag:%{public}s", webTagValue);

  182. // 将webTag保存在实例对象中
  183. jsbridge_object_ptr = std::make_shared<JSBridgeObject>(webTagValue);
  184. if (jsbridge_object_ptr)
  185. jsbridge_object_ptr->Init();

  187. controller = reinterpret_cast<ArkWeb_ControllerAPI *>(OH_ArkWeb_GetNativeAPI(ARKWEB_NATIVE_CONTROLLER));
  188. component = reinterpret_cast<ArkWeb_ComponentAPI *>(OH_ArkWeb_GetNativeAPI(ARKWEB_NATIVE_COMPONENT));
  189. SetComponentCallback(component, webTagValue);

  191. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk NativeWebInit end");
  192. delete[] webTagValue;
  193. return nullptr;
  194. }

  196. // 发送JS脚本到H5侧执行
  197. static napi_value RunJavaScript(napi_env env, napi_callback_info info) {
  198. size_t argc = 2;
  199. napi_value args[2] = {nullptr};
  200. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

  202. // 获取第一个参数webTag
  203. size_t webTagSize = 0;
  204. napi_get_value_string_utf8(env, args[0], nullptr, 0, &webTagSize);
  205. char *webTagValue = new (std::nothrow) char[webTagSize + 1];
  206. size_t webTagLength = 0;
  207. napi_get_value_string_utf8(env, args[0], webTagValue, webTagSize + 1, &webTagLength);
  208. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk OH_NativeArkWeb_RunJavaScript webTag:%{public}s",
  209. webTagValue);

  211. // 获取第二个参数 jsCode
  212. size_t bufferSize = 0;
  213. napi_get_value_string_utf8(env, args[1], nullptr, 0, &bufferSize);
  214. char *jsCode = new (std::nothrow) char[bufferSize + 1];
  215. size_t byteLength = 0;
  216. napi_get_value_string_utf8(env, args[1], jsCode, bufferSize + 1, &byteLength);

  218. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  219. "ndk OH_NativeArkWeb_RunJavaScript jsCode len:%{public}zu", strlen(jsCode));

  221. // 构造runJS执行的结构体
  222. ArkWeb_JavaScriptObject object = {(uint8_t *)jsCode, bufferSize, &JSBridgeObject::StaticRunJavaScriptCallback,
  223. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr())};
  224. controller->runJavaScript(webTagValue, &object);
  225. delete[] webTagValue;
  226. delete[] jsCode;
  227. return nullptr;
  228. }

  230. EXTERN_C_START
  231. static napi_value Init(napi_env env, napi_value exports) {
  232. napi_property_descriptor desc[] = {
  233. {"nativeWebInit", nullptr, NativeWebInit, nullptr, nullptr, nullptr, napi_default, nullptr},
  234. {"runJavaScript", nullptr, RunJavaScript, nullptr, nullptr, nullptr, napi_default, nullptr},
  235. };
  236. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
  237. return exports;
  238. }
  239. EXTERN_C_END

  241. static napi_module demoModule = {
  242. .nm_version = 1,
  243. .nm_flags = 0,
  244. .nm_filename = nullptr,
  245. .nm_register_func = Init,
  246. .nm_modname = "entry",
  247. .nm_priv = ((void *)0),
  248. .reserved = {0},
  249. };

  251. extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
  ```
* Native侧业务代码

  ```
  1. // entry/src/main/cpp/jsbridge_object.h
  2. #include "web/arkweb_type.h"
  3. #include <string>

  5. class JSBridgeObject : public std::enable_shared_from_this<JSBridgeObject> {
  6. public:
  7. JSBridgeObject(const char* webTag);
  8. ~JSBridgeObject() = default;
  9. void Init();
  10. std::weak_ptr<JSBridgeObject>* GetWeakPtr();
  11. static void StaticRunJavaScriptCallback(const char *webTag, const ArkWeb_JavaScriptBridgeData *data, void *userData);
  12. void RunJavaScriptCallback(const char *result);
  13. void ProxyMethod1(const ArkWeb_JavaScriptBridgeData *dataArray, int32_t arraySize);
  14. void ProxyMethod2(const ArkWeb_JavaScriptBridgeData *dataArray, int32_t arraySize);
  15. void SaySomething(const char* say);

  17. private:
  18. std::string webTag_;
  19. std::weak_ptr<JSBridgeObject> weak_ptr_;
  20. };
  ```

  ```
  1. // entry/src/main/cpp/jsbridge_object.cpp
  2. #include "jsbridge_object.h"

  4. #include "hilog/log.h"

  6. constexpr unsigned int LOG_PRINT_DOMAIN = 0xFF00;

  8. JSBridgeObject::JSBridgeObject(const char *webTag) : webTag_(webTag) {}

  10. void JSBridgeObject::Init() { weak_ptr_ = shared_from_this(); }

  12. std::weak_ptr<JSBridgeObject> *JSBridgeObject::GetWeakPtr() { return &weak_ptr_; }

  14. void JSBridgeObject::StaticRunJavaScriptCallback(const char *webTag, const ArkWeb_JavaScriptBridgeData *data,
  15. void *userData) {
  16. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  17. "JSBridgeObject StaticRunJavaScriptCallback webTag:%{public}s", webTag);
  18. if (!userData) {
  19. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  20. "JSBridgeObject StaticRunJavaScriptCallback userData is nullptr");
  21. return;
  22. }
  23. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);
  24. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
  25. std::string result((char *)data->buffer, data->size);
  26. jsb_ptr->RunJavaScriptCallback(result.c_str());
  27. } else {
  28. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  29. "JSBridgeObject StaticRunJavaScriptCallback jsb_weak_ptr lock failed");
  30. }
  31. }

  33. void JSBridgeObject::RunJavaScriptCallback(const char *result) {
  34. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  35. "JSBridgeObject OH_NativeArkWeb_RunJavaScript result:%{public}s", result);
  36. }

  38. void JSBridgeObject::ProxyMethod1(const ArkWeb_JavaScriptBridgeData *dataArray, int32_t arraySize) {
  39. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "JSBridgeObject ProxyMethod1 argc:%{public}d",
  40. arraySize);
  41. for (int i = 0; i < arraySize; i++) {
  42. std::string result((char *)dataArray[i].buffer, dataArray[i].size);
  43. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  44. "JSBridgeObject ProxyMethod1 argv[%{public}d]:%{public}s, size:%{public}d", i, result.c_str(),
  45. dataArray[i].size);
  46. }
  47. }

  49. void JSBridgeObject::ProxyMethod2(const ArkWeb_JavaScriptBridgeData *dataArray, int32_t arraySize) {
  50. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "JSBridgeObject ProxyMethod2 argc:%{public}d",
  51. arraySize);
  52. for (int i = 0; i < arraySize; i++) {
  53. std::string result((char *)dataArray[i].buffer, dataArray[i].size);
  54. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  55. "JSBridgeObject ProxyMethod2 argv[%{public}d]:%{public}s, size:%{public}d", i, result.c_str(),
  56. dataArray[i].size);
  57. }
  58. }

  60. void JSBridgeObject::SaySomething(const char *say) {
  61. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "JSBridgeObject SaySomething argc:%{public}s", say);
  62. }
  ```
