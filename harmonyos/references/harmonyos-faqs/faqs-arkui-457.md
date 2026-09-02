---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-457
title: 当一个组件同时绑定了点击事件（onClick）和并行手势（.parallelGesture），为什么当操作为长按时，两个手势都会响应
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 当一个组件同时绑定了点击事件（onClick）和并行手势（.parallelGesture），为什么当操作为长按时，两个手势都会响应
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:96e703a72d4d84d867c8b784ef55fb68e2468332d58dfee7cae48e70e51f9062
---

**问题描述**

由于onClick和.parallelGesture绑定的手势被组合成并行手势组，在长按操作时，系统会同时检测到长按手势和潜在的单击手势（在未达到长按时间阈值前），因此两者都会被触发。

```typescript
@Entry
@Component
struct onClickAndParallelGestureProblematic {
  @State message: string = '多种手势，长按这里';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('TwoGestureHelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          console.info('TapGesture--单击');
        })
        .parallelGesture(
          GestureGroup(GestureMode.Exclusive,
            LongPressGesture({ repeat: false })
              .onAction(() => {
                console.info('LongPressGesture--长按');
              })
          )
        )
    }
    .height('100%')
    .width('100%')
  }
}
```

**解决措施**

如需实现当前组件上绑定两个互斥的点击和长按手势，同时该组件上的手势又需要和子节点的手势同时识别时，可以参考下列代码，将两个互斥的点击和长按手势先绑定到一个互斥手势组内，然后通过.parallelGesture方式将手势组和子节点手势绑定成并行。示例代码如下：

```typescript
@Entry
@Component
struct onClickAndParallelGestureSolution {
  @State message: string = '多种手势，长按这里';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .parallelGesture(
          GestureGroup(GestureMode.Exclusive,
            TapGesture({ count: 1, fingers: 1 })
              .onAction(() => {
                console.info('TapGesture--单击');
              }),
            LongPressGesture({ repeat: false })
              .onAction(() => {
                console.info('LongPressGesture--长按');
              })
          )
        )
    }
    .height('100%')
    .width('100%')
  }
}
```
