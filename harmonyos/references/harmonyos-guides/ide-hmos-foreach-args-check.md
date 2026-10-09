---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-foreach-args-check
title: "@performance/foreach-args-check"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/foreach-args-check
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:568ec3b1f54a66d12b68dc5809a02cca27323464fcd7a7828cdeb036fdc51a2d
---

建议在ForEach参数中设置keyGenerator。

[滑动丢帧场景](arkts-rendering-control-foreach.md#键值生成规则)下，建议优先修改。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@performance/foreach-args-check": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```ts
@Entry
@Component
struct ForeachTest {
  private data: string[] = ['1', '2', '3'];
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
  private data: string[] = ['1', '2', '3'];
  build() {
    RelativeContainer() {
      List() {
        // ForEach缺少第三个参数，告警
        ForEach(this.data, (item: string, index: number) => {
          ListItem() {
            Text(item);
          }
        })
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
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
