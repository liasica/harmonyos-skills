---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-476
title: aboutToReuse使用入参params刷新UI崩溃
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > aboutToReuse使用入参params刷新UI崩溃
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f753d824ce13bd7916c02508b5991f9c3cb0e8dab9bfad4474618a93888827f7
---

**问题描述**

当一个可复用的自定义组件从复用缓存中重新加入到节点树时，触发aboutToReuse生命周期回调，并将组件的构造参数传递给aboutToReuse。

```
1. // ...
2. @ObjectLink person: Person
3. // ...
4. aboutToReuse(params: Record<string, Object>): void {
5. const originItem = this.person
6. const originIndex = this.index
7. this.index = params.index as number;

9. // this.person = params.person as Person 会崩溃
10. console.info(`aboutToReuse index:${this.index} person.name:${this.person.name} 复用前的数据index : ${originIndex} name: ${originItem.name}`);
11. }
```

在aboutToReuse中使用this.person = params.person as Person 会崩溃

**解决措施**

如果在aboutToReuse中，对@Link、@StorageLink、@ObjectLink、@Consume、@Prop装饰的变量，进行刷新，可能导致未定义的行为。并且可能导致性能劣化。这些变量会由ArkUI框架自动刷新。可参考：[避免对@Link/@ObjectLink/@Prop等自动更新的状态变量，在aboutToReuse()中重复赋值](../best-practices/bpta-component-reuse.md#section7441712174414)。
