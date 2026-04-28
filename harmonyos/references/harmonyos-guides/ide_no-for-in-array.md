---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-for-in-array
title: @typescript-eslint/no-for-in-array
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-for-in-array
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:33+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:6440e68dfb098c3f4a90383df1e1d45613781c09337e7ea8cbbf6ad8415e1fab
---

禁止使用 for-in 循环来遍历数组元素。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-for-in-array": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. declare const array: string[];

3. for (const value of array) {
4. console.log(value);
5. }

7. array.forEach((value) => {
8. console.log(value);
9. });
```

## 反例

```
1. declare const array: string[];

3. for (const i in array) {
4. console.log(array[i]);
5. }

7. for (const i in array) {
8. console.log(i, array[i]);
9. }
```

## 规则集

```
1. plugin:@typescript-eslint/recommended
2. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
