---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-this-alias
title: @typescript-eslint/no-this-alias
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-this-alias
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:39+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:51057e6ce7cf53a1467768721e00e1c420850d7f1430ecdcd63f77f95adb4998
---

禁止将“this”赋值给一个变量。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-this-alias": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-this-alias选项](https://typescript-eslint.nodejs.cn/rules/no-this-alias/#options)。

## 正例

```
1. const time = 1000;
2. export class CC {
3. public doWork(): void {
4. console.info('work');
5. }

7. public init(): void {
8. setTimeout(function () {
9. this.doWork();
10. });
11. }
12. }
```

## 反例

```
1. // 禁止将this赋值给一个变量
2. const self = this;

4. setTimeout(function () {
5. self.doWork();
6. });
```

## 规则集

```
1. plugin:@typescript-eslint/recommended
2. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
