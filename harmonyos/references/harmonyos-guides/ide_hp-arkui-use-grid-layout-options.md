---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-grid-layout-options
title: "@performance/hp-arkui-use-grid-layout-options"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-grid-layout-options
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f65ba536d0cd40e51d703be40ea780ac65c8e04b995d93d9e36f5aeaa8734c50
---

建议在指定位置时使用GridLayoutOptions提升Grid性能。

通用丢帧场景下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-use-grid-layout-options": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';

@Reusable
@Component
struct TextItem {
  @State item: string = "";

  build() {
    Text(this.item)
      .fontSize(16)
      .backgroundColor(0xF9CF93)
      .width('100%')
      .height(80)
      .textAlign(TextAlign.Center)
      .onClick(() => {
        this.item = 'click';
      })
  }
}

@Entry
@Component
export struct MyComponent{
  private datasource: MyDataSource = new MyDataSource();
  scroller: Scroller = new Scroller();
  private irregularData: number[] = [];
  layoutOptions: GridLayoutOptions = {
    regularSize: [1, 1],
    irregularIndexes: this.irregularData,
  };

  aboutToAppear() {
    for (let i = 1; i <= 2000; i++) {
      this.datasource.pushData(i + '');
      if ((i - 1) % 4 === 0) {
        this.irregularData.push(i - 1);
      }
    }
  }

  build() {
    Column({ space: 5 }) {
      Text('Set GridItem size using GridLayoutOptions').fontColor(0xCCCCCC).fontSize(9).width('90%')
      Grid(this.scroller, this.layoutOptions) {
        LazyForEach(this.datasource, (item: string, index: number) => {
          GridItem() {
            TextItem({ item: item })
          }
        }, (item: string) => item)
      }
      .cachedCount(1)
      .columnsTemplate('1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .width('90%')
      .height('40%')

      Button("scrollToIndex:1900").onClick(() => {
        this.scroller.scrollToIndex(1900);
      })
    }.width('100%')
    .margin({ top: 5 })
  }
}
```

## 反例

```screen
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';

@Reusable
@Component
struct TextItem {
  @State item: string = "";

  build() {
    Text(this.item)
      .fontSize(16)
      .backgroundColor(0xF9CF93)
      .width('100%')
      .height(80)
      .textAlign(TextAlign.Center)
      .onClick(() => {
        this.item = 'click';
      })
  }
}

@Entry
@Component
struct MyComponent{
  private datasource: MyDataSource = new MyDataSource();
  scroller: Scroller = new Scroller();

  aboutToAppear() {
    for (let i = 1; i <= 2000; i++) {
      this.datasource.pushData(i + '');
    }
  }

  build() {
    Column({ space: 5 }) {
      Text('Use columnStart and columnEnd to set the GridItem size').fontColor(0xCCCCCC).fontSize(9).width('90%')
      Grid(this.scroller) {
        LazyForEach(this.datasource, (item: string, index: number) => {
          if ((index % 4) === 0) {
            GridItem() {
              TextItem({ item: item })
            }
            .columnStart(0).columnEnd(2)
          } else {
            GridItem() {
              TextItem({ item: item })
            }
          }
        }, (item: string) => item)
      }
      .cachedCount(1)
      .columnsTemplate('1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .width('90%')
      .height('40%')

      Button("scrollToIndex:1900").onClick(() => {
        this.scroller.scrollToIndex(1900);
      })
    }.width('100%')
    .margin({ top: 5 })
  }
}
```

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
