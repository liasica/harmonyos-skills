---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-load-on-demand
title: "@performance/hp-arkui-load-on-demand"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-load-on-demand
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3d06d2ea65916e24969582d281ca5dd2bca8189821dae09f3949c1cb806dd39b
---

建议使用按需加载。

滑动丢帧场景下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-load-on-demand": "warn",
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
struct ItemComponent {
  @State introduce: string = ''

  aboutToReuse(params: Record<string, ESObject>) {
    this.introduce = params.introduce
  }

  build() {
    Text(this.introduce)
      .fontSize(14)
      .padding({ left: 5, right: 5 })
      .margin({ top: 5 })
  }
}

@Entry
@Component
struct MyComponent {
  private data: MyDataSource = new MyDataSource()

  build() {
    List() {
      LazyForEach(this.data, (item: string) => {
        ListItem() {
          // 使用reuseId对不同的自定义组件实例分别标注复用组，以达到最佳的复用效果
          ItemComponent({ introduce: item }).reuseId(item)
        }
      }, (item: string) => item)
    }
    .width('100%')
    .height('100%')
  }
}
```

## 反例

```screen
@Entry
@Component
struct MyComponent {
  @State arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

  build() {
    List() {
      // List中建议使用LazyForEach
      ForEach(this.arr, (item: number) => {
        ListItem() {
          Text(`item value: ${item}`)
        }
      }, (item: number) => item.toString())
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
