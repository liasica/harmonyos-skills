---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-643
title: 实现影视App首页内容推荐功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现影视App首页内容推荐功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ed98f7d2002fe9753bc2d3a18d792a8864946f776bdd8c39ef34e24aa2d5e767
---

## 问题现象

如何实现影视类app首页的内容推荐功能？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/a0UDfGJ8SFK_3WVJHzeJlw/zh-cn_image_0000002628394512.gif "点击放大")

## 背景知识

* ArkUI提供轻量的UI元素复用机制[@Builder](../harmonyos-guides/arkts-builder.md)，其内部UI结构固定，仅与使用方进行数据传递。开发者可将重复使用的UI元素抽象成函数，在build函数中调用。
* [translate](../harmonyos-references/ts-universal-attributes-transformation.md#translate)是HarmonyOS提供的一种通用属性，用于设置组件的平移。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)事件会在组件区域变化时触发该回调。该事件仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。由绘制变化所导致的渲染属性变化不会响应回调，如translate、offset。若组件自身位置由绘制变化决定也不会响应回调，如bindSheet。
* UIContext提供[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)接口来指定由于闭包代码导致的状态变化插入过渡动效。

## 解决方案

1. 创建ZonesItem数组，用来存储影视的图片数据，自定义SegmentButton组件，用来存储并渲染影视的标题数据。
2. 在ForEach方法中对zonesList进行渲染，并根据当前显示页对图片进行动画效果处理。

完整示例参考如下：

```ts
class ZoneConst {
  static readonly ITEM_WIDTH: number = 70;
  static readonly SHOW_COUNT: number = 3;
  static readonly HALF_COUNT: number = Math.floor(ZoneConst.SHOW_COUNT / 2);
  static readonly OPACITY_COEFFICIENTS: number = 0.1;
  static readonly OFFSET_COEFFICIENTS: number = 10;
  static readonly MAX_OFFSET_X: number = 100;
  static readonly MAX_MOVE_OFFSET: number = 60;
  static readonly SWIPER_DURATION: number = 300;
  static readonly SHADOW_RADIUS: number = 50;
  static readonly SWIPER_ASPECT_RATIO: number = 6 / 4;
}

interface itemButton {
  text: string;
}

class ZonesItem {
  thumbnail: ResourceStr = '';
}

const defaultList: ZonesItem[] = [
  {
    thumbnail: $r('app.media.startIcon'), // 此处仅为样例，请开发者更换为可用图片
  },
  {
    thumbnail: $r('app.media.startIcon'),
  },
  {
    thumbnail: $r('app.media.startIcon'),
  },
];

@Component
struct SegmentButton {
  @Prop buttonOptions: itemButton[] = [{
    text: 'ljx'
  }, {
    text: 'byfx'
  }, {
    text: 'narm'
  }];
  @Link currentIndex: number;
  @State w: number = 0;
  @State h: number = 0;
  @State color: string | Resource = '#272727';
  @State selectColor: string | Resource = '#ffffff';
  @State backColor: string | Resource = '#e1dfe0';
  @Prop offsetX: number = 0;
  private buttonClick = (index: number) => {
    console.info('index:', index);
  };

  @Builder
  overItem() {
    Row()
      .zIndex(1)
      .width(this.w / this.buttonOptions.length)
      .backgroundColor(Color.Red)
      .height('100%')
      .borderRadius(this.h / 2)
      .backgroundColor(this.selectColor)
      .linearGradient({
        angle: 90,
        colors: [['#ff6c8e', 0.0], [' #ff2754', 1.0]]
      })
      .translate({
        x: this.currentIndex * this.w / this.buttonOptions.length + this.offsetX
      })
      .position({
        left: 0,
        top: 0
      });
  }

  // 构建项目
  build() {
    Row() {
      this.overItem();
      ForEach(this.buttonOptions, (item: itemButton, index) => {
        Row({
          space: 10
        }) {
          Text(item.text)
            .fontSize(15)
            .fontColor(this.currentIndex === index ? this.selectColor : this.color);
        }
        .justifyContent(FlexAlign.Center)
        .zIndex(2)
        .width(this.w / this.buttonOptions.length)
        .height('100%')
        .onClick(() => {
          this.buttonClick(index);
          this.getUIContext().animateTo({
            duration: 300
          }, () => {
            this.currentIndex = index;
          });
        });
      }, (item: itemButton) => JSON.stringify(item));
    }
    .onAreaChange((_old, n) => {
      this.w = n.width as number;
      this.h = n.height as number;
    })
    .zIndex(0)
    .borderRadius(30)
    .height(40)
    .width('100%')
    .backgroundColor(this.backColor)
    .clip(true);
  }
}

@Entry
@Component
struct RecommendApp {
  changedIndex: boolean = true;
  zonesList: ZonesItem[] = defaultList;
  @State aheadIndex: number = ZoneConst.HALF_COUNT;
  @State marginBottom: number = 0;
  uiContext: UIContext | undefined = undefined;

  aboutToAppear(): void {
    this.uiContext = this.getUIContext();
  }

  getImgCoefficients(index: number): number {
    let coefficient = this.aheadIndex - index;
    let tempCoefficient = Math.abs(coefficient);
    if (tempCoefficient <= ZoneConst.HALF_COUNT) {
      return coefficient;
    }
    let dataLength = this.zonesList.length;
    let tempOffset = dataLength - tempCoefficient;
    if (tempOffset <= ZoneConst.HALF_COUNT) {
      if (coefficient > 0) {
        return -tempOffset;
      }
      return tempOffset;
    }
    return 0;
  }

  getOffSetX(index: number): number {
    let offsetIndex = this.getImgCoefficients(index);
    let tempOffset = Math.abs(offsetIndex);
    let offsetX = this.marginBottom / (tempOffset + 1);
    if (tempOffset === 1) {
      offsetX += -offsetIndex * ZoneConst.MAX_OFFSET_X;
    } else if (tempOffset === ZoneConst.HALF_COUNT) {
      offsetX += -offsetIndex * (ZoneConst.MAX_OFFSET_X - ZoneConst.OFFSET_COEFFICIENTS);
    }
    return offsetX;
  }

  startAnimation(isUp: boolean): void {
    this.getUIContext().animateTo({
      duration: ZoneConst.SWIPER_DURATION,
    }, () => {
      let dataLength = this.zonesList.length;
      let tempIndex = isUp ? this.aheadIndex + 1 : dataLength + this.aheadIndex - 1;
      this.aheadIndex = tempIndex % dataLength;
      this.marginBottom = 0;
    });
  }

  handlePanGesture(offsetX: number): void {
    if (Math.abs(offsetX) < ZoneConst.MAX_MOVE_OFFSET) {
      this.marginBottom = offsetX;
    } else {
      if (this.changedIndex) {
        return;
      }
      this.changedIndex = true;
      this.startAnimation(offsetX < 0);
    }
  }

  build() {
    Column({
      space: 20
    }) {
      Stack() {
        ForEach(this.zonesList, (item: ZonesItem, index: number) => {
          Row() {
            Image(item.thumbnail)
              .objectFit(ImageFit.Cover)
              .borderRadius(16)
              .shadow({
                radius: 50,
                color: `rgba(0,0,0,0.3)`,
                offsetY: 1
              })
              .opacity(1 - Math.min(ZoneConst.HALF_COUNT,
                Math.abs(this.getImgCoefficients(index))) * ZoneConst.OPACITY_COEFFICIENTS);
          }
          .width(index !== this.aheadIndex && this.getImgCoefficients(index) === 0 ? '10%' : `${ZoneConst.ITEM_WIDTH - ZoneConst.OFFSET_COEFFICIENTS * Math.abs(this.getImgCoefficients(index))}%`)
          .aspectRatio(ZoneConst.SWIPER_ASPECT_RATIO)
          .borderRadius(16)
          .offset({ x: this.getOffSetX(index) })
          .zIndex(index !== this.aheadIndex && this.getImgCoefficients(index) === 0 ?
            0 : ZoneConst.HALF_COUNT - Math.abs(this.getImgCoefficients(index)));
        }, (item: ZonesItem) => JSON.stringify(item));
      }
      .width('100%')
      .alignContent(Alignment.Center)
      .gesture(
        PanGesture({ direction: PanDirection.Horizontal })
          .onActionStart((event: GestureEvent) => {
            this.changedIndex = false;
            this.handlePanGesture(event.offsetX);
          })
          .onActionUpdate((event: GestureEvent) => {
            this.handlePanGesture(event.offsetX);
          })
          .onActionEnd(() => {
            this.getUIContext().animateTo({
              duration: ZoneConst.SWIPER_DURATION,
            }, () => {
              this.marginBottom = 0;
            });
          })
      );

      SegmentButton({
        currentIndex: this.aheadIndex
      });
    }
    .justifyContent(FlexAlign.Start)
    .height('100%')
    .backgroundColor($r('sys.color.point_color_checked'));
  }
}
```
