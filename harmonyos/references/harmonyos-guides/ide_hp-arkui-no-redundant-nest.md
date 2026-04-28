---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-no-redundant-nest
title: @performance/hp-arkui-remove-redundant-nest-container
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-remove-redundant-nest-container
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:06+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:29649515f7157df8001dbec3b80273dbfab399aa295582934080a6c1b4c9f8a7
---

避免冗余的嵌套。

通用丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-remove-redundant-nest-container": "suggestion",
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
4. @State children: number[] = Array.from(Array<number>(900), (v, k) => k);

6. build() {
7. Scroll() {
8. Grid() {
9. ForEach(this.children, (item: Number[]) => {
10. GridItem() {
11. Text(item.toString())
12. }.backgroundColor(Color.Yellow)
13. }, (item: string) => item)
14. }
15. .columnsTemplate('1fr 1fr 1fr 1fr')
16. .columnsGap(0)
17. .rowsGap(0)
18. .size({ width: "100%", height: "100%" })
19. }
20. }
21. }
```

## 反例

```
1. @Entry
2. @Component
3. struct MyComponent {
4. @State children: number[] = Array.from(Array<number>(900), (v, k) => k);

6. build() {
7. Scroll() {
8. Grid() {
9. ForEach(this.children, (item: Number[]) => {
10. GridItem() {
11. // 冗余Stack
12. Stack() {
13. Stack() {
14. Stack() {
15. Text(item.toString())
16. }.size({ width: "100%"})
17. }.backgroundColor(Color.Yellow)
18. }.backgroundColor(Color.Pink)
19. }
20. }, (item: string) => item)
21. }
22. .columnsTemplate('1fr 1fr 1fr 1fr')
23. .columnsGap(0)
24. .rowsGap(0)
25. .size({ width: "100%", height: "100%" })
26. }
27. }
28. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
