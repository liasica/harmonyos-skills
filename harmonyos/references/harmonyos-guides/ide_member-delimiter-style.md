---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_member-delimiter-style
title: @typescript-eslint/member-delimiter-style
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/member-delimiter-style
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:28+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:4a02f45e1ea1450e4bc43799ba083cfd9011eb6f6b087a2f1eeef8f1572033fd
---

要求接口和类型别名中的成员之间使用特定的分隔符。

支持定义的分隔符有三种：分号、逗号、无分隔符。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/member-delimiter-style": "error"
5. }
6. }
```

## 选项

支持配置以下选项：

```
1. type BaseOption = {
2. multiline: {
3. delimiter: 'none' | 'semi' | 'comma';
4. requireLast: boolean;
5. };
6. singleline: {
7. delimiter: 'semi' | 'comma';
8. requireLast: boolean;
9. };
10. }

12. type Options = {
13. multiline: {
14. delimiter: 'none' | 'semi' | 'comma';
15. requireLast: boolean;
16. };
17. singleline: {
18. delimiter: 'semi' | 'comma';
19. requireLast: boolean;
20. };
21. overrides: {
22. interface: BaseOption;
23. typeLiteral: BaseOption;
24. };
25. multilineDetection: 'brackets' | 'last-member';
26. }
```

* multiline/singleline：对象类型，分别定义多行/单行的interface/type alias成员之间分隔符风格，支持以下两种属性：
  + delimiter：枚举类型，定义分隔符风格，取值范围如下：
    - none：表示不需要加分隔符。
    - semi：表示建议使用分号作为分隔符。
    - comma：表示建议使用逗号作为分隔符。
  + requireLast：布尔类型，可以设置为true或者false，true表示最后一个成员的末尾需要加分隔符，false表示最后一个成员的末尾不加分隔符。

* multilineDetection：枚举类型，判断多行的依据，可取值如下：
  + brackets：默认值，表示interface/type alias中存在换行，即视为多行。
  + last-member：表示interface/type alias的最后一个成员与右括号（“}”）处于同一行，则视为单行。
* overrides：对象类型，可以针对interface/type alias进行差异化配置，支持以下两种属性：
  + interface：对象类型，可以对interface进行差异化配置，配置方式同multiline/singleline。
  + typeLiteral：对象类型，可以对type alias进行差异化配置，配置方式同multiline/singleline。

示例：

```
1. "@typescript-eslint/member-delimiter-style": [
2. "error",
3. {
4. // 多行interface/type alias使用逗号作为分隔符，最后一个成员末尾不加分隔符
5. "multiline": {
6. "delimiter": "comma",
7. "requireLast": false
8. },
9. // 单行interface/type alias使用分号作为分隔符，最后一个成员末尾需要加分隔符
10. "singleline": {
11. "delimiter": "semi",
12. "requireLast": true
13. },
14. // 分别对interface和type alias进行差异化配置
15. overrides: {
16. interface: {
17. "multiline": {
18. "delimiter": "comma",
19. "requireLast": false
20. },
21. "singleline": {
22. "delimiter": "semi",
23. "requireLast": true
24. }
25. },
26. typeLiteral: {
27. "multiline": {
28. "delimiter": "comma",
29. "requireLast": false
30. },
31. "singleline": {
32. "delimiter": "semi",
33. "requireLast": true
34. }
35. }
36. },
37. multilineDetection: "brackets",
38. },
39. ]
```

## 正例

```
1. // 默认接口/类型别名定义为多行的场景下，每个成员应以分号 (;) 分隔。 最后一个成员必须有一个分隔符。
2. // 默认接口/类型别名定义为单行的场景下，每个成员应以分号 (;) 分隔。最后一个成员不能有分隔符。
3. // 接口/类型别名中的任何换行符都会使其成为多行。
4. export interface Foo1 {
5. name: string;

7. greet(): string;
8. }

10. export interface Foo2 { name: string }
```

## 反例

```
1. // missing semicolon delimiter
2. export interface Foo {
3. name: string
4. greet(): string
5. }

7. // using incorrect delimiter
8. export interface Bar {
9. name: string,
10. greet(): string,
11. }

13. // missing last member delimiter
14. export interface Baz {
15. name: string;
16. greet(): string
17. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
