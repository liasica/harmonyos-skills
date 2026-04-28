---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-80
title: 如何一键清空TextInput、TextArea组件内容
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何一键清空TextInput、TextArea组件内容
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1df8d820fdbe0a55ba3444fd17253f3acdcc6a7751ccdcf084b8d53d99b19c24
---

通过将状态变量绑定到TextInput或TextArea的text属性，点击清空按钮时更新状态变量为空字符串即可实现内容清除。参考代码如下：

```
1. @Entry
2. @Component
3. struct Index {
4. @State text: string = 'Hello World';
5. controller: TextInputController = new TextInputController();

7. build() {
8. Row() {
9. Column() {
10. TextInput({ placeholder: 'Please input your words.', text: this.text,
11. controller:this.controller}).onChange((value) => {
12. this.text = value;
13. })
14. Button('Clear TextInput').onClick(() => {
15. this.text = '';
16. })
17. }
18. .width('100%')
19. }
20. .height('100%')
21. }
22. }
```

[OneClickClearOfComponentContent.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/OneClickClearOfComponentContent.ets#L21-L42)
