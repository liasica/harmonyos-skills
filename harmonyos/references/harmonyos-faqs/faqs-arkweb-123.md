---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-123
title: Web组件如何正确设置User-Agent
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件如何正确设置User-Agent
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b80d3cf93cabf4e4e98bec0cdb826b8c7951945580b3c75d5cea8f5a433e9a74
---

## 问题现象

通过Web组件加载H5页面，设置自定义User-Agent后出现以下问题：

1. 通过以下代码设置User-Agent后，点击页面功能无反应。

   ```ts
   import { webview } from '@kit.ArkWeb';

   @Entry
   @Component
   struct WebComponent {
     controller: webview.WebviewController = new webview.WebviewController();
     customUserAgent: string = ' DemoApp';

     build() {
       Column() {
         Web({ src: 'www.example.com', controller: this.controller })
           .fileAccess(false)
           .geolocationAccess(false)
           .onLoadIntercept(() => {
             let userAgent = this.controller.getUserAgent() + this.customUserAgent;
             this.controller.setCustomUserAgent(userAgent);
             return false;
           })
       };
     }
   }
   ```
2. 通过defaultFontSize无法设置网页的默认字体大小，去掉自定义User-Agent正常。设置User-Agent的代码如下：

   ```ts
   this.controller.setCustomUserAgent('xxx_xxx_xxx_harmony')
   ```

## 背景知识

* [User-Agent开发指导](../harmonyos-guides/web-default-useragent.md)：User-Agent（简称UA）是一个特殊的字符串，包含设备类型、操作系统及版本等关键信息。如果页面无法正确识别UA，可能会导致多种异常情况。
* [setCustomUserAgent](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setcustomuseragent10)接口设置的是对ArkWeb对象整个生命周期起作用的，若需要根据加载的网页临时调整UA，针对此种情况，API20新增了如下两个全局设置接口。
  1. 针对域名配置UA：[setUserAgentForHosts](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setuseragentforhosts20)。
  2. 设置App默认UA：[setAppCustomUserAgent](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setappcustomuseragent20)。

## 问题定位

1. 检查自定义UA的设置时机。推荐当WebController成功绑定到Web组件后在[onControllerAttached](../harmonyos-references/arkts-basic-components-web-events.md#oncontrollerattached10)事件中设置，否则可能会出现加载的页面与实际设置User-Agent不匹配的异常现象。
2. 检查自定义UA设置的格式是否正确。HarmonyOS[默认User-Agent结构](../harmonyos-guides/web-default-useragent.md#默认user-agent结构)如下：

   ```ts
   Mozilla/5.0 ({DeviceType}; {OSName} {OSVersion}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ChromeCompatibleVersion}.0.0.0 Safari/537.36  ArkWeb/{ArkWeb VersionCode} {DeviceCompat} {扩展区}
   ```

## 分析结论

1. 自定义UA设置的时机不对，导致页面功能异常。
2. 自定义UA设置的格式不正确。

## 修改建议

1. 当WebController成功绑定到Web组件后，在onControllerAttached事件中通过[setCustomUserAgent](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setcustomuseragent10)接口设置自定义UA。

   ```ts
   import { webview } from '@kit.ArkWeb';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct WebComponent {
     controller: webview.WebviewController = new webview.WebviewController();
     customUserAgent: string = ' DemoApp';

     build() {
       Column() {
         Web({ src: 'www.example.com', controller: this.controller })
           .fileAccess(false)
           .geolocationAccess(false)
           .onControllerAttached(() => {
             console.info('onControllerAttached');
             try {
               let userAgent = this.controller.getUserAgent() + this.customUserAgent;
               this.controller.setCustomUserAgent(userAgent);
             } catch (error) {
               console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
             }
           });
       };
     }
   }
   ```
2. 按照规范格式设置UA。例如：

   ```ts
   Mozilla/5.0 (Phone; OpenHarmony 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36  ArkWeb/6.0.0.120 Mobile
   ```

* 加载在线网页时需要在module.json5中配置ohos.permission.INTERNET网络访问权限。具体配置方式请参考：[声明权限](../harmonyos-guides/declare-permissions.md)。

## 总结

如果页面出现加载白屏、内容布局异常、点击链接无反应，都可排查是否需要设置User-Agent或User-Agent设置是否正确。
