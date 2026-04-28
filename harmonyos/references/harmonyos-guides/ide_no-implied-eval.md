---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-implied-eval
title: @typescript-eslint/no-implied-eval
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-implied-eval
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:33+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:86854d9eeba61c86fbddae38ef0f01620ca4bab1fbf12c00e25151a326e73cd4
---

禁止使用类似“eval()”的方法。

setTimeout()、setInterval()、setImmediate()或者execScript()这些函数可以接受一个字符串作为其第一个参数，比如

```
1. setTimeout('alert(`Hi!`);', 100);
```

这种行为被认为是隐式“eval()”，不推荐使用。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-implied-eval": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. function alert(arg: string) {
2. console.log(arg);
3. }

5. const time = 100;

7. setTimeout(() => {
8. alert('Hi!');
9. }, time);

11. setInterval(() => {
12. alert('Hi!');
13. }, time);

15. const fn = () => {
16. console.info('fn');
17. };
18. setTimeout(fn, time);

20. class Foo {
21. public static fn = () => {
22. console.info('static');
23. };

25. public meth() {
26. console.info('method');
27. }
28. }

30. setTimeout(Foo.fn, time);
```

## 反例

```
1. const time = 100;
2. setTimeout('alert(`Hi!`);', time);

4. setInterval('alert(`Hi!`);', time);

6. const fn1 = '() = {}';
7. setTimeout(fn1, time);

9. const fn2 = () => {
10. return 'x = 10';
11. };
12. setTimeout(fn2(), time);

14. export const fn3 = new Function('a', 'b', 'return a + b');
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
