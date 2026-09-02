---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-763
title: 如何添加并且动态修改全局水印
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何添加并且动态修改全局水印
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-08-20
content_hash: sha256:8c0c08003d57d0e0d66bf7554fd111fc60336df841316ee84a602be83192bb2c
---

## 问题现象

在HarmonyOS开发中如何添加全局水印，动态控制水印的展示与隐藏，并且能够修改水印内容使每个页面的水印内容不同？

## 背景知识

* [overlay](../harmonyos-references/ts-universal-attributes-overlay.md#overlay)：在当前组件上，增加遮罩文本或者叠加自定义组件以及ComponentContent作为该组件的浮层。
* [hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)：设置组件的触摸测试类型。
* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)：Navigation组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)的子组件）或非首页显示（NavDestination的子组件），首页和非首页通过路由进行切换。
* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)：提供画布组件，用于自定义绘制图形。

## 解决方案

* 场景一：页面需要统一添加全局水印内容，请参考官方示例[页面上添加水印](../best-practices/bpta-add-watermark.md#section12388834480)。
* 场景二：页面需要自定义各个页面的水印内容，可在场景一的方案中稍作改动，在目标页面自定义watermarkBuilder函数并将公共水印方法传入，根据需要传入不同参数可实现不同的显示内容，同时设置其触摸测试类型为None或Transparent，否则正常组件无法响应事件。

  在需要添加水印页面的根节点上设置overlay属性，并配置watermarkBuilder可实现添加全局水印效果。设置一个按钮通过[@State装饰器](../harmonyos-guides/arkts-state.md)声明一个状态变量可动态控制水印的显示与隐藏。详情请参考如下代码：

  ```ts
  // Index.ets
  import { WaterMark} from '../pages/WaterMark';

  @Builder
  // 传入不同参数显示不同内容
  export function watermarkBuilder(watermarkText = '', rotationAngle = -10,
    fillColor: string | number | CanvasGradient | CanvasPattern = '#99158ef3', font = '16vp') {
    Column() {
      WaterMark({
        watermarkText: watermarkText,
        rotationAngle: rotationAngle,
        fillColor: fillColor,
        font: font
      });
    }.hitTestBehavior(HitTestMode.Transparent) // 添加浮层并配置公共水印方法
  }

  @Entry
  @Component
  struct waterOver {
    @State text: string = '';
    @State state: Boolean = true;

    aboutToAppear(): void {
      setInterval(() => {
        this.text += '_+';
      }, 500);
    };

    build() {
      Column() {
        Button('跳转其他页面')
          .margin({ bottom: 100 })
          .onClick(() => {
            this.getUIContext().getRouter().pushUrl({
              url: 'pages/PageSecond',
            });
          });
        Button('显示隐藏')
          .onClick(() => {
            // 通过state状态变量控制水印的显示和隐藏
            this.state = !this.state;
          });
      }
      .overlay(this.state ? watermarkBuilder(this.text) : undefined) // 添加浮层并配置公共水印方法
      .width('100%');
    }
  }
  ```

  ```ts
  // 其他页面
  import { WaterMark } from '../pages/WaterMark';

  @Builder
  // 传入不同参数显示不同内容
  export function watermarkBuilder(watermarkText = '', rotationAngle = -10,
    fillColor: string | number | CanvasGradient | CanvasPattern = '#9937470c', font = '16vp') {
    Column() {
      WaterMark({
        watermarkText: watermarkText,
        rotationAngle: rotationAngle,
        fillColor: fillColor,
        font: font
      });
    }.hitTestBehavior(HitTestMode.Transparent)
  };

  @Entry
  @Component
  struct waterOver {
    @State text: string = '';

    aboutToAppear(): void {
      setInterval(() => {
        this.text = '水印';
      }, 500);
    };

    build() {
      Column() {
        Button('其他页面')
      }
      .width('100%')
      .height('100%')
      .overlay(watermarkBuilder(this.text))
    };
  };
  ```

  ```ts
  // 自定义水印公共方法
  @Entry
  @Component
  export struct WaterMark {
    @Prop watermarkWidth: number = 120;
    @Prop watermarkHeight: number = 120;
    @Prop watermarkText: string = '0000-2025-01-01';
    @Prop rotationAngle: number = -30;
    @Prop fillColor: string | number | CanvasGradient | CanvasPattern = '#10000000';
    @Prop font: string = '16vp';
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

    build() {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .hitTestBehavior(HitTestMode.Transparent)
        .onReady(() => this.draw());
    };

    draw() {
      this.context.fillStyle = this.fillColor;
      this.context.font = this.font;
      const colCount = Math.ceil(this.context.width / this.watermarkWidth);
      const rowCount = Math.ceil(this.context.height / this.watermarkHeight);
      for (let col = 0; col <= colCount; col++) {
        let row = 0;
        for (; row <= rowCount; row++) {
          const angle = this.rotationAngle * Math.PI / 180;
          this.context.rotate(angle);
          const positionX = this.rotationAngle > 0 ? this.watermarkHeight * Math.tan(angle) : 0;
          const positionY = this.rotationAngle > 0 ? 0 : this.watermarkWidth * Math.tan(-angle);
          this.context.fillText(this.watermarkText, positionX, positionY);
          this.context.rotate(-angle);
          this.context.translate(0, this.watermarkHeight);
        };
        this.context.translate(0, -this.watermarkHeight * row);
        this.context.translate(this.watermarkWidth, 0);
      };
    };
  };
  ```

  场景二效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/kqOKdwflTXyOWl_qrZPVlg/zh-cn_image_0000002712944509.png "点击放大")
* 场景三：页面使用了Navigation布局想实现添加全局水印，可使用透明背景的Canvas画布绘制文字水印，再使用[Stack](../harmonyos-references/ts-container-stack.md)组件叠加在Navigation组件上即可。详情请参考如下代码：

  ```ts
  import { SymbolGlyphModifier } from '@kit.ArkUI';

  @Component
  struct MyPageOne {
    private listScroller: Scroller = new Scroller();
    private scrollScroller: Scroller = new Scroller();
    private arr: number[] = [];

    aboutToAppear(): void {
      for (let i = 0; i < 5; i++) {
        this.arr.push(i);
      }
    }

    build() {
      NavDestination() {
        Column() {
          Scroll(this.scrollScroller) {
            Column() {
              List({ space: 0, initialIndex: 0, scroller: this.listScroller }) {
                ForEach(this.arr, (item: number) => {
                  ListItem() {
                    Text('' + item)
                      .height(100)
                      .fontSize(16)
                      .textAlign(TextAlign.Center)
                      .width('90%')
                      .margin({ left: '5%', top:'5%' })
                      .borderRadius(15)
                      .backgroundColor('#e5e5ea');
                  };
                }, (item: string) => item);
              }.width('100%').scrollBar(BarState.Off)
              .height('90%')
              .margin(80)
              .nestedScroll({ scrollForward: NestedScrollMode.SELF_FIRST, scrollBackward: NestedScrollMode.SELF_FIRST });
            }
          }
          .width('100%')
          .scrollBar(BarState.Off)
          .scrollable(ScrollDirection.Vertical)
          .edgeEffect(EdgeEffect.Spring);
        }
      }
      // .height('100%')
      .title('PageOne', { backgroundColor: '#f1f3f5', barStyle: BarStyle.STACK })
      .toolbarConfiguration([
        {
          value: 'item1',
          symbolIcon: new SymbolGlyphModifier($r('sys.symbol.phone_badge_star'))
        }
      ], { backgroundColor: '#f1f3f5', barStyle: BarStyle.STACK })
      // 绑定有父子关系的可滚动容器组件
      .bindToNestedScrollable([{ parent: this.scrollScroller, child: this.listScroller }]);
    }
  }

  @Component
  struct MyPageTwo {
    private listScroller: Scroller = new Scroller();
    private arr: number[] = [];

    aboutToAppear(): void {
      for (let i = 0; i < 5; i++) {
        this.arr.push(i);
      }
    }

    build() {
      NavDestination() {
        List({ scroller: this.listScroller }) {
          ForEach(this.arr, (item: number) => {
            ListItem() {
              Text('' + item)
                .height(100)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .width('90%')
                .borderRadius(15)
                .backgroundColor('#e5e5ea')
                .margin({ left: '5%', top: '5%' });
            };
          }, (item: string) => item);
        }
        .margin(80)
        .width('100%');
      }

      .title('PageTwo', { backgroundColor: '#f1f3f5', barStyle: BarStyle.STACK })
      .toolbarConfiguration([
        {
          value: 'item1',
          symbolIcon: new SymbolGlyphModifier($r('sys.symbol.phone_badge_star'))
        }
      ],
        { backgroundColor: '#f1f3f5', barStyle: BarStyle.STACK })
      // 绑定可滚动容器组件
      .bindToScrollable([this.listScroller]);
    }
  }

  @Entry
  @Component
  struct Index {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
    private stack: NavPathStack = new NavPathStack();

    @Builder
    MyPageMap(name: string) {
      if (name === 'myPageTwo') {
        MyPageTwo();
      } else {
        MyPageOne();
      }
    }

    build() {
      Stack({ alignContent: Alignment.Center }) {
        Navigation(this.stack) {
          Column() {

            Button('push PageOne')
              .onClick(() => {
                this.stack.pushPath({ name: 'myPageOne' });
              });

            Button('push PageTwo')
              .margin({ top: 20 })
              .onClick(() => {
                this.stack.pushPath({ name: 'myPageTwo' });
              });
          }
          .padding({ top: '35%' })
          .height('45%').justifyContent(FlexAlign.SpaceAround);
        }
        .width('100%')
        .height('100%')
        .title({ main: 'MainTitle', sub: 'subTitle' })
        .navDestination(this.MyPageMap)
        .backgroundColor('rgba(128, 243, 245, 1.00)')
        .mode(NavigationMode.Auto)
        .mode(NavigationMode.Stack)
        .backgroundColor('rgba(200,200,200,0.4)');

        Canvas(this.context)
          .width('100%')
          .height('100%')
          .hitTestBehavior(HitTestMode.Transparent)
          .onReady(() => {
            this.context.fillStyle = '#10000000';
            this.context.font = '16vp';
            this.context.textAlign = 'center';
            this.context.textBaseline = 'middle';
            // 在这里绘制文字水印，也可以是图片水印
            for (let i = 0; i < this.context.width / 120; i++) {
              this.context.translate(120, 0);
              let j = 0;
              for (; j < this.context.height / 120; j++) {
                this.context.rotate(-Math.PI / 180 * 30);
                // 此处水印数据是写死的，具体请替换为自己的水印
                this.context.fillText('水印水印', -60, -60);
                this.context.rotate(Math.PI / 180 * 30);
                this.context.translate(0, 120);
              }
              this.context.translate(0, -120 * j);
            }
          });
      };
    }
  }
  ```

  场景三效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/R4n-AViIQDavjG16UNLMyQ/zh-cn_image_0000002712945851.png "点击放大")

## 常见FAQ

Q：实现了水印效果后，但是发现有些页面点击不了了。

A：overlay会将浮层组件覆盖在所绑定的组件上方，阻塞用户对浮层下方组件的所有交互操作。若需用户可操作下方组件，应参照示例[（通过builder设置浮层）](../harmonyos-references/ts-universal-attributes-overlay.md#示例2通过builder设置浮层)中的实现，在浮层builder的最外层组件上配置.hitTestBehavior(HitTestMode.Transparent)。

## 总结

| 场景 | 适用场景内容 |
| --- | --- |
| 场景一 | 统一添加所有页面的水印内容 |
| 场景二 | 可以自定义各个页面的水印内容 |
| 场景三 | 使用Navigation布局，设置全局水印 |
