---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-attribute-update-refresh-scope
title: @performance/hp-arkui-use-attributeUpdater-control-refresh-scope
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-attributeUpdater-control-refresh-scope
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:08+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:61b05f96012c3313da105ae958c5748c982a24f183b588b7a4a33de696860d75
---

建议使用attributeUpdater精准控制组件属性的刷新。

通用丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-use-attributeUpdater-control-refresh-scope": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import { AttributeUpdater } from '@ohos.arkui.modifier';
2. // 源码文件，请以工程实际为准
3. import { MyDataSource } from './MyDataSource';
4. import { FriendMoment } from './data/DataEntry'

6. export class MyTextUpdater extends AttributeUpdater<TextAttribute> {
7. private color: string | number | Resource = "";

9. constructor(color: string | number | Resource) {
10. super();
11. this.color = color
12. }

14. initializeModifier(instance: TextAttribute): void {
15. instance.fontColor(this.color)
16. }
17. }

19. @Component
20. export struct UpdaterComponent {
21. private momentData: MyDataSource = new MyDataSource();

23. build() {
24. Column() {
25. Text('use MyTextUpdater')
26. List({ space: 5 }) {
27. LazyForEach(this.momentData, (moment: FriendMoment) => {
28. ListItem() {
29. OneMomentNoModifier({ color: moment.color })
30. .onClick(() => {
31. console.log(`my id is ${moment.id}`)
32. })
33. }
34. }, (moment: FriendMoment) => moment.id)
35. }.width('100%')
36. .height('100%')
37. .cachedCount(5)
38. }
39. }
40. }

42. @Reusable
43. @Component
44. export struct OneMomentNoModifier {
45. color: string | number | Resource = "";
46. textUpdater: MyTextUpdater | null = null;

48. aboutToAppear(): void {
49. this.textUpdater = new MyTextUpdater(this.color);
50. }

52. aboutToReuse(params: Record<string, Object>): void {
53. this.color = params.color as string | number | Resource;
54. this.textUpdater?.attribute?.fontColor(this.color);
55. }

57. build() {
58. Column() {
59. Text('This is the title')
60. Text('This is the internal text')
61. .attributeModifier(this.textUpdater)
62. .textAlign(TextAlign.Center)
63. .fontStyle(FontStyle.Normal)
64. .fontSize(13)
65. .lineHeight(30)
66. .opacity(0.6)
67. .margin({ top: 10 })
68. .fontWeight(30)
69. .clip(false)
70. .backgroundBlurStyle(BlurStyle.NONE)
71. .foregroundBlurStyle(BlurStyle.NONE)
72. .borderWidth(1)
73. .borderColor(Color.Pink)
74. .borderStyle(BorderStyle.Solid)
75. .alignRules({
76. 'top': { 'anchor': '__container__', 'align': VerticalAlign.Top },
77. 'left': { 'anchor': 'image', 'align': HorizontalAlign.End }
78. })
79. }
80. }
81. }
```

## 反例

```
1. // 源码文件，请以工程实际为准
2. import { MyDataSource } from './MyDataSource';
3. import { FriendMoment } from './data/DataEntry'

5. @Component
6. export struct UpdaterComponent {
7. private momentData: MyDataSource = new MyDataSource();

9. build() {
10. Column() {
11. Text('use nothing')
12. List({ space: 5 }) {
13. LazyForEach(this.momentData, (moment: FriendMoment) => {
14. ListItem() {
15. OneMomentNoModifier({ color: moment.color })
16. .onClick(() => {
17. console.log(`my id is ${moment.id}`)
18. })
19. }
20. }, (moment: FriendMoment) => moment.id)
21. }
22. .width("100%")
23. .height("100%")
24. .cachedCount(5)
25. }
26. }
27. }

29. @Reusable
30. @Component
31. export struct OneMomentNoModifier {
32. @State color: string | number | Resource = "";

34. aboutToReuse(params: Record<string, Object>): void {
35. this.color = params.color as string | number | Resource;
36. }

38. build() {
39. Column() {
40. Text('This is the title')
41. Text('This is the internal text')
42. .fontColor(this.color)
43. .textAlign(TextAlign.Center)
44. .fontStyle(FontStyle.Normal)
45. .fontSize(13)
46. .lineHeight(30)
47. .opacity(0.6)
48. .margin({ top: 10 })
49. .fontWeight(30)
50. .clip(false)
51. .backgroundBlurStyle(BlurStyle.NONE)
52. .foregroundBlurStyle(BlurStyle.NONE)
53. .borderWidth(1)
54. .borderColor(Color.Pink)
55. .borderStyle(BorderStyle.Solid)
56. .alignRules({
57. 'top': { 'anchor': '__container__', 'align': VerticalAlign.Top },
58. 'left': { 'anchor': 'image', 'align': HorizontalAlign.End }
59. })
60. }
61. }
62. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
