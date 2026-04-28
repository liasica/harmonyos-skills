---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-high-frequency-log-check
title: @performance/high-frequency-log-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/high-frequency-log-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:12+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:3cec2aa56192687e262396998cbcf53b853c9b70199830c48c83ddcdc417588c
---

不建议在高频函数中使用Hilog。

高频函数包括：onTouch、onItemDragMove、onDragMove、onMouse、onVisibleAreaChange、onAreaChange、onScroll（已废弃）、onWillScroll。

高耗时函数处理场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/high-frequency-log-check": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // Test.ets
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Column() {
7. Scroll()
8. .onWillScroll(() => {
9. const TAG = 'onWillScroll';
10. })
11. }
12. }
13. }
```

## 反例

```
1. // Test.ets
2. import hilog from '@ohos.hilog';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Column() {
9. Scroll()
10. .onWillScroll(() => {
11. // Avoid printing logs
12. hilog.info(1001, 'Index', 'onWillScroll');
13. })
14. }
15. }
16. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
