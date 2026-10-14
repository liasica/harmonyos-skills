---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-troubleshooting-0001
title: ArkUI一多适配布局问题定位
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 故障排查 > ArkUI一多适配布局问题定位
category: harmonyos-faqs
scraped_at: 2026-10-15T07:14:32+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:967cf2a96e70d420d9ae18321c781f9ed0a845176f9c59fe7dc6f0670017aff9
---

## 平板竖屏场景，底部组件位置错乱

### 问题现象

平板竖屏场景，切换到异常页面时底部组件位置突变，且覆盖了其他组件。

### 定位过程

1. 若使用position给组件设置了绝对定位，在平板为竖屏时由于屏幕位置改变导致定位错误出现组件位置错乱的现象。检查异常页面是否使用了绝对定位。

   ```ts
   Row() {
     Text('2 position(30, 10)')
       .size({ width: '60%', height: '30' })
       .backgroundColor(0xbbb2cb)
       .border({ width: 1 })
       .fontSize(16)
       .align(Alignment.Start)
       .position({ x: 30, y: 10 })
     Text('4 position(50%, 70%)')
       .size({ width: '50%', height: '50' })
       .backgroundColor(0xbbb2cb)
       .border({ width: 1 })
       .fontSize(16)
       .position({ x: '50%', y: '70%' })
   }
   .width('90%')
   .height(100)
   .border({ width: 1, style: BorderStyle.Dashed })
   ```
2. 若使用Stack布局会导致组件覆盖。Stack层叠布局会优先显示最上层的组件，检查异常页面是否是Stack布局。

   ```ts
   Stack({ alignContent: Alignment.TopStart }) {
     Scroll() {
       Column() {
         // ...
       }
     }
     .zIndex(0)

     Button('结算').onClick((event: ClickEvent) => {
       // ...
     })
     .zIndex(1)
   }
   .margin({ top: 25 })
   .border({ width: 1, style: BorderStyle.Dashed })
   ```

### 分析结论

Stack布局导致组件覆盖，position绝对定位导致组件位置错乱。

### 修改建议

不同屏幕尺寸下绝对定位的适配性差，建议优先使用[Flex](../harmonyos-references/ts-universal-attributes-flex-layout.md)等响应式布局替代。以购物页面为例，简单的购物页面一般为Scroll包含的商品列表和底部结算按钮，可以将这两个组件放在同一图层，并给Scroll设置一个百分比高度，这样按钮组件默认会在Scroll底部显示，避免使用绝对定位。

```ts
@Entry
@Component
struct ShoppingPage {
  numArr: number[] = [];

  aboutToAppear(): void {
    for (let i = 0; i < 100; i++) {
      this.numArr.push(i);
    }
  }

  build() {
    Column() {
      Scroll() {
        Column({ space: 5 }) {
          ForEach(this.numArr, (item: number) => {
            Text(item.toString())
              .fontColor(Color.Black)
              .fontSize(20)
              .width('95%')
              .height('20%')
              .textAlign(TextAlign.Center)
              .backgroundColor('#f1f3f5');
          });
        }
        .width('100%')
        .justifyContent(FlexAlign.Center);
      }
      .expandSafeArea([SafeAreaType.SYSTEM])
      .height('90%')
      .scrollBar(BarState.Off)
      .scrollable(ScrollDirection.Vertical);

      Row({ space: 10 }) {
        Row({ space: 10 }) {
          Column() {

          }
          .width('30%')
          .height('100%')
          .backgroundColor('#f1f3f5');

          Column({ space: 5 }) {
            Row() {

            }
            .width('60%')
            .height('40%')
            .backgroundColor('#f1f3f5');

            Row() {

            }
            .width('60%')
            .height('40%')
            .backgroundColor('#f1f3f5');
          }
          .justifyContent(FlexAlign.Center);
        }
        .layoutWeight(1);

        Text('结算')
          .backgroundColor('#0A59F7')
          .fontColor(Color.White)
          .textAlign(TextAlign.Center)
          .width(100)
          .height(50)
          .borderRadius(25)
          .margin(10)
          .onClick(() => {
            // ...
          });
      }
      .width('95%')
      .layoutWeight(1)
      .margin({ top: 5 })
      .alignItems(VerticalAlign.Center)
      .justifyContent(FlexAlign.SpaceBetween);
    };
  }
}
```

## 平板打开应用，部分组件不可见

### 问题现象

对比手机，平板打开相同应用，因应用未适配多端设备，导致部分组件不可见。

### 定位过程

1. 使用UIView查看平板上的页面布局，可见组件存在，只是挤压到了屏幕之外。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/HuANnfiVSz6m1LhjPh0w_Q/zh-cn_image_0000002760004412.png "点击放大")
2. 检查页面的相关组件的尺寸属性是否设置成了固定值。

### 分析结论

平板上页面内的组件并没有消失，只是组件的尺寸设置成了固定值，未能适配平板的屏幕尺寸，显示在了屏幕之外。

### 修改建议

可采用自适应布局的方式设置组件尺寸和位置属性，例如此例中可通过自适应缩放中的占比能力保证组件能够正常的显示，例如下面代码。

```ts
@Entry
@Component
struct ViewHidingIssueDemo {
  build() {
    Column() {
      Row() {
        Text('不同意，退出')
          .textAlign(TextAlign.Center)
          .width('50%')
        Divider()
          .vertical(true)
        Text('同意')
          .width('50%')
          .textAlign(TextAlign.Center)
      }
      .width('100%')
      .height('20%')
      .backgroundColor(Color.Gray)
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}
```

## 折叠屏，页面底部页签与导航栏间空白过大

### 问题现象

使用折叠屏打开应用，页面底部页签与导航栏之间空白过大。

### 定位过程

查阅页面代码中，根组件是否设置padding属性，以及该属性内bottom字段的值。

### 分析结论

页面代码中，根组件padding属性的bottom字段设置的下边距过大，导致页面底部页签距离导航栏过远。

### 修改建议

通过on('avoidAreaChange')接口监听系统规避区域的变化，使用getWindowAvoidArea接口实时获取系统规避区域的高度，将实时的导航栏高度赋值给根组件的padding属性，避免padding数值过大产生空白的问题，代码如下：

```ts
import { common } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct BottomRectDemo {
  @State bottomRect: number = 0;

  aboutToAppear(): void {
    const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let windowStage: window.WindowStage = context.windowStage;
    let windowClass: window.Window = windowStage.getMainWindowSync();
    // 初始化获得导航栏区域高度
    this.bottomRect = windowClass.getWindowAvoidArea(window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR).bottomRect.height;
    // 监听系统规避区域的变化，动态获取状态栏区域和导航栏区域
    windowClass.on('avoidAreaChange', () => {
      this.bottomRect =
        windowClass.getWindowAvoidArea(window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR).bottomRect.height;
    });
  }

  build() {
    Column() {
      Text(`测试页面具体底部导航条的距离: ${this.bottomRect}`);
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#D1D1D6')
    // 将导航栏的高度赋值给根组件的padding属性
    .padding({
      bottom: this.getUIContext().px2vp(this.bottomRect)
    });
  }
}
```
