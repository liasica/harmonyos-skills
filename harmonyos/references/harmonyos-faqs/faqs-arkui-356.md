---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-356
title: 如何更改TextInput密码输入模式下passwordIcon的大小、颜色、位置
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何更改TextInput密码输入模式下passwordIcon的大小、颜色、位置
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:31+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:994971c6bf873aac1156871bcde37169612664dbb9bf4651735f9aa93535b9d0
---

使用Stack容器作为父容器，子组件使用Image组件自定义passwordIcon。通过该方式可调整Image组件的位置、大小和颜色。示例代码如下：

```
1. @Entry
2. @Component
3. struct TextInputDemo {
4. @State text: string = '';
5. @State changeType: InputType = InputType.Password;
6. @State isVisible: boolean = false;
7. @State isPasswordVisible: boolean = false;
8. controller: TextInputController = new TextInputController();

10. build() {
11. Stack() {
12. TextInput({ text: this.text, controller: this.controller })
13. .type(this.changeType)
14. .placeholderFont({
15. size: 16,
16. weight: 400
17. })
18. .showPasswordIcon(false)// You need to disable the native password icon (showPasswordIcon(false)) for it to take effect.
19. .width(336)
20. .height(56)
21. .padding({ right: 50 })
22. .onChange((value: string) => {
23. this.text = value;
24. })
25. //Image overlay passwordIcon implementation
26. Image($r(this.isVisible ? 'app.media.startIcon' : 'app.media.invisible'))
27. .margin({ left: 280 })
28. .backgroundColor('#E7E8EA')
29. .width(20)
30. .height(20)
31. .onClick(() => {
32. this.isPasswordVisible = !this.isPasswordVisible;
33. this.isVisible = !this.isVisible;
34. if (this.isPasswordVisible) {
35. this.changeType = InputType.Normal;
36. } else {
37. this.changeType = InputType.Password;
38. }
39. })
40. }
41. .width('100%')
42. .height('100%')
43. .backgroundColor('#F1F3F5')
44. }
45. }
```

[ChangeTextInputInputMode.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ChangeTextInputInputMode.ets#L21-L66)
