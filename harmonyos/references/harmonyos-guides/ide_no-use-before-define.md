---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-use-before-define
title: @typescript-eslint/no-use-before-define
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-use-before-define
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:43+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:633ed20a8d8e87a951dbff42b3a425fd00ec6634e7718ac9de079462dc49c7e9
---

禁止在变量声明之前使用变量。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-use-before-define": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-use-before-define选项](https://eslint.nodejs.cn/docs/rules/no-use-before-define#选项)。

## 正例

```
1. const a = '10';
2. console.info(a);

4. function ff(): void {
5. console.info('function');
6. }
7. ff();

9. const foo = '1';
10. export { foo };
```

## 反例

```
1. console.info(a);
2. const a = '10';

4. ff();
5. function ff(): void {
6. console.info('function');
7. }

9. export { foo };
10. const foo = '1';
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
