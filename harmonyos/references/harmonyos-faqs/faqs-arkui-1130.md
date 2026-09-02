---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1130
title: 设置RichEditor键盘输入的字体颜色、字间距
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 设置RichEditor键盘输入的字体颜色、字间距
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a1a5da1abbe65a0789173c669a4d2938127100efeabade0840e0a608a9cb1e3b
---

## 问题现象

使用RichEditor控制器添加绿色双#号文本后，键盘输入的文本颜色也是绿色，如何设置键盘输入文本的字体颜色为黑色并调整字间距？

代码如下：

```ts
onReady(() => {
  this.controller.addTextSpan(`#${this.message}# `, {
    style:
    { fontColor: Color.Green }
  })
})
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/uTHF-dLVRimaO_xzhl1BQA/zh-cn_image_0000002658928735.gif "点击放大")

## 背景知识

* [addTextSpan](../harmonyos-references/ts-basic-components-richeditor.md#addtextspan)：添加文本内容，如果组件光标闪烁，插入后光标位置更新为新插入文本的后面。
* [letterSpacing](../harmonyos-references/ts-basic-components-richeditor.md#richeditortextstyle)：设置文本字符间距。

## 解决方案

RichEditor组件的字体样式会默认跟随最后TextSpan的样式，所以添加绿色双#号文本后，键盘输入的字体样式也是绿色。设置字间距使用style的letterSpacing属性即可。

* 方案一：style设置字体颜色，onReady事件中控制器使用addTextSpan接口添加一个''（引号里有空格），设置其样式为黑色。

  **注意** 

  必须添加一个空格字符(' ')，不是''（引号里无空格）。

  ```ts
  @Entry
  @Component
  struct RichEditorDemo {
    controller: RichEditorController = new RichEditorController();
    options: RichEditorOptions = { controller: this.controller };
    message: string = 'Hello World';

    build() {
      Column() {
        RichEditor(this.options)
          .onReady(() => {
            this.controller.addTextSpan(`#${this.message}# `, {
              style:
              { fontColor: Color.Green, letterSpacing: 1 }
            });
            this.controller.addTextSpan(' ', {
              style:
              { fontColor: Color.Black }
            });
          });
      }.padding(16);
    }
  }
  ```

* **方案二**：使用aboutToIMEInput回调，设置样式。

  ```ts
  @Entry
  @Component
  struct RichEditorText {
    controller: RichEditorController = new RichEditorController();
    options: RichEditorOptions = { controller: this.controller };
    message: string = 'Hello World';

    build() {
      Column() {
        RichEditor(this.options)
          .onReady(() => {
            this.controller.addTextSpan(`#${this.message}# `, {
              style:
              { fontColor: Color.Green }
            });
          })
          .aboutToIMEInput((value: RichEditorInsertValue) => {
            this.controller.addTextSpan(value.insertValue, {
              offset: value.insertOffset,
              style: {
                fontColor: Color.Black, letterSpacing: 1
              }
            });
            return false;
          });
      }.padding(16);
    }
  }
  ```

## 常见FAQ

Q：RichEditor的TextSpan是否可以配置backgroudcolor？

A：不可以。

Q：RichEditor是否可以通过非index的方式标记span？

A：不可以。
