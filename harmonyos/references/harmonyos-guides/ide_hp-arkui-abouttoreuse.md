---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-abouttoreuse
title: "@performance/hp-arkui-avoid-update-auto-state-var-in-aboutToReuse"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-avoid-update-auto-state-var-in-aboutToReuse
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9bc1f26331c02f736bff46403f5107b186f2a84843726c7be8f9799ff2b2a4b1
---

避免在aboutToReuse中对自动更新值的状态变量进行更新。

通用丢帧场景下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-avoid-update-auto-state-var-in-aboutToReuse": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';

// 此处为复用的自定义组件
@Reusable
@Component
struct ItemComponent {
  @State desc: string = '';
  @State sum: number = 0;
  @State avg: number = 0;

  aboutToReuse(params: Record<string, Object>): void {
    this.desc = params.desc as string;
    this.sum = params.sum as number;
    this.avg = params.avg as number;
  }

  build() {
    Column() {
      Text('子组件' + this.desc)
        .fontSize(30)
        .fontWeight(30)
      Text('结果' + this.sum)
        .fontSize(30)
        .fontWeight(30)
      Text('平均值' + this.avg)
        .fontSize(30)
        .fontWeight(30)
    }
  }
}

@Entry
@Component
struct MyComponent {
  private data: MyDataSource = new MyDataSource();

  aboutToAppear(): void {
    for (let index = 0; index < 20; index++) {
      this.data.pushData(index.toString())
    }
  }

  build() {
    Column() {
      List() {
        LazyForEach(this.data, (item: string) => {
          ListItem() {
            ItemComponent({ desc: item, sum: 0, avg: 0 })
          }
          .width('100%')
          .height(100)
        }, (item: string) => item)
      }
      .width('100%')
      .height('100%')
    }
    .width('100%')
    .height('100%')
  }
}
```

## 反例

```screen
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';

// 此处为复用的自定义组件
@Reusable
@Component
struct ItemComponent {
  @State desc: string = '';
  @State sum: number = 0;
  @Link avg: number;

  aboutToReuse(params: Record<string, Object>): void {
    this.desc = params.desc as string;
    this.sum = params.sum as number;
    this.avg = params.avg as number;
  }

  build() {
    Column() {
      Text('子组件' + this.desc)
        .fontSize(30)
        .fontWeight(30)
      Text('结果' + this.sum)
        .fontSize(30)
        .fontWeight(30)
      Text('平均值' + this.avg)
        .fontSize(30)
        .fontWeight(30)
    }
  }
}

@Entry
@Component
struct MyComponent {
  private data: MyDataSource = new MyDataSource();

  aboutToAppear(): void {
    for (let index = 0; index < 20; index++) {
      this.data.pushData(index.toString())
    }
  }

  build() {
    Column() {
      List() {
        LazyForEach(this.data, (item: string) => {
          ListItem() {
            ItemComponent({ desc: item, sum: 0, avg: 0 })
          }
          .width('100%')
          .height(100)
        }, (item: string) => item)
      }
      .width('100%')
      .height('100%')
    }
    .width('100%')
    .height('100%')
  }
}
```

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
