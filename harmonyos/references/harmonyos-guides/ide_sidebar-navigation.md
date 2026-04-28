---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_sidebar-navigation
title: @cross-device-app-dev/sidebar-navigation
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/sidebar-navigation
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:23+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b9a848bb4b09fb6673ad8fc895bfb73a67e7c9890b2d2a63fd05c12a46df7a1b
---

对于2in1和tablet设备，应将Tabs组件设置为侧边导航栏。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@cross-device-app-dev/sidebar-navigation": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Tabs() {
6. TabContent() {
7. }.tabBar("tab1")

9. TabContent() {
10. }.tabBar("tab2")
11. }.vertical(true)
12. }
13. }
```

## 反例

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Tabs() {
6. TabContent() {
7. }.tabBar("tab1")

9. TabContent() {
10. }.tabBar("tab2")
11. }
12. }
13. }
```

## 规则集

```
1. plugin:@cross-device-app-dev/recommended
2. plugin:@cross-device-app-dev/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
