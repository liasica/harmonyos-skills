---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-rtc
title: 在Web中打开摄像头和麦克风
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 使用网页多媒体 > 在Web中打开摄像头和麦克风
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:79fb67137bb7bd2054c029830c5399a36fd244aaee2424efe6c9d4c6b0b2b629
---

WebRTC（Web Real-Time Communications）是一项实时通讯技术，它允许网络应用或站点在无需中间媒介的情况下建立浏览器之间的点对点（Peer-to-Peer）连接，实现视频流、音频流或其他任意数据的传输。WebRTC所包含的标准使得用户无需安装任何插件或第三方软件即可创建点对点（Peer-to-Peer）的数据共享与音视频会议。WebRTC技术适用于所有现代浏览器和主要平台的本机客户端，其背后的技术作为开放的Web标准实现，并在所有主要浏览器中作为常规JavaScript API提供。

Web组件可以通过W3C标准协议接口访问摄像头和麦克风，通过[onPermissionRequest](../harmonyos-references/arkts-basic-components-web-events.md#onpermissionrequest9)接口接收权限请求通知，需在配置文件中声明相应的音视频权限。

* 使用摄像头和麦克风功能前请在module.json5中添加音视频相关权限，权限的添加方法请参考[在配置文件中声明权限](declare-permissions.md#在配置文件中声明权限)。

  ```
  1. // src/main/resources/base/element/string.json
  2. {
  3. "name": "reason_for_camera",
  4. "value": "reason_for_camera"
  5. },
  6. {
  7. "name": "reason_for_microphone",
  8. "value": "reason_for_microphone"
  9. }
  ```

  ```
  1. // src/main/module.json5
  2. "requestPermissions":[
  3. {
  4. "name" : "ohos.permission.CAMERA",
  5. "reason": "$string:reason_for_camera",
  6. "usedScene": {
  7. "abilities": [
  8. "EntryAbility"
  9. ],
  10. "when":"inuse"
  11. }
  12. },
  13. {
  14. "name" : "ohos.permission.MICROPHONE",
  15. "reason": "$string:reason_for_microphone",
  16. "usedScene": {
  17. "abilities": [
  18. "EntryAbility"
  19. ],
  20. "when":"inuse"
  21. }
  22. }
  23. ]
  ```

通过在JavaScript中调用W3C标准协议接口navigator.mediaDevices.getUserMedia()，该接口用于拉起摄像头和麦克风。constraints参数是一个包含了video和audio两个成员的MediaStreamConstraints对象，用于说明请求的媒体类型。

在下面的示例中，点击前端页面中的开启摄像头按钮再点击onConfirm，打开摄像头和麦克风。

* 应用侧代码。

  ```
  1. import { webview } from '@kit.ArkWeb';
  2. import { BusinessError } from '@kit.BasicServicesKit';
  3. import { abilityAccessCtrl } from '@kit.AbilityKit';

  5. @Entry
  6. @Component
  7. struct WebComponent {
  8. controller: webview.WebviewController = new webview.WebviewController();
  9. uiContext: UIContext = this.getUIContext();

  11. aboutToAppear() {
  12. // 配置Web开启调试模式
  13. webview.WebviewController.setWebDebuggingAccess(true);
  14. // 获取权限请求通知，点击onConfirm按钮后，拉起摄像头和麦克风。
  15. let atManager = abilityAccessCtrl.createAtManager();
  16. atManager.requestPermissionsFromUser(this.uiContext.getHostContext(), ['ohos.permission.CAMERA', 'ohos.permission.MICROPHONE'])
  17. .then((data) => {
  18. console.info('data:' + JSON.stringify(data));
  19. console.info('data permissions:' + data.permissions);
  20. console.info('data authResults:' + data.authResults);
  21. }).catch((error: BusinessError) => {
  22. console.error(`Failed to request permissions from user. Code is ${error.code}, message is ${error.message}`);
  23. })
  24. }

  26. build() {
  27. Column() {
  28. Web({ src: $rawfile('index.html'), controller: this.controller })
  29. .onPermissionRequest((event) => {
  30. if (event) {
  31. this.uiContext.showAlertDialog({
  32. title: 'title',
  33. message: 'text',
  34. primaryButton: {
  35. value: 'deny',
  36. action: () => {
  37. event.request.deny();
  38. }
  39. },
  40. secondaryButton: {
  41. value: 'onConfirm',
  42. action: () => {
  43. event.request.grant(event.request.getAccessibleResource());
  44. }
  45. },
  46. cancel: () => {
  47. event.request.deny();
  48. }
  49. })
  50. }
  51. })
  52. }
  53. }
  54. }
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UsingWebMultimedia/entry/src/main/ets/pages/Index.ets#L15-L70)
* 前端页面index.html代码。

  ```
  1. <!-- index.html -->
  2. <!DOCTYPE html>
  3. <html>
  4. <head>
  5. <meta charset="UTF-8">
  6. </head>
  7. <body>
  8. <video id="video" width="500px" height="500px" autoplay></video>
  9. <canvas id="canvas" width="500px" height="500px"></canvas>
  10. <br>
  11. <input type="button" title="HTML5摄像头" value="开启摄像头" onclick="getMedia()"/>
  12. <script>
  13. function getMedia()
  14. {
  15. let constraints = {
  16. video: {width: 500, height: 500},
  17. audio: true
  18. };
  19. // 获取video摄像头区域
  20. let video = document.getElementById("video");
  21. // 返回的Promise对象
  22. let promise = navigator.mediaDevices.getUserMedia(constraints);
  23. // then()异步，调用MediaStream对象作为参数
  24. promise.then(function(MediaStream) {
  25. video.srcObject = MediaStream;
  26. video.play();
  27. }).catch(function(err) {
  28. console.info(err.name + ": " + err.message);
  29. });
  30. }
  31. </script>
  32. </body>
  33. </html>
  ```
