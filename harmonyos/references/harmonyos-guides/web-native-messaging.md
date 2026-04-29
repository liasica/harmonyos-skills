---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-native-messaging
title: 使用WebNativeMessagingExtensionAbility组件实现浏览器扩展和应用通信场景
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 使用WebNativeMessagingExtensionAbility组件实现浏览器扩展和应用通信场景
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:31+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:06e842bb11a13d33059d7b273e3fbf5223db5b2a2242c9bd54b64081b54c36a6
---

## 概述

浏览器的扩展程序（extension）支持与系统上安装的应用交换消息，应用向扩展提供服务，帮助扩展实现一些应用才具备的能力，常见的例子是密码管理器：应用负责存储和加密你的密码信息，以便浏览器扩展程序自动填充网页中的表单字段。

从API version 21开始，支持开发者在应用中使用[WebNativeMessagingExtensionAbility](../harmonyos-references/arkts-apis-web-webnativemessagingextensionability.md)组件，为浏览器扩展提供后台服务能力。

浏览器扩展通过[WebExtensions runtime API](https://developer.mozilla.org/zh-CN/docs/Mozilla/Add-ons/WebExtensions/API/runtime)连接WebNativeMessagingExtensionAbility，双方通信是通过共享pipe文件描述符后调用IO接口实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/JsFYnZqSTsSjptRtTJZWLw/zh-cn_image_0000002558605084.png?HW-CC-KV=V1&HW-CC-Date=20260429T052929Z&HW-CC-Expire=86400&HW-CC-Sign=72882719BD9048AAC220BEDDA2F9FDBE96B85EA411B3F1D1D5CC800253A53B2A)

说明

本文将浏览器扩展调用WebExtension接口runtime.connectNative建立的连接称为NativeMessaging连接。

NativeMessaging面向两类开发者：应用开发者和浏览器应用开发者。两者均需要了解WebNativeMessagingExtensionAbility运作机制，但关注的场景和接口不同。应用开发者关注[WebNativeMessagingExtensionAbility](../harmonyos-references/arkts-apis-web-webnativemessagingextensionability.md)组件的使用，负责相关业务开发；浏览器应用开发者负责建立NativeMessaging连接，关注[WebNativeMessagingExtensionManager](../harmonyos-references/arkts-apis-web-webnativemessagingextensionmanager.md)相关接口。

本文会在具体的描述中，特意标注需要哪类开发者关注。

## 约束与限制

### 设备限制

WebNativeMessagingExtensionAbility组件当前仅支持2in1设备。

### 规格限制

* WebNativeMessagingExtensionAbility组件无需额外权限，允许任意三方应用集成使用，但拉起方（浏览器）需申请ACL权限（ohos.permission.WEB\_NATIVE\_MESSAGING）。此权限仅对浏览器类应用开放。
* WebNativeMessagingExtensionAbility组件内不支持调用[Window](../harmonyos-references/arkts-apis-window.md)相关API。
* WebNativeMessagingExtensionAbility仅支持拉起本应用的[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)，不支持拉起其他应用UIAbility或者其他类型ExtensionAbility。
* WebNativeMessagingExtensionAbility仅用于浏览器扩展与应用通信场景，不支持如后台服务等其他场景使用。

## 运作机制

### 整体流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/VzeK4dOyTx6oAxnv7-j4gw/zh-cn_image_0000002589324609.png?HW-CC-KV=V1&HW-CC-Date=20260429T052929Z&HW-CC-Expire=86400&HW-CC-Sign=9D78DFFF213BDA05D4F16B636D2C228CE201B562C1DA44A6158242F0785C9FE9)

* **流程：**

1. **浏览器扩展**调用runtime.connectNative接口传入应用包名，来创建NativeMessaging连接。
2. **浏览器应用**调用[dataShare](share-config.md)获取应用配置信息，包括WebNativeMessagingExtension的名称，和限制访问规则（是否允许某个扩展访问该WebNativeMessagingExtension）。
3. **浏览器应用**创建两组pipe作为收发双向通道，调用[WebNativeMessagingExtensionManager.connectNative](../harmonyos-references/arkts-apis-web-webnativemessagingextensionmanager.md#webnativemessagingextensionmanagerconnectnative)接口，拉起WebNativeMessagingExtension并创建一条NativeMessaging连接，并将pipe的收发文件描述符作为参数传输过去。
4. **应用**WebNativeMessagingExtensionAbility被拉起，[WebNativeMessagingExtensionAbility.onConnectNative](../harmonyos-references/arkts-apis-web-webnativemessagingextensionability.md#onconnectnative)生命周期回调触发，获取pipe的文件描述符。
5. **应用**监听读端的文件描述符，获取浏览器扩展发过来的消息指令，并通过写端的文件描述符发送回去。
6. **应用**使用[WebNativeMessagingExtensionContext.startAbility](../harmonyos-references/arkts-apis-web-webnativemessagingextensioncontext.md#startability)拉起本应用的UIAbility图形界面。

说明

WebNativeMessagingExtensionAbility为单实例独立进程，多次调用connectNative接口仅拉起一个实例，同时触发多次onConnectNative回调，需要**应用**管理多会话场景。

### dataShare存放应用extension配置信息

应用集成WebNativeMessagingExtensionAbility时，需要通过dataShare能力向浏览器应用提供extension配置。该配置用于浏览器应用判断允许访问的扩展及指定要拉起的WebNativeMessagingExtensionAbility名称。

extension配置采用json字符串格式

* abilityName属性：字符串，WebNativeMessagingExtensionAbility名称，用于填充want中abilityName字段，一个应用仅有一个WebNativeMessagingExtensionAbility。
* allowed\_origins属性：数组，允许访问该WebNativeMessagingExtensionAbility的浏览器扩展url信息，可以配置多条，不同浏览器的扩展有不同的scheme协议，例如华为浏览器使用chrome-extension协议头。

extension配置格式：

```
1. {
2. // 应用包名
3. "name": "com.example.myapplication",
4. // 具体描述
5. "description": "Send message to native app.",
6. /*
7. * WebNativeMessagingExtensionAbility名称，用于元能力want填充abilityName，一个应用应只有一个
8. * WebNativeMessagingExtensionAbility
9. */
10. "abilityName": "webExtensionAbility",
11. /*
12. * 允许访问该WebNativeMessagingExtensionAbility的浏览器扩展url信息，不同的浏览器的扩展有不同的scheme协议，华为浏览器使用chrome-extension协议头
13. */
14. "allowed_origins":[
15. "chrome-extension://knldjmfmopnpolahpmmgbagdohdnhkik/"
16. ]
17. }
```

extension配置通过[dataShare配置项](share-config.md#modulejson5-配置)向浏览器应用暴露，具体的配置方式可参考下方[实现一个WebNativeMessagingExtensionAbility（应用开发者）](web-native-messaging.md#实现一个webnativemessagingextensionability应用开发者)中步骤6。其中，uri为固定格式：datashareproxy://[包名]/browserNativeMessagingHosts，value字段填写上述extension配置的JSON字符串，allowList字段填写允许访问该配置的浏览器应用的appIdentifier。

### WebNativeMessagingExtensionAbility生命周期管理

* [onConnectNative](../harmonyos-references/arkts-apis-web-webnativemessagingextensionability.md#onconnectnative)：当浏览器扩展调用一次runtime.connectNative时触发，如果WebNativeMessagingExtensionAbility尚未运行，调用runtime.connectNative会拉起WebNativeMessagingExtensionAbility，并触发该回调。
* [onDisconnectNative](../harmonyos-references/arkts-apis-web-webnativemessagingextensionability.md#ondisconnectnative)：当浏览器扩展销毁runtime.port时，会触发一次该回调，每条NativeMessaging连接的断开，都会触发一次该回调，当全部连接都断开时，会触发onDestroy的回调后关闭WebNativeMessagingExtensionAbility。
* [onDestroy](../harmonyos-references/arkts-apis-web-webnativemessagingextensionability.md#ondestroy)：当WebNativeMessagingExtensionAbility销毁前触发该回调，全部NativeMessaging连接断开会触发WebNativeMessagingExtensionAbility的销毁。
* [stopNativeConnection](../harmonyos-references/arkts-apis-web-webnativemessagingextensioncontext.md#stopnativeconnection)：WebNativeMessagingExtensionAbility可以主动断开一条NativeMessaging连接，如果断开的是最后一条连接，则会触发WebNativeMessagingExtensionAbility的销毁。
* [terminateSelf](../harmonyos-references/arkts-apis-web-webnativemessagingextensioncontext.md#terminateself)：WebNativeMessagingExtensionAbility可以主动退出，触发后会销毁所有NativeMessaging连接。

### 消息格式和限制

NativeMessaging连接使用的具体格式，每个消息都使用JSON进行序列化，编码为UTF-8，并在前面附加32位消息长度（采用原生字节顺序）。来自WebNativeMessagingExtensionAbility的单个消息的大小上限为 1 MB，这主要是为了保护浏览器免受行为异常的应用影响。发送到WebNativeMessagingExtensionAbility的消息大小上限为 64 MB。

### 实现一个connectNative的扩展（应用开发者）

说明

需按w3c标准配置manifest.json和background.js实现通信。

支持使用chrome.runtime.connectNative或chrome.runtime.sendNativeMessage进行连接。

配置插件内容，发送ping字符串并接收pong响应的插件代码，示例如下：

**实现配置manifest.json**

```
1. {
2. "name": "com.example.myapplication",
3. "version": "1.0.1",
4. "description": "Launch APP",
5. "manifest_version": 3,
6. "permissions": ["nativeMessaging", "tabs", "scripting"], // 根据实际场景是否需要进行选择
7. "host_permissions": ["http://*/*", "https://*/*", "ftp://*/*", "file://*/*"], // 根据实际场景选择
8. "background": {
9. "service_worker": "background.js" // 用于运行插件runtime命令
10. },
11. "content_scripts": [
12. {
13. "matches": ["http://*/*", "https://*/*", "ftp://*/*", "file://*/*"], // 根据实际场景选择
14. "js": ["main.js"] // 用于运行插件js命令
15. }
16. ],
17. "action": {
18. "default_popup": "index.html" // 插件页面展示
19. }
20. }
```

**实现main.js**

```
1. // 从html中触发调用
2. function sendMessageToNative() {
3. var message = "ping"; // 发送ping
4. chrome.runtime.sendMessage({
5. type: "sendMessage",
6. message: message
7. }, function (response) {});
8. }
```

**实现配置background.js**

1. 使用chrome.runtime.connectNative连接

   ```
   1. var port = null;
   2. // 监听来自main.js的信息
   3. chrome.runtime.onMessage.addListener(
   4. function (request, sender, sendResponse) {
   5. if (request.type == "sendMessage") {
   6. if (port == null) {
   7. connectToNativeHost();
   8. }
   9. port.postMessage(request.message); // 向应用程序发送信息
   10. }
   11. return true; // 保持消息通道开放
   12. });
   13. function connectToNativeHost() {
   14. var bundleName = "com.example.app"; // 插件对应应用的bundleName
   15. port = chrome.runtime.connectNative(bundleName); // 根据bundleName名得到通信端口port
   16. port.onMessage.addListener(onNativeMessage); // 监听native应用程序是否发来消息
   17. port.onDisconnect.addListener(onDisconnected); // 监听是否断开连接
   18. }
   19. // 接收到来自native程序的消息时触发
   20. async function onNativeMessage(message) {
   21. console.info('接收到从本地应用程序发送来的消息：' + JSON.stringify(message)); // 示例中的pong
   22. }
   23. // 断开连接时触发
   24. function onDisconnected() {
   25. port = null;
   26. }
   ```
2. 使用chrome.runtime.sendNativeMessage连接

   ```
   1. function sendNativeMessage() {
   2. var bundleName = "com.example.app"; // 插件对应应用的bundleName
   3. var nativeMessage = "ping"; // 插件要发给应用的内容
   4. chrome.runtime.sendNativeMessage(
   5. bundleName,
   6. {message: nativeMessage},
   7. function(response) {
   8. // 收到一次应用回复的信息后断开连接
   9. console.info("sendNativeMessage收到应用程序响应:", JSON.stringify (response));
   10. }
   11. )
   12. }
   ```

### 实现一个WebNativeMessagingExtensionAbility（应用开发者）

在DevEco Studio工程中手动新建一个WebNativeMessagingExtensionAbility组件，具体步骤如下：

1. 在工程Module对应的ets目录下，右键选择“New > Directory”，新建一个目录并命名为MyWebNativeMessageExtAbility。
2. 在MyWebNativeMessageExtAbility目录，右键选择“New > ArkTS File”，新建一个文件并命名为MyWebNativeMessageExtAbility.ets。

   其目录结构如下所示：

   ```
   1. ├── ets
   2. │ ├── MyWebNativeMessageExtAbility
   3. │ │   ├── MyWebNativeMessageExtAbility.ets
   4. └
   ```
3. 在MyWebNativeMessageExtAbility.ets文件中，增加导入[WebNativeMessagingExtensionAbility](../harmonyos-references/arkts-apis-web-webnativemessagingextensionability.md)的依赖包，自定义类继承WebNativeMessagingExtensionAbility组件并实现生命周期回调。

   ```
   1. import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import {buffer, util} from '@kit.ArkTS';
   4. import { fileIo } from '@kit.CoreFileKit';

   6. const TAG: string = '[MyWebNativeMessageExtAbility]';
   7. const DOMAIN_NUMBER: number = 0xFF00;

   9. export default class MyWebNativeMessageExtAbility extends WebNativeMessagingExtensionAbility {
   10. // 读取扩展发来的消息，并回复
   11. async ReadAsync(fdRead:number, fdWrite:number) : Promise<void> {
   12. try {
   13. // read
   14. let arrayBuffer = new ArrayBuffer(1024);
   15. let readLen = await fileIo.read(fdRead, arrayBuffer);
   16. if (readLen <= 4) {
   17. hilog.error(DOMAIN_NUMBER, TAG, 'read pipe length failed');
   18. return;
   19. }
   20. hilog.info(DOMAIN_NUMBER, TAG, 'read pipe %{public}s', buffer.from(arrayBuffer, 4, readLen - 4).toString());

   22. // write
   23. let strResponse : string = "pong";
   24. const encoder = new util.TextEncoder("utf-8");
   25. const strBytes = encoder.encodeInto(strResponse);
   26. let bufferLen = strBytes.length;
   27. const lenBytes = new Uint8Array(4);
   28. lenBytes[0] = (bufferLen >> 0) & 0xFF;
   29. lenBytes[1] = (bufferLen >> 8) & 0xFF;
   30. lenBytes[2] = (bufferLen >> 16) & 0xFF;
   31. lenBytes[3] = (bufferLen >> 24) & 0xFF;
   32. const writeBuffer = new Uint8Array(4 + bufferLen);
   33. writeBuffer.set(lenBytes, 0);
   34. writeBuffer.set(strBytes, 4);
   35. let writeLen = await fileIo.write(fdWrite, writeBuffer.buffer);
   36. hilog.info(DOMAIN_NUMBER, TAG, 'write pipe length %{public}d', writeLen);
   37. } catch (err) {
   38. hilog.error(DOMAIN_NUMBER, TAG, 'fileIo failed, error code: ' + err.code + " message: " + err.code);
   39. }
   40. }

   42. onConnectNative(info: ConnectionInfo): void {
   43. hilog.info(DOMAIN_NUMBER, TAG,
   44. `onConnectNative, connectionId ${info.connectionId} caller bundle: ${info.bundleName}, extension origin: ${info.extensionOrigin}, pipe Read: ${info.fdRead}, pipe write ${info.fdWrite}  `);
   45. this.ReadAsync(info.fdRead, info.fdWrite)
   46. }

   48. onDisconnectNative(info: ConnectionInfo): void {
   49. hilog.info(DOMAIN_NUMBER, TAG, `onDisconnectNative, connectionId: ${info.connectionId}`);
   50. }

   52. onDestroy(): void {
   53. hilog.info(DOMAIN_NUMBER, TAG, 'onDestroy');
   54. }
   55. };
   ```
4. 在工程Module的[module.json5配置文件](module-configuration-file.md)中注册WebNativeMessagingExtensionAbility组件。设置type标签为“webNativeMessaging”，srcEntry标签指向组件代码路径。

   ```
   1. {
   2. "module": {
   3. // ...
   4. "extensionAbilities": [
   5. {
   6. "name": "MyWebNativeMessageExtAbility",
   7. "description": "webNativeMessaging",
   8. "type": "webNativeMessaging",
   9. "exported": true,
   10. "srcEntry": "./ets/MyWebNativeMessageExtAbility/MyWebNativeMessageExtAbility.ets"
   11. }
   12. ]
   13. }
   14. }
   ```
5. 在工程Module对应的[module.json5配置文件](module-configuration-file.md)中配置crossAppSharedConfig，定义共享配置项，共享配置文件需放置在工程resources/base/profile目录下，并通过$资源访问方式引用。

   ```
   1. {
   2. "module": {
   3. "crossAppSharedConfig": "$profile:shared_config"
   4. }
   5. }
   ```

6.在shared\_config.json添加[extension配置](web-native-messaging.md#datashare存放应用extension配置信息)。

```
1. {
2. "crossAppSharedConfig": [
3. // ...
4. {
5. // uri固定格式，datashareproxy://[包名]/browserNativeMessagingHosts，浏览器应用通过该uri获取的value，即extension配置。
6. "uri": "datashareproxy://com.example.app/browserNativeMessagingHosts",
7. // extension配置，格式参考extension配置章节的格式，注意转义字符
8. "value": "{\"name\": \"com.example.myapplication\",\"description\": \"Send message to native app.\",\"abilityName\": \"MyWebNativeMessageExtAbility\", \"allowed_origins\":[\"chrome-extension://knldjmfmopnpolahpmmgbagdohdnhkik/\"]}",
9. "allowList": [
10. // 允许访问的应用appIdentifier, 这里加入具体浏览器的appIdentifier
11. "1234567890123456789"
12. ]
13. }
14. ]
15. }
```

### 实现拉起WebNativeMessagingExtensionAbility（浏览器开发者）

浏览器负责实现扩展runtime接口，拉起WebNativeMessagingExtensionAbility，建立和管理NativeMessaging连接。需要申请权限：ohos.permission.WEB\_NATIVE\_MESSAGING。

1. 当接收到创建NativeMessaging连接时，先通过[应用间配置共享接口](../harmonyos-references/js-apis-data-datashare.md#get20)获取目标应用的extension配置。然后读取WebNativeMessagingExtensionAbility名称和允许访问的扩展列表。最后校验是否允许访问。

   ```
   1. import { dataShare } from '@kit.ArkData';

   3. interface ExtensionConfig {
   4. abilityName:string;
   5. allowed_origins:string[];
   6. }

   8. async function getManifestData(bundleName:string, connectExtensionOrigin:string) {
   9. try {
   10. // 调用dataShare接口获取extension配置
   11. const dsProxyHelper = await dataShare.createDataProxyHandle();
   12. const urisToGet = [`datashareproxy://${bundleName}/browserNativeMessagingHosts`];
   13. const config : dataShare.DataProxyConfig = {
   14. type: dataShare.DataProxyType.SHARED_CONFIG,
   15. };
   16. const results = await dsProxyHelper.get(urisToGet, config);
   17. let foundValid = false;
   18. for (let i = 0; i < results.length; i++) {
   19. try {
   20. const result = results[i];
   21. const json = result.value;
   22. if (typeof json !== "string") {
   23. continue;
   24. }
   25. let jsonStr:string = json as string;
   26. let info:ExtensionConfig = JSON.parse(jsonStr);
   27. if (info.abilityName) {
   28. console.info('Native message json info is ok');
   29. if (!Array.isArray(info.allowed_origins)) {
   30. info.allowed_origins = [info.allowed_origins];
   31. }
   32. if (!info.allowed_origins.includes(connectExtensionOrigin)) {
   33. console.error('Origin not allowed, continue searching');
   34. continue;
   35. }
   36. foundValid = true;
   37. break;
   38. }
   39. } catch (error) {
   40. console.error('NativeMessage JSON parse error:', error);
   41. }
   42. }
   43. if (!foundValid) {
   44. console.error('NativeMessage JSON no valid manifest found');
   45. } else {
   46. console.info('NativeMessage allowed_origins match ok');
   47. }
   48. } catch (error) {
   49. console.error('Error getting config:', error);
   50. }
   51. }
   ```
2. 调用[webNativeMessagingExtensionManager.connectNative](../harmonyos-references/arkts-apis-web-webnativemessagingextensionmanager.md#webnativemessagingextensionmanagerconnectnative)创建NativeMessaging连接，如WebNativeMessagingExtensionAbility尚未运行，该接口则会拉起ExtensionAbility并触发。

   ```
   1. import { UIAbility, Want, common } from '@kit.AbilityKit';
   2. import { webNativeMessagingExtensionManager } from '@kit.ArkWeb'

   4. class ConnectionCallback implements webNativeMessagingExtensionManager.WebExtensionConnectionCallback {
   5. onConnect(connection:webNativeMessagingExtensionManager.ConnectionNativeInfo) {
   6. // connected
   7. console.error(`onConnect id ${connection.connectionId} is connected`);
   8. }
   9. onDisconnect(connection:webNativeMessagingExtensionManager.ConnectionNativeInfo) {
   10. // disconnect
   11. console.error(`onDisconnect id ${connection.connectionId} is connected`);
   12. }
   13. onFailed(code:webNativeMessagingExtensionManager.NmErrorCode, errMsg:string) {
   14. console.error(`onFailed error code is ${code}, errMsg is ${errMsg}`);
   15. }
   16. }

   18. function connectNative(abilityContext: common.UIAbilityContext, bundleName: string, abilityName: string,
   19. connectExtensionOrigin: string, readPipe: number, writePipe: number) : void {
   20. try {
   21. let wantInfo:Want = {
   22. bundleName: bundleName,
   23. abilityName: abilityName,
   24. parameters: {
   25. 'ohos.arkweb.messageReadPipe': { 'type': 'FD', 'value': readPipe },
   26. 'ohos.arkweb.messageWritePipe': { 'type': 'FD', 'value': writePipe },
   27. 'ohos.arkweb.extensionOrigin': connectExtensionOrigin
   28. },
   29. };

   31. let options : ConnectionCallback = new ConnectionCallback;
   32. let connectId = webNativeMessagingExtensionManager.connectNative(abilityContext, wantInfo, options);
   33. console.info(`innerWebNativeMessageManager  connectionId : ${connectId}` );
   34. } catch (error) {
   35. console.info(`inner callback error Message: ${JSON.stringify(error)}`);
   36. }
   37. }
   ```
3. 需要销毁NativeMessaging连接时，调用[webNativeMessagingExtensionManager.disconnectNative](../harmonyos-references/arkts-apis-web-webnativemessagingextensionmanager.md#webnativemessagingextensionmanagerdisconnectnative)。

   ```
   1. import { webNativeMessagingExtensionManager } from '@kit.ArkWeb'

   3. function disconnectNative(connectId: number) : void {
   4. console.info(`NativeMessageDisconnect start connectionId is ${connectId}`);
   5. webNativeMessagingExtensionManager.disconnectNative(connectId);
   6. }
   ```
