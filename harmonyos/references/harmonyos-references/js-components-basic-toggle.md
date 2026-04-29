---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-toggle
title: toggle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 基础组件 > toggle
category: harmonyos-references
scraped_at: 2026-04-29T13:53:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6d8f6ce3c7317dab19fc8f61f933b17975b438a4d361bad1c9cc01b5b93b827f
---

说明

从API version 5开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

状态按钮用于从一组选项中进行选择，并可能在界面上实时显示选择后的结果。通常这一组选项都是由状态按钮构成。

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
| value | string | - | 是 | 状态按钮的文本值。 |
| checked | boolean | false | 否 | 状态按钮是否被选中。true表示选中，false表示未选中。 |

## 样式

PhonePC/2in1TabletTVWearable

除支持[通用样式](js-components-common-styles.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| text-color | <color> | #E5000000 | 否 | 状态按钮的文本颜色。 |
| font-size | <length> | 16px | 否 | 状态按钮的文本尺寸。 |
| allow-scale | boolean | true | 否 | 状态按钮的文本尺寸是否跟随系统设置字体缩放尺寸进行放大缩小。true表示跟随系统放大缩小，false表示不跟随系统放大缩小。  如果在config描述文件中针对ability配置了fontSize的config-changes标签，则应用不会重启而直接生效。 |
| font-style | string | normal | 否 | 状态按钮的字体样式。 |
| font-weight | number | string | normal | 否 | 状态按钮的字体粗细。见[text组件font-weight的样式属性](js-components-basic-text.md#样式)。 |
| font-family | <string> | sans-serif | 否 | 状态按钮的字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过[自定义字体](js-components-common-customizing-font.md)指定的字体，会被选中作为文本的字体。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | { checked：isChecked } | 组件选中状态发生变化时触发。 |

## 方法

PhonePC/2in1TabletTVWearable

支持[通用方法](js-components-common-methods.md)。

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div style="flex-direction: column;">
3. <text class="margin">1. Multiple choice example</text>
4. <div style="flex-wrap: wrap">
5. <toggle class="margin" for="{{toggles}}">{{$item}}</toggle>
6. </div>
7. <text class="margin">2. Single choice example</text>
8. <div style="flex-wrap: wrap">
9. <toggle class="margin" for="{{toggle_list}}" id="{{$item.id}}" checked="{{$item.checked}}"
10. value="{{$item.name}}" @change="allchange" @click="allclick({{$item.id}})"></toggle>
11. </div>
12. </div>
```

```
1. /* xxx.css */
2. .margin {
3. margin: 7px;
4. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. toggle_list: [
5. {
6. "id": "1001", "name": "Living room", "checked": true
7. },
8. {
9. "id": "1002", "name": "Bedroom", "checked": false
10. },
11. {
12. "id": "1003", "name": "Second bedroom", "checked": false
13. },
14. {
15. "id": "1004", "name": "Kitchen", "checked": false
16. },
17. {
18. "id": "1005", "name": "Study", "checked": false
19. },
20. {
21. "id": "1006", "name": "Garden", "checked": false
22. },
23. {
24. "id": "1007", "name": "Bathroom", "checked": false
25. },
26. {
27. "id": "1008", "name": "Balcony", "checked": false
28. },
29. ],
30. toggles: ["Living room", "Bedroom", "Kitchen", "Study"],
31. idx: ""
32. },
33. allclick(arg) {
34. this.idx = arg;
35. },
36. allchange(e) {
37. if (e.checked != true) {
38. return;
39. }
40. for (var i = 0; i < this.toggle_list.length; i++) {
41. if (this.toggle_list[i].id === this.idx) {
42. this.toggle_list[i].checked = true;
43. } else {
44. this.toggle_list[i].checked = false;
45. }
46. }
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/5soaElyaTzyX62Ltviu5Cg/zh-cn_image_0000002589246537.png?HW-CC-KV=V1&HW-CC-Date=20260429T055328Z&HW-CC-Expire=86400&HW-CC-Sign=E281399929952E63113F0FFF6D0BB9878716E8EB92B55233ED7C196F856ABE31)
