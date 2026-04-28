---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-member-access
title: @typescript-eslint/no-unsafe-member-access
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unsafe-member-access
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:41+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:e30a1511d0cc0b142beb2c16a1b1742dc47fdb20fe58702dd3f287bc9d9e87ff
---

禁止成员访问“any”类型的值。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-unsafe-member-access": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. declare const properlyTyped: { prop: { a: string } };

3. export const v1 = properlyTyped.prop.a;

5. const key = 'a';
6. export const v2 = properlyTyped.prop[key];

8. const arr = ['1', '2', '3'];
9. let idx = 1;
10. export const v3 = arr[idx];
11. export const v4 = arr[idx++];
```

## 反例

```
1. declare const properlyTyped: { prop: { a: any } };

3. export const v1 = properlyTyped.prop.a;

5. const key = 'a' as any;
6. export const v2 = properlyTyped.prop[key];

8. const arr = ['1', '2', '3'];
9. let idx: any = 1;
10. export const v3 = arr[idx];
11. export const v4 = arr[idx++];
```

## 规则集

```
1. plugin:@typescript-eslint/recommended
2. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
