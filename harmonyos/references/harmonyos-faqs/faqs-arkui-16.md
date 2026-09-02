---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-16
title: 如何实现软键盘弹出后，整体布局不变
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现软键盘弹出后，整体布局不变
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1a82d2e2ac6707b55badd87337f3f23b9c78e04a9116d256b87daa3d2f9e829a
---

通过[expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)属性把组件扩展其安全区域，使页面整体布局保持不变，当type为SafeAreaType.KEYBOARD时默认生效，组件不避让键盘。可参考如下代码：

```ts
// xxx.ets
@Entry
@Component
struct TextInputExample {
  scroller: Scroller = new Scroller();
  @State text: string = '';

  build() {
    Scroll(this.scroller) {
      Column({ space: 20 }) {
        TextInput({ placeholder: 'Please enter the content.' })
          .expandSafeArea([SafeAreaType.KEYBOARD])
          .type(InputType.Password)
          .margin({ top: 200 })
        TextInput({ placeholder: 'Please enter the content.' })
          .expandSafeArea([SafeAreaType.KEYBOARD])
          .margin({ top: 200 })
        Text(`UserName：${this.text}`)
          .expandSafeArea([SafeAreaType.KEYBOARD])
          .width('80%')
          .margin({ top: 200 })
        TextInput({ placeholder: 'Please enter a user name.', text: this.text })
          .expandSafeArea([SafeAreaType.KEYBOARD])
          .margin({ top: 200 })
          .onChange((value: string) => {
            this.text = value;
          })
      }
      .width('100%')
    }
    .scrollBar(BarState.Off)
  }
}
```
