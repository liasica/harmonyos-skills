---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1581
title: 如何实现Swiper部分区域响应左右滑动事件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现Swiper部分区域响应左右滑动事件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:2b38b491292ac8a1e4cd0179c04fda372a0576987e95310e59162a0890616dfe
---

## 问题现象

Swiper设置子组件底部高度自适应后，希望上方区域不再响应Swiper的左右滑动事件。

## 背景知识

* [Swiper：](../harmonyos-references/ts-container-swiper.md)滑块视图容器，提供子组件滑动轮播显示的能力。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。返回值类型为[Area](../harmonyos-references/ts-types.md#area8)。
* [responseRegion](../harmonyos-references/ts-universal-attributes-touch-target.md#responseregion)：设置一个或多个触摸热区。

## 解决方案

实现思路如下：

1. Swiper组件实现了滑动页面切换功能，包含多个不同高度的页面项。
2. 通过ForEach动态生成滑动页面内容。
3. 使用onAreaChange回调监听页面高度变化，Swiper切换过程中动态计算触摸响应区域。

示例代码如下：

```ts
@Entry
@Component
struct SwiperDemo {
  private controller: SwiperController = new SwiperController();
  private list: string[] =
    [
      '我是第1个item，占1行',
      '我是第2个item，\n' + '占2行',
      '我是\n' + '第3个item，\n' + '占3行',
    ];
  @State map: Map<ESObject, number> = new Map(); // 存储Swiper自适应内容区域距离屏幕顶部的距离，用于设置触摸热区
  @State currentIndex: number = 0;
  @State region: Rectangle = {
    x: 0,
    y: 0,
    width: '100%',
    height: '100%'
  };

  build() {
    RelativeContainer() {
      Column() {
        Text('白色区域部分不希望响应Swiper拖动事件')
          .fontSize(20)
          .fontColor(Color.Black);
      }
      .justifyContent(FlexAlign.Center)
      .alignRules({
        left: { anchor: '__container__', align: HorizontalAlign.Start },
        right: { anchor: '__container__', align: HorizontalAlign.End },
        top: { anchor: '__container__', align: VerticalAlign.Top },
        bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
      });

      Swiper(this.controller) {
        ForEach(this.list, (item: number, index: number) => {
          Column() {
            Column() {
              Text(this.list[index])
                .fontSize(30);
            }
            .backgroundColor("#f1f3f5")
            .width('100%')
            .borderRadius(6)
            .onAreaChange((oldValue: Area, newValue: Area) => {
              console.info('item', item);
              console.info('oldValue', oldValue);
              if (!this.map.get(index.toString())) {
                // onAreaChange回调监听页面自适应高度变化，存储Swiper自适应内容区域距离屏幕顶部的距离。
                this.map.set(index.toString(), newValue.position.y as number);
                this.region = {
                  width: '100%',
                  height: '100%',
                  x: 0,
                  y: this.map.get(this.currentIndex.toString()) as number // 触摸热区的范围
                };
              }
            });
          }
          .justifyContent(FlexAlign.End)
          .width('100%')
          .padding(10);
        });
      }
      .onChange((index: number) => {
        this.currentIndex = index;
        // Swiper切换过程中动态设置触摸响应区域
        this.region = {
          width: '100%',
          height: '100%',
          x: 0,
          y: this.map.get(this.currentIndex.toString()) as number
        };
      })
      .indicator(false)
      .autoPlay(false)
      .loop(false)
      .height('100%')
      .responseRegion(
        this.region
      )
      .alignRules({
        left: { anchor: '__container__', align: HorizontalAlign.Start },
        right: { anchor: '__container__', align: HorizontalAlign.End },
        bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
      });
    }
    .width('100%')
    .height('100%');
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/yXKCAYmDQK2XkFnqySfFaw/zh-cn_image_0000002712946877.png "点击放大")
