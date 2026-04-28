---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-combine-same-arg-animateto
title: @performance/hp-arkui-combine-same-arg-animateto
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-combine-same-arg-animateto
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:03+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:23b6965711e290131a624fa0031727f7bb74b803ab502a45d0a32e898d07307d
---

建议动画参数相同时使用同一个animateTo。

动效丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-combine-same-arg-animateto": "warn",
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
4. @State textWidth: number = 200;
5. @State color: Color = Color.Red;

7. func() {
8. this.getUIContext().animateTo({ curve: Curve.Sharp, duration: 1000 }, () => {
9. this.textWidth = (this.textWidth === 100 ? 200 : 100);
10. this.color = (this.color === Color.Yellow ? Color.Red : Color.Yellow);
11. });
12. }

14. build() {
15. Column() {
16. Row()
17. .width(this.textWidth)
18. .height(10)
19. .backgroundColor(this.color)
20. Text('click')
21. .onClick(() => {
22. this.func();
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

## 反例

```
1. @Entry
2. @Component
3. struct MyComponent {
4. @State textWidth: number = 200;
5. @State color: Color = Color.Red;

7. func1() {
8. animateTo({ curve: Curve.Sharp, duration: 1000 }, () => {
9. this.textWidth = (this.textWidth === 100 ? 200 : 100);
10. });
11. }

13. func2() {
14. animateTo({ curve: Curve.Sharp, duration: 1000 }, () => {
15. this.color = (this.color === Color.Yellow ? Color.Red : Color.Yellow);
16. });
17. }

19. build() {
20. Column() {
21. Row()
22. .width(this.textWidth)
23. .height(10)
24. .backgroundColor(this.color)
25. Text('click')
26. .onClick(() => {
27. this.func1();
28. this.func2();
29. })
30. }
31. .width('100%')
32. .height('100%')
33. }
34. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
