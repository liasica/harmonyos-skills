---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_init-declarations
title: @typescript-eslint/init-declarations
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/init-declarations
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0e2839ff59ce43015453d140fbba12201f9c4189804549fe6d9065dc4d958e78
---

禁止或者要求在变量声明中进行初始化。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/init-declarations": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/init-declarations选项](https://eslint.nodejs.cn/docs/rules/init-declarations#选项)。

## 正例

```
1. // 默认变量必须在声明时初始化
2. export function foo() {
3. console.info('hello');
4. }

6. export const bar = 1;
7. export const qux = 3;
```

## 反例

```
1. // 默认变量必须在声明时初始化
2. export function foo() {
3. console.info('hello');
4. }

6. export let bar: string;
7. export let qux: number;
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
