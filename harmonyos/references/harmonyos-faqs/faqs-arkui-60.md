---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-60
title: Navigation的toolbar中设置大图标时被切断
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation的toolbar中设置大图标时被切断
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5f16cb713cd2cea93082678fcb834f9b3046f63d694417df3932d24ab18a9f6f
---

当图片尺寸超过toolbar高度时，可通过scale属性进行缩放调整。参考代码如下：

```
1. @Entry
2. @Component
3. struct NavigationExample {
4. build() {
5. Column() {
6. Navigation() {
7. }.toolbarConfiguration(this.navigationToolbar)
8. }
9. .height('100%')
10. .width('100%')
11. .backgroundColor(Color.Gray)
12. }

14. @Builder
15. navigationToolbar() {
16. Row() {
17. Column() {
18. Image($r('app.media.icon')).width(24)
19. }.layoutWeight(1)

21. Column() {
22. Image($r('app.media.icon')).width(24).scale({ x: 2, y: 2 })
23. }.layoutWeight(1)

25. Column() {
26. Image($r('app.media.icon')).width(24)
27. }.layoutWeight(1)
28. }
29. .height(34)
30. .width('100%').backgroundColor(Color.White)
31. }
32. }
```

[CutOffWhenSettingLargeIcon.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/CutOffWhenSettingLargeIcon.ets#L21-L52)

**参考链接**

[图形变换](../harmonyos-references/ts-universal-attributes-transformation.md)
