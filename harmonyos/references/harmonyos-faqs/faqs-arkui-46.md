---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-46
title: Text组件如何加载Unicode字符
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Text组件如何加载Unicode字符
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6c33dc9551ccf77494ed0b34c6ad310cc52833502336c69e2cb463c0bd600543
---

在Text组件的content参数中使用字符串，并在字符串中转义Unicode编码。示例代码如下：

```
1. @Entry
2. @Component
3. struct TextView {
4. build() {
5. Column() {
6. Text("\u{1F468}\u200D\u{1F469}\u200D\u{1F467}\u200D\u{1F466}")
7. .width(100)
8. .height(100)
9. .fontSize(50)
10. }
11. }
12. }
```

[LoadUnicodeCharacters.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/LoadUnicodeCharacters.ets#L36-L47)

字符串转Unicode编码：

```
1. let chineseStr: string = "中文";
2. const encodedStr = Array.from(chineseStr).map(char =>`\\u${char.codePointAt(0)!.toString(16).padStart(4, '0')}`).join("");
```

[LoadUnicodeCharacters.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/LoadUnicodeCharacters.ets#L22-L23)

Unicode编码转字符串：

```
1. let unicodeStr: string = "\\u4e2d\\u6587";
2. const decodedStr = unicodeStr.replace(/\\u([\dA-Fa-f]{4})/g,(_,p1:string) => String.fromCodePoint(parseInt(p1, 16)));
```

[LoadUnicodeCharacters.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/LoadUnicodeCharacters.ets#L29-L30)
