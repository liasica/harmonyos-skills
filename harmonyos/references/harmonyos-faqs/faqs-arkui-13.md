---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-13
title: TextInput组件获取焦点的几种场景
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > TextInput组件获取焦点的几种场景
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:01+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:777dbc61c30717fe45798fa25bfe2aa62d99246fe22583a2c5c05b6c175c6170
---

* 场景一：TextInput[主动获焦/失焦](../harmonyos-guides/arkts-common-events-focus-event.md#主动获焦失焦)。

  调用focusControl.requestFocus接口可以主动让焦点转移至参数指定的组件上。可参考如下代码：

  ```
  1. // xxx.ets
  2. @Entry
  3. @Component
  4. struct TextInputExample {
  5. build() {
  6. Row() {
  7. Column() {
  8. Button('The second focus acquisition')
  9. .onClick(() => {
  10. focusControl.requestFocus('BBB'); // Get focus on the second input box
  11. })

  14. TextInput({ placeholder: 'Please enter the content.' })
  15. .showUnderline(true)
  16. .width(380)
  17. .height(60)
  18. .id('AAA')
  19. TextInput({ placeholder: 'Please enter the content.' })
  20. .showUnderline(true)
  21. .width(380)
  22. .height(60)
  23. .id('BBB')
  24. }
  25. .width('100%')
  26. }
  27. .height('100%')
  28. }
  29. }
  ```

  [GetTheFocusScene\_One.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetTheFocusScene_One.ets#L21-L49)
* 场景二：页面初次构建完成时，使第二个TextInput获取[默认焦点](../harmonyos-guides/arkts-common-events-focus-event.md#默认焦点)。

  设置defaultFocus属性，defaultFocus可以使绑定的组件成为页面创建后首次获焦的焦点。可参考如下代码：

  ```
  1. // xxx.ets
  2. @Entry
  3. @Component
  4. struct TextInputExample {
  5. build() {
  6. Row() {
  7. Column() {
  8. TextInput({ placeholder: 'Please enter the content.' })
  9. .showUnderline(true)
  10. .width(380)
  11. .height(60)

  14. TextInput({ placeholder: 'Please enter the content.' })
  15. .showUnderline(true)
  16. .defaultFocus(true) // When the page is first opened, this TextInput gets focus
  17. .width(380)
  18. .height(60)
  19. }
  20. .width('100%')
  21. }
  22. .height('100%')
  23. }
  24. }
  ```

  [GetTheFocusScene\_Two.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetTheFocusScene_Two.ets#L21-L44)
* 场景三：页面初次构建完成时，使TextInput获取焦点且不弹出键盘。

  设置enableKeyboardOnFocus(false)，在页面进入后不弹出键盘。可参考如下代码：

  ```
  1. // xxx.ets
  2. @Entry
  3. @Component
  4. struct TextInputExample {
  5. build() {
  6. Row() {
  7. Column() {
  8. TextInput({ placeholder: 'Please enter the content.' })
  9. .defaultFocus(true) // When the page is first opened, this TextInput gets focus
  10. .enableKeyboardOnFocus(false) // Is TextInput bound to an input method when focusing through methods other than clicking.
  11. .placeholderColor(Color.Grey)
  12. .placeholderFont({ size: 14, weight: 400 })
  13. .caretColor(Color.Blue)
  14. .width('95%')
  15. .height(40)
  16. .margin(20)
  17. }
  18. .width('100%')
  19. }
  20. .height('100%')
  21. }
  22. }
  ```

  [GetTheFocusScene\_Three.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetTheFocusScene_Three.ets#L21-L42)
* 场景四：页面初次构建完成时，使TextInput不获取焦点且不弹出键盘。

  TextInput默认不获取焦点，不弹出键盘。可参考如下代码：

  ```
  1. // xxx.ets
  2. @Entry
  3. @Component
  4. struct TextInputExample {
  5. build() {
  6. Column() {
  7. TextInput({ placeholder: 'Please enter the content.' })
  8. }
  9. .width('100%')
  10. }
  11. }
  ```

  [GetTheFocusScene\_Four.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetTheFocusScene_Four.ets#L21-L31)
