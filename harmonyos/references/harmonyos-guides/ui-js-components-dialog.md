---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-dialog
title: dialog开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 容器组件 > dialog开发指导
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:45+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8b8212b706a342d05f2178c66aabb9b598a5fb37dc195acd1abb68432315c587
---

dialog组件用于创建自定义弹窗，通常用来展示用户当前需要或用户必须关注的信息或操作。具体用法请参考[dialog API](../harmonyos-references/js-components-container-dialog.md)。

## 创建dialog组件

在pages/index目录下的hml文件中创建一个dialog组件，并添加Button组件来触发dialog。dialog组件仅支持width、height、margin、margin-[left|top|right|bottom]、margin-[start|end]样式。

```
1. <!-- xxx.hml -->
2. <div class="doc-page">
3. <dialog class="dialogClass" id="dialogId" dragable="true">
4. <div class="content">
5. <text>this is a dialog</text>
6. </div>
7. </dialog>
8. <button value="click me" onclick="openDialog"></button>
9. </div>
```

```
1. /* xxx.css */
2. .doc-page {
3. width:100%;
4. height:100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. background-color: #F1F3F5;
9. }
10. .dialogClass{
11. width: 80%;
12. height: 250px;
13. margin-start: 1%;
14. }
15. .content{
16. width: 100%;
17. height: 250px;
18. justify-content: center;
19. background-color: #e8ebec;
20. border-radius: 20px;
21. }
22. text{
23. width: 100%;
24. height: 100%;
25. text-align: center;
26. }
27. button{
28. width: 70%;
29. height: 60px;
30. }
```

```
1. // xxx.js
2. export default {
3. //Touch to open the dialog box.
4. openDialog(){
5. this.$element('dialogId').show()
6. },
7. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/G5m89Rt5RsS26IYOF5nMgg/zh-cn_image_0000002558604922.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052844Z&HW-CC-Expire=86400&HW-CC-Sign=F9570B5E0ADC29CAC9F02473ACA6DA230AAB1B0D42988CD8E44F4E3ECEB08AF0)

## 设置弹窗响应

开发者点击页面上非dialog的区域时，将触发cancel事件而关闭弹窗。同时也可以通过对dialog添加show和close方法来显示和关闭弹窗。

```
1. <!-- xxx.hml -->
2. <div class="doc-page">
3. <dialog class="dialogClass" id="dialogId" oncancel="cancelDialog">
4. <div class="dialogDiv">
5. <text>dialog</text>
6. <button value="confirm" onclick="confirmClick"></button>
7. </div>
8. </dialog>
9. <button value="click me" onclick="openDialog"></button>
10. </div>
```

```
1. /* xxx.css */
2. .doc-page {
3. width:100%;
4. height:100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. background-color: #F1F3F5;
9. }
10. .dialogClass{
11. width: 80%;
12. height: 300px;
13. margin-start: 1%;
14. }
15. .dialogDiv{
16. width: 100%;
17. flex-direction: column;
18. justify-content: center;
19. align-self: center;
20. }
21. text{
22. height: 100px;
23. align-self: center;
24. }
25. button{
26. align-self: center;
27. margin-top: 20px;
28. width: 60%;
29. height: 80px;
30. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. cancelDialog(e){
5. promptAction.showToast({
6. message: 'dialogCancel'
7. })
8. },
9. openDialog(){
10. this.$element('dialogId').show()
11. promptAction.showToast({
12. message: 'dialogShow'
13. })
14. },
15. confirmClick(e) {
16. this.$element('dialogId').close()
17. promptAction.showToast({
18. message: 'dialogClose'
19. })
20. },
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/luQRQQ1MSZuJXOlWlxGg1Q/zh-cn_image_0000002589324447.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052844Z&HW-CC-Expire=86400&HW-CC-Sign=C8213C5EC258235D0DD15A09DAAE1E9D959D97A3F8BB6D367C88F29B64E7230C)

说明

* 仅支持单个子组件。
* dialog属性、样式均不支持动态更新。
* dialog组件不支持focusable、click-effect属性。

## 场景示例

在本场景中，开发者可以通过dialog组件实现一个日程表。弹窗在打开状态下，利用[textarea](../harmonyos-references/js-components-basic-textarea.md)组件输入当前日程，点击确认按钮后获取当前时间并保存输入文本。最后以列表形式将各日程进行展示。

```
1. <!-- xxx.hml -->
2. <div class="doc-page">
3. <text style="margin-top: 60px;margin-left: 30px;">
4. <span>{{date}} events</span>
5. </text>
6. <div class="btnDiv">
7. <button type="circle" class="btn" onclick="addSchedule">+</button>
8. </div>
9. <!--  for Render events data  -->
10. <list style="width: 100%;">
11. <list-item type="item" for="scheduleList" style="width:100%;height: 200px;">
12. <div class="scheduleDiv">
13. <text class="text1">{{date}}  event</text>
14. <text class="text2">{{$item.schedule}}</text>
15. </div>
16. </list-item>
17. </list>
18. <dialog id="dateDialog" oncancel="cancelDialog" >
19. <div class="dialogDiv">
20. <div class="innerTxt">
21. <text class="text3">{{date}}</text>
22. <text class="text4">New event</text>
23. </div>
24. <textarea placeholder="Event information" onchange="getSchedule" class="area" extend="true"></textarea>
25. <div class="innerBtn">
26. <button type="text" value="Cancel" onclick="cancelSchedule" class="innerBtn"></button>
27. <button type="text" value="OK" onclick="setSchedule" class="innerBtn"></button>
28. </div>
29. </div>
30. </dialog>
31. </div>
```

```
1. /* xxx.css */
2. .doc-page {
3. flex-direction: column;
4. background-color: #F1F3F5;
5. }
6. .btnDiv {
7. width: 100%;
8. height: 200px;
9. flex-direction: column;
10. align-items: center;
11. justify-content: center;
12. }
13. .btn {
14. radius:60px;
15. font-size: 100px;
16. background-color: #1E90FF;
17. }
18. .scheduleDiv {
19. width: 100%;
20. height: 200px;
21. flex-direction: column;
22. justify-content: space-around;
23. padding-left: 55px;
24. }
25. .text1 {
26. color: #000000;
27. font-weight: bold;
28. font-size: 39px;
29. }
30. .text2 {
31. color: #a9a9a9;
32. font-size: 30px;
33. }
34. .dialogDiv {
35. flex-direction: column;
36. align-items: center;
37. }
38. .innerTxt {
39. width: 320px;
40. height: 160px;
41. flex-direction: column;
42. align-items: center;
43. justify-content: space-around;
44. }
45. .text3 {
46. font-family: serif;
47. color: #1E90FF;
48. font-size: 38px;
49. }
50. .text4 {
51. color: #a9a9a9;
52. font-size: 33px;
53. }
54. .area {
55. width: 320px;
56. border-bottom: 1px solid #1E90FF;
57. }
58. .innerBtn {
59. width: 320px;
60. height: 120px;
61. justify-content: space-around;
62. text-color: #1E90FF;
63. }
```

```
1. // xxx.js
2. var info = null;
3. import promptAction from '@ohos.promptAction';
4. export default {
5. data: {
6. curYear:'',
7. curMonth:'',
8. curDay:'',
9. date:'',
10. schedule:'',
11. scheduleList:[]
12. },
13. onInit() {
14. // Obtain the current date.
15. var date = new Date();
16. this.curYear = date.getFullYear();
17. this.curMonth = date.getMonth() + 1;
18. this.curDay = date.getDate();
19. this.date = this.curYear + '-' + this.curMonth + '-' + this.curDay;
20. this.scheduleList = []
21. },
22. addSchedule(e) {
23. this.$element('dateDialog').show()
24. },
25. cancelDialog(e) {
26. promptAction.showToast({
27. message: 'Event setting canceled.'
28. })
29. },
30. getSchedule(e) {
31. info = e.value
32. },
33. cancelSchedule(e) {
34. this.$element('dateDialog').close()
35. promptAction.showToast({
36. message: 'Event setting canceled.'
37. })
38. },
39. //    Touch OK to save the data.
40. setSchedule(e) {
41. if (e.text === '') {
42. this.schedule = info
43. } else {
44. this.schedule = info
45. var addItem =  {schedule: this.schedule,}
46. this.scheduleList.push(addItem)
47. }
48. this.$element('dateDialog').close()
49. }
50. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/pLmg2mncSe2Y20Lc-F9FPg/zh-cn_image_0000002589244387.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052844Z&HW-CC-Expire=86400&HW-CC-Sign=13C8A1D9A2A91095FBC3F8D8DB7939EA5EDB0331121D564E8C610851CFB859CE)
