---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-textreadericon
title: TextReaderIcon（朗读听筒图标）
breadcrumb: API参考 > AI > Speech Kit（场景化语音服务） > ArkTS组件 > TextReaderIcon（朗读听筒图标）
category: harmonyos-references
scraped_at: 2026-04-28T08:19:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:68158f7aee87089c6fc92c99dd0a8e44c14d6e0417e391e81b49393824567f16
---

朗读听筒图标，可以作为动态组件加载，并配置成为播放面板的主入口。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { TextReaderIcon } from '@kit.SpeechKit';
```

## TextReaderIcon

PhonePC/2in1Tablet

朗读听筒图标，可以作为动态组件加载。设置onClick回调，在用户点击听筒图标时启动朗读控件。

**装饰器类型：** @Component

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| readState | [ReadStateCode](speech-readstatecode.md) | 是 | @Link | 播报状态。  **说明：**  ReadState使用[@Link装饰器：父子双向同步](../harmonyos-guides/arkts-link.md)。 |

### build

PhonePC/2in1Tablet

build(): void

用于创建[TextReaderIcon](speech-textreadericon.md#textreadericon)对象的构造函数。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**示例：**

```
1. import { TextReader, TextReaderIcon, ReadStateCode } from '@kit.SpeechKit';

3. @Entry
4. @Component
5. struct Index {

7. /**
8. * 待加载的文章
9. */
10. @State readInfoList: TextReader.ReadInfo[] = [];
11. @State selectedReadInfo: TextReader.ReadInfo = this.readInfoList[0];

13. /**
14. * 播放状态
15. */
16. @State readState: ReadStateCode = ReadStateCode.WAITING;

18. /**
19. * 用于显示当前页的按钮状态
20. */
21. @State isInit: boolean = false;

23. async aboutToAppear(){
24. /**
25. * 加载数据
26. */
27. let readInfoList: TextReader.ReadInfo[] = [{
28. id: '001',
29. title: {
30. text:'水调歌头.明月几时有',
31. isClickable:true
32. },
33. author:{
34. text:'宋.苏轼',
35. isClickable:true
36. },
37. date: {
38. text:'2024/01/01',
39. isClickable:false
40. },
41. bodyInfo: '明月几时有？把酒问青天。'
42. }];
43. this.readInfoList = readInfoList;
44. this.selectedReadInfo = this.readInfoList[0];
45. this.init();
46. }

48. /**
49. * 初始化
50. */
51. async init() {
52. const readerParam: TextReader.ReaderParam = {
53. isVoiceBrandVisible: true,
54. businessBrandInfo: {
55. panelName: '小艺朗读',
56. panelIcon: $r('app.media.startIcon')
57. }
58. }
59. try {
60. let context: Context | undefined = this.getUIContext().getHostContext()
61. if (context) {
62. await TextReader.init(context, readerParam);
63. this.isInit = true;
64. }
65. } catch (err) {
66. console.error(`TextReader failed to init. Code: ${err.code}, message: ${err.message}`);
67. }
68. }

70. // 设置操作监听
71. setActionListener() {
72. TextReader.on('stateChange', (state: TextReader.ReadState) => {
73. this.onStateChanged(state)
74. });
75. TextReader.on('requestMore', () => this.onStateChanged);
76. }

78. onStateChanged = (state: TextReader.ReadState) => {
79. if (this.selectedReadInfo?.id === state.id) {
80. this.readState = state.state;
81. } else {
82. this.readState = ReadStateCode.WAITING;
83. }
84. }

86. build() {
87. Column() {
88. TextReaderIcon({ readState: this.readState })
89. .margin({ right: 20 })
90. .width(32)
91. .height(32)
92. .onClick(async () => {
93. try {
94. this.setActionListener();
95. await TextReader.start(this.readInfoList, this.selectedReadInfo?.id);
96. } catch (err) {
97. console.error(`TextReader failed to start. Code: ${err.code}, message: ${err.message}`);
98. }
99. })
100. }
101. .height('100%')
102. }
103. }
```
