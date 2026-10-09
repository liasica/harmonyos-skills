---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-sidebar-navigation
title: "@cross-device-app-dev/sidebar-navigation"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/sidebar-navigation
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:32+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:2183fbcc971b92254ab2408af1907c484236b6e2926ff343782cb735f07e839c
---

对于2in1和tablet设备，应将Tabs组件设置为侧边导航栏。

## 规则配置

```json
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

```ts
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

```ts
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
