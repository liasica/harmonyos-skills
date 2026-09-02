---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-163
title: 如何在H5中调用麦克风
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何在H5中调用麦克风
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f7b8e36a8996ae16f84aaf1d7506d6eb16e117b522bd2e136250d5219fa4c1a3
---

## 问题现象

WebView网页端获取麦克风录音权限时，没有成功开启录音。

## 背景知识

* [声明权限](../harmonyos-guides/declare-permissions.md)：应用在申请权限时，需要在项目的配置文件中，逐个声明需要的权限，否则应用将无法获取授权。
* [onPermissionRequest](../harmonyos-references/arkts-basic-components-web-events.md#onpermissionrequest9)：通知收到获取权限请求，需配置"ohos.permission.CAMERA"、"ohos.permission.MICROPHONE"权限。

## 解决方案

1. 在module.json5文件配置'ohos.permission.MICROPHONE'话筒权限。

   ```json
   {
     "module": {
       // ...
       "requestPermissions":[
         {
           "name" : "ohos.permission.MICROPHONE",
           "reason": "$string:micro_reason",
           "usedScene": {
             "abilities": [
               "FormAbility"
             ],
             "when":"inuse"
           }
         },
       ]
     }
   }
   ```
2. Web组件通过onPermissionRequest方法获取话筒权限请求。

   ```ts
   import { webview } from '@kit.ArkWeb';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { abilityAccessCtrl } from '@kit.AbilityKit';

   @Entry
   @Component
   struct Index {
     controller: webview.WebviewController = new webview.WebviewController();

     aboutToAppear() {
       let atManager = abilityAccessCtrl.createAtManager();
       // 通过onPermissionRequest获取权限请求
       atManager.requestPermissionsFromUser(this.getUIContext().getHostContext(), ['ohos.permission.MICROPHONE'])
         .then((data) => {
           console.info(`data: ${JSON.stringify(data)}`);
           console.info(`data permissions: ${data.permissions}`);
           console.info(`data authResults: ${data.authResults}`);

         }).catch((error: BusinessError) => {
         console.error(`Failed to request permissions from user. Code is ${error.code}, message is ${error.message}`);
       });
     }

     build() {
       Column() {
         Web({ src: $rawfile('index.html'), controller: this.controller })
           .geolocationAccess(false)
           .javaScriptAccess(true)
           .fileAccess(true)
           .domStorageAccess(true)
           .onPermissionRequest((event) => {
             if (event) {
               this.getUIContext().showAlertDialog({
                 title: '麦克风权限请求',
                 message: '是否允许获取麦克风权限',
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
           })
       }
     }
   }
   ```

   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>测试网页</title>
       <meta name="viewport" content="initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0,user-scalable=no">
   </head>
   <body>
   <button id="recordButton">录音</button>
   <button id="stopButton" disabled>停止</button>
   <audio id="player" controls preload="auto"></audio>
   </body>
   <script>
       const recordButton = document.getElementById('recordButton');
       const stopButton = document.getElementById('stopButton');
       const player = document.getElementById('player');
       let chunks = [];
       navigator.mediaDevices
           .getUserMedia({ audio: true })
           .then((stream) => {
               const mediaRecorder = new MediaRecorder(stream);
               recordButton.onclick = () => {
                   mediaRecorder.start();
                   stopButton.disabled = false;
                   recordButton.disabled = true;
               };
       
               stopButton.onclick = () => {
                   mediaRecorder.stop();
                   recordButton.disabled = false;
                   stopButton.disabled = true;
               };
       
               mediaRecorder.onstop = (e) => {
                   player.controls = true;
                   const blob = new Blob(chunks, { type: 'audio/mpeg-3' });
                   chunks = [];
                   const audioURL = URL.createObjectURL(blob);
                   player.src = audioURL;
                   player.load();
               };
       
               mediaRecorder.ondataavailable = (e) => {
                   chunks.push(e.data);
               };
           }).catch((err) => {
           console.error(`The following error occurred: ${err}`);
       });
       player.onloadedmetadata = e => {
           const audio = e.target;
           const audioDuration = audio.duration;
           if (audioDuration === Infinity) {
               audio.currentTime = 1e101;
               audio.ontimeupdate = function () {
                   this.ontimeupdate = () => {
                       return;
                   };
                   audio.currentTime = 1e101;
                   audio.currentTime = 0;
               };
           }
       };
   </script>
   </html>
   ```

## 常见FAQ

Q：调用getUserMedia()接口无响应或返回权限拒绝错误。

A：非安全上下文(非HTTPS)下getUserMedia()会被自动拒绝。
