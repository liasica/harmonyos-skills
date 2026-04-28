---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_indent
title: @hw-stylistic/indent
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/indent
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:26+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:4900ba178e596f6dc3c827f08abc426e9a701186c46423f7b2f071e601be4bb6
---

强制switch语句中的case和default缩进一层。该规则仅检查.ets文件类型。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@hw-stylistic/indent": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. enum E {
2. a = 'a',
3. b = 'b',
4. c = 'c'
5. }

7. export function test(e: E) {
8. switch (e) {
9. case E.a:
10. console.info('doSomething');
11. break;
12. case E.b:
13. case E.c:
14. console.info('doSomething');
15. break;
16. default:
17. console.info('doSomething');
18. }
19. }
```

## 反例

```
1. enum E {
2. a = 'a',
3. b = 'b',
4. c = 'c'
5. }

7. export function test(e: E) {
8. switch (e) {
9. // Expected indentation of 2 relative to switch.
10. case E.a:
11. // Expected indentation of 2 relative to case.
12. console.info('hello');
13. // Expected indentation of 2 relative to case.
14. break;
15. case E.b:
16. console.info('hello');
17. break;
18. case E.c:
19. // Expected indentation of 2 relative to case.
20. console.info('hello');
21. break;
22. default:
23. // Expected indentation of 2 relative to default.
24. console.info('hello');
25. }
26. }
```

## 规则集

```
1. "plugin:@hw-stylistic/recommended"
2. "plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
