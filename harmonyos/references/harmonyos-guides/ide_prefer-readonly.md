---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-readonly
title: @typescript-eslint/prefer-readonly
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-readonly
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:47+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:59ece901b20cc2a8d53c1444e4eb582126d1a4f1419bdcd82707667eb93dc567
---

如果私有成员从未在构造函数之外进行修改，则要求将其标记为“只读”。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/prefer-readonly": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/prefer-readonly选项](https://typescript-eslint.nodejs.cn/rules/prefer-readonly/#options)。

## 正例

```
1. export class Container {
2. // Public members might be modified externally
3. public publicMember: boolean = true;

5. // Protected members might be modified by child classes
6. protected protectedMember: number = Number.MAX_VALUE;

8. // This is modified later on by the class
9. private modifiedLater = 'unchanged';

11. public mutate() {
12. this.modifiedLater = 'mutated';
13. }
14. }
```

## 反例

```
1. export class Container {
2. // These member variables could be marked as readonly
3. private neverModifiedMember = true;

5. private onlyModifiedInConstructor: number;

7. // Private parameter properties can also be marked as readonly
8. private neverModifiedParameter: string;

10. public constructor(
11. onlyModifiedInConstructor: number,
12. // Private parameter properties can also be marked as readonly
13. neverModifiedParameter: string,
14. ) {
15. this.neverModifiedParameter = neverModifiedParameter;
16. this.onlyModifiedInConstructor = onlyModifiedInConstructor;
17. }
18. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
