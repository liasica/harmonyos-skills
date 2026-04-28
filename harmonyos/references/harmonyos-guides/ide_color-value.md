---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_color-value
title: @cross-device-app-dev/color-value
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/color-value
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:21+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:473adb098b101e143ab2638f8991ccf704e770306d5314b84944de55ddce39d3
---

颜色值应当使用“$r”从color.json中引用，以适配不同的系统颜色模式，禁止使用固定的值。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@cross-device-app-dev/color-value": "warn"
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
6. // 通过'sys.color.xxx'引用的颜色值，默认支持dark和light颜色模式
7. Text()
8. .fontColor($r('sys.color.ohos_id_color_activated'));
9. // 通过'app.color.xxx'引用的颜色值，需要分别在dark和light颜色模式的color.json中配置
10. Text()
11. .fontColor($r('app.color.text_color'));
12. }
13. }
14. }
```

## 反例

```
1. @Entry
2. @Component
3. struct Index1 {
4. build() {
5. RelativeContainer() {
6. Text('message').fontColor('#000000')
7. Text('message').fontColor('rgb(0, 0, 0)')
8. Text('message').fontColor(Color.Black)
9. }
10. }
11. }
```

## 规则集

```
1. plugin:@cross-device-app-dev/recommended
2. plugin:@cross-device-app-dev/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
