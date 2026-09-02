---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-144
title: 如何解决Web组件加载H5页面时拉起系统拨号等功能出现白屏
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何解决Web组件加载H5页面时拉起系统拨号等功能出现白屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d4076851cbdff71cca0f94383aacd8d702f773ae59351eaee4c65c2c6a6b7633
---

## 问题现象

Web加载H5页面，点击H5中“tel:”、“sms:”、“mailto:”开头的特殊链接，没有跳转到对应的拨号、短信、邮件应用，而是出现Web组件白屏现象。代码如下：

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  webviewController: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('call.html'), controller: this.webviewController })
    }
  }
}
```

```html
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no"/>
</head>
<body>
<div>
    <a href="tel:xxx">拨打电话</a>
    <a href="sms:xxx">发送信息</a>
    <a href="mailto:xxx@example">发送邮件</a>
</div>
</body>
</html>
```

## 背景知识

* [跨应用跳转](../harmonyos-guides/web-redirection-and-browsing-history-mgmt.md#跨应用跳转)：Web组件可以实现点击前端页面超链接跳转到其他应用。
* [onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)：当Web组件加载URL之前触发该回调，用于判断是否阻止此次访问。
* [makeCall](../harmonyos-references/js-apis-call.md#callmakecall7)：跳转到拨号界面，并显示待拨出的号码。
* [startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)：启动一个UIAbility。使用callback异步回调。仅支持在主线程调用。
* [拉起邮件类应用（mailto方式）](../harmonyos-guides/start-email-apps-by-mailto.md)：通过mailto电子邮件协议，可以创建指向电子邮件地址的超链接，方便用户通过网页或应用中的超链接直接跳转电子邮件应用。同时，支持在mailto:的相关字段中定义邮件的收件人、主题、正文内容等，节省用户编辑邮件的时间。
* [sms方式跳转到短信编辑界面](../harmonyos-guides/telephony-sms.md#sms方式跳转到短信编辑界面)：通过sms短信协议，可以创建指向短信收件人的超链接，方便用户通过网页或应用中的超链接直接跳转到短信应用。同时，支持在sms:的相关字段中定义短信的收件人、发送内容等，节省用户编辑短信的时间。

## 问题定位

Web组件不支持通过“tel:”、“sms:”、“mailto:”链接直接拉起对应应用（拨号、短信、邮件）。

## 分析结论

Web组件不支持通过“tel:”、“sms:”、“mailto:”链接直接拉起对应应用（拨号、短信、邮件），需要通过[onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)回调拦截这些链接，调用ArkTS API拉起对应应用。

## 修改建议

通过Web组件的[onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)回调拦截“tel:”、“sms:”、“mailto:”链接跳转，调用ArkTS API拉起对应应用。示例代码如下：

```ts
import { call } from '@kit.TelephonyKit';
import { common, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';

const SUB_COUNT: number = 4;

@Entry
@Component
struct Index {
  webviewController: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('call.html'), controller: this.webviewController })
        .fileAccess(false)
        .geolocationAccess(false)
        .onLoadIntercept((event) => {
          if (event) {
            let url: string = event.data.getRequestUrl();
            // 判断链接是否为拨号链接
            if (url.indexOf('tel:') === 0) {
              // 跳转拨号界面
              call.makeCall(url.substring(SUB_COUNT), (err) => {
                if (!err) {
                  console.info('make call succeeded.');
                } else {
                  console.error(`make call fail, err is: ${err}`);
                }
              });
              return true;
            }
            // 判断链接是否为发短信链接
            if (url.indexOf('sms:') === 0) {
              // 跳转到短信编辑界面
              let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
              let want: Want = {
                bundleName: 'com.ohos.mms',
                action: 'ohos.want.action.viewData',
                uri: url,
              };
              context.startAbility(want).then((data) => {
                console.info(`Success, ${data}`);
              }).catch(() => {
                console.error('error');
              });
              return true;
            }
            // 判断链接是否为发邮件链接
            if (url.indexOf('mailto:') === 0) {
              // 跳转到邮件应用
              let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
              let want: Want = {
                action: 'ohos.want.action.sendToData',
                uri: url
              };
              context.startAbility(want).then((data) => {
                console.info(`Success, ${data}`);
              }).catch(() => {
                console.error('error');
              });
              return true;
            }
          }
          return false;
        });
    };
  }
}
```

```html
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no"/>
</head>
<body>
<div>
    <a href="tel:xxx">拨打电话</a>
    <a href="sms:xxx">发送信息</a>
    <a href="mailto:xxx@example">发送邮件</a>
</div>
</body>
</html>
```
