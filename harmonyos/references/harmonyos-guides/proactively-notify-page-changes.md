---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/proactively-notify-page-changes
title: 主动通知页面变化的场景
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 主动通知页面变化的场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ccb853c08d6ada1c3d6d649b8129ecd8056034bff27395abe6245bab2561759b
---

## 设计场景

应用自定义的页面可以通过堆叠的方式覆盖在原页面上，实现页面切换的效果，但是系统无法自动识别到这种场景，可能会导致焦点丢失。此时，应用可以调用主动通知页面变化的接口，通知屏幕朗读在新页面上寻找节点聚焦。该接口支持指定新页面的根节点，如果指定了有效的根节点，则从该根节点开始找首焦点聚焦，如果未指定，则默认从当前窗口根节点开始找首焦点聚焦。

## 主动通知页面变化接口相关参数说明：

**表1** EventInfo 说明

| 属性 | 类型 | 说明 | 例 |
| --- | --- | --- | --- |
| type | EventType | 主动通知页面变化事件类型。 | pageActive |
| bundleName | string | 目标应用名。 | 'com.example.accessibilityinfo' |
| triggerAction | Action | 触发事件的Action。 | common |
| customId | string | 自定义页面根节点id。 | 'abc345' |

## 开发实例

如下示例实现一个自定义页面切换，通过改变[Stack](../harmonyos-references/ts-container-stack.md)子组件Z序的方式实现切换页面的效果：

```
1. import accessibility from '@ohos.accessibility';

3. @Entry
4. @Component
5. struct Rule_2_1_16 {
6. title: string = 'Rule 2.1.16';
7. // 定义状态变量，用于控制顶层显示的层数
8. @State topLayer: number = 0;

10. // 定义自定义页面
11. @Builder
12. Layer(text: string, index: number) {
13. Column() {
14. Column() {
15. Text(text)
16. .fontSize(24)
17. .fontWeight(FontWeight.Bold)
18. .margin({ bottom: 20 })
19. Text(`${text} 测试节点1`)
20. Text(`${text} 测试节点2`)
21. Text(`${text} 测试节点3`)
22. // 创建按钮用于切换页面
23. Button(`页面切换${index}`)
24. .onClick(() => {
25. // 判断当前顶层，在0与1之间切换
26. if (this.topLayer === 0) {
27. this.topLayer = 1;
28. } else {
29. this.topLayer = 0;
30. }
31. // 定义事件信息描述，事件类型为pageActive，页面根节点id为`Layer_${this.topLayer}`
32. const eventInfo: accessibility.EventInfo = ({
33. type: 'pageActive',
34. bundleName: 'com.example.accessibilityinfo',
35. triggerAction: 'common',
36. customId: `Layer_${this.topLayer}`
37. });
38. // 发送主动通知页面变化的事件
39. accessibility.sendAccessibilityEvent(eventInfo).then(() => {
40. console.info(`pageActive event send Successed, customId=Layer_${this.topLayer}.`); // 发送成功日志
41. });
42. })
43. }
44. // 指定自定义节点id，用于标识页面根节点
45. .id('Layer_' + index)
46. }
47. .height('100%')
48. .width('100%')
49. .backgroundColor(index === 0 ? Color.Red : Color.Green)
50. .justifyContent(FlexAlign.Center)
51. .alignItems(HorizontalAlign.Center)
52. .borderRadius(16)
53. .padding(20)
54. // 修改页面Z序，用于实现页面切换效果
55. .zIndex(this.topLayer === index ? 1 : 0)
56. // 根据当前页面是否顶层显示，指定自定义页面节点是否无障碍可识别，若否，则设置为不可识别
57. .accessibilityLevel(this.topLayer === index ? 'no' : 'no-hide-descendants')
58. }

60. build() {
61. NavDestination() {
62. Column() {
63. Stack() {
64. this.Layer('页面0', 0)
65. this.Layer('页面1', 1)
66. }
67. }
68. }
69. }
70. }
```
