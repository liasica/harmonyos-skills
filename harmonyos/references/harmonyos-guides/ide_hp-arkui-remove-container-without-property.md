---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-remove-container-without-property
title: @performance/hp-arkui-remove-container-without-property
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-remove-container-without-property
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:05+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:03fef9cb9b6bb6408f517f493aaf25300736fa0b2d5d2564828396121e204731
---

建议尽量减少视图嵌套层次。该规则曾用名：@performance/hp-arkui-reduce-view-nest-level 。

通用丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-remove-container-without-property": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. @Entry
2. @Component
3. struct MyComponent{
4. @State number: Number[] = Array.from(Array<number>(1000), (val, i) => i);
5. scroller: Scroller = new Scroller()
6. build() {
7. Column() {
8. Grid(this.scroller) {
9. ForEach(this.number, (item: number) => {
10. GridItem() {
11. Text(item.toString())
12. .fontSize(16)
13. .backgroundColor(0xF9CF93)
14. .width('100%')
15. .height(80)
16. .textAlign(TextAlign.Center)
17. .border({width:1})
18. }
19. }, (item:string) => item)
20. }
21. .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
22. .columnsGap(0)
23. .rowsGap(0)
24. .size({ width: "100%", height: "100%" })
25. }
26. }
27. }
```

## 反例

```
1. @Entry
2. @Component
3. struct MyComponent{
4. @State number: Number[] = Array.from(Array<number>(1000), (val, i) => i);
5. scroller: Scroller = new Scroller()
6. build() {
7. Column() {
8. Grid(this.scroller) {
9. ForEach(this.number, (item: number) => {
10. GridItem() {
11. Flex() {
12. Flex() {
13. Flex() {
14. Text(item.toString())
15. .fontSize(16)
16. .backgroundColor(0xF9CF93)
17. .width('100%')
18. .height(80)
19. .textAlign(TextAlign.Center)
20. .border({width:1})
21. }
22. }
23. }
24. }
25. }, (item:string) => item)
26. }
27. .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
28. .columnsGap(0)
29. .rowsGap(0)
30. .size({ width: "100%", height: "100%" })
31. }
32. }
33. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
