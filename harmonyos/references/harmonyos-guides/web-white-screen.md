---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-white-screen
title: 定位与解决Web白屏问题
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > Web调试维测 > 定位与解决Web白屏问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9b244221bfcabff5f3d40fda359f1c6271d7bad540397b40998a8b327f8c4bb7
---

Web页面出现白屏的原因众多，本文列举了若干常见白屏问题的排查步骤，供开发者快速定位。

1. 首先排查权限和网络状态。
2. 通过[使用DevTools工具调试前端页面](web-debugging-with-devtools.md)定位具体报错类型（跨域、资源404、JS异常）。
3. 在复杂布局场景中，排查渲染模式及组件约束条件的问题。
4. 处理H5代码兼容性问题。
5. 从日志中排查生命周期和网络加载相关关键字。
6. 检查是否开启[坚盾守护模式](web-secure-shield-mode.md)，坚盾守护模式开启后相关限制见：[ArkWeb限制的HTML5特性](web-secure-shield-mode.md#arkweb限制的html5特性)。

## 检查权限和网络状态

如果应用未开启联网或文件访问权限或者设备网络状态不佳，将导致Web组件加载失败或页面元素缺失，进而引起白屏。

* 验证设备的网络状态，包括是否已连接网络，设备自带的浏览器能否正常访问网页等（在线页面场景）。
* 确保应用已添加网络权限：ohos.permission.INTERNET（在线页面必需）。

  ```
  1. "requestPermissions":[
  2. {
  3. "name" : "ohos.permission.INTERNET"
  4. }
  5. ],
  ```

  [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/WebWriteScreenIssue/entry/src/main/module.json5#L17-L23)
* 开启相关权限：

  | 名称 | 说明 |
  | --- | --- |
  | [domStorageAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#domstorageaccess) | DOM Storage API权限，若不开启，无法使用localStorage存储数据，任何调用localStorage的代码都将失效，依赖本地存储的功能会异常。 |
  | [fileAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#fileaccess) | ‌若不开启，文件读写功能完全被阻断，依赖文件的模块会崩溃。 |
  | [imageAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#imageaccess) | 设置是否允许自动加载图片资源。 |
  | [onlineImageAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#onlineimageaccess) | 设置是否允许从网络加载图片资源（通过HTTP和HTTPS访问的资源）。 |
  | [javaScriptAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#javascriptaccess) | 设置是否允许执行JavaScript脚本。 |

  ```
  1. import { webview } from '@kit.ArkWeb';

  3. @Entry
  4. @Component
  5. struct WebComponent {
  6. controller: webview.WebviewController = new webview.WebviewController();

  8. build() {
  9. Column() {
  10. Web({ src: 'www.example.com', controller: this.controller })
  11. .domStorageAccess(true)
  12. .fileAccess(true)
  13. .imageAccess(true)
  14. .onlineImageAccess(true)
  15. .javaScriptAccess(true)
  16. }
  17. }
  18. }
  ```

  [OpenPermissions.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/WebWriteScreenIssue/entry/src/main/ets/pages/OpenPermissions.ets#L15-L34)
* 修改[UserAgent](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setcustomuseragent10)后再观察页面是否恢复正常。

  ```
  1. import { webview } from '@kit.ArkWeb';
  2. import { BusinessError } from '@kit.BasicServicesKit';

  4. @Entry
  5. @Component
  6. struct WebComponent {
  7. controller: webview.WebviewController = new webview.WebviewController();
  8. @State customUserAgent: string = ' DemoApp';

  10. build() {
  11. Column() {
  12. Web({ src: 'www.example.com', controller: this.controller })
  13. .onControllerAttached(() => {
  14. console.info('onControllerAttached');
  15. try {
  16. let userAgent = this.controller.getUserAgent() + this.customUserAgent;
  17. this.controller.setCustomUserAgent(userAgent);
  18. } catch (error) {
  19. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  20. }
  21. })
  22. }
  23. }
  24. }
  ```

  [ChangeUserAgent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/WebWriteScreenIssue/entry/src/main/ets/pages/ChangeUserAgent.ets#L15-L40)

## 使用DevTools工具进行页面内容验证

在确保网络与权限配置无误后，若仍出现白屏，则应利用DevTools工具调试前端页面以及监听Web相关错误上报接口，来定位具体报错类型。

1. 查阅控制台的错误信息，定位具体的资源加载失败问题。资源加载失败会导致页面元素缺失，布局紊乱，图片和动画效果失效等，严重时可能导致渲染进程崩溃，页面呈现空白。如图所示，依次排查：

   （1）元素是否完整，html元素、结构是否正确。

   （2）控制台是否有报错。

   （3）网络里面是否有资源加载时间特别长等。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/gNB9-Gx3QZCK6W3Oo5Kj-Q/zh-cn_image_0000002552798606.png?HW-CC-KV=V1&HW-CC-Date=20260427T234107Z&HW-CC-Expire=86400&HW-CC-Sign=1052CBA96B09321E50813C62AB34DCD795EBE7B090D0E6DA84762D385171FFC2)
2. 检查控制台，确认是否存在因MixedContent策略或CORS策略导致的异常，或JS错误等。可参考[解决Web组件本地资源跨域问题](web-cross-origin.md)。为了提高安全性，ArkWeb内核禁止file协议和resource协议访问跨域请求。因此，在使用Web组件加载本地离线资源的时候，Web组件会拦截file协议和resource协议的跨域访问。Web组件无法访问本地跨域资源时，DevTools控制台会显示报错信息：

   ```
   1. Access to script at 'xxx' from origin 'xxx' has been blocked by CORS policy: Cross origin requests are only supported for protocol schemes:   http, arkweb, data, chrome-extension, chrome, https, chrome-untrusted.
   ```

   有如下两种解决方法：

   方法一：

   开发者应使用HTTP或HTTPS协议替代file或resource协议，确保Web组件能够成功访问跨域资源。替代的URL域名应为自定义构造，仅限于个人或组织使用，以防止与互联网上的实际域名冲突。此外，开发者需要利用Web组件的[onInterceptRequest](../harmonyos-references/arkts-basic-components-web-events.md#oninterceptrequest9)方法，对本地资源进行拦截和相应替换。

   以下结合示例说明如何使用HTTP或HTTPS等协议解决本地资源跨域访问失败的问题。其中，index.html和js/script.js文件置于工程的rawfile目录下。当使用resource协议访问index.html时，js/script.js文件因跨域而被拦截，无法加载。在示例中，使用https://www.example.com/域名替换了原有的resource协议，同时利用onInterceptRequest接口替换资源，确保js/script.js文件可以成功加载，从而解决跨域拦截问题。

   ```
   1. // main/ets/pages/Index.ets
   2. import { webview } from '@kit.ArkWeb';

   4. @Entry
   5. @Component
   6. struct Index {
   7. @State message: string = 'Hello World';
   8. webviewController: webview.WebviewController = new webview.WebviewController();
   9. // 构造域名和本地文件的映射表
   10. schemeMap = new Map([
   11. ["https://www.example.com/index.html", "index.html"],
   12. ["https://www.example.com/js/script.js", "js/script.js"],
   13. ])
   14. // 构造本地文件和构造返回的格式mimeType
   15. mimeTypeMap = new Map([
   16. ["index.html", 'text/html'],
   17. ["js/script.js", "text/javascript"]
   18. ])

   20. build() {
   21. Row() {
   22. Column() {
   23. // 针对本地index.html,使用HTTP或HTTPS协议代替file协议或者resource协议，并且构造一个属于自己的域名。
   24. // 本例中构造www.example.com为例。
   25. Web({ src: "https://www.example.com/index.html", controller: this.webviewController })
   26. .javaScriptAccess(true)
   27. .fileAccess(true)
   28. .domStorageAccess(true)
   29. .geolocationAccess(true)
   30. .width("100%")
   31. .height("100%")
   32. .onInterceptRequest((event) => {
   33. if (!event) {
   34. return;
   35. }
   36. // 此处匹配自己想要加载的本地离线资源，进行资源拦截替换，绕过跨域
   37. if (this.schemeMap.has(event.request.getRequestUrl())) {
   38. let rawfileName: string = this.schemeMap.get(event.request.getRequestUrl())!;
   39. let mimeType = this.mimeTypeMap.get(rawfileName);
   40. if (typeof mimeType === 'string') {
   41. let response = new WebResourceResponse();
   42. // 构造响应数据，如果本地文件在rawfile下，可以通过如下方式设置
   43. response.setResponseData($rawfile(rawfileName));
   44. response.setResponseEncoding('utf-8');
   45. response.setResponseMimeType(mimeType);
   46. response.setResponseCode(200);
   47. response.setReasonMessage('OK');
   48. response.setResponseIsReady(true);
   49. return response;
   50. }
   51. }
   52. return null;
   53. })
   54. }
   55. .width('100%')
   56. }
   57. .height('100%')
   58. }
   59. }
   ```

   ```
   1. <!-- main/resources/rawfile/index.html -->
   2. <!DOCTYPE html>
   3. <html>
   4. <head>
   5. <meta name="viewport" content="width=device-width,initial-scale=1">
   6. </head>
   7. <body>
   8. <script crossorigin src="./js/script.js"></script>
   9. </body>
   10. </html>
   ```

   ```
   1. // main/resources/rawfile/js/script.js
   2. const body = document.body;
   3. const element = document.createElement('div');
   4. element.textContent = 'success';
   5. body.appendChild(element);
   ```

   方法二：

   通过[setPathAllowingUniversalAccess](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setpathallowinguniversalaccess12)设置一个路径列表。当使用file协议访问该列表中的资源时，允许进行跨域访问本地文件。此外，一旦设置了路径列表，file协议将仅限于访问列表内的资源（此时，[fileAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#fileaccess)的行为将会被此接口行为覆盖）。

   setPathAllowingUniversalAccess放开目录的跨域访问限制是一个高风险操作。基于最小权限原则，当前el1，el2放开的路径是固定的，路径列表中的路径应符合以下任一路径格式：

   1. 应用文件目录通过[Context.filesDir](../harmonyos-references/js-apis-inner-application-context.md#属性)获取，其子目录示例如下：

      * /data/storage/el2/base/files/example
      * /data/storage/el2/base/haps/entry/files/example
   2. 应用资源目录通过[Context.resourceDir](../harmonyos-references/js-apis-inner-application-context.md#属性)获取，其子目录示例如下：

      * /data/storage/el1/bundle/entry/resources/resfile
      * /data/storage/el1/bundle/entry/resources/resfile/example
   3. 从API version 21开始，还包括了应用缓存目录通过[Context.cacheDir](../harmonyos-references/js-apis-inner-application-context.md#属性)获取，其子目录示例如下：

      * /data/storage/el2/base/cache
      * /data/storage/el2/base/haps/entry/cache/example
      * 设置的目录路径中，不允许包含cache/web，否则会抛出异常码401。如果设置目录路径是cache，cache/web也不允许访问。
   4. 从API version 21开始，还包括了应用临时目录通过[Context.tempDir](../harmonyos-references/js-apis-inner-application-context.md#属性)获取，其子目录示例如下：

      * /data/storage/el2/base/temp
      * /data/storage/el2/base/haps/entry/temp/example

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
   19. ])
   20. this.controller.loadUrl('file://' + this.uiContext.getHostContext()!.resourceDir + '/index.html')
   21. } catch (error) {
   22. console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
   23. }
   24. })
   25. .javaScriptAccess(true)
   26. .fileAccess(true)
   27. .domStorageAccess(true)
   28. }
   29. }
   30. }
   ```

   [SetPath.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/WebWriteScreenIssue/entry2/src/main/ets/pages/SetPath.ets#L15-L46)

   HTML示例代码：

   ```
   1. <!-- main/resources/resfile/index.html -->
   2. <!DOCTYPE html>
   3. <html lang="en">

   5. <head>
   6. <meta charset="utf-8">
   7. <title>Demo</title>
   8. <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no, viewport-fit=cover">
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
   1. // main/resources/resfile/js/script.js
   2. const body = document.body;
   3. const element = document.createElement('div');
   4. element.textContent = 'success';
   5. body.appendChild(element);
   ```
3. 查看onErrorReceive、onHttpErrorReceive、onSslErrorEvent、onHttpAuthRequest、onClientAuthenticationRequest等错误上报接口是否有被调用。请根据返回的错误码，对照[网络协议栈错误列表](../harmonyos-references/arkts-apis-neterrorlist.md)进行排查。

   | 名称 | 说明 |
   | --- | --- |
   | [onErrorReceive](../harmonyos-references/arkts-basic-components-web-events.md#onerrorreceive) | 资源加载失败会上报该回调，比如访问内核不支持的scheme， 会报302(UNKNOWN\_URL\_SCHEME)。 |
   | [onHttpErrorReceive](../harmonyos-references/arkts-basic-components-web-events.md#onhttperrorreceive) | 服务器返回HTTP错误码，这类问题一般需要跟服务器进行联调。 |
   | [onHttpAuthRequest](../harmonyos-references/arkts-basic-components-web-events.md#onhttpauthrequest9) | 服务器返回407需要端侧提供用户名密码认证，如果不正确处理，可能会导致加载异常、白屏。 |
   | [onClientAuthenticationRequest](../harmonyos-references/arkts-basic-components-web-events.md#onclientauthenticationrequest9) | 服务器向端侧请求证书，如果不正确处理，会导致页面加载异常。 |
   | [onSslErrorEvent](../harmonyos-references/arkts-basic-components-web-events.md#onsslerrorevent12) | 证书错误，需要应用根据证书错误信息进行排查，是证书配错了？还是过期了。 |

## 复杂的布局与渲染模式导致白屏

若页面使用了复杂布局或渲染模式，需注意其应用场景和约束条件，不当使用可能导致布局混乱或白屏。

Web组件提供了两种渲染模式，能够根据不同的容器大小进行适配，从而满足使用场景中对容器尺寸的需求，详情见[Web组件渲染模式](web-render-mode.md)。在使用过程中需要注意以下几点：

* 异步渲染模式下（renderMode: [RenderMode](../harmonyos-references/arkts-basic-components-web-e.md#rendermode12).ASYNC\_RENDER），Web组件的宽高不能超过7,680px（物理像素），超过会导致白屏。

Web组件提供了自适应页面布局的能力，详情见 [Web组件大小自适应页面内容布局](web-fit-content.md)，使用时也需要注意以下约束条件：

* 配置同步渲染模式：webSetting({renderingMode: WebRenderingMode.SYNCHRONOUS})。
* 关闭滚动效果：webSetting({overScrollMode: OverScrollMode.NEVER})。
* 此模式下不支持动态调整组件高度，确保页面高度固定。
* 避免在FIT\_CONTENT模式下启用键盘避让属性RESIZE\_CONTENT，以免导致布局失效。
* css样式height：<number> vh和Web组件大小自适应页面布局存在计算冲突，请检查height：<number> vh是否是由body节点而内的第一个高度css样式。如以下结构，id为2的dom节点高度将为0，导致白屏。

  ```
  1. <body>
  2. <div id = "1">
  3. <div id = "2" style = "height: 100vh">子dom</div>
  4. <div id = "3" style = "height: 20px">子dom</div>
  5. </div>
  6. </body>
  ```

  解决此白屏问题的参考方案如下：

  + 子dom使用具体高度样式撑开父元素。

    ```
    1. <body>
    2. <div id = "1">
    3. <div id = "2"><div style = "height: 20px"><div/></div>
    4. <div id = "3" style = "height: 20px">子dom</div>
    5. </div>
    6. </body>
    ```
  + 父元素使用实际高度样式。

    ```
    1. <body>
    2. <div id = "1">
    3. <div id = "2" style = "height: 20px">子dom</div>
    4. <div id = "3" style = "height: 20px">子dom</div>
    5. </div>
    6. </body>
    ```

## 处理H5代码兼容性

兼容性问题处理不当也会导致页面白屏。

* 特殊协议拦截。
* 若H5页面调用tel:、mailto:等协议导致白屏，需通过onInterceptRequest拦截并调用系统拨号能力：

  ```
  1. .onInterceptRequest((event) => {
  2. if (event.request.url.startsWith('tel:')) {
  3. // 调用系统拨号能力
  4. call.makeCall({ phoneNumber: '123456' });
  5. return { responseCode: 404 }; // 阻止默认行为
  6. }
  7. return null;
  8. })
  ```

## 监控内存与生命周期

内存达到阈值会导致渲染进程被终止，从而引发白屏现象；同样，渲染进程创建失败或非正常销毁也会导致白屏。可从日志中排查原因。检查Web组件是否与WebController正确绑定，或是否因WebController提前释放导致白屏。关注日志中与Render进程相关的信息：是否存在内存泄漏使渲染内存不足。关键字“MEMORY\_PRESSURE\_LEVEL\_CRITICAL”表明内存已达到阈值，此情形下Web可能遭遇黑屏、花屏或闪屏等异常状况，需排查是否存在内存泄漏问题。Render进程是否成功启动或异常退出。

下面列举一些日志中的关键字和对应的情况说明：

| 日志关键字 | 说明 |
| --- | --- |
| StartRenderProcess failed | 渲染render进程启动失败。 |
| MEMORY\_PRESSURE\_LEVEL\_CRITICAL | 整机内存压力达到阈值，继续使用可能造成黑屏、闪屏白屏等问题。 |
| crashpad SandboxedHandler::HandlerCrash, received signo = xxx | 渲染render进程crash，会造成白屏、Web组件卡死等问题。 |
| SharedContextState context lost via Skia OOM | 共享内存不足，会导致应用闪退、花屏卡死等问题。 |
| CreateNativeViewGLSurfaceEGLOhos::normal surface | 创建egl surface成功，如果没有该日志打印则会造成白屏问题。 |
| INFO: request had no response within 5 seconds | 网络超时。 |
| final url: \*\*\*, error\_code xxx(net::ERR\_XXX) | 主资源加载报错。 |

下面说明一下Web组件网络加载过程中的关键日志，正常情况下一个Web组件的加载过程应该包含这些关键节点：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/B4KhVIY7QqypNjIjXw6YWA/zh-cn_image_0000002583438301.png?HW-CC-KV=V1&HW-CC-Date=20260427T234107Z&HW-CC-Expire=86400&HW-CC-Sign=55EB5ED81269C7815E08BFCF569993C9DCEE0F449BC07AD46225CBB250AF28BF)

| 日志关键字 | 说明 |
| --- | --- |
| NWebRenderMain start | 子进程启动。 |
| RendererMain startup 、  render thread init | 子进程初始化开始。 |
| event\_message: WillProcessNavigationResponse source\_id xxx navigation\_handle id: xxx | 收到主资源的response。 |
| event\_message: commit navigation in main frame, routing\_id: 4, url: \*\*\* | Commit到子进程。 |
| RenderFrameImpl::CommitNavigation、  event\_message: page load start | 子进程收到commit。 |
| NWebHandlerDelegate::OnNavigationEntryCommitted、  event\_message: Commit source\_id xxx | 主进程收到DidCommitNavigation。 |
| event\_message: load\_timing\_info error\_code:0,... | 主资源加载完成，以及各阶段耗时。 |
| event\_message: MarkFirstContentfulPaint | 标记解析到有可显示内容的元素。 |
| NWebHandlerDelegate::OnPageVisible | 第一帧展示。 |
| NWebHandlerDelegate::OnFirstContentfulPaint | 第一帧有内容展示。 |
| event\_message: content load finished | 页面解析完成。 |
| event\_message: page load finished、  NWebHandlerDelegate::OnLoadEnd、  NWebHandlerDelegate::MainFrame OnLoadEnd、  NWebHandlerDelegate::OnFirstMeaningfulPaint | 页面以及子资源加载完成。 |

## 设备的WebView默认加载进程不一致导致加载H5页面白屏

**问题：**

用WebView加载H5在Phone上表现正常，但是在Table/PC/2in1上白屏。

**原因：**

Table/PC/2in1的WebView默认采用多进程加载，iframe默认使用子进程加载。主进程加载完成后，若子进程尚未加载完成，会导致白屏现象。

**解决方案：**

通过[setRenderProcessMode](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setrenderprocessmode12)设置WebView渲染模式为单进程加载。

```
1. webview.WebviewController.setRenderProcessMode(webview.RenderProcessMode.SINGLE);
```
