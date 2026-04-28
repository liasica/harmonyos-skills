---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_class-literal-property-style
title: @typescript-eslint/class-literal-property-style
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/class-literal-property-style
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:24+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:92c3de360824575411bee0247ed3def94418038ef4645f6e5b2acba370822d1a
---

建议类中的字面量属性对外暴露时，保持一致的风格。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/class-literal-property-style": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/class-literal-property-style选项](https://typescript-eslint.nodejs.cn/rules/class-literal-property-style/#options)。

## 正例

```
1. class Mx {
2. public readonly myField1 = 'hello';

4. public readonly myField2 = ['a', 'b'];

6. public readonly ['myField3'] = 'hello world';

8. public get myField4() {
9. return `hello ${this.myField1}`;
10. }
11. }

13. export { Mx };
```

## 反例

```
1. class Mx {
2. public static get myField1() {
3. return '1';
4. }

6. public get ['myField2']() {
7. return 'hello world';
8. }
9. }

11. export { Mx };
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
