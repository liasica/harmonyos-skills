---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-243
title: 如何解决点击子组件模块区域会触发父组件的点击事件问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决点击子组件模块区域会触发父组件的点击事件问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:941f93982400e70f95f904a95e69ecfe919f664266b34bf494682053e7205ba4
---

**问题现象**

当enabled的值为false时，点击Button按钮会触发父组件的点击事件。

**解决措施**

将Button组件包裹在容器组件中，并设置hitTestBehavior属性为[HitTestMode](../harmonyos-references/ts-appendix-enums.md#hittestmode9).Block，以阻止事件冒泡。具体代码如下：

```ts
@Entry
@Component
struct TouchExample {
  @State text: string = 'Parent component'
  @State parentComponentResponse: string = 'Response times of parent component'
  @State parentComponentResponseNum: number = 0

  build() {
    Column() {
      Column(){
        Text(this.text).margin({bottom: 20})
        Text(this.parentComponentResponse + ':' + `${this.parentComponentResponseNum}`)
        Row(){
          //Wrap a container component around the Button component and set the hitTestBehavior property to HitTestMode.Block, which can prevent event bubbling.
          Button('Disable sub components').height(40).width(100).margin({top: 20})
        }
        .hitTestBehavior(HitTestMode.Block)
      }.onClick((e) => {
        this.parentComponentResponseNum ++;
      })
      .width('80%')
      .height('30%')
      .backgroundColor(Color.Gray)
    }
    .width('100%')
    .padding(30)
  }
}
```

**参考链接**

[触摸测试控制](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md)
