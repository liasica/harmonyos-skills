---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-limit-refresh-scope
title: @performance/hp-arkui-limit-refresh-scope（已下线）
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-limit-refresh-scope（已下线）
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:04+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:3c851a5124d9b93007f94dee28ac2e0d972a989f7144414e2a004e4b65697185
---

建议减少组件刷新范围。该规则已于5.0.3.500版本下线。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-limit-refresh-scope": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. @Entry
2. @Component
3. struct StackExample6 {
4. @State isVisible : boolean = false;
5. build() {
6. Column() {
7. Stack({alignContent: Alignment.Top}) {
8. Text().width('100%').height('70%').backgroundColor(0xd2cab3)
9. .align(Alignment.Center).textAlign(TextAlign.Center);
10. // 此处省略100个相同的背景Text组件
11. Stack() {
12. if (this.isVisible) {
13. Text('New Page').height("70%").backgroundColor(0xd2cab3)
14. .align(Alignment.Center).textAlign(TextAlign.Center);
15. }
16. }.width('100%').height('70%')
17. }
18. Button("press").onClick(() => {
19. this.isVisible = !(this.isVisible);
20. })
21. }
22. }
23. }
```

## 反例

```
1. @Entry
2. @Component
3. struct StackExample5 {
4. @State isVisible : boolean = false;
5. build() {
6. Column() {
7. Stack({alignContent: Alignment.Top}) {
8. Text().width('100%').height('70%').backgroundColor(0xd2cab3)
9. .align(Alignment.Center).textAlign(TextAlign.Center);
10. // 此处省略100个相同的背景Text组件
11. if (this.isVisible) {
12. Text('New Page').height("70%").backgroundColor(0xd2cab3)
13. .align(Alignment.Center).textAlign(TextAlign.Center);
14. }
15. }
16. Button("press").onClick(() => {
17. this.isVisible = !(this.isVisible);
18. })
19. }
20. }
21. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
