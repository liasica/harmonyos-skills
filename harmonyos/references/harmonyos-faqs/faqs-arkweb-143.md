---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-143
title: Web组件如何实现拦截网络超链接后在浏览器中打开
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件如何实现拦截网络超链接后在浏览器中打开
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3b6ab6952cca9d6822cf0930a1e84bf1c091e17bc90d61fa99f5f342d0d27e9a
---

## 问题现象

Web中加载包含网络图片链接的HTML网页，如何实现点击网络图片链接后跳转至手机浏览器打开？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/mQ059uSASoil1iK-WKZjUw/zh-cn_image_0000002659258357.png "点击放大")

## 背景知识

* [WebviewController](../harmonyos-references/arkts-apis-webview-webviewcontroller.md)：WebviewController可以控制Web组件各种行为。一个WebviewController对象只能控制一个Web组件，且必须在Web组件和WebviewController绑定后，才能调用WebviewController上的方法（静态方法除外）。
* [onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)：当Web组件加载URL之前触发该回调，用于判断是否阻止此次访问。默认允许加载。
* [startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)：启动一个UIAbility。使用callback异步回调。仅支持在主线程调用。

## 解决方案

* 访问在线网页时需添加网络权限：[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)，具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。
* 创建Web组件来加载网页内容，通过onLoadIntercept回调拦截需要跳转的网址，然后使用系统能力打开外部浏览器并加载拦截的网址。

```ts
import { webview } from '@kit.ArkWeb';
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebJumpBrowser {
  controller: webview.WebviewController = new webview.WebviewController();
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    Column() {
      Web({
        // 此处地址实际使用过程中替换为真实地址
        src: 'www.example.com',
        controller: this.controller
      })
        .fileAccess(false)
        .geolocationAccess(false)
        .domStorageAccess(true)
        .onLoadIntercept((event) => {
          // 拦截所有请求
          let url = event.data.getRequestUrl();
          console.info('Intercepting URL: ' + url);
          // 判断是否需要外部打开（这里示例所有https链接都外部打开）
          if (url.startsWith('https://')) {
            // 调用方法在外部浏览器打开
            this.openInExternalBrowser(url);
            return true;
          }
          return false;
        });
    }
    .width('100%')
    .height('100%');
  }

  // 在外部浏览器打开链接的方法
  openInExternalBrowser(url: string) {
    try {
      let want: Want = {
        action: 'ohos.want.action.viewData',
        entities: ['entity.system.browsable'],
        uri: url,
      };
      this.context.startAbility(want)
        .then(() => {
          console.info('Open browser successfully');
        })
        .catch((err: BusinessError) => {
          let code = (err as BusinessError).code;
          let message = (err as BusinessError).message;
          console.error(`startAbility failed, code is ${code}, message is ${message}`);
        });
    } catch (error) {
      console.error(`An unexpected error occurred. Error code: ${error.code}, message is ${error.message}`);
    }
  }
}
```
