---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_grid-span-value
title: @cross-device-app-dev/grid-span-value
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/grid-span-value
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:22+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:8b7dea1c2e326692203dd1b66713d8e2dd3e24128df9ed5e73f1d7b7761afc5e
---

在栅格布局组件GridCol中，span和offset不建议使用小数。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@cross-device-app-dev/grid-span-value": "warn"
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
5. Column() {
6. GridRow({
7. columns: { sm: 4, md: 8, lg: 12 }
8. }) {
9. GridCol({
10. span: { sm: 4, md: 4, lg: 4 }, offset: { sm: 0, md: 2, lg: 4 }
11. }) {
12. Row().backgroundColor($r('sys.color.ohos_id_color_palette_aux1'))
13. }
14. }
15. }
16. }
17. }
```

## 反例

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. GridRow({
6. columns: { sm: 4, md: 8, lg: 12 }
7. }) {
8. GridCol({
9. span: { sm: 2.5, md: 4, lg: 4 }, offset: { sm: 0, md: 2.5, lg: 4 }
10. }) {
11. Row().backgroundColor($r('sys.color.ohos_id_color_palette_aux1'))
12. }
13. }
14. }
15. }
```

## 规则集

```
1. plugin:@cross-device-app-dev/recommended
2. plugin:@cross-device-app-dev/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
