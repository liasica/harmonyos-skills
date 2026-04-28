---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_unbound-method
title: @typescript-eslint/unbound-method
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/unbound-method
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:52+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:092fadf2ce767008d4c75dfb5990d6771172720102042cfd16b1b6acb6f477df
---

强制类作用域中的方法在预期范围内调用。

类方法作为独立变量传递时，不会保留类作用域，“this”不再指代当前类。解决方法是定义为“this: void”或者使用箭头函数。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/unbound-method": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/unbound-method选项](https://typescript-eslint.nodejs.cn/rules/unbound-method/#options)。

## 正例

```
1. class MyClass {
2. public logUnbound(): void {
3. this.logUnbound();
4. }

6. public logBound = () => {
7. this.logUnbound();
8. };
9. }

11. const instance = new MyClass();

13. // logBound will always be bound with the correct scope
14. const logBound = instance.logBound;
15. logBound();
```

## 反例

```
1. class MyClass {
2. public logUnbound(): void {
3. this.logUnbound();
4. }

6. public logBound = () => {
7. this.logUnbound();
8. };
9. }

11. const instance = new MyClass();

13. // logBound will always be bound with the correct scope
14. const logUnbound = instance.logUnbound;
15. logUnbound();
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
