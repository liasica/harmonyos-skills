---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-174
title: 当父组件绑定了onTouch，其子组件Button绑定了onClick，如何做到点击Button只响应Button的onClick，而不用响应父组件的onTouch
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 当父组件绑定了onTouch，其子组件Button绑定了onClick，如何做到点击Button只响应Button的onClick，而不用响应父组件的onTouch
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:45+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b705c9850bc0c7d1e85ee308310e456b69dfdbb6685824eaf59fea0bcf093101
---

可以在Button组件中绑定onTouch，并在onTouch中使用stopPropagation()阻止事件冒泡到父组件。参考代码如下：

```
1. @Entry
2. @Component
3. struct Index {

5. build() {
6. Row() {
7. Button('Click on me')
8. .width(100)
9. .backgroundColor('#f00')
10. .onClick(() => {
11. console.log('Button onClick');
12. })
13. .onTouch((event) => {
14. console.log('Button onTouch');
15. event.stopPropagation();
16. })
17. }
18. .onTouch(() => {
19. console.log('Row onTouch');
20. })
21. }
22. }
```

[NotRespondToParentComponentOnTouch.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/NotRespondToParentComponentOnTouch.ets#L21-L42)
