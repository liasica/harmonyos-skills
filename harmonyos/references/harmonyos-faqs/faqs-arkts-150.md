---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-150
title: 如何在URL编码时处理特殊字符
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何在URL编码时处理特殊字符
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0fffa37af573585f855b89b9e996324e1b8bc4a469e0b14a255a095e6d40afdf
---

由于URL只能包含特定的ASCII字符集（主要是字母、数字和部分保留符号），其他字符（如空格、中文、特殊符号等）必须经过编码才能在URL中正确传输。URL编码规则如下：

* **非保留字符（Unreserved）**

  无需编码，包括：

  1. 字母：A-Z、a-z
  2. 数字：0-9
  3. 符号：-、\_、.、~

* **保留字符（Reserved）**

  有特殊含义，用作数据时需编码。包括 !、\*、'、(、)、;、:、@、&、=、+、$、,、/、?、#、[、]，例如可以使用encodeURIComponent()对‘+’转义为‘%2B’。

  ```ts
  @Entry
  @Component
  export struct HandlingSpecialCharactersForURLEncoding {
    @State message: string = 'encode';

    build() {
      Row() {
        Column() {
          Text(this.message)
            .fontSize(50)
            .fontWeight(FontWeight.Bold)
            .onClick(() => {
              const originalString = '123+456';
              const encoded = encodeURIComponent(originalString);
              console.info(encoded); // output: '123%2B456'.
            })
        }
        .width('100%')
      }
      .height('100%')
    }
  }
  ```

* **非ASCII字符**（如中文、日文、表情符号等）

  先按UTF-8编码为字节序列，再对每个字节进行百分号编码。
