---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-471
title: 在子容器的onTouch中调用stopPropagation，为什么无法阻止外层容器的onClick事件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 在子容器的onTouch中调用stopPropagation，为什么无法阻止外层容器的onClick事件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e5426fa44b6ceb05d8242f3c56fafbca4034f59377e2d2760b9e0462aab36356
---

在onTouch事件回调中调用stopPropagation只会影响触摸事件的冒泡传递，无法阻止点击事件的触发。在下面Demo中，子组件调用stopPropagation只会阻止父组件响应onTouch事件，无法阻止onClick事件的触发。

```ts
// xxx.ets
@Entry
@Component
struct TouchExample {
  @State text: string = '';

  build() {
    Column() {
      Button('Touch')
        .height(40)
        .width(100)
        .onTouch((event?: TouchEvent) => {
          console.info("child onTouch");
          event?.stopPropagation();
        })
      // Used to display the event trigger status
      Text(this.text)
    }
    .onTouch((event?: TouchEvent) => {
      // Since the child component called the stopPropagation interface, the onTouch event of the parent component cannot be triggered
      console.info("father onTouch");
    })
    .onClick(() => {
      // The child component called the stopPropagation interface but was unable to prevent the onClick event from being triggered. The parent component's onClick event was triggered as expected
      console.info("father onClick");
    })
    .width('100%')
    .padding(30)
  }
}
```
