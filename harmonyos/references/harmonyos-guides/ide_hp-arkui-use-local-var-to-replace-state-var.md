---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-local-var-to-replace-state-var
title: @performance/hp-arkui-use-local-var-to-replace-state-var
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-local-var-to-replace-state-var
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:09+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:953577a2f6b7926d4dc8fde6a6923271b6221745f81544645b3dc86958fd6550
---

建议使用临时变量替换状态变量。

通用丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-use-local-var-to-replace-state-var": "warn",
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
4. @State message: string = '';
5. appendMsg(newMsg: string) {
6. let message = this.message;
7. message += newMsg;
8. message += ";";
9. message += "<br/>";
10. this.message = message;
11. }
12. build() {
13. // 业务代码...
14. }
15. }
```

## 反例

```
1. @Entry
2. @Component
3. struct MyComponent {
4. @State message: string = '';
5. appendMsg(newMsg: string) {
6. this.message += newMsg;
7. this.message += ";";
8. this.message += "<br/>";
9. }
10. build() {
11. // 业务代码...
12. }
13. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
