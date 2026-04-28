---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_semi-spacing
title: @hw-stylistic/semi-spacing
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:30+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:828a86222e64cbcbbfcb8518d8d5798270bbaaaf0c04b38ae8688784ecd79883
---

强制分号之前不加空格。该规则仅检查.ets文件类型。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@hw-stylistic/semi-spacing": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export {x, test, C};

3. const x = 10;

5. function test(size: number): number {
6. let sum = 0;
7. for (let a = 0; a < size; a++) {
8. sum += a;
9. }
10. return sum;
11. }

13. class C {
14. public name: string = 'hello';
15. }
```

## 反例

```
1. // Unexpected whitespace before semicolon.
2. export {x, test, C} ;

4. // Unexpected whitespace before semicolon.
5. const x = 10 ;

7. function test(size: number): number {
8. let sum = 0;
9. // Unexpected whitespace before semicolon.
10. // Unexpected whitespace before semicolon.
11. for (let a = 0 ; a < size ; a++) {
12. sum += a;
13. }
14. // Unexpected whitespace before semicolon.
15. return sum ;
16. }

18. class C {
19. // Unexpected whitespace before semicolon.
20. public name: string = 'hello' ;
21. }
```

## 规则集

```
1. "plugin:@hw-stylistic/recommended"
2. "plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
