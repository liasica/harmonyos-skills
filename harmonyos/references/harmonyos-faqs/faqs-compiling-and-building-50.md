---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-50
title: 如何解决自定义组件struct内不支持定义成员变量get/set方法的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决自定义组件struct内不支持定义成员变量get/set方法的问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b82f315d8877194fdf1e3589809075fd8858ddf54c58de20ab5162d7572a9a9d
---

**问题现象**

运行DevEco Studio的build编译构建功能后，产物中不会生成get/set方法的代码逻辑。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/FL9_BnmTTJa8soA9nN_DwQ/zh-cn_image_0000002229758625.png?HW-CC-KV=V1&HW-CC-Date=20260428T002916Z&HW-CC-Expire=86400&HW-CC-Sign=B9582CF1332C4DD4D9CB2952F75E19C1FCA97BCB98C900567E150B726E8AAD14)

错误示例如下：

```
1. @Entry
2. @Component
3. struct GetSetDemo {
4. private get value(): string {
5. return "Hello";
6. }
7. private set value(value: string) {
8. this.value = value;
9. }

11. build() {
12. Row() {
13. Column() {
14. Text("Hello World")
15. .fontSize(50)
16. .fontWeight(FontWeight.Bold)
17. }
18. }
19. }
20. }
```

**解决措施**

1.可以使用以下方法替代get方法：

private value: string = "Hello";

2.可以使用以下方式替代 set方法：

this.value = "World"；
