---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_grid-span-value
title: "@cross-device-app-dev/grid-span-value"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/grid-span-value
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5defa9641a1b6374eaff99810de8791ba50aa55f37de51f882e17c29bbb1ff4d
---

在栅格布局组件GridCol中，span和offset不建议使用小数。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@cross-device-app-dev/grid-span-value": "warn"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
@Entry
@Component
struct Index {
  build() {
    Column() {
      GridRow({
        columns: { sm: 4, md: 8, lg: 12 }
      }) {
        GridCol({
          span: { sm: 4, md: 4, lg: 4 }, offset: { sm: 0, md: 2, lg: 4 }
        }) {
          Row().backgroundColor($r('sys.color.ohos_id_color_palette_aux1'))
        }
      }
    }
  }
}
```

## 反例

```screen
@Entry
@Component
struct Index {
  build() {
    GridRow({
      columns: { sm: 4, md: 8, lg: 12 }
    }) {
      GridCol({
        span: { sm: 2.5, md: 4, lg: 4 }, offset: { sm: 0, md: 2.5, lg: 4 }
      }) {
        Row().backgroundColor($r('sys.color.ohos_id_color_palette_aux1'))
      }
    }
  }
}
```

## 规则集

```screen
plugin:@cross-device-app-dev/recommended
plugin:@cross-device-app-dev/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
