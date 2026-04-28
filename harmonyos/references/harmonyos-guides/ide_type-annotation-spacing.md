---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_type-annotation-spacing
title: @typescript-eslint/type-annotation-spacing
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/type-annotation-spacing
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:51+08:00
doc_updated_at: 2026-02-09
content_hash: sha256:462e8b02556aa1c514e83cc3f16d783ef9e16d2e896bc377a67aad160893ee22
---

类型注解前后需要一致的空格风格。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/type-annotation-spacing": "error"
5. }
6. }
```

## 选项

支持配置以下选项：

```
1. type Options = {
2. before: boolean;
3. after: boolean;
4. overrides: {
5. colon: {
6. before: boolean;
7. after: boolean;
8. };
9. arrow: {
10. before: boolean;
11. after: boolean;
12. };
13. variable: {
14. before: boolean;
15. after: boolean;
16. };
17. parameter: {
18. before: boolean;
19. after: boolean;
20. };
21. property: {
22. before: boolean;
23. after: boolean;
24. };
25. returnType: {
26. before: boolean;
27. after: boolean;
28. };
29. }
30. }
```

* before/after：布尔类型，可以设置为true或者false。true表示类型注解中的冒号（:）和箭头（=>）之前/之后需要加空格，false表示类型注解中的冒号（:）和箭头（=>）之前/之后不需要加空格。
* overrides：对象类型，可以对不同的语法场景进行差异化配置，支持以下属性：
  + colon：对象类型，可以对类型注解中的冒号（:）进行差异化配置，支持以下属性：
    - before：布尔类型，可以设置为true或者false。默认值为false，表示类型注解中的冒号（:）之前不需要加空格；true表示类型注解中的冒号（:）之前需要加空格。
    - after：布尔类型，可以设置为true或者false。默认值为false，表示类型注解中的冒号（:）之后不需要加空格；true表示类型注解中的冒号（:）之后需要加空格。
  + arrow：对象类型，可以对类型注解中的箭头（=>）进行差异化配置，支持以下属性：
    - before：布尔类型，可以设置为true或者false。默认值为true，表示类型注解中的箭头（=>）之前需要加空格；false表示类型注解中的箭头（=>）之前不需要加空格。
    - after：布尔类型，可以设置为true或者false。默认值为true，表示类型注解中的箭头（=>）之后需要加空格；false表示类型注解中的箭头（=>）之后不需要加空格。
  + variable：对象类型，可以对变量中类型注解的冒号（:）进行差异化配置，支持配置为before/after：
    - before/after：布尔类型，可以设置为true或者false，true表示类型注解中的冒号（:）之前/之后需要加空格。
  + parameter：对象类型，可以对参数中类型注解的冒号（:）进行差异化配置，支持配置为before/after：
    - before/after：布尔类型，可以设置为true或者false，true表示类型注解中的冒号（:）之前/之后需要加空格。
  + property：对象类型，可以对类/接口成员中类型注解的冒号（:）进行差异化配置，支持配置为before/after：
    - before/after：布尔类型，可以设置为true或者false，true表示类型注解中的冒号（:）之前/之后需要加空格。
  + returnType：对象类型，可以对函数返回类型中类型注解的冒号（:）进行差异化配置，支持配置为before/after：
    - before/after：布尔类型，可以设置为true或者false，true表示类型注解中的冒号（:）之前/之后需要加空格。

示例：

```
1. "@typescript-eslint/type-annotation-spacing": [
2. "error",
3. {
4. "before": true,
5. "after": true,
6. "overrides": {
7. "colon": {
8. "before": false,
9. "after": true
10. },
11. "arrow": {
12. "before": true,
13. "after": true
14. },
15. "variable": {
16. "before": true,
17. "after": false
18. },
19. "parameter": {
20. "before": false,
21. "after": true
22. },
23. "property": {
24. "before": true,
25. "after": false
26. },
27. "returnType": {
28. "before": true,
29. "after": false
30. }
31. }
32. }
33. ]
```

说明

选项存在优先级，overrides下的配置会覆盖overrides之外的配置：overrides.variable/parameter/property/returnType > overrides.colon/arrow > before/after。

## 正例

```
1. // 默认冒号前无空格，冒号后有空格
2. export const foo1: string = 'bar';

4. export declare function foo2(): string;

6. export class Foo3 {
7. public name: string = 'hello';
8. }
9. // 默认箭头前后都有空格
10. export declare type Foo4 = () => void;
```

## 反例

```
1. // 默认冒号前无空格，冒号后有空格
2. export const foo1 :string = 'bar';

4. export declare function foo2() :string;

6. export class Foo3 {
7. public name :string = 'hello';
8. }
9. // 默认箭头前后都有空格
10. export declare type Foo4 = ()=>void;
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
