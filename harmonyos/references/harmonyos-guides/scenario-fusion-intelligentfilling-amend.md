---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-intelligentfilling-amend
title: 动态修改ContentType值
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 智能填充服务 > 动态修改ContentType值
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6308a28609303ec93c94a18699e1c821b583c80a5bccaa164c28245106ce0e8c
---

在填写实名信息表单的场景，表单中存在身份证和其他证件输入，其中，多种证件号共用一个输入框，ContentType.ID\_CARD\_NUMBER目前只支持身份证号的推荐、填充，不支持其他类型的证件，需要开发者根据输入场景动态配置输入框的ContentType，只在身份证输入场景下使用ContentType.ID\_CARD\_NUMBER。

## 效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/Vr7juKBQQC-GKu5KfxBGKg/zh-cn_image_0000002558606002.png?HW-CC-KV=V1&HW-CC-Date=20260429T053616Z&HW-CC-Expire=86400&HW-CC-Sign=46B9FD1A9EC58B1DEBC7666D4B6E5364B9281390CF63CD89EDB28A6A34DA37F7)

## 示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { autoFillManager } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct SmartFill {
8. // 与证件号码类型对应的ContentType。在此情况下，默认将ContentType设置为身份证号码对应的类型值。
9. @State type: ContentType | undefined = ContentType.ID_CARD_NUMBER;
10. @State isClicked: boolean = false;

12. build() {
13. Column({ space: 5 }) {
14. Row() {
15. Text('证件类型：').textAlign(TextAlign.End).width('25%')
16. Select([{ value: '身份证' }, { value: '港澳通行证' }])
17. .width('75%')
18. .selected(0)
19. .value('身份证')
20. .onSelect((index: number, value: string) => {
21. // 当用户选择ID类型时，更改与证件号码输入组件对应的ContentType值。
22. hilog.info(0x000, 'testTag', 'Select item changed, value: ' + value + ', index: ' + index);
23. if (value === "身份证") {
24. this.type = ContentType.ID_CARD_NUMBER;
25. } else if (value === "港澳通行证") {
26. this.type = undefined;
27. }
28. hilog.info(0x000, 'testTag', 'ContentType changed, current type: ' + this.type);
29. })
30. }

32. Row() {
33. Text('姓名：').textAlign(TextAlign.End).width('25%')
34. TextInput().width('75%').contentType(ContentType.PERSON_FULL_NAME)
35. }

37. Row() {
38. Text('手机号码：').textAlign(TextAlign.End).width('25%')
39. TextInput().width('75%').contentType(ContentType.PHONE_NUMBER)
40. }

42. Row() {
43. Text('证件号码').textAlign(TextAlign.End).width('25%')
44. TextInput().width('75%').contentType(this.type)
45. }

47. Button('保存')
48. .onClick(() => {
49. if (!this.isClicked) {
50. // 主动触发保存历史表单输入。
51. try {
52. autoFillManager.requestAutoSave(this.getUIContext())
53. } catch (err) {
54. let e: BusinessError = err as BusinessError;
55. hilog.error(0x0000, 'DemoTest', 'error: %{public}d %{public}s', e.code, e.message);
56. }
57. this.isClicked = true;
58. // 设置超时时间以防止重复点击按钮保存历史表单输入。
59. setTimeout(() => {
60. this.isClicked = false;
61. }, 1000)
62. // 或者通过路由跳转其他页面触发保存历史表单输入。
63. this.getUIContext().getRouter().pushUrl({
64. url: 'xxx'
65. })
66. }
67. })
68. .width("50%")
69. }
70. .alignItems(HorizontalAlign.Center)
71. .height('100%')
72. .width('100%')
73. }
74. }
```
