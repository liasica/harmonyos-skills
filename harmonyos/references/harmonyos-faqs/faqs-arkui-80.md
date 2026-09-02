---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-80
title: 如何一键清空TextInput、TextArea组件内容
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何一键清空TextInput、TextArea组件内容
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:d328c41cdfa389bc44ac04c4f7f1a4d65e7e49b311045860cf5e7ea33b06622d
---

通过将状态变量绑定到TextInput或TextArea的text属性，点击清空按钮时更新状态变量为空字符串即可实现内容清除。参考代码如下：

```typescript
@Entry
@Component
struct Index {
  @State text: string = 'Hello World';
  controller: TextInputController = new TextInputController();

  build() {
    Row() {
      Column() {
        TextInput({ placeholder: 'Please input your words.', text: this.text,
          controller:this.controller}).onChange((value) => {
          this.text = value;
        })
        Button('Clear TextInput').onClick(() => {
          this.text = '';
        })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
