---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-introduction-typical-scenario
title: 典型场景展示
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 智能填充服务 > 典型场景展示
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4dc2eca45441e3c94872c1e1fb2caae7d00fb1205e20ff350b6cd1bdf2d85287
---

如下展示两种智能填充的典型场景。

## 实名购票场景

示例一：智能识别剪贴板内容，一键复制，一键填充。

说明

剪贴板数据源推荐场景目前仅支持中文姓名和中文地址。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/0HsQR6qST5aakjxASD4Nqw/zh-cn_image_0000002552799506.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=DA96FE6DCFC5EE7B59E11A47937E1BF842EAA4AA50460844D7E57D5BC8AFF307)

示例二：根据用户输入，智能关联设备上历史表单输入、华为账号等信息提供输入建议，一键填充。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/DmJ7E8m-QrCM6Qasi1v8Ng/zh-cn_image_0000002583439201.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=B98B1FA97A992FC43A286C1CF319677C4F6DD3B9B72433F66F88B936A08FF24E)

## 填写收货地址场景

示例一：智能识别剪贴板内容，一键复制，一键填充。

说明

剪贴板数据源推荐场景目前仅支持中文姓名和中文地址。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/JKi3bwxgQS2Vng3nqpLutg/zh-cn_image_0000002552959156.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=D1F0F9BD7C3A76FD458D4F2707C1896A725B1A88AE8A030B8B5A3F3975EE2CF6)

示例二：根据用户输入，智能关联设备上历史表单输入、华为账号等信息提供输入建议，一键填充。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/nLBHnHOAS-y0k3ywogypkA/zh-cn_image_0000002583479157.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=0E66F17DEB0E0671FD3E7B8EAC6D3D9F02794EDA9599AA0F8642AFB5A1605035)

## 示例代码

```
1. import { autoFillManager } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct SmartFill {
8. @State isClicked: boolean = false;

10. build() {
11. Column({ space: 5 }) {
12. Row() {
13. Text('昵称：').textAlign(TextAlign.End).width('25%')
14. TextInput().width('75%').contentType(ContentType.NICKNAME).selectionMenuHidden(true)
15. }

17. Row() {
18. Text('姓名：').textAlign(TextAlign.End).width('25%')
19. TextInput().width('75%').contentType(ContentType.PERSON_FULL_NAME).selectionMenuHidden(true)
20. }

22. Row() {
23. Text('手机号码：').textAlign(TextAlign.End).width('25%')
24. TextInput().width('75%').contentType(ContentType.PHONE_NUMBER).selectionMenuHidden(true)
25. }

27. Row() {
28. Text('邮箱：').textAlign(TextAlign.End).width('25%')
29. TextInput().width('75%').contentType(ContentType.EMAIL_ADDRESS).selectionMenuHidden(true)
30. }

32. Row() {
33. Text('身份证号：').textAlign(TextAlign.End).width('25%')
34. TextInput().width('75%').contentType(ContentType.ID_CARD_NUMBER).selectionMenuHidden(true)
35. }

37. Row() {
38. Text('地址：').textAlign(TextAlign.End).width('25%')
39. TextInput().width('75%').contentType(ContentType.FORMAT_ADDRESS).selectionMenuHidden(true)
40. }

42. Button('保存')
43. .onClick(() => {
44. if (!this.isClicked) {
45. // 主动触发保存历史表单输入。
46. try {
47. autoFillManager.requestAutoSave(this.getUIContext())
48. } catch (err) {
49. let e: BusinessError = err as BusinessError;
50. hilog.error(0x0000, 'DemoTest', 'error: %{public}d %{public}s', e.code, e.message);
51. }
52. this.isClicked = true;
53. // 设置超时时间以防止重复点击按钮保存历史表单输入。
54. setTimeout(() => {
55. this.isClicked = false;
56. }, 1000)
57. // 或者通过路由跳转其他页面触发保存历史表单输入。
58. this.getUIContext().getRouter().pushUrl({
59. url: 'xxx'
60. })
61. }
62. })
63. .width("50%")
64. }
65. .alignItems(HorizontalAlign.Center)
66. .height('100%')
67. .width('100%')
68. }
69. }
```

说明

* 智能填充在页面发生跳转的时候，或者手动触发保存逻辑的时候，方可触发保存表单逻辑。
* 剪贴板文本内容识别功能现已实现超过90%的准确率。尽管如此，我们认识到在特定场景下仍可能出现识别误差。为了提升填表数据的准确性，我们建议在关键环节引入增强校验。这些校验措施包括但不限于：

  1. 格式校验：自动检测输入格式，确保数据符合预设标准。
  2. 确认提示：在提交前通过弹窗提示用户再次确认信息，避免输入错误。
* 若在页面中也提供了弹窗提醒填充建议的功能，为避免弹窗冲突，建议将对应输入组件的[enableAutoFill](../harmonyos-references/ts-basic-components-textinput.md#enableautofill11)属性设置为"false"以关闭智能填充功能。
