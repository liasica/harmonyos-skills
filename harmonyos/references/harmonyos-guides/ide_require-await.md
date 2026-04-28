---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_require-await
title: @typescript-eslint/require-await
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/require-await
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:49+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:a4c7b9868b9c25fc110b4d2f7607d74e48d09e5fc74ca9bafd446dc1ed5f88a0
---

异步函数必须包含“await”。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/require-await": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. async function doSomething(): Promise<void> {
2. return Promise.resolve();
3. }

5. export async function foo() {
6. await doSomething();
7. }

9. export function baz() {
10. doSomething().catch(() => {
11. console.info('error');
12. });
13. }
```

## 反例

```
1. async function doSomething(): Promise<void> {
2. return Promise.resolve();
3. }

5. export async function foo() {
6. doSomething();
7. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
