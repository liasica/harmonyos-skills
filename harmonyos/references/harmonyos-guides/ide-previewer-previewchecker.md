---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-previewchecker
title: PreviewChecker检测规则
breadcrumb: 指南 > 编写与调试应用 > 界面预览 > PreviewChecker检测规则
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b850d2026c29114d96cc77784bc1645c30d8cb7945bc67154a87577816fb1f6f
---

DevEco Studio启动预览时将执行PreviewChecker，检测通过后才可进行预览，以确保在使用预览器前识别到已知的不支持预览的场景，若存在不支持预览的场景，将给出优化提示，以便于开发者根据提示的建议进行代码优化。

## @previewer/mandatory-default-value-for-local-initialization

对于所有将被预览到的组件，如果组件的属性支持本地初始化，则都应当设置一个合法的不依赖运行时的默认值，以确保异常调用到该组件时，即使入参不完整，也能正常运行渲染。

**反例**

```
1. @Entry
2. @Component
3. struct Index {
4. message?: string;
5. @BuilderParam myBuilder: () => void;

7. build() {
8. Row() {
9. Column() {
10. Text(this.message)
11. this.myBuilder()
12. }
13. }
14. }
15. }
```

**正例**

```
1. @Builder function MyBuilderFunction(): void {}

3. @Entry
4. @Component
5. struct Index {
6. message?: string = 'message';
7. @Provide messageA: string = 'messageA';
8. @StorageLink('varA') varA: number = 2;
9. @StorageProp('languageCode') lang: string = 'en';
10. @LocalStorageLink('PropA') storageLink1: number = 1;
11. @LocalStorageProp('PropB') storageLink2: number = 2;
12. @BuilderParam myBuilder: () => void = MyBuilderFunction;

14. build() {
15. Row() {
16. Column() {
17. Text(this.message)
18. this.myBuilder()
19. }
20. }
21. }
22. }
```

## @previewer/no-unallowed-decorator-on-root-component

不允许直接预览包含@Consume、@Link、@ObjectLink、@Prop等装饰器的子组件；建议使用一个定义了完整的、合法的、不依赖运行时的默认值的父组件，并预览此父组件来查看子组件的预览效果。

**反例**

```
1. @Preview
2. @Component
3. struct LinkSample {
4. @Link message: string;

6. build() {
7. Row() {
8. Text(this.message)
9. }
10. }
11. }
```

**正例**

```
1. @Entry
2. @Component
3. struct LinkSampleContainer {
4. @State message: string = 'Hello World';

6. build() {
7. Row() {
8. LinkSample({message: this.message})
9. }
10. }
11. }

13. @Component
14. struct LinkSample {
15. @Link message: string;

17. build() {
18. Row() {
19. Text(this.message)
20. }
21. }
22. }
```

## @previewer/paired-use-of-consume-and-provide

如果缺少@Provide定义，@Consume组件在预览时将无法获取有效值。

API version 19及以前，@Consume装饰的变量不支持设置默认值，建议被@Consume修饰的组件的祖先组件上应当有对应的@Provide属性，并且该属性应当有合法的不依赖运行时的默认值。

从API version 20开始，@Consume装饰的变量支持设置默认值，建议优先对@Consume装饰的变量设置默认值，或者按照API version 19及以前版本的方式进行设置。

**反例**

```
1. @Entry
2. @Component
3. struct Parent {
4. build() {
5. Column() {
6. Child()
7. }
8. }
9. }

11. @Component
12. struct Child {
13. @Consume message: string;

15. build() {
16. Text(this.message)
17. }
18. }
```

**正例**一

```
1. // API 20及以上推荐此方式
2. @Entry
3. @Component
4. struct Parent {
5. @Consume message: string = 'hello world';
6. build() {
7. Column() {
8. Text(this.message)
9. .fontSize(50)
10. }
11. }
12. }
```

**正例二**

```
1. // 所有版本均可使用此方式
2. @Entry
3. @Component
4. struct Parent {
5. @Provide message: string = 'hello world';

7. build() {
8. Column() {
9. Child()
10. }
11. }
12. }

14. @Component
15. struct Child {
16. @Consume message: string;

18. build() {
19. Text(this.message)
20. }
21. }
```

## @previewer/no-page-method-on-preview-component

@Preview通常修饰在组件上，而非@Entry的页面入口。onPageShow、onPageHide、onBackPress仅在@Entry组件上生效。因此禁止在非路由组件上实例化onPageShow等页面级方法。

**反例**

```
1. @Preview
2. @Component
3. struct Index {
4. @State message: string = 'Hello World';

6. onPageShow(): void {}
7. onPageHide(): void {}
8. onBackPress(): void {}

10. build() {
11. Column() {
12. Text(this.message)
13. }
14. }
15. }
```

**正例**

```
1. @Entry
2. @Component
3. struct Index {
4. @State message: string = 'Hello World';

6. onPageShow(): void {}
7. onPageHide(): void {}
8. onBackPress(): void {}

10. build() {
11. Column() {
12. Text(this.message)
13. }
14. }
15. }
```

## @previewer/no-page-import-unmocked-hsp

由于能力缺失，预览器无法确保HSP是可以正常运行的。界面代码调用HSP可能会在预览运行时无法按预期执行，未正确初始化的接口调用可能会导致运行异常，从而影响界面渲染结果。建议待预览的组件及其依赖的组件避免引用HSP，或为该HSP设置Mock实现，更多关于Mock实现的介绍请参考[预览数据模拟](ide-previewer-mock.md)。

**反例**

```
1. import { add } from 'library'; // 该模块未配置自定义mock。

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'Hello World';

8. build() {
9. Row() {
10. Text(this.message)
11. .onClick(() => add(1, 2))
12. }
13. }
14. }
```

**正例**

```
1. import { add } from 'library'; // 该模块已配置自定义mock，配置方法见下文。

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'Hello World';

8. build() {
9. Row() {
10. Text(this.message)
11. .onClick(() => add(1, 2))
12. }
13. }
14. }
```

自定义mock配置：

```
1. // src/mock/mock-config.json5
2. {
3. "library": {
4. "source": "src/mock/myhsp.mock.ets"
5. },
6. }
```

```
1. // src/mock/myhsp.mock.ets
2. export function add(a: number, b: number): number {
3. return a + b;
4. }
```
