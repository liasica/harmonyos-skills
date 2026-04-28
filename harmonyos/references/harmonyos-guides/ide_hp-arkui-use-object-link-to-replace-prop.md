---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-object-link-to-replace-prop
title: @performance/hp-arkui-use-object-link-to-replace-prop
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-object-link-to-replace-prop
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:09+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:c438bd60ede5420eb6986d05a6c7c5040960a03d660a19dfe92159007e9ee4cd
---

建议使用@ObjectLink代替@Prop减少不必要的深拷贝。

通用丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-use-object-link-to-replace-prop": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. @Observed
2. class ClassA {
3. public c: number = 0;
4. constructor(c: number) {
5. this.c = c;
6. }
7. }
8. @Component
9. struct PropChild {
10. // @ObjectLink 装饰状态变量不会深拷贝
11. // 当修饰为ObjectLink时 ClassA必须同时被Observed修饰
12. @ObjectLink testNum: ClassA;
13. build() {
14. Text(`PropChild testNum ${this.testNum.c}`)
15. }
16. }
17. @Entry
18. @Component
19. struct Parent {
20. @State testNum: ClassA[] = [new ClassA(1)];
21. build() {
22. Column() {
23. Text(`Parent testNum ${this.testNum[0].c}`)
24. .onClick(() => {
25. this.testNum[0].c += 1;
26. })
27. // 当子组件不需要发生本地改变时，优先使用@ObjectLink，因为@Prop是会深拷贝数据，具有拷贝的性能开销，所以这个时候@ObjectLink是比@Link和@Prop更优的选择
28. PropChild({ testNum: this.testNum[0] })
29. }
30. }}
```

## 反例

```
1. @Observed
2. class ClassA {
3. public c: number = 0;
4. constructor(c: number) {
5. this.c = c;
6. }
7. }
8. @Component
9. struct PropChild {
10. // @Prop 装饰状态变量会深拷贝
11. @Prop testNum: ClassA;
12. build() {
13. Text(`PropChild testNum ${this.testNum.c}`)
14. }
15. }
16. @Entry
17. @Component
18. struct Parent {
19. @State testNum: ClassA[] = [new ClassA(1)];
20. build() {
21. Column() {
22. Text(`Parent testNum ${this.testNum[0].c}`)
23. .onClick(() => {
24. this.testNum[0].c += 1;
25. })
26. // PropChild没有改变@Prop testNum: ClassA的值，所以这时最优的选择是使用@ObjectLink
27. PropChild({ testNum: this.testNum[0] })
28. }
29. }
30. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
