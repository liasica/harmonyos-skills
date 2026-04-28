---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-150
title: 如何在URL编码时处理特殊字符
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何在URL编码时处理特殊字符
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:19+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:e0f0cc1267255d9af6474eebf7ce17338a81056e484a0c390f1b983d61fbdc0c
---

由于URL只能包含特定的ASCII字符集（主要是字母、数字和部分保留符号），其他字符（如空格、中文、特殊符号等）必须经过编码才能在URL中正确传输。URL编码规则如下：

* **非保留字符（Unreserved）**

  无需编码，包括：

  1. 字母：A-Z、a-z
  2. 数字：0-9
  3. 符号：-、\_、.、~

* **保留字符（Reserved）**

  有特殊含义，用作数据时需编码。包括 !、\*、'、(、)、;、:、@、&、=、+、$、,、/、?、#、[、]，例如可以使用encodeURIComponent()对‘+’转义为‘%2B’。

  ```
  1. @Entry
  2. @Component
  3. export struct HandlingSpecialCharactersForURLEncoding {
  4. @State message: string = 'encode';

  6. build() {
  7. Row() {
  8. Column() {
  9. Text(this.message)
  10. .fontSize(50)
  11. .fontWeight(FontWeight.Bold)
  12. .onClick(() => {
  13. const originalString = '123+456';
  14. const encoded = encodeURIComponent(originalString);
  15. console.info(encoded); // output: '123%2B456'.
  16. })
  17. }
  18. .width('100%')
  19. }
  20. .height('100%')
  21. }
  22. }
  ```

  [HandlingSpecialCharactersForURLEncoding.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/HandlingSpecialCharactersForURLEncoding.ets#L21-L43)

* **非ASCII字符**（如中文、日文、表情符号等）

  先按UTF-8编码为字节序列，再对每个字节进行百分号编码。
