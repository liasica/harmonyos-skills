---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-959
title: RichEditor组件设置属性字符串后如何监听文本行数
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > RichEditor组件设置属性字符串后如何监听文本行数
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:14+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:e9d69abe54606b2fbf28fd3a63d49c5b695b378679dc461421070fac7b35ec90
---

## 问题现象

RichEditor组件使用控制器方法RichEditorStyledStringController.setStyledString设置属性字符串，无法触发onContentChanged回调，如何监听渲染后的文本行数。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/bnuWDYpYRH6Ghc1PTinRog/zh-cn_image_0000002628561580.png "点击放大")

## 背景知识

* [RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)组件支持图文混排和文本交互式编辑，通常用于响应用户对图文混合内容的输入操作。
* 通过控制器（RichEditorController、RichEditorStyledStringController）对富文本内容和样式等进行操作，当文本内容发生变化时，触发onContentChanged回调；但因规格原因，当前使用setStyledString设置显示属性字符串时，不会触发onContentChanged回调。当RichEditor的内容选择区域或编辑状态下的光标位置发生变化时，将触发onSelectionChange回调。

## 解决方案

可以通过监听光标位置变动触发onSelectionChange回调，并在回调中使用getLayoutManager().getLineCount()获取文本行数。示例代码如下：

```ts
@Entry
@Component
struct RichEditorExample {
  @State lineCount: number = 0;
  controller: RichEditorStyledStringController = new RichEditorStyledStringController();
  options: RichEditorStyledStringOptions = { controller: this.controller };
  stringStyle: StyleOptions = { styledKey: StyledStringKey.FONT, styledValue: { fontColor: Color.Black } };
  mutableStyledString: MutableStyledString = new MutableStyledString('', [this.stringStyle]);
  richEditorStyledString: MutableStyledString = new MutableStyledString('');
  newStringStyle: StyleOptions =
    { styledKey: StyledStringKey.BACKGROUND_COLOR, styledValue: new BackgroundColorStyle({ color: Color.White }) };
  styledString: StyledString = new StyledString('举头望明月，低头思故乡。', [this.newStringStyle]);
  contentChangedListener: StyledStringChangedListener = {
    onWillChange: () => {
      return true;
    },
    onDidChange: () => {
    }
  };

  build() {
    Column() {
      Text('文本行数：' + this.lineCount)
        .fontSize('20fp')
        .fontWeight(FontWeight.Bold)
        .margin({ bottom: 10 });
      RichEditor(this.options)
        .onReady(() => {
          // 设定组件展示的属性字符串
          this.controller.setStyledString(this.mutableStyledString);
          this.controller.onContentChanged(this.contentChangedListener);
        })
        .onSelectionChange(() => {
          setTimeout(() => {
            let layoutManager: LayoutManager = this.controller.getLayoutManager();
            this.lineCount = layoutManager.getLineCount();
            console.info('=> ', this.lineCount);
          }, 100);
        })
        .enableKeyboardOnFocus(false)  // 首次进入页面获取焦点不弹出软键盘
        .defaultFocus(true) // 首次进入页面获取焦点
        .height('20%')
        .width('100%');
      Button('插入文本').onClick(() => {
        // 获取组件展示的属性字符串
        this.richEditorStyledString = this.controller.getStyledString();
        this.richEditorStyledString.appendStyledString(this.styledString);
        // 使插入文本后的属性字符串展示在组件上
        this.controller.setStyledString(this.richEditorStyledString);
        this.controller.setCaretOffset(this.richEditorStyledString.length);
      });
    };
  }
}
```

## 常见FAQ

Q：使用RichEditorStyledStringController初始化的RichEditor组件如何监听软键盘输入？

A：[onContentChanged](../harmonyos-references/ts-basic-components-richeditor.md#oncontentchanged12)回调中onWillChange可以监听文本内容将要变化，请参考：[示例21（属性字符串基本功能）](../harmonyos-references/ts-basic-components-richeditor.md#示例21属性字符串基本功能)。
