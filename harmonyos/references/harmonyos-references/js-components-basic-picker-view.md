---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-picker-view
title: picker-view
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 基础组件 > picker-view
category: harmonyos-references
scraped_at: 2026-04-28T08:03:03+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:093f85d8082b3ebc9d0aa4f39cae96d9a8f3beb9787b03a071e485a369ad7d68
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

嵌入页面的滑动选择器。

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | string | text | 否 | 设置滑动选择器的类型，该属性不支持动态修改，可选项有：  - text：文本选择器。  - time：时间选择器。  - date：日期选择器。  - datetime：日期时间选择器。  - multi-text：多列文本选择器。 |

### 文本选择器

PhonePC/2in1TabletTVWearable

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| range | Array | - | 否 | 设置文本选择器的取值范围。  使用时需要使用数据绑定的方式range ={{data}}，js中声明相应变量data：["15","20","25"]。 |
| selected | string | 0 | 否 | 设置文本选择器的默认选择值，该值需要为range的索引。 |
| indicatorprefix | string | - | 否 | 文本选择器选定值增加的前缀字段。 |
| indicatorsuffix | string | - | 否 | 文本选择器选定值增加的后缀字段。 |

### 时间选择器

PhonePC/2in1TabletTVWearable

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| containsecond | boolean | false | 否 | 时间选择器是否包含秒。  默认值：false，表示时间选择器不包含秒。 |
| selected | string | 当前时间 | 否 | 设置时间选择器的默认取值，格式为 HH:mm；  当包含秒时，格式为HH:mm:ss。 |
| hours | number | 241-4  -5+ | 否 | 设置时间选择器采用的时间格式，可选值：  - 12：按照12小时制显示，用上午和下午进行区分；  - 24：按照24小时制显示。  从API version 5开始，默认值会依据系统当前所选地区和语言选择当地习惯的小时制(12小时制或24小时制)。 |

### 日期选择器

PhonePC/2in1TabletTVWearable

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| start | <time> | 1970-1-1 | 否 | 设置日期选择器的起始时间，格式为 YYYY-MM-DD。 |
| end | <time> | 2100-12-31 | 否 | 设置日期选择器的结束时间，格式为 YYYY-MM-DD。 |
| selected | string | 当前日期 | 否 | 设置日期选择器的默认选择值，格式为 YYYY-MM-DD。 |
| lunar5+ | boolean | false | 否 | 设置日期选择器弹窗界面是否为农历展示。  默认值：false，表示设置日期选择器弹窗界面为公历展示。 |
| lunarswitch | boolean | false | 否 | 设置日期选择器是否显示农历开关，显示农历开关时，可以在弹窗界面通过农历开关进行公历和农历切换。在设置显示农历时，开关状态为开，当设置不显示农历时，开关状态为关。 |

### 日期时间选择器

PhonePC/2in1TabletTVWearable

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| selected | string | 当前日期时间 | 否 | 设置日期时间选择器的默认取值，格式有两种，为月日时分MM-DD-HH-mm或者年月日时分YYYY-MM-DD-HH-mm，不设置年时，默认使用当前年，该取值表示选择器弹窗时弹窗界面的默认选择值。 |
| hours | number | 241-4  -5+ | 否 | 设置日期时间选择器采用的时间格式，可选值：  - 12：按照12小时制显示，用上午和下午进行区分；  - 24：按照24小时制显示。  从API version 5开始，默认值会依据系统当前所选地区和语言选择当地习惯的小时制(12小时制或24小时制)。 |
| lunar5+ | boolean | false | 否 | 设置日期时间选择器弹窗界面是否为农历展示。  默认值：false，表示设置日期选择器弹窗界面为公历展示。 |
| lunarswitch | boolean | false | 否 | 设置日期时间选择器是否显示农历开关，显示农历开关时，可以在弹窗界面展现农历开关以便公历和农历切换。在设置显示农历时，开关状态为开，当设置不显示农历时，开关状态为关。 |

### 多列文本选择器

PhonePC/2in1TabletTVWearable

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| columns | number | - | 是 | 设置多列文本选择器的列数。 |
| range | 二维Array | - | 否 | 设置多列文本选择器的选择值，该值为二维数组。长度表示多少列，数组的每项表示每列的数据，如 [["a","b"], ["c","d"]]。  使用时需要使用数据绑定的方式range ={{data}}，js中声明相应变量data：["15","20","25"]。 |
| selected | Array | [0,0,0,…] | 否 | 设置多列文本选择器的默认值，每一列被选中项对应的索引构成的数组，该取值表示选择器弹窗时弹窗界面的默认选择值。 |

## 样式

PhonePC/2in1TabletTVWearable

除支持[通用样式](js-components-common-styles.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | <color> | #ffffff | 否 | 候选项字体颜色。 |
| font-size | <length> | 16px | 否 | 候选项字体尺寸，类型length，单位px。 |
| selected-color | <color> | #ff0a69f7 | 否 | 选中项字体颜色。 |
| selected-font-size | <length> | 20px | 否 | 选中项字体尺寸，类型length，单位px。 |
| disappear-color5+ | <color> | #ffffff | 否 | 渐变消失项的字体颜色。消失项是在一列中有五个选项场景下最上和最下的两个选项。 |
| disappear-font-size5+ | <length> | 14px | 否 | 渐变消失项的字体尺寸。消失项是在一列中有五个选项场景下最上和最下的两个选项。 |
| font-family | string | sans-serif | 否 | 选项字体类型。字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过[自定义字体](js-components-common-customizing-font.md)指定的字体，会被选中作为文本的字体。 |

## 事件

PhonePC/2in1TabletTVWearable

仅支持如下事件：

### 文本选择器

PhonePC/2in1TabletTVWearable

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | { newValue: newValue, newSelected: newSelected } | 文本选择器选定值后触发该事件。 |

### 时间选择器

PhonePC/2in1TabletTVWearable

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | { hour: hour, minute: minute, [second:second]} | 时间选择器选定值后触发该事件。  包含秒时，返回时分秒。 |

### 日期选择器

PhonePC/2in1TabletTVWearable

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | { year:year, month:month, day:day } | 日期选择器选择值后触发该事件。 |

### 日期时间选择器

PhonePC/2in1TabletTVWearable

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | { year:year, month:month, day:day, hour:hour, minute:minute } | 日期时间选择器选择值后触发该事件。 |

### 多列文本选择器

PhonePC/2in1TabletTVWearable

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| columnchange | { column:column, newValue:newValue, newSelected:newSelected } | 多列文本选择器某一列的值改变时触发该事件，column：第几列修改，newValue：选中的值，newSelected：选中值对应的索引。 |

## 方法

PhonePC/2in1TabletTVWearable

不支持。

## 示例

PhonePC/2in1TabletTVWearable

### 文本选择器

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <text class="title">
4. 选中值：{{value}}  选中下标： {{index}}
5. </text>
6. <picker-view class="text-picker" type="text" range="{{options}}" selected="0" indicatorprefix="prefix" indicatorsuffix="suffix" @change="handleChange"></picker-view>
7. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. justify-content: center;
5. align-items: center;
6. width: 100%;
7. height: 50%;
8. }
9. .title {
10. font-size: 30px;
11. text-align: center;
12. margin-top: 50%;
13. }
```

```
1. /* xxx.js */
2. export default {
3. data: {
4. options: ['选项1', '选项2', '选项3'],
5. value: "选项1",
6. index: 0
7. },
8. handleChange(data) {
9. this.value = data.newValue;
10. this.index = data.newSelected;
11. },
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/Jo_uTIXSShqOfqLU4MOzIw/zh-cn_image_0000002583480195.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000301Z&HW-CC-Expire=86400&HW-CC-Sign=64B22E265F11E25A2181BD78B688B655A20B2D23F85E71BB6039182D26C0D9C3)

### 时间选择器

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <text class="title">
4. Selected：{{time}}
5. </text>
6. <picker-view class="time-picker" type="time" selected="{{defaultTime}}" @change="handleChange"></picker-view>
7. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. justify-content: center;
5. align-items: center;
6. width: 100%;
7. height: 50%;
8. }
9. .title {
10. font-size: 31px;
11. text-align: center;
12. margin-top: 50%;
13. }
```

```
1. /* xxx.js */
2. export default {
3. data: {
4. defaultTime: "",
5. time: "",
6. },
7. onInit() {
8. this.defaultTime = this.now();
9. },
10. handleChange(data) {
11. this.time = this.concat(data.hour, data.minute);
12. },
13. now() {
14. const date = new Date();
15. const hours = date.getHours();
16. const minutes = date.getMinutes();
17. return this.concat(hours, minutes);
18. },
19. fill(value) {
20. return (value > 9 ? "" : "0") + value;
21. },
22. concat(hours, minutes) {
23. return `${this.fill(hours)}:${this.fill(minutes)}`;
24. },
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/n3_roYVtR5O1-UdqmAwxag/zh-cn_image_0000002552800546.png?HW-CC-KV=V1&HW-CC-Date=20260428T000301Z&HW-CC-Expire=86400&HW-CC-Sign=1D7E86A2591DA12F7EB80B6A37B45F2FB41ADB674DDAEF6FFFEBA9CAD69C1739 "点击放大")

### 日期选择器

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <text class="title">
4. Selected：{{date}}
5. </text>
6. <picker-view class="time-picker" type="date" selected="{{defaultTime}}" @change="handleChange" lunarswitch="true"></picker-view>
7. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. justify-content: center;
5. align-items: center;
6. width: 100%;
7. height: 50%;
8. }
9. .title {
10. font-size: 31px;
11. text-align: center;
12. margin-top: 50%;
13. }
```

```
1. /* xxx.js */
2. export default {
3. data: {
4. date: "",
5. },
6. handleChange(data) {
7. this.date = data.year + "年" + data.month + "月" + data.day + "日";
8. },
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/wWtPKjuBRYiJ3d1zazYtiA/zh-cn_image_0000002583440241.png?HW-CC-KV=V1&HW-CC-Date=20260428T000301Z&HW-CC-Expire=86400&HW-CC-Sign=23F95BCBBEF8B6AF206C0C635B214DC970BE533C1284159632B00E14914483C5 "点击放大")

### 日期时间选择器

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <text class="title">
4. Selected：{{datetime}}
5. </text>
6. <picker-view class="date-picker" type="datetime"  hours="24" lunarswitch="true" @change="handleChange"></picker-view>
7. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. justify-content: center;
5. align-items: center;
6. width: 100%;
7. height: 50%;
8. }
9. .title {
10. font-size: 31px;
11. text-align: center;
12. margin-top: 50%;
13. }
```

```
1. /* xxx.js */
2. export default {
3. data: {
4. datetime: "",
5. },
6. handleChange(data) {
7. this.datetime = data.year + "年" + data.month + "月" + data.day + "日" + data.hour + "时" + data.minute + "分";
8. },
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/qGpz1btMRZ6QPlio9wtTHQ/zh-cn_image_0000002552960196.png?HW-CC-KV=V1&HW-CC-Date=20260428T000301Z&HW-CC-Expire=86400&HW-CC-Sign=4B62FB5CB0209D5DAB83175694F1C463180A81ED38B6617C82AB3B423407C4FA "点击放大")

### 多列文本选择器

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <text class="title">
4. Selected：{{ value }}
5. </text>
6. <picker-view class="multitype-picker" type="multi-text" columns="3" range="{{ multitext }}" @columnchange="handleChange"></picker-view>
7. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. justify-content: center;
5. align-items: center;
6. width: 100%;
7. height: 50%;
8. }
9. .title {
10. font-size: 31px;
11. text-align: center;
12. margin-top: 50%;
13. }
```

```
1. /* xxx.js */
2. export default {
3. data: {
4. multitext: [
5. [1, 2, 3],
6. [4, 5, 6],
7. [7, 8, 9],
8. ],
9. value: ""
10. },
11. handleChange(data) {
12. this.value = data.column + "列，" + "值为" + data.newValue + "，下标为" + data.newSelected;
13. },
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/DP1MylW_R-SOw2-NWEgBNg/zh-cn_image_0000002583480197.png?HW-CC-KV=V1&HW-CC-Date=20260428T000301Z&HW-CC-Expire=86400&HW-CC-Sign=962A1CB7D288CB846898262CDB55CCC7D0104999FD7475197C5372F4B62C6143 "点击放大")
