---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_font-size-unit
title: @cross-device-app-dev/font-size-unit
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/font-size-unit
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:22+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:21c0bfdcda94edbab007afdd50fae4ff23316c52a9b7fa74333d36d3cd3c0008
---

字体大小单位建议使用fp，以适配系统字体设置。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@cross-device-app-dev/font-size-unit": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. const FONT_SIZE = 12;

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. RelativeContainer() {
8. Text('message').fontSize(FONT_SIZE)
9. Text('message').fontSize('12fp')
10. }
11. }
12. }
```

## 反例

```
1. @Entry
2. @Component
3. struct Index1 {
4. build() {
5. RelativeContainer() {
6. Text('message').fontSize('12vp')
7. Text('message').fontSize('12px')
8. Text('message').fontSize('12lpx')
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
