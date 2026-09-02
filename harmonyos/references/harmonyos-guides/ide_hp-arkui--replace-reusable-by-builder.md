---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui--replace-reusable-by-builder
title: "@performance/hp-arkui-replace-nested-reusable-component-by-builder"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-replace-nested-reusable-component-by-builder
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8c75f5c7645f48164777b29e90a940245122dd96e2f0a8926059e929e010d50f
---

建议使用@Builder替代嵌套的自定义组件。

通用丢帧场景下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-replace-nested-reusable-component-by-builder": "warn",
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
  private data: MyDataSource = new MyDataSource();

  aboutToAppear(): void {
    for (let index = 0; index < 30; index++) {
      this.data.pushData(index.toString())
    }
  }

  build() {
    Column() {
      List() {
        LazyForEach(this.data, (item: string) => {
          ListItem() {
            //  正例
            ChildComponent({ desc: item })
          }
        }, (item: string) => item)
      }
      .height('100%')
      .width('100%')
    }
    .width('100%')
  }
}

// 正例 使用组件复用
@Reusable
@Component
struct ChildComponent {
  @State desc: string = '';

  aboutToReuse(params: Record<string, Object>): void {
    this.desc = params.desc as string;
  }

  build() {
    Column() {
      // 使用@Builder，可以减少自定义组件创建和渲染的耗时
      ChildComponentBuilder({ paramA: this.desc })
    }
    .width('100%')
  }
}

class Temp {
  paramA: string = '';
}

@Builder
function ChildComponentBuilder($$: Temp) {
  Column() {
    // 此处使用`${}`来进行按引用传递，让@Builder感知到数据变化，进行UI刷新
    Text(`子组件 + ${$$.paramA}`)
      .fontSize(30)
      .fontWeight(30)
  }
  .width('100%')
}
```

## 反例

```screen
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';

@Entry
@Component
struct MyComponent{
  private data: MyDataSource = new MyDataSource();

  aboutToAppear(): void {
    for (let index = 0; index < 30; index++) {
      this.data.pushData(index.toString())
    }
  }

  build() {
    Column() {
      List() {
        LazyForEach(this.data, (item: string) => {
          ListItem() {
            //反例 使用自定义组件
            ComponentA({ desc: item })
          }
        }, (item: string) => item)
      }
      .height('100%')
      .width('100%')
    }
  }
}

@Reusable
@Component
struct ComponentA {
  @State desc: string = '';

  aboutToReuse(params: ESObject): void {
    this.desc = params.desc as string;
  }

  build() {
    // 在复用组件中嵌套使用自定义组件
    ComponentB({ desc: this.desc })
  }
}

@Component
struct ComponentB {
  @State desc: string = '';

  // 嵌套的组件中也需要实现aboutToReuse来进行UI的刷新
  aboutToReuse(params: ESObject): void {
    this.desc = params.desc as string;
  }

  build() {
    Column() {
      Text('子组件' + this.desc)
        .fontSize(30)
        .fontWeight(30)
    }
    .width('100%')
  }
}
```

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
