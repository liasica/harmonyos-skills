---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_color-contrast
title: @cross-device-app-dev/color-contrast
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/color-contrast
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:21+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:e235ffdd3b3a7ab130a2346119c722ed71274031142b57ccbdfa5498eaac2627
---

文本和背景之间的颜色对比度至少为4.5:1以确保可读性。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@cross-device-app-dev/color-contrast": "warn"
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
6. Text('message')
7. // app.color.color1=#ffffff
8. .fontColor($r('app.color.color1'))
9. // app.color.color2=#000000
10. .backgroundColor($r('app.color.color2'))
11. }
12. }
13. }
```

## 反例

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. RelativeContainer() {
6. Text('message')
7. // app.color.color1=#000000
8. .fontColor($r('app.color.color1'))
9. // app.color.color2=#333333
10. .backgroundColor($r('app.color.color2'))
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
