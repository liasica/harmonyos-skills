---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-229
title: 使用BuilderParam在父组件调用this的方法报错：Error message: undefined is not callable
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 使用BuilderParam在父组件调用this的方法报错：Error message: undefined is not callable
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:59+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:7f7eb2f66a5256a441cf5322fb3c413164b0ef264742f1dfcc2b88f1d0e12649
---

**问题场景**

在子组件Child中使用@BuilderParam参数时，如果在父组件中将父组件的builder函数传递给子组件，并在builder函数中调用父组件的方法，可能会出现Error message: undefined is not callable的错误。

问题代码如下：

```
1. @Component
2. struct Child {
3. @Builder
4. FunABuilder0() {};

6. @BuilderParam aBuilder0: () => void = this.FunABuilder0;

8. build() {
9. Column() {
10. this.aBuilder0()
11. }
12. }
13. }

15. @Entry
16. @Component
17. struct Parent {
18. @Builder
19. componentBuilder() {
20. Text('Parent builder')
21. .onClick(() => {
22. this.test1();
23. })
24. }

26. test1(): void {
27. console.info('test1');
28. }

30. build() {
31. Column() {
32. Child({ aBuilder0: this.componentBuilder })
33. }
34. }
35. }
```

[ResolvingIsNotCallable.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ResolvingIsNotCallable.ets#L21-L56)

**解决方案**

在JavaScript中调用this时，需要注意this的指向。当前代码在子组件中声明builder方法时，this指向的是父组件。而@Builder componentBuilder()通过this.componentBuilder的形式传给子组件@BuilderParam customBuilderParam，此时this指向的是子组件Child的label，即 “Child”。因此，在点击事件响应时，this指向的是Child，而Child中没有test1()方法，从而导致 JavaScript 错误。

为了解决这个问题，需要在父组件中声明子组件时，通过监听函数将 `this` 传递到子组件。应改为：

```
1. Child({
2. aBuilder0: () => {
3. this.componentBuilder()
4. }
5. })
```

[ResolvingIsNotCallable.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ResolvingIsNotCallable.ets#L71-L75)

**参考链接**

[@BuilderParam装饰器：引用@Builder函数](../harmonyos-guides/arkts-builderparam.md)
