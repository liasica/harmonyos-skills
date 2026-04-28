---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_touch-target-size
title: @cross-device-app-dev/touch-target-size
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/touch-target-size
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:23+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:a4b6fc200de5f34dc97f1ff944a4f48602c74dc8fea9b2c7d552fe1064cf0526
---

组件通用属性responseRegion点击热区需满足最小尺寸要求。

主要交互元素或控件的可点击热区至少为48vp×48vp（推荐），不得小于40vp×40vp。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@cross-device-app-dev/touch-target-size": "warn"
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
5. RelativeContainer() {
6. Text('message').responseRegion({width: 60, height: 60})
7. }
8. }
9. }
```

## 反例

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. RelativeContainer() {
6. Text('message').responseRegion({width: 27, height: 40})
7. }
8. }
9. }
```

## 规则集

```
1. plugin:@cross-device-app-dev/recommended
2. plugin:@cross-device-app-dev/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
