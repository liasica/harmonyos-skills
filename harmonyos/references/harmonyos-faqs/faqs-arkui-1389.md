---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1389
title: 输入字符时光标总会跳转到最后
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 输入字符时光标总会跳转到最后
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:09+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4ca24ff68335eef2f72e6dce3947d8b45a7b6dfccc5e8b3f020758f474e27100
---

## 问题现象

用户将光标移动到内容中间，执行输入或删除操作后，光标总是跳到最后。

## 背景知识

[TextInput](../harmonyos-references/ts-basic-components-textinput.md)：单行文本输入框组件。

[onChange](../harmonyos-references/ts-basic-components-textinput.md#onchange)：输入内容发生变化时，触发该回调。

[caretPosition](../harmonyos-references/ts-basic-components-textinput.md#caretposition10)：设置光标位置。

## 问题定位

1. 使用ArkUI Inspector查看组件实现方式，确认为TextInput组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/2UpV3wjOQU-0Fbx4Wb_yXg/zh-cn_image_0000002658961877.png "点击放大")
2. 检查TextInput的onChange事件，没有使用caretPosition设置光标位置，根据onChange函数的定义，该回调会在输入值变化后被触发，所以中间执行插入或删除操作改变value值，导致数据需要重新格式化，也就是重新赋值，此时光标会位于输入值的末尾。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/AdaHBNTxQ_u58r0qOjyB0A/zh-cn_image_0000002628602666.png)

## 分析结论

onChange函数的规格，未在value值变化之前获取光标位置并重新定位。

## 修改建议

参考以下Demo正确展示光标位置：

```ts
@Entry
@Component
struct TextInputExample {
  controller: TextInputController = new TextInputController();
  @State inputValue: string = '';
  @State currentCaretOffset: number = 0;

  // 自定义键盘组件
  @Builder
  CustomKeyboardBuilder() {
    Column() {
      // 数字键盘
      Grid() {
        ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {
          GridItem() {
            Button(`${item}`)
              .width(110)
              .backgroundColor('#ffffff')
              .fontColor('#000000')
              .onClick(() => {
                // 在当前光标位置插入字符
                this.inputValue = this.inputValue.slice(0, this.currentCaretOffset) +
                  item + this.inputValue.slice(this.currentCaretOffset);
                this.currentCaretOffset++;
              })
          }
        })
      }
      .maxCount(3)
      .columnsGap(10)
      .rowsGap(10)
      .padding(5)
    }
    .backgroundColor(Color.Gray)
    .margin({ bottom: 36 })
    .padding({ top: 16, bottom: 16 })
  }

  build() {
    Column() {
      TextInput({ controller: this.controller, text: $$this.inputValue })
        .onChange(() => {
          this.controller.caretPosition(this.currentCaretOffset);
        })
        .onEditChange((isEditing: boolean) => {
          if (isEditing) {
            // 开始编辑时同步光标位置
            const caret = this.controller.getCaretOffset();
            this.currentCaretOffset = caret.index;
          }
        })
        .onTextSelectionChange((selectionStart) => {
          // 记录光标位置
          this.currentCaretOffset = selectionStart;
        })
        .onPaste((pasteValue: string) => {
          // 处理粘贴功能
          if (pasteValue && pasteValue.length > 0) {
            this.inputValue = this.inputValue.slice(0, this.currentCaretOffset) +
              pasteValue + this.inputValue.slice(this.currentCaretOffset);
            this.currentCaretOffset += pasteValue.length;
          }
          // 返回true表示已处理粘贴事件
          return true;
        })
        .customKeyboard(this.CustomKeyboardBuilder())
        .margin(10)
        .width('100%')
        .padding(10)
        .borderRadius(30)
    }.padding(16)
  }
}
```

效果展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/k7dVa3HWQ_ilxJHhXDMGDA/zh-cn_image_0000002658841937.png "点击放大")
