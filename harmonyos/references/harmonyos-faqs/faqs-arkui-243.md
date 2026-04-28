---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-243
title: 如何解决点击子组件模块区域会触发父组件的点击事件问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何解决点击子组件模块区域会触发父组件的点击事件问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:02+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:550c3f3f384f6cb7f5b61d842780900186537e17bd41db7efec4d0a07a27f67c
---

**问题现象**

当enabled的值为false时，点击Button按钮会触发父组件的点击事件。

**解决措施**

将Button组件包裹在容器组件中，并设置hitTestBehavior属性为[HitTestMode](../harmonyos-references/ts-appendix-enums.md#hittestmode9).Block，以阻止事件冒泡。具体代码如下：

```
1. @Entry
2. @Component
3. struct TouchExample {
4. @State text: string = 'Parent component'
5. @State parentComponentResponse: string = 'Response times of parent component'
6. @State parentComponentResponseNum: number = 0

8. build() {
9. Column() {
10. Column(){
11. Text(this.text).margin({bottom: 20})
12. Text(this.parentComponentResponse + ':' + `${this.parentComponentResponseNum}`)
13. Row(){
14. //Wrap a container component around the Button component and set the hitTestBehavior property to HitTestMode.Block, which can prevent event bubbling.
15. Button('Disable sub components').height(40).width(100).margin({top: 20})
16. }
17. .hitTestBehavior(HitTestMode.Block)
18. }.onClick((e) => {
19. this.parentComponentResponseNum ++;
20. })
21. .width('80%')
22. .height('30%')
23. .backgroundColor(Color.Gray)
24. }
25. .width('100%')
26. .padding(30)
27. }
28. }
```

[ResolveTriggerParentComponentClickEvent.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ResolveTriggerParentComponentClickEvent.ets#L21-L48)

**参考链接**

[触摸测试控制](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md)
