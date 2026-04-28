---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unallowed-decorator-on-root-component
title: @previewer/no-unallowed-decorator-on-root-component
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 预览规则@previewer > @previewer/no-unallowed-decorator-on-root-component
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:21+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b718176346f90068688a99ae546cbca2df0165fab90662500663be1136e3be22
---

不允许直接预览包含@Consume、@Link、@ObjectLink、@Prop等装饰器的子组件；

建议使用一个定义了完整的、合法的、不依赖运行时的默认值的父组件，并预览此父组件来查看子组件的预览效果。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@previewer/no-unallowed-decorator-on-root-component": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. @Entry
2. @Component
3. struct LinkSampleContainer {
4. @State message: string = 'Hello World';
5. build() {
6. Row() {
7. LinkSample({message: this.message})
8. }
9. }
10. }
11. @Component
12. struct LinkSample {
13. @Link message: string;
14. build() {
15. Row() {
16. Text(this.message)
17. }
18. }
19. }
```

## 反例

```
1. @Preview
2. @Component
3. struct LinkSample {
4. @Link message: string;
5. build() {
6. Row() {
7. Text(this.message)
8. }
9. }
10. }
```

## 规则集

```
1. plugin:@previewer/recommended
2. plugin:@previewer/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
