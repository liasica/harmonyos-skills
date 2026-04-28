---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-avoid-empty-callback
title: @performance/hp-arkui-avoid-empty-callback
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-avoid-empty-callback
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:02+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:0c9c2bb0eab64cf1740b588d229ccb3470a68254e0fd33c146d0f5fb94386c16
---

避免设置空的系统回调监听。

根据ArkUI编程规范，建议修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-avoid-empty-callback": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. @Component
2. struct MyComponent {
3. doSomething() {
4. //业务逻辑
5. }

7. build() {
8. Button('Click', { type: ButtonType.Normal, stateEffect: true })
9. .onClick(() => {
10. this.doSomething()
11. })
12. }
13. }
```

## 反例

```
1. @Component
2. struct MyComponent {
3. build() {
4. Button('Click', { type: ButtonType.Normal, stateEffect: true })
5. .onClick(() => {
6. // 无业务逻辑
7. })
8. }
9. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
