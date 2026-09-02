---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-509
title: 如何自定义cancelButton点击事件的业务逻辑
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何自定义cancelButton点击事件的业务逻辑
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ebf4430adb72bf5af08dbcf5c080837ef18458824d1c7cc91e1dd6a3e8042823
---

## 问题现象

开发者使用cancelButton属性时，有以下经典场景：

* **场景一**：Search组件的cancelButton点击事件目前无法自定义业务逻辑，比如控制页面的显示和隐藏，只能设置样式。如何自定义Search组件的cancelButton点击事件的业务逻辑？
* **场景二**：TextInput组件的cancelButton属性设置为CancelButtonStyle.INPUT，输入内容不为空时，失焦后如何使图标隐藏？

## 背景知识

* Search组件的[cancelButton](../harmonyos-references/ts-basic-components-search.md#cancelbutton10)设置右侧清除按钮样式，仅支持自定义样式，不支持自定义点击事件。
* [onEditChange](../harmonyos-references/ts-basic-components-textinput.md#oneditchange8)：输入状态变化时，触发该回调。有光标时为编辑态，无光标时为非编辑态。

## 解决方案

* **针对场景一**：Search组件的cancelButton点击事件，只支持设置样式，如果要自定义业务逻辑，可以使用Stack在搜索框上堆叠一个图标，自行对这个图标增加业务逻辑。

  ```ts
  @Entry
  @Component
  struct Index {
    @State isFocus: boolean = false;

    build() {
      Column() {
        Stack({ alignContent: Alignment.End }) {
          Search({  placeholder: '请输入搜索内容' })
            .id('search_001')
            .height(44)
            .width('100%')
            .defaultFocus(false)
            .backgroundColor(0xFFF7F7F7)
            .textAlign(TextAlign.Start)
            .copyOption(CopyOptions.None)
            .placeholderFont({ size: 16 })
            .textFont({ size: 16 })
            .fontColor(Color.Black)
            .borderRadius(16)
            .layoutWeight(1)
            .border({
              width: 1,
              color: this.isFocus ? Color.Red : Color.Transparent,
              style: BorderStyle.Solid
            })
            .caretStyle({ width: 2, color: Color.Red })
            .cancelButton({
              style: CancelButtonStyle.INPUT,
              icon: {
                size: 80,
                src: $r('app.media.startIcon')
              }
            });
          Image($r('app.media.background'))
            .height(44)
            .onClick(() => {
              // 此处编写自定义逻辑。
              this.isFocus = !this.isFocus;
            });
        };
      };
    }
  }
  ```
* **针对场景二**：
  1. 使用三元表达式更改图标的显示模式，通过onEditChange判断当前是否为输入状态，isEditing为true时表示正在输入。
  2. 当前为编辑状态时，设置清除按钮的样式为CancelButtonStyle.INPUT，当前为非编辑态时，设置清除按钮的样式为CancelButtonStyle.INVISIBLE。

  ```ts
  @Entry
  @Component
  struct ClearNodeExample {
    @State text: string = '';
    // 编辑状态
    @State isOK: boolean = false;
    controller: TextInputController = new TextInputController();

    build() {
      Column() {
        TextInput({ placeholder: 'input ...', controller: this.controller })
          .width(350)
          .height(60)
          .margin({ bottom: 16, left: 20, right: 20 })
          .cancelButton({
            // 使用三元表达式更改图标的显示模式
            style: (this.isOK ? CancelButtonStyle.INPUT : CancelButtonStyle.INVISIBLE),
            icon: {
              size: 45,
              src: $r('app.media.startIcon'),
              color: Color.Blue
            }
          })
          .onEditChange((isEditing: boolean) => {
            // 存储TextInput组件的编辑状态
            this.isOK = isEditing;
          })
          .onChange((value: string) => {
            this.text = value;
          });
        TextInput({ placeholder: 'input ...', controller: this.controller })
          .width(350)
          .height(60)
          .margin({ left: 20, right: 20 })
          .cancelButton({
            icon: {
              size: 45,
              src: $r('app.media.startIcon'),
              color: Color.Blue
            }
          });
      };
    }
  }
  ```

## 常见FAQ

Q：[TextInput](../harmonyos-references/ts-basic-components-textinput.md)组件的cancelButton的内边距如何取消？

A：为了使cancelButton的图标在视觉上更贴近TextInput组件的最右侧，可以使用[Stack](../harmonyos-references/ts-container-stack.md)布局组件来实现图标的覆盖效果。以下是一个示例代码，展示了如何通过Stack来调整cancelButton的位置：

```ts
@Entry
@Component
struct TextInputPage {
  @State flag: boolean = false;
  @State isOK: boolean = false;
  @State text: string = '';

  build() {
    Column() {
      Stack() {
        TextInput({ placeholder: 'input ...', })
          .width(350)
          .height(60)
          .margin({ bottom: 16, left: 20, right: 20 })
          .cancelButton({
            style: (CancelButtonStyle.INPUT),
            icon: {
              size: 0,
              src: $r('app.media.startIcon'),
              color: Color.Blue
            }
          })
          .onEditChange((isEditing: boolean) => {
            this.flag = isEditing;
            this.isOK = this.flag;
          })
          .onChange((value: string) => {
            this.text = value;
          });
        if (this.isOK) {
          Image($r('app.media.startIcon')).height(50).width(50).margin({ bottom: 16, left: 318, right: 20 })
            .onClick(() => {
            });
        }
      };
    }
    .height('100%')
    .width('100%');
  }
}
```

Q：如何实现TextInput的清除按钮功能？

A：在API11及以上版本可以[设置右侧清除按钮样式](../harmonyos-references/ts-basic-components-textinput.md#示例4设置右侧清除按钮样式)；在API18及以上版本可以[设置symbol类型清除按钮](../harmonyos-references/ts-basic-components-textinput.md#示例15设置symbol类型清除按钮)。
