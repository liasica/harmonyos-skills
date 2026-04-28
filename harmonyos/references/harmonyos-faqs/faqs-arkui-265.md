---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-265
title: 如何实现点击输入框时会拉起软键盘，点击Button时软键盘关闭
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现点击输入框时会拉起软键盘，点击Button时软键盘关闭
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0115542989e0359e0b40bd19da4c11270497852e6265a540b979e763da43b4e1
---

可以通过调用输入法服务 @kit.IMEKit 的 stopInputSession()方法来隐藏软键盘。示例代码如下：

```
1. import { inputMethod } from '@kit.IMEKit';

3. @Entry
4. @Component
5. struct ClickBlankHideKeyboard {
6. build() {
7. Column({ space: 12 }) {
8. TextInput({ placeholder: 'Please enter your account' })
9. .height(40)
10. TextInput({ placeholder: 'Please input a password' })
11. .height(40)
12. Button('log on').width('100%')
13. .onClick(() => {
14. // Exit text editing mode
15. try {
16. this.inputRef.blur();
17. // Close the current input session and hide the soft keyboard.
18. inputMethod.getController().stopInputSession();
19. } catch (err) {
20. console.error('Failed to hide keyboard: ' + err);
21. }
22. })
23. }
24. }
25. }
```

[ClickButtonSoftwareKeyboardToClose.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ClickButtonSoftwareKeyboardToClose.ets#L21-L45)

参考链接：

[@ohos.inputMethod (输入法框架)](../harmonyos-references/js-apis-inputmethod.md)
