---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-103
title: Button组件如何设置渐变背景色
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Button组件如何设置渐变背景色
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:28+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:79c35c97099ccaec0919ef8f8d59ae0ed9629b664d13b15f165ed8e4d9c8c42e
---

将Button的默认背景色设置为全透明，以确保渐变颜色正常显示。参考代码如下：

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Button('test')
6. .width(200)
7. .height(50)
8. .backgroundColor('#00000000')
9. .linearGradient({
10. angle: 90,
11. colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 1.0]]
12. })
13. }
14. }
```

[ButtonSetGradientBackgroundColor.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ButtonSetGradientBackgroundColor.ets#L21-L34)

**参考链接**

[Button](../harmonyos-references/ts-basic-components-button.md)
