---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-331
title: 如何给不同输入框绑定不同的自定义键盘
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何给不同输入框绑定不同的自定义键盘
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d8c35dfeebf8e3349f41ab7fd83243910062a456a1cc915f271415434fd62195
---

1. 为不同的输入框定义相应的控制器。

   ```
   1. private controller: TextInputController = new TextInputController();
   2. private controller1: TextInputController = new TextInputController();
   ```

   [BindDifferentCustomKeyboards2.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/BindDifferentCustomKeyboards2.ets#L26-L27)
2. 定义键盘组件。

   ```
   1. // Customize keyboard components
   2. @Component
   3. export struct CustomKeyboardBuilder {
   4. controller?: TextInputController = new TextInputController();
   5. index: number = 0;
   6. @Link inputValue: string

   8. build() {
   9. Column() {
   10. // ...
   11. }
   12. }
   13. }
   ```

   [BindDifferentCustomKeyboards2.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/BindDifferentCustomKeyboards2.ets#L86-L99)
3. 给TextInput组件添加customKeyboard属性，绑定自定义键盘。

   ```
   1. TextInput({ controller: this.controller, text: this.inputValue })// Bind custom keyboard
   2. .customKeyboard(this.CustomKeyboardBuilder()).margin(10).border({ width: 1 }).height('48vp')
   ```

   [BindDifferentCustomKeyboards2.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/BindDifferentCustomKeyboards2.ets#L56-L57)

   参考以下代码：

   ```
   1. @Entry
   2. @Component
   3. struct TextInputExample {
   4. controller: TextInputController = new TextInputController();
   5. @State inputValue: string = '';
   6. controller1: TextInputController = new TextInputController();
   7. @State inputValue1: string = '';
   8. controller2: TextInputController = new TextInputController();
   9. @State inputValue2: string = '';

   12. build() {
   13. Column() {
   14. this.input({ inputValue: this.inputValue, controller: this.controller, index: 0 });
   15. this.input({ inputValue: this.inputValue1, controller: this.controller1, index: 1 });
   16. this.input({ inputValue: this.inputValue2, controller: this.controller2, index: 2 });
   17. }
   18. }

   21. @Builder
   22. input(tmp: Tmp) {
   23. if (tmp.index === 0) {
   24. TextInput({ controller: tmp.controller, text: tmp.inputValue })
   25. .customKeyboard(this.keyboard())
   26. .margin(10)
   27. .border({ width: 1 })
   28. .height('48vp')
   29. } else if (tmp.index === 1) {
   30. TextInput({ controller: tmp.controller, text: tmp.inputValue })
   31. .customKeyboard(this.keyboard1())
   32. .margin(10)
   33. .border({ width: 1 })
   34. .height('48vp')
   35. } else {
   36. TextInput({ controller: tmp.controller, text: tmp.inputValue })
   37. .customKeyboard(this.keyboard2())
   38. .margin(10)
   39. .border({ width: 1 })
   40. .height('48vp')
   41. }
   42. }

   45. @Builder
   46. keyboard() {
   47. CustomKeyboardBuilder({ inputValue: this.inputValue, controller: this.controller, index: 0 });
   48. }

   51. @Builder
   52. keyboard1() {
   53. CustomKeyboardBuilder({ inputValue: this.inputValue1, controller: this.controller1, index: 1 });
   54. }

   57. @Builder
   58. keyboard2() {
   59. CustomKeyboardBuilder({ inputValue: this.inputValue2, controller: this.controller2, index: 2 });
   60. }
   61. }

   64. class Tmp {
   65. inputValue?: string;
   66. controller?: TextInputController;
   67. index?: number;
   68. }

   71. // Customize keyboard components
   72. @Component
   73. export struct CustomKeyboardBuilder {
   74. controller?: TextInputController = new TextInputController();
   75. index: number = 0;
   76. @Link inputValue: string;

   79. build() {
   80. Column() {
   81. Button('x').onClick(() => {
   82. // Turn off custom keyboard
   83. this.controller?.stopEditing();
   84. })
   85. Grid() {
   86. ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {
   87. GridItem() {
   88. Button(item + '')
   89. .backgroundColor(this.index === 0 ? Color.Blue :
   90. (this.index === 1 ? Color.Green : Color.Red))
   91. .width(110)
   92. .onClick(() => {
   93. this.inputValue += item;
   94. })
   95. }
   96. })
   97. }
   98. .maxCount(3)
   99. .columnsGap(10)
   100. .rowsGap(10)
   101. .padding(5)
   102. }
   103. .backgroundColor(Color.Gray)
   104. }
   105. }
   ```

   [BindDifferentCustomKeyboards.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/BindDifferentCustomKeyboards.ets#L21-L125)
