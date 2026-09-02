---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-635
title: RichEditor设置内容自适应宽度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > RichEditor设置内容自适应宽度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0d0ed386f624469f1d30a6bc89b2b753faad1833c2268f160433ed0ebb9152d7
---

## 问题现象

RichEditor与Text组件不同，无法根据内容自适应自身宽度，组件会超出文本占据宽度。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/TY_llpqJTNSyJeKFB8RXXg/zh-cn_image_0000002658793547.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/smuywre-Tt2TPAG47mHWqg/zh-cn_image_0000002628554180.png "点击放大")

## 背景知识

* [RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)：是支持图文混排和文本交互式编辑的组件，通常用于响应用户对图文混合内容的输入操作，例如可以输入图文的评论区。
* [onDidChange](../harmonyos-references/ts-basic-components-richeditor.md#ondidchange12)：在组件执行增删操作后，触发回调。如果文本实际未发生增删，则不触发该回调。
* [onReady](../harmonyos-references/ts-basic-components-richeditor.md#onready)：富文本组件初始化完成后触发回调。

## 解决方案

通过文本宽度、边框宽度以及内边距宽度动态计算RichEditor的宽度。

```ts
import { display } from '@kit.ArkUI';

@Entry
@Component
struct RichEditorWidthChange {
  controller: RichEditorController = new RichEditorController();
  textStr: string = '获取指定行的行信息';
  @State richEditorWidth: number | string = '100%';
  richEditorPadding: number = 12;
  richEditorBorder: number = 1;
  private displayWidth: number = this.getUIContext().px2vp(display.getDefaultDisplaySync().width);

  // 避免调整尺寸模式
  aboutToAppear(): void {
    this.getUIContext().setKeyboardAvoidMode(1);
    console.info('displayWidth: ', this.displayWidth);
  }

  getLayoutWidth() {
    let layoutManager: LayoutManager = this.controller.getLayoutManager();
    let lineCount = layoutManager.getLineCount();
    let lineWidthSum = 0;
    for (let i = 0; i < lineCount && layoutManager.getLineMetrics(i); i++) {
      lineWidthSum = lineWidthSum + layoutManager.getLineMetrics(i).width;
    }
    lineWidthSum = this.getUIContext().px2vp(lineWidthSum) + this.richEditorPadding * 2 + this.richEditorBorder * 2;
    // 总文本宽度超过当前窗口宽度
    this.richEditorWidth = lineWidthSum >= this.displayWidth ? '100%' : lineWidthSum;
  }

  build() {
    Scroll() {
      Column() {
        RichEditor({ controller: this.controller })
          .padding(this.richEditorPadding)
          .borderRadius(20)
          .borderColor(Color.White)
          .borderWidth(this.richEditorBorder)
          .backgroundColor('#fff3f3f3')
          .width(this.richEditorWidth)
          .height('auto')
          .onReady(() => {
            this.controller.addTextSpan(this.textStr);
          })
          .onDidChange(() => {
            // 等待10ms，确保addTextSpan添加文本后，layoutManager.getLineCount()能正确感知当前行数
            setTimeout(() => {
              this.getLayoutWidth();
            }, 10);
          })
          .animation({
            duration: 200
          });
      }
      .margin({ top: 10, left: 10, right: 8 });
    };
  }
}
```
