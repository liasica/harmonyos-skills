---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-529
title: 进入页面后，页面自动滑动
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 进入页面后，页面自动滑动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:48d6afb56ddb13312635b2479fa96c7d57078a5961158d33a57a00cef1ca7ec7
---

## 问题现象

应用跳转到新的页面时，页面开始移动（页面没受到触碰）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/i44HPNlfTmuz6piHyr_pxw/zh-cn_image_0000002628551062.png "点击放大")

## 背景知识

* [Scroll](../harmonyos-references/ts-container-scroll.md)为可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
* 设置[fling](../harmonyos-references/ts-container-scroll.md#fling12)属性时，滚动类组件根据传入的初始速度进行惯性滚动。

## 问题定位

1. 使用DevEco Testing查看问题组件，该组件为Scroll组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/3WyKNVzZSqqFb9NFbRDASA/zh-cn_image_0000002658910379.png "点击放大")
2. 查看该组件的设置，该组件设置了fling属性，且值不为0，进入页面时会有向下滚动的初速度。

   ```screen
   Scroll(this.scroller) {
     // 列表组件
   }
   .onAppear(() => {
     setTimeout(() => {
       this.scroller.fling(-100); // 设置了fling属性，且值不为0
     }, 500);
   })
   ```

## 分析结论

Scroll组件设置了fling属性，且值不为0，进入页面时会有向下滚动的初速度，导致跳转到新页面时会自动滑动。

## 修改建议

Scroll组件不设置fling属性。

```screen
@Entry
@Component
struct Index {
  pageInfos: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.pageInfos) {
      Stack() {
        Button('点击跳转')
          .backgroundColor('#0A59F7')
          .fontColor(Color.White)
          .borderRadius('50%')
          .width(130)
          .height(50)
          .onClick(() => {
            this.pageInfos.pushPath({ name: 'Scroll' }); // 跳转到新页面
          });
      }
      .height('100%')
      .width('100%');
    }
    .hideTitleBar(true)
    .height('100%')
    .width('100%')
    .mode(NavigationMode.Stack);
  }
}
```

跳转后的页面src/main/ets/pages/ScrollPage.ets：

```screen
import { common } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

@Builder
export function ScrollPageBuilder() {
  ScrollPage();
}

@Entry
@Component
struct ScrollPage {
  pageInfos: NavPathStack = new NavPathStack();
  private scroller = new Scroller();
  @State arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  build() {
    NavDestination() {
      Scroll(this.scroller) {
        Column({ space: 10 }) {
          ForEach(this.arr, (item: number) => {
            Text(item.toString())
              .width('90%')
              .height(150)
              .backgroundColor('#f1f3f5')
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center);
          });
        }
        .width('100%');
      }
      // 不设置fling属性
      .scrollBar(BarState.Off)
      .friction(0.1)
    }
    .onBackPressed(() => {
      this.pageInfos.pop(); // 弹出路由栈栈顶元素
      return true;
    })
    .onReady((navContext: NavDestinationContext) => {
      this.pageInfos = navContext.pathStack;
      let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
      window.getLastWindow(context).then((lastWindow) => {
        lastWindow.setWindowLayoutFullScreen(true);
      });
    })
    .hideTitleBar(true)
    .height('100%')
    .width('100%')
    .padding({ top: '123px' })
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
  }
}
```

src/main/resources/base/profile/router\_map.json：

```screen
{
  "routerMap": [
    {
      "name": "Scroll",
      "pageSourceFile": "src/main/ets/pages/ScrollPage.ets",
      "buildFunction": "ScrollPageBuilder"
    }
  ]
}
```

src/main/module.json5文件中需添加"routerMap": "$profile:router\_map"。

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/g-e6H3E7TxeTmxTOO85Z0g/zh-cn_image_0000002628391174.png "点击放大")
