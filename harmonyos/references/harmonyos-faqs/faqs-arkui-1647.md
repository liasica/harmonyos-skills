---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1647
title: Tabs组件如何实现预加载
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Tabs组件如何实现预加载
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4389375ad2aef6f729d34567db74fb2a1469f5f88db490688429192e4f8ebcdf
---

## 问题现象

Tabs的子组件是否可以实现预加载，具体实现方式是什么？

## 背景知识

* Tabs组件的[preloadItems](../harmonyos-references/ts-container-tabs.md#preloaditems12)方法可以控制Tabs预加载指定子节点。
* Swiper组件的[cachedCount](../harmonyos-references/ts-container-swiper.md#cachedcount15)能够设置预加载子组件个数。

## 解决方案

方案一：调用Tabs组件的preloadItems接口后会一次性加载所有指定的子节点，为了性能考虑，建议分批加载子节点。具体代码示例可参考官网：[预加载子节点](../harmonyos-references/ts-container-tabs.md#示例11预加载子节点)。

方案二：Swiper组件支持通过cachedCount属性设置预加载子组件。可以基于Swiper组件来构建自定义的Tabs。

```ts
@Entry
@ComponentV2
struct TabsPreLoadDemo {
  @Local tabNames: string[] = ['飞机', '铁路', '自驾', '地铁', '公交', '骑行'];
  @Local selectedTabIndex: number = 0; // 当前选中标签页的索引值
  @Local indicatorLeftOffset: number = 0; // 指示器左侧偏移量
  @Local indicatorOffset: number = 0; // 指示器整体偏移量
  @Local firstWidth: number = -1; // 选中标签宽度
  @Local otherWidth: number = -1; // 其他标签宽度
  @Local swiperController: SwiperController = new SwiperController();
  @Local swiperWidth: number = 0;

  build() {
    RelativeContainer() {
      Stack() {
        Rect()
          .height(30)
          .stroke(Color.Black)
          .radius(10)
          .width(this.firstWidth)
          .fill('#bff9f2')
          .animation({ duration: 300, curve: Curve.LinearOutSlowIn })
          .position({ left: this.indicatorLeftOffset + this.indicatorOffset, bottom: 0 });
      }
      .width('100%')
      .alignRules({
        center: { anchor: 'TabBar', align: VerticalAlign.Center }
      });

      // 自定义标签栏
      Row() {
        ForEach(this.tabNames, (name: string, index: number) => {
          Row() {
            Text(name)
              .fontSize(16)
              .fontWeight(this.selectedTabIndex === index ? FontWeight.Bold : FontWeight.Normal)
              .textAlign(TextAlign.Center)
              .animation({ duration: 300 });
            Image($r('app.media.startIcon'))
              .width(14)
              .height(14)
              .margin({ left: 2 })
              .visibility(this.selectedTabIndex === index ? Visibility.Visible : Visibility.None)
              .animation({ duration: 300 });
          }
          .justifyContent(FlexAlign.Center)
          .layoutWeight(this.selectedTabIndex === index ? 1.5 : 1)
          .animation({ duration: 300 })
          .onClick(() => {
            // 点击标签栏切换swiper
            this.selectedTabIndex = index;
            this.swiperController.changeIndex(index, false);
            this.getUIContext().animateTo({ duration: 500, curve: Curve.LinearOutSlowIn }, () => {
              this.indicatorLeftOffset = this.otherWidth * index;
            });
          });
        });
      }
      .width('100%')
      .height(30)
      .id('TabBar')
      .onAreaChange((_: Area, newValue: Area) => {
        // 设置被选中标签宽度和其它标签宽度
        let tabBarWidth = newValue.width.valueOf() as number;
        this.firstWidth = 1.5 * tabBarWidth / (this.tabNames.length + 0.5);
        this.otherWidth = tabBarWidth / (this.tabNames.length + 0.5);
      });

      Swiper(this.swiperController) {
        ForEach(this.tabNames, (name: string, index: number) => {
          Column() {
            Text(`${name} - ${index}`)
              .fontSize(24);
          }
          .alignItems(HorizontalAlign.Center)
          .justifyContent(FlexAlign.Center)
          .height('100%')
          .width('100%');
        });
      }
      .cachedCount(3) // 设置预加载，即当前页面前后各3个组件均会被加载
      .onAnimationStart((index: number, targetIndex: number) => {
        // 控制指示器同步效果
        if (targetIndex > index) {
          this.indicatorLeftOffset += this.otherWidth;
        } else if (targetIndex < index) {
          this.indicatorLeftOffset -= this.otherWidth;
        }
        this.indicatorOffset = 0;
        this.selectedTabIndex = targetIndex;
      })
      .onAnimationEnd(() => {
        this.indicatorOffset = 0;
      })
      .onGestureSwipe((_: number, extraInfo: SwiperAnimationEvent) => {
        // 控制边界项的滑动
        let move: number = this.getOffset(extraInfo.currentOffset);
        if ((this.selectedTabIndex === 0 && extraInfo.currentOffset > 0) ||
          (this.selectedTabIndex === this.tabNames.length - 1 && extraInfo.currentOffset < 0)) {
          return;
        }
        this.indicatorOffset = extraInfo.currentOffset < 0 ? move : -move;
      })
      .onAreaChange((_: Area, newValue: Area) => {
        let width = newValue.width.valueOf() as number;
        this.swiperWidth = width;
      })
      .curve(Curve.LinearOutSlowIn)
      .loop(false)
      .indicator(false)
      .width('100%')
      .id('MainContext')
      .alignRules({
        top: { anchor: 'Tabs', align: VerticalAlign.Bottom },
        bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
      });
    }
    .height('100%')
    .width('100%')
    .padding(10);
  }

  // 计算偏移量的方法（根据Swiper滑动偏移量计算标签指示器位置）
  getOffset(swiperOffset: number): number {
    let swiperMoveRatio: number = Math.abs(swiperOffset / this.swiperWidth);
    let tabMoveValue: number = swiperMoveRatio >= 1 ? this.otherWidth : this.otherWidth * swiperMoveRatio;
    return tabMoveValue;
  }
}
```

两种方案对比：

| 方案 | 优缺点 |
| --- | --- |
| 方案一：preloadItems | 数据量多的情况下需要手动控制分批次预加载。 |
| 方案二：Swiper | 会根据显示的子项自动加载前后项，但需要控制标签栏和Swiper的联动。 |

## 常见FAQ

Q：在Tabs组件中添加多个TabContent时，节点树中TabBar的子节点数量始终比实际TabContent的数量多两个，但TabContent的数量是正确的。这种现象的原因是什么？

A：当使用ForEach动态生成TabBar时，框架会默认创建2个额外的缓存节点用于预加载优化，额外节点不会影响功能逻辑和性能。
