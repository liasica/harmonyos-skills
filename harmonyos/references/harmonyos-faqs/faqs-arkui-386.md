---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-386
title: 如何禁用Refresh组件的下拉刷新
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何禁用Refresh组件的下拉刷新
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:28a3dfe15757a0d94a6e74d9e8b03e5e99da75477d4edaa759380dadb3011c86
---

**问题现象**

在使用Refresh组件时，开发者需要控制Refresh组件的下拉刷新功能，实现临时禁用或者开启下拉刷新。

**解决措施**

可以通过[pullDownRatio](../harmonyos-references/ts-container-refresh.md#pulldownratio12)设置跟手系数，当设置为0时，表示不跟随手势下拉，即可禁用下拉刷新。

禁用Refresh组件下拉刷新的示例如下：

```typescript
@Entry
@Component
struct Index {
  @State isRefreshing: boolean = false;
  @State arr: String[] = ['0', '1', '2', '3', '4', '5'];
  @State downRatio: number = 1;

  build() {
    Column() {
      Refresh({ refreshing: $$this.isRefreshing }) {
        Column() {
          Row({ space: 10 }) {
            Button('不允许下拉刷新')
              .onClick(() => {
                this.downRatio = 0;
              })
            Button('允许下拉刷新')
              .onClick(() => {
                this.downRatio = 1;
              })
          }

          List() {
            ForEach(this.arr, (item: string) => {
              ListItem() {
                Text('' + item)
                  .width('70%')
                  .height(80)
                  .fontSize(16)
                  .margin(10)
                  .textAlign(TextAlign.Center)
                  .borderRadius(10)
                  .backgroundColor(0xFFFFFF)
              }
            }, (item: string) => item)
          }
          .onScrollIndex((first: number) => {
            console.info(first.toString());
          })
          .width('100%')
          .height('100%')
          .alignListItem(ListItemAlign.Center)
          .scrollBar(BarState.Off)
        }
      }
      .onRefreshing(() => {
        setTimeout(() => {
          this.isRefreshing = false;
        }, 2000)
        console.info('onRefreshing test');
      })
      .pullDownRatio(this.downRatio)
      .backgroundColor(0x89CFF0)
      .refreshOffset(64)
      .pullToRefresh(true)
    }
  }
}
```
