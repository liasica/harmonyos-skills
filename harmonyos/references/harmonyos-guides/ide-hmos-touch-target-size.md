---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-touch-target-size
title: "@cross-device-app-dev/touch-target-size"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/touch-target-size
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:32+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:dfcf249a635220060dbe9fa9e83b81112e79d0c8065192944c5de89d6e3f7f09
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

该规则无需配置额外选项。

## 正例

```ts
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

```ts
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
