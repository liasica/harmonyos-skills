---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_font-size-unit
title: "@cross-device-app-dev/font-size-unit"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/font-size-unit
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f069b77737db51d947b0110d21738a6dbc0501cdeedf3e5eb44558443d072b23
---

字体大小单位建议使用fp，以适配系统字体设置。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@cross-device-app-dev/font-size-unit": "warn"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
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

```screen
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
