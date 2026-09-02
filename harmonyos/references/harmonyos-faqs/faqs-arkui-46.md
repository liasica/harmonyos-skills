---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-46
title: Text组件如何加载Unicode字符
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Text组件如何加载Unicode字符
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:7440cde1244b5aad0126c8788dca65e2f7c03d096d5bdf06d46c39ef5b567acd
---

在Text组件的content参数中使用字符串，并在字符串中转义Unicode编码。示例代码如下：

```typescript
@Entry
@Component
struct TextView {
  build() {
    Column() {
      Text("\u{1F468}\u200D\u{1F469}\u200D\u{1F467}\u200D\u{1F466}")
        .width(100)
        .height(100)
        .fontSize(50)
    }
  }
}
```

字符串转Unicode编码：

```typescript
let chineseStr: string = "中文";
const encodedStr = Array.from(chineseStr).map(char =>`\\u${char.codePointAt(0)!.toString(16).padStart(4, '0')}`).join("");
```

Unicode编码转字符串：

```typescript
let unicodeStr: string = "\\u4e2d\\u6587";
const decodedStr = unicodeStr.replace(/\\u([\dA-Fa-f]{4})/g,(_,p1:string) => String.fromCodePoint(parseInt(p1, 16)));
```
