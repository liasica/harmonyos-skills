---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-loop-func
title: @typescript-eslint/no-loop-func
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-loop-func
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:35+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:4b89b8e26658c7c5b82ecfaff631edaa740a60166b9947277ba6951167bccabb
---

禁止在循环语句内包含不安全引用的函数声明。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-loop-func": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. const a = function(): void {
2. console.info('hello');
3. };

5. for (let i = 10; i; i--) {
6. a();
7. }

9. for (let i = 10; i; i--) {
10. const b = function(): void {
11. a();
12. }; // OK, no references to variables in the outer scopes.
13. b();
14. }
```

## 反例

```
1. const num = 10;
2. for (let i = num; i; i--) {
3. // 变量i是不安全的引用
4. (function(): number {
5. return i;
6. })();
7. }

9. let i1 = 0;
10. while (i1 < num) {
11. // 变量i是不安全的引用
12. const a = function(): number {
13. return i1;
14. };
15. a();

17. i1++;
18. }

20. let i2 = 0;
21. do {
22. // 变量i是不安全的引用
23. function a(): number {
24. return i2;
25. }
26. a();

28. i2++;
29. } while (i2 < num);
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
