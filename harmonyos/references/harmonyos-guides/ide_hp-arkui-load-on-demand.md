---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-load-on-demand
title: @performance/hp-arkui-load-on-demand
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-load-on-demand
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:04+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:4c51880e2dfb8db1cc98338bda585059ed40bee6f7a5055b5863c03b2929bead
---

建议使用按需加载。

滑动丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-load-on-demand": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // 源码文件，请以工程实际为准
2. import { MyDataSource } from './MyDataSource';

4. @Reusable
5. @Component
6. struct ItemComponent {
7. @State introduce: string = ''

9. aboutToReuse(params: Record<string, ESObject>) {
10. this.introduce = params.introduce
11. }

13. build() {
14. Text(this.introduce)
15. .fontSize(14)
16. .padding({ left: 5, right: 5 })
17. .margin({ top: 5 })
18. }
19. }

21. @Entry
22. @Component
23. struct MyComponent {
24. private data: MyDataSource = new MyDataSource()

26. build() {
27. List() {
28. LazyForEach(this.data, (item: string) => {
29. ListItem() {
30. // 使用reuseId对不同的自定义组件实例分别标注复用组，以达到最佳的复用效果
31. ItemComponent({ introduce: item }).reuseId(item)
32. }
33. }, (item: string) => item)
34. }
35. .width('100%')
36. .height('100%')
37. }
38. }
```

## 反例

```
1. @Entry
2. @Component
3. struct MyComponent {
4. @State arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

6. build() {
7. List() {
8. // List中建议使用LazyForEach
9. ForEach(this.arr, (item: number) => {
10. ListItem() {
11. Text(`item value: ${item}`)
12. }
13. }, (item: number) => item.toString())
14. }
15. .width('100%')
16. .height('100%')
17. }
18. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
