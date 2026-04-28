---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-cross-origin
title: 解决Web组件本地资源跨域问题
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 管理Web组件的网络安全与隐私 > 解决Web组件本地资源跨域问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8db5f276bfff13750c9a3e0ab26d7d16a4294755af88c3f219b85af092b56a75
---

## 拦截本地资源跨域

为了提高安全性，ArkWeb内核禁止file协议和resource协议访问跨域请求。因此，在使用Web组件加载本地离线资源的时候，Web组件会拦截file协议和resource协议的跨域访问。通过方法二设置一个路径列表，再使用file协议访问该路径列表中的资源，允许跨域访问本地文件。Web组件无法访问本地跨域资源时，DevTools控制台会显示报错信息：

```
1. Access to script at 'xxx' from origin 'xxx' has been blocked by CORS policy: Cross origin requests are only supported for protocol schemes: http, arkweb, data, chrome-extension, chrome, https, chrome-untrusted.
```

## 本地资源跨域问题解决方法

* 方法一

  开发者应使用http或https协议替代file或resource协议，使Web组件成功访问跨域资源。替代的URL域名为自定义构造，仅供个人或组织使用，避免与互联网上的实际域名冲突。同时，开发者需使用Web组件的[onInterceptRequest](../harmonyos-references/arkts-basic-components-web-events.md#oninterceptrequest9)方法，对本地资源进行拦截和相应的替换。

  以下结合示例说明如何使用http或者https等协议解决本地资源跨域访问失败的问题。其中，index.html和js/script.js置于工程中的rawfile目录下。当使用resource协议访问index.html时，js/script.js将因跨域而被拦截，无法加载。在示例中，使用https://www.example.com/域名替换了原本的resource协议，同时利用onInterceptRequest接口替换资源，使得js/script.js可以成功加载，从而解决了跨域拦截的问题。

  ```
  1. import { webview } from '@kit.ArkWeb';

  3. @Entry
  4. @Component
  5. struct Index {
  6. @State message: string = 'Hello World';
  7. webviewController: webview.WebviewController = new webview.WebviewController();
  8. // 构造域名和本地文件的映射表
  9. schemeMap = new Map([
  10. ['https://www.example.com/index.html', 'index.html'],
  11. ['https://www.example.com/js/script.js', 'js/script.js'],
  12. ]);
  13. // 构造本地文件和构造返回的格式mimeType
  14. mimeTypeMap = new Map([
  15. ['index.html', 'text/html'],
  16. ['js/script.js', 'text/javascript']
  17. ]);

  19. build() {
  20. Row() {
  21. Column() {
  22. // 针对本地index.html,使用http或者https协议代替file协议或者resource协议，并且构造一个属于自己的域名。
  23. // 本例中构造www.example.com为例。
  24. Web({ src: 'https://www.example.com/index.html', controller: this.webviewController })
  25. .javaScriptAccess(true)
  26. .fileAccess(true)
  27. .domStorageAccess(true)
  28. .geolocationAccess(true)
  29. .width('100%')
  30. .height('100%')
  31. .onInterceptRequest((event) => {
  32. if (!event) {
  33. return;
  34. }
  35. // 此处匹配自己想要加载的本地离线资源，进行资源拦截替换，绕过跨域
  36. if (this.schemeMap.has(event.request.getRequestUrl())) {
  37. let rawfileName: string = this.schemeMap.get(event.request.getRequestUrl())!;
  38. let mimeType = this.mimeTypeMap.get(rawfileName);
  39. if (typeof mimeType === 'string') {
  40. let response = new WebResourceResponse();
  41. // 构造响应数据，如果本地文件在rawfile下，可以通过如下方式设置
  42. response.setResponseData($rawfile(rawfileName));
  43. response.setResponseEncoding('utf-8');
  44. response.setResponseMimeType(mimeType);
  45. response.setResponseCode(200);
  46. response.setReasonMessage('OK');
  47. response.setResponseIsReady(true);
  48. return response;
  49. }
  50. }
  51. return null;
  52. })
  53. }
  54. .width('100%')
  55. }
  56. .height('100%')
  57. }
  58. }
  ```

  [LocCrossOriginResAccSol\_one.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebCompSecPriv/entry/src/main/ets/pages/LocCrossOriginResAccSol_one.ets#L16-L76)

  ```
  1. <!-- main/resources/rawfile/index.html -->
  2. <html>
  3. <head>
  4. <meta name="viewport" content="width=device-width,initial-scale=1">
  5. </head>
  6. <body>
  7. <script crossorigin src="./js/script.js"></script>
  8. </body>
  9. </html>
  ```

  ```
  1. const body = document.body;
  2. const element = document.createElement('div');
  3. element.textContent = 'success';
  4. body.appendChild(element);
  ```

  [script.js](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebCompSecPriv/entry/src/main/resources/rawfile/js/script.js#L16-L22)
* 方法二

  通过[setPathAllowingUniversalAccess](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setpathallowinguniversalaccess12)设置一个路径列表。当使用file协议访问该列表中的资源时，允许进行跨域访问本地文件。此外，一旦设置了路径列表，file协议将仅限于访问列表内的资源（此时，[fileAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#fileaccess)的行为将会被此接口行为覆盖）。

  setPathAllowingUniversalAccess放开目录的跨域访问限制是一个高风险操作。基于最小权限原则，当前el1，el2放开的路径是固定的，路径列表中的路径应符合以下任一路径格式：

  1.应用文件目录通过[Context.filesDir](../harmonyos-references/js-apis-inner-application-context.md#属性)获取，其子目录示例如下：

  + /data/storage/el2/base/files/example
  + /data/storage/el2/base/haps/entry/files/example

  2.应用资源目录通过[Context.resourceDir](../harmonyos-references/js-apis-inner-application-context.md#属性)获取，其子目录示例如下：

  + /data/storage/el1/bundle/entry/resources/resfile
  + /data/storage/el1/bundle/entry/resources/resfile/example

  3.从API version 21开始，还包括了应用缓存目录通过[Context.cacheDir](../harmonyos-references/js-apis-inner-application-context.md#属性)获取，其子目录示例如下：

  + /data/storage/el2/base/cache
  + /data/storage/el2/base/haps/entry/cache/example
  + 设置的目录路径中，不允许包含cache/web，否则会抛出异常码401。如果设置目录路径是cache，cache/web也不允许访问。

  4.从API version 21开始，还包括了应用临时目录通过[Context.tempDir](../harmonyos-references/js-apis-inner-application-context.md#属性)获取，其子目录示例如下：

  + /data/storage/el2/base/temp
  + /data/storage/el2/base/haps/entry/temp/example

  当路径列表中的任一路径不满足上述条件时，系统将抛出异常码401，并判定路径列表设置失败。如果路径列表设置为空，file协议的可访问范围将遵循[fileAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#fileaccess)规则，具体示例如下。

  ```
  1. import { webview } from '@kit.ArkWeb';
  2. import { BusinessError } from '@kit.BasicServicesKit';

  4. @Entry
  5. @Component
  6. struct WebComponent {
  7. controller: WebviewController = new webview.WebviewController();
  8. uiContext: UIContext = this.getUIContext();

  10. build() {
  11. Row() {
  12. Web({ src: '', controller: this.controller })
  13. .onControllerAttached(() => {
  14. try {
  15. // 设置允许可以跨域访问的路径列表
  16. this.controller.setPathAllowingUniversalAccess([
  17. this.uiContext.getHostContext()!.resourceDir,
  18. this.uiContext.getHostContext()!.filesDir + '/example'
  19. ]);
  20. this.controller.loadUrl('file://' + this.uiContext.getHostContext()!.resourceDir + '/index.html');
  21. } catch (error) {
  22. console.error(
  23. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as   BusinessError).message}`);
  24. }
  25. })
  26. .javaScriptAccess(true)
  27. .fileAccess(true)
  28. .domStorageAccess(true)
  29. }
  30. }
  31. }
  ```

  [LocCrossOriginResAccSol\_two.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebCompSecPriv/entry/src/main/ets/pages/LocCrossOriginResAccSol_two.ets#L16-L49)

  ```
  1. <!-- main/resources/resfile/index.html -->
  2. <!DOCTYPE html>
  3. <html lang="en">

  5. <head>
  6. <meta charset="utf-8">
  7. <title>Demo</title>
  8. <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no,   viewport-fit=cover">
  9. <script>
  10. function getFile() {
  11. var file = "file:///data/storage/el1/bundle/entry/resources/resfile/js/script.js";
  12. // 使用file协议通过XMLHttpRequest跨域访问本地js文件。
  13. var xmlHttpReq = new XMLHttpRequest();
  14. xmlHttpReq.onreadystatechange = function(){
  15. console.info("readyState:" + xmlHttpReq.readyState);
  16. console.info("status:" + xmlHttpReq.status);
  17. if(xmlHttpReq.readyState == 4){
  18. if (xmlHttpReq.status == 200) {
  19. // 如果ets侧正确设置路径列表，则此处能正常获取资源
  20. const element = document.getElementById('text');
  21. element.textContent = "load " + file + " success";
  22. } else {
  23. // 如果ets侧不设置路径列表，则此处会触发CORS跨域检查错误
  24. const element = document.getElementById('text');
  25. element.textContent = "load " + file + " failed";
  26. }
  27. }
  28. }
  29. xmlHttpReq.open("GET", file);
  30. xmlHttpReq.send(null);
  31. }
  32. </script>
  33. </head>

  35. <body>
  36. <div class="page">
  37. <button id="example" onclick="getFile()">loadFile</button>
  38. </div>
  39. <div id="text"></div>
  40. </body>

  42. </html>
  ```

```
1. const body = document.body;
2. const element = document.createElement('div');
3. element.textContent = 'success';
4. body.appendChild(element);
```

[script.js](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebCompSecPriv/entry/src/main/resources/resfile/js/script.js#L16-L22)
