---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-384
title: 如何解决组件消失动画偏移闪烁
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何解决组件消失动画偏移闪烁
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ee9c90e1fab0ec3a2267af43e1a7b25c38730eabf793f76c710bcac4fb4e7282
---

**问题描述**

运行下面demo，点击使色块消失时，会突然出现在左上角闪烁。

```
1. @Entry
2. @ComponentV2
3. struct Index {
4. @Local isShow: boolean = true;

6. build() {
7. Stack() {
8. Stack() {
9. if (this.isShow) {
10. Row()
11. .width(100)
12. .height(100)
13. .backgroundColor(Color.Red)
14. .transition(TransitionEffect.OPACITY.animation({ duration: 150 }));
15. }
16. }
17. .backgroundColor(Color.Green)
18. }
19. .width('100%')
20. .height('100%')
21. .onClick(() => {
22. this.isShow = !this.isShow;
23. });
24. }
25. }
```

**解决措施**

原因是当变量置为false时，组件会从视图树中移除，导致内层Stack失去内容后位置重置到左上角，可以固定内层Stack组件的宽高来避免，示例如下：

```
1. @Entry
2. @ComponentV2
3. struct DisappearanceAnimationOffsetFlicker {
4. @Local isShow: boolean = true;

6. build() {
7. Stack() {
8. Stack() {
9. if (this.isShow) {
10. Row()
11. .width(100)
12. .height(100)
13. .backgroundColor(Color.Red)
14. .transition(TransitionEffect.OPACITY.animation({ duration: 150 }))
15. }
16. }
17. .width('100%')
18. .height('100%')
19. .onClick(() => {
20. this.isShow = !this.isShow
21. })
22. }
23. }
24. }
```

[DisappearanceAnimationOffsetFlicker.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/DisappearanceAnimationOffsetFlicker.ets#L21-L45)
