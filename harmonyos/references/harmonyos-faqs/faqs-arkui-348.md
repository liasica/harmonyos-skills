---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-348
title: 如何实现List的折叠动画效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现List的折叠动画效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b938d48933ac94934b67b304d91ff7c230e08e81c90e95e754c6b97b62656e86
---

可以使用显式动画animateTo结合条件渲染if控制 ListItem内容区域的展开和收起，示例代码如下：

```ts
@Entry
@Component
struct ListCollapseExpand {
  private numberList: number[] = [0, 1, 2, 3, 4, 5, 6];
  @State isContentShow: boolean = true;
  @State selectItem: number = 0;

  build() {
    Column() {
      List({ initialIndex: 0 }) {
        ForEach(this.numberList, (item: number, index: number) => {
          ListItem() {
            Column() {
              Row() {
                Text(item.toString())
                Button(this.isContentShow && this.selectItem === item ? 'Collapse' : 'Expand')
                  .onClick(() => {
                    this.getUIContext().animateTo({
                      duration: 300,
                      onFinish: () => {
                        console.info('animation end');
                      }
                    }, () => {
                      this.isContentShow = !this.isContentShow;
                      this.selectItem = item;
                    })
                  })
              }
              .width('100%')
              .justifyContent(FlexAlign.SpaceBetween)

              // Display the content area only when the current item is selected and is in an expanded state.
              if (this.isContentShow && this.selectItem === item) {
                Text('This is the content area')
                  .backgroundColor(Color.Gray)
                  .width('100%')
                  .height(100)
              }
            }
            .backgroundColor(0xFFFFFF)
            .width('100%')
            .padding({
              top: 12,
              bottom: 12
            })
            .margin({ top: 10 })
          }
        }, (item: string) => item.toString())
      }
      .scrollBar(BarState.Off)
      .height('100%')
      .width('100%')
    }
    .backgroundColor(0xF1F3F5)
    .padding(12)
  }
}
```
