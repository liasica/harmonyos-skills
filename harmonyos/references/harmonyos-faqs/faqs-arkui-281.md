---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-281
title: 自定义键盘和系统键盘如何切换
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 自定义键盘和系统键盘如何切换
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:14+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:90ba93d55fc12ba918c3eeda24f3f7c67bc2a626d7ad1ae5557617afc255b651
---

声明状态变量，动态控制customKeyboard属性的值，实现自定义键盘与系统键盘的切换。示例代码如下：

```
1. @Component
2. export struct CustomSystemKeyboardToggle {
3. controller: TextInputController = new TextInputController();
4. @State inputValue: string = '';
5. @State show: boolean = false;

7. // Customize keyboard components
8. @Builder
9. customKeyboardBuilder() {
10. Column() {
11. Button('x')
12. .onClick(() => {
13. // Turn off custom keyboard
14. this.controller.stopEditing();
15. this.show = !this.show;
16. })
17. Grid() {
18. ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {
19. GridItem() {
20. Button(item + '')
21. .width(110)
22. .onClick(() => {
23. this.inputValue += item;
24. })
25. }
26. })
27. }
28. .maxCount(3)
29. .columnsGap(10)
30. .rowsGap(10)
31. .padding(5)
32. }
33. .backgroundColor(Color.Gray)
34. }

36. build() {
37. Column() {
38. TextInput({ controller: this.controller, text: this.inputValue })// Bind custom keyboard
39. .customKeyboard(this.show ? this.customKeyboardBuilder() : undefined)
40. .margin(10)
41. .height(48)
42. Button('switch')
43. .onClick(() => {
44. this.show = !this.show;
45. })
46. }
47. }
48. }
```

[SwitchingBetweenCustomAndSystemKeyboard.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/SwitchingBetweenCustomAndSystemKeyboard.ets#L21-L68)
