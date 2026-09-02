---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1051
title: HarmonyOS如何加载HTML文本
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > HarmonyOS如何加载HTML文本
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5d75b2a7a4a800f66fd6ea8ff975f1b1f8989a97420becbb6682b7ef96c12329
---

## 问题现象

HarmonyOS组件如何实现加载富文本HTML文本。

## 背景知识

* [RichText](../harmonyos-references/ts-basic-components-richtext.md)组件适用于加载与显示一段HTML字符串，且不需要对显示效果进行较多自定义的应用场景。
* [RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)：支持图文混排和文本交互式编辑的组件。
* [RichEditorController.fromStyledString](../harmonyos-references/ts-basic-components-richeditor.md#fromstyledstring12)：将属性字符串转换为span信息。
* [StyledString.fromHtml](../harmonyos-references/ts-universal-styled-string.md#fromhtml)：将HTML格式字符串转换成属性字符串，当前支持转换的HTML标签范围：<p>、<span>、<img>、<br>、<strong>、<b>、<a>、<i>、<em>、<s>、<u>、<del>、<sup>、<sub>。支持将标签中的style属性样式转换成对应的属性字符串样式。
* [ArkWeb](../harmonyos-guides/web-component-overview.md)：提供了[Web](../harmonyos-references/ts-basic-components-web.md)组件，用于在应用程序中显示Web页面内容。

## 解决方案

由背景知识可知，有以下三种解决方案可以实现HarmonyOS加载HTML文本。

方案一：RichText是HarmonyOS中的富文本组件，能够解析并显示HTML格式文本。示例代码如下：

```ts
@Entry
@Component
struct Solution3Page {
  data: string = '<p style="color:black;font-size:50px;font-weight:800">穿越时空回到过去我也是一个人才了</p>' +
    '<p style="color:black;font-size:50px;">神作大赏</p>' +
    '<span style="color:blue;font-size:50px;">#我重生在国庆放假的前一天</span>' + '</p><p>' +
    '<a style="color:blue;font-size:40px;" href="https://developer.huawei.com/consumer/cn/discover/" >《苏梅梅的超市》</a>' +
    '</p><p>' + '<br/>';
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  build() {
    Flex({
      direction: FlexDirection.Column, alignItems: ItemAlign.Start,
      justifyContent: FlexAlign.Start
    }) {
      RichText(this.data)
        .onStart(() => {
          console.info('RichText onStart');
        })
        .onComplete(() => {
          console.info('RichText onComplete');
        })
        .width('100%')
        .height(300)
        .backgroundColor(0XBDDB69)
    }
  }
}
```

方案二：RichEditor可通过属性字符串的fromHtml将HTML转为属性字符串，再将得到属性字符串通过fromStyledString方法转换为span信息，最终将span信息添加到RichEditor中。参考代码如下：

```ts
@Entry
@Component
struct Solution2Page {
  private controller: RichEditorController = new RichEditorController();
  @State StyledString: StyledString | undefined = undefined;
  message: string =
    '<span style="font-size: 16.00px;font-style: normal;font-weight: normal;color: #000000E5;">啦啦啦</span><span style="font-size: 16.00px;font-style: normal;font-weight: normal;color: #FF0000FF;">啦</span><span style="font-size: 16.00px;font-style: normal;font-weight: normal;color: #000000E5;">啦啦</span><span style="font-size: 16.00px;font-style: normal;font-weight: bolder;color: #000000E5;">啦</span><span style="font-size: 16.00px;font-style: normal;font-weight: normal;color: #000000E5;">啦啦啦啦啦啦啦啦啦啦</span>';

  aboutToAppear(): void {
    StyledString.fromHtml(this.message).then((StyledString: StyledString) => {
      this.StyledString = StyledString; // 将html转属性字符串
    });
  }

  build() {
    Column() {
      RichEditor({ controller: this.controller })
        .height('35%')
        .border({ width: 1, color: Color.Blue })
        .onReady(() => {
          let t = this.controller.fromStyledString(this.StyledString); // 将属性字符串
          t.forEach(item => { // 编辑span并添加
            this.controller.addTextSpan((item as RichEditorTextSpanResult).value,
              { style: (item as RichEditorTextSpanResult).textStyle });
          });
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

方案三：Web组件可以通过loadData()接口实现加载HTML格式的文本数据。当开发者不需要加载整个页面，只需要显示一些页面片段时，可通过此功能来快速加载页面，当加载大量HTML文件时，需设置第四个参数baseUrl为"data"。示例代码如下：

```ts
import { webview } from '@kit.ArkWeb';
import call from '@ohos.telephony.call';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  msg: string =
    '<!DOCTYPE html>' + '<html><body><header></header>' +
      '<p style="font-size:60px">登录遇到问题？请联系官方客服</p><a href=\'tel:021-60314450\'>021-60314450</a><br>服务时间：工作日9:00-19:00</body></html>';

  build() {
    Column() {
      Web({ src: '', controller: this.controller })
        .onControllerAttached(() => {
          this.controller.loadData(
            encodeURIComponent(this.msg),
            'text/html',
            'UTF-8',
            '',
            ''
          );
        })
        .onOverrideUrlLoading((webResourceRequest: WebResourceRequest) => {
          console.log(webResourceRequest.getRequestUrl().slice(4));
          call.makeCall(webResourceRequest.getRequestUrl().slice(4), (err: BusinessError) => {
            console.log(`callback: err->${JSON.stringify(err)}}`);
          });
          return true;
        })
        .fileAccess(false)
        .geolocationAccess(false)
    }
  }
}
```

## 总结

以上介绍了HarmonyOS中主流富文本方案和可运行示例代码，可以总结出以下差异点，在实际使用过程中，可以根据适用场景来选择合适的方案实现加载富文本HTML。

| 方案 | 适用场景 | 优势 | 局限 |
| --- | --- | --- | --- |
| RichText | 简单一段HTML渲染 | 轻量、性能好 | 样式支持有限 |
| RichEditor | 可编辑富文本 | 支持插入图片、链接、样式 | 不适合纯展示，有输入法干扰 |
| Web 组件 | 完整HTML/CSS/JS支持 | 功能最全，兼容Web标准 | 重量级、性能开销大 |
