---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-168
title: 根据Web页面是否成功加载动态展示不同页面
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 根据Web页面是否成功加载动态展示不同页面
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:93d6a7822454eb20baf2a706e5c0cbff7e3b44cd1b12ab02b4966fe6059beed3
---

## 问题现象

需要实现如下功能：

1. Web正常加载时，页面展示Web页面。
2. Web异常加载时，展示默认页面（页面包含重新加载按钮）。

## 背景知识

* [onErrorReceive](../harmonyos-references/arkts-basic-components-web-events.md#onerrorreceive)：网页加载遇到错误时触发该回调。主资源与子资源出错都会回调该接口，可以通过isMainFrame来判断是否是主资源报错。出于性能考虑，建议此回调中尽量执行简单逻辑。在无网络的情况下，触发此回调。
* [visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)：控制组件的显示或隐藏。当未设置visibility时，组件默认为显示。
  + Hidden：隐藏，但参与布局进行占位。
  + Visible：显示。
  + None：隐藏，但不参与布局，不进行占位。

## 解决方案

[ArkWeb的网络协议栈错误列表](../harmonyos-references/arkts-apis-neterrorlist.md)中当ErrorCode为0时表示正常加载，为其他值时表示异常加载。

可以定义一个successLoad变量，当加载失败后把ErrorCode值赋值给successLoad变量，重新刷新页面的时候设置successLoad的值为0（若不设置为0，则默认页面将持续显示），页面使用Stack布局，一层为默认页面，一层为Web页面，当successLoad为0时展示Web页面，successLoad为其他值展示默认页面。

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  @State successLoad: number = 0;
  webController: webview.WebviewController = new webview.WebviewController();

  build() {
    Stack() {
      Column() {
        Button('重新加载')
          .onClick(() => {
            this.successLoad = 0;
            this.webController.refresh();
          });
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
      .backgroundColor('#fff1f1f1')
      .visibility(this.successLoad !== 0 ? Visibility.Visible : Visibility.None);

      Web({ controller: this.webController, src: 'www.example.com' }) // Web页面
        .width('100%')
        .height('100%')
        .fileAccess(false)
        .geolocationAccess(false)
        .visibility(this.successLoad === 0 ? Visibility.Visible : Visibility.Hidden)
        .onErrorReceive((event) => {
          this.successLoad = event.error.getErrorCode();
        });
    }
    .width('100%')
    .height('100%');
  }
}
```

**说明** 

访问在线网页时需添加网络权限：[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)，具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。
