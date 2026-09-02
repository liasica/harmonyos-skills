---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-476
title: aboutToReuse使用入参params刷新UI崩溃
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > aboutToReuse使用入参params刷新UI崩溃
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:acd17c986a35f7af393d05e14b134fee67586bd16b11fd063355641e3042f9b2
---

**问题描述**

当一个可复用的自定义组件从复用缓存中重新加入到节点树时，触发aboutToReuse生命周期回调，并将组件的构造参数传递给aboutToReuse。

```ts
// ...
@ObjectLink person: Person
// ... 
aboutToReuse(params: Record<string, Object>): void {
  const originItem = this.person
  const originIndex = this.index
  this.index = params.index as number;

  // this.person = params.person as Person 会崩溃
  console.info(`aboutToReuse index:${this.index} person.name:${this.person.name} 复用前的数据index : ${originIndex} name: ${originItem.name}`);
}
```

在aboutToReuse中使用this.person = params.person as Person 会崩溃

**解决措施**

如果在aboutToReuse中，对@Link、@StorageLink、@ObjectLink、@Consume、@Prop装饰的变量，进行刷新，可能导致未定义的行为。并且可能导致性能劣化。这些变量会由ArkUI框架自动刷新。可参考：[避免对@Link/@ObjectLink/@Prop等自动更新的状态变量，在aboutToReuse()中重复赋值](../harmonyos-guides/arkts-component_reuse.md#避免对linkobjectlinkprop等自动更新的状态变量在abouttoreuse中重复赋值)。
