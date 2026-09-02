---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-drag
title: 使用Web组件的拖拽功能与网页交互
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 管理网页交互 > 使用Web组件的拖拽功能与网页交互
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b122af384f2f975b4a9b7a2de991418cdbfbd3462c0a363a3e2aa22a9b99d452
---

ArkWeb的拖拽功能使应用能够在网页中实现元素的拖放，用户可以长按可拖拽的元素，将其拖至可放置的元素上，然后松手完成放置。ArkWeb在网页内容中的拖拽功能满足H5标准。

## 将网页内容拖拽至其他应用

ArkWeb目前支持以下四种数据格式。应用按照H5标准设置这些格式的拖拽数据，即可将内容拖拽到其他应用中。

| 数据格式 | 说明 |
| --- | --- |
| text/plain | 文本 |
| text/uri-list | 链接 |
| text/html | HTML格式 |
| Files | 文件 |

## 拖拽事件通知

ArkWeb拖拽不同于ArkUI的组件级拖拽，主要针对网页内容的拖拽，因此仅支持部分拖拽事件的监听方法。

| 监听方法 | 说明 |
| --- | --- |
| [onDragStart](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart) | 不建议使用此方法，否则会影响Web组件的拖拽行为，造成拖拽逻辑不符合预期，如无法触发H5拖拽事件监听，预览图无法创建或预览图错误，拖拽数据无法预置等。 |
| [onDragEnter](../harmonyos-references/ts-universal-events-drag-drop.md#ondragenter) | 拖拽的元素进入Web区域。 |
| [onDragMove](../harmonyos-references/ts-universal-events-drag-drop.md#ondragmove) | 拖拽的元素在Web区域移动。 |
| [onDragLeave](../harmonyos-references/ts-universal-events-drag-drop.md#ondragleave) | 拖拽的元素离开Web区域。 |
| [onDrop](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop15) | 拖拽的元素落入Web区域。 |
| [onDragEnd](../harmonyos-references/ts-universal-events-drag-drop.md#ondragend10) | 由Web发起的拖拽元素结束拖拽。 |

## 在ArkTS侧实现拖拽相关逻辑

在多数情况下，应用在H5端实现的拖拽功能能够满足需求。如有需要，请参考以下案例，实现在ArkTS端进行拖拽数据读取等操作。

1. [建立应用侧与前端页面数据通道](web-app-page-data-channel.md)。
2. 在onDrop方法中，做简单逻辑，例如暂存一些关键数据。
3. 在ArkTS侧接收消息的方法中，添加应用处理逻辑，可以进行耗时任务。

由于ArkTS侧的onDrop方法会早于H5中放置事件的处理方法（H5示例中的droppable.addEventListener('drop')）执行，若在onDrop方法中进行页面跳转等操作，将导致H5中的drop方法无法正确执行，产生不符合预期的结果。因此，应建立双向通信机制，在H5中的drop方法执行完毕后，通知ArkTS侧执行相应的业务逻辑，以确保业务逻辑的预期执行。

```typescript
import { webview } from '@kit.ArkWeb'
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';

@Entry
@Component
struct DragDrop {
  private controller: webview.WebviewController = new webview.WebviewController()
  @State ports: Array<webview.WebMessagePort> = []
  @State dragData: Array<unifiedDataChannel.UnifiedRecord> = []

  build() {
    Column() {
      Web({
        src: $rawfile('drag.html'),
        controller: this.controller,
      }).onPageEnd((event) => {
        // 注册通信端口
        this.ports = this.controller.createWebMessagePorts();
        this.ports[1].onMessageEvent((result: webview.WebMessage) => {
          // ArkTS收到html传来的数据后的处理，可以先打日志确认下消息，双端的消息格式可以自己约定，能唯一识别就行
          console.info('ETS receive Message: typeof (result) = ' + typeof (result) + ';' + result);
          // 这里添加result中消息接收到后的处理,可进行耗时任务
        });
        console.info('ETS postMessage set h5port ');
        // 完成通信端口注册后，向前端发送注册完成消息，完成双向的端口绑定
        this.controller.postMessage('__init_port__', [this.ports[0]], '*');
      })// onDrop 可做简单逻辑，例如暂存一些关键数据
        .onDrop((dragEvent: DragEvent) => {
          console.info('ETS onDrop!')
          let data: UnifiedData = dragEvent.getData();
          if(!data) {
            return false;
          }
          let uriArr: unifiedDataChannel.UnifiedRecord[] = data.getRecords();
          if (!uriArr || uriArr.length <= 0) {
            return false;
          }
          // 可以遍历records取数据暂存，或者以其他方式暂存数据
          for (let i = 0; i < uriArr.length; ++i) {
            if (uriArr[i].getType() === uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) {
              let plainText = uriArr[i] as unifiedDataChannel.PlainText;
              if (plainText.textContent) {
                console.info('plainText.textContent: ', plainText.textContent);
              }
            }
          }
          return true
        })
    }

  }
}
```

H5示例:

```html
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>H5 拖拽 Demo</title>
</head>
<style>
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
    }

    .draggable {
      width: 100px;
      height: 100px;
      background-color: #4CAF50;
      color: white;
      text-align: center;
      line-height: 100px;
      margin-bottom: 20px;
      cursor: grab;
    }

    .droppable {
      width: 300px;
      height: 150px;
      border: 2px dashed #999;
      background-color: #f0f0f0;
      text-align: center;
      line-height: 150px;
      font-size: 16px;
    }

    .success {
      background-color: #4CAF50;
      color: white;
    }
</style>
<body>

<h2>H5 拖拽 Demo</h2>

<div id="draggable" class="draggable" draggable="true">可拖拽元素</div>

<div id="droppable" class="droppable">请将方块拖到这里</div>

<script>
    const draggable = document.getElementById('draggable');
    const droppable = document.getElementById('droppable');

    // 拖拽开始事件
    draggable.addEventListener('dragstart', function (e) {
      e.dataTransfer.setData('text/plain', this.id);
      this.style.opacity = '0.4';
    });

    // 拖拽结束事件
    draggable.addEventListener('dragend', function (e) {
      this.style.opacity = '1';
    });

    // 拖入目标区域时触发
    droppable.addEventListener('dragover', function (e) {
      e.preventDefault(); // 必须调用，否则无法触发 drop 事件
    });

    // 放置事件
    droppable.addEventListener('drop', function (e) {
      e.preventDefault();
      const data = e.dataTransfer.getData('text/plain');
      // 传入ArkTS
      PostMsgToArkTS(data);
      const draggableEl = document.getElementById(data);
      this.appendChild(draggableEl);
      this.classList.add('success');
      this.textContent = "放置成功！";
    });

    // scriptproxy端口在js侧设置
    var h5Port;
    window.addEventListener('message', function (event) {
    console.info("H5 receive settingPort message");
        if (event.data == '__init_port__') {
            if (event.ports[0] != null) {
                console.info("H5 set h5Port " + event.ports[0]);
                h5Port = event.ports[0];
            }
        }
    });

    // 通过scriptproxy方式,发送数据到ArkTS侧的实现
    function PostMsgToArkTS(data) {
        console.info("H5 PostMsgToArkTS, h5Port " + h5Port);
        if (h5Port) {
          h5Port.postMessage(data);
        } else {
          console.error("h5Port is null, Please initialize first");
        }
    }
</script>

</body>
</html>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/gTDCpzdVSS61PWzK7u2Ykw/zh-cn_image_0000002706834064.gif)

日志打印：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/FjIaZvR_TPObpfhLWI6j0A/zh-cn_image_0000002736313173.png)

## 常见问题

### 为什么H5设置的拖拽事件没有触发？

请检查相关CSS资源是否正常设置，因为有些网页UA做了判断，针对特定设备的UA才会进行CSS样式设置。可以考虑在Web组件设置自定义UA解决这种问题，例如：

```typescript
import { webview } from '@kit.ArkWeb'

@Entry
@Component
struct Index {
  private webController: webview.WebviewController = new webview.WebviewController()
  build(){
    Column() {
      Web({
        src: 'example.com',
        controller: this.webController,
      }).onControllerAttached(() => {
        // 特定UA
        let customUA = 'android'
        this.webController.setCustomUserAgent(this.webController.getUserAgent() + customUA)
      })
    }
  }
}
```

### 如何禁用Web组件拖拽能力

在未进行特殊配置的情况下，Web组件默认支持拖拽功能。如果不需要拖拽功能，可以参考以下示例禁用拖拽。

禁用拖拽方式主要分为两类：

1. 网页侧通过W3C CSS、JS进行拦截/禁用。
2. 应用侧通过Web组件runJavaScriptExt接口注入JS进行拦截/禁用。

H5示例1:

```html
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>w3c通用属性/方法禁用拖拽</title>
</head>
<style>
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
    }
    .normal {
      width: 100px;
      height: 100px;
      margin-bottom: 40px;
    }
    .undraggable {
      width: 100px;
      height: 100px;
      margin-bottom: 40px;
      -webkit-user-drag: none;
    }

</style>
<body>

<h2>w3c通用属性/方法禁用拖拽</h2>

<!--一，通过显式设置draggable样式为false来禁用该元素的拖拽-->
<!--仅对img或div这种整个元素节点的拖拽行为生效，对节点中选中的文字不生效-->
<div>draggable设置禁用拖拽</div>
<img class="normal" draggable="false" src="./any-pic.png"><br>

<!--二，通过引用一个样式class，class中设置-webkit-user-drag为none来禁用拖拽-->
<!--生效范围同方式一-->
<div>-webkit-user-drag设置禁用拖拽</div>
<img class="undraggable" src="./any-pic.png"><br>

<!--三，通过对设置ondragstart事件监听并preventDefault来禁用拖拽-->
<!--对任意内容的拖拽行为都生效-->
<!--可通过扩大监听器监听的范围来禁用更大区域内的拖拽，比如监听在window上可实现整个Web组件的拖拽禁用-->
<!--由于生效节点较靠后，拖拽事实上已进行部分，会对菜单功能产生影响-->
<div>ondragstart设置禁用拖拽</div>
<div ondragstart="dragstartHandler(event)">
    <img class="normal" src="./any-pic.png">
    <p>
        此段文本用于验证ondragstart脚本对选中文本的禁用拖拽效果
    </p>
</div>

<script>
    function dragstartHandler(event) {
        console.info('forbid drag when drag start');
        event.preventDefault();
    }
</script>

</body>
</html>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/pimeBwnKT4qmo5HtaGb2tw/zh-cn_image_0000002706674130.gif)

html示例2:

```html
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>runJavascriptExt注入js禁用拖拽</title>
</head>
<style>
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
    }
    .normal {
      width: 100px;
      height: 100px;
      margin-bottom: 40px;
    }
</style>
<body>

<h2>runJavascriptExt注入js禁用拖拽</h2>

<div>
    <img class="normal" src="./any-pic.png">
    <p>
        此段文本用于验证runJavascriptExt注入js对选中文本的禁止拖拽效果
    </p>
</div>

</body>
</html>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/PQhR6WOnRGq5BhbJ08JRyw/zh-cn_image_0000002736433221.gif)

ArkTS示例:

```typescript
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  webViewController: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('w3cDemoPage')
        .onClick(() => {
          this.webViewController.loadUrl($rawfile('w3c-forbid.html'));
        })
      Button('runJsDemoPage')
        .onClick(() => {
          this.webViewController.loadUrl($rawfile('runJs-forbid.html'));
        })
      Button('runJsForbidDrag')
        .onClick(() => {
          try {
            // 使用runJavaScriptExt执行脚本添加dragstart事件监听器去禁用拖拽
            this.webViewController.runJavaScriptExt(
              'window.addEventListener(\'dragstart\', (ev) => {\n' +
                'ev.preventDefault();\n' +
                '});',
              (error, result) => {
                if (error) {
                  console.error(`run JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`)
                  return;
                }
              });
          } catch (resError) {
            console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
          }
        })
      Web({
        src: $rawfile('w3c-forbid.html'),
        controller: this.webViewController
      })
        .domStorageAccess(true)
        .javaScriptAccess(true)
        .fileAccess(true)
    }
    .height('100%')
    .width('100%')
  }
}
```
