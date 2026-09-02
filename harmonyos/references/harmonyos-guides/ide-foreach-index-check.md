---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-foreach-index-check
title: "@performance/foreach-index-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/foreach-index-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:903a12aa13cfc2eec230d88de965c1ed57e5bc2d07f211c1f041e6a2ba70cef5
---

使用Foreach组件时，不建议在keyGenerator中使用index作为返回值或者返回值的一部分，可能会导致性能问题。

[滑动丢帧场景](arkts-rendering-control-foreach.md#渲染性能降低)下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/foreach-index-check": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
@Entry
@Component
struct ForeachTest {
  private data: string[] = ['one', 'two', 'three'];
  build() {
    RelativeContainer() {
      List() {
        ForEach(this.data, (item: string, index: number) => {
          ListItem() {
            Text(item);
          }
        }, (item: string, index: number) => item)
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
    .width('100%')
  }
}
```

## 反例

```screen
@Entry
@Component
struct ForeachTest {
  private data: string[] = ['one', 'two', 'three'];
  build() {
    RelativeContainer() {
      List() {
        // warning line
        ForEach(this.data, (item: string, index: number) => {
          ListItem() {
            Text(item);
          }
        }, (item: string, index: number) => item + index)
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
    .width('100%')
  }
}
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
