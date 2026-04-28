---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-471
title: 在子容器的onTouch中调用stopPropagation，为什么无法阻止外层容器的onClick事件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 在子容器的onTouch中调用stopPropagation，为什么无法阻止外层容器的onClick事件
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:04+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9f9c1db2850a187cde5b391faaf10d86141d9a90b7de637e99f9dfaad6400213
---

在onTouch事件回调中调用stopPropagation只会影响触摸事件的冒泡传递，无法阻止点击事件的触发。在下面Demo中，子组件调用stopPropagation只会阻止父组件响应onTouch事件，无法阻止onClick事件的触发。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TouchExample {
5. @State text: string = '';

7. build() {
8. Column() {
9. Button('Touch')
10. .height(40)
11. .width(100)
12. .onTouch((event?: TouchEvent) => {
13. console.info("child onTouch");
14. event?.stopPropagation();
15. })
16. // Used to display the event trigger status
17. Text(this.text)
18. }
19. .onTouch((event?: TouchEvent) => {
20. // Since the child component called the stopPropagation interface, the onTouch event of the parent component cannot be triggered
21. console.info("father onTouch");
22. })
23. .onClick(() => {
24. // The child component called the stopPropagation interface but was unable to prevent the onClick event from being triggered. The parent component's onClick event was triggered as expected
25. console.info("father onClick");
26. })
27. .width('100%')
28. .padding(30)
29. }
30. }
```

[TouchExample.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/TouchExample.ets#L21-L51)
