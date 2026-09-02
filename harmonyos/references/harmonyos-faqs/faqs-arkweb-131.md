---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-131
title: 通过网页拉起摄像头/麦克风实现拍照、录音录像、视频通话和拉起图库等功能
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 通过网页拉起摄像头/麦克风实现拍照、录音录像、视频通话和拉起图库等功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5aa7809c70f79be96267714c3fa952c0ac55e62fbeabb2c0552175517a09e329
---

## 问题现象

使用Web组件嵌入H5网页时，如下四个场景分别如何实现：

场景一：调用系统相机实现拍照录像。

场景二：调用系统相机和麦克风实现视频通话预览。

场景三：调用系统相册图库。

场景四：调用系统麦克风录音。

## 背景知识

* <input type="file">是HTML标准中用于文件选择的元素。在HarmonyOS的Web组件中，该元素的行为由系统底层的picker服务实现，而非浏览器原始的文件选择器。
* [onShowFileSelector](../harmonyos-references/arkts-basic-components-web-events.md#onshowfileselector9)：调用此函数以处理具有“文件”输入类型的HTML表单。如果不调用此函数或返回false，Web组件会提供默认的“选择文件”处理界面。如果返回true，应用可以自定义“选择文件”的响应行为。
* Web组件可以通过W3C标准协议接口拉起摄像头和麦克风，通过在JavaScript中调用W3C标准协议接口navigator.mediaDevices.getUserMedia()，该接口用于拉起摄像头和麦克风。constraints参数是一个包含了video和audio两个成员的MediaStreamConstraints对象，用于说明请求的媒体类型。
* [onPermissionRequest](../harmonyos-references/arkts-basic-components-web-events.md#onpermissionrequest9)：通知收到获取权限请求，需配置"ohos.permission.CAMERA"、"ohos.permission.MICROPHONE"权限。具体权限配置可参考[声明权限](../harmonyos-guides/declare-permissions.md)。

## 解决方案

* **场景一：调用系统相机实现拍照录像。**
  1. **H5实现方案**：通过H5的<input type="file">的capture属性，直接拉起系统相机，无需申请权限。

     ```ts
     import { webview } from '@kit.ArkWeb';

     @Entry
     @Component
     struct SolutionOne {
       controller: webview.WebviewController = new webview.WebviewController();

       build() {
         Column() {
           Web({ src: $rawfile('videoCapture.html'), controller: this.controller })
             .fileAccess(false)
             .geolocationAccess(false);
         };
       }
     }
     ```

     ```html
     <!-- videoCapture.html -->
     <!DOCTYPE html>
     <html>
     <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
     </head>
     <body>
     <p>
         <!-- 拉起系统相机拍照 -->
         <input type="file" accept="image/*" capture="user"/>
     </p>
     <p>
         <!-- 拉起系统相机录像 -->
         <input type="file" accept="video/*" capture="user"/>
     </p>
     </body>
     </html>
     ```

     注意：本场景下，底层实际是调用的picker接口拉起的相机，使得应用能够便捷地访问系统资源，由于picker本身不需要授权，并且有安全机制保障，所以对外表现上无须授权即可拉起，实际拉起相机后会出现“安全访问”的提示，所以并非越权行为。

     其中的type，accept以及capture存在不同的取值，可进行组合实现不同的场景需要，属性组合表如下：

     + 用前置摄像头拍照<input type="file" accept="image/\*" capture="user"> 。
     + 用前置摄像头录像<input type="file" accept="video/\*" capture="user"> 。
     + 用后置摄像头拍照<input type="file" accept="image/\*" capture="environment">。
     + 用后置摄像头录像<input type="file" accept="video/\*" capture="environment">。
     + 从相册选择图片或拍照<input type="file" accept="image/\*">。
  2. **ArkTS层实现方案**：
     + 方案一：通过ArkTS中的startAbility能力拉起相机。

       ```ts
       import { common, Want } from '@kit.AbilityKit';
       import { BusinessError } from '@kit.BasicServicesKit';
       import { webview } from '@kit.ArkWeb';

       @Entry
       @Component
       struct SolutionTwo {
         uiContext: UIContext = this.getUIContext();
         webviewController: webview.WebviewController = new webview.WebviewController();

         invokeCamera(callback: (uri: string) => void) {
           const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
           let want: Want = {
             action: 'ohos.want.action.imageCapture',
             parameters: {
               'callBundleName': context.abilityInfo.bundleName,
             }
           };
           let result: (error: BusinessError, data: common.AbilityResult) => void =
             (error: BusinessError, data: common.AbilityResult) => {
               if (error && error.code !== 0) {
                 console.info(`error:${error.message}`);
                 return;
               }
               let resultUri: string = data.want?.parameters?.resourceUri as string;
               if (callback && resultUri) {
                 callback(resultUri);
               }
             };
           context.startAbilityForResult(want, result);
         }

         build() {
           Column() {
             Web({ src: $rawfile("webCamera.html"), controller: this.webviewController })
               .onShowFileSelector((event) => {
                 this.invokeCamera((uri) => {
                   console.info(`uri:${uri}`);
                   event.result.handleFileList([uri]);
                 });
                 return true;
               })
               .fileAccess(false)
               .geolocationAccess(false)
           }
           .height('100%')
           .width('100%')
         };
       }
       ```

       其中不同的action取值可用于选择拍照或者录像：ohos.want.action.videoCapture为拉起相机进行录像，ohos.want.action.imageCapture为拉起相机进行拍照。
     + 方案二：使用onShowFileSelector拉起相机。

       ```ts
       import { webview } from '@kit.ArkWeb';
       import { camera, cameraPicker } from '@kit.CameraKit';
       import { BusinessError } from '@kit.BasicServicesKit';
       import { common } from '@kit.AbilityKit';

       async function openCamera(callback: Callback<string>, uiContext: UIContext) {
         let mContext = uiContext.getHostContext() as common.Context;
         try {
           let pickerProfile: cameraPicker.PickerProfile = {
             cameraPosition: camera.CameraPosition.CAMERA_POSITION_BACK
           };
           let pickerResult: cameraPicker.PickerResult = await cameraPicker.pick(mContext,
             [cameraPicker.PickerMediaType.PHOTO, cameraPicker.PickerMediaType.VIDEO], pickerProfile);
           callback(pickerResult.resultUri);
         } catch (error) {
           let err = error as BusinessError;
           console.error(`the pick call failed. error code: ${err.code}`);
         }
       }

       @Entry
       @Component
       struct SolutionThree {
         webviewController: webview.WebviewController = new webview.WebviewController();

         build() {
           Column() {
             Web({ src: $rawfile("webCamera.html"), controller: this.webviewController })
               .onShowFileSelector((event) => {
                 openCamera((result) => {
                   if (event) {
                     event.result.handleFileList([result]);
                   }
                 }, this.getUIContext())
                 return true;
               })
               .fileAccess(false)
               .geolocationAccess(false)
           }
           .height('100%')
           .width('100%')
         }
       }
       ```

       ```html
       <!-- webCamera.html -->
       <!DOCTYPE html>
       <html lang="en">
       <head>
           <meta charset="UTF-8">
           <meta name="viewport" content="width=device-width, initial-scale=1.0">
           <title>WebCamera</title>
       </head>
       <body>
       <input type="file" name="photo" id="photo"><br>
       <img style="display: none;width:200px;" id="img">
       <script>
           let photo = document.getElementById("photo");
           photo.addEventListener("change", preViewImg)
           function preViewImg(event) {
               let fileReader = new FileReader();
               let img = document.getElementById("img");
               fileReader.addEventListener(
                   "load",
                   () => {
                       // 将图像文件转换为 Base64 字符串
                       img.src = fileReader.result;
                       img.style.display = "block";
                   },
                   false
               );
               if (event.target.files && event.target.files[0]) {
                 fileReader.readAsDataURL(event.target.files[0]);
               } else {
                 console.error("File not exist.");
               }
           }
       </script>
       </body>
       </html>
       ```
* **场景二：调用系统相机和麦克风实现视频通话预览。**

  实现方案：调用W3C标准协议接口navigator.mediaDevices.getUserMedia()拉起麦克风和摄像头，实现前置摄像头视频通话预览，以下为实现步骤：

  1. 步骤一：在module.json5文件中配置相关权限：[ohos.permission.CAMERA](../harmonyos-guides/permissions-for-all-user.md#ohospermissioncamera)、[ohos.permission.MICROPHONE](../harmonyos-guides/permissions-for-all-user.md#ohospermissionmicrophone)，具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。
  2. 步骤二：Web组件向用户请求手动授权，示例代码如下：

     ```ts
     import { webview } from '@kit.ArkWeb';
     import { BusinessError } from '@kit.BasicServicesKit';
     import { abilityAccessCtrl } from '@kit.AbilityKit';

     @Entry
     @Component
     struct SceneTwo {
       controller: webview.WebviewController = new webview.WebviewController();
       uiContext: UIContext = this.getUIContext();

       aboutToAppear() {
         let atManager = abilityAccessCtrl.createAtManager();
         atManager.requestPermissionsFromUser(this.uiContext.getHostContext(),
           ['ohos.permission.CAMERA', 'ohos.permission.MICROPHONE'])
           .then((data) => {
             console.info(`data:${data}`);
             console.info(`data permissions:${data.permissions}`);
             console.info(`data authResults:${data.authResults}`);
           }).catch((error: BusinessError) => {
           console.error(`Failed to request permissions from user. Code is ${error.code}, message is ${error.message}`);
         });
       }

       build() {
         Column() {
           Web({ src: $rawfile('videoCall.html'), controller: this.controller })
             .fileAccess(false)
             .geolocationAccess(false)
             .onPermissionRequest((event) => {
               if (event) {
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

     加载的HTML文件：

     ```html
     <!-- videoCall.html -->
     <!DOCTYPE html>
     <html>
     <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="initial-scale=1.0">
     </head>
     <body>
     <div>
     <video id="video" width="500px" height="500px" autoplay="autoplay"></video>
     <br>
     <input type="button" title="HTML5摄像头" value="开启摄像头" onclick="getMedia()"/>
     </div>
     <script>
         function getMedia()
         {
           // 通过facingMode指定使用摄像头,前置为user，后置为environment
           let constraints = {
             video: {width: 500, height: 500, facingMode: "user"},
             audio: true
           };
           let video = document.getElementById("video");
           let promise = navigator.mediaDevices.getUserMedia(constraints);
           promise.then(function (MediaStream) {
             video.srcObject = MediaStream;
             video.play();
           });
         }
     </script>
     </body>
     </html>
     ```
* **场景三：拉起系统相册图库。**
  + **H5实现方案**：通过h5的input标签，不设置capture属性，点击input标签会弹出文件管理选项，用户可选择拉起图库实现拉起系统相册。

    ```ts
    import { webview } from '@kit.ArkWeb';

    @Entry
    @Component
    struct SolutionOne {
      controller: webview.WebviewController = new webview.WebviewController();

      build() {
        Column() {
          Web({
            src: $rawfile('album.html'),
            controller: this.controller
          })
            .fileAccess(false)
            .geolocationAccess(false);
        };
      }
    }
    ```

    ```html
    <!-- album.html -->
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
    <p>
        <input type="file" accept="image/*" capture="environment">
    </p>
    <p>
        <input type="file" accept="image/*">
    </p>
    </body>
    </html>
    ```
  + **ArkTS层实现方案**：使用onShowFileSelector拉起图库。

    ```ts
    import { webview } from '@kit.ArkWeb';
    import { photoAccessHelper } from '@kit.MediaLibraryKit';

    @Entry
    @Component
    struct WebComponent {
      controller: webview.WebviewController = new webview.WebviewController();

      async selectFile(result: FileSelectorResult): Promise<void> {
        let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
        let photoPicker = new photoAccessHelper.PhotoViewPicker();
        // 过滤选择媒体文件类型为IMAGE_VIDEO
        photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
        // 设置最大选择数量
        photoSelectOptions.maxSelectNumber = 5;
        let chooseFile: photoAccessHelper.PhotoSelectResult = await photoPicker.select(photoSelectOptions);
        // 获取选择的文件列表
        result.handleFileList(chooseFile.photoUris);
      }

      build() {
        Column() {
          Web({ src: $rawfile('local.html'), controller: this.controller })
            .onShowFileSelector((event) => {
              if (event) {
                this.selectFile(event.result);
              }
              return true;
            })
            .fileAccess(false)
            .geolocationAccess(false)
        }
      }
    }
    ```

    ```html
    <!-- local.html -->
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>

    <body>
    <!-- 点击上传文件按钮 -->
    <input type="file"><br>
    </body>
    </html>
    ```
* **场景四：调用系统麦克风录音。**

  实现方案：调用W3C标准协议接口navigator.mediaDevices.getUserMedia()拉起麦克风实现录音，以下为实现步骤：

  1. 步骤一：在module.json5文件中配置相关权限：[ohos.permission.MICROPHONE](../harmonyos-guides/permissions-for-all-user.md#ohospermissionmicrophone)，具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。
  2. 步骤二：Web组件向用户请求手动授权，示例代码如下：

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
           Web({ src: $rawfile('record.html'), controller: this.controller })
             .geolocationAccess(false)
             .fileAccess(false)
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
     <button id="recordButton" onclick="record()">录音</button>
     <button id="stopButton" disabled>停止</button>
     <audio id="player" controls preload="auto"></audio>
     </body>
     <script>
         const recordButton = document.getElementById('recordButton');
         const stopButton = document.getElementById('stopButton');
         const player = document.getElementById('player');
         function record() {
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
                     mediaRecorder.start();
                     stopButton.disabled = false;
                     recordButton.disabled = true;
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
         }
     </script>
     </html>
     ```
