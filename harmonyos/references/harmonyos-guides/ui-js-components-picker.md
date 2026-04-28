---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-picker
title: picker开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > picker开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e2776b0371d92a21024f6e6ddc70d1359010b85be6bc97ac63adf3ecce16914a
---

picker是滑动选择器组件，类型支持普通选择器、日期选择器、时间选择器、时间日期选择器和多列文本选择器。具体用法请参考[picker](../harmonyos-references/js-components-basic-picker.md)。

## 创建picker组件

在pages/index目录下的hml文件中创建一个picker组件。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <picker>picker</picker>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/cSpRYkYQSRCxtM3OyyqNnA/zh-cn_image_0000002583438151.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234025Z&HW-CC-Expire=86400&HW-CC-Sign=BD91A62194D1445C6B5EC4194BAD70A8ED110A905D1BB725F340352204AB88E4)

## 设置picker类型

通过设置picker的type属性来选择滑动选择器类型，如定义picker为日期选择器。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <picker id="picker_text" type="text" value="{{textvalue}}"range="{{rangetext}}" class="pickertext" ></picker>
4. <picker id="picker_date" type="date" value="{{datevalue}}" lunarswitch="true" start="2002-2-5" end="2030-6-5" class="pickerdate"></picker>
5. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }
10. .pickertext{
11. margin-bottom: 30px;
12. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. rangetext:['15', "20", "25"],
5. textvalue:'Select text',
6. datevalue:'Select date',
7. }
8. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/P5W3GFhpR3u-GMSZXpl-CQ/zh-cn_image_0000002552958106.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234025Z&HW-CC-Expire=86400&HW-CC-Sign=980B16726D380EEC76AE36C609B29AE7986C2884F9443FF8F619BFAA411F090B)

说明

普通选择器设置取值范围时，需要使用数据绑定的方式。

## 设置时间显示格式

picker组件的hours属性用于设置时间显示格式，支持12小时制和24小时制两种模式。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <picker id="picker_time" type="time" value="12-hour format" hours="12" onchange="timeonchange"  class="pickertime"></picker>
4. <picker id="picker_time" type="time" value="24-hour format" hours="24" onchange="timeonchange"  class="pickertime"></picker>
5. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }
10. .pickertime {
11. margin-bottom:50px;
12. width: 300px;
13. height: 50px;
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/TqJNqfPISvavIjGfNvuECQ/zh-cn_image_0000002583478107.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234025Z&HW-CC-Expire=86400&HW-CC-Sign=CC6ACC2E086842AB8B7ABBBAF73E3146D1B37496FB6A960F497AE25A6827BBAE)

说明

* hours属性为12：按照12小时制显示，用上午和下午进行区分。
* hours属性为24：按照24小时制显示。

## 添加响应事件

为picker组件添加change和cancel事件，可以处理用户的选择确定和取消操作。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <picker id="picker_multi" type="multi-text" value="{{multitextvalue}}" columns="3" range="{{multitext}}" selected="
4. {{multitextselect}}" onchange="multitextonchange" oncancel="multitextoncancel" class="pickermuitl"></picker>
5. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }
10. .pickermuitl {
11. margin-bottom:20px;
12. width: 600px;
13. height: 50px;
14. font-size: 25px;
15. letter-spacing:15px;
16. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. data: {
5. multitext:[["a", "b", "c"], ["e", "f", "g"], ["h", "i"]],
6. multitextvalue:'Select multi-line text',
7. multitextselect:[0,0,0],
8. },
9. multitextonchange(e) {
10. this.multitextvalue=e.newValue;
11. promptAction.showToast({ message:"Multi-column text changed to:" + e.newValue })
12. },
13. multitextoncancel() {
14. promptAction.showToast({ message:"multitextoncancel" })
15. },
16. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/qXK7AJjBQwmoRRg2g7j06A/zh-cn_image_0000002552798458.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234025Z&HW-CC-Expire=86400&HW-CC-Sign=F42694C033534D130AED3236280BE3D39329615E66BED5B728308C7F5CC12892)

## 场景示例

在本场景中，开发者可以自定义填写健康情况以完成打卡。

```
1. <!-- xxx.hml -->
2. <div class="doc-page">
3. <text class="title">Health check-in</text>
4. <div class="out-container">
5. <text class="txt">Office:</text>
6. <picker class="pick" focusable="true" type="text" value="{{pos}}" range="{{posarr}}" onchange="setPos"></picker>
7. </div>
8. <divider class="dvd"></divider>
9. <div class="out-container">
10. <text class="txt">Office hours:</text>
11. <picker class="pick" type="date" value="{{datevalue}}"  start="2002-2-5" end="2030-6-5" selected="{{dateselect}}"
12. lunarswitch="true" onchange="dateonchange"></picker>
13. </div>
14. <divider class="dvd"></divider>
15. <div class="out-container">
16. <text class="txt">Having fever or cold symptoms</text>
17. <picker class="pick" type="text" value="{{yorn1}}" range="{{yesno}}" selected="1" onchange="isFever"></picker>
18. </div>
19. <divider class="dvd"></divider>
20. <div class="out-container">
21. <text class="txt">Close contact with someone with COVID-19</text>
22. <picker class="pick" type="text" value="{{yorn2}}" range="{{yesno}}" selected="1" onchange="isTouch"></picker>
23. </div>
24. <div class="out-container">
25. <button value="Submit" style="margin-top:100px;width:50%;font-color:#0000ff;height:80px" onclick="showtoast"></button>
26. </div>
27. </div>
```

```
1. /* xxx.css */
2. .doc-page {
3. flex-direction: column;
4. background-color: #F1F3F5;
5. }
6. .title {
7. margin-top: 30px;
8. margin-bottom: 30px;
9. margin-left: 50px;
10. font-weight: bold;
11. color: #0000ff;
12. font-size: 38px;
13. }
14. .out-container {
15. flex-direction: column;
16. align-items: center;
17. }
18. .pick {
19. width: 80%;
20. height: 76px;
21. border: 1px solid #0000ff;
22. border-radius: 20px;
23. padding-left: 12px;
24. }
25. .txt {
26. width: 80%;
27. font-size: 18px;
28. text-align: left;
29. margin-bottom: 12px;
30. margin-left: 12px;
31. }
32. .dvd {
33. margin-top: 30px;
34. margin-bottom: 30px;
35. margin-left: 80px;
36. margin-right: 80px;
37. color: #6495ED;
38. stroke-width: 6px;
39. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction'
3. export default {
4. data: {
5. yorn1:'No',
6. yorn2:'No',
7. pos:'Home',
8. yesno:['Yes', 'No'],
9. posarr:['Home', 'Company'],
10. datevalue:'Select time',
11. datetimeselect:'2012-5-6-11-25',
12. dateselect:'2021-9-17',
13. showbuild:true
14. },
15. onInit() {
16. },
17. isFever(e) {
18. this.yorn1 = e.newValue
19. },
20. isTouch(e) {
21. this.yorn2 = e.newValue
22. },
23. setPos(e) {
24. this.pos = e.newValue
25. if (e.newValue === 'Non-research center') {
26. this.showbuild = false
27. } else {
28. this.showbuild = true
29. }
30. },
31. setbuild(e) {
32. this.build = e.newValue
33. },
34. dateonchange(e) {
35. e.month=e.month+1;
36. this.datevalue = e.year + "-" + e.month + "-" + e.day;
37. promptAction.showToast({ message:"date:"+e.year+"-"+e.month+"-"+e.day })
38. },
39. showtoast() {
40. promptAction.showToast({
41. message: 'Submitted.',
42. duration: 2000,
43. gravity: 'center'
44. })
45. }
46. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/FOHOBiJgRzOH0EUpkICLKg/zh-cn_image_0000002583438153.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234025Z&HW-CC-Expire=86400&HW-CC-Sign=CC8640E143999DBAAD6155204AB785D5AA015AC30F5EA138F5DB80B3C23A76ED)
