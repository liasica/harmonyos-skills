---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-update-state-var-between-animatetos-check
title: @performance/update-state-var-between-animatetos-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/update-state-var-between-animatetos-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:19+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:1c55d0c684db0963daf74919903a9c47997e4d755d9523b9a2b7c4bae37d47a5
---

如果多个animateTo之间存在状态更新，会导致执行下一个animateTo之前又存在需要更新的脏节点，可能造成冗余更新。因此不建议在两次animateTo之间进行状态变量更新。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/update-state-var-between-animatetos-check": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. @Entry
2. @Component
3. struct UpdateMultipleProperties {
4. @State w: number = 100
5. @State h: number = 2
6. @State color: Color = Color.Red
7. build() {
8. Column() {
9. Column() {

11. Button('Tap2')
12. .width('100%')
13. .margin({ top: 12 })
14. .onClick(() => {
15. let doTimes = 5;
16. for (let i = 0; i < doTimes; i++) {
17. setTimeout(() => {
18. // Explicitly specify the initial values of all properties to be animated before the animation.
19. this.w = 80
20. this.color = Color.Yellow
21. this.getUIContext().animateTo({ curve: Curve.Sharp, duration: 1000 }, () => {
22. this.w = (this.w === 80 ? 150 : 80);
23. });
24. this.getUIContext().animateTo({ curve: Curve.Linear, duration: 2000 }, () => {
25. this.color = (this.color === Color.Yellow ? Color.Red : Color.Yellow);
26. });
27. // Refresh non-animated properties after animation completes
28. this.h = 5
29. }, 2000 * i)
30. }
31. })
32. Button('Tap3')
33. .width('100%')
34. .margin({ top: 12 })
35. .onClick(() => {
36. let doTimes = 5;
37. for (let i = 0; i < doTimes; i++) {
38. setTimeout(() => {
39. this.getUIContext().animateTo({ curve: Curve.Sharp, duration: 1000 }, () => {
40. this.w = (this.w === 80 ? 150 : 80);
41. });
42. this.getUIContext().animateTo({ curve: Curve.Linear, duration: 2000 }, () => {
43. this.color = (this.color === Color.Yellow ? Color.Red : Color.Yellow);
44. });
45. }, 2000 * i)
46. }
47. })
48. }
49. .justifyContent(FlexAlign.End)
50. .height('25%')
51. }
52. .padding({
53. left: 16,
54. right: 16,
55. bottom: 16
56. })
57. .width('100%')
58. .height('100%')
59. .justifyContent(FlexAlign.Start)
60. }
61. }
```

## 反例

```
1. @Entry
2. @Component
3. struct UpdateMultipleProperties {
4. @State w: number = 100
5. @State h: number = 2
6. @State color: Color = Color.Red
7. build() {
8. Column() {
9. Column() {
10. Button('Tap1')
11. .width('100%')
12. .margin({ top: 12 })
13. .onClick(() => {
14. let doTimes = 5;
15. for (let i = 0; i < doTimes; i++) {
16. setTimeout(() => {
17. this.w = 80
18. this.h = 4
19. this.getUIContext().animateTo({ curve: Curve.Sharp, duration: 1000 }, () => {
20. this.w = (this.w === 80 ? 150 : 80);
21. });
22. // Updating state variables between two animateTo calls
23. this.color = Color.Yellow
24. this.getUIContext().animateTo({ curve: Curve.Linear, duration: 2000 }, () => {
25. this.color = (this.color === Color.Yellow ? Color.Red : Color.Yellow);
26. });
27. }, 2000 * i)
28. }
29. })
30. }
31. .justifyContent(FlexAlign.End)
32. .height('25%')
33. }
34. .padding({
35. left: 16,
36. right: 16,
37. bottom: 16
38. })
39. .width('100%')
40. .height('100%')
41. .justifyContent(FlexAlign.Start)
42. }
43. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
