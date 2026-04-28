---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-throw-literal
title: @typescript-eslint/no-throw-literal
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-throw-literal
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:39+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:a4d577ce68b0df3096c39b5bacdae1e60405c62494fafe490a570f79d02971bc
---

禁止将字面量作为异常抛出。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-throw-literal": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-throw-literal选项](https://typescript-eslint.nodejs.cn/rules/no-throw-literal#options)。

## 正例

```
1. // 抛出Error对象
2. throw new Error();

4. const e = new Error('error');
5. throw e;

7. const err1 = new Error();
8. throw err1;

10. function err2() {
11. return new Error();
12. }
13. throw err2();

15. class CustomError extends Error {
16. // ...
17. }
18. throw new CustomError();
```

## 反例

```
1. throw 'error';

3. throw 0;

5. throw undefined;

7. throw null;

9. const err1 = new Error();
10. throw 'an ' + err1;

12. const err2 = new Error();
13. throw `${err2}`;

15. const err3 = '';
16. throw err3;

18. function err() {
19. return '';
20. }
21. throw err();
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
