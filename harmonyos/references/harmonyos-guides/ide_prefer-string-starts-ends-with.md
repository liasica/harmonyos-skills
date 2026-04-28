---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-string-starts-ends-with
title: @typescript-eslint/prefer-string-starts-ends-with
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-string-starts-ends-with
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:46+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:db0117e4346b0fbafeecbdd5fbe4378205796755c436aba3fa4d5a4a050d588e
---

强制使用“String#startsWith”和“String#endsWith”而不是其他检查子字符串的等效方法。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/prefer-string-starts-ends-with": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. declare const foo: string;

3. // starts with
4. foo.startsWith('bar');

6. // ends with
7. foo.endsWith('bar');
```

## 反例

```
1. declare const foo: string;
2. declare const index: number;
3. // starts with
4. foo[index] === 'b';
5. foo.charAt(index) === 'b';
6. foo.indexOf('bar') === index;
7. foo.slice(index) === 'bar';
8. foo.substring(index) === 'bar';
9. foo.match(/^bar/) !== null;
10. /^bar/.test(foo);

12. // ends with
13. foo[foo.length - index] === 'b';
14. foo.charAt(foo.length - index) === 'b';
15. foo.lastIndexOf('bar') === foo.length - index;
16. foo.slice(-index) === 'bar';
17. foo.substring(foo.length - index) === 'bar';
18. foo.match(/bar$/) !== null;
19. /bar$/.test(foo);
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
