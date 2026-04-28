---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unused-vars
title: @typescript-eslint/no-unused-vars
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unused-vars
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:42+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:bf4c4d82fd9ca7bc3d0bcd168c276f4938588c31127c73141e5de63b7fc29c9c
---

禁止定义未使用的变量。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-unused-vars": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-unused-vars选项](https://eslint.nodejs.cn/docs/rules/no-unused-vars#选项)。

## 正例

```
1. const x = 10;
2. console.info(`${x}`);

4. ((foo) => {
5. return foo;
6. })();

8. const num = 50;
9. let myFunc1: () => number = () => num;
10. myFunc1 = () => setTimeout(() => {
11. // myFunc is considered used
12. myFunc1();
13. }, num);
```

## 反例

```
1. const x = 10;

3. ((foo) => {
4. return 'hello';
5. })();

7. const num = 50;
8. const myFunc1: () => number = () => num;
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
