---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-124
title: 进入Web页面后，点击返回出现空白页面，再次返回正常
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 进入Web页面后，点击返回出现空白页面，再次返回正常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5a2c752e44bfc23944246e16d8347469029f4212ef319bb44304314a84526ca0
---

## 问题现象

在首页点击内容后，页面跳转到Web页面，当用户点击返回按钮想回到首页时，会出现空白页面，无法正常显示内容，但再次点击返回按钮后，页面返回到首页。

## 背景知识

* [onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)：当Web组件加载url之前触发该回调，用于判断是否阻止此次访问。
* [onInterceptRequest](../harmonyos-references/arkts-basic-components-web-events.md#oninterceptrequest9)：当Web组件加载url之前触发该回调，用于拦截url并返回响应数据。onInterceptRequest可拦截所有跳转请求并返回响应数据，但无法访问POST请求体（Body）内容，且不支持分片缓冲（buffer）类型数据获取。此类场景需改用WebSchemeHandler实现，依据具体业务需求进行判断。
* [accessStep](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#accessstep)：判断当前页面是否可前进或者后退给定的step步。

## 问题定位

页面在加载Web内容时，进度条到一半后出现重新加载的现象。是页面加载被拦截后再次跳转新的页面，导致加载页面时，初始出现短暂空白，随后页面正常加载。返回上一页时，因页面加载过程被中断或拦截，进入一个处于半加载状态的界面，呈现为空白页。在日志中，OnBeforeBrowse字段为拦截关键字：

```txt
[web_contents_impl.cc:10430] [Adblock] set adblock switch for site, frame tree node id:14 adblock switch from UI: 1
[render_frame_host_impl.cc:15523] [AdBlock] Update adblock site switch:1
[nweb_handler_delegate.cc:1524] NWebHandlerDelegate::OnBeforeBrowse
```

## 分析结论

当点击页面中自定义类型的url链接时，onLoadIntercept回调中执行了跳转到其他HarmonyOS页面，但未终止onLoadIntercept回调中代码的执行，导致执行到了最后一行返回false，表示允许此次访问。

于是Web内跳转到了链接指向的url是不存在的页面，看到Web组件显示空白的现象。

```ts
build() {
  Column() {
    Web({
      controller: this.webController,
      src: this.webUrl
    })
      .onInterceptRequest((event) => {
        if (!event) {
          return;
        }
        return null;
      })
      .onLoadIntercept((event) => {
        let url = event.data.getRequestUrl();
        if (url.includes(`xx.com`)) {
          // 加载最终的url
          this.controller.loadUrl('');
        }
        return false;
      });
  }
  .height('100%');
}
```

## 修改建议

当H5跳转链接为无需访问的链接时，可在Web组件的onLoadIntercept回调中自定义处理逻辑。处理完成后，应立即返回true，以阻止当前url的加载，从而有效拦截跳转。代码示例：

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct NavToWeb {
  @Provide('NavPathStack') pageStack: NavPathStack = new NavPathStack();

  @Builder
  PagesMap(name: string) {
    if (name === 'Page1') {
      JumpInterceptCase();
    }
  }

  build() {
    Navigation(this.pageStack) {
      Text('首页')
        .fontSize(30)
        .offset({ y: '50%' })
        .onClick(() => {
          this.pageStack.pushPathByName('Page1', '');
        });
    }
    .mode(NavigationMode.Stack)
    .navDestination(this.PagesMap);
  }
}

@Component
export struct JumpInterceptCase {
  @Consume('NavPathStack') pageStack: NavPathStack;
  controller: webview.WebviewController = new webview.WebviewController();

  @Builder
  myBuilder() {
    Column() {
      Button('content1')
        .margin(10)
        .fontSize(20);

      Button('content2')
        .margin(10)
        .fontSize(20);
    }
    .width('100%');
  }

  build() {
    NavDestination() {
      Column() {
        Row() {
          Blank().width(10)
          Text('返回')
            .onClick(() => {
              this.pageStack.pop();
            })
            .fontSize(18)
            .width('100%')
            .alignSelf(ItemAlign.Start)
        }
        Web({ src: '', controller: this.controller })
          .width('100%')
          .height('100%')
          .fileAccess(false)
          .javaScriptAccess(true)
          .domStorageAccess(true)
          .geolocationAccess(false)
          .horizontalScrollBarAccess(false)
          .verticalScrollBarAccess(false)
          .copyOptions(CopyOptions.LocalDevice)
          .onControllerAttached(() => {
            this.controller.loadUrl($rawfile('audio.html')); // 替换成开发者自己的HTML
          })
          .onInterceptRequest((event) => {
            if (!event) {
              return;
            }
            return null;
          })
          .onLoadIntercept((event) => {
            let url = event.data.getRequestUrl();
            if (url.includes(`resource://rawfile/audio.html`)) { // 替换成开发者自己的HTML
              // 加载最终的url
              this.controller.loadUrl($rawfile('webBlock.html')); // 替换成开发者自己的HTML
              return true;
            }
            return false;
          });
      }
      .width('100%')
      .height('100%');
    }
    .hideTitleBar(true)
    .mode(NavDestinationMode.STANDARD);
  }
}
```

audio.html示例代码如下：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>播放音频</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        textarea {
            width: 100%;
            height: 100px;
        }
        button {
            margin-top: 10px;
        }
        audio {
            margin-top: 10px;
        }
    </style>
</head>
<body onload='playAudio()'>
<audio id="audioPlayer" muted="" controls></audio>
<script>
    function playAudio(hexInput) {
        // 将16进制字符串转换为二进制字节数组
        const binaryData = Uint8Array.from(hexInput.match(/.{1,2}/g), byte => parseInt(byte, 16));
        // 创建一个Blob对象
        const blob = new Blob([binaryData], { type: 'audio/mpeg' });
        // 创建一个url对应于该Blob
        const url = URL.createObjectURL(blob);
        // 设置音频元素的src属性
        const audioPlayer = document.getElementById('audioPlayer');
        audioPlayer.src = url;
        // 播放音频
        audioPlayer.play().catch(error => {
        });
    }
</script>
</body>
</html>
```

webBlock.html示例代码如下：

```html
<!DOCTYPE html>
<html lang="zh">
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>简单示例</title>
</head>
<body>
<h1>欢迎</h1>
<p>这是一个简单的 HTML 页面。</p>
</body>
</html>
```
