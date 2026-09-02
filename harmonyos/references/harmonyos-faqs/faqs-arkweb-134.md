---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-134
title: 如何解决Web组件首次加载完网页立即滑动发生明显卡顿问题
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何解决Web组件首次加载完网页立即滑动发生明显卡顿问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f9af4de2cc2ca952c2574fe5e4c63f941218bd0f207d34d8f04e7c6151f4d50b
---

## 问题现象

Web组件首次加载完网页时，此时立即去滑动网页会发生明显的卡顿。

问题代码示例参考如下：

```screen
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private webviewController: webview.WebviewController = new webview.WebviewController();
  // 此处地址实际使用过程中替换为真实地址
  private url = 'xx.xx.xx';
  private customUserAgent: string = ' DemoApp';

  build() {
    Column() {
      Web({
        src: this.url,
        controller: this.webviewController
      })
        .onPageEnd(() => {
          try {
            let userAgent = this.webviewController.getUserAgent() + this.customUserAgent;
            this.webviewController.setCustomUserAgent(userAgent);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## 背景知识

[setCustomUserAgent](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setcustomuseragent10)：接口用于设置自定义用户代理，会覆盖系统的用户代理。

## 问题定位

分析代码发现，在onPageEnd回调中，做了一个设置自定义用户代理的操作，会导致页面重新加载，这样相当于页面加载了两次，此时滑动页面就可能发生“卡顿”现象。

## 分析结论

在onPageEnd回调中设置自定义用户代理，导致页面重新加载，相当于页面加载了两次，在加载过程中滑动页面就可能发生“卡顿”现象。

## 修改建议

将设置用户自定义代理的代码放到[onControllerAttached](../harmonyos-references/arkts-basic-components-web-events.md#oncontrollerattached10)中。

```screen
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private webviewController: webview.WebviewController = new webview.WebviewController();
  // 此处地址实际使用过程中替换为真实地址
  private url = 'xx.xx.xx';
  private customUserAgent: string = ' DemoApp';

  build() {
    Column() {
      Web({
        src: this.url,
        controller: this.webviewController
      })
        .geolocationAccess(false)
        .fileAccess(false)
        .onControllerAttached(() => {
          console.info('onControllerAttached');
          try {
            let userAgent = this.webviewController.getUserAgent() + this.customUserAgent;
            this.webviewController.setCustomUserAgent(userAgent);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
