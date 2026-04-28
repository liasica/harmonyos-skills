---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-focus-position-setting
title: 重新设置新焦点位置的场景
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 重新设置新焦点位置的场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:40845434aacbf749dd1ac8447a2cf3a6c1bacf2e8e84223ccad6587d2ae05865
---

## 设计场景

当前焦点所在的控件消失或者隐藏后，需要重新设置新的焦点位置。一般情况下，新焦点应该在原控件位置的下一个控件上，不应该跳变到前面的控件。应用可以调用主动聚焦的接口对想要聚焦的组件进行主动聚焦。

主动聚焦接口相关参数说明

**表1** **EventInfo 说明**

| 属性 | 类型 | 说明 | 例 |
| --- | --- | --- | --- |
| type | EventType | 主动聚焦事件类型 | requestFocusForAccessibility |
| bundleName | string | 目标应用名 | 当前应用包名 |
| triggerAction | Action | 触发事件的Action | click或其他都不会有任何影响 |
| customId | string | 组件id | abc345 |

## 开发实例

```
1. import accessibility from '@ohos.accessibility';

3. @Entry
4. @Component
5. export struct Rule_2_1_12 {
6. title: string = 'Rule 2.1.12';
7. eventInfo: accessibility.EventInfo = ({
8. type: 'requestFocusForAccessibility',
9. bundleName: 'com.example.pagesrouter',
10. triggerAction: 'common',
11. customId: 'button1'
12. });

14. build() {
15. NavDestination() {
16. Column() {
17. Blank()
18. Button('button1')
19. .accessibilityText('点击聚焦到button2')
20. .align(Alignment.Center)
21. .fontSize(20)
22. .id('button1')
23. .onClick(() => {
24. this.eventInfo.customId = 'button2';
25. accessibility.sendAccessibilityEvent(this.eventInfo).then(() => {
26. console.info(`Succeeded in send event, eventInfo is ${JSON.stringify(this.eventInfo)}`);
27. });
28. })
29. Blank().height('10px')
30. Button('button2')
31. .accessibilityText('点击聚焦到button1')
32. .align(Alignment.Center)
33. .fontSize(20)
34. .id('button2')
35. .onClick(() => {
36. this.eventInfo.customId = 'button1';
37. accessibility.sendAccessibilityEvent(this.eventInfo).then(() => {
38. console.info(`Succeeded in send event, eventInfo is ${JSON.stringify(this.eventInfo)}`);
39. });
40. })
41. Blank()
42. }
43. .width('100%')
44. .height('100%')
45. }
46. .title(this.title)
47. }
48. }
```
