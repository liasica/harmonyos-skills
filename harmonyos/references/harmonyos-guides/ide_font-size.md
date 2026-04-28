---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_font-size
title: @cross-device-app-dev/font-size
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/font-size
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:22+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:d0fc33e3381d86bdd17899b11b9e4255ae1303691ea80652df71ad01fe4f0740
---

字体大小要求至少为8fp以便于阅读。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@cross-device-app-dev/font-size": "warn"
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
8. Text('message').fontSize(12)
9. Text('message').fontSize('12fp')
10. }
11. }
12. }
```

## 反例

```
1. const FONT_SIZE = 7;

3. @Entry
4. @Component
5. struct Index1 {
6. build() {
7. RelativeContainer() {
8. Text('message').fontSize(FONT_SIZE)
9. Text('message').fontSize('7fp')
10. }
11. }
12. }
```

## 规则集

```
1. plugin:@cross-device-app-dev/recommended
2. plugin:@cross-device-app-dev/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
