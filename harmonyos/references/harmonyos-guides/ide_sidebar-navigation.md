---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_sidebar-navigation
title: "@cross-device-app-dev/sidebar-navigation"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/sidebar-navigation
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:047f95e6b4ed29579d121fc9e5f500dae1491527a4a97139c5783d07dfbfb3d5
---

对于2in1和tablet设备，应将Tabs组件设置为侧边导航栏。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@cross-device-app-dev/sidebar-navigation": "warn"
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
    Tabs() {
      TabContent() {
      }.tabBar("tab1")

      TabContent() {
      }.tabBar("tab2")
    }.vertical(true)
  }
}
```

## 反例

```screen
@Entry
@Component
struct Index {
  build() {
    Tabs() {
      TabContent() {
      }.tabBar("tab1")

      TabContent() {
      }.tabBar("tab2")
    }
  }
}
```

## 规则集

```screen
plugin:@cross-device-app-dev/recommended
plugin:@cross-device-app-dev/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
