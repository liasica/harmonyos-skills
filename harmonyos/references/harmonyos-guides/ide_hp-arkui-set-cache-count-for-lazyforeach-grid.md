---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-set-cache-count-for-lazyforeach-grid
title: @performance/hp-arkui-set-cache-count-for-lazyforeach-grid
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-set-cache-count-for-lazyforeach-grid
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:07+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:37db515d88cd97d34d0bef42e5243b2fdff1a7530d17b9080946b48e6af229a6
---

建议在Grid下使用LazyForEach时设置合理的cacheCount。

滑动丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-set-cache-count-for-lazyforeach-grid": "suggestion",
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
6. struct MyComponent {
7. // 数据源
8. private data: MyDataSource = new MyDataSource();

10. aboutToAppear() {
11. for (let i = 1; i < 1000; i++) {
12. this.data.pushData(i);
13. }
14. }

16. build() {
17. Column({ space: 5 }) {
18. Grid() {
19. LazyForEach(this.data, (item: number) => {
20. GridItem() {
21. // 使用可复用自定义组件
22. // 业务逻辑
23. }
24. }, (item: string) => item.toString())
25. }
26. // 设置GridItem的缓存数量
27. .cachedCount(2)
28. .columnsTemplate('1fr 1fr 1fr')
29. .columnsGap(10)
30. .rowsGap(10)
31. .margin(10)
32. .height(500)
33. .backgroundColor(0xFAEEE0)
34. }
35. }
36. }
```

## 反例

```
1. // 源码文件，请以工程实际为准
2. import { MyDataSource } from './MyDataSource';

4. @Entry
5. @Component
6. struct MyComponent {
7. // 数据源
8. private data: MyDataSource = new MyDataSource();

10. aboutToAppear() {
11. for (let i = 1; i < 1000; i++) {
12. this.data.pushData(i);
13. }
14. }

16. build() {
17. Column({ space: 5 }) {
18. Grid() {
19. LazyForEach(this.data, (item: number) => {
20. GridItem() {
21. // 使用可复用自定义组件
22. // 业务逻辑
23. }
24. }, (item: string) => item.toString())
25. }
26. // 未设置GridItem的缓存数量
27. .columnsTemplate('1fr 1fr 1fr')
28. .columnsGap(10)
29. .rowsGap(10)
30. .margin(10)
31. .height(500)
32. .backgroundColor(0xFAEEE0)
33. }
34. }
35. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
