---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-floating-promises
title: @typescript-eslint/no-floating-promises
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-floating-promises
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:33+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:f475ec795a8ab49deead4c861c637b05c8d19e5c82d99a198ac6dbf553fbe9b5
---

要求正确处理Promise表达式。

floating-promise是指在创建Promise时，没有使用任何代码来处理它可能引发的错误，这是一种不正确的使用方式。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-floating-promises": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-floating-promises选项](https://typescript-eslint.nodejs.cn/rules/no-floating-promises/#options)。

## 正例

```
1. export async function bar() {
2. const promise = new Promise<string>(resolve => {
3. resolve('value');
4. return 'finish';
5. });
6. await promise;

8. Promise.reject('value').catch(() => {
9. console.error('error');
10. });

12. await Promise.reject('value').finally(() => {
13. console.info('finally');
14. });

16. await Promise.all(['1', '2', '3'].map(x => x + '1'));
17. }
```

## 反例

```
1. export async function bar() {
2. const promise = new Promise<string>(resolve => {
3. resolve('value');
4. return 'finish';
5. });
6. promise;

8. Promise.reject('value').catch();

10. await Promise.reject('value').finally();

12. ['1', '2', '3'].map(async x => x + '1');
13. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
