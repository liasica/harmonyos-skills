---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-image-async-load
title: "@performance/hp-arkui-image-async-load"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-image-async-load
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:57+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:2f57d2e787472a35004e0f0db074243337f33e098b4fc73f497d98bb9dc44467
---

建议大图片使用异步加载。

通用丢帧场景下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-image-async-load": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
@Entry
@Component
struct MyComponent {
  build() {
    Row() {
      // 本地图片4k.png
      Image($r('app.media.4k'))
        .border({ width: 1 })
        .borderStyle(BorderStyle.Dashed)
        .height(100)
        .width(100)
    }
  }
}
```

## 反例

```screen
@Entry
@Component
struct MyComponent {
  build() {
    Row() {
      // 本地图片4k.png
      Image($r('app.media.4k'))
        .border({ width: 1 })
        .borderStyle(BorderStyle.Dashed)
        .height(100)
        .width(100)
        .syncLoad(true)
    }
  }
}
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
