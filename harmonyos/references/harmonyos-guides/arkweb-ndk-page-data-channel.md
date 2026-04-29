---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkweb-ndk-page-data-channel
title: 建立应用侧与前端页面数据通道(C/C++)
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 在应用中使用前端页面JavaScript > 建立应用侧与前端页面数据通道(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b98dfc439e6f1a56937519fe9a9eee391dfd2828d2375cd441277e9ccb71790f
---

前端页面和应用侧之间可以使用Native方法实现两端通信（以下简称Native PostWebMessage），可解决ArkTS环境的冗余切换，同时允许发送消息、回调在非UI线程上运行，避免造成UI阻塞。当前只支持string和buffer数据类型。

## 适用的应用架构

应用使用ArkTS、C++语言混合开发，或本身应用架构较贴近于小程序架构，自带C++侧环境，推荐使用ArkWeb在Native侧提供的[ArkWeb\_ControllerAPI](../harmonyos-references/capi-web-arkweb-controllerapi.md)、[ArkWeb\_WebMessageAPI](../harmonyos-references/capi-web-arkweb-webmessageapi.md)、[ArkWeb\_WebMessagePortAPI](../harmonyos-references/capi-web-arkweb-webmessageportapi.md)实现PostWebMessage功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/ynXZbepBR6Wj68zEDVirCA/zh-cn_image_0000002558764704.png?HW-CC-KV=V1&HW-CC-Date=20260429T052917Z&HW-CC-Expire=86400&HW-CC-Sign=4965F83A5DF71C2C67E38838B0594DA01E28B910920234CA52EDF5B95350D669)

上图展示了具有普遍适用性的小程序的通用架构。在这一架构中，逻辑层依赖于应用程序自带的JavaScript运行时，该运行时在一个已有的C++环境中运行。通过Native接口，逻辑层能够直接在C++环境中与视图层（其中ArkWeb充当渲染器）进行通信，无需回退至ArkTS环境使用ArkTS PostWebMessage接口。

左图是使用ArkTS PostWebMessage接口构建小程序的方案，如红框所示，应用需要先调用到ArkTS环境，再调用到C++环境。右图是使用Native PostWebMessage接口构建小程序的方案，不需要ArkTS环境和C++环境的切换，执行效率更高。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/FCAODJ4MQpOlwp_asDcu_w/zh-cn_image_0000002589324575.png?HW-CC-KV=V1&HW-CC-Date=20260429T052917Z&HW-CC-Expire=86400&HW-CC-Sign=FB0C4D9C876968ACA68F6913B77E7D17E8051AF9CE97547B0375F43B1ADA3332)

## 使用Native接口实现PostWebMessage通信

### 使用Native接口绑定ArkWeb

* ArkWeb组件声明在ArkTS侧，需要用户自定义一个标识webTag，并将webTag通过Node-API传至应用C++侧。后续ArkWeb Native接口使用时，均需webTag作为对应组件的唯一标识。
* ArkTS侧

  ```
  1. import { webview } from '@kit.ArkWeb';
  2. // 自定义webTag，在WebviewController创建时作为入参传入，建立controller与webTag的映射关系
  3. webTag: string = 'ArkWeb1';
  4. controller: webview.WebviewController = new webview.WebviewController(this.webTag);
  5. // ...
  6. // aboutToAppear中将webTag通过Node-API接口传入C++侧，作为C++侧ArkWeb组件的唯一标识
  7. aboutToAppear() {
  8. console.info("aboutToAppear")
  9. // 初始化web ndk
  10. testNapi.nativeWebInit(this.webTag);
  11. }
  12. // ...
  ```

### 使用Native接口获取API结构体

ArkWeb Native侧需先获取API结构体，才能调用结构体里的Native API。ArkWeb Native侧API通过函数[OH\_ArkWeb\_GetNativeAPI](../harmonyos-references/capi-arkweb-interface-h.md#oh_arkweb_getnativeapi)获取，根据入参type不同，可获取对应的函数指针结构体。其中本指导涉及[ArkWeb\_ControllerAPI](../harmonyos-references/capi-web-arkweb-controllerapi.md)、[ArkWeb\_WebMessageAPI](../harmonyos-references/capi-web-arkweb-webmessageapi.md)、[ArkWeb\_WebMessagePortAPI](../harmonyos-references/capi-web-arkweb-webmessageportapi.md)。

```
1. static ArkWeb_ControllerAPI *controller = nullptr;
2. static ArkWeb_WebMessagePortAPI *webMessagePort = nullptr;
3. static ArkWeb_WebMessageAPI *webMessage = nullptr;
4. // ...
5. controller = reinterpret_cast<ArkWeb_ControllerAPI *>(OH_ArkWeb_GetNativeAPI(ARKWEB_NATIVE_CONTROLLER));
6. webMessagePort =
7. reinterpret_cast<ArkWeb_WebMessagePortAPI *>(OH_ArkWeb_GetNativeAPI(ARKWEB_NATIVE_WEB_MESSAGE_PORT));
8. webMessage = reinterpret_cast<ArkWeb_WebMessageAPI *>(OH_ArkWeb_GetNativeAPI(ARKWEB_NATIVE_WEB_MESSAGE));
```

### 完整示例

在调用API前建议通过[ARKWEB\_MEMBER\_MISSING](../harmonyos-references/capi-arkweb-type-h.md#宏定义)校验该函数结构体是否有对应函数指针，避免SDK与设备ROM不匹配导致crash问题。[createWebMessagePorts](../harmonyos-references/capi-web-arkweb-controllerapi.md#createwebmessageports)、[postWebMessage](../harmonyos-references/capi-web-arkweb-controllerapi.md#postwebmessage)、[close](../harmonyos-references/capi-web-arkweb-webmessageportapi.md#close)需运行在UI线程。

* 前端页面代码

  ```
  1. <!-- entry/src/main/resources/rawfile/index.html -->
  2. <!-- index.html -->
  3. <!DOCTYPE html>
  4. <html lang="en-gb">
  5. <body>
  6. <h1>etsRunJavaScriptExt测试demo</h1>
  7. <h1 id="h1"></h1>
  8. <h3 id="msg">Receive string:</h3>
  9. <h3 id="msg2">Receive arraybuffer:</h3>

  11. </body>
  12. <script type="text/javascript">
  13. var h5Port;

  15. window.addEventListener('message', function (event) {
  16. if (event.data == 'init_web_messageport') {
  17. const port = event.ports[0]; // 1. 保存从应用侧发送过来的端口。
  18. if (port) {
  19. console.info("hwd In html got message");
  20. h5Port = port;
  21. port.onmessage = function (event) {
  22. console.info("hwd In html got message");
  23. // 2. 接收应用侧发送过来的消息.
  24. var result = event.data;
  25. var type_s = typeof (result)
  26. switch (type_s) {
  27. case "object":
  28. if (result instanceof ArrayBuffer) {
  29. type_s = "ArrayBuffer";
  30. var view = new Uint8Array(result);
  31. const decoder = new TextDecoder('utf-8');
  32. result = decoder.decode(result);
  33. } else if (result instanceof Error) {
  34. type_s = "Error";
  35. } else if (result instanceof Array) {
  36. type_s = "Array";
  37. }
  38. break;
  39. default:
  40. break;
  41. }
  42. console.info("H5 recv type: " + type_s + "\nH5 recv result: " + result)
  43. document.getElementById("msg").innerHTML = "recv type: " + type_s;
  44. document.getElementById("msg2").innerHTML = "recv value: " + result;
  45. }
  46. h5Port.onmessageerror = (event) => {
  47. console.error(`hwd In html Error receiving message: ${event}`);
  48. };
  49. }
  50. }
  51. })
  52. window.onerror = function(message, url, line, column, error) {
  53. console.info("JavaScript Error: " + message + " on line " + line + " in " + url);
  54. document.getElementById("h1").innerHTML = "执行函数失败"
  55. };

  57. // 3. 使用h5Port向应用侧发送消息。
  58. function postStringToApp() {
  59. if (h5Port) {
  60. h5Port.postMessage("send string from H5");
  61. } else {
  62. console.error("In html h5port is null, please init first");
  63. }
  64. }
  65. function postBufferToApp() {
  66. if (h5Port) {
  67. const str = "Hello, World!";
  68. const encoder = new TextEncoder();
  69. const uint8Array = encoder.encode(str);
  70. h5Port.postMessage(uint8Array.buffer);
  71. } else {
  72. console.error("In html h5port is null, please init first");
  73. }
  74. }

  76. function postJsonToApp() {
  77. if (h5Port) {
  78. var e = {"json": "json"};
  79. h5Port.postMessage(e);
  80. } else {
  81. console.error("In html h5port is null, please init first");
  82. }
  83. }

  85. function postArrayStringToApp() {
  86. if (h5Port) {
  87. h5Port.postMessage(["1", "2", "3"]);
  88. } else {
  89. console.error("In html h5port is null, please init first");
  90. }
  91. }

  93. function postNumberToApp() {
  94. if (h5Port) {
  95. h5Port.postMessage(123);
  96. } else {
  97. console.error("In html h5port is null, please init first");
  98. }
  99. }
  100. class MyClass {
  101. constructor() {
  102. // 构造器
  103. this.myProperty = 'Hello, World!';
  104. }

  106. myMethod() {
  107. // 实例方法
  108. console.info(this.myProperty);
  109. }

  111. static myStaticMethod() {
  112. // 静态方法
  113. console.info('This is a static method.');
  114. }
  115. }
  116. function postObjectToApp() {
  117. if (h5Port) {
  118. h5Port.postMessage(new MyClass());
  119. } else {
  120. console.error("In html h5port is null, please init first");
  121. }
  122. }

  124. </script>
  125. </html>
  ```
* ArkTS侧代码

  ```
  1. import testNapi from 'libentry.so';
  2. import { webview } from '@kit.ArkWeb';
  3. import { BusinessError } from '@kit.BasicServicesKit';

  5. @Entry
  6. @Component
  7. struct Index {
  8. @State webTag: string = 'postMessage';
  9. controller: webview.WebviewController = new webview.WebviewController(this.webTag);
  10. @State h5Log: string = 'Display received message send from HTML';

  12. aboutToAppear() {
  13. webview.WebviewController.setWebDebuggingAccess(true);
  14. // 初始化web Native Development Kit
  15. testNapi.nativeWebInit(this.webTag);
  16. }

  18. aboutToDisAppear() {
  19. console.error('aboutToDisAppear');
  20. }

  22. build() {
  23. Scroll() {
  24. Column({ space: 10 }) {
  25. // 展示H5接收到的内容
  26. Text('H5_Side_Message_Display_From_App')
  27. TextArea({text: this.h5Log})
  28. .id('log_area')
  29. .width('100%')
  30. .height(100)
  31. .border({ width: 1 })
  32. Text('App_Side_Button')
  33. Row() {
  34. Button('createNoControllerTagPort')
  35. .id('create_no_tag_btn')
  36. .onClick(() => {
  37. try {
  38. testNapi.createWebMessagePorts('noTag');
  39. } catch (error) {
  40. console.error(
  41. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  42. }
  43. })
  44. Button('createPort')
  45. .id('create_port_btn')
  46. .onClick(() => {
  47. try {
  48. testNapi.createWebMessagePorts(this.webTag);
  49. } catch (error) {
  50. console.error(
  51. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  52. }
  53. })
  54. }

  56. Row({ space: 10 }) {

  58. Button('setHandler')
  59. .id('set_handler_btn')
  60. .onClick(() => {
  61. try {
  62. testNapi.setMessageEventHandler(this.webTag);
  63. } catch (error) {
  64. console.error(
  65. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  66. }
  67. })

  69. Button('setHandlerThread')
  70. .id('set_handler_thread_btn')
  71. .onClick(() => {
  72. try {
  73. testNapi.setMessageEventHandlerThread(this.webTag);
  74. } catch (error) {
  75. console.error(
  76. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  77. }
  78. })
  79. }

  81. Row({ space: 10 }) {
  82. Button('SendString')
  83. .id('send_string_btn')
  84. .onClick(() => {
  85. try {
  86. this.h5Log = ''
  87. testNapi.postMessage(this.webTag);
  88. } catch (error) {
  89. console.error(
  90. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  91. }
  92. })
  93. Button('SendStringThread')
  94. .id('send_string_thread_btn')
  95. .onClick(() => {
  96. try {
  97. this.h5Log = ''
  98. testNapi.postMessageThread(this.webTag);
  99. } catch (error) {
  100. console.error(
  101. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  102. }
  103. })
  104. }

  106. Row({ space: 10 }) {
  107. Button('SendBuffer')
  108. .id('send_buffer_btn')
  109. .onClick(() => {
  110. try {
  111. this.h5Log = ''
  112. testNapi.postBufferMessage(this.webTag);
  113. } catch (error) {
  114. console.error(
  115. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  116. }
  117. })
  118. Button('SendNone')
  119. .id('send_none_btn')
  120. .onClick(() => {
  121. try {
  122. this.h5Log = ''
  123. testNapi.postNoneMessage(this.webTag);
  124. } catch (error) {
  125. console.error(
  126. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  127. }
  128. })
  129. }

  131. Row({ space: 10 }) {

  133. Button('closePort')
  134. .id('close_port_btn')
  135. .onClick(() => {
  136. try {
  137. testNapi.closeMessagePort(this.webTag);
  138. } catch (error) {
  139. console.error(
  140. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  141. }
  142. })
  143. Button('destroyNullPort')
  144. .id('destroy_null_btn')
  145. .onClick(() => {
  146. try {
  147. testNapi.destroyNullMessagePort(this.webTag);
  148. } catch (error) {
  149. console.error(
  150. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  151. }
  152. })
  153. Button('destroyPort')
  154. .id('destroy_port_btn')
  155. .onClick(() => {
  156. try {
  157. testNapi.destroyMessagePort(this.webTag);
  158. } catch (error) {
  159. console.error(
  160. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  161. }
  162. })
  163. }
  164. .width('100%')
  165. .padding(10)
  166. .border({ width: 1 })

  168. Column({ space: 10 }) {
  169. Text('H5_Side_Send_Button')
  170. Row({ space: 10 }) {
  171. Button('H5String')
  172. .id('h5_send_string_btn')
  173. .onClick(() => {
  174. try {
  175. this.controller.runJavaScript('for(var i = 0; i < 2000; i++) postStringToApp()');
  176. } catch (error) {
  177. console.error(
  178. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  179. }
  180. })
  181. Button('H5Buffer')
  182. .id('h5_send_buffer_btn')
  183. .onClick(() => {
  184. try {
  185. this.controller.runJavaScript('postBufferToApp()');
  186. } catch (error) {
  187. console.error(
  188. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  189. }
  190. })
  191. Button('H5Number')
  192. .id('h5_send_number_btn')
  193. .onClick(() => {
  194. try {
  195. this.controller.runJavaScript('postNumberToApp()');
  196. } catch (error) {
  197. console.error(
  198. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  199. }
  200. })
  201. }

  203. Row({ space: 10 }) {
  204. Button('H5Json')
  205. .id('h5_send_json_btn')
  206. .onClick(() => {
  207. try {
  208. this.controller.runJavaScript('postJsonToApp()');
  209. } catch (error) {
  210. console.error(
  211. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  212. }
  213. })
  214. Button('H5Array')
  215. .id('h5_send_array_btn')
  216. .onClick(() => {
  217. try {
  218. this.controller.runJavaScript('postArrayStringToApp()');
  219. } catch (error) {
  220. console.error(
  221. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  222. }
  223. })
  224. Button('H5Object')
  225. .id('h5_send_object_btn')
  226. .onClick(() => {
  227. try {
  228. this.controller.runJavaScript('postObjectToApp()');
  229. } catch (error) {
  230. console.error(
  231. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  232. }
  233. })
  234. }
  235. }
  236. .width('100%')
  237. .margin(10)
  238. .padding(10)
  239. .border({ width: 1 })

  241. Web({ src: $rawfile('index.html'), controller: this.controller })
  242. .onConsole((event) => {
  243. if (event) {
  244. let msg = event.message.getMessage();
  245. if (msg.startsWith('H5')) {
  246. this.h5Log = event.message.getMessage() + '\n' + this.h5Log;
  247. }
  248. }
  249. return false;
  250. })
  251. }
  252. }.height('100%')
  253. .scrollable(ScrollDirection.Vertical)
  254. .scrollBar(BarState.Off)
  255. .edgeEffect(EdgeEffect.Spring)
  256. }
  257. }
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseFrontendJSApp/entry5/src/main/ets/pages/Index.ets#L16-L274)
* Node-API侧暴露ArkTS接口

  ```
  1. // entry5/src/main/cpp/types/libentry5/index.d.ts
  2. export const nativeWebInit: (webName: string) => void;
  3. export const createWebMessagePorts: (webName: string) => void;
  4. export const postMessage: (webName: string) => void;
  5. export const postNoneMessage: (webName: string) => void;
  6. export const setMessageEventHandler: (webName: string) => void;
  7. export const closeMessagePort: (webName: string) => void;
  8. export const destroyMessagePort: (webName: string) => void;
  9. export const postBufferMessage: (webName: string) => void;
  10. export const destroyNullMessagePort: (webName: string) => void;
  11. export const setMessageEventHandlerThread: (webName: string) => void;
  12. export const postMessageThread: (webName: string) => void;
  ```

  [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseFrontendJSApp/entry5/src/main/cpp/types/libentry5/Index.d.ts#L16-L29)
* Node-API侧编译配置

  ```
  1. # entry/src/main/cpp/CMakeLists.txt
  2. # the minimum version of CMake.
  3. cmake_minimum_required(VERSION 3.4.1)
  4. project(NDKPostMessage)

  6. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

  8. if(DEFINED PACKAGE_FIND_FILE)
  9. include(${PACKAGE_FIND_FILE})
  10. endif()

  12. include_directories(${NATIVERENDER_ROOT_PATH}
  13. ${NATIVERENDER_ROOT_PATH}/include)

  15. add_library(entry SHARED hello.cpp)

  17. find_library(
  18. # Sets the name of the path variable.
  19. hilog-lib
  20. # Specifies the name of the NDK library that
  21. # you want CMake to locate.
  22. hilog_ndk.z
  23. )

  25. target_link_libraries(entry PUBLIC libace_napi.z.so ${hilog-lib} libohweb.so)
  ```
* Node-API层代码

  ```
  1. #include "hilog/log.h"
  2. #include "napi/native_api.h"
  3. #include "web/arkweb_interface.h"
  4. #include <string>
  5. #include <thread>

  7. constexpr unsigned int LOG_PRINT_DOMAIN = 0xFF00;
  8. ArkWeb_ControllerAPI *controller = nullptr;

  10. ArkWeb_WebMessagePortAPI *webMessagePort = nullptr;
  11. ArkWeb_WebMessageAPI *webMessage = nullptr;
  12. size_t g_webMessagePortSize = 0;
  13. ArkWeb_WebMessagePortPtr *g_web_message_port_arr = nullptr;

  15. static void WebMessagePortCallback(
  16. const char *webTag, const ArkWeb_WebMessagePortPtr port, const ArkWeb_WebMessagePtr message, void *userData)
  17. {
  18. OH_LOG_Print(
  19. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  20. "Native Development Kit WebMessagePortCallback webTag:%{public}s,messageType:%{public}d",
  21. webTag, webMessage->getType(message));
  22. size_t len = 0;
  23. void *back = webMessage->getData(message, &len);
  24. if (webMessage->getType(message) == ArkWeb_WebMessageType::ARKWEB_STRING) {
  25. OH_LOG_Print(
  26. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  27. "Native Development Kit WebMessagePortCallback message:%{public}s,messageSize:%{public}d", back, len);
  28. } else if (webMessage->getType(message) == ArkWeb_WebMessageType::ARKWEB_BUFFER) {
  29. OH_LOG_Print(
  30. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  31. "Native Development Kit WebMessagePortCallback messageSize:%{public}d", len);
  32. }
  33. }

  35. static napi_value NativeWebInit(napi_env env, napi_callback_info info)
  36. {
  37. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "Native Development Kit NativeWebInit start");
  38. size_t argc = 1;
  39. napi_value args[1] = {nullptr};
  40. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
  41. // 获取第一个参数webTag
  42. size_t webTagSize = 0;
  43. napi_get_value_string_utf8(env, args[0], nullptr, 0, &webTagSize);
  44. char *webTagValue = new (std::nothrow) char[webTagSize + 1];
  45. size_t webTagLength = 0;
  46. napi_get_value_string_utf8(env, args[0], webTagValue, webTagSize + 1, &webTagLength);
  47. OH_LOG_Print(
  48. LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb",
  49. "Native Development Kit NativeWebInit webTag:%{public}s", webTagValue);

  51. controller = reinterpret_cast<ArkWeb_ControllerAPI *>(OH_ArkWeb_GetNativeAPI(ARKWEB_NATIVE_CONTROLLER));
  52. if (controller)
  53. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "get ArkWeb_ControllerAPI success");

  55. webMessagePort =
  56. reinterpret_cast<ArkWeb_WebMessagePortAPI *>(OH_ArkWeb_GetNativeAPI(ARKWEB_NATIVE_WEB_MESSAGE_PORT));
  57. if (webMessagePort)
  58. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "get ArkWeb_WebMessagePortAPI success");

  60. webMessage = reinterpret_cast<ArkWeb_WebMessageAPI *>(OH_ArkWeb_GetNativeAPI(ARKWEB_NATIVE_WEB_MESSAGE));
  61. if (webMessage)
  62. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "get ArkWeb_WebMessageAPI success");

  64. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "Native Development Kit NativeWebInit end");
  65. delete[] webTagValue;
  66. return nullptr;
  67. }

  69. static napi_value createWebMessagePorts(napi_env env, napi_callback_info info)
  70. {
  71. size_t argc = 2;
  72. napi_value args[2] = {nullptr};
  73. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

  75. // 获取第一个参数webTag
  76. size_t webTagSize = 0;
  77. napi_get_value_string_utf8(env, args[0], nullptr, 0, &webTagSize);
  78. char *webTagValue = new (std::nothrow) char[webTagSize + 1];
  79. size_t webTagLength = 0;
  80. napi_get_value_string_utf8(env, args[0], webTagValue, webTagSize + 1, &webTagLength);
  81. OH_LOG_Print(
  82. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  83. "Native Development Kit Refresh webTag:%{public}s", webTagValue);

  85. // 初始化端口
  86. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "Native Development Kit createWebMessagePorts begin");
  87. g_web_message_port_arr = controller->createWebMessagePorts(webTagValue, &g_webMessagePortSize);
  88. // 把其中一个端口发送给HTML
  89. ArkWeb_ErrorCode code =
  90. controller->postWebMessage(webTagValue, "init_web_messageport", g_web_message_port_arr, 1, "*");
  91. OH_LOG_Print(
  92. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  93. "Native Development Kit postWebMessage ArkWeb_ErrorCode:%{public}d", code);
  94. OH_LOG_Print(
  95. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  96. "Native Development Kit createWebMessagePorts end, web message port size:%{public}d", g_webMessagePortSize);
  97. delete[] webTagValue;
  98. return nullptr;
  99. }

  101. static napi_value postMessage(napi_env env, napi_callback_info info)
  102. {
  103. size_t argc = 2;
  104. napi_value args[2] = {nullptr};
  105. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

  107. // 获取第一个参数webTag
  108. size_t webTagSize = 0;
  109. napi_get_value_string_utf8(env, args[0], nullptr, 0, &webTagSize);
  110. char *webTagValue = new (std::nothrow) char[webTagSize + 1];
  111. size_t webTagLength = 0;
  112. napi_get_value_string_utf8(env, args[0], webTagValue, webTagSize + 1, &webTagLength);
  113. OH_LOG_Print(
  114. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  115. "Native Development Kit Refresh webTag:%{public}s", webTagValue);

  117. // 发送消息
  118. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "Native Development Kit postMessage begin");

  120. if (g_web_message_port_arr == nullptr) {
  121. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "webMessagePort is nullptr");
  122. return nullptr;
  123. }
  124. ArkWeb_WebMessagePtr message = webMessage->createWebMessage();
  125. webMessage->setType(message, ArkWeb_WebMessageType::ARKWEB_STRING);
  126. std::string str = "send string from native";
  127. webMessage->setData(message, (void *)str.c_str(), str.length() + 1);
  128. ArkWeb_ErrorCode code = webMessagePort->postMessage(g_web_message_port_arr[1], webTagValue, message);
  129. OH_LOG_Print(
  130. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  131. "Native Development Kit postMessage ArkWeb_ErrorCode:%{public}d", code);
  132. webMessage->destroyWebMessage(&message);
  133. OH_LOG_Print(
  134. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  135. "Native Development Kit postMessage end, web message port size:%{public}d", g_webMessagePortSize);
  136. delete[] webTagValue;
  137. return nullptr;
  138. }

  141. // 在线程中发消息
  142. void sendMessage(const char *webTag, const ArkWeb_WebMessagePtr message)
  143. {
  144. // 发送1000次
  145. for (int i = 0; i < 1000; i++) {
  146. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "sendMessage in thread %{public}d", i);
  147. if (g_web_message_port_arr && webTag && message) {
  148. webMessagePort->postMessage(g_web_message_port_arr[1], webTag, message);
  149. }
  150. }
  151. }
  152. static napi_value postMessageThread(napi_env env, napi_callback_info info)
  153. {
  154. size_t argc = 2;
  155. napi_value args[2] = {nullptr};
  156. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

  158. // 获取第一个参数webTag
  159. size_t webTagSize = 0;
  160. napi_get_value_string_utf8(env, args[0], nullptr, 0, &webTagSize);
  161. char *webTagValue = new (std::nothrow) char[webTagSize + 1];
  162. size_t webTagLength = 0;
  163. napi_get_value_string_utf8(env, args[0], webTagValue, webTagSize + 1, &webTagLength);
  164. OH_LOG_Print(
  165. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  166. "Native Development Kit Refresh webTag:%{public}s", webTagValue);

  168. // 构造消息
  169. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "Native Development Kit postMessage begin");

  171. if (g_web_message_port_arr == nullptr) {
  172. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "webMessagePort is nullptr");
  173. return nullptr;
  174. }
  175. ArkWeb_WebMessagePtr message = webMessage->createWebMessage();
  176. webMessage->setType(message, ArkWeb_WebMessageType::ARKWEB_STRING);
  177. std::string str = "thread message";
  178. webMessage->setData(message, (void *)str.c_str(), str.length() + 1);
  179. const int numThreads = 5;
  180. std::thread threads[numThreads];

  182. // 创建线程
  183. for (int i = 0; i < numThreads; ++i) {
  184. threads[i] = std::thread(sendMessage, webTagValue, message);
  185. }

  187. // 等待所有线程完成
  188. for (int i = 0; i < numThreads; ++i) {
  189. threads[i].join();
  190. }
  191. delete[] webTagValue;
  192. return nullptr;
  193. }

  195. // 在线程中注册回调
  196. void SetHandler(const char *webTag)
  197. {
  198. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "setMessageEventHandler in thread");
  199. webMessagePort->setMessageEventHandler(g_web_message_port_arr[1], webTag, WebMessagePortCallback, NULL);
  200. }

  202. static napi_value setMessageEventHandlerThread(napi_env env, napi_callback_info info)
  203. {
  204. size_t argc = 2;
  205. napi_value args[2] = {nullptr};
  206. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

  208. // 获取第一个参数webTag
  209. size_t webTagSize = 0;
  210. napi_get_value_string_utf8(env, args[0], nullptr, 0, &webTagSize);
  211. char *webTagValue = new (std::nothrow) char[webTagSize + 1];
  212. size_t webTagLength = 0;
  213. napi_get_value_string_utf8(env, args[0], webTagValue, webTagSize + 1, &webTagLength);
  214. OH_LOG_Print(
  215. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  216. "Native Development Kit Refresh webTag:%{public}s", webTagValue);

  218. // 注册回调
  219. OH_LOG_Print(
  220. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  221. "Native Development Kit SetMessageEventHandler begin");
  222. if (g_web_message_port_arr == nullptr) {
  223. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "webMessagePort is nullptr");
  224. return nullptr;
  225. }
  226. std::thread thread(SetHandler, webTagValue);
  227. thread.detach();
  228. webMessagePort->setMessageEventHandler(g_web_message_port_arr[1], webTagValue, WebMessagePortCallback, NULL);
  229. OH_LOG_Print(
  230. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  231. "Native Development Kit SetMessageEventHandler end, web message port size:%{public}d", g_webMessagePortSize);
  232. delete[] webTagValue;
  233. return nullptr;
  234. }
  235. static napi_value postNoneMessage(napi_env env, napi_callback_info info)
  236. {
  237. size_t argc = 2;
  238. napi_value args[2] = {nullptr};
  239. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

  241. // 获取第一个参数webTag
  242. size_t webTagSize = 0;
  243. napi_get_value_string_utf8(env, args[0], nullptr, 0, &webTagSize);
  244. char *webTagValue = new (std::nothrow) char[webTagSize + 1];
  245. size_t webTagLength = 0;
  246. napi_get_value_string_utf8(env, args[0], webTagValue, webTagSize + 1, &webTagLength);
  247. OH_LOG_Print(
  248. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN,
  249. "ArkWeb", "Native Development Kit Refresh webTag:%{public}s", webTagValue);

  251. // 发送消息
  252. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "Native Development Kit 发消息开始");

  254. if (g_web_message_port_arr == nullptr) {
  255. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "webMessagePort is nullptr");
  256. return nullptr;
  257. }
  258. ArkWeb_WebMessagePtr message = webMessage->createWebMessage();
  259. webMessage->setType(message, ArkWeb_WebMessageType::ARKWEB_NONE);
  260. std::string str = "send string from native";
  261. webMessage->setData(message, (void *)str.c_str(), str.length() + 1);
  262. webMessagePort->postMessage(g_web_message_port_arr[1], webTagValue, message);
  263. webMessage->destroyWebMessage(&message);
  264. OH_LOG_Print(
  265. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  266. "Native Development Kit postMessage end, web message port size:%{public}d", g_webMessagePortSize);
  267. delete[] webTagValue;
  268. return nullptr;
  269. }

  271. static napi_value postBufferMessage(napi_env env, napi_callback_info info)
  272. {
  273. size_t argc = 2;
  274. napi_value args[2] = {nullptr};
  275. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

  277. // 获取第一个参数webTag
  278. size_t webTagSize = 0;
  279. napi_get_value_string_utf8(env, args[0], nullptr, 0, &webTagSize);
  280. char *webTagValue = new (std::nothrow) char[webTagSize + 1];
  281. size_t webTagLength = 0;
  282. napi_get_value_string_utf8(env, args[0], webTagValue, webTagSize + 1, &webTagLength);
  283. OH_LOG_Print(
  284. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  285. "Native Development Kit Refresh webTag:%{public}s", webTagValue);

  287. // 发送消息
  288. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "Native Development Kit postMessage begin");

  290. if (g_web_message_port_arr == nullptr) {
  291. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "webMessagePort is nullptr");
  292. return nullptr;
  293. }
  294. ArkWeb_WebMessagePtr message1 = webMessage->createWebMessage();
  295. webMessage->setType(message1, ArkWeb_WebMessageType::ARKWEB_BUFFER);
  296. std::string str1 = "send buffer from native";
  297. webMessage->setData(message1, (void *)str1.c_str(), str1.length()+1);
  298. webMessagePort->postMessage(g_web_message_port_arr[1], webTagValue, message1);
  299. webMessage->destroyWebMessage(&message1);
  300. OH_LOG_Print(
  301. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  302. "Native Development Kit postMessage end, web message port size:%{public}d", g_webMessagePortSize);
  303. delete[] webTagValue;
  304. return nullptr;
  305. }

  307. static napi_value setMessageEventHandler(napi_env env, napi_callback_info info)
  308. {
  309. size_t argc = 2;
  310. napi_value args[2] = {nullptr};
  311. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

  313. // 获取第一个参数webTag
  314. size_t webTagSize = 0;
  315. napi_get_value_string_utf8(env, args[0], nullptr, 0, &webTagSize);
  316. char *webTagValue = new (std::nothrow) char[webTagSize + 1];
  317. size_t webTagLength = 0;
  318. napi_get_value_string_utf8(env, args[0], webTagValue, webTagSize + 1, &webTagLength);
  319. OH_LOG_Print(
  320. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  321. "Native Development Kit Refresh webTag:%{public}s", webTagValue);

  323. // 注册回调
  324. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "Native Development Kit SetMessageEventHandler begin");
  325. if (g_web_message_port_arr == nullptr) {
  326. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "webMessagePort is nullptr");
  327. return nullptr;
  328. }
  329. webMessagePort->setMessageEventHandler(g_web_message_port_arr[1], webTagValue, WebMessagePortCallback, NULL);
  330. OH_LOG_Print(
  331. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  332. "Native Development Kit SetMessageEventHandler end, web message port size:%{public}d", g_webMessagePortSize);
  333. delete[] webTagValue;
  334. return nullptr;
  335. }

  337. static napi_value closeMessagePort(napi_env env, napi_callback_info info)
  338. {
  339. size_t argc = 2;
  340. napi_value args[2] = {nullptr};
  341. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

  343. // 获取第一个参数webTag
  344. size_t webTagSize = 0;
  345. napi_get_value_string_utf8(env, args[0], nullptr, 0, &webTagSize);
  346. char *webTagValue = new (std::nothrow) char[webTagSize + 1];
  347. size_t webTagLength = 0;
  348. napi_get_value_string_utf8(env, args[0], webTagValue, webTagSize + 1, &webTagLength);
  349. OH_LOG_Print(
  350. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  351. "Native Development Kit Refresh webTag:%{public}s", webTagValue);

  353. // 关闭端口，先调用close，再调用destroyWebMessagePorts
  354. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "Native Development Kit SetMessageEventHandler begin");
  355. if (g_web_message_port_arr == nullptr) {
  356. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "webMessagePort is nullptr");
  357. return nullptr;
  358. }
  359. webMessagePort->close(g_web_message_port_arr[0], webTagValue);
  360. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  361. "Native Development Kit SetMessageEventHandler end, web message port size:%{public}d", g_webMessagePortSize);
  362. controller->refresh(webTagValue);
  363. delete[] webTagValue;
  364. return nullptr;
  365. }

  367. static napi_value destroyMessagePort(napi_env env, napi_callback_info info)
  368. {
  369. size_t argc = 2;
  370. napi_value args[2] = {nullptr};
  371. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

  373. // 获取第一个参数webTag
  374. size_t webTagSize = 0;
  375. napi_get_value_string_utf8(env, args[0], nullptr, 0, &webTagSize);
  376. char *webTagValue = new (std::nothrow) char[webTagSize + 1];
  377. size_t webTagLength = 0;
  378. napi_get_value_string_utf8(env, args[0], webTagValue, webTagSize + 1, &webTagLength);
  379. OH_LOG_Print(
  380. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  381. "Native Development Kit Refresh webTag:%{public}s", webTagValue);

  383. // 释放内存，先调用close，再调用destroyWebMessagePorts
  384. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "Native Development Kit SetMessageEventHandler begin");
  385. if (g_web_message_port_arr == nullptr) {
  386. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "webMessagePort is nullptr");
  387. return nullptr;
  388. }
  389. controller->destroyWebMessagePorts(&g_web_message_port_arr, g_webMessagePortSize);
  390. OH_LOG_Print(
  391. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  392. "Native Development Kit SetMessageEventHandler end, web message port size:%{public}d", g_webMessagePortSize);
  393. delete[] webTagValue;
  394. return nullptr;
  395. }

  397. static napi_value destroyNullMessagePort(napi_env env, napi_callback_info info)
  398. {
  399. size_t argc = 2;
  400. napi_value args[2] = {nullptr};
  401. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

  403. // 获取第一个参数webTag
  404. size_t webTagSize = 0;
  405. napi_get_value_string_utf8(env, args[0], nullptr, 0, &webTagSize);
  406. char *webTagValue = new (std::nothrow) char[webTagSize + 1];
  407. size_t webTagLength = 0;
  408. napi_get_value_string_utf8(env, args[0], webTagValue, webTagSize + 1, &webTagLength);
  409. OH_LOG_Print(
  410. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  411. "Native Development Kit Refresh webTag:%{public}s", webTagValue);

  413. // 释放内存，先调用close，再调用destroyWebMessagePorts
  414. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "Native Development Kit SetMessageEventHandler begin");

  416. controller->destroyWebMessagePorts(&g_web_message_port_arr, g_webMessagePortSize);

  418. OH_LOG_Print(
  419. LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
  420. "Native Development Kit SetMessageEventHandler end, web message port size:%{public}d", g_webMessagePortSize);
  421. delete[] webTagValue;
  422. return nullptr;
  423. }

  425. EXTERN_C_START
  426. static napi_value Init(napi_env env, napi_value exports)
  427. {
  428. napi_property_descriptor desc[] = {
  429. {"nativeWebInit", nullptr, NativeWebInit, nullptr, nullptr, nullptr, napi_default, nullptr},
  430. {"createWebMessagePorts", nullptr, createWebMessagePorts, nullptr, nullptr, nullptr, napi_default, nullptr},
  431. {"postMessage", nullptr, postMessage, nullptr, nullptr, nullptr, napi_default, nullptr},
  432. {"postNoneMessage", nullptr, postNoneMessage, nullptr, nullptr, nullptr, napi_default, nullptr},
  433. {"postBufferMessage", nullptr, postBufferMessage, nullptr, nullptr, nullptr, napi_default, nullptr},
  434. {"setMessageEventHandler", nullptr, setMessageEventHandler, nullptr, nullptr, nullptr, napi_default, nullptr},
  435. {"closeMessagePort", nullptr, closeMessagePort, nullptr, nullptr, nullptr, napi_default, nullptr},
  436. {"destroyMessagePort", nullptr, destroyMessagePort, nullptr, nullptr, nullptr, napi_default, nullptr},
  437. {"postMessageThread", nullptr, postMessageThread, nullptr, nullptr, nullptr, napi_default, nullptr},
  438. {"setMessageEventHandlerThread", nullptr, setMessageEventHandlerThread, nullptr, nullptr, nullptr,
  439. napi_default, nullptr},
  440. {"destroyNullMessagePort", nullptr, destroyNullMessagePort, nullptr, nullptr, nullptr, napi_default, nullptr},
  441. };
  442. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
  443. return exports;
  444. }
  445. EXTERN_C_END

  447. static napi_module demoModule = {
  448. .nm_version = 1,
  449. .nm_flags = 0,
  450. .nm_filename = nullptr,
  451. .nm_register_func = Init,
  452. .nm_modname = "entry",
  453. .nm_priv = ((void *)0),
  454. .reserved = {0},
  455. };

  457. extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
  ```

  [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseFrontendJSApp/entry5/src/main/cpp/hello.cpp#L16-L474)
