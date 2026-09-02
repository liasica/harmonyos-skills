---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-86
title: 如何将Map转换为JSON字符串
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何将Map转换为JSON字符串
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:21555ba6135c262bf3763d6716579bbf9b1167084f795e9bde7fb99cdadd6a9a
---

将Map转换为Record后，再通过JSON.stringify()方法转换为JSON字符串。示例如下：

```ts
let mapSource = new Map<string, string>();
mapSource.set('name', 'name1');
mapSource.set('width', '100');
mapSource.set('height', '50');

let jsonObject: Record<string, Object> = {};
mapSource.forEach((value, key) => {
  if (key !== undefined && value !== undefined) {
    jsonObject[key] = value;
  }
})
let jsonInfo: string = JSON.stringify(jsonObject);

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('Map to JSON')
        .onClick(() => {
          console.log('jsonInfo:', jsonInfo); // jsonInfo: {"name":"name1","width":"100","height":"50"}
        })
    }
  }
}
```
