---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1314
title: 如何获取Span的位置信息
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何获取Span的位置信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fc702959dfdbe1851b897db4afaeba0fb3d5cea9c36d5c85a7874a1c5e50a612
---

## 问题现象

在UI开发中，如何获取Text中某个Span的位置信息？

## 背景知识

* [Span](../harmonyos-references/ts-basic-components-span.md)：作为Text、ContainerSpan组件的子组件，用于显示行内文本的组件。
* [ImageSpan](../harmonyos-references/ts-basic-components-imagespan.md)：Text、ContainerSpan组件的子组件，用于显示行内图片。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)：组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。

## 解决方案

Text中的ImageSpan支持onAreaChange事件，可通过在Span前添加一个宽高均为0的ImageSpan，在ImageSpan的onAreaChange获取到ImageSpan的位置，即为Span的位置。

```ts
@Entry
@Component
struct SpanPage {
  @State span2x: number = 0;
  @State span2y: number = 0;

  build() {
    Column() {
      Text() {
        Span('Span1')
          .fontSize(18);
        ImageSpan($r('app.media.startIcon'))
          .width(0)
          .height(0)
          .border({ width: 1 })
          .onAreaChange((oldValue: Area, newValue: Area) => {
            this.span2x = newValue.globalPosition.x as number;
            this.span2y = newValue.globalPosition.y as number;
            console.info(`Span2相对页面左上角的x坐标为${newValue.globalPosition.x},y坐标为${newValue.globalPosition.y}`);
          });
        Span('Span2')
          .fontSize(18);
      };

      Text(`Span2相对页面左上角的x坐标为${this.span2x},y坐标为${this.span2y}`);
    }
    .height('100%')
    .width('100%');
  }
}
```
