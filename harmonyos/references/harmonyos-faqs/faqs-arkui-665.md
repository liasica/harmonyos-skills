---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-665
title: 平板悬浮窗模式下，组件存在遮挡
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 平板悬浮窗模式下，组件存在遮挡
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:3b78b8d3863911f9a1407f64b16bece04111271de6bb37ecd545406debc611e2
---

## 问题现象

应用切换到悬浮窗模式时，按钮组件遮挡底部布局，导致内容看不清。

## 背景知识

[悬浮窗](../harmonyos-guides/multi-window-intro.md#悬浮窗)：悬浮窗是一种在设备屏幕上悬浮的非全屏应用窗口。当应用进入智慧多窗模式时，应用的窗口尺寸发生变化，所以应用需要根据不同的窗口尺寸调整自身布局。

## 问题定位

建议检查应用布局是否使用自适应布局中具有延伸能力的组件，如Scroll、List等，当使用这些容器组件时，页面尺寸缩小后，页面内容可以延伸放置在底部，通过滑动来完整显示整个页面避免遮挡。

## 分析结论

应用未使用具有延伸能力的滚动容器布局，导致窗口尺寸缩小时，原页面底部的内容遮挡了页面内容。

## 修改建议

对应小屏状态下内容展示，推荐使用具有延伸能力的滚动容器布局。

```screen
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
