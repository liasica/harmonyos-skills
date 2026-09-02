---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-171
title: 如何根据Web中的权限请求去动态申请权限
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何根据Web中的权限请求去动态申请权限
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c5a748d4da5cc4cc3e85d29be3a684ff07c98c85172ccf280676424008f43163
---

## 问题现象

如何根据Web的onPermissionRequest回调方法监听网页请求了什么权限，然后通过atManager.requestPermissionsFromUser统一申请权限。

## 背景知识

* [onPermissionRequest](../harmonyos-references/arkts-basic-components-web-events.md#onpermissionrequest9)：通知收到获取权限请求，需配置"ohos.permission.CAMERA"、"ohos.permission.MICROPHONE"权限。具体权限配置可参考[声明权限](../harmonyos-guides/declare-permissions.md)。
* [getAccessibleResource](../harmonyos-references/arkts-basic-components-web-permissionrequest.md#getaccessibleresource9)：获取网页所请求的权限资源列表。
* [requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)：用于UIAbility/UIExtensionAbility拉起弹框请求[用户授权](../harmonyos-guides/request-user-authorization.md)。

## 解决方案

通过Web组件的onPermissionRequest回调方法返回值event.request.getAccessibleResource()获取网页所请求的权限资源列表，随后遍历判断具体的资源类型，添加对应的权限，生成权限列表传给atManager.requestPermissionsFromUser统一申请权限。

具体步骤如下：

1. 允许应用使用相机时需添加相机权限：[ohos.permission.CAMERA](../harmonyos-guides/permissions-for-all-user.md#ohospermissioncamera)，允许应用使用麦克风时需添加麦克风权限：[ohos.permission.MICROPHONE](../harmonyos-guides/permissions-for-all-user.md#ohospermissionmicrophone)，具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。
2. 根据Web中的权限请求向用户手动授权，示例代码如下：

   ```ts
   import { webview } from '@kit.ArkWeb';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';

   @Entry
   @Component
   struct WebPermissionsPage {
     controller: webview.WebviewController = new webview.WebviewController();
     uiContext: UIContext = this.getUIContext();

     requestPermissions(arr: Array<string>) {
       let permissionList: Array<Permissions> = [];
       arr.forEach((it) => {
         if (it.toString() === 'TYPE_VIDEO_CAPTURE') {
           permissionList.push('ohos.permission.CAMERA');
           permissionList.push('ohos.permission.MICROPHONE');
         } else if (it.toString() === 'TYPE_AUDIO_CAPTURE') {
           permissionList.push('ohos.permission.MICROPHONE');
         }
       });
       let atManager = abilityAccessCtrl.createAtManager();
       atManager.requestPermissionsFromUser(this.getUIContext().getHostContext() as Context, permissionList)
         .then((data) => {
           console.info('data permissions:' + data.permissions);
           console.info('data authResults:' + data.authResults);
         }).catch((error: BusinessError) => {
         console.error(`Failed to request permissions from user. Code is ${error.code}, message is ${error.message}`);
       });
     }

     build() {
       Column() {
         Web({ src: $rawfile('webPermissions.html'), controller: this.controller })
           .fileAccess(false)
           .geolocationAccess(false)
           .metaViewport(true)
           .onPermissionRequest((event) => {
             if (event) {
               this.requestPermissions(event.request.getAccessibleResource());
               this.uiContext.showAlertDialog({
                 title: 'title',
                 message: 'text',
                 primaryButton: {
                   value: 'deny',
                   action: () => {
                     event.request.deny();
                   }
                 },
                 secondaryButton: {
                   value: 'onConfirm',
                   action: () => {
                     event.request.grant(event.request.getAccessibleResource());
                   }
                 },
                 cancel: () => {
                   event.request.deny();
                 }
               });
             }
           });
       };
     }
   }
   ```
3. webPermissions.html示例代码如下：

   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
   </head>
   <body>
   <video id="video" autoplay="autoplay"></video>
   <canvas id="canvas"></canvas>
   <br>
   <input type="button" title="HTML5摄像头" style="width: 200px; height: 40px;" value="开启摄像头" onclick="getMedia()"/>
   <script>
       function getMedia() {
          let constraints = {
             video: {width: 500, height: 500},
             audio: true
          };
          // 获取video摄像头区域
          let video = document.getElementById("video");
          // 返回的Promise对象
          let promise = navigator.mediaDevices.getUserMedia(constraints);
          // then()异步，调用MediaStream对象作为参数
          promise.then(function (MediaStream) {
             video.srcObject = MediaStream;
             video.play();
          });
       }

      function test(text) {
         let output = document.getElementById("container");
         output.innerText = text;
         return 'html_' + text;
       }
   </script>
   <div>
       <span>message: </span> <span id="container"></span>
   </div>
   </body>
   </html>
   ```

## 常见FAQ

Q：通过event.request.getAccessibleResource获取网页所请求的权限类型有（TYPE\_MIDI\_SYSEX、TYPE\_VIDEO\_CAPTURE 、TYPE\_AUDIO\_CAPTURE、TYPE\_SENSOR）四种，如何通过这四种枚举判断是请求了什么权限？

A：[ProtectedResourceType](../harmonyos-references/arkts-basic-components-web-e.md#protectedresourcetype9)枚举有4种类型：

1. TYPE\_MIDI\_SYSEX目前还不支持申请使用midi设备相关的权限；
2. TYPE\_VIDEO\_CAPTURE是视频捕获资源，可申请[ohos.permission.CAMERA](../harmonyos-guides/permissions-for-all-user.md#ohospermissioncamera)相机权限；
3. TYPE\_AUDIO\_CAPTURE是音频捕获资源，可申请[ohos.permission.MICROPHONE](../harmonyos-guides/permissions-for-all-user.md#ohospermissionmicrophone)麦克风权限；
4. TYPE\_SENSOR是传感器资源，可申请[ohos.permission.ACCELEROMETER](../harmonyos-guides/permissions-for-all.md#ohospermissionaccelerometer)加速度传感器和[ohos.permission.GYROSCOPE](../harmonyos-guides/permissions-for-all.md#ohospermissiongyroscope)陀螺仪传感器。

具体使用详情可以参考文档：[onPermissionRequest](../harmonyos-references/arkts-basic-components-web-events.md#onpermissionrequest9)和[使用运动和方向传感器监测设备状态](../harmonyos-guides/web-sensor.md)。
