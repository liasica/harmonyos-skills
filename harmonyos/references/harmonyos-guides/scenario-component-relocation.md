---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-component-relocation
title: 控件位置调整场景
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 控件位置调整场景
category: harmonyos-guides
scraped_at: 2026-04-29T13:26:10+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b2db3d0956611982ea3c0b4d126a823d7d93b2dda75503ccbc882ce7459b929d
---

## 设计场景

移动过程中需要实时播报即将移动到的位置，新位置的播报会打断老位置的播报，放置到确定位置后，需要再播报已经放置的位置信息，尽量保证视障用户耳朵听到的信息和我们通过眼睛看到的信息是一致的。

## 开发实例

例如，当前展示的网页书签被托起时，会播报”华为专区已托起”，移动的过程中，根据即将放置的位置播报“移动到华为手机服务|华为官网上面”。应用可调用主动播报的接口来进行主动播报。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/ETG_OD9tRO-9mZIZicg53A/zh-cn_image_0000002558604354.png)

```
1. import accessibility from '@ohos.accessibility';

3. @Entry
4. @Component
5. export struct Rule_2_1_11 {
6. title: string = 'Rule 2.1.11';
7. eventInfo: accessibility.EventInfo = ({
8. type: 'announceForAccessibility',
9. bundleName: 'com.example.pagesrouter',
10. triggerAction: 'common',
11. textAnnouncedForAccessibility: '移动到华为手机服务|华为官网上面'
12. });

14. build() {
15. NavDestination() {
16. Column() {
17. Blank()
18. Button('button')
19. .accessibilityText('主动播报')
20. .align(Alignment.Center)
21. .fontSize(20)
22. .id('button1')
23. .onClick(() => {
24. accessibility.sendAccessibilityEvent(this.eventInfo).then(() => {
25. console.info(`Succeeded in send event, eventInfo is ${JSON.stringify(this.eventInfo)}`);
26. });
27. })
28. Blank()
29. }
30. .width('100%')
31. .height('100%')
32. }
33. .title(this.title)
34. }
35. }
```
