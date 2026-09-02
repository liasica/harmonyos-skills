---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_size-unit
title: "@cross-device-app-dev/size-unit"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/size-unit
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:25090301a936fb1bb12b2529d767393a6d462ef169f1c93cfb1dfaed2dc83abf
---

组件通用属性width、height和size，应当使用vp作为单位，以适配不同设备屏幕宽度。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@cross-device-app-dev/size-unit": "warn"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
const WIDTH_SIZE = 100;

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('btn').size({ width: 40, height: '20vp' })
      }.width(WIDTH_SIZE)
      .height('100vp')
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

## 反例

```screen
@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('btn').size({ width: '40px', height: '20px' })
      }.width('100px')
      .height('100px')
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

## 规则集

```screen
plugin:@cross-device-app-dev/recommended
plugin:@cross-device-app-dev/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
