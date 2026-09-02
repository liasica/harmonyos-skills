---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1284
title: 如何利用属性字符串实现文字长按变色
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何利用属性字符串实现文字长按变色
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8c8e4fda3d5c81e197a313f705cd61c7ab76117cc8f251a0e2ba0238c846925f
---

## 问题现象

使用Text组件嵌套Span组件如何做到选中之后单独设置颜色，并且添加点击事件？

## 背景知识

* [属性字符串](../harmonyos-references/ts-universal-styled-string.md)是方便灵活应用文本样式的对象，可通过TextController中的[setStyledString](../harmonyos-references/ts-basic-components-richeditor.md#setstyledstring12)方法与Text组件绑定。
* [replaceString](../harmonyos-references/ts-universal-styled-string.md#replacestring)：可以替换指定范围的字符串。

## 解决方案

* 可以利用属性字符串实现，实现思路如下：
  1. 参照官网示例-[设置事件](../harmonyos-references/ts-universal-styled-string.md#示例2设置事件)给Text绑定长按事件。

     ```screen
     mutableStyledString: MutableStyledString = new MutableStyledString(this.message, [
       {
         start: 0,
         length: 5,
         styledKey: StyledStringKey.GESTURE,
         styledValue: this.clickGestureAttr
       },
       {
         start: 0,
         length: 5,
         styledKey: StyledStringKey.FONT,
         styledValue: this.fontStyleAttr1
       },
       {
         start: 6,
         length: 5,
         styledKey: StyledStringKey.FONT,
         styledValue: this.fontStyleAttr2
       }
     ]);
     ```
  2. 参照官网示例-[属性字符串处理](../harmonyos-references/ts-universal-styled-string.md#示例1属性字符串处理)给已绑定的属性字符串实现长按替换效果。

     ```screen
     clickGestureAttr: GestureStyle = new GestureStyle({
       onLongPress: () => {
         this.mutableStyledString.replaceStyle({
           start: 0,
           length: 5,
           styledKey: StyledStringKey.FONT,
           styledValue: new TextStyle({ fontColor: Color.Pink })
         });
         this.controller.setStyledString(this.mutableStyledString);
       }
     });
     ```

  完整示例参考如下：

  ```screen
  @Entry
  @Component
  struct MutableStyledStringChangeColor {
    @State message: string = 'Hello World';
    fontStyleAttr1: TextStyle = new TextStyle({ fontColor: Color.Blue });
    fontStyleAttr2: TextStyle = new TextStyle({ fontColor: Color.Green });
    controller: TextController = new TextController();
    clickGestureAttr: GestureStyle = new GestureStyle({
      onLongPress: () => {
        this.mutableStyledString.replaceStyle({
          start: 0,
          length: 5,
          styledKey: StyledStringKey.FONT,
          styledValue: new TextStyle({ fontColor: Color.Pink })
        });
        this.controller.setStyledString(this.mutableStyledString);
      }
    });
    mutableStyledString: MutableStyledString = new MutableStyledString(this.message, [
      {
        start: 0,
        length: 5,
        styledKey: StyledStringKey.GESTURE,
        styledValue: this.clickGestureAttr
      },
      {
        start: 0,
        length: 5,
        styledKey: StyledStringKey.FONT,
        styledValue: this.fontStyleAttr1
      },
      {
        start: 6,
        length: 5,
        styledKey: StyledStringKey.FONT,
        styledValue: this.fontStyleAttr2
      }
    ]);

    async onPageShow() {
      this.controller.setStyledString(this.mutableStyledString);
    }

    build() {
      Column() {
        // 包含事件的属性字符串
        Text(undefined, { controller: this.controller })
          .fontSize(30)
          .copyOption(CopyOptions.InApp)
          .draggable(true)
          .clip(true);
      }
      .height('100%')
      .width('100%');
    }
  }
  ```
