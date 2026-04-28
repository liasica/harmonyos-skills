---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_member-ordering
title: @typescript-eslint/member-ordering
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/member-ordering
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:28+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:dc1fe86a7811ea913fab6f9b91b305f100806da81f0e4aabd6e6a50867ca1597
---

要求类、接口和类型字面量中成员的排序方式保持一致的风格。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/member-ordering": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/member-ordering选项](https://typescript-eslint.nodejs.cn/rules/member-ordering/#options)。

## 正例

```
1. // 默认排序规则：field-constructor-method
2. export class Foo2 {
3. // -> field
4. protected static e: string = '';

6. public d: string = '';

8. private readonly c: string = '';

10. // -> constructor
11. public constructor() {
12. console.info('constructor');
13. }

15. // -> method
16. public static a(): void {
17. console.info('static method');
18. }

20. public b(): void {
21. console.info(this.c);
22. }
23. }
```

## 反例

```
1. // 默认排序规则：field-constructor-method
2. export class Foo2 {
3. // -> method
4. public static a(): void {
5. console.info('static method');
6. }

8. public b(): void {
9. console.info(this.c);
10. }

12. // -> field
13. protected static e: string = '';

15. private readonly c: string = '';

17. public d: string = '';

19. // -> constructor
20. public constructor() {
21. console.info('constructor');
22. }
23. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
