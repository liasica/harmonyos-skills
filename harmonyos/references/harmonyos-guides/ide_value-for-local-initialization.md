---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_value-for-local-initialization
title: @previewer/mandatory-default-value-for-local-initialization
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 预览规则@previewer > @previewer/mandatory-default-value-for-local-initialization
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:20+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:dad33a192a6dea5481d8b50fa19900a7a7d3bba6b21a3f1896a04338a30da470
---

如果组件的属性支持本地初始化，需要设置一个合法的不依赖运行时的默认值。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@previewer/mandatory-default-value-for-local-initialization": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. @Builder
2. function MyBuilderFunction(): void {
3. }

5. @Entry
6. @Component
7. struct Index {
8. messageA?: string;
9. message: string = 'Hello World';
10. @Provide messageB: string = 'messageB';
11. @StorageLink('varA') varA: number = 2;
12. @StorageProp('languageCode') lang: string = 'en';
13. @LocalStorageLink('PropA') storageLink1: number = 1;
14. @LocalStorageProp('PropB') storageLink2: number = 2;
15. @BuilderParam myBuilder: () => void = MyBuilderFunction;

17. build() {
18. Row() {
19. Column() {
20. Text(this.message)
21. this.myBuilder()
22. }
23. }
24. }
25. }
```

## 反例

```
1. @Entry
2. @Component
3. struct Index {
4. @BuilderParam myBuilder: () => void;

6. build() {
7. Row() {
8. Column() {
9. Text('Hello World')
10. this.myBuilder()
11. }
12. }
13. }
14. }
```

## 规则集

```
1. plugin:@previewer/recommended
2. plugin:@previewer/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
