---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_grid-columns-span
title: @cross-device-app-dev/grid-columns-span
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/grid-columns-span
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:22+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:68f4d690f92207086a661598ba615bca4e958b7833283379559600fad61d37e9
---

不推荐开发者将栅格中所有的GridCol子组件只设置span属性，且值与父组件的columns属性相等。这等效于子组件宽度始终为父容器的100%，栅格系统没有发挥作用，徒增页面组件树复杂度，影响性能。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@cross-device-app-dev/grid-columns-span": "warn"
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
5. Column() {
6. GridRow({
7. columns: { sm: 4, md: 8, lg: 12 }
8. }) {
9. GridCol({
10. span: { sm: 4, md: 8, lg: 12 }
11. }) {
12. Row().backgroundColor($r('sys.color.ohos_id_color_palette_aux1'))
13. }
14. }
15. }
16. }
17. }
```

## 规则集

```
1. plugin:@cross-device-app-dev/recommended
2. plugin:@cross-device-app-dev/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
