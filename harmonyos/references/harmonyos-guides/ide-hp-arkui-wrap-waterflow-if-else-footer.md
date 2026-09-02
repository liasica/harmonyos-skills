---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkui-wrap-waterflow-if-else-footer
title: "@performance/hp-arkui-wrap-waterflow-if-else-footer（已下线）"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-wrap-waterflow-if-else-footer（已下线）
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:808fbd55debc7b91004955b410af3cac95186c0c5ada1cd50911df3f1ecb5dc1
---

建议使用容器包裹waterflow中footer的if-else逻辑。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-wrap-waterflow-if-else-footer": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';

@Entry
@Component
struct MyComponent{
  private datasource: MyDataSource = new MyDataSource();
  private showFooterStatus = 2;

  aboutToAppear() {
    for (let i = 0; i <= 20; i++) {
      this.datasource.pushData(i)
    }
  }

  build() {
    Column({ space: 2 }) {
      WaterFlow({ footer: (): void => this.itemFoot() }) {
        LazyForEach(this.datasource, (item: number) => {
          FlowItem() {
            ReusableFlowItem({ item: item })

          }.onAppear(() => {
            if (item + 20 == this.datasource.totalCount()) {
              for (let i = 0; i < 100; i++) {
                this.datasource.addLastItem()
              }
            }
          })

          .width('100%')
        }, (item: string) => item)
      }
      .columnsTemplate('1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(5)
      .width('100%')
      .height('50%')
    }
  }

  @Builder
  itemFoot() {
    //  外层加了一个column容器控制
    Column() {
      if (this.showFooterStatus == 1) {
        // Code to show try again
      } else if (this.showFooterStatus == 2) {
        // Code to show end
      } else {
        // Code to show footer loading
      }
    }
  }
}

@Component
@Reusable
struct ReusableFlowItem {
  @State item: number = 0

  aboutToReuse(params: Record<string, ESObject>) {
    this.item = params.item;
  }

  build() {
    Column() {
      Text('N' + this.item)
        .fontSize(12)
        .height('16')
      Image('res/waterFlowTest (' + this.item % 5 + ').jpg')
        .objectFit(ImageFit.Fill)
        .width('100%')
        .layoutWeight(1)
    }
  }
}
```

## 反例

```screen
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';

@Entry
@Component
struct MyComponent{
  private datasource: MyDataSource = new MyDataSource();
  private showFooterStatus = 2;

  aboutToAppear() {
    for (let i = 0; i <= 20; i++) {
      this.datasource.pushData(i)
    }
  }

  build() {
    Column({ space: 2 }) {
      WaterFlow({ footer: (): void => this.itemFoot() }) {
        LazyForEach(this.datasource, (item: number) => {
          FlowItem() {
            ReusableFlowItem({ item: item })

          }.onAppear(() => {
            if (item + 20 == this.datasource.totalCount()) {
              for (let i = 0; i < 100; i++) {
                this.datasource.addLastItem()
              }
            }
          })

          .width('100%')
        }, (item: string) => item)
      }
      .columnsTemplate('1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(5)
      .width('100%')
      .height('50%')
    }
  }

  @Builder
  itemFoot() {
    //  这个作为footer的build的逻辑里有if逻辑，应该在外层加一个容器控制
    if (this.showFooterStatus == 1) {
      // Code to show try again
    } else if (this.showFooterStatus == 2) {
      // Code to show end
    } else {
      // Code to show footer loading
    }
  }
}

@Component
@Reusable
struct ReusableFlowItem {
  @State item: number = 0

  aboutToReuse(params: Record<string, ESObject>) {
    this.item = params.item;
  }

  build() {
    Column() {
      Text('N' + this.item)
        .fontSize(12)
        .height('16')
      Image('res/waterFlowTest (' + this.item % 5 + ').jpg')
        .objectFit(ImageFit.Fill)
        .width('100%')
        .layoutWeight(1)
    }
  }
}
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
