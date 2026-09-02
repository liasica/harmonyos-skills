---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-106
title: TextInput如何限制输入字符为某些字符
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > TextInput如何限制输入字符为某些字符
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c26f549c4cbefb86e2fe532c58e499fc637d0c8a2ce3635c7d90406cf8a46b7c
---

TextInput的inputFilter属性可设置正则表达式，用于校验输入字符。校验不通过时，输入无效。参考代码如下：

```ts
@Entry
@Component
struct Index {
  controller: TextInputController = new TextInputController();

  build() {
    Column() {
      TextInput({ placeholder: 'Please input a password', text: '123456', controller: this.controller })
        .type(InputType.Password)
        .placeholderColor(Color.Gray)
        .inputFilter('[0-9]', (val) => { //Only allow the input of characters 0-9, other characters are invalid
          console.error('TextInputExample : ' + val);
          // Invalid input return 0
          return 0;
        })
    }
  }
}
```
