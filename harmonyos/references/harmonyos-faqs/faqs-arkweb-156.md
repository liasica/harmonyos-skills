---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-156
title: 如何使Web组件不自动获取焦点
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何使Web组件不自动获取焦点
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7711bbf5501ba595703f17d901f41cb4792dae45f0c36079d47dd5a157e8192d
---

## 问题现象

Web组件调用loadUrl方法后如何设置不自动获取焦点？

## 背景知识

* [loadUrl](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)：用于加载指定的URL，该API除了指定需要加载的URL外，还可以设置URL的附加HTTP请求头。
* [焦点事件](../harmonyos-references/ts-universal-focus-event.md)：指页面焦点在可获焦组件间移动时触发的事件，组件可使用焦点事件来处理相关逻辑。
* [onFocus](../harmonyos-references/ts-universal-focus-event.md#onfocus)：当前组件获取焦点时触发的回调。
* [onBlur](../harmonyos-references/ts-universal-focus-event.md#onblur)：当前组件失去焦点时触发的回调。
* [focusable](../harmonyos-references/ts-universal-attributes-focus.md#focusable)：为通用属性，设置当前组件是否可以获焦。
  + 当focusable设置为false时为失焦状态，并触发失焦回调onBlur。
  + 当focusable设置为true时为获焦状态，并触发获焦回调onFocus。

## 解决方案

Web组件调用loadUrl方法后，将focusable属性设置为false时就可以不自动获取焦点，通过onBlur和onFocus回调获取当前焦点状态。

```screen
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  @State webBorderColor: Color = Color.Yellow;
  @State isFocus: boolean = false;

  build() {
    Column() {
      Row({ space: 10 }) {
        Button('loadUrl调用按钮')
          .onClick(() => {
            try {
              this.controller.loadUrl('www.example.com');
              this.isFocus = false;
            } catch (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          });
        Button('获取焦点按钮')
          .onClick(() => {
            try {
              this.controller.requestFocus();
              this.isFocus = true;
            } catch (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          });
      }.padding({ top: 20, bottom: 20 });

      Web({ src: 'www.example.com', controller: this.controller }) // 监听获焦事件，获焦后改变颜色
        .onFocus(() => {
          this.webBorderColor = Color.Red;
        }) // 监听失焦事件，失焦后改变颜色
        .onBlur(() => {
          this.webBorderColor = Color.Yellow;
        })
        .fileAccess(false)
        .geolocationAccess(false)
        .margin(3)
        .borderWidth(10)
        .borderColor(this.webBorderColor)
        .focusable(this.isFocus)
        .height('45%');
    };
  }
}
```
