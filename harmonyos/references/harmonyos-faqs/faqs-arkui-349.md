---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-349
title: 如何修改bindPopup绑定的弹窗圆角大小和箭头颜色
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何修改bindPopup绑定的弹窗圆角大小和箭头颜色
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4ab324a1eba75a6947a49f0190480a8514c2efcde18b3da25be0bbc4b67541c8
---

通过radius参数调整圆角大小，但箭头颜色需通过popupColor间接设置。示例代码如下：

```
1. @Entry
2. @Component
3. struct BindPopupDemo {
4. @State handlePopup: boolean = false;
5. @State customPopup: boolean = false;

8. // Popup constructor defines the content of the popup box
9. @Builder
10. popupBuilder() {
11. Row({ space: 2 }) {
12. Image($r('app.media.startIcon'))
13. .width(24)
14. .height(24)
15. .margin({ left: -5 })
16. Text('Custom Popup')
17. .fontSize(10)
18. }
19. .width(100)
20. .height(50)
21. .padding(5)
22. }

25. build() {
26. RelativeContainer() {
27. Button('CustomPopupOptions')
28. .onClick(() => {
29. this.customPopup = !this.customPopup;
30. })
31. .bindPopup(this.customPopup, {
32. builder: this.popupBuilder,
33. radius: 30,
34. popupColor: Color.Yellow,
35. enableArrow: true,
36. onStateChange: (e) => {
37. if (!e.isVisible) {
38. this.customPopup = false;
39. }
40. }
41. })
42. }
43. }
44. }
```

[ModifyTheCornerSizeAndArrowColorOfBindPopup.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ModifyTheCornerSizeAndArrowColorOfBindPopup.ets#L21-L64)
