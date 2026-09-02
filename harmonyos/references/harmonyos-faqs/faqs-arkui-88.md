---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-88
title: TextInput在聚焦时如何使光标回到起点
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > TextInput在聚焦时如何使光标回到起点
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:506a7f00dae07ae6031aafcb8df7bedf965b4d8a4a74dbb9ad377cb4699bcf61
---

1. TextInput组件绑定[onEditChange](../harmonyos-references/ts-basic-components-textinput.md#oneditchange8)事件，该事件可以在TextInput输入状态变化时触发。
2. 在事件回调用TextInputController.[caretPosition](../harmonyos-references/ts-basic-components-textinput.md#caretposition10)方法设置光标位置，并需要用到setTimeout延迟方法。

   ```ts
   @Entry
   @Component
   struct TextInputDemo {
     controller: TextInputController = new TextInputController();

     build() {
       Column() {
         TextInput({ controller: this.controller })
           .onEditChange((isEditing: boolean) => {
             if (isEditing) {
               setTimeout(() => {
                 // The cursor will reset to the beginning of the text after 100ms
                 this.controller.caretPosition(0);
               }, 100)
             }
           })
       }
     }
   }
   ```

**参考链接**

[TextInput](../harmonyos-references/ts-basic-components-textinput.md)
