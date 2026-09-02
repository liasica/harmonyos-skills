---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-244
title: 当子组件触发触摸事件时，如果父组件也设置了触摸事件，如何解决父组件同时被触发的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 当子组件触发触摸事件时，如果父组件也设置了触摸事件，如何解决父组件同时被触发的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:6a6c0123c965d610bdeea9c6221fddba677bcef41b1920b04c3b98818e61f8ba
---

**问题现象**

当子组件触发触摸事件时，如果父组件也设置了触摸事件，父组件同样会触发。

**解决措施**

在onTouch函数中调用event.stopPropagation()可阻止事件冒泡。参考以下代码：

```typescript
@Entry
@Component
struct TouchExample {
  @State text: string = 'Parent component'
  @State parentComponentResponse: string = 'Response times of parent component'
  @State parentComponentResponseNum: number = 0
  @State childComponentResponse: string = 'Number of sub component responses'
  @State childComponentResponseNum: number = 0

  build() {
    Column() {
      Column(){
        Text(this.text).margin({bottom: 20})
        Text(this.parentComponentResponse + ':' + `${this.parentComponentResponseNum}`)
        Text(this.childComponentResponse + ':' + `${this.childComponentResponseNum}`)

        Button('child').height(40).width(100).margin({top: 20})
          .onTouch((e) => {
            this.childComponentResponseNum ++
            e.stopPropagation()
          })
      }
      .onTouch(() => {
        this.parentComponentResponseNum ++
      })
    }.width('100%').padding(30)
  }
}
```

**参考链接**

[触摸事件](../harmonyos-references/ts-universal-events-touch.md)中的TouchEvent对象说明
