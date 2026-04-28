---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-scale-to-replace-attr-animateto
title: @performance/hp-arkui-use-scale-to-replace-attr-animateto
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-scale-to-replace-attr-animateto
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:10+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:42c66b2a3b94470488a6e85137c31a83ebe182a1c7425ef701db68929ad8611f
---

建议组件布局改动时使用图形变换属性动画。

动效丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-use-scale-to-replace-attr-animateto": "warn",
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
4. @State textScaleX: number = 1;
5. @State textScaleY: number = 1;
6. build() {
7. Column() {
8. Text()
9. .backgroundColor(Color.Blue)
10. .fontColor(Color.White)
11. .fontSize(20)
12. .width(10)
13. .height(10)
14. .scale({ x: this.textScaleX, y: this.textScaleY })
15. .margin({ top: 100 })
16. Button('图形变换属性')
17. .backgroundColor(Color.Blue)
18. .fontColor(Color.White)
19. .fontSize(20)
20. .margin({ top: 60 })
21. .borderRadius(30)
22. .padding(10)
23. .onClick(() => {
24. animateTo({ duration: 1000 }, () => {
25. this.textScaleX = 10;
26. this.textScaleY = 10;
27. })
28. })
29. }
30. }
31. }
```

## 反例

```
1. @Entry
2. @Component
3. struct MyComponent {
4. @State textWidth: number = 10;
5. @State textHeight: number = 10;
6. build() {
7. Column() {
8. Text()
9. .backgroundColor(Color.Blue)
10. .fontColor(Color.White)
11. .fontSize(20)
12. .width(this.textWidth)
13. .height(this.textHeight)
14. Button('布局属性')
15. .backgroundColor(Color.Blue)
16. .fontColor(Color.White)
17. .fontSize(20)
18. .margin({ top: 30 })
19. .borderRadius(30)
20. .padding(10)
21. .onClick(() => {
22. animateTo({ duration: 1000 }, () => {
23. this.textWidth = 100;
24. this.textHeight = 100;
25. })
26. })
27. }
28. }
29. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
