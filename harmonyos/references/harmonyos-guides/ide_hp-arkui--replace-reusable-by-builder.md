---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui--replace-reusable-by-builder
title: @performance/hp-arkui-replace-nested-reusable-component-by-builder
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-replace-nested-reusable-component-by-builder
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:06+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:dd5db4cdf7650a8138f831a47d65acbd6b2bbe10852438348683329a42ee5b15
---

建议使用@Builder替代嵌套的自定义组件。

通用丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-replace-nested-reusable-component-by-builder": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // 源码文件，请以工程实际为准
2. import { MyDataSource } from './MyDataSource';

4. @Entry
5. @Component
6. struct MyComponent{
7. private data: MyDataSource = new MyDataSource();

9. aboutToAppear(): void {
10. for (let index = 0; index < 30; index++) {
11. this.data.pushData(index.toString())
12. }
13. }

15. build() {
16. Column() {
17. List() {
18. LazyForEach(this.data, (item: string) => {
19. ListItem() {
20. //  正例
21. ChildComponent({ desc: item })
22. }
23. }, (item: string) => item)
24. }
25. .height('100%')
26. .width('100%')
27. }
28. .width('100%')
29. }
30. }

32. // 正例 使用组件复用
33. @Reusable
34. @Component
35. struct ChildComponent {
36. @State desc: string = '';

38. aboutToReuse(params: Record<string, Object>): void {
39. this.desc = params.desc as string;
40. }

42. build() {
43. Column() {
44. // 使用@Builder，可以减少自定义组件创建和渲染的耗时
45. ChildComponentBuilder({ paramA: this.desc })
46. }
47. .width('100%')
48. }
49. }

51. class Temp {
52. paramA: string = '';
53. }

55. @Builder
56. function ChildComponentBuilder($$: Temp) {
57. Column() {
58. // 此处使用`${}`来进行按引用传递，让@Builder感知到数据变化，进行UI刷新
59. Text(`子组件 + ${$$.paramA}`)
60. .fontSize(30)
61. .fontWeight(30)
62. }
63. .width('100%')
64. }
```

## 反例

```
1. // 源码文件，请以工程实际为准
2. import { MyDataSource } from './MyDataSource';

4. @Entry
5. @Component
6. struct MyComponent{
7. private data: MyDataSource = new MyDataSource();

9. aboutToAppear(): void {
10. for (let index = 0; index < 30; index++) {
11. this.data.pushData(index.toString())
12. }
13. }

15. build() {
16. Column() {
17. List() {
18. LazyForEach(this.data, (item: string) => {
19. ListItem() {
20. //反例 使用自定义组件
21. ComponentA({ desc: item })
22. }
23. }, (item: string) => item)
24. }
25. .height('100%')
26. .width('100%')
27. }
28. }
29. }

31. @Reusable
32. @Component
33. struct ComponentA {
34. @State desc: string = '';

36. aboutToReuse(params: ESObject): void {
37. this.desc = params.desc as string;
38. }

40. build() {
41. // 在复用组件中嵌套使用自定义组件
42. ComponentB({ desc: this.desc })
43. }
44. }

47. @Component
48. struct ComponentB {
49. @State desc: string = '';

51. // 嵌套的组件中也需要实现aboutToReuse来进行UI的刷新
52. aboutToReuse(params: ESObject): void {
53. this.desc = params.desc as string;
54. }

56. build() {
57. Column() {
58. Text('子组件' + this.desc)
59. .fontSize(30)
60. .fontWeight(30)
61. }
62. .width('100%')
63. }
64. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
