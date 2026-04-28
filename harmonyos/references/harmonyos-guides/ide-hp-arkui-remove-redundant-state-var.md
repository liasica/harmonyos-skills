---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkui-remove-redundant-state-var
title: @performance/hp-arkui-remove-redundant-state-var
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-remove-redundant-state-var
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:07+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:78eb6fc4bab9c27658a3269a82c472e434748325ab5d280fbdd3d45ca45b044d
---

建议移除不关联UI组件的状态变量设置。

通用丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-remove-redundant-state-var": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. @Entry
2. @Component
3. struct MyComponent {
4. @State message: string = "";

6. appendMsg(newMsg: string): string {
7. this.message += newMsg;
8. return this.message;
9. }

11. build() {
12. Column() {
13. Stack() {
14. Text(this.message)
15. }
16. .backgroundColor("black")
17. .width(200)
18. .height(400)

20. Button("move")
21. }
22. }
23. }
```

## 反例

```
1. @Entry
2. @Component
3. struct MyComponent {
4. @State message: string = "";

6. appendMsg(newMsg: string): string {
7. this.message += newMsg;
8. return this.message;
9. }

11. build() {
12. Column() {
13. Stack() {
14. }
15. .backgroundColor("black")
16. .width(200)
17. .height(400)

19. Button("move")
20. }
21. }
22. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
