---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-338
title: Marquee组件的文字滚动，第一次滚动出现大量空白，如何避免空白出现
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Marquee组件的文字滚动，第一次滚动出现大量空白，如何避免空白出现
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:bf489111ff38ca8918b2af080ae2ab8bdcc39234b22fd096d65dff66a12a9f70
---

**问题现象**

Marquee组件在文本滚动时，文本滚动到控件的开头，会造成大量空白，如何实现让文本末尾滚动到控件末尾时停止，避免空白出现。

**解决措施**

推荐使用Scroll代替跑马灯组件实现文字滚动。示例代码如下：

```typescript
@Entry
@Component
struct MarqueeScroll {
  @State textList: string[] = [
    'this is a test string1 this is a test string1',
    'this is a test string2 this is a test string2 this is a test string2',
    'this is a test string3 this is a test string3 this is a test string3 this is a test string3'
  ];
  @State count: number = 1;

  build() {
    Row() {
      Column() {
        myMarqueeCard({
          textList: $textList,
          updateList: () => {
            this.textList = [
              `This is test data${this.count++}This is test data${this.count++}`,
              `This is test data${this.count++}This is test data${this.count++}This is test data${this.count++}`,
              `This is test data${this.count++}This is test data${this.count++}This is test data${this.count++}This is test data${this.count++}`
            ];
          }
        })
      }
      .width('100%')
      .margin(20)
    }
    .height('100%')
  }
}

@Component
struct myMarqueeCard {
  @Link @Watch('handleNewList') textList: string[];
  @State list: string[] = [];
  scroller1: Scroller = new Scroller();
  scroller2: Scroller = new Scroller();
  scroller3: Scroller = new Scroller();
  updateList?: () => void;
  private intervalID?: number;

  handleNewList() {
    console.info(JSON.stringify(this.textList));
  }

  handleScroll(scroller: Scroller) {
    this.intervalID = setInterval(() => {
      const curOffset: OffsetResult = scroller.currentOffset();
      scroller.scrollTo({
        xOffset: curOffset.xOffset + 50, yOffset: curOffset.yOffset, animation: {
          duration: 1000,
          curve: Curve.Linear
        }
      });
      if (scroller.isAtEnd() && this.scroller1.isAtEnd() && this.scroller2.isAtEnd() && this.scroller3.isAtEnd() &&
      this.updateList) {
        this.scroller1.scrollTo({ xOffset: 0, yOffset: 0, animation: { duration: 0 } });
        this.scroller2.scrollTo({ xOffset: 0, yOffset: 0, animation: { duration: 0 } });
        this.scroller3.scrollTo({ xOffset: 0, yOffset: 0, animation: { duration: 0 } });
        this.updateList();
      }
    }, 500);
  }

  @Builder
  SingleText($$: SingleTextParams) {
    Scroll($$.scroller) {
      Row() {
        Text($$.text)
          .fontSize(30)
          .onAppear(() => {
            this.handleScroll($$.scroller);
          })
      }
    }
    .width(300)
    .scrollable(ScrollDirection.Horizontal)
    .enableScrollInteraction(false)
    .scrollBar(BarState.Off)
  }

  aboutToDisappear(): void {
    clearInterval(this.intervalID);
  }

  build() {
    Column() {
      this.SingleText({ text: this.textList[0], scroller: this.scroller1 })
      this.SingleText({ text: this.textList[1], scroller: this.scroller2 })
      this.SingleText({ text: this.textList[2], scroller: this.scroller3 })
    }
  }
}

class SingleTextParams {
  text: string = '';
  scroller: Scroller = new Scroller();
}
```
