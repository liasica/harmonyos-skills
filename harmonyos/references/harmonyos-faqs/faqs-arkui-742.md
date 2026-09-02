---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-742
title: 实现占位文字跟随内容一起上滑
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 实现占位文字跟随内容一起上滑
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:de66488db63e379e83a808ce98e3bfc8769d1a817c60e3707bdb373f1b7f1bb4
---

## 问题现象

设置一段占位文字，如何实现该占位文字无法被删除并且会随着输入数据的增加自动上滑的功能？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/v1o6FZW1SvenFbT7HMw3GQ/zh-cn_image_0000002628395466.gif "点击放大")

## 背景知识

* [Stack](../harmonyos-references/ts-container-stack.md)是一种堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。
* [TextArea](../harmonyos-references/ts-basic-components-textarea.md)是一种多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示。
* [onContentScroll](../harmonyos-references/ts-basic-components-textarea.md#oncontentscroll10)回调函数会在TextArea组件文本内容滚动时触发，可以用来实现占位文字跟随内容一起上滑的功能。
* [onWillDelete](../harmonyos-references/ts-basic-components-textarea.md#onwilldelete12)回调函数会在TextArea组件将要删除内容时触发，可以用来实现占位文字无法被删除的功能。

## 解决方案

1. 使用Stack组件实现占位文字和文本输入框的组合。
2. 在onContentScroll回调方法中，通过修改offsetY属性改变占位文字在Y轴上的相对偏移量，实现占位文字自动上滑的功能。
3. 在onWillDelete回调方法中，通过deleteOffset的值判断当前光标是否可以向前缩进，以实现占位文字无法被删除的功能。

完整示例参考如下：

```screen
@Entry
@Component
struct StackExample {
  txt: string = '占位文本';
  @State text: string = ' ';
  @State textValue: string = '';
  @State txtWidth: number = 0;
  @State offsetY: number = 0;
  controller: TextAreaController = new TextAreaController();

  build() {
    Row() {
      Column() {
        // 使用Stack组件实现占位文字和文本输入框的组合。
        Stack({ alignContent: Alignment.TopStart }) {
          Column() {
            Text(this.txt)
              .margin({ left: 14 })
              .fontSize(15)
              .fontColor(Color.Blue)
              .onAreaChange((oldValue: Area, newValue: Area) => {
                this.txtWidth = newValue.width as number;
              })
              .offset({ x: 0, y: this.offsetY })
          }
          .width(300)
          .height(92)
          .alignItems(HorizontalAlign.Start)
          .border({ width: 1 })
          .margin({ top: 8 })
          .clip(true)

          TextArea({ text: this.text, controller: this.controller })
            .width(300)
            .height(100)
            .wordBreak(WordBreak.BREAK_ALL)
            .textIndent(this.txtWidth)
            .onChange((info) => {
              this.text = info;
              this.textValue = this.text.trim();
            })
              // 在onContentScroll回调方法中，通过修改offsetY属性改变占位文字在Y轴上的相对偏移量，实现占位文字自动上滑的功能。
            .onContentScroll((totalOffsetX: number, totalOffsetY: number) => {
              if ((this.getUIContext().px2vp(totalOffsetY) - 8) > 0) {
                this.offsetY = 0;
              } else if ((this.getUIContext().px2vp(totalOffsetY) - 8) < -16) {
                this.offsetY = -16;
              } else {
                this.offsetY = (this.getUIContext().px2vp(totalOffsetY) - 8);
              }
            })
              // 在onWillDelete回调方法中，通过deleteOffset的值判断当前光标是否可以向前缩进，以实现占位文字无法被删除的功能。
            .onWillDelete((info: DeleteValue) => {
              if (info.deleteOffset === 1 || this.text === ' ') {
                return false;
              }
              return true;
            })
            .onDidDelete((info: DeleteValue) => {
              if (info.deleteOffset === 0) {
                this.text = ' ';
              }
            })
            .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
              if (selectionStart === 0) {
                if (selectionStart === selectionEnd) {
                  this.controller.caretPosition(1);
                } else {
                  this.controller.setTextSelection(1, selectionEnd);
                }
              }
            })
        }
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
