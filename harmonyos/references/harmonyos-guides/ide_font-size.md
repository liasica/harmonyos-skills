---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_font-size
title: "@cross-device-app-dev/font-size"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/font-size
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b86fb448cd3a15043531a0acd9d34077e30804167e532bdf7358cf77e0da55e7
---

字体大小要求至少为8fp以便于阅读。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@cross-device-app-dev/font-size": "warn"
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
      Text('message').fontSize(12)
      Text('message').fontSize('12fp')
    }
  }
}
```

## 反例

```screen
const FONT_SIZE = 7;

@Entry
@Component
struct Index1 {
  build() {
    RelativeContainer() {
      Text('message').fontSize(FONT_SIZE)
      Text('message').fontSize('7fp')
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
