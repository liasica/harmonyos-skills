---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-331
title: 如何给不同输入框绑定不同的自定义键盘
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何给不同输入框绑定不同的自定义键盘
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:00217db40dd4bc14b02bc368ec42e213fd2c430a6fa331716ab09abf97f7a3ae
---

1. 为不同的输入框定义相应的控制器。

   ```typescript
   private controller: TextInputController = new TextInputController();
   private controller1: TextInputController = new TextInputController();
   ```
2. 定义键盘组件。

   ```ts
   // Customize keyboard components
   @Component
   export struct CustomKeyboardBuilder {
     controller?: TextInputController = new TextInputController();
     index: number = 0;
     @Link inputValue: string

     build() {
       Column() {
         // ...
       }
     }
   }
   ```
3. 给TextInput组件添加customKeyboard属性，绑定自定义键盘。

   ```ts
   TextInput({ controller: this.controller, text: this.inputValue })// Bind custom keyboard
     .customKeyboard(this.CustomKeyboardBuilder()).margin(10).border({ width: 1 }).height('48vp')
   ```

   参考以下代码：

   ```ts
   @Entry
   @Component
   struct TextInputExample {
     controller: TextInputController = new TextInputController();
     @State inputValue: string = '';
     controller1: TextInputController = new TextInputController();
     @State inputValue1: string = '';
     controller2: TextInputController = new TextInputController();
     @State inputValue2: string = '';

     build() {
       Column() {
         this.input({ inputValue: this.inputValue, controller: this.controller, index: 0 });
         this.input({ inputValue: this.inputValue1, controller: this.controller1, index: 1 });
         this.input({ inputValue: this.inputValue2, controller: this.controller2, index: 2 });
       }
     }

     @Builder
     input(tmp: Tmp) {
       if (tmp.index === 0) {
         TextInput({ controller: tmp.controller, text: tmp.inputValue })
           .customKeyboard(this.keyboard())
           .margin(10)
           .border({ width: 1 })
           .height('48vp')
       } else if (tmp.index === 1) {
         TextInput({ controller: tmp.controller, text: tmp.inputValue })
           .customKeyboard(this.keyboard1())
           .margin(10)
           .border({ width: 1 })
           .height('48vp')
       } else {
         TextInput({ controller: tmp.controller, text: tmp.inputValue })
           .customKeyboard(this.keyboard2())
           .margin(10)
           .border({ width: 1 })
           .height('48vp')
       }
     }

     @Builder
     keyboard() {
       CustomKeyboardBuilder({ inputValue: this.inputValue, controller: this.controller, index: 0 });
     }

     @Builder
     keyboard1() {
       CustomKeyboardBuilder({ inputValue: this.inputValue1, controller: this.controller1, index: 1 });
     }

     @Builder
     keyboard2() {
       CustomKeyboardBuilder({ inputValue: this.inputValue2, controller: this.controller2, index: 2 });
     }
   }

   class Tmp {
     inputValue?: string;
     controller?: TextInputController;
     index?: number;
   }

   // Customize keyboard components
   @Component
   export struct CustomKeyboardBuilder {
     controller?: TextInputController = new TextInputController();
     index: number = 0;
     @Link inputValue: string;

     build() {
       Column() {
         Button('x').onClick(() => {
           // Turn off custom keyboard
           this.controller?.stopEditing();
         })
         Grid() {
           ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {
             GridItem() {
               Button(item + '')
                 .backgroundColor(this.index === 0 ? Color.Blue :
                   (this.index === 1 ? Color.Green : Color.Red))
                 .width(110)
                 .onClick(() => {
                   this.inputValue += item;
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
     }
   }
   ```
