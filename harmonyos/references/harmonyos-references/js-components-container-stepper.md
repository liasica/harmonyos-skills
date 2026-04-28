---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-stepper
title: stepper
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 容器组件 > stepper
category: harmonyos-references
scraped_at: 2026-04-28T08:02:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8cdfd0fa1d80f60648a6f97b71dd1d6689358cd6fe574b253e972ea8c85d97a9
---

说明

从API version 5开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

步骤导航器。当完成一个任务需要多个步骤时，可以使用步骤导航器展示当前进展。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

仅支持<stepper-item>子组件。

说明

步骤导航器内的步骤顺序按照子组件<stepper-item>的顺序进行排序。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| index | number | 0 | 设置步骤导航器步骤显示第几个stepper-item子组件，默认显示第一个stepper-item。 |

## 样式

PhonePC/2in1TabletTVWearable

支持[通用样式](js-components-common-styles.md)。

说明

stepper组件默认占满父容器大小，建议父组件使用应用窗口大小（或者父组件为根节点）来优化体验。

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| finish | 无 | 当步骤导航器最后一个步骤完成时,触发该事件。 |
| skip | 无 | 当前步骤导航器下一步按钮状态为skip，即可跳过时，点击右侧跳过按钮触发该事件。 |
| change | { prevIndex: prevIndex, index: index} | 当用户点击步骤导航器的左边或者右边按钮进行步骤切换时触发该事件，prevIndex表示老步骤的序号，index表示新步骤的序号。 |
| next | { index: index, pendingIndex: pendingIndex } | 当用户点击下一步按钮时触发该事件，index表示当前步骤序号，pendingIndex表示将要跳转的序号，该事件有返回值，返回值格式为：{ pendingIndex: pendingIndex }，可以通过指定pendingIndex来修改下一个步骤使用哪个stepper-item子组件。 |
| back | { index: index, pendingIndex: pendingIndex } | 当用户点击上一步按钮时触发该事件，index表示当前步骤序号，pendingIndex表示将要跳转的序号，该事件有返回值，返回值格式为Object: { pendingIndex: pendingIndex }，可以通过指定pendingIndex来修改上一个步骤使用哪个stepper-item子组件。 |

## 方法

PhonePC/2in1TabletTVWearable

除支持[通用方法](js-components-common-methods.md)外，支持如下方法：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| setNextButtonStatus | { status: string, label: label } | 设置当前步骤中下一步按钮的文本与状态，参数中label为指定按钮文本，status指定按钮状态，status可选值为：  - normal：正常状态，下一步文本按钮正常显示，可点击进入下一个步骤；  - disabled：不可用状态，下一步文本按钮灰度显示，不可点击进入下一个步骤；  - waiting：等待状态，下一步文本按钮不显示，使用等待进度条，不可点击进入下一个步骤；  - skip：跳过状态，下一步文本按钮显示跳过按钮，点击时会跳过剩下步骤。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <stepper class="stepper" id="mystepper" onnext="nextclick" onback="backclick" onchange="statuschange"
4. onfinish="finish" onskip="skip" style="height : 100%;">
5. <stepper-item class="stepper-item" label="{{ label_1 }}">
6. <div class="item">
7. <text>Page One</text>
8. <button type="capsule" class="button" value="change status" onclick="setRightButton"></button>
9. </div>
10. </stepper-item>
11. <stepper-item class="stepper-item" label="{{ label_2 }}">
12. <div class="item">
13. <text>Page Two</text>
14. <button type="capsule" class="button" value="change status" onclick="setRightButton"></button>
15. </div>
16. </stepper-item>
17. <stepper-item class="stepper-item" label="{{ label_3 }}">
18. <div class="item">
19. <text>Page Three</text>
20. <button type="capsule" class="button" value="change status" onclick="setRightButton"></button>
21. </div>
22. </stepper-item>
23. </stepper>
24. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. align-items: center;
5. height: 100%;
6. width: 100%;
7. background-color: #f7f7f7;
8. }
9. .stepper{
10. width: 100%;
11. height: 100%;
12. }
13. .stepper-item {
14. width: 100%;
15. height: 100%;
16. flex-direction: column;
17. align-items: center;
18. }
19. .item{
20. width: 90%;
21. height: 86%;
22. margin-top: 80px;
23. background-color: white;
24. border-radius: 60px;
25. flex-direction: column;
26. align-items: center;
27. padding-top: 160px;
28. }
29. text {
30. font-size: 78px;
31. color: #182431;
32. opacity: 0.4;
33. }
34. .button {
35. width: 40%;
36. margin-top: 100px;
37. justify-content: center;
38. }
```

```
1. // xxx.js
2. import prompt from '@ohos.promptAction';

4. export default {
5. data: {
6. label_1:
7. {
8. prevLabel: 'BACK',
9. nextLabel: 'NEXT',
10. status: 'normal'
11. },
12. label_2:
13. {
14. prevLabel: 'BACK',
15. nextLabel: 'NEXT',
16. status: 'normal'
17. },
18. label_3:
19. {
20. prevLabel: 'BACK',
21. nextLabel: 'NEXT',
22. status: 'normal'
23. }
24. },
25. setRightButton(e) {
26. this.$element('mystepper').setNextButtonStatus({
27. status: 'waiting', label: 'SKIP'
28. });
29. },
30. nextclick(e) {
31. var index = {
32. pendingIndex: e.pendingIndex
33. }
34. return index;
35. },
36. backclick(e) {
37. var index = {
38. pendingIndex: e.pendingIndex
39. }
40. return index;
41. },
42. statuschange(e) {
43. prompt.showToast({
44. message: '上一步序号' + e.prevIndex + '当前序号' + e.index
45. })
46. },
47. finish() {
48. prompt.showToast({
49. message: '最后一步已完成'
50. })
51. },
52. skip() {
53. prompt.showToast({
54. message: 'skip触发'
55. })
56. }
57. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/gCoQB5XXS5aWNtJdhU8y5Q/zh-cn_image_0000002552800536.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000257Z&HW-CC-Expire=86400&HW-CC-Sign=DAE8BA04B43BFC7BAD079DADA861DFAB78EB1DFAB5FE6C866E2244D0EFB79216)
