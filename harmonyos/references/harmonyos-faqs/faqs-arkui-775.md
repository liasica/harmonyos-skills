---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-775
title: 如何设置半模态窗口高度自适应，同时自定义最高高度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何设置半模态窗口高度自适应，同时自定义最高高度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3b7093b39a78d0eb1e9c6caf9cd05a3118beedd770fb508d0be7ccf3b7b77b21
---

## 问题现象

bindSheet设置高度为SheetSize.FIT\_CONTENT自适应内容高度时，半模态页面限高只能为系统设定的值，无法自定义。如何根据半模态页面内容去设置高度，同时要求最大高度设置为百分比，例如希望设置为80%？

问题代码：

```ts
@Entry
@Component
struct SheetDemo {
  @State isShowSheet: boolean = false
  private items: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  @Builder
  SheetBuilder() {
    Column() {
      List({ space: '10vp' }) {
        ForEach(this.items, (item: number) => {
          ListItem() {
            Text(String(item)).fontSize(16).fontWeight(FontWeight.Bold)
          }.width('90%').height('80vp').backgroundColor('#ff53ecd9').borderRadius(10)
        })
      }.alignListItem(ListItemAlign.Center).margin({ top: '10vp' }).width('100%')
    }
    .width('90%')
    .height('100%')
  }

  build() {
    Column() {
      Button('Open Sheet').width('90%').height('80vp')
        .onClick(() => {
          this.isShowSheet = !this.isShowSheet
        })
        .bindSheet($$this.isShowSheet, this.SheetBuilder(), {
          height: SheetSize.FIT_CONTENT,
          showClose: false,
          preferType: SheetType.BOTTOM,
        })
    }.width('100%').height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

## 背景知识

[半模态转场](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)：通过bindSheet属性为组件绑定半模态页面，在组件插入时可通过设置自定义或默认的内置高度确定半模态大小。

## 解决方案

根据半模态页面内容的高度计算在窗口高度中的占比，高度大于最大高度，则显示最大高度，将高度配置到SheetOptions中：

```ts
import { window } from '@kit.ArkUI';

@Entry
@Component
struct SheetDemo {
  @State sheetHeight: string = '80%';
  @State windowHeight: number = 0;
  @State isShowSheet: boolean = false;
  private items: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  private itemHeight: number = 80;
  private spaceHeight: number = 10;
  private maxHeightPercent: number = 80;

  @Builder
  SheetBuilder() {
    Column() {
      List({ space: this.spaceHeight }) {
        ForEach(this.items, (item: number) => {
          ListItem() {
            Text(String(item)).fontSize(16).fontWeight(FontWeight.Bold);
          }.width('90%').height(this.itemHeight).backgroundColor('#5291FF').borderRadius(10);
        });
      }.alignListItem(ListItemAlign.Center).margin({ top: '10vp' }).width('100%');
    }
    .width('90%')
    .height('100%');
  }

  // 根据List内容去设置高度，同时要求最大高度小于80%
  build() {
    Column() {
      Button('Open Sheet').width('90%').height('80vp')
        .onClick(() => {
          this.isShowSheet = !this.isShowSheet;
          // 计算List组件内元素在窗口中的高度占比
          let height: number =
            ((this.itemHeight + this.spaceHeight) * this.items.length + this.spaceHeight) / this.windowHeight * 100;
          this.sheetHeight = `${Math.min(this.maxHeightPercent, height)}%`;
        })
        .bindSheet($$this.isShowSheet, this.SheetBuilder(), {
          height: this.sheetHeight, // this.sheetHeight为string类型的百分比
          showClose: false,
          preferType: SheetType.BOTTOM,
        });
    }.width('100%').height('100%')
    .justifyContent(FlexAlign.Center);
  }

  onPageShow(): void {
    let windowClass: window.Window | undefined = undefined;
    window.getLastWindow(this.getUIContext().getHostContext()).then((data) => {
      windowClass = data;
      try {
        let properties = windowClass.getWindowProperties();
        let rect = properties.windowRect;
        // rect.width:窗口宽度；rect.height:窗口高度。单位px。
        this.windowHeight = this.getUIContext().px2vp(rect.height);
      } catch (exception) {
        console.error(`Failed to obtain the window properties. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
}
```

列表高度超过最大高度时，效果如图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/yvJttPUhQAODsRpI4qe23A/zh-cn_image_0000002658795073.png "点击放大")

列表高度小于最大高度时，效果如图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/NccUwnVOR3GLEkznfmcf2A/zh-cn_image_0000002628555704.png "点击放大")
