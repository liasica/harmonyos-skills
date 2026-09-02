---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-151
title: Web组件如何监听页面加载进度
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件如何监听页面加载进度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0b10a61bfef450e7aa921d0665987a3e5b1214f438c9ab94a1ae6cb889f5aa8a
---

## 问题现象

加载Web页面时，如何实时监听Web页面的加载进度并通过进度条展示出来？

## 背景知识

* [onProgressChange](../harmonyos-references/arkts-basic-components-web-events.md#onprogresschange)：网页加载进度变化时触发该回调。
* [Progress](../harmonyos-references/ts-basic-components-progress.md)：进度条组件，用于显示内容加载或操作处理等进度。

## 解决方案

* 实现思路如下：
  1. 加载在线网页时需要在module.json5中配置ohos.permission.INTERNET网络访问权限。具体配置方式请参考：[声明权限](../harmonyos-guides/declare-permissions.md)。
  2. 在Web控件里添加onProgressChange属性监听当前网页加载进度。
  3. 使用Progress组件展示当前加载进度。
* 完整示例参考如下：

  ```screen
  import { webview } from '@kit.ArkWeb';

  @Entry
  @Component
  struct Index {
    controller: webview.WebviewController = new webview.WebviewController();
    @State currentProgress: number = 0;
    private total: number = 100;
    @State webLoadingEnd: boolean = false;

    build() {
      Column() {
        Progress({ value: this.currentProgress, total: this.total })
          .visibility(this.webLoadingEnd ? Visibility.None : Visibility.Visible)
          .width('100%');

        Web({ src: 'www.example.com', controller: this.controller })
          .geolocationAccess(false)
          .fileAccess(false)
          .onProgressChange((event) => {
            if (event) {
              console.info(`newProgress: ${event.newProgress}`);
            }
            this.currentProgress = event.newProgress;
            if (event.newProgress === this.total) {
              this.webLoadingEnd = true;
              this.currentProgress = 0;
            } else {
              this.webLoadingEnd = false;
            }
          });
      };
    }
  }
  ```
