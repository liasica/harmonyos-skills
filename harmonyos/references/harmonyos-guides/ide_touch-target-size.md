---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_touch-target-size
title: "@cross-device-app-dev/touch-target-size"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/touch-target-size
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5f9ad88ae5b9e22e37ce2b0ba98930b08699373780ed0bd5fdbb17cbbdb4d805
---

组件通用属性responseRegion点击热区需满足最小尺寸要求。

主要交互元素或控件的可点击热区至少为48vp×48vp（推荐），不得小于40vp×40vp。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@cross-device-app-dev/touch-target-size": "warn"
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
      Text('message').responseRegion({width: 60, height: 60})
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
      Text('message').responseRegion({width: 27, height: 40})
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
