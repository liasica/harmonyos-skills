---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-483
title: 设置了动态的visibility属性，切换组件的显示隐藏，使用requestFocus让组件获取焦点报错150003：the component is not on tree or does not exist.
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 设置了动态的visibility属性，切换组件的显示隐藏，使用requestFocus让组件获取焦点报错150003：the component is not on tree or does not exist.
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0cce7f192e9996388051c3a7a7d954584901eacc36d5d8b69b90b6b4f42a722b
---

根据焦点错误码[150003 节点不存在](../harmonyos-references/errorcode-focus.md#section150003-节点不存在)表明传入的id指向不存在、未挂树或者不可见节点。requestFocus前需要确保节点已经可见。

如以下代码的实现，在切换可见性时，并不能保证获取焦点时组件已经可见：

```
1. @Entry
2. struct Index {
3. @State isEdit: boolean = true;

5. build() {
6. Column() {
7. TextInput().id('input')
8. .visibility(this.isEdit ? Visibility.Visible : Visibility.None)
9. Button('change visibility')
10. .onClick(() => {
11. this.isEdit = !this.isEdit;
12. if (this.isEdit) {
13. try {
14. this.getUIContext().getFocusController().requestFocus('input');
15. } catch (e) {
16. console.error("requestFocus error: " + e);
17. }
18. }
19. })
20. }
21. }
22. }
```

推荐在[onVisibleAreaChange](../harmonyos-references/ts-universal-component-visible-area-change-event.md#onvisibleareachange)回调中进行焦点获取，参考示例代码如下：

```
1. @Entry
2. @Component
3. struct GetFocusByOnVisibleAreaChange {
4. @State isEdit: boolean = true;

6. build() {
7. Column() {
8. TextInput().id('input')
9. .visibility(this.isEdit ? Visibility.Visible : Visibility.None)
10. .onVisibleAreaChange([1.0], () => {
11. if (this.isEdit) {
12. try {
13. this.getUIContext().getFocusController().requestFocus('input');
14. } catch (e) {
15. console.error('requestFocus error:' + e);
16. }
17. }
18. })
19. Button('change visibility')
20. .onClick(() => {
21. this.isEdit = !this.isEdit;
22. })
23. }
24. }
25. }
```

[GetFocusByOnVisibleAreaChange.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetFocusByOnVisibleAreaChange.ets#L21-L46)
