---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-248
title: 如何设置Text的字体，可以不受系统设置里显示大小缩放的影响
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何设置Text的字体，可以不受系统设置里显示大小缩放的影响
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:04+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2b27ad3f5c79da353f1cf015a2cef8f1a70726741c18225512cc426c076aa16a
---

目前，px2fp()和px2vp()等方法在修改系统显示大小后不会实时更新。字体的默认单位是 fp，界面像素单位是 px，可以使用像素单位来设置字体大小。参考如下：

```
1. @Entry
2. @Component
3. struct CustomFontSetting {
4. @State message: string = 'hello world';

6. build() {
7. Column() {
8. Text(this.message)
9. .fontSize(53) // Default unit is fp, which changes with system display size.
10. Text(this.message)
11. .fontSize(this.getUIContext().fp2px(160) + 'px') // Use pixel units, unaffected by system display size.
12. Blank()
13. .color(0xff0000)
14. .height(30)
15. .width(226)
16. .margin({ bottom: 20 }) // Default unit vp changes with system display size.
17. Blank()
18. .color(0xff0000)
19. .height(30 + 'px')
20. .width(this.getUIContext().vp2px(672) + 'px') // Use pixel units, unaffected by system display size.
21. }
22. }
23. }
```

[FontSetting.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/FontSetting.ets#L21-L44)
