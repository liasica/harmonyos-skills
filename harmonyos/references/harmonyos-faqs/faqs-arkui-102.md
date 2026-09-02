---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-102
title: 通过$r访问应用资源是否支持嵌套形式
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 通过$r访问应用资源是否支持嵌套形式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6ef0aa2f2b5e1fc62595659db2c0d8f44b7d2291d5a41112b296b6e138da80fe
---

$r当前不支持嵌套。第二个参数需使用ResourceManager获取应用资源的字符串。参考代码如下：

```ts
@Entry
@Component
struct Page16 {
  context = this.getUIContext();

  build() {
    Row() {
      Column() {
        Text($r('app.string.EntryAbility1_label2',
          this.context.getHostContext()!.resourceManager.getStringSync($r('app.string.EntryAbility_label'))))// path: resources\base\element\string.json
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

**参考链接**

[ResourceManager](../harmonyos-references/js-apis-resource-manager.md#resourcemanager)
