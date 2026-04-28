---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-enum-initializers
title: @typescript-eslint/prefer-enum-initializers
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-enum-initializers
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a7beb401249e7ce986c50c16aa5f6df3966666c4c9fcab35a59a12cd9f432839
---

推荐显式初始化每个枚举成员值。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/prefer-enum-initializers": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export enum Status {
2. open = 'Open',
3. close = 'Close'
4. }

6. export enum Direction {
7. up = '1',
8. down = '2'
9. }

11. export enum Color {
12. red = 'Red',
13. green = 'Green',
14. blue = 'Blue'
15. }
```

## 反例

```
1. export enum Status {
2. open,
3. close
4. }

6. export enum Direction {
7. up,
8. down
9. }

11. export enum Color {
12. red,
13. green,
14. blue
15. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
