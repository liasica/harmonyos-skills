---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-rtc
title: 在Web中打开摄像头和麦克风
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 使用网页多媒体 > 在Web中打开摄像头和麦克风
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a628a7d0fb4d140c5fce5c929f965b956c1f470cb4b0aa76ca604e4404c3aba1
---

WebRTC（Web Real-Time Communications）是一项实时通讯技术，它允许网络应用或站点在无需中间媒介的情况下建立浏览器之间的点对点（Peer-to-Peer）连接，实现视频流、音频流或其他任意数据的传输。WebRTC所包含的标准使得用户无需安装任何插件或第三方软件即可创建点对点（Peer-to-Peer）的数据共享与音视频会议。WebRTC技术适用于所有现代浏览器和主要平台的本机客户端，其背后的技术作为开放的Web标准实现，并在所有主要浏览器中作为常规JavaScript API提供。

## 申请权限

Web组件可以通过W3C标准协议接口访问摄像头和麦克风，通过[onPermissionRequest](../harmonyos-references/arkts-basic-components-web-events.md#onpermissionrequest9)接口接收权限请求通知，需在配置文件中声明相应的音视频权限并且进行系统侧授权与应用侧授权。

### 在module.json5配置权限

* 使用摄像头和麦克风功能前请在module.json5中添加音视频相关权限，权限的添加方法请参考[在配置文件中声明权限](declare-permissions.md#在配置文件中声明权限)。

  ```json5
    // src/main/resources/base/element/string.json
    "string":[
      {
        "name": "reason_for_camera",
        "value": "reason_for_camera"
      },
      {
        "name": "reason_for_microphone",
        "value": "reason_for_microphone"
      }
    ]
  ```

  ```json5
    // src/main/module.json5
    "requestPermissions":[
      {
        "name" : "ohos.permission.CAMERA",
        "reason": "$string:reason_for_camera",
        "usedScene": {
          "abilities": [
            "EntryAbility"
          ],
          "when":"inuse"
        }
      },
      {
        "name" : "ohos.permission.MICROPHONE",
        "reason": "$string:reason_for_microphone",
        "usedScene": {
          "abilities": [
            "EntryAbility"
          ],
          "when":"inuse"
        }
      }
    ]
  ```

通过在JavaScript中调用W3C标准协议接口navigator.mediaDevices.getUserMedia()，该接口用于打开摄像头和麦克风。constraints参数是一个包含了video和audio两个成员的MediaStreamConstraints对象，用于说明请求的媒体类型。

### 系统侧授权

参考[完整示例代码](web-rtc.md#完整示例代码)中，调用requestPermissionsFromUser，使得进入应用后会弹出是否允许该应用访问摄像头和麦克风的授权框，需点击"始终允许"或"每次使用时询问"按钮，授权应用访问摄像头和麦克风。

### 应用侧授权

参考[完整示例代码](web-rtc.md#完整示例代码)中，点击前端界面中的"开启摄像头"按钮后会通过onPermissionRequest触发权限请求，在弹出的对话框中单击"onConfirm"按钮后，打开摄像头和麦克风。

## 完整示例代码

```typescript
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl } from '@kit.AbilityKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  aboutToAppear() {
    // 配置Web开启调试模式
    webview.WebviewController.setWebDebuggingAccess(true);
    // 获取摄像头和麦克风权限，在组件创建时主动申请权限。
    let atManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionsFromUser(this.uiContext.getHostContext(), ['ohos.permission.CAMERA', 'ohos.permission.MICROPHONE'])
      .then((data) => {
        console.info('data:' + JSON.stringify(data));
        console.info('data permissions:' + data.permissions);
        console.info('data authResults:' + data.authResults);
      }).catch((error: BusinessError) => {
      console.error(`Failed to request permissions from user. Code is ${error.code}, message is ${error.message}`);
    })
  }

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
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
            })
          }
        })
    }
  }
}
```

* 前端界面index.html代码。

  ```html
  <!-- index.html -->
  <!DOCTYPE html>
  <html>
  <head>
    <meta charset="UTF-8">
  </head>
  <body>
  <video id="video" width="500px" height="500px" autoplay></video>
  <canvas id="canvas" width="500px" height="500px"></canvas>
  <br>
  <input type="button" title="HTML5摄像头" value="开启摄像头" onclick="getMedia()"/>
  <script>
    function getMedia()
    {
      let constraints = {
        video: {width: 500, height: 500},
        audio: true
      };
      // 获取video摄像头区域
      let video = document.getElementById("video");
      // 返回的Promise对象
      let promise = navigator.mediaDevices.getUserMedia(constraints);
      // then()异步，调用MediaStream对象作为参数
      promise.then(function(MediaStream) {
        video.srcObject = MediaStream;
        video.play();
      }).catch(function(err) {
          console.info(err.name + ": " + err.message);
      });
    }
  </script>
  </body>
  </html>
  ```

## WebRTC常见问题

WebRTC在实际应用中可能会遇到包括设备调用相关的问题，常见问题如下。

### 华为浏览器中HTML5页面选择长焦摄像头无法对焦

**问题现象**

网站打开相机，设备默认选择长焦摄像头，无法对焦。

**可能原因**

* 当前鸿蒙平台的相机列表顺序返回deviceId。
* 华为浏览器是系统应用，最后一个摄像头是长焦摄像头。

部分网站遍历设备后通过deviceId来强选最后一个摄像头，这两个因素叠加，在华为浏览器上就选择到长焦了。

**解决措施**

鸿蒙平台的相机列表顺序返回deviceId，因此有两个修改方案。

方案一：可以直接使用facingMode: 'environment'让浏览器自动选择后置摄像头，从而绕过直接指定deviceId的逻辑。

示例如下：

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>后置摄像头预览</title>
    <style>
        body { text-align: center; padding-top: 50px; }
        button { font-size: 18px; padding: 12px 24px; margin: 10px; }
        video { width: 80%; max-width: 500px; border: 1px solid #ccc; margin-top: 20px; background: #222; }
    </style>
</head>
<body>
<h2>后置摄像头预览facingMode</h2>
<video id="video" autoplay playsinline></video>
<br>
<button id="onBtn">打开后置摄像头</button>
<button id="offBtn" disabled>关闭摄像头</button>

<script>
    let currentStream = null;
    const video = document.getElementById('video');
    const onBtn = document.getElementById('onBtn');
    const offBtn = document.getElementById('offBtn');

    async function openCamera() {
        try {
            if (currentStream) {
                currentStream.getTracks().forEach(t => t.stop());
                currentStream = null;
            }
            // 使用facingMode:'environment'让浏览器自动选择后置摄像头
            const stream = await navigator.mediaDevices.getUserMedia({
                video: { facingMode: 'environment' },
                audio: false
            });
            video.srcObject = stream;
            currentStream = stream;
            onBtn.disabled = true;
            offBtn.disabled = false;
            console.info('后置摄像头已打开');
        } catch (err) {
            console.error('打开摄像头失败：', err);
            alert('无法打开后置摄像头，请检查权限或 HTTPS 环境。');
        }
    }

    function closeCamera() {
        if (currentStream) {
            currentStream.getTracks().forEach(t => t.stop());
            currentStream = null;
        }
        video.srcObject = null;
        onBtn.disabled = false;
        offBtn.disabled = true;
        console.info('摄像头已关闭');
    }

    onBtn.addEventListener('click', openCamera);
    offBtn.addEventListener('click', closeCamera);

    window.addEventListener('beforeunload', () => {
        if (currentStream) {
            currentStream.getTracks().forEach(t => t.stop());
        }
    });
</script>
</body>
</html>
```

方案二：遍历后置摄像头选择第一个后置摄像头。

* 遍历设备，获取第一个后置摄像头的deviceId。
* 通过deviceId来强选第一个后置摄像头。

示例如下：

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>打开后置摄像头</title>
    <style>
        body { text-align: center; padding-top: 50px; }
        button { font-size: 18px; padding: 12px 24px; margin: 10px; }
        video { width: 80%; max-width: 500px; border: 1px solid #ccc; margin-top: 20px; background: #222; }
    </style>
</head>
<body>
<h2>后置摄像头预览</h2>
<video id="video" autoplay playsinline></video>
<br>
<button id="onBtn">打开后置摄像头</button>
<button id="offBtn" disabled>关闭摄像头</button>

<script>
    let currentStream = null;
    const video = document.getElementById('video');
    const onBtn = document.getElementById('onBtn');
    const offBtn = document.getElementById('offBtn');

    // 遍历设备，获取第一个后置摄像头的 deviceId
    async function getFirstBackCameraId() {
        const devices = await navigator.mediaDevices.enumerateDevices();
        const videoDevices = devices.filter(d => d.kind === 'videoinput');
        const back = videoDevices.find(d => {
            const label = d.label.toLowerCase();
            return label.includes('back') || label.includes('rear') || label.includes('后置');
        });
        return back ? back.deviceId : (videoDevices[0] ? videoDevices[0].deviceId : null);
    }

    async function openCamera() {
        try {
            if (currentStream) {
                currentStream.getTracks().forEach(t => t.stop());
                currentStream = null;
            }
            // 通过deviceId来强选第一个后置摄像头
            const deviceId = await getFirstBackCameraId();
            if (!deviceId) {
                alert('未找到摄像头');
                return;
            }
            const stream = await navigator.mediaDevices.getUserMedia({
                video: { deviceId: { exact: deviceId } },
                audio: false
            });
            video.srcObject = stream;
            currentStream = stream;
            onBtn.disabled = true;
            offBtn.disabled = false;
            console.info('后置摄像头已打开');
        } catch (err) {
            console.error('打开摄像头失败：', err);
            alert('无法打开摄像头，请检查权限或 HTTPS 环境。');
        }
    }

    function closeCamera() {
        if (currentStream) {
            currentStream.getTracks().forEach(t => t.stop());
            currentStream = null;
        }
        video.srcObject = null;
        onBtn.disabled = false;
        offBtn.disabled = true;
        console.info('摄像头已关闭');
    }

    onBtn.addEventListener('click', openCamera);
    offBtn.addEventListener('click', closeCamera);

    window.addEventListener('beforeunload', () => {
        if (currentStream) {
            currentStream.getTracks().forEach(t => t.stop());
        }
    });
</script>
</body>
</html>
```
