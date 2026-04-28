---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-disable-screen-reading-focus
title: 禁用屏幕朗读焦点的场景
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 禁用屏幕朗读焦点的场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:07+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7eaa939e67c4a86987847b7399be3894f337dfa5e55da133ec0dfc3e6aadcab7
---

## 设计场景

装饰性的控件一般为分隔符、占位符和美化图标等，这类图形元素仅仅起到调整页面布局或装饰性效果，并不会向用户传达有效的信息或提供交互功能，删除后不影响指引用户体验。可以设置控件的无障碍组accessibilityGroup、无障碍重要性accessibilityLevel、组件可见性visibility等属性将其设置为无障碍不可聚焦，这样在屏幕朗读模式下控件就不会获取焦点和朗读。

通过以下无障碍属性可以改变控件可聚焦属性：

* accessibilityGroup(true) 用于多个组件的组合，拼接所有子组件text文本并设置到无障碍组节点，除非子组件设置了accessibilityLevel为yes，否则子组件默认一定都不可聚焦。
* accessibilityLevel("no")用于组件设置不可聚焦，忽略当前组件的文本属性和点击属性。
* accessibilityLevel("no-hide-descendants")用于组件及其所有子组件设置不可聚焦，忽略当前组件及其所有子组件的文本属性和点击属性。

## 开发实例

以下代码同时显示“Broadcast”和“No broadcast”消息，但当ScreenReader处于“打开”状态时，message可被聚焦，但message1将不被聚焦。

```
1. @Entry
2. @Component
3. export struct Rule_2_1_2 {
4. title: string = 'Rule 2.1.2'
5. @State message: string = 'Broadcast';
6. @State message1: string = 'No broadcast';

8. build() {
9. NavDestination() {
10. Column() {
11. Row() {
12. Text(this.message)
13. .fontSize(40)
14. .fontWeight(FontWeight.Bold)
15. .fontColor(Color.Blue)
16. .margin({
17. left: 40
18. })
19. }
20. .width('100%')
21. .height('50%')
22. Row() {
23. Text(this.message1)
24. .fontSize(40)
25. .fontWeight(FontWeight.Bold)
26. .fontColor(Color.Grey)
27. .margin({
28. left: 40
29. }).accessibilityLevel("no") // use for component
30. }
31. //.accessibilityGroup(true)
32. //.accessibilityLevel("no-hide-descendants") // use for container
33. // 可以使用这两行代替28行的accessibilityLevel("no")
34. .width('100%')
35. .height('50%')
36. }
37. .height('100%')
38. }
39. .title(this.title)
40. }
41. }
```
