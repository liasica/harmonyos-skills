---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-853
title: 列表左右滑动时表头与列表内容未整体双向同步滑动
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 列表左右滑动时表头与列表内容未整体双向同步滑动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c811df553e02817be52da1b5f699fb4e6e85f3eca0b7ef07326fb49a241af5f8
---

## 问题现象

滑动列表内容时，表头内容跟随列表滑动，滑动表头时，列表内容未跟随表头滑动。

## 背景知识

* [Scroll](../harmonyos-references/ts-container-scroll.md)：可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
* [ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md)：该组件用来展示列表item分组，宽度默认充满List组件，必须配合List组件来使用。
* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)：滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件。

## 问题定位

* 排查应用中是否使用[ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md)组件结合[Scroll](../harmonyos-references/ts-container-scroll.md)组件实现表头和列表内容的同步滑动。
* 排查应用中的列表是否使用[scrollTo](../harmonyos-references/ts-container-scroll.md#scrollto)接口实时监听表头的滑动距离实现表头和列表内容的同步滑动。

## 分析结论

* 应用中未使用ListItemGroup组件结合Scroll组件实现同步滑动效果。
* 应用列表内容未使用[scrollTo](../harmonyos-references/ts-container-scroll.md#scrollto)接口实时监听列表内容的滑动距离，实现同步滑动。

## 修改建议

* 通过[ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md)组件和[Scroll](../harmonyos-references/ts-container-scroll.md)组件构建页面布局，结合PanGesture手势滑动事件实现滑动效果。

  ```screen
  @Entry
  @Component
  struct ScrollExample {
    private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Left | PanDirection.Right });
    @Provide offsetX: number | undefined = undefined;

    aboutToAppear(): void {
      let windowClass: window.Window | undefined = undefined;
      window.getLastWindow(this.getUIContext()?.getHostContext(), (err: BusinessError, data) => {
        windowClass = data;
        let SystemBarProperties: window.SystemBarProperties = {
          statusBarColor: '#F1F3F5',
          navigationBarColor: '#000'
        };
        try {
          let promise = windowClass.setWindowSystemBarProperties(SystemBarProperties);
          promise.then(() => {
            console.info('Succeeded in setting the system bar properties.');
          }).catch((err: BusinessError) => {
            console.error(`Failed to set the system bar properties. Cause code: ${err.code}, message: ${err.message}`);
          });
        } catch (exception) {
          console.error(`Failed to set the system bar properties. Cause code: ${exception.code}, message: ${exception.message}`);
        }
      });

    }

    build() {
      Column() {
        Column() {
          MainArea();
        }

        .backgroundColor('#fff')
        .padding(12)
        .gesture(
          // 用于触发拖动手势事件，滑动的最小距离为5vp时拖动手势识别成功。
          PanGesture(this.panOption).onActionStart((event?: GestureEvent) => {
            this.offsetX = event?.offsetX;
            console.info('gesture11: PanGesture start' + event?.offsetX);
          })
        )
        .borderRadius(24);
      }
      .height('100%')
      .width('100%')
      .padding(10)
      .backgroundColor('#F1F3F5')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM]);
    }
  }

  @Component
  struct tableRow {
    @Prop infos: IndustryInfo;

    build() {
      Flex({ alignItems: ItemAlign.Center }) {
        Text(this.infos.industryName).fontSize(16).width(86).textAlign(TextAlign.Start);
        ScrollComponent({ stock: this.infos.datas });
      }.width('100%');
    }
  }

  @Component
  struct ScrollComponent {
    scroller: Scroller = new Scroller();
    @Prop stock: StocksInfo;
    @Consume @Watch('onCountUpdated') offsetX: number;

    // 监听滑动距离
    onCountUpdated() {
      if (this.offsetX) {
        this.scroller.scrollTo({
          xOffset: this.scroller.currentOffset()?.xOffset - this.offsetX * 50, // 滑动距离可根据实际情况设置
          yOffset: 0,
          animation: { duration: 1000, curve: Curve.Ease }
        });
      }
    }

    build() {
      Scroll(this.scroller) {
        Row() {
          Text(this.stock.increase).fontSize(16).width(86).textAlign(TextAlign.Center);
          Text(this.stock.limit + '').fontSize(16).width(86).textAlign(TextAlign.Center);
          Text(this.stock.score + '').fontSize(16).width(86).textAlign(TextAlign.Center);
          Text(this.stock.buy).fontSize(16).width(86).textAlign(TextAlign.Center);
          Text(this.stock.funds).fontSize(16).width(86).textAlign(TextAlign.Center);
          Text(this.stock.quantity).fontSize(16).width(86).textAlign(TextAlign.Center);
          Text(this.stock.growth).fontSize(16).width(86).textAlign(TextAlign.Center);
          Text(this.stock.board + '').fontSize(16).width(86).textAlign(TextAlign.Center);
          Text(this.stock.leading + '').fontSize(16).width(86).textAlign(TextAlign.Center);
        }.padding({ top: 4, bottom: 4 });
      }
      .scrollable(ScrollDirection.Horizontal) // 滚动方向纵向
      .scrollBar(BarState.Off) // 滚动条常驻显示
      .edgeEffect(EdgeEffect.None)
      .width('100%')
      // 禁止scroll滚动
      .enabled(false);
    }
  }
  ```
* 通过给表头和列表内容添加[scrollTo](../harmonyos-references/ts-container-scroll.md#scrollto)接口实时监听列表的滑动距离，实现表头与列表内容的双向同步滑动。

  ```screen
  @Consume @Watch('onCountUpdated') offsetX: number;

  // 监听滑动距离
  onCountUpdated() {
    if (this.offsetX) {
      this.scroller.scrollTo({
        xOffset: this.scroller.currentOffset()?.xOffset - this.offsetX * 50, // 滑动距离可根据实际情况设置
        yOffset: 0,
        animation: { duration: 1000, curve: Curve.Ease }
      });
    }
  }
  ```

完整示例如下：

```screen
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

interface IndustryInfo {
  industryName: string;
  datas: StocksInfo;
}

interface StocksInfo {
  id: string;
  increase: string;
  limit: number;
  score: number;
  buy: string;
  funds: string;
  quantity: string;
  growth: string;
  board: number;
  leading: number;
}

@Entry
@Component
struct ScrollExample {
  private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Left | PanDirection.Right });
  @Provide offsetX: number | undefined = undefined;

  aboutToAppear(): void {
    let windowClass: window.Window | undefined = undefined;
    window.getLastWindow(this.getUIContext()?.getHostContext(), (err: BusinessError, data) => {
      windowClass = data;
      let SystemBarProperties: window.SystemBarProperties = {
        statusBarColor: '#F1F3F5',
        navigationBarColor: '#000'
      };
      try {
        let promise = windowClass.setWindowSystemBarProperties(SystemBarProperties);
        promise.then(() => {
          console.info('Succeeded in setting the system bar properties.');
        }).catch((err: BusinessError) => {
          console.error(`Failed to set the system bar properties. Cause code: ${err.code}, message: ${err.message}`);
        });
      } catch (exception) {
        console.error(`Failed to set the system bar properties. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });

  }

  build() {
    Column() {
      Column() {
        MainArea();
      }

      .backgroundColor('#fff')
      .padding(12)
      .gesture(
        // 用于触发拖动手势事件，滑动的最小距离为5vp时拖动手势识别成功。
        PanGesture(this.panOption).onActionStart((event?: GestureEvent) => {
          this.offsetX = event?.offsetX;
          console.info('gesture11: PanGesture start' + event?.offsetX);
        })
      )
      .borderRadius(24);
    }
    .height('100%')
    .width('100%')
    .padding(10)
    .backgroundColor('#F1F3F5')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM]);
  }
}

@Component
struct tableRow {
  @Prop infos: IndustryInfo;

  build() {
    Flex({ alignItems: ItemAlign.Center }) {
      Text(this.infos.industryName).fontSize(16).width(86).textAlign(TextAlign.Start);
      ScrollComponent({ stock: this.infos.datas });
    }.width('100%');
  }
}

@Component
struct ScrollComponent {
  scroller: Scroller = new Scroller();
  @Prop stock: StocksInfo;
  @Consume @Watch('onCountUpdated') offsetX: number;

  // 监听滑动距离
  onCountUpdated() {
    if (this.offsetX) {
      this.scroller.scrollTo({
        xOffset: this.scroller.currentOffset()?.xOffset - this.offsetX * 50, // 滑动距离可根据实际情况设置
        yOffset: 0,
        animation: { duration: 1000, curve: Curve.Ease }
      });
    }
  }

  build() {
    Scroll(this.scroller) {
      Row() {
        Text(this.stock.increase).fontSize(16).width(86).textAlign(TextAlign.Center);
        Text(this.stock.limit + '').fontSize(16).width(86).textAlign(TextAlign.Center);
        Text(this.stock.score + '').fontSize(16).width(86).textAlign(TextAlign.Center);
        Text(this.stock.buy).fontSize(16).width(86).textAlign(TextAlign.Center);
        Text(this.stock.funds).fontSize(16).width(86).textAlign(TextAlign.Center);
        Text(this.stock.quantity).fontSize(16).width(86).textAlign(TextAlign.Center);
        Text(this.stock.growth).fontSize(16).width(86).textAlign(TextAlign.Center);
        Text(this.stock.board + '').fontSize(16).width(86).textAlign(TextAlign.Center);
        Text(this.stock.leading + '').fontSize(16).width(86).textAlign(TextAlign.Center);
      }.padding({ top: 4, bottom: 4 });
    }
    .scrollable(ScrollDirection.Horizontal) // 滚动方向纵向
    .scrollBar(BarState.Off) // 滚动条常驻显示
    .edgeEffect(EdgeEffect.None)
    .width('100%')
    // 禁止scroll滚动
    .enabled(false);
  }
}

@Component
struct MainArea {
  private scroller: Scroller = new Scroller();
  private arr: IndustryInfo[] = [
    {
      industryName: '乳制品',
      datas: {
        id: '10001',
        increase: '5%',
        limit: 1,
        score: 49,
        buy: '1.01亿',
        funds: '1.60亿',
        quantity: '0.6%',
        growth: '2073万',
        board: 3,
        leading: 102
      }
    },
    {
      industryName: '啤酒',
      datas: {
        id: '10002',
        increase: '5%',
        limit: 1,
        score: 49,
        buy: '1.01亿',
        funds: '1.60亿',
        quantity: '0.6%',
        growth: '2073万',
        board: 3,
        leading: 102
      }
    },
    {
      industryName: '葡萄酒',
      datas: {
        id: '10003',
        increase: '5%',
        limit: 1,
        score: 49,
        buy: '1.01亿',
        funds: '1.60亿',
        quantity: '0.6%',
        growth: '2073万',
        board: 3,
        leading: 102
      }
    },
    {
      industryName: '白糖',
      datas: {
        id: '10004',
        increase: '5%',
        limit: 1,
        score: 49,
        buy: '1.01亿',
        funds: '1.60亿',
        quantity: '0.6%',
        growth: '2073万',
        board: 3,
        leading: 102
      }
    },
    {
      industryName: '无人配送',
      datas: {
        id: '10005',
        increase: '5%',
        limit: 1,
        score: 49,
        buy: '1.01亿',
        funds: '1.60亿',
        quantity: '0.6%',
        growth: '2073万',
        board: 3,
        leading: 102
      }
    }
  ];
  private settings: string[] = ['涨幅', '涨停数', 'AI得分', '主动净买', '主力资金', '量比', '涨速', '连板', '龙头股'];
  @Consume @Watch('onCountUpdated') offsetX: number;

  // 监听滑动距离
  onCountUpdated() {
    if (this.offsetX) {
      this.scroller.scrollTo({
        xOffset: this.scroller.currentOffset()?.xOffset - this.offsetX * 50, // 滑动距离可根据实际情况设置
        yOffset: 0,
        animation: { duration: 1000, curve: Curve.Ease }
      });
    }
  }

  // table header
  @Builder
  tabHeader() {
    Column() {
      Flex({ alignItems: ItemAlign.Center }) {
        Text('设置')
          .fontSize(16)
          .width(86)
          // .height(100)
          .padding({ bottom: 4 })
          .textAlign(TextAlign.Start);
        Scroll(this.scroller) {
          Row() {
            ForEach(this.settings, (setting: string) => {
              Text(setting)
                .fontSize(16)
                .width(86)
                .textAlign(TextAlign.Center);
            });
          };
        }
        .scrollable(ScrollDirection.Horizontal) // 滚动方向纵向
        .width('100%')
        .padding({ bottom: 4 })
        .scrollBar(BarState.Off) // 滚动条常驻显示
        .edgeEffect(EdgeEffect.None)
        // 禁止scroll滚动
        .enabled(false);
      }
      .padding(4);

      Divider()
        .strokeWidth(1)
        .width("100%")
        .color('#eee');
    }.width('100%');
  }

  build() {
    List() {
      ListItemGroup({ header: this.tabHeader() }) {
        ForEach(this.arr, (item: IndustryInfo, index: number) => {
          ListItem() {
            Column() {
              tableRow({ infos: item }).padding(4);
              if (index !== this.arr.length - 1) {
                Divider()
                  .strokeWidth(1)
                  .width("100%")
                  .color('#eee');
              }
            };
          };
        });
      };
    }.sticky(StickyStyle.Header);
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/l_Bkh0LtTn6hTqaOCj0V_A/zh-cn_image_0000002658917861.png "点击放大")
