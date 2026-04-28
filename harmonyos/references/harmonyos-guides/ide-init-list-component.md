---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-init-list-component
title: @performance/init-list-component
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/init-list-component
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:12+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:9e9027a48896dc00031d93f4eccdcacaeae338c0b5b8fd502e7ee22765fef682
---

List组件在使用时，建议同时定义width和height属性。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/init-list-component": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. @Component
2. struct Greeting {
3. @Builder myBuilder() {
4. List().width(10).height(10)
5. }
6. build() {
7. List() {
8. }.width(10).height(10);
9. }
10. }

12. @Builder function globalBuilder() {
13. List().width(10).height(10)
14. }
```

## 反例

```
1. @Component
2. struct Greeting {
3. @Builder myBuilder() {
4. // missing initialization of attribute 'height'
5. List().width(10)
6. }
7. build() {
8. // missing initialization of attribute 'width'
9. List().height(10);
10. }
11. }

13. @Builder function myBuilder() {
14. // missing initialization of attribute 'height'
15. List().width(10)
16. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
