---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-14
title: RichEditor组件如何设置光标的起始位置位于左上角
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > RichEditor组件如何设置光标的起始位置位于左上角
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:02+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:66b71faf1cccdb0a3624397688422104a9a94469807c24034be5dcbb84a0f252
---

可以通过align属性传入参数Alignment.TopStart，来设置光标位置位于左上角。示例代码如下：

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RichEditorExample {
5. controller: RichEditorController = new RichEditorController();

7. build() {
8. Column() {
9. RichEditor({ controller: this.controller })
10. .align(Alignment.TopStart) // Set the starting position of the cursor to the upper left corner
11. .height(200)
12. .borderWidth(1)
13. .borderColor(Color.Red)
14. .width('100%')
15. }
16. }
17. }
```

[SetStartingPositionOfTheCursor.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/SetStartingPositionOfTheCursor.ets#L21-L37)
