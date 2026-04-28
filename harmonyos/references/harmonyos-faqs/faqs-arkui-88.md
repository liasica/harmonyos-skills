---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-88
title: TextInput在聚焦时如何使光标回到起点
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > TextInput在聚焦时如何使光标回到起点
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:25+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:77c20bd3359f06ec4629c5efc5340f2b2609b9a6c290d41639082a3b88426dfe
---

1. TextInput组件绑定[onEditChange](../harmonyos-references/ts-basic-components-textinput.md#oneditchange8)事件，该事件可以在TextInput输入状态变化时触发。
2. 在事件回调用TextInputController.[caretPosition](../harmonyos-references/ts-basic-components-textinput.md#caretposition10)方法设置光标位置，并需要用到setTimeout延迟方法。

   ```
   1. @Entry
   2. @Component
   3. struct TextInputDemo {
   4. controller: TextInputController = new TextInputController();

   6. build() {
   7. Column() {
   8. TextInput({ controller: this.controller })
   9. .onEditChange((isEditing: boolean) => {
   10. if (isEditing) {
   11. setTimeout(() => {
   12. // The cursor will reset to the beginning of the text after 100ms
   13. this.controller.caretPosition(0);
   14. }, 100)
   15. }
   16. })
   17. }
   18. }
   19. }
   ```

   [ReturnTheCursorToTheStartPoint.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ReturnTheCursorToTheStartPoint.ets#L21-L39)

**参考链接**

[TextInput](../harmonyos-references/ts-basic-components-textinput.md)
