---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_keyword-spacing
title: @typescript-eslint/keyword-spacing
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/keyword-spacing
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:27+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:33823ab1f3ac1539727148bdcbf03599c9a9b90815436b1c06580f74d2f80307
---

强制在关键字之前和关键字之后保持一致的空格风格。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/keyword-spacing": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/keyword-spacing选项](https://eslint.nodejs.cn/docs/rules/keyword-spacing#选项)。

## 正例

```
1. function isSatisfy1(): boolean {
2. return true;
3. }

5. function isSatisfy2(): boolean {
6. return false;
7. }
8. // 默认关键字前至少需要一个空格，关键字后至少需要一个空格
9. if (isSatisfy1()) {
10. //...
11. } else if (isSatisfy2()) {
12. //...
13. } else {
14. //...
15. }
```

## 反例

```
1. function isSatisfy1(): boolean {
2. return true;
3. }

5. function isSatisfy2(): boolean {
6. return false;
7. }
8. // 默认关键字前至少需要一个空格，关键字后至少需要一个空格
9. if (isSatisfy1()) {
10. //...
11. }else if(isSatisfy2()) {
12. //...
13. }else{
14. //...
15. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
