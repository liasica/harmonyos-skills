---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-windmana-troubleshooting-0002
title: 切换智慧多窗模式后页面内容遮挡如何排查
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 故障排查 > 切换智慧多窗模式后页面内容遮挡如何排查
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:06+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:0e15a7ce6dda0481151a44d96f121ac3c5811a94958cf046890a02210352cfc0
---

## 平板悬浮窗模式下，组件存在遮挡问题现象

### 问题现象

应用切换到悬浮窗模式时，按钮组件遮挡底部布局，导致内容看不清。

### 定位过程

建议检查应用布局是否使用自适应布局中具有延伸能力的组件，如Scroll、List等，当使用这些容器组件时，页面尺寸缩小后，页面内容可以延伸放置在底部，通过滑动来完整显示整个页面避免遮挡。

### 分析结论

应用未使用具有延伸能力的滚动容器布局，导致窗口尺寸缩小时，原页面底部的内容遮挡了页面内容。

### 修改建议

对应小屏状态下内容展示，推荐使用具有延伸能力的滚动容器布局。

```ts
@Entry
@Component
struct ExtensionCapability2 {
  private appList: number [] = [0, 1, 2, 3, 4, 5, 6, 7];

  build() {
    Row() {
      Row({ space: 10 }) {
        // 使用list可延伸组件
        List({ space: 10 }) {
          ForEach(this.appList, () => {
            ListItem() {
              Column() {
                Image($r('app.media.startIcon'))
                  .width(48)
                  .height(48)
                  .margin({ top: 8 });
                Text('appName')
                  .width(64)
                  .height(30)
                  .lineHeight(15)
                  .fontSize(12)
                  .textAlign(TextAlign.Center)
                  .margin({ top: 8 })
                  .padding({ bottom: 15 });
              }
              .width(80)
              .height(102);
            }
            .width(80)
            .height(102);
          }, (item: number, index: number) => JSON.stringify(item) + index);
        }
        .padding({ top: 16, left: 10 })
        .listDirection(Axis.Horizontal)
        .width('100%')
        .height(118)
        .borderRadius(16)
        .backgroundColor(Color.White);
      }
      .width('60%');
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(VerticalAlign.Center);
  }
}
```

## 应用分屏模式下，页面不可滑动，底部内容无法查看

### 问题现象

应用分屏模式下，页面无法滑动，部分内容在底部显示不全，无法查看。

### 定位过程

1. 检查代码，查看被截断页面是否未设置宽高，只定义了内部内容高度，外容器由内部内容撑开。
2. 检查代码，查看被截断页面布局是否使用了具有延伸能力的容器组件包裹，例如List组件，Scroll组件。

### 分析结论

应用截断页面只适配了全屏大小，当应用分屏后，窗口会变小，导致页面显示不全，超出窗口的区域无法显示，而页面未使用具有延伸能力的容器组件包裹，导致页面也无法滑动查看超出的部分。

### 修改建议

使用具有延伸能力的容器组件包裹。以下是使用Scroll组件，让列表或者文字区域可以按照指定方向滑动的示例：

```ts
@Entry
@Component
struct ScrollExampleDemo {
  private arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  scroller: Scroller = new Scroller();

  build() {
    Flex() {
      Column() {
        Text("Scroll Area")
          .width("100%")
          .height('40%')
          .backgroundColor('#D1D1D6')
          .fontSize(16)
          .textAlign(TextAlign.Center);

        Scroll(this.scroller) {
          Column() {
            ForEach(this.arr, (item: number) => {
              Text("ListItem" + item)
                .width("100%")
                .height(150)
                .borderRadius(15)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .backgroundColor(Color.White);
            }, (item: string) => item);
          }
          .width('100%');
        }
        .width("100%")
        .height(200);

        Text("Scroll Area")
          .width("100%")
          .height('40%')
          .backgroundColor('#D1D1D6')
          .fontSize(16)
          .textAlign(TextAlign.Center);
      };
    }
    .width("100%").height("100%");
  }
}
```
