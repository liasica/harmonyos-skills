---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-54
title: 输入框拉起键盘时，如何将底部布局弹起到键盘顶部
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 输入框拉起键盘时，如何将底部布局弹起到键盘顶部
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f0c0d0178a446d437a8aa2d0bf31e50bfeca13666bf5e4034b94e977a5d3e145
---

**原因分析**

软键盘弹出时，默认顶起输入框，下方的显示组件将被遮挡。

**解决措施**

获取窗口内容规避的区域，规避区域类型为软键盘区域（TYPE\_KEYBOARD）。当软键盘弹出时，获取规避区域的高度，并通过设置margin-bottom顶起组件。参考代码如下：

```ts
import { window } from '@kit.ArkUI';

@Entry
struct BottomPopsUpAsTheTopOfKeyboard {
  context = this.getUIContext();
  scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4, 5];
  @State scrollHeight: number = 0;
  @State isRebuild: boolean = false;
  @State keyHeight: number = 0;
  @State text: string = '';
  aboutToAppear() {
    window.getLastWindow(this.context.getHostContext()).then(currentWindow => {
      // Set the layout of the window to immersive layout
      currentWindow.setWindowLayoutFullScreen(true);
      let property = currentWindow.getWindowProperties();
      // Initialize window height
      let avoidArea = currentWindow.getWindowAvoidArea(window.AvoidAreaType.TYPE_KEYBOARD);
      this.scrollHeight = this.getUIContext().px2vp(property.windowRect.height - avoidArea.bottomRect.height);
      // Monitor the hiding and showing of the soft keyboard
      currentWindow.on('avoidAreaChange', data => {
        if (data.type == window.AvoidAreaType.TYPE_KEYBOARD) {
          this.keyHeight = this.getUIContext().px2vp(data.area.bottomRect.height);
          this.scrollHeight =
            this.getUIContext().px2vp(currentWindow.getWindowProperties().windowRect.height - data.area.bottomRect.height);
          return;
        }
      })
    })
  }
  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Column() {
        Scroll(this.scroller) {
          Column() {
            TextInput({ text: this.text, placeholder: 'input your word...' })
              .placeholderFont({
                size: 14,
                weight: 400
              })
              .width(320)
              .height(40)
              .margin(200)
              .fontSize(14)
              .fontColor(Color.Black)
              .backgroundColor(Color.White)
            ForEach(this.arr, (item: number) => {
              Text(item.toString())
                .width('90%')
                .height(150)
                .backgroundColor(0xFFFFFF)
                .borderRadius(15)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .margin({ top: 10 })
            })
          }
          .width('100%')
        }
        .width('100%')
        .height(this.scrollHeight)
        .layoutWeight(1)
        Text('This is a test text')
          .width('100%')
          .height(50)
          .backgroundColor(Color.Red)
          .margin({ bottom: this.keyHeight })
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Start)
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
  }
}
```

**参考链接**

[AvoidAreaType](../harmonyos-references/arkts-apis-window-e.md#avoidareatype7)
