---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-operation-error
title: 操作错误场景
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 操作错误场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:08+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:531ee50b11c0928ef195f968611a96b03170a745a3cda0f418ff2a5d02735253
---

## 设计场景

比如网络连接错误，或者其他警告信息，不能仅仅以颜色区分，需要实时告诉用户错误提示和改进方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/z20ef-7USZaYhkTgihv_sg/zh-cn_image_0000002583477519.png?HW-CC-KV=V1&HW-CC-Date=20260427T233807Z&HW-CC-Expire=86400&HW-CC-Sign=C07AF16BDC6DD06DFE0815D9A33CEC894CE941BDCF75B8769CFC86DB6FFEB74D)

## 开发实例

如下是一个将连接中断播报出来的例子。

```
1. @Entry
2. @Component
3. export struct Rule_2_1_9 {
4. title: string = 'Rule 2.1.9'

6. build() {
7. NavDestination() {
8. Column() {
9. Flex({
10. direction: FlexDirection.Column,
11. alignItems: ItemAlign.Center,
12. justifyContent: FlexAlign.Center,
13. }) {
14. Row() {
15. Text('Connection state').fontSize(30)
16. }
17. Row() {
18. Radio({ value: 'Radio1', group: 'radioGroup' }).checked(true)
19. .radioStyle({
20. checkedBackgroundColor: Color.Red
21. })
22. .height(50)
23. .width(50)
24. .onChange((isChecked: boolean) => {
25. console.log('Radio1 status is ' + isChecked)
26. })
27. Text('Connection interrupted').fontColor(Color.Red)
28. }.width('80%')
29. .accessibilityGroup(true) //将单选和文本合并到单个对象中
30. }
31. .width('100%')
32. .height('100%')
33. .backgroundColor(Color.White)
34. }
35. }.title(this.title)
36. }
37. }
```
