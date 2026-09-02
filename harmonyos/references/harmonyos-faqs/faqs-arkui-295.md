---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-295
title: Scroll中嵌套List，可否设置事件响应顺序，让List不响应滚动事件，让外层的Scroll滚动整个布局
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Scroll中嵌套List，可否设置事件响应顺序，让List不响应滚动事件，让外层的Scroll滚动整个布局
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1e8086e63b684b1e7e789e2553416adda39a74a8d16411dc00c4e44f5b473210
---

Scroll嵌套List的时候，如果List默认不设置高度是会默认全部展开的，可以实现Scroll滚动整个布局的效果，但是要注意这样会失去懒加载效果，推荐使用List组件的nestedScroll属性来实现嵌套滚动效果。

示例代码如下：

```ts
@Component
export struct ScrollNestingList {
  build() {
    Scroll() {
      Column() {
        Text('This is the title')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
        List() {
          ForEach(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], (item: string) => {
            ListItem() {
              Text(item)
                .fontSize(50)
                .height(150)
            }
          }, (item: string) => item)
        }
        .nestedScroll({
          scrollForward: NestedScrollMode.PARENT_FIRST, // Triggering the parent scroll first when scrolling down
          scrollBackward: NestedScrollMode.SELF_FIRST  // When scrolling up, the current List is triggered first
        })
        .divider({
          strokeWidth: 1,
          color: Color.Gray
        })
        .edgeEffect(EdgeEffect.None)
        .height('100%')
        .width('100%')
      }
    }
    .width('100%')
    .height('100%')
  }
}
```
