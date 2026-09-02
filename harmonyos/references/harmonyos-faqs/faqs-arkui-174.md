---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-174
title: 当父组件绑定了onTouch，其子组件Button绑定了onClick，如何做到点击Button只响应Button的onClick，而不用响应父组件的onTouch
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 当父组件绑定了onTouch，其子组件Button绑定了onClick，如何做到点击Button只响应Button的onClick，而不用响应父组件的onTouch
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:03b0f33072e6e31e226dc000be9dcbe07a76f17cb678370f0d93d992ea5b94c8
---

可以在Button组件中绑定onTouch，并在onTouch中使用stopPropagation()阻止事件冒泡到父组件。参考代码如下：

```screen
@Entry
@Component
struct Index {

  build() {
    Row() {
      Button('Click on me')
        .width(100)
        .backgroundColor('#f00')
        .onClick(() => {
          console.log('Button onClick');
        })
        .onTouch((event) => {
          console.log('Button onTouch');
          event.stopPropagation();
        })
    }
    .onTouch(() => {
      console.log('Row onTouch');
    })
  }
}
```
