---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-177
title: Web组件同层渲染时如何传自定义参数
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件同层渲染时如何传自定义参数
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:07+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:88fca94f4d5191da663f1f47fd8d2f4fb3e7b55dfb30f2c368bcf70d057f804c
---

## 问题现象

在Web组件同层渲染场景下，H5中的object标签如何传自定义参数并通过onNativeEmbedLifecycleChange回调接收参数？

## 背景知识

* [同层渲染](../harmonyos-guides/web-same-layer.md)：在系统中，应用可以使用Web组件加载Web网页。当非系统框架的UI组件功能或性能不如系统组件时，可使用同层渲染技术，通过ArkUI组件渲染这些组件（简称为同层组件）。
  + 支持embed标签：在开启同层渲染后，仅支持type类型为native前缀的标签识别为同层组件，不支持自定义属性。
  + 支持object标签：在开启同层渲染后，支持将非标准MIME type的object标签识别为同层组件，支持通过param/value的自定义属性解析。
* [onNativeEmbedLifecycleChange](../harmonyos-references/arkts-basic-components-web-events.md#onnativeembedlifecyclechange11)：当同层标签生命周期变化时触发该回调。
* [enableNativeEmbedMode](../harmonyos-references/arkts-basic-components-web-attributes.md#enablenativeembedmode11)：设置是否开启同层渲染功能。当属性没有显式调用时，默认不开启同层渲染功能。
* [registerNativeEmbedRule](../harmonyos-references/arkts-basic-components-web-attributes.md#registernativeembedrule12)：注册使用同层渲染的HTML标签名和类型。标签名仅支持使用object和embed。标签类型只能使用ASCII可显示字符。

## 解决方案

object标签支持param/value的自定义属性传值，使用时需要将enableNativeEmbedMode属性设置为true，调用registerNativeEmbedRule注册同层渲染的HTML标签名和类型，最后通过onNativeEmbedLifecycleChange回调中获取到自定义属性值。

应用侧示例代码如下：

```screen
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebRender {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('render.html'), controller: this.controller })
        .domStorageAccess(true)
        .fileAccess(true)
        .geolocationAccess(false)
        .enableNativeEmbedMode(true)
        .registerNativeEmbedRule('object', 'test/input')
        .onNativeEmbedLifecycleChange((event) => {
          if (event.info) {
            console.info('NativeEmbedParams: ' + event.info.params?.['testName']);
          }
        });
    };
  }
}
```

HTML示例代码如下：

```screen
<!--src/main/resources/rawfile/render.html-->
<!DOCTYPE html>
<html>
<head>
    <title>同层渲染html</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="background:white">
<object id = "input1" type="test/input" style="width: 300px; height: 100px">
    <param name="testName" value="testValue">
</object>
</body>
</html>
```

打印结果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/lE0SjmieQmW3k_QRhp1zjw/zh-cn_image_0000002659138435.png "点击放大")
