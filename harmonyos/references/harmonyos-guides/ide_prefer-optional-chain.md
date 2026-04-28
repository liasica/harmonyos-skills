---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-optional-chain
title: @typescript-eslint/prefer-optional-chain
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-optional-chain
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:48+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:fed57c0bfbf5dd2d57921938f9ceaab88a0299519a963aacdcfcae5371275eee
---

强制使用链式可选表达式，而不是链式逻辑与、否定逻辑或、或空对象。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/prefer-optional-chain": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/prefer-optional-chain选项](https://typescript-eslint.nodejs.cn/rules/prefer-optional-chain/#options)。

## 正例

```
1. class Foo {
2. public a?: Foo = new Foo();

4. public b?: Foo = new Foo();

6. public c?: Foo = new Foo();

8. public method?(): void {
9. console.info('method');
10. }
11. }

13. const foo = new Foo();
14. export const c = foo.a?.b?.c;
15. foo.a?.b?.method?.();
```

## 反例

```
1. class Foo {
2. public a?: Foo = new Foo();

4. public b?: Foo = new Foo();

6. public c?: Foo = new Foo();

8. public method?(): void {
9. console.info('method');
10. }
11. }

13. const foo = new Foo();
14. let c = foo.a;
15. c = c && c.b;
16. c = c && c.c;
17. export { c };
18. if (foo.a && foo.a.b && foo.a.b.method) {
19. foo.a.b.method();
20. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
