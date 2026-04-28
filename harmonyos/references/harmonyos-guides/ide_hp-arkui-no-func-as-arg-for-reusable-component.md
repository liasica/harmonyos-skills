---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-no-func-as-arg-for-reusable-component
title: @performance/hp-arkui-no-func-as-arg-for-reusable-component
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-no-func-as-arg-for-reusable-component
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:04+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:69d9a5d02512d7d050e30d9a4e8c342e4afaf9e9e212b15ee61d00da170ab45f
---

避免使用函数作为复用的自定义组件创建时的入参。

滑动丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-no-func-as-arg-for-reusable-component": "warn",
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
6. struct ChildComponent {
7. @State desc: string = '';
8. @State sum: number = 0;

10. aboutToReuse(params: Record<string, Object>): void {
11. this.desc = params.desc as string;
12. this.sum = params.sum as number;
13. }

15. build() {
16. Column() {
17. Text('子组件' + this.desc)
18. .fontSize(30)
19. .fontWeight(30)
20. Text('结果' + this.sum)
21. .fontSize(30)
22. .fontWeight(30)
23. }
24. }
25. }

27. @Entry
28. @Component
29. struct MyComponent{
30. private data: MyDataSource = new MyDataSource();
31. @State sum: number = 0;

33. aboutToAppear(): void {
34. for (let index = 0; index < 20; index++) {
35. this.data.pushData(index.toString())
36. }
37. // 执行该异步函数
38. this.count();
39. }

41. // 模拟耗时操作逻辑
42. async count() {
43. let temp: number = 0;
44. for (let index = 0; index < 10000; index++) {
45. temp += index;
46. }
47. // 将结果放入状态变量中
48. this.sum = temp;
49. }

51. build() {
52. Column() {
53. List() {
54. LazyForEach(this.data, (item: string) => {
55. ListItem() {
56. // 子组件的传参通过状态变量进行
57. ChildComponent({ desc: item, sum: this.sum })
58. }
59. .width('100%')
60. .height(100)
61. }, (item: string) => item)
62. }
63. .width('100%')
64. .height('100%')
65. }
66. }
67. }
```

## 反例

```
1. // 源码文件，请以工程实际为准
2. import { MyDataSource } from './MyDataSource';

4. // 此处为复用的自定义组件
5. @Reusable
6. @Component
7. struct ChildComponent {
8. @State desc: string = '';
9. @State sum: number = 0;

11. aboutToReuse(params: Record<string, Object>): void {
12. this.desc = params.desc as string;
13. this.sum = params.sum as number;
14. }

16. build() {
17. Column() {
18. Text('子组件' + this.desc)
19. .fontSize(30)
20. .fontWeight(30)
21. Text('结果' + this.sum)
22. .fontSize(30)
23. .fontWeight(30)
24. }
25. }
26. }

28. @Entry
29. @Component
30. struct MyComponent{
31. private data: MyDataSource = new MyDataSource();

33. aboutToAppear(): void {
34. for (let index = 0; index < 20; index++) {
35. this.data.pushData(index.toString())
36. }
37. }

39. // 真实场景的函数中可能存在未知的耗时操作逻辑，此处用循环函数模拟耗时操作
40. count(): number {
41. let temp: number = 0;
42. for (let index = 0; index < 10000; index++) {
43. temp += index;
44. }
45. return temp;
46. }

48. build() {
49. Column() {
50. List() {
51. LazyForEach(this.data, (item: string) => {
52. ListItem() {
53. // 此处sum参数是函数获取的，实际开发场景无法预料该函数可能出现的耗时操作，每次进行组件复用都会重复触发此函数的调用
54. ChildComponent({ desc: item, sum: this.count() })
55. }
56. .width('100%')
57. .height(100)
58. }, (item: string) => item)
59. }
60. .height('100%')
61. .width('100%')
62. }
63. }
64. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
