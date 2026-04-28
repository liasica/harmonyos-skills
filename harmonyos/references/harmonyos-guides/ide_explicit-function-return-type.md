---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_explicit-function-return-type
title: @typescript-eslint/explicit-function-return-type
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/explicit-function-return-type
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:26+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:d9c3a509de744bf6c5d38870269f52ed192c6bbdf17e10cf238b13c6e8358edb
---

函数和类方法需要显式的定义返回类型。

该规则仅支持对.ts文件进行检查。通过配置选项，可以支持对.ets文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/explicit-function-return-type": "error"
5. }
6. }
```

## 选项

该规则支持配置以下选项：

```
1. type Options = [
2. {
3. // 是否忽略.ets文件的检查，默认为false，不检查.ets文件
4. allowArkTS?: boolean
5. }
6. ]
```

配置示例：

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/explicit-function-return-type": ["error", { "allowArkTS": true }]
5. }
6. }
```

其余配置详情请参考[@typescript-eslint/explicit-function-return-type选项](https://typescript-eslint.nodejs.cn/rules/explicit-function-return-type/#options)。

## 正例

```
1. // No return value should be expected (void)
2. function test(): void {
3. return;
4. }

6. // A return value of type number
7. const fn = function (): number {
8. return Number.MAX_VALUE;
9. };

11. // A return value of type string
12. const arrowFn = (): string => 'test';

14. class Test {
15. // No return value should be expected (void)
16. public method(): void {
17. return;
18. }
19. }

21. export { test, fn, arrowFn, Test };
```

## 反例

```
1. // Should indicate that no value is returned (void)
2. function test() {
3. return;
4. }

6. // Should indicate that a number is returned
7. const fn = function () {
8. return Number.MAX_VALUE;
9. };

11. // Should indicate that a string is returned
12. const arrowFn = () => 'test';

14. class Test {
15. // Should indicate that no value is returned (void)
16. public method() {
17. return;
18. }
19. }

21. export { test, fn, arrowFn, Test };
```

## 规则集

```
1. plugin:@typescript-eslint/recommended
2. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
