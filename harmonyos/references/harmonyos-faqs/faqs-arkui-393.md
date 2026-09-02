---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-393
title: Swiper如何自定义导航点高度位置
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Swiper如何自定义导航点高度位置
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:b32752ab4e5ac1268b3f5794cdc0310259e461d81b4cfee2e0cf1df29db424fe
---

**问题描述**

[Swiper](../harmonyos-references/ts-container-swiper.md)组件内置[indicator](../harmonyos-references/ts-container-swiper.md#indicator)UI样式有宽高，不支持自定义修改。

**解决措施**

方案一：可以使用自定义Indicator的方式。当前DotIndicator的规格固定存在内边距，无法满足问题需求。可以通过以下步骤实现无内边距的导航指示器效果：

1. 在Stack组件中创建Swiper轮播组件与导航点Column组件。
2. 使用[LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)循环渲染Column组件，并设置合适的高度和外边距，例如在Stack组件内设置[alignContent](../harmonyos-references/ts-container-stack.md#aligncontent): Alignment.Bottom参数，表示底部对齐，也可以采用[位置设置](../harmonyos-references/ts-universal-attributes-location.md)的方式，直接指定指示器位置。
3. 将index的值与currentIndex作比较，当两者相同时，改变Column的宽度与颜色，以此实现导航点效果。

具体参考代码如下所示：

```typescript
@Entry
@Component
struct SwiperExample {
  private swiperController: SwiperController = new SwiperController();
  @State arr: string[] = ['1', '2', '3', '4', '5', '6'];
  @State widthLength: number = 0;
  @State heightLength: number = 0;
  @State currentIndex: number = 0;

  build() {
    Column({ space: 5 }) {
      Stack({ alignContent: Alignment.Bottom }) {
        Swiper(this.swiperController) {
          ForEach(this.arr, (item: string) => {
            Text(item)
              .width('90%')
              .height(200)
              .backgroundColor(0xAFEEEE)
              .textAlign(TextAlign.Center)
              .fontSize(30)
          }, (item: string) => item)
        }
        .cachedCount(2)
        .index(0)
        .indicator(false)
        .onChange((index: number) => {
          this.currentIndex = index;
        })

        Row() {
          ForEach(this.arr, (_: string, index: number) => {
            Column()
              .width(this.currentIndex == index ? 15 : 5)
              .height(5)
              .margin(5)
              .backgroundColor(this.currentIndex == index ? Color.Gray : Color.White)
          }, (item: string) => item)
        }
      }
    }
    .width('100%')
    .height('100%')
  }
}
```

方案二：采用API15中Indicator组件。 Indicator组件采用的依旧是Swiper中的默认指示器样式，一样有32vp的交互高度限制，不过该组件将Swiper与指示器单独分割，可以通过Column组件单独封装指示器，再通过clip属性裁剪，控制Indicator组件高度，其它的与方案一类似，采用Stack组件封装。 实现方式如下：

```typescript
@Entry
@Component
struct DotIndicatorDemo {
  private indicatorController: IndicatorComponentController = new IndicatorComponentController();
  private swiperController: SwiperController = new SwiperController();
  @State list: string[] = ['1', '2', '3', '4', '5', '6'];

  build() {
    Stack({ alignContent: Alignment.Bottom }) {
      Swiper(this.swiperController) {
        ForEach(this.list, (item: string) => {
          Text(item)
            .width('90%')
            .height(200)
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
        }, (item: string) => item)
      }
      .cachedCount(2)
      .index(0)
      .indicator(this.indicatorController)

      Column() {
        IndicatorComponent(this.indicatorController)
          .style(
            new DotIndicator()
              .itemWidth(10)
              .itemHeight(10)
              .selectedItemWidth(20)
              .selectedItemHeight(10)
              .color(Color.White)
              .selectedColor(Color.Gray)
          )
      }
      .height(25)
      .clip(true)
    }
    .width('100%')
  }
}
```

注意：若方案二指示器背景为透明，不使用clip裁剪也可。同时若背景颜色为透明，也可采用margin属性，设置底部为负值达成类似效果。
