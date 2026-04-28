---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-102
title: 通过$r访问应用资源是否支持嵌套形式
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 通过$r访问应用资源是否支持嵌套形式
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:28+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:14effe1a014ed6824c92954305b68171b746207941ab878ba1a8e4b828abf0ef
---

$r当前不支持嵌套。第二个参数需使用ResourceManager获取应用资源的字符串。参考代码如下：

```
1. @Entry
2. @Component
3. struct Page16 {
4. context = this.getUIContext();

6. build() {
7. Row() {
8. Column() {
9. Text($r('app.string.EntryAbility1_label2',
10. this.context.getHostContext()!.resourceManager.getStringSync($r('app.string.EntryAbility_label'))))// path: resources\base\element\string.json
11. .fontSize(50)
12. .fontWeight(FontWeight.Bold)
13. }
14. .width('100%')
15. }
16. .height('100%')
17. }
18. }
```

[ResourceNesting.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ResourceNesting.ets#L21-L38)

**参考链接**

[ResourceManager](../harmonyos-references/js-apis-resource-manager.md#resourcemanager)
