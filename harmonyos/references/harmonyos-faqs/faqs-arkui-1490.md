---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1490
title: 应用开启智慧多窗时底部导航栏缺失
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 应用开启智慧多窗时底部导航栏缺失
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:b0ac015a348e077f54824349b4fce2532287441b261cb843946c6df5ea075daf
---

## 问题现象

在启用智慧多窗功能后，应用底部导航栏未能正常显示。

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/_eLkn_hTRQ-pW0R3nFrxbg/zh-cn_image_0000002639596616.png "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/H3LiML3vR9OFe_px9DaoYQ/zh-cn_image_0000002669796487.png "点击放大")

## 背景知识

[自适应延伸](../harmonyos-guides/arkts-layout-development-linear.md#自适应延伸)通过在内容超出屏幕时启用滚动条实现拖动展示，常见方法包括为长列表添加滚动条和使用Scroll组件包裹线性布局以支持垂直或水平滚动。

智慧多窗开启方式参考[分屏的触发方式](../harmonyos-guides/multi-window-intro.md#分屏的触发方式)。

## 问题定位

开启智慧多窗后，当前页面内容超出屏幕大小导致无法完全显示。

## 分析结论

通过在Column组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。

## 修改建议

推荐参考[选项卡示例代码](../harmonyos-guides/arkts-navigation-tabs.md#示例代码)中提供的[常见Tab导航样式合集](https://gitee.com/harmonyos_samples/multi-tab-navigation)，使用Tabs组件布局指南Demo的[BottomTab.ets](https://gitee.com/harmonyos_samples/multi-tab-navigation/blob/master/entry/src/main/ets/pages/BottomTab.ets)实现底部导航栏。修改后符合本场景代码如下：

```ts
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct BottomTabLayout {
  @State currentIndex: number = 0;
  private tabsController: TabsController = new TabsController();

  @Builder
  tabBuilder(title: ResourceStr, index: number) {
    Column() {
      Image($r('app.media.startIcon'))
        .width(24)
        .height(24)
        .objectFit(ImageFit.Contain);

      Text(title)
        .margin({ top: 4 })
        .fontColor(this.currentIndex === index ? '#0a59f7' : '#8e8e8f');
    }
    .justifyContent(FlexAlign.Center)
    .height(52)
    .padding(6)
    .width('100%')
    .onClick(() => {
      this.currentIndex = index;
      this.tabsController.changeIndex(this.currentIndex);
    });
  }

  @Builder
  tabContentBuilder(text: ResourceStr, index: number) {
    TabContent() {
      Column() {
        Column() {
          Text('标题')
            .fontSize(20);
        }
        .width('100%')
        .alignItems(HorizontalAlign.Start)
        .padding(15);

        Scroll() {
          Column() {
            Text(text)
              .height(300)
              .fontSize(30);
          }
          .justifyContent(FlexAlign.Center)
          .height(700)
          .width('100%');
        }
        .layoutWeight(1)
        .scrollBar(BarState.Off);
      }
      .width('100%')
      .height('100%');
    }
    .height('100%')
    .padding({ left: 12, right: 12 })
    .backgroundColor(Color.White)
    .tabBar(this.tabBuilder(text, index));
  }

  build() {
    Tabs({
      barPosition: BarPosition.End,
      controller: this.tabsController
    }) {
      this.tabContentBuilder('Tab', 0);
      this.tabContentBuilder('Tab', 1);
      this.tabContentBuilder('Tab', 2);
    }
    .width('100%')
    .backgroundColor('#F3F4F5')
    .barHeight(52)
    .barMode(BarMode.Fixed)
    .onAnimationStart((index: number, targetIndex: number) => {
      hilog.info(0x0000, 'index', index.toString());
      this.currentIndex = targetIndex;
    });
  }
}
```

如需使用Swiper实现该效果，请参考以下示例代码：

```ts
import { display } from '@kit.ArkUI';

@Entry
@Component
struct SwiperBottomTab {
  private swiperController: SwiperController = new SwiperController();
  private data: string[] = [];
  @State selectIndex: number = 0;

  aboutToAppear(): void {
    let list: string[] = [];
    for (let i = 1; i < 4; i++) {
      list.push(i.toString());
    }
    this.data = list;
  }

  build() {
    Column() {
      Scroll() { // 添加Scroll来实现可滑动的线性布局
        Column() {
          Column() {
            Text('标题')
              .fontSize(20);
          }
          .width('100%')
          .alignItems(HorizontalAlign.Start)
          .padding(15);

          Swiper(this.swiperController) {
            ForEach(this.data, (item: string) => {
              Text(item.toString())
                .width('100%')
                .textAlign(TextAlign.Center)
                .fontSize(30);
            }, (item: string) => item);
          }
          .autoPlay(false)
          .indicator(false)
          .loop(false)
          .disableSwipe(false) // 禁用组件滑动切换功能。设置为true禁用，false不禁用。
          .height((display.getDefaultDisplaySync().height * 0.88 - 100) + 'px')
          .index(this.selectIndex)
          .onChange((index) => {
            this.selectIndex = index;
          });
        }
        .width('100%');
      }
      .layoutWeight(1)
      .scrollBar(BarState.Off);

      Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        ForEach(['Tab', 'Tab', 'Tab'], (item: string, index) => {
          Column({ space: 10 }) {
            Image($r('app.media.startIcon'))
              .width(24)
              .aspectRatio(1);

            Text(item)
              .fontSize(16)
              .fontColor(this.selectIndex === index ? '#0a59f7' : '#8e8e90');
          }
          .onClick(() => {
            this.selectIndex = index;
          });
        }, (item: string, index) => item + index);
      }
      .width('100%');
    };
  }
}
```
