---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_size-unit
title: @cross-device-app-dev/size-unit
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/size-unit
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:23+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:3ed702de2cd4af0e3ddff3c0051f10c7707225e22654a98fe9734475a25e82cb
---

组件通用属性width、height和size，应当使用vp作为单位，以适配不同设备屏幕宽度。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@cross-device-app-dev/size-unit": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. const WIDTH_SIZE = 100;

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Row() {
8. Column() {
9. Button('btn').size({ width: 40, height: '20vp' })
10. }.width(WIDTH_SIZE)
11. .height('100vp')
12. }
13. .height('100%')
14. .width('100%')
15. .justifyContent(FlexAlign.Center)
16. }
17. }
```

## 反例

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Row() {
6. Column() {
7. Button('btn').size({ width: '40px', height: '20px' })
8. }.width('100px')
9. .height('100px')
10. }
11. .height('100%')
12. .width('100%')
13. .justifyContent(FlexAlign.Center)
14. }
15. }
```

## 规则集

```
1. plugin:@cross-device-app-dev/recommended
2. plugin:@cross-device-app-dev/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
