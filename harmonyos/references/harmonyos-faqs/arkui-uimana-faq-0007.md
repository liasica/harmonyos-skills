---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0007
title: TextInput组件常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > TextInput组件常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:10+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:3e4e6b0caafe2428043c8b1f8d719adcce36b775b813dd7a63f3a3584841443b
---

**Q：如何实现不限字数的单行输入框，且TextInput获取焦点时，光标应正常显示在文本末尾；失去焦点时，超出宽度的文本应该以省略号结尾？**

**A**：

* 方案一：
  1. textOverflow仅在内联模式的编辑态、非编辑态下支持，需设置style属性。
  2. 设置状态变量观测textOverflow、style的类型，在TextInput获焦、失焦时，展示不同的文本形式。
  3. 获焦时，判断当前类型是否为Inline，是则将style设置为Default，textOverflow设置为MARQUEE；失焦时，style设置为Inline，textOverflow设置为Ellipsis。
  4. 在Column上添加onClick事件，点击时，使用[clearFocus](../harmonyos-references/arkts-apis-uicontext-focuscontroller.md#clearfocus12)清除TextInput焦点。

  ```ts
  @Entry
  @Component
  struct Index {
    @State queryContent: string = '';
    @State textInputStyleType: TextInputStyle = TextInputStyle.Default;
    @State textOverflowType: TextOverflow = TextOverflow.Clip;
    private controller: TextInputController = new TextInputController();

    build() {
      Column() {
        TextInput({ text: this.queryContent, placeholder: '搜索感兴趣的内容', controller: this.controller })
          .borderRadius(25)
          .height(50)
          .fontSize(14)
          .fontColor('#66000000')
          .placeholderFont({ size: 14, weight: FontWeight.Medium })
          .style(this.textInputStyleType)
          .maxLines(1)
          .textOverflow(this.textOverflowType)
          .backgroundColor('#f1f3f5')
          .padding({ left: 20, right: 20 })
          .outline({ width: 0 })
          .lineBreakStrategy(LineBreakStrategy.BALANCED)
          .onFocus(() => {
            if (this.textInputStyleType === TextInputStyle.Inline) {
              this.textInputStyleType = TextInputStyle.Default;
              this.textOverflowType = TextOverflow.MARQUEE;
            }
            this.controller.caretPosition(this.queryContent.length);
          })
          .onBlur(() => {
            this.textInputStyleType = TextInputStyle.Inline;
            this.textOverflowType = TextOverflow.Ellipsis;
          })
          .onChange((value: string) => {
            this.queryContent = value;
          });
      }
      .padding(24)
      .height('100%')
      .width('100%')
      .onClick(() => {
        this.getUIContext().getFocusController().clearFocus();
      });
    }
  }
  ```

  代码运行效果：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/gfkShA-ZRcaLj_jFnBSsbg/zh-cn_image_0000002766065524.png "点击放大")
* 方案二：
  1. 失焦时，使用Text覆盖TextInput，textOverflow设置为Ellipsis，超出正常文本宽度显示省略号。
  2. 获焦时，Text隐藏，显示TextInput，不需要设置textOverflow，光标正常展示在文本最后面。
  3. 设置状态变量观测失焦和获焦状态，通过[visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)来控制Text组件的隐现。

  ```ts
  @Entry
  @Component
  struct InputTextDemo {
    @State text: string =
      '这是一个超长文本测试这是一个超长文本测试这是一个超长文本测试这是一个超长文本测试这是一个超长文本测试这是一个超长文本测试这是一个超长文本测试这是一个超长文本测试';
    @State isFocus: boolean = false;

    build() {
      Column() {
        Text('今天星期二')
          .fontSize(50)
          .margin(16);
        Stack() {
          Text(this.text)
            .width('90%')
            .height(70)
            .fontSize(16)
            .fontWeight(FontWeight.Medium)
            .fontColor('#000000')
            .maxLines(1)
            .textOverflow({ overflow: TextOverflow.Ellipsis })
            .visibility(this.isFocus ? Visibility.None : Visibility.Visible)
            .onClick(() => {
              focusControl.requestFocus('TextInput');
              this.isFocus = true;
            });

          TextInput()
            .id('TextInput')
            .width('100%')
            .height(50)
            .fontSize(16)
            .borderRadius(16)
            .fontColor('#66000000')
            .defaultFocus(false)
            .border({
              width: 1,
              color: this.isFocus ? '#f1f3f5' : Color.Transparent
            })
            .visibility(this.isFocus ? Visibility.Visible : Visibility.None)
            .onFocus(() => {
              this.isFocus = true;
            })
            .onBlur(() => {
              this.isFocus = false;
            })
            .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {
              if (event.text === '') {
                console.info(`enterKey: ${enterKey}`);
                this.isFocus = false;
              } else {
                this.text = event.text;
                this.isFocus = false;
              }
            });
        };
      }.padding(16);
    }
  }
  ```

  代码运行效果：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/ZkepsuL0Q_6hPoLAxoOjaQ/zh-cn_image_0000002795304363.png "点击放大")

**Q：TextInput组件绑定自定义键盘，如何实现当内容超过父组件宽度时新输入的内容能够全部显示，已输入的内容向左移动，超出父组件部分的内容可以隐藏的效果？主要代码如下：**

**A**：

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

异常效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/a-kh7raQRQmSNmlmUEtVjg/zh-cn_image_0000002767983188.png "点击放大")

输入内容时给自定义键盘点击事件添加获焦逻辑，使TextInput组件获取到焦点实现当内容超过组件宽度时自动左滑的功能，示例代码如下：

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

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/e1E4CLmRQwi9f3ZBbxAVSg/zh-cn_image_0000002765905994.png "点击放大")

**Q：TextInput组件获取焦点的几种场景有哪些？**

**A**：TextInput组件获取焦点的几种场景如下：

* 场景一：TextInput[主动获焦/失焦](../harmonyos-guides/arkts-common-events-focus-event.md#主动获焦失焦)。

  调用focusControl.requestFocus接口可以主动让焦点转移至参数指定的组件上。可参考如下代码：

  ```ts
  // xxx.ets
  @Entry
  @Component
  struct TextInputExample {
    build() {
      Row() {
        Column() {
          Button('The second focus acquisition')
            .onClick(() => {
              focusControl.requestFocus('BBB'); // Get focus on the second input box
            })

          TextInput({ placeholder: 'Please enter the content.' })
            .showUnderline(true)
            .width(380)
            .height(60)
            .id('AAA')
          TextInput({ placeholder: 'Please enter the content.' })
            .showUnderline(true)
            .width(380)
            .height(60)
            .id('BBB')
        }
        .width('100%')
      }
      .height('100%')
    }
  }
  ```

* 场景二：页面初次构建完成时，使第二个TextInput获取[默认焦点](../harmonyos-guides/arkts-common-events-focus-event.md#默认焦点)。

  设置defaultFocus属性，defaultFocus可以使绑定的组件成为页面创建后首次获焦的焦点。可参考如下代码：

  ```ts
  // xxx.ets
  @Entry
  @Component
  struct TextInputExample {
    build() {
      Row() {
        Column() {
          TextInput({ placeholder: 'Please enter the content.' })
            .showUnderline(true)
            .width(380)
            .height(60)

          TextInput({ placeholder: 'Please enter the content.' })
            .showUnderline(true)
            .defaultFocus(true) // When the page is first opened, this TextInput gets focus
            .width(380)
            .height(60)
        }
        .width('100%')
      }
      .height('100%')
    }
  }
  ```

* 场景三：页面初次构建完成时，使TextInput获取焦点且不弹出键盘。

  设置enableKeyboardOnFocus(false)，在页面进入后不弹出键盘。可参考如下代码：

  ```ts
  // xxx.ets
  @Entry
  @Component
  struct TextInputExample {
    build() {
      Row() {
        Column() {
          TextInput({ placeholder: 'Please enter the content.' })
            .defaultFocus(true) // When the page is first opened, this TextInput gets focus
            .enableKeyboardOnFocus(false) // Is TextInput bound to an input method when focusing through methods other than clicking.
            .placeholderColor(Color.Grey)
            .placeholderFont({ size: 14, weight: 400 })
            .caretColor(Color.Blue)
            .width('95%')
            .height(40)
            .margin(20)
        }
        .width('100%')
      }
      .height('100%')
    }
  }
  ```

* 场景四：页面初次构建完成时，使TextInput不获取焦点且不弹出键盘。

  TextInput默认不获取焦点，不弹出键盘。可参考如下代码：

  ```ts
  // xxx.ets
  @Entry
  @Component
  struct TextInputExample {
    build() {
      Column() {
        TextInput({ placeholder: 'Please enter the content.' })
      }
      .width('100%')
    }
  }
  ```
