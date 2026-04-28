---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-246
title: 如何实现背景跟随文字大小改变
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现背景跟随文字大小改变
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:03+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b6a7c93275b4cc3b874e79925fd7feabe7778f3a162eac89e06493e41355fd59
---

可以通过文字长度自动调整宽度。参考代码如下：

```
1. @Entry
2. @Component
3. struct Index {
4. @State message: string = 'Hello World';

6. build() {
7. Column() {
8. Row() {
9. Text(this.message)
10. }
11. .backgroundImage($r('app.media.startIcon'))
12. .backgroundImageSize({
13. width: '100%',
14. height: '100%'
15. })
16. .height(100)
17. .border({
18. width: 3,
19. color: Color.Pink
20. })

22. TextInput()
23. .onChange((value: string) => {
24. this.message = value;
25. })
26. }
27. }
28. }
```

[BackgroundChangesWithTextSize.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/BackgroundChangesWithTextSize.ets#L21-L48)
