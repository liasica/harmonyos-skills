---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-dynamic-content-change
title: 内容动态变化场景
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 内容动态变化场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:07+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2517ee1b9f1b0bae425cb191023b63d86cd1a75059f69fc138b806c0b50fd9b1
---

## 设计场景

界面上重要内容在动态变化后，需要实时发送变化后的朗读内容。具体地，当界面上内容发生动态变化且其内容对用户具有必要的提示/告知/指导作用，则其发生变化后需对其变化内容进行播报，可调用无障碍提供的主动播报接口进行播报。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/J7RvYrGWQQ6HvdUXq9lmaQ/zh-cn_image_0000002583437563.png?HW-CC-KV=V1&HW-CC-Date=20260427T233806Z&HW-CC-Expire=86400&HW-CC-Sign=DAFF1ECA126D0C701D76ABE6E3626DCD3C1F26F4D9F8F71A1F34582AABBF4CBE)

主动播报接口相关参数说明：

**表1** EventInfo 说明

| 属性 | 类型 | 说明 | 例 |
| --- | --- | --- | --- |
| type | EventType | 主动播报事件类型 | announceForAccessibility |
| bundleName | string | 目标应用名 | 当前应用包名 |
| triggerAction | Action | 触发事件的Action | click或其他都不会有任何影响 |
| textAnnouncedForAccessibility | string | 主动播报的内容 | test123 text |

## 开发实例

```
1. import accessibility from '@ohos.accessibility';

3. @Entry
4. @Component
5. export struct Rule_2_1_7 {
6. title: string = 'Rule 2.1.7';
7. shortText: string = 'Button';
8. longText: string = 'sendAccessibilityEvent';
9. eventInfo: accessibility.EventInfo = ({
10. type: 'announceForAccessibility',
11. bundleName: 'com.example.pagesrouter',
12. triggerAction: 'common',
13. textAnnouncedForAccessibility: 'test123 text'
14. });

16. build() {
17. NavDestination() {
18. Column() {
19. Blank()
20. Button(this.shortText)
21. .accessibilityText(this.longText)
22. .align(Alignment.Center)
23. .fontSize(20)
24. .onClick(() => {
25. accessibility.sendAccessibilityEvent(this.eventInfo).then(() => {
26. console.info(`test123 Succeeded in send event, eventInfo is ${JSON.stringify(this.eventInfo)}`);
27. });
28. })
29. Blank()
30. }
31. .width('100%')
32. .height('100%')
33. }
34. .title(this.title)
35. }
36. }
```
