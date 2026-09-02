---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1123
title: 页面上沿重叠显示
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 页面上沿重叠显示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a20e5b81db96aa7589ab47d2b2388202af630d5adf82550cd9824d71ddcf9180
---

## 问题现象

页面在向上滑动过程中，页面顶部区域透视出应用其他页面的内容，页面重叠显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/r7vyjFTOS1-dTH05pNUyJA/zh-cn_image_0000002628409514.png)

## 背景知识

设置组件的透明度：[opacity](../harmonyos-references/ts-universal-attributes-opacity.md)。

## 问题定位

1. 检查主页面在向上滑动过程中自定义个人信息栏透明度变化情况。页面在向上缓慢滑动时，自定义个人信息栏逐渐浮现出来，直至彻底显示在页面顶端。自定义个人信息栏固定显示后，页面下滑，自定义个人信息栏又会逐渐透明，直至彻底消失不见。
2. 根据上述UI状态变化，可以确定自定义个人信息栏，透明度是随主页面向上滑动从0到1从而使自定义个人信息栏组件逐渐显示出来。反之，透明度从1到0从而使自定义个人信息栏组件逐渐透明消失。
3. 在出现或消失过程中，由于自定义个人信息栏组件半透明，可以透视出底层页面内容，出现重叠显示问题。

## 分析结论

由于自定义个人信息栏透明度属性设置错误，导致主页面向上滑动过程中页面会重叠显示问题。

## 修改建议

主页面向上滑动一定距离后，手机顶部状态栏以及自定义个人信息栏透明度直接由0更新为1，而不是由0至1随主页面向上滑动距离渐变。

```ts
import { window } from '@kit.ArkUI';

@Entry
@Component
struct OpacityTest {
  @State arr: number[] = [];
  @State opacityNum: number = 0;
  @State curYOffset: number = 0;
  @State statusbarHeight: number = 40;
  @State navbarHeight: number = 30;
  scroller = new Scroller();
  backImageHeight = 300;

  aboutToAppear() {
    // 模拟列表数据
    for (let i = 0; i < 30; i++) {
      this.arr.push(i);
    }
    // 启用沉浸式布局
    window.getLastWindow(this.getUIContext().getHostContext(), (err, data) => {
      data.setWindowLayoutFullScreen(true);
      let statusbar = data.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM);
      this.statusbarHeight = this.getUIContext().px2vp(statusbar.topRect.height); // 状态栏高度
      let navIndicator = data.getWindowAvoidArea(window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR);
      this.navbarHeight = this.getUIContext().px2vp(navIndicator.bottomRect.height); // 导航条高度
    });
  }

  // 列表item样式
  @Styles
  listCard() {
    .backgroundColor(Color.White)
    .height(72)
    .width('100%')
    .borderRadius(12);
  }

  build() {
    Stack() {
      // 底部区域占位
      Column() {
        Text('页面底层内容占位')
          .margin({ left: 16, right: 16 });
      }
      .width('100%')
      .height('100%')
      .alignItems(HorizontalAlign.Start);

      Scroll(this.scroller) {
        Column() {
          Column()
            .width('100%')
            .height(this.backImageHeight)
            .backgroundColor('#fff')// 可自行替换背景色/背景图
            .borderRadius(12);
          Tabs({ barPosition: BarPosition.Start }) {
            TabContent() {
              List({ space: 10 }) {
                ForEach(this.arr, (item: number) => {
                  ListItem() {
                    Text('item' + item)
                      .fontSize(20);
                  }.listCard();
                }, (item: string) => item);
              }
              .scrollBar(BarState.Off)
              .width('100%')
              .height('auto')
              .edgeEffect(EdgeEffect.None)
              .nestedScroll({
                scrollForward: NestedScrollMode.PARENT_FIRST,
                scrollBackward: NestedScrollMode.SELF_FIRST
              });
            }
            .tabBar('待办');

            TabContent().tabBar('待阅');
          }
          .vertical(false)
          .width('100%');
        }
        .width('100%')
        .borderRadius(12)
        .padding({ left: 12, right: 12 });
      }
      .friction(0.6)
      .scrollBar(BarState.Off)
      .width('100%')
      .height(`auto`)
      .position({
        top: 40,
      })
      .onDidScroll(() => {
        // 获取Scroller组件在Y轴方向的滚动距离
        this.curYOffset = this.scroller.currentOffset().yOffset;
        // 计算透明度
        let opacity = this.curYOffset / this.backImageHeight;
        this.opacityNum = opacity >= 1 ? 1 : 0;
      })
      .margin({ bottom: this.navbarHeight });

      // 悬浮标题栏
      Text('个人信息')
        .fontSize(24)
        .fontColor(Color.Black)
        .fontWeight(FontWeight.Bold)
        .backgroundColor('#f1f3f5')
        .opacity(this.opacityNum)
        .position({ top: 0 })
        .width('100%')
        .height(40)
        .padding({ left: 20, right: 0 });
    }
    .backgroundColor('#f1f3f5')
    .padding({ top: this.statusbarHeight, bottom: this.navbarHeight })
    .width('100%')
    .height('100%');
  }
}
```
