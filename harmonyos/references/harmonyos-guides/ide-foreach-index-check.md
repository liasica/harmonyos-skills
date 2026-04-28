---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-foreach-index-check
title: @performance/foreach-index-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/foreach-index-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:01+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:0080bdff6b5cd8e4a9905fe8776970037bd3981e2e17c28d8fc11a813eb19042
---

使用Foreach组件时，不建议在keyGenerator中使用index作为返回值或者返回值的一部分，可能会导致性能问题。

[滑动丢帧场景](arkts-rendering-control-foreach.md#渲染性能降低)下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/foreach-index-check": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. @Entry
2. @Component
3. struct ForeachTest {
4. private data: string[] = ['one', 'two', 'three'];
5. build() {
6. RelativeContainer() {
7. List() {
8. ForEach(this.data, (item: string, index: number) => {
9. ListItem() {
10. Text(item);
11. }
12. }, (item: string, index: number) => item)
13. }
14. .width('100%')
15. .height('100%')
16. }
17. .height('100%')
18. .width('100%')
19. }
20. }
```

## 反例

```
1. @Entry
2. @Component
3. struct ForeachTest {
4. private data: string[] = ['one', 'two', 'three'];
5. build() {
6. RelativeContainer() {
7. List() {
8. // warning line
9. ForEach(this.data, (item: string, index: number) => {
10. ListItem() {
11. Text(item);
12. }
13. }, (item: string, index: number) => item + index)
14. }
15. .width('100%')
16. .height('100%')
17. }
18. .height('100%')
19. .width('100%')
20. }
21. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
