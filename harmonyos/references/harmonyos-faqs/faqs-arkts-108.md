---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-108
title: 如何通过key获取对象值
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何通过key获取对象值
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:940de6eac3ec508b39d5ee79a97ddfd3beb1823d408f109a933b0a2df666810a
---

ArkTS中不支持通过索引访问字段，要使用索引的话可以考虑Record<key, value>，参考代码如下：

```ts
class Student {
  data: Record<string, string> = { 'name': 'aaa', 'age': 'bbb' };
}

@Entry
@Component
struct KeyObject {
  build() {
    Column() {
      Button('click')
        .onClick(() => {
          let student = new Student();
          console.info(`${student.data['name']}`);
        })
    }
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
    .width('100%')
    .height('100%')
  }
}
```
