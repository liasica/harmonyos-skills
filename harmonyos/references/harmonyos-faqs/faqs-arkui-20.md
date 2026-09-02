---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-20
title: 如何主动清除控件的焦点
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何主动清除控件的焦点
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:39b8dbb22f86c090aa9905b9329e4c8dc005ee41a15fc450990868d5b08bfc21
---

当组件处于获焦状态时，将其focusable属性或enabled属性设置为false，会自动使该组件失焦。焦点将按照[走焦规则](../harmonyos-guides/arkts-common-events-focus-event.md#走焦规范)转移给其他组件。参考代码如下：

```ts
@Entry
@Component
struct ClearComponentFocus {
  // Whether textInput is focus
  @State textFocusable: boolean = true;
  @State text: string = 'Gain focus';

  build() {
    Column() {
      TextInput({ text: this.text })
        .focusable(this.textFocusable)
        .onFocus(() => {
          this.text = 'Gain focus';
        })
        .onBlur(() => {
          this.text = 'Lost Focus';
        })
      Button('Button1')
        .width(160)
        .height(70)
        .margin({ top: 20 })
        .onClick(() => {
          this.textFocusable = !this.textFocusable;
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

**参考链接**

[设置组件是否获焦](../harmonyos-guides/arkts-common-events-focus-event.md#设置组件是否可获焦)
