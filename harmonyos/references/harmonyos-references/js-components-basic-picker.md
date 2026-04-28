---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-picker
title: picker
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 基础组件 > picker
category: harmonyos-references
scraped_at: 2026-04-28T08:03:02+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1d6fe664b20a2603e7f1b8fee2da31fe70c3024172afd475d9c9772fe426e341
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

滑动选择器组件，类型支持普通选择器、日期选择器、时间选择器、时间日期选择器和多列文本选择器。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | string | - | 否 | 该属性值不支持动态修改。可选择项有：  - text：文本选择器。  - date：日期选择器。  - time：时间选择器。  - datetime：日期时间选择器。  - multi-text：多列文本选择器。 |

### 普通选择器

PhonePC/2in1TabletTVWearable

滑动选择器类型设置为text时表示普通选择器。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| range | Array | - | 否 | 设置普通选择器的取值范围，如["15", "20", "25"]。  使用时需要使用数据绑定的方式range ={{data}}，js中声明相应变量data：["15","20","25"]。 |
| selected | string | 0 | 否 | 设置普通选择器弹窗的默认取值，取值需要是 range 的索引值，该取值表示选择器弹窗界面的默认选择值。 |
| value | string | - | 否 | 设置普通选择器的值。 |

### 日期选择器

PhonePC/2in1TabletTVWearable

滑动选择器类型设置为date时表示日期选择器。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| start | <time> | 1970-1-1 | 否 | 设置日期选择器的起始时间，格式为 YYYY-MM-DD。 |
| end | <time> | 2100-12-31 | 否 | 设置日期选择器的结束时间，格式为 YYYY-MM-DD。 |
| selected | string | 当前日期 | 否 | 设置日期选择器弹窗的默认取值，格式为 YYYY-MM-DD，该取值表示选择器弹窗界面的默认选择值。 |
| value | string | - | 是 | 设置日期选择器的值。 |
| lunar5+ | boolean | false | 否 | 设置日期选择器是否为农历展示。  默认值：false，表示设置日期选择器是公历展示。 |
| lunarswitch | boolean | false | 否 | 设置日期选择器是否显示农历开关。当值为true时，显示农历开关，点击农历开关可切换公历和农历。当值为false时，不显示农历开关。  当lunarswitch=true且lunar=true时，开关按钮处于被选中状态。 |

### 时间选择器

PhonePC/2in1TabletTVWearable

滑动选择器类型设置为time时表示时间选择器。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| containsecond | boolean | false | 否 | 设置时间选择器是否包含秒。  默认值：false，表示设置时间选择器不包含秒。 |
| selected | string | 当前时间 | 否 | 设置时间选择器弹窗的默认取值，格式为 HH:mm；当包含秒时，格式为HH:mm:ss，  该取值表示选择器弹窗界面的默认选择值。 |
| value | string | - | 否 | 设置时间选择器的值。 |
| hours | number | 241-4  -5+ | 否 | 设置时间选择器采用的时间格式，可选值：  - 12：按照12小时制显示，用上午和下午进行区分；  - 24：按照24小时制显示。  从API version 5开始，默认值会依据系统当前所选地区和语言选择当地习惯的小时制(12小时制或24小时制)。 |

### 日期时间选择器

PhonePC/2in1TabletTVWearable

滑动选择器类型设置为datetime时表示日期时间选择器，日期的选择范围为本年的日月。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| selected | string | 当前日期时间 | 否 | 设置日期时间选择器弹窗的默认取值，有两种可选格式。  - 月日时分：MM-DD-HH-mm  - 年月日时分：YYYY-MM-DD-HH-mm  不设置年时，默认使用当前年，该取值表示选择器弹窗界面的默认选择值。 |
| value | string | - | 是 | 设置日期时间选择器的值。 |
| hours | number | 241-4  -5+ | 否 | 设置日期时间选择器采用的时间格式，可选值：  - 12：按照12小时制显示，用上午和下午进行区分；  - 24：按照24小时制显示。  从API version 5开始，默认值会依据系统当前所选地区和语言选择当地习惯的小时制(12小时制或24小时制)。 |
| lunar5+ | boolean | false | 否 | 设置日期时间选择器是否为农历展示。  默认值：false，表示设置日期选择器为公历展示。 |
| lunarswitch | boolean | false | 否 | 设置日期选择器是否显示农历开关。当值为true时，显示农历开关，点击农历开关可切换公历和农历。当值为false时，不显示农历开关。  当lunarswitch=true且lunar=true时，开关按钮处于被选中状态。 |

### 多列文本选择器

PhonePC/2in1TabletTVWearable

滑动选择器类型设置为multi-text时表示多列文本选择器。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| columns | number | - | 是 | 设置多列文本选择器的列数。 |
| range | 二维Array | - | 否 | 设置多列文本选择器的选择项，其中range 为二维数组。长度表示多少列，数组的每项表示每列的数据，如 [["a","b"], ["c","d"]]。  使用时需要使用数据绑定的方式range ={{data}}，js中声明相应变量data：["15","20","25"]。 |
| selected | Array | [0,0,0,…] | 否 | 设置多列文本选择器弹窗的默认值，每一列被选中项对应的索引构成的数组，该取值表示选择器弹窗界面的默认选择值。 |
| value | Array | - | 否 | 设置多列文本选择器的值，每一列被选中项对应的值构成的数组。 |

## 样式

PhonePC/2in1TabletTVWearable

除支持[通用样式](js-components-common-styles.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| text-color | <color> | - | 否 | 选择器的文本颜色。 |
| font-size | <length> | - | 否 | 选择器的文本尺寸。 |
| allow-scale | boolean | true | 否 | 选择器的文本尺寸是否跟随系统设置字体缩放尺寸进行放大缩小。  如果在config描述文件中针对ability配置了fontSize的config-changes标签，则应用不会重启而直接生效。  默认值：true，表示选择器的文本尺寸跟随系统设置字体缩放尺寸进行放大缩小。 |
| letter-spacing | <length> | 0 | 否 | 选择器的字符间距。见[text组件的letter-spacing样式属性](js-components-basic-text.md#样式)。 |
| text-decoration | string | - | 否 | 选择器的文本修饰。见[text组件的text-decoration样式属性](js-components-basic-text.md#样式)。 |
| font-style | string | normal | 否 | 选择器的字体样式。见[text组件的font-style样式属性](js-components-basic-text.md#样式)。 |
| font-weight | number | string | normal | 否 | 选择器的字体粗细。见[text组件的font-weight样式属性](js-components-basic-text.md#样式)。 |
| font-family | string | sans-serif | 否 | 选择器的字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过[自定义字体](js-components-common-customizing-font.md)指定的字体，会被选中作为文本的字体。 |
| line-height | <length> | 0px | 否 | 选择器的文本行高。 |
| column-height5+ | <length> | - | 否 | 选择器的选择项列表高度。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

### 普通选择器

PhonePC/2in1TabletTVWearable

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | { newValue: newValue, newSelected: newSelected } | 普通选择器选择值后点击弹窗中的确定按钮时触发该事件（newSelected为索引）。 |
| cancel | - | 用户点击弹窗中的取消按钮时触发该事件。 |

### 日期选择器

PhonePC/2in1TabletTVWearable

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | { year: year, month: month, day: day } | 日期选择器选择值后点击弹窗中的确认按钮时触发该事件。  从API version 5开始，month值范围为： 0（1月）~11（12月）。 |
| cancel | - | 用户点击弹窗中的取消按钮时触发该事件。 |

### 日期时间选择器

PhonePC/2in1TabletTVWearable

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | { year: year, month: month, day: day, hour: hour, minute: minute} | 日期时间选择器选择值后点击弹窗中的确认按钮时触发该事件。 |
| cancel | - | 用户点击弹窗中的取消按钮时触发该事件。 |

### 时间选择器

PhonePC/2in1TabletTVWearable

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | { hour: hour, minute: minute, [second: second] } | 时间选择器选择值后点击弹窗中的确认按钮时触发该事件，当使用时分秒时，还包含秒数据。 |
| cancel | - | 用户点击弹窗中的取消按钮时触发该事件。 |

### 多列文本选择器

PhonePC/2in1TabletTVWearable

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | { newValue: [newValue1, newValue2, newValue3, …], newSelected:[newSelected1, newSelected2, newSelected3, …] } | 多列文本选择器选择值后点击弹窗中的确认按钮时触发该事件，其中：  - newValue：被选中项对应的值构成的数组。  - newSelected：被选中项对应的索引构成的数组，两者的长度和range的长度一致。 |
| columnchange | { column: column, newValue: newValue, newSelected: newSelected } | 多列文本选择器中某一列的值改变时触发该事件，其中：  - column：第几列修改。  - newValue：选中的值。  - newSelected：选中值对应的索引。 |
| cancel | - | 用户点击弹窗中的取消按钮时触发该事件。 |

## 方法

PhonePC/2in1TabletTVWearable

除支持[通用方法](js-components-common-methods.md)外，支持如下方法：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| show | - | 显示 picker。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <select @change="selectChange">
4. <option value="{{ item }}" for="item in selectList">
5. {{ item }}
6. </option>
7. </select>
8. <picker id="picker0" type="text" value="{{ textvalue }}" selected="{{ textselect }}" range="{{ rangetext }}"
9. onchange="textonchange"
10. oncancel="textoncancel" class="pickertext" show="false"></picker>

12. <picker id="picker1" type="date" value="{{ datevalue }}" start="2002-2-5" end="2030-6-5" selected="{{ dateselect }}"
13. lunarswitch="true"
14. onchange="dateonchange" oncancel="dateoncancel" class="pickerdate" show="false"></picker>

16. <picker id="picker2" type="time" value="{{ timevalue }}" containsecond="{{ containsecond }}"
17. selected="{{ timeselect }}" hours="12"
18. onchange="timeonchange" oncancel="timeoncancel" class="pickertime" show="false"></picker>

20. <picker id="picker3" type="datetime" value="{{ datetimevalue }}" selected="{{ datetimeselect }}" hours="24"
21. lunarswitch="true"
22. onchange="datetimeonchange" oncancel="datetimeoncancel" class="pickerdatetime" show="false"></picker>

24. <picker id="picker4" type="multi-text" value="{{ multitextvalue }}" columns="3" range="{{ multitext }}"
25. selected="{{ multitextselect }}"
26. onchange="multitextonchange" oncancel="multitextoncancel" class="pickermuitl" show="false"></picker>
27. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. justify-content: center;
5. align-items: center;
6. }

8. picker {
9. width: 60%;
10. height: 80px;
11. border-radius: 20px;
12. text-color: white;
13. font-size: 15px;
14. background-color: #4747e3;
15. margin-left: 20%;
16. }

18. select {
19. background-color: #efecec;
20. height: 50px;
21. width: 60%;
22. margin-left: 20%;
23. margin-top: 300px;
24. margin-bottom: 50px;
25. font-size: 22px;
26. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';

4. export default {
5. data: {
6. selectList: ["text", "data", "time", "datetime", "multitext"],
7. rangetext: ['15', "20", "25"],
8. multitext: [["a", "b", "c"], ["e", "f", "g"], ["h", "i"], ["k", "l", "m"]],
9. textvalue: 'default textvalue',
10. datevalue: 'default datevalue',
11. timevalue: 'default timevalue',
12. datetimevalue: 'default datetimevalue',
13. multitextvalue: 'default multitextvalue',
14. containsecond: true,
15. multitextselect: [1, 2, 0],
16. datetimeselect: '2012-5-6-11-25',
17. timeselect: '11:22:30',
18. dateselect: '2021-3-2',
19. textselect: '2'
20. },
21. selectChange(e) {
22. for (let i = 0;i < this.selectList.length; i++) {
23. if (e.newValue == this.selectList[i]) {
24. this.$element("picker" + i).show();
25. }
26. }
27. },
28. textonchange(e) {
29. this.textvalue = e.newValue;
30. promptAction.showToast({
31. message: "text:" + e.newValue + ",newSelected:" + e.newSelected
32. })
33. },
34. textoncancel(e) {
35. promptAction.showToast({
36. message: "text: textoncancel"
37. })
38. },
39. dateonchange(e) {
40. this.datevalue = e.year + "-" + e.month + "-" + e.day;
41. promptAction.showToast({
42. message: "date:" + e.year + "-" + (e.month + 1) + "-" + e.day
43. })
44. },
45. dateoncancel() {
46. promptAction.showToast({
47. message: "date: dateoncancel"
48. })
49. },
50. timeonchange(e) {
51. if (this.containsecond) {
52. this.timevalue = e.hour + ":" + e.minute + ":" + e.second;
53. promptAction.showToast({
54. message: "Time:" + e.hour + ":" + e.minute + ":" + e.second
55. })
56. } else {
57. this.timevalue = e.hour + ":" + e.minute;
58. promptAction.showToast({
59. message: "Time:" + e.hour + ":" + e.minute
60. })
61. }
62. },
63. timeoncancel() {
64. promptAction.showToast({
65. message: "timeoncancel"
66. })
67. },
68. datetimeonchange(e) {
69. this.datetimevalue = e.year + "-" + e.month + "-" + e.day + " " + e.hour + ":" + e.minute;
70. promptAction.showToast({
71. message: "Time:" + (e.month + 1) + "-" + e.day + " " + e.hour + ":" + e.minute
72. })
73. },
74. datetimeoncancel() {
75. promptAction.showToast({
76. message: "datetimeoncancel"
77. })
78. },
79. multitextonchange(e) {
80. this.multitextvalue = e.newValue;
81. promptAction.showToast({
82. message: "Multi-column text change" + e.newValue
83. })
84. },
85. multitextoncancel() {
86. promptAction.showToast({
87. message: "multitextoncancel"
88. })
89. },
90. popup_picker() {
91. this.$element("picker_text").show();
92. },
93. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/CZ_5nsspTniM17RLPj1Q2g/zh-cn_image_0000002552960194.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000301Z&HW-CC-Expire=86400&HW-CC-Sign=E8F8CDE714BFC6EBF7E31D1F5F6036AE999F1EE82534AEA58A102C464A1719D1)
