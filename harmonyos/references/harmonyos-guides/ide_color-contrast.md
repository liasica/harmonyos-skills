---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_color-contrast
title: "@cross-device-app-dev/color-contrast"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/color-contrast
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dffd21e42364e12defd7b2b446651ea24f79c02ff5d64575d423a289f45aa4b9
---

文本和背景之间的颜色对比度至少为4.5:1以确保可读性。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@cross-device-app-dev/color-contrast": "warn"
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
    RelativeContainer() {
      Text('message')
        // app.color.color1=#ffffff
        .fontColor($r('app.color.color1'))
          // app.color.color2=#000000
        .backgroundColor($r('app.color.color2'))
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
    RelativeContainer() {
      Text('message')
        // app.color.color1=#000000
        .fontColor($r('app.color.color1'))
        // app.color.color2=#333333
        .backgroundColor($r('app.color.color2'))
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
