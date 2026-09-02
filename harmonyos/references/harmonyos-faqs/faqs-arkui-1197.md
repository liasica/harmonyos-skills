---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1197
title: 如何解决TextInput文本内容超出父组件的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决TextInput文本内容超出父组件的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9bbe4bfc3f0d631b548f6884d6336620abdb6f56d39baf71c208b0a9ba6d4644
---

## 问题现象

TextInput组件绑定自定义键盘，如何实现当内容超过父组件宽度时新输入的内容能够全部显示，已输入的内容向左移动，超出父组件部分的内容可以隐藏的效果？

问题代码示例参考如下：

```ts
build() {
  // ...
  RelativeContainer() {
    Text("￥")
      .fontSize(24)
      .fontColor($r('app.color.black'))
      .maxLines(1)
      .padding({ left: 3, right: 3 })
      .id('money_symbol')

    TextInput({ text: this.input, placeholder: "0.00" })
      .placeholderColor($r('app.color.black'))
      .placeholderFont({ size: 24, weight: FontWeight.Regular })
      .fontSize(24)
      .fontWeight(FontWeight.Regular)
      .fontColor($r('app.color.black'))
      .maxLines(1)
      .textAlign(TextAlign.End)
      .enableKeyboardOnFocus(false) // 不弹起系统键盘
      .caretColor(Color.Transparent) // 设置光标透明色
      .backgroundColor(Color.Transparent)
      .margin({ right: 12 })
      .padding(0)
      .id('money')
      .width('auto')
      .alignRules({
        top: { anchor: '__container__', align: VerticalAlign.Top },
        bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
        right: { anchor: '__container__', align: HorizontalAlign.End }
      })

  }
  .backgroundImage($r('app.media.bg_keyboard_input_box'))
  .backgroundImageSize(ImageSize.FILL)
  .width(289)

  Row({ space: 10 }) {
    KeyboardButton({ text: this.numbers[7] })
      .onClick(() => {
        this.input = this.calculator.input(this.numbers[7])
      })
    KeyboardButton({ text: this.numbers[8] })
      .onClick(() => {
        this.input = this.calculator.input(this.numbers[8])
      })
    KeyboardButton({ text: this.numbers[9] })
      .onClick(() => {
        this.input = this.calculator.input(this.numbers[9])
      })
    KeyboardButton({
      text: this.date,
      fontSize: 15,
      fontWeight: FontWeight.Medium,
      imageWidth: 18,
    })
  }

  // ...

}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/Fe9q4jv_RX25XDf8ulwYiQ/zh-cn_image_0000002658952189.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/gMrJc8KNSzOKfUEu3eX9vA/zh-cn_image_0000002628592998.png "点击放大")

## 背景知识

* [TextInput](../harmonyos-references/ts-basic-components-textinput.md)：单行文本输入框组件。
* [textAlign](../harmonyos-references/ts-basic-components-textinput.md#textalign9)：设置文本在输入框中的水平对齐方式。仅支持TextAlign.Start、TextAlign.Center和TextAlign.End。
* [requestFocus](../harmonyos-references/ts-universal-attributes-focus.md#requestfocus9)：调用此接口可以主动让焦点在下一帧渲染时转移至参数指定的组件上。

## 解决方案

输入内容时给自定义键盘点击事件添加获焦逻辑，使TextInput组件获取到焦点实现当内容超过组件宽度时自动左滑的功能。

* Index页面内容：

  ```ts
  import { Calculator } from './Calculator';

  @Entry
  @Component
  struct Index {
    @State input: ResourceStr = '';
    date: string = '日期';
    private calculator: Calculator = new Calculator(100, 100);
    private context: Context = this.getUIContext().getHostContext() as Context;
    private numbers: Array<string> =
      this.context.resourceManager.getStringArrayValueSync($r('app.strarray.accounting_keyboard').id); // 根据具体情况加载资源

    build() {

      Column({ space: 5 }) {
        Row() {
          Text('￥')
            .fontSize(24)
            .fontColor($r('app.color.black')) // 根据具体情况加载资源
            .maxLines(1)
            .padding({ left: 3, right: 0 })
            .id('money_symbol')
            .alignRules({
              top: { anchor: '__container__', align: VerticalAlign.Top },
              bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
              right: { anchor: 'money', align: HorizontalAlign.Start }
            });

          RelativeContainer() {
            TextInput({ text: this.input, placeholder: '0.00' })
              .placeholderColor($r('app.color.black')) // 根据具体情况加载资源
              .placeholderFont({ size: 24, weight: FontWeight.Regular })
              .fontSize(24)
              .fontWeight(FontWeight.Regular)
              .fontColor($r('app.color.black')) // 根据具体情况加载资源
              .maxLines(1)
              .textAlign(TextAlign.End)
              .enableKeyboardOnFocus(false) // 不弹起系统键盘
              .caretColor(Color.Transparent) // 不希望有光标
              .backgroundColor(Color.Transparent)
              .margin({ right: 12 })
              .padding(0)
              .id('money')
              .width('auto')
              .alignRules({
                top: { anchor: '__container__', align: VerticalAlign.Top },
                bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
                right: { anchor: '__container__', align: HorizontalAlign.End }
              });
          }
          .width(289);
        }
        .height(52)
        .border({ width: 2 })
        .borderRadius(12)
        .margin({ top: 16 });

        Column() {
          Row({ space: 10 }) {
            // 给自定义键盘点击事件添加获焦操作。以按键数字“7”为例
            KeyboardButton({ text: this.numbers[7] })
              .onClick(() => {
                this.input = this.calculator.input(this.numbers[7]);
                this.getUIContext().getFocusController().requestFocus('money');
              });
            KeyboardButton({ text: this.numbers[8] })
              .onClick(() => {
                this.input = this.calculator.input(this.numbers[8]);
                this.getUIContext().getFocusController().requestFocus('money');
              });
            KeyboardButton({ text: this.numbers[9] })
              .onClick(() => {
                this.input = this.calculator.input(this.numbers[9]);
                this.getUIContext().getFocusController().requestFocus('money');
              });
            KeyboardButton({
              text: this.date,
              fontSize: 18,
              fontWeight: FontWeight.Medium,
              imageWidth: 18,
            });
          };

          Row({ space: 10 }) {
            KeyboardButton({ text: this.numbers[4] })
              .onClick(() => {
                this.input = this.calculator.input(this.numbers[4]);
                this.getUIContext().getFocusController().requestFocus('money');
              });
            KeyboardButton({ text: this.numbers[5] })
              .onClick(() => {
                this.input = this.calculator.input(this.numbers[5]);
                this.getUIContext().getFocusController().requestFocus('money');
              });
            KeyboardButton({ text: this.numbers[6] })
              .onClick(() => {
                this.input = this.calculator.input(this.numbers[6]);
                this.getUIContext().getFocusController().requestFocus('money');
              });
            KeyboardButton({ text: this.numbers[12], fontSize: 27 })
              .onClick(() => {
                this.input = this.calculator.input(this.numbers[12]);
              });
          };

          Row({ space: 10 }) {
            KeyboardButton({ text: this.numbers[1] })
              .onClick(() => {
                this.input = this.calculator.input(this.numbers[1]);
                this.getUIContext().getFocusController().requestFocus('money');
              });
            KeyboardButton({ text: this.numbers[2] })
              .onClick(() => {
                this.input = this.calculator.input(this.numbers[2]);
                this.getUIContext().getFocusController().requestFocus('money');
              });
            KeyboardButton({ text: this.numbers[3] })
              .onClick(() => {
                this.input = this.calculator.input(this.numbers[3]);
                this.getUIContext().getFocusController().requestFocus('money');
              });
            KeyboardButton({ text: this.numbers[11], fontSize: 27 })
              .onClick(() => {
                this.input = this.calculator.input(this.numbers[11]);
              });
          };

          Row({ space: 10 }) {
            KeyboardButton({ text: this.numbers[10] })
              .onClick(() => {
                this.input = this.calculator.input(this.numbers[10]);
              });
            KeyboardButton({ text: this.numbers[0] })
              .onClick(() => {
                this.input = this.calculator.input(this.numbers[0]);
                this.getUIContext().getFocusController().requestFocus('money');
              });
            KeyboardButton({ icon: $r('app.media.ic_keyboard_del') }) // 根据具体情况加载资源
              .onClick(() => {
                this.input = this.calculator.delete();
              });
            KeyboardButton({
              text: '完成',
              fontSize: 18,
              fonColor: $r('app.color.white'), // 根据具体情况加载资源
              fontWeight: FontWeight.Medium
            })
              .onClick(() => {
                this.input = this.calculator.input(this.numbers[13]);
              });
          };
        }
        .justifyContent(FlexAlign.SpaceAround)
        .alignItems(HorizontalAlign.Center)
        .width('100%')
        .height('30%')
        .backgroundColor('#DEE0E6')
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.SpaceBetween)
      .alignItems(HorizontalAlign.Center)
      .padding({ bottom: 0 });
    }
  }

  @Preview
  @Component
  export struct KeyboardButton {
    @State isClick: boolean = false;
    text?: ResourceStr;
    icon?: ResourceStr;
    buttonWidth: number = 80;
    imageWidth: number = 29.5;
    fontSize: number = 24;
    fonColor: ResourceStr = $r('app.color.black'); // 根据具体情况加载资源
    fontWeight: FontWeight = FontWeight.Regular;
    btnBackground: ResourceStr = '';
    btnBackgroundPress: ResourceStr = '';

    build() {
      Stack({ alignContent: Alignment.Center }) {
        Image(this.isClick ? this.btnBackgroundPress : this.btnBackground)
          .draggable(false)
          .width(this.buttonWidth);

        Row({ space: 4 }) {
          if (this.icon) {
            Image(this.icon)
              .width(this.imageWidth);
          }
          if (this.text) {
            Text(this.text)
              .fontSize(this.fontSize)
              .fontColor(this.fonColor)
              .fontWeight(this.fontWeight);
          }
        };
      }
      .height('18%')
      .backgroundColor(Color.White)
      .borderRadius(24)
      .onTouch((event?: TouchEvent) => {
        if (event) {
          if (event.type == TouchType.Down) {
            this.isClick = true;
          }
          if (event.type == TouchType.Up) {
            this.isClick = false;
          }
        }
      });
    }
  }
  ```
* Calculator页面内容：

  ```ts
  /**
   */
  export class Calculator {
    /**
     * 整数位数
     */
    private digit: number = 10;
    /**
     * 小数点的位数
     */
    private accuracy: number = 2;
    /**
     * 匹配的正则表达式
     */
    private regExp: RegExp;
    /**
     * 当前数字的字符串
     */
    private currentStr: string = '';
    /**
     * 前一个数字的字符串
     */
    private lastStr: string = '';
    /**
     * 符号
     */
    private symbol: string = '';

    constructor(digit: number = 10, accuracy: number = 2) {
      if (digit >= 2) {
        this.digit = digit;
      }
      if (accuracy >= 0) {
        this.accuracy = accuracy;
      }
      this.regExp = new RegExp(`^-?\\\d{1,${this.digit}}(\\\.\\\d{1,${this.accuracy}})?$`);
    }

    /**
     * 输入内容
     */
    input(str: string): string {
      if (str === '+' || str === '-') {
        if (this.symbol.length > 0) {
          if (this.currentStr.length > 0) {
            if (!this.calculate()) {
              return this.lastStr + this.symbol + this.currentStr;
            }
          }
        } else if (this.lastStr.length <= 0) {
          return this.lastStr;
        } else if (this.lastStr.endsWith('.')) {
          this.lastStr += '0';
        }
        this.symbol = str;
        return this.lastStr + this.symbol + this.currentStr;
      } else if (str === '=') {
        this.calculate();
        return this.lastStr + this.symbol + this.currentStr;
      } else if (str === '.') {
        if (this.accuracy <= 0) {
          return this.lastStr + this.symbol + this.currentStr;
        }
        if (this.symbol.length > 0) {
          if (this.currentStr.length <= 0) {
            this.currentStr = '0.';
          } else if (this.currentStr.indexOf(str) < 0) {
            this.currentStr += str;
          }
        } else {
          if (this.lastStr.length <= 0) {
            this.lastStr = '0.';
          } else if (this.lastStr.indexOf(str) < 0) {
            this.lastStr += str;
          }
        }
        return this.lastStr + this.symbol + this.currentStr;
      } else {
        let result: string;
        if (this.symbol.length > 0) {
          result = this.currentStr + str;
        } else {
          result = this.lastStr + str;
        }
        if (this.regExp.test(result)) {
          if (this.symbol.length > 0) {
            this.currentStr = result;
          } else {
            this.lastStr = result;
          }
        }
        return this.lastStr + this.symbol + this.currentStr;
      }
    }

    /**
     * 删除内容
     */
    delete(): string {
      if (this.currentStr.length > 0) {
        this.currentStr = this.currentStr.slice(0, -1);
        return this.lastStr + this.symbol + this.currentStr;
      } else if (this.symbol.length > 0) {
        this.symbol = this.symbol.slice(0, -1);
        return this.lastStr + this.symbol;
      } else if (this.lastStr.length > 0) {
        this.lastStr = this.lastStr.slice(0, -1);
        return this.lastStr;
      }
      return '';
    }

    /**
     * 计算
     */
    private calculate(): boolean {
      if (this.currentStr && this.lastStr) {
        const a: number = parseFloat(this.lastStr);
        const b: number = parseFloat(this.currentStr);
        let result: number = 0;
        switch (this.symbol) {
          case '+':
            result = a + b;
            break;
          case '-':
            result = a - b;
            break;
          default:
            return false;
        }
        this.lastStr = result.toString();
        this.currentStr = '';
        this.symbol = '';
        return true;
      }
      return false;
    }
  }
  ```
