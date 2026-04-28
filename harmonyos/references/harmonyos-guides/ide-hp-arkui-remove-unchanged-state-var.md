---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkui-remove-unchanged-state-var
title: @performance/hp-arkui-remove-unchanged-state-var
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-remove-unchanged-state-var
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:07+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:6d59289e69e617439200cbe4c8b8456348bec5745030b114e35c7c8bade72e69
---

建议移除未改变的状态变量设置。

通用丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-remove-unchanged-state-var": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. class Translate {
2. translateX: number = 20;
3. }

5. @Component
6. struct Title {
7. build() {
8. Row() {
9. // 本地资源 icon.png
10. Image($r('app.media.icon'))
11. .width(50)
12. .height(50)
13. Text("Title")
14. .fontSize(20)
15. }
16. }
17. }

19. @Entry
20. @Component
21. struct MyComponent {
22. @State translateObj: Translate = new Translate();
23. // 直接使用一般变量即可
24. button_msg: string = "i am button";

26. build() {
27. Column() {
28. Title()
29. Stack() {
30. }
31. .backgroundColor("black")
32. .width(200)
33. .height(400)

35. Button(this.button_msg)
36. .onClick(() => {
37. animateTo({
38. duration: 50
39. }, () => {
40. this.translateObj.translateX = (this.translateObj.translateX + 50) % 150
41. })
42. })
43. }
44. .translate({
45. x: this.translateObj.translateX
46. })
47. }
48. }
```

## 反例

```
1. @Observed
2. class Translate {
3. translateX: number = 20;
4. }

6. @Component
7. struct Title {
8. build() {
9. Row() {
10. // 本地资源 icon.png
11. Image($r('app.media.icon'))
12. .width(50)
13. .height(50)
14. Text("Title")
15. .fontSize(20)
16. }
17. }
18. }

20. @Entry
21. @Component
22. struct MyComponent {
23. @State translateObj: Translate = new Translate();
24. @State button_msg: string = "i am button";

26. build() {
27. Column() {
28. Title()
29. Stack() {
30. }
31. .backgroundColor("black")
32. .width(200)
33. .height(400)

35. // 这里只是用了状态变量button_msg的值，没有任何写的操作
36. Button(this.button_msg)
37. .onClick(() => {
38. animateTo({
39. duration: 50
40. }, () => {
41. this.translateObj.translateX = (this.translateObj.translateX + 50) % 150
42. })
43. })
44. }
45. .translate({
46. x: this.translateObj.translateX
47. })
48. }
49. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
