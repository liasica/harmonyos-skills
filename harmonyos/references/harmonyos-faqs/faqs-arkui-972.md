---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-972
title: 如何实现评论输入框支持自定义表情展示
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现评论输入框支持自定义表情展示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6b047716329b0dad75b41476e456bdb2464dfa3927e91a9885221115c01cee92
---

## 问题现象

直播弹幕输入评论功能，在自定义键盘中使用TextArea不支持表情展示，用户体验不佳，希望实现底部模态弹窗评论输入框，支持自定义表情预览展示。

## 背景知识

* [bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)：通过bindSheet属性为组件绑定半模态页面，在组件插入时可通过设置自定义或默认的内置高度确定半模态大小。
* [RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)：支持图文混排和文本交互式编辑的组件，其中可通过[addImageSpan](../harmonyos-references/ts-basic-components-richeditor.md#addimagespan)添加图片内容。

## 解决方案

1. 通过半模态弹窗实现自定义表情UI视图。
2. 使用RichEditor组件实现图文混排输入框功能。
3. 使用[focusControl.requestFocus](../harmonyos-references/ts-universal-attributes-focus.md#requestfocus9)控制输入框获焦，获焦后半模态弹窗时软键盘会自动弹出。
4. 点击自定义表情时通过addImageSpan接口添加到输入框。

完整示例参考如下：

```screen
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct RichEditorPage {
  controller: RichEditorController = new RichEditorController();
  @State isShow: boolean = false;

  @Builder
  myBuilder() {
    Column() {
      RichEditor({ controller: this.controller }) // 绑定自定义键盘
        .margin(10)
        .height(50)
        .backgroundColor(Color.White)
        .borderRadius(20)
        .id('RichEditor')
        .onDidChange((rangeBefore: TextRange, rangeAfter: TextRange) => {
          console.info(`RichEditor onDidChange rangeBefore: ${JSON.stringify(rangeBefore)} And rangeAfter: ${JSON.stringify(rangeAfter)}`);
        });
      Button('点击添加自定义表情')
        .onClick(() => {
          this.controller.stopEditing();
          // $r('app.media.emoji')需要替换为开发者所需的图像资源文件。
          this.controller.addImageSpan($r('app.media.emoji'), {
            imageStyle: {
              size: ['80px', '80px'],
              layoutStyle: {
                borderRadius: '50px',
                margin: '40px'
              }
            }
          });
        });
    }
    .backgroundColor(Color.Orange)
    .width('100%')
    .height('100%');
  }

  build() {
    Column() {
      Button('半模态弹框')
        .onClick(() => {
          this.isShow = true;
        })
        .fontSize(20)
        .bindSheet($$this.isShow, this.myBuilder(), {
          height: 450,
          backgroundColor: Color.Green,
          showClose: false,
          radius: { topStart: LengthMetrics.vp(0), topEnd: LengthMetrics.vp(0) },
          onWillAppear: () => {
            console.info('BindSheet onWillAppear.');
            focusControl.requestFocus('RichEditor'); // 使RichEditor获焦
          },
          onAppear: () => {
            console.info('BindSheet onAppear.');
          },
          onWillDisappear: () => {
            console.info('BindSheet onWillDisappear.');
          },
          onDisappear: () => {
            this.isShow = false;
            console.info('BindSheet onDisappear.');
          }
        });
    }
    .width('100%')
    .height('100%');
  }
}
```
