---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-dupe-class-members
title: @typescript-eslint/no-dupe-class-members
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-dupe-class-members
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:30+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:5156c9ffdc1ebf929e908e3e6b6985ae9167e9c86b341f65c3ef9ab580a42c23
---

不允许重复的类成员。如果类成员中有同名的声明，最后一个声明会覆盖其他声明，可能会导致意外行为。

编译器会自动校验该规则检查的代码问题，新建项目时可以不开启此规则。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-dupe-class-members": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. /*eslint no-dupe-class-members: "error"*/
2. export class A {
3. public bar() {
4. console.info('bar');
5. }

7. public qux() {
8. console.info('qux');
9. }
10. }

12. export class B {
13. private name: string = 'bar';

15. public get bar() {
16. return this.name;
17. }

19. public set bar(value) {
20. this.name = value;
21. }
22. }

24. export class E {
25. public static bar() {
26. console.info('static bar');
27. }

29. public bar() {
30. console.info('method bar');
31. }
32. }
```

## 反例

```
1. /*eslint no-dupe-class-members: "error"*/
2. export class A {
3. public bar() {
4. console.info('bar');
5. }

7. public bar() {
8. console.info('bar');
9. }
10. }

12. export class B {
13. private readonly name: string = 'bar';

15. public get bar() {
16. return this.name;
17. }

19. public bar() {
20. return this.name;
21. }
22. }

24. export class E {
25. public static bar() {
26. console.info('static bar');
27. }

29. public static bar() {
30. console.info('static bar');
31. }
32. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
