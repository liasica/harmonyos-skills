---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-933
title: TextInput修改数据后光标位置重置
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > TextInput修改数据后光标位置重置
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b40345dad585cd94afcc4a7a5b3ba14c3c4c0aa478c6531f318feed92568bcca
---

## 问题现象

在使用TextInput组件银行卡号格式化（每四位数字后自动添加一个空格）或电话号码格式化时，用户在任意位置进行删除或新增操作，光标应保留在操作位置。但实际使用中存在两个问题：一是空格可以被删除，二是执行删除或插入操作时，光标会重置到输入框末尾。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/-_7ynMj4Rn2jhgrIpKNU0Q/zh-cn_image_0000002658919559.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/FtMZhx3sRTGXp0I4GQEjvw/zh-cn_image_0000002628400356.gif "点击放大")

## 背景知识

[TextInput](../harmonyos-references/ts-basic-components-textinput.md)组件为单行输入框组件，通常用于响应用户的输入操作。当输入框中输入的内容发生变化时，会自动触发[onChange](../harmonyos-references/ts-basic-components-textinput.md#onchange)回调，该组件还可通过[caretPosition](../harmonyos-references/ts-basic-components-textinput.md#caretposition10)函数设置光标位置。

## 问题定位

onChange函数的规格为value值变化后执行，所以删除空格、删除数字或者添加数字等编辑操作改变value值，导致数据需要重新格式化，也就是重新赋值，此时光标会位于输入值的末尾。

## 分析结论

为了达到预期效果，在value值变化前就将展示结果和光标位置获取到，之后再进行赋值以及光标位置定位。

## 修改建议

参考[电话号码格式化](../harmonyos-references/ts-basic-components-textinput.md#示例6电话号码格式化)中示例，做出以下修改：

1. 在onTextSelectionChange回调函数中记录当前光标的位置；
2. 实现calcCaretPosition计算光标位置的函数；
3. 在onWillInsert和onWillDelete方法中，自定义处理增删空格逻辑。

完整示例参考如下：

```screen
@Entry
@Component
struct caretPositionExample {
  @State text: string = '';
  @State bankNumberNoSpace: string = '';
  @State nextCaret: number = -1; // 用于记录下次光标设置的位置
  @State actualCh: number = -1; // 用于记录光标在第i个数字后插入或者第i个数字前删除
  @State lastCaretPosition: number = 0;
  @State lastCaretPositionEnd: number = 0;
  controller: TextInputController = new TextInputController();

  isEmpty(str?: string): boolean {
    return str === 'undefined' || !str || !new RegExp('[^\\s]').test(str);
  }

  removeSpace(str: string): string {
    if (this.isEmpty(str)) {
      return '';
    }
    return str.replace(new RegExp('[\\s]', 'g'), '');
  }

  setCaret() {
    if (this.nextCaret !== -1) {
      console.info('to keep caret position right, change caret to', this.nextCaret);
      this.controller.caretPosition(this.nextCaret);
      this.nextCaret = -1;
    }
  }

  calcCaretPosition(nextText: string) {
    let befNumberNoSpace: string = this.removeSpace(this.text);
    this.actualCh = 0;
    if (befNumberNoSpace.length < this.bankNumberNoSpace.length) { // 插入场景
      for (let i = 0; i < this.lastCaretPosition; i++) {
        if (this.text[i] !== ' ') {
          this.actualCh += 1;
        }
      }
      this.actualCh += this.bankNumberNoSpace.length - befNumberNoSpace.length;
      for (let i = 0; i < nextText.length; i++) {
        if (nextText[i] !== ' ') {
          this.actualCh -= 1;
          if (this.actualCh <= 0) {
            this.nextCaret = i + 1;
            break;
          }
        }
      }
    } else if (befNumberNoSpace.length > this.bankNumberNoSpace.length) { // 删除场景
      if (this.lastCaretPosition === this.text.length) {
        console.info('Caret at last, no need to change');
      } else if (this.lastCaretPosition === this.lastCaretPositionEnd) {
        // 按键盘上回退键一个一个删的情况
        for (let i = this.lastCaretPosition; i < this.text.length; i++) {
          if (this.text[i] !== ' ') {
            this.actualCh += 1;
          }
        }
        for (let i = nextText.length - 1; i >= 0; i--) {
          if (nextText[i] !== ' ') {
            this.actualCh -= 1;
            if (this.actualCh <= 0) {
              this.nextCaret = i;
              break;
            }
          }
        }
      } else {
        // 剪切/手柄选择一次删多个字符
        this.nextCaret = this.lastCaretPosition; // 保持光标位置
      }
    }
  }

  build() {
    Column() {
      Row() {
        TextInput({ text: `${this.text}`, controller: this.controller })
          .height('48vp')
          .onChange((number: string) => {
            this.bankNumberNoSpace = this.removeSpace(number);
            let nextText: string = '';
            if (this.bankNumberNoSpace.length <= 4) {
              nextText = this.bankNumberNoSpace;
            } else {
              for (let i = 0; i < this.bankNumberNoSpace.length; i++) {
                nextText += this.bankNumberNoSpace[i];
                if ((i + 1) % 4 === 0 && i !== this.bankNumberNoSpace.length - 1) {
                  nextText += ' ';
                }
              }
            }
            if (this.text === nextText && nextText === number) {
              // 此时说明数字已经格式化完成了，在这个时候改变光标位置不会被重置掉
              this.setCaret();
            } else {
              this.calcCaretPosition(nextText);
            }
            this.text = nextText;
          })
          .onTextSelectionChange((selectionStart, selectionEnd) => {
            // 记录光标位置
            console.info('selection change: ', selectionStart, selectionEnd);
            this.lastCaretPosition = selectionStart;
            this.lastCaretPositionEnd = selectionEnd;
          }) // 使用onWillInsert和onWillDelete判断是否为空格，是空格就不给添加和删除，如果需要用户删除空格的时候不删除空格而是直接后退一位
          .onWillInsert((info: InsertValue) => {
            let value = info.insertValue;
            if (value === ' ') {
              return false;
            } else {
              return true;
            }
          })
          .onWillDelete((info: DeleteValue) => {
            let value = info.deleteValue;
            if (value === ' ') {
              return false;
            } else {
              return true;
            }
          })
      }
    }
    .width('100%')
    .height('100%')
  }
}
```

## 总结

TextInput组件通过onChange自定义处理输入值时，重新赋值后光标位置会默认位于末尾，故需要记录光标位置，进行赋值。
