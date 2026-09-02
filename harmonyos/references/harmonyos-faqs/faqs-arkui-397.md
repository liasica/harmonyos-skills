---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-397
title: 如何实现swiper根据内容高度随滑动距离变动的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现swiper根据内容高度随滑动距离变动的效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a26d6c6f59598ab72a5b4509c1b0c09bbef4b12526e21ff1c58875b98a002132
---

可通过[onContentDidScroll()](../harmonyos-references/ts-container-swiper.md#oncontentdidscroll12)监听Swiper页面滑动事件来实现，示例代码如下：

```ts
let COLUMN_NUMBER = 5;
let COLUMN_GAP = 20;
let ROWS_GAP = 20;

@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('Head area')
        .textAlign(TextAlign.Center)
        .backgroundColor(Color.Yellow)
        .width('100%')
        .height(40)
      GridDemo()
        .width('90%')
      Text('Tail area')
        .textAlign(TextAlign.Center)
        .backgroundColor(Color.Green)
        .width('100%')
        .height('30%')
    }
  }
}

@Component
struct GridDemo {
  @State gridHeights: number[] = [];
  @State swiperHeight: number = 0;
  @State tipList: string[] = ['Mathematics', 'Chinese Language', 'English', 'Biology'];
  @State tipImageX: string = '0%';
  @State tipIndex: number = 0;
  @State numberList: number[][] = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
  ];
  private swiperController: SwiperController = new SwiperController();

  aboutToAppear(): void {
    this.getHeights();
  }

  getHeights() {
    for (let index = 0; index < this.numberList.length; index++) {
      let rowNumer = Math.ceil(this.numberList[index].length / COLUMN_NUMBER);
      let gridHeight = px2vp(122) * rowNumer + COLUMN_GAP * (rowNumer - 1);
      this.gridHeights.push(gridHeight);
    }
    this.swiperHeight = this.gridHeights[0];
  }

  build() {
    Column() {
      Stack() {
        Image($r('app.media.background'))
          .objectFit(ImageFit.Contain)
          .width((100 / this.tipList.length) + '%')
          .offset({ x: this.tipImageX })
        Row() {
          ForEach(this.tipList, (item: string, index: number) => {
            ListItem() {
              Text(item)
                .backgroundImage(this.tipIndex == index ? $r('app.media.background') : null, ImageRepeat.NoRepeat)
                .backgroundImageSize({
                  width: '100%',
                  height: '100%'
                })
            }
          }, (item: string) => item)
        }
        .justifyContent(FlexAlign.SpaceAround)
        .height(20)
        .width('100%')
        .margin({
          top: 5,
          bottom: 5
        })
      }
      .alignContent(Alignment.Start)
      .height(30)
      .backgroundColor(Color.Pink)

      Column() {
        Swiper(this.swiperController) {
          ForEach(this.numberList, (item: number, index: number) => {
            Child({ numberList: this.numberList[index] })
          })
        }
        .effectMode(EdgeEffect.None)
        .indicator(false)
        .loop(false)
        .onContentDidScroll((selectedIndex: number, index: number, position: number, mainAxisLength: number) => {
          // The direct scrolling positions of the two indices change the height of the parent control
          if (selectedIndex != index && Math.abs(selectedIndex - index) == 1) {
            let curHeight = this.gridHeights[selectedIndex];
            let targetHeight = this.gridHeights[index];
            this.swiperHeight = targetHeight +
              (selectedIndex < index ? (curHeight - targetHeight) : (targetHeight - curHeight)) * position;
          }
          // Switch the subscript of the selected status
          if (selectedIndex == index) {
            let curIndex = -1 / this.tipList.length * position + selectedIndex / this.tipList.length;
            this.tipImageX = (curIndex * 100).toFixed(2) + '%';
            this.tipIndex = Math.ceil(curIndex / 0.25 + 0.5) - 1;
          }
        })
      }
      .height(this.swiperHeight)
    }
    .width('100%')
  }
}

@Component
struct Child {
  @Prop numberList: number[];

  build() {
    Grid() {
      ForEach(this.numberList, (item: number) => {
        GridItem() {
          Column() {
            Image($r('app.media.startIcon'))
              .width(20)
              .height(20)
            Text('Menu' + item)
              .fontSize(15)
          }
        }
      })
    }
    .columnsGap(COLUMN_GAP)
    .rowsGap(ROWS_GAP)
    .scrollBar(BarState.Off)
    .columnsTemplate('1fr '.repeat(COLUMN_NUMBER))
    .animation({
      duration: 1000
    })
  }
}
```
