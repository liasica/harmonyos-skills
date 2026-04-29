---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-monopolize-events
title: 事件独占控制
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 交互属性 > 触摸交互控制 > 事件独占控制
category: harmonyos-references
scraped_at: 2026-04-29T13:51:26+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:100332a226c4c23e06c5990500e8fc215b3efcd6c650602d2724c66bc0963052
---

设置组件是否独占事件，事件范围包括组件自带的事件和开发者自定义的点击、触摸、手势事件。

在一个窗口内，设置了独占控制的组件上的事件如果首先响应，则本次交互只允许此组件上设置的事件响应，窗口内其他组件上的事件不会响应。

说明

从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## monopolizeEvents

PhonePC/2in1TabletTVWearable

monopolizeEvents(monopolize: boolean): T

设置组件是否独占事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monopolize | boolean | 是 | 组件是否独占事件。true表示组件独占事件，false表示组件不独占事件。  默认值：false  **说明：**  1、如果第一根手指触发了组件事件独占，在抬起前又按下了一根手指，则第二根手指的交互继续处于组件独占状态，依次类推。  2、如果开发者通过[parallelGesture](ts-gesture-settings.md#parallelgesture)绑定了与子组件同时触发的手势，如[PanGesture](ts-basic-gestures-pangesture.md)，子组件设置了独占控制且首个响应事件，则父组件的手势不会响应。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例通过配置monopolizeEvents实现组件是否独占事件。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. @State message: string = 'set monopolizeEvents false';
6. @State messageOut: string = ' ';
7. @State messageInner: string = ' ';
8. @State monopolize: boolean = false;

10. build() {
11. Column() {
12. Text(this.message)
13. .fontSize(22)
14. .margin(10)
15. Text(this.messageOut)
16. .fontSize(22)
17. .margin(10)
18. Text(this.messageInner)
19. .fontSize(22)
20. .margin(10)
21. Button('clean')
22. .fontSize(22)
23. .margin(10)
24. // 通过button的点击事件来切换内层column的独占控制属性
25. .onClick(() => {
26. this.messageOut = " "
27. this.messageInner = " "
28. })
29. Button('change monopolizeEvents')
30. .fontSize(22)
31. .margin(10)
32. // 通过button的点击事件来切换内层column的独占控制属性
33. .onClick(() => {
34. this.monopolize = !this.monopolize
35. if (!this.monopolize) {
36. this.message = "set monopolizeEvents false"
37. } else {
38. this.message = "set monopolizeEvents true"
39. }
40. })
41. Column() {
42. Column() {
43. }
44. // this.monopolize是true时，点击内层column只会触发自身的触摸事件，不会触发外层column的触摸事件
45. // this.monopolize是false时，点击内层column会同时触发自身的触摸事件和外层column的触摸事件
46. .monopolizeEvents(this.monopolize)
47. .width('100%')
48. .height('40%')
49. .backgroundColor(Color.Blue)
50. // 内层column绑定触摸事件
51. .onTouch((event: TouchEvent) => {
52. if (event.type == TouchType.Down) {
53. console.info("inner column touch down")
54. this.messageInner = "inner column touch down"
55. }
56. })
57. }
58. .backgroundColor(Color.Gray)
59. .height('100%')
60. .width('100%')
61. // 外层column绑定触摸事件
62. .onTouch((event) => {
63. if (event.type == TouchType.Down) {
64. console.info("outside column touch down")
65. this.messageOut = "outside column touch down"
66. }
67. })
68. }
69. .height('100%')
70. }
71. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/oxlAgrw5T7WecSbKhKW7Eg/zh-cn_image_0000002558766066.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055125Z&HW-CC-Expire=86400&HW-CC-Sign=D1E4F563BDAACF83CAA47C7126314E22B10A19ACED337D9A12148C8266458BF3)
