---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-type-alias
title: @typescript-eslint/no-type-alias
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-type-alias
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:39+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:7fcbd34ad84fc8e94c1f1fd5c653301b150b639dfa152cc81e2c93e5a1a2fdb6
---

禁止使用类型别名。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-type-alias": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-type-alias选项](https://typescript-eslint.nodejs.cn/rules/no-type-alias/#options)。

## 正例

```
1. interface Person {
2. readonly firstName: string;
3. readonly lastName: string;
4. readonly age: number;
5. }

7. export function addPerson(person: Person): Person {
8. return person;
9. }
```

## 反例

```
1. // 不允许使用类型别名，建议使用接口替代
2. type Person = {
3. readonly firstName: string;
4. readonly lastName: string;
5. readonly age: number;
6. };

8. export function addPerson(person: Person): Person {
9. return person;
10. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
