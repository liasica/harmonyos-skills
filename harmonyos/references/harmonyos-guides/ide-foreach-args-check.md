---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-foreach-args-check
title: @performance/foreach-args-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/foreach-args-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:02+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:ff68e02c426364811491e9e2f2a8449cfc55e60c3d0b8e5fd103830b5c82be58
---

建议在ForEach参数中设置keyGenerator。

[滑动丢帧场景](arkts-rendering-control-foreach.md#键值生成规则)下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/foreach-args-check": "warn",
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
4. private data: string[] = ['1', '2', '3'];
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
4. private data: string[] = ['1', '2', '3'];
5. build() {
6. RelativeContainer() {
7. List() {
8. // ForEach缺少第三个参数，告警
9. ForEach(this.data, (item: string, index: number) => {
10. ListItem() {
11. Text(item);
12. }
13. })
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
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
