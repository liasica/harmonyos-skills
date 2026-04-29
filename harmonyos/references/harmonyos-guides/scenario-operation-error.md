---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-operation-error
title: 操作错误场景
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 操作错误场景
category: harmonyos-guides
scraped_at: 2026-04-29T13:26:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:302fedc813856832bc3a7907037721b429f0c2c1105841509eb42d3a847ef7d5
---

## 设计场景

比如网络连接错误，或者其他警告信息，不能仅仅以颜色区分，需要实时告诉用户错误提示和改进方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/FdXV0Lv3QCeCvv8SaZZdCA/zh-cn_image_0000002558764010.png?HW-CC-KV=V1&HW-CC-Date=20260429T052608Z&HW-CC-Expire=86400&HW-CC-Sign=19FCFDA36B687225A3A23D6D0BCB7D14E7B6E12A8B2397E20951291D126E6803)

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
