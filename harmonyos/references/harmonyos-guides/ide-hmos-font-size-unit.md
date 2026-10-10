---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-font-size-unit
title: "@cross-device-app-dev/font-size-unit"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/font-size-unit
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:20+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:a954b6a2473c11ff69ca0f6599e2ba7419be000047b7e6198835475967770e44
---

字体大小单位建议使用fp，以适配系统字体设置。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@cross-device-app-dev/font-size-unit": "warn"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
const FONT_SIZE = 12;

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text('message').fontSize(FONT_SIZE)
      Text('message').fontSize('12fp')
    }
  }
}
```

## 反例

```ts
@Entry
@Component
struct Index1 {
  build() {
    RelativeContainer() {
      Text('message').fontSize('12vp')
      Text('message').fontSize('12px')
      Text('message').fontSize('12lpx')
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
