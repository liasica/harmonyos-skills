---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1472
title: onSizeChange计算有偏差，如何保持和onAreaChange计算一致
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > onSizeChange计算有偏差，如何保持和onAreaChange计算一致
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cb368a0f0fe84ef74d7bc1fd3c981f74e6dd67863f44f788d82de6471f915511
---

## 问题现象

onSizeChange测量值不准，onSizeChange和onAreaChange计算结果不一致。

## 背景知识

* [onSizeChange](../harmonyos-references/ts-universal-component-size-change-event.md#onsizechange)：组件区域变化时触发该回调。仅会响应由布局变化所导致的组件尺寸发生变化时的回调。该接口在布局发生变化时触发，由于计算精度的关系，其返回值可能与真实物理尺寸存在细微的差异。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)：组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。
* [pixelRound](../harmonyos-references/ts-universal-attributes-pixelroundforcomponent.md#pixelround)：指定当前组件在指定方向上的像素取整对齐方式，某方向不设置时默认在该方向进行四舍五入取整。

## 解决方案

onSizeChange是实际绘制的值，可以使用组件级像素取整pixelRound把组件的对齐方式设置为不取整计算。

```screen
@Component
struct onAreaChangeSolution1 {
  aboutToAppear() {
  }

  build() {
    Column() {
      Column() {
      }
      .pixelRound({
        start: PixelRoundCalcPolicy.NO_FORCE_ROUND,
        end: PixelRoundCalcPolicy.NO_FORCE_ROUND,
        top: PixelRoundCalcPolicy.NO_FORCE_ROUND,
        bottom: PixelRoundCalcPolicy.NO_FORCE_ROUND
      })
      .height('2')
      .onSizeChange((_, area: SizeOptions) => {
        console.info('=====onSizeChange: ' + this.getUIContext().vp2px(area.height as number));
      })
      .onAreaChange((_, area: Area) => {
        console.info('=====onAreaChange: ' + this.getUIContext().vp2px(area.height as number));
      });

      Column() {
      }
      .pixelRound({
        start: PixelRoundCalcPolicy.NO_FORCE_ROUND,
        end: PixelRoundCalcPolicy.NO_FORCE_ROUND,
        top: PixelRoundCalcPolicy.NO_FORCE_ROUND,
        bottom: PixelRoundCalcPolicy.NO_FORCE_ROUND
      })

      .height('2')
      .onSizeChange((_, area: SizeOptions) => {
        console.info('=====onSizeChange2: ' + this.getUIContext().vp2px(area.height as number));
      })
      .onAreaChange((_, area: Area) => {
        console.info('=====onAreaChange2: ' + this.getUIContext().vp2px(area.height as number));
      });
    }
    .pixelRound({
      start: PixelRoundCalcPolicy.NO_FORCE_ROUND,
      end: PixelRoundCalcPolicy.NO_FORCE_ROUND,
      top: PixelRoundCalcPolicy.NO_FORCE_ROUND,
      bottom: PixelRoundCalcPolicy.NO_FORCE_ROUND
    })
    .backgroundColor(Color.Pink)
    .width('100%')
    .onSizeChange((_, area: SizeOptions) => {
      console.info('=====onSizeChange_out: ' + this.getUIContext().vp2px(area.height as number));
    })
    .onAreaChange((_, area: Area) => {
      console.info('=====onAreaChange_out: ' + this.getUIContext().vp2px(area.height as number));
    });
  }
}
```

## 常见FAQ

Q：如何使用[onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)对[Row](../harmonyos-references/ts-container-row.md)组件进行布局？

A：可以使用[onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)获取[Row](../harmonyos-references/ts-container-row.md)组件的宽度，进行布局。

```screen
@Component
struct onAreaChangeSolution2 {
  @State widthAll: number = 0;
  @State widthA: number = 0;

  build() {
    Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.SpaceBetween }) {
      Stack() {
        Row() {
          Text('标题');
          Text('字符串字符串字符串字符串字符串字符串');
        }
        .height(50)
        .backgroundColor('red')
        .id('A')
        .onAreaChange((oldValue: Area, newValue: Area) => {
          let info = JSON.stringify(newValue.width);
          this.widthA = parseFloat(info);
        })
        .margin({ left: -1 });

        Row() {
          Text('增长率70.5%');
        }
        .height(50)
        .backgroundColor('blue')
        .width(this.widthAll - this.widthA)
        .id('B')
        .margin({ left: 281 });
      };
    }
    .width('100%')
    .onAreaChange((oldValue: Area, newValue: Area) => {
      let info = JSON.stringify(newValue.width);
      this.widthAll = parseFloat(info);
      console.log('=================>all:' + this.widthAll);
    })
    .backgroundColor(Color.Green);
  }
}
```
