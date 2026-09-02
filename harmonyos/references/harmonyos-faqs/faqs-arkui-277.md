---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-277
title: 如何将ListItem的swipeAction滑动效果恢复到初始状态
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何将ListItem的swipeAction滑动效果恢复到初始状态
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d3860fab14ad0da1909bf7df9108040234ddb2c7ed7a230a5e026a6f0d926bc9
---

使用 ListScroller 提供的 closeAllSwipeActions() 方法恢复滑动效果，示例代码如下：

```ts
@Component
export struct SwiperActionRecover {
  @State arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  private scrollerForList: ListScroller = new ListScroller();

  @Builder
  itemEnd() {
    Row() {
      Button('Delete')
      Button('Set')
        .onClick(() => {
          this.scrollerForList.closeAllSwipeActions(); // This is the key line of code
        })
    }
    .justifyContent(FlexAlign.SpaceEvenly)
  }

  build() {
    Column() {
      List({ space: 5, scroller: this.scrollerForList }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text('item' + item)
              .width('100%')
              .height(100)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
          .transition({
            type: TransitionType.Delete,
            opacity: 0
          })
          .swipeAction({
            end: {
              builder: () => {
                this.itemEnd();
              },
              onAction: () => {
                this.getUIContext().animateTo({ duration: 1000 }, () => {
                  let index = this.arr.indexOf(item);
                  this.arr.splice(index, 1);
                });
              },
              actionAreaDistance: 56
            }
          })
        }, (item: string) => item)
      }
    }
    .padding(20)
    .backgroundColor(0xDCDCDC)
    .width('100%')
    .height('100%')
  }
}
```
