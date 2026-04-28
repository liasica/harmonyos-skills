---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-transition-to-replace-animateto
title: @performance/hp-arkui-use-transition-to-replace-animateto
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-transition-to-replace-animateto
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:11+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:99aa24727f47d5b7d6213eb96a284bcaf53de3aaec2ad81e8a34c32de7b748d4
---

建议组件转场动画使用transition。

动效丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-use-transition-to-replace-animateto": "warn",
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
4. @State show: boolean = true;

6. build() {
7. Column() {
8. Row() {
9. if (this.show) {
10. Text('value')
11. // Set id to make transition interruptible
12. .id('myText')
13. .transition(TransitionEffect.OPACITY.animation({ duration: 1000 }))
14. }
15. }.width('100%')
16. .height(100)
17. .justifyContent(FlexAlign.Center)
18. Text('toggle state')
19. .onClick(() => {
20. // Through transition, animates the appearance or disappearance of transparency.
21. this.show = !this.show;
22. })
23. }
24. }
25. }
```

## 反例

```
1. @Entry
2. @Component
3. struct MyComponent {
4. @State mOpacity: number = 1;
5. @State show: boolean = true;

7. build() {
8. Column() {
9. Row() {
10. if (this.show) {
11. Text('value')
12. .opacity(this.mOpacity)
13. }
14. }
15. .width('100%')
16. .height(100)
17. .justifyContent(FlexAlign.Center)

19. Text('toggle state')
20. .onClick(() => {
21. this.show = true;
22. animateTo({
23. duration: 1000, onFinish: () => {
24. if (this.mOpacity === 0) {
25. this.show = false;
26. }
27. }
28. }, () => {
29. this.mOpacity = this.mOpacity === 1 ? 0 : 1;
30. })
31. })
32. }
33. }
34. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
