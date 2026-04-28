---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-263
title: Navigation容器中，如何设置子组件的高度为100%，撑满父容器
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation容器中，如何设置子组件的高度为100%，撑满父容器
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a0179eac0ea457b89602561fbade69b79c969ed89100d0d6f69d456a5e341f88
---

参考代码如下：

```
1. import { window } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;
5. const TAG = 'FullNavigationSubComponent';

7. @Entry
8. @Component
9. struct FullNavigationSubComponent {
10. context = this.getUIContext();

12. onPageShow(): void {
13. window.getLastWindow(this.context.getHostContext(), (err, win) => {
14. if (err != null) {
15. hilog.error(DOMAIN, TAG, `getLastWindow failed  code:${err.code};message:${err.message}`);
16. } else {
17. win.setWindowLayoutFullScreen(true);
18. }
19. })
20. }

22. build() {
23. Navigation() {
24. Column() {
25. }
26. .width('100%')
27. .height('100%')
28. .backgroundColor(Color.Black)
29. }
30. .width('100%')
31. .height('100%')
32. .title('Personalization Settings')
33. .titleMode(NavigationTitleMode.Mini)
34. .backgroundColor(Color.Grey)
35. }
36. }
```

[FullNavigationSubcomponent.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/FullNavigationSubcomponent.ets#L21-L56)
