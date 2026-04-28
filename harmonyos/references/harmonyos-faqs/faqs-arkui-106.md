---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-106
title: TextInput如何限制输入字符为某些字符
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > TextInput如何限制输入字符为某些字符
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f147cc5ad2f0e8c5732333af77c04f5c303f353abdbe8c53ce22e6692363d510
---

TextInput的inputFilter属性可设置正则表达式，用于校验输入字符。校验不通过时，输入无效。参考代码如下：

```
1. @Entry
2. @Component
3. struct Index {
4. controller: TextInputController = new TextInputController();

6. build() {
7. Column() {
8. TextInput({ placeholder: 'Please input a password', text: '123456', controller: this.controller })
9. .type(InputType.Password)
10. .placeholderColor(Color.Gray)
11. .inputFilter('[0-9]', (val) => { //Only allow the input of characters 0-9, other characters are invalid
12. console.error('TextInputExample : ' + val);
13. // Invalid input return 0
14. return 0;
15. })
16. }
17. }
18. }
```

[LimitInputCharacters.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/LimitInputCharacters.ets#L21-L38)
