---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-color-contrast
title: "@cross-device-app-dev/color-contrast"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/color-contrast
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:32+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:51333aee8e31f5c07b807c0003eaab4baff3283502b3023b61eb0d41f52d2055
---

文本和背景之间的颜色对比度至少为4.5:1以确保可读性。

## 规则配置

```json
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

```ts
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

```ts
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
