---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-image-async-load
title: @performance/hp-arkui-image-async-load
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-image-async-load
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:03+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:d67a14db3827bacc31f60247b1e2bf54bfd00c49c985070375d2ed5e04733096
---

建议大图片使用异步加载。

通用丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-image-async-load": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. @Entry
2. @Component
3. struct MyComponent {
4. build() {
5. Row() {
6. // 本地图片4k.png
7. Image($r('app.media.4k'))
8. .border({ width: 1 })
9. .borderStyle(BorderStyle.Dashed)
10. .height(100)
11. .width(100)
12. }
13. }
14. }
```

## 反例

```
1. @Entry
2. @Component
3. struct MyComponent {
4. build() {
5. Row() {
6. // 本地图片4k.png
7. Image($r('app.media.4k'))
8. .border({ width: 1 })
9. .borderStyle(BorderStyle.Dashed)
10. .height(100)
11. .width(100)
12. .syncLoad(true)
13. }
14. }
15. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
