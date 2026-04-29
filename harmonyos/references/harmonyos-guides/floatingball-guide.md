---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/floatingball-guide
title: 全局闪控球开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 全局闪控球开发指导
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:08+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:6c561d7520f159b1e5dfb6d9912e4919e846356c33774b774ab7856cb09bb05b
---

## 场景介绍

闪控球是一种在设备屏幕上悬浮的非全屏应用窗口，为应用提供临时的全局能力，完成跨应用交互。

应用可以将关键信息以小窗（闪控球）模式呈现。切换为小窗（闪控球）模式后，用户可以进行其他界面操作，提升使用体验。

说明

* 从API version 20开始，支持使用闪控球能力。
* 支持在DevEco Studio 6.0.1 Release及以上版本的模拟器中使用闪控球相关功能。

## 约束与限制

* 基于安全考虑，仅允许应用在前台时启动闪控球，并且需要具有[ohos.permission.USE\_FLOAT\_BALL](restricted-permissions.md#ohospermissionuse_float_ball)权限，具体可见[申请受限权限](declare-permissions-in-acl.md)。
* 当前仅对跨应用的题目搜索、账单记录、商品比价、抢单、翻译场景，以及金融类应用的实时盯盘场景开放此权限。接入后需在以上场景范围内使用，否则将会进行相关处罚与限制。
* 同一个应用只能启动一个闪控球，同一个设备最多同时存在两个闪控球，在超出闪控球最大个数限制时，打开新的闪控球会替换最早启动的闪控球。
* 仅支持手机和平板设备。

## 接口说明

以下是闪控球功能的常用接口，更多接口及使用参考[@ohos.window.floatingBall (闪控球窗口)](../harmonyos-references/js-apis-floatingball.md) 。

| 接口名 | 描述 |
| --- | --- |
| isFloatingBallEnabled(): boolean | 判断当前设备是否支持闪控球功能。 |
| create(config: FloatingBallConfiguration): Promise<FloatingBallController> | 创建闪控球控制器。 |
| startFloatingBall(params: FloatingBallParams): Promise<void> | 启动闪控球。 |
| updateFloatingBall(params: FloatingBallParams): Promise<void> | 更新闪控球。 |
| stopFloatingBall(): Promise<void> | 停止闪控球。 |
| on(type: 'stateChange', callback: Callback<FloatingBallState>): void | 开启闪控球生命周期状态的监听。 |
| off(type: 'stateChange', callback?: Callback<FloatingBallState>): void | 关闭闪控球生命周期状态的监听。 |
| on(type: 'click', callback: Callback<void>): void | 开启闪控球点击事件的监听。 |
| off(type: 'click', callback?: Callback<void>): void | 关闭闪控球点击事件的监听。 |
| getFloatingBallWindowInfo(): Promise<FloatingBallWindowInfo> | 获取闪控球窗口信息。 |
| restoreMainWindow(want: Want): Promise<void> | 恢复应用主窗口，加载指定页面。 |

## 交互方式

闪控球提供以下交互方式：

* 单击闪控球：触发闪控球点击事件。
* 长按闪控球：长按闪控球震动变为待删除态，可以点击图标单个删除或全部删除。
* 拖动闪控球：可以手动拖拽闪控球改变位置，拖拽时自动避让状态栏、固定态软键盘（改变软键盘为固定态或者悬浮态的详细介绍请参见[输入法服务](../harmonyos-references/js-apis-inputmethodengine.md#changeflag10)）、导航条等其他组件，设备处于横屏场景时不会自动避让输入法。拖拽松手时闪控球自动吸附在最近的侧边，拖拽到垃圾桶区域（底部中部区域）松手即可删除。
* 闪控球位置记忆：关闭闪控球会记录当前位置，下一次打开功能时自动展示在上次关闭时的位置。旋转屏幕或重启设备会恢复到默认位置，默认位置位于屏幕右上侧。

## 闪控球规格与样式布局

目前支持四种闪控球模板布局，具体可见闪控球模板类型枚举[FloatingBallTemplate](../harmonyos-references/js-apis-floatingball.md#floatingballtemplate)。

* 静态布局：支持图标和标题。
* 普通文本布局：支持标题和内容。
* 强调文本布局：支持图标、标题和内容。
* 纯文本布局：仅支持标题，可双行展示。

目前闪控球的规格为：整体尺寸宽为70vp-98vp之间，高为40vp，标题和内容不支持自定义字体大小。

不同闪控球模板与样式布局示意如下，不同语言或内容以实际显示效果为准：

**图1** 静态布局

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/uG0dUp1nTIqpbrTvReFD_g/zh-cn_image_0000002558764672.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=13A502295C3A03DC82E0FB9E31D4DC393F053FDFB793A37AA0335F3AC198FC18)

**图2** 静态布局-超长文本标题

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/qDMTIcc8TXG0IWShW0WlXA/zh-cn_image_0000002558605018.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=D3DC79C098525CA4E945FD0484AC12FCFF7E1BFF3B907094DCF8EF10E67F0231)

**图3** 普通文本布局

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/3ZXI7mlnR_OJUl994kM-4g/zh-cn_image_0000002589324543.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=72CD524CE039F905F0C5BF60B76D3E9FE0583186F0C56CA5A7CB07F23C31F2AB)

**图4** 普通文本布局-超长文本内容

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/AJnR08hCRhugV88ipkt8XA/zh-cn_image_0000002589244481.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=C8893C92C705272CB178B9E13C986D06551397B5DACCDA581BD5C709C55EA823)

**图5** 强调文本布局

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/ABiEIswWQZmcwRvZDZ9Zgg/zh-cn_image_0000002558764674.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=E47781A3B8FC4625A42537475B8B43A112783B24D4EFB8FC712526D14838DB9B)

**图6** 强调文本布局-超长文本内容

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/bVRLZ_MfStuiHnYbpSnv1A/zh-cn_image_0000002558605020.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=7CA8C6805793E1E2E74EB98B345D13F3F31486834D04C2D5EEBEFE7697BE3724)

**图7** 强调文本布局-图标

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/pDDByHFcSLOPTHnHb6ZCiw/zh-cn_image_0000002589324545.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=901B13DDD24F7FCF5B4ADD0FCBC51EFD514AE0B3D81E3AAAC57A38A4ADC529DB)

**图8** 强调文本布局-图标和超长文本内容

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/v7oT1VtbS8yGAtL8kxT4kQ/zh-cn_image_0000002589244483.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=8B0D99B81F8B5DB7322B93B95896290F62A24B18CC61C06B190D15EAC2F838AC)

**图9** 纯文本布局

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/b0psRErjQuye8IGfqUyjKw/zh-cn_image_0000002558764676.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=00CAD47EDBA67D0CE864265B6D8EC2ADCA37580A416DF495D4C885A8298C1D81)

**图10** 纯文本布局-超长文本标题

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/V50KnkvhRw-SbSAFsGoAHQ/zh-cn_image_0000002558605022.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=8E58D3372DA6FF346B55F242063EEF64EA2BC0127CA4F38EAF95BC14F0D24716)

当有两个应用启动了闪控球后，闪控球将合并展示，如下图所示。整体高度为76vp。

**图11** 闪控球上下合并展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/ITWFn8XiTWGyOJCKLXpeIg/zh-cn_image_0000002589324547.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=607B364213F6E5E0F525863DB8076C74F53F305E99272C1C78D2FC8467D91DB9)

## 开发步骤

1. 导入模块并声明闪控球控制器。
2. 使用[create()](../harmonyos-references/js-apis-floatingball.md#floatingballcreate)接口创建闪控球控制器实例后注册点击事件回调和状态变化事件回调，通过[startFloatingBall()](../harmonyos-references/js-apis-floatingball.md#startfloatingball)接口启动闪控球。
3. 通过[updateFloatingBall()](../harmonyos-references/js-apis-floatingball.md#updatefloatingball)更新闪控球信息，以此控制闪控球展示的内容。
4. 通过[stopFloatingBall()](../harmonyos-references/js-apis-floatingball.md#stopfloatingball)停止闪控球。当不再需要显示闪控球时，可根据业务需要关闭闪控球。

```
1. // Utils.ts
2. // 该页面提供工具类，展示闪控球的创建、更新、关闭逻辑
3. import hilog from '@ohos.hilog';
4. import image from '@ohos.multimedia.image';
5. import { BusinessError } from '@kit.BasicServicesKit';
6. import { floatingBall } from '@kit.ArkUI';
7. import { Want } from '@kit.AbilityKit';
8. import { ContextUtil } from './ContextUtil';

10. const DOMAIN: number = 0xF811;
11. const TAG: string = '[Sample_FloatingBall]';
12. const BUNDLE_NAME: string = ContextUtil.context.abilityInfo.bundleName;

14. export class Utils {
15. public static getRawfilePixelMapSync(path: string): image.PixelMap {
16. try {
17. const BUFFER = ContextUtil.context.resourceManager.getRawFileContentSync(path);
18. const IMAGE_SOURCE: image.ImageSource = image.createImageSource(BUFFER.buffer as ArrayBuffer);
19. hilog.debug(DOMAIN, TAG, `Get rawfile pixelMap path '${path}' successfully`);
20. return IMAGE_SOURCE.createPixelMapSync();
21. } catch (e) {
22. hilog.error(DOMAIN, TAG, `Get rawfile pixelMap path '${path}' failed, error: ${e}`);
23. throw e as Error;
24. }
25. }

27. // 闪控球启动逻辑
28. public static async onClickCreateFloatingBall(
29. floatingBallController: floatingBall.FloatingBallController | undefined,
30. template: floatingBall.FloatingBallTemplate,
31. onActiveRowChange: (value: number) => void,  // 接收状态更新回调函数
32. title: string = 'title',
33. content: string = 'content',
34. backgroundColor: string = '#0ff77c',
35. icon?: image.PixelMap): Promise<void> {
36. // 注册 监听点击回调事件
37. floatingBallController?.on('click', () => {
38. hilog.debug(DOMAIN, TAG, `FloatingBall onClickEvent`);
39. let want: Want = {
40. bundleName: BUNDLE_NAME,
41. abilityName: 'MainAbility'
42. }
43. // 使用promise异步回调
44. floatingBallController?.restoreMainWindow(want)
45. .then(() => {
46. hilog.debug(DOMAIN, TAG, `Success in restoring FloatingBall main window`);
47. }).catch((err: BusinessError) => {
48. hilog.error(DOMAIN, TAG, `failed to restore FloatingBall main window. code: ${err.code}, message: ${err.message}`);
49. })
50. })
51. // 注册 监听状态变化事件
52. floatingBallController?.on('stateChange',
53. (state: floatingBall.FloatingBallState) => {
54. hilog.debug(DOMAIN, TAG, `FloatingBall stateCange: ${state}`);
55. if(state === floatingBall.FloatingBallState.STOPPED) {
56. floatingBallController?.off('click')
57. floatingBallController?.off('stateChange')
58. floatingBallController = undefined;
59. // 执行状态更新回调
60. onActiveRowChange?.(-1);
61. }
62. })
63. // 最后启动闪控球
64. let startParams: floatingBall.FloatingBallParams = icon? {
65. template: template,
66. title: title,
67. content: content,
68. backgroundColor: backgroundColor,
69. icon: icon
70. } : {
71. template: template,
72. title: title,
73. content: content,
74. backgroundColor: backgroundColor
75. }
76. try {
77. floatingBallController?.startFloatingBall(startParams)
78. .then(() => {
79. hilog.debug(DOMAIN, TAG, `succeed in starting FloatingBall`);
80. }).catch((err: BusinessError) => {
81. hilog.error(DOMAIN, TAG, `failed to start FloatingBall. code: ${err.code}, message: ${err.message}`);
82. })
83. } catch (e) {
84. console.error('startFloatingBall Error', e)
85. }
86. }

88. // 闪控球更新逻辑
89. public static onClickUpdateFloatingBall(
90. floatingBallController: floatingBall.FloatingBallController | undefined,
91. template: floatingBall.FloatingBallTemplate,
92. title: string = 'newTitle',
93. content: string = 'newContent',
94. icon?: image.PixelMap): void {
95. // 更新时给标题、内容 随机使用数字后缀
96. let random_string: string = Math.floor(Math.random() * 100).toString();
97. let updateParams: floatingBall.FloatingBallParams = icon ? {
98. template: template,
99. title: title + random_string,
100. content: content + random_string,
101. backgroundColor: '#f6ea0a',
102. icon: icon
103. } : {
104. template: template,
105. title: title + random_string,
106. content: content + random_string,
107. backgroundColor: '#f6ea0a',
108. }
109. try {
110. floatingBallController?.updateFloatingBall(updateParams).then(() => {
111. hilog.debug(DOMAIN, TAG, `Succeed in updating FloatingBall`);
112. }).catch((err: BusinessError) => {
113. hilog.error(DOMAIN, TAG, `failed to update FloatingBall. code: ${err.code}, message: ${err.message}`);
114. })
115. } catch (e) {
116. console.error('updateFloatingBall Error:', e)
117. }
118. }

120. // 闪控球停止逻辑
121. public static onClickStopFloatingBall(floatingBallController: floatingBall.FloatingBallController | undefined): void {
122. // stop 是异步流程，需要通过 stateChange 状态回调获取实际删除结果
123. floatingBallController?.stopFloatingBall().then(() => {
124. hilog.debug(DOMAIN, TAG, `Succeed in stopping FloatingBall`);
125. }).catch((err: BusinessError) => {
126. hilog.error(DOMAIN, TAG, `failed to stop FloatingBall. code: ${err.code}, message: ${err.message}`);
127. })
128. }
129. }
```

```
1. // Index.ets
2. // 该页面利用按钮点击事件展示闪控球基本操作
3. import hilog from '@ohos.hilog';
4. import image from '@ohos.multimedia.image';
5. import { floatingBall } from '@kit.ArkUI';
6. import { Utils } from '../util/Utils';

8. const DOMAIN: number = 0xF811;
9. const TAG: string = '[Sample_FloatingBall]';

11. @Entry
12. @Component
13. struct Index {
14. // 当前可用的行，-1 表示全部行可见
15. @State private activeRow: number = -1;
16. // 声明闪控球控制器
17. private floatingBallController: floatingBall.FloatingBallController | undefined = undefined;
18. // 缓存 icon 图标（静态布局）
19. private cachedIcon1: image.PixelMap | undefined = undefined;
20. // 缓存 icon 图标（强调文本布局）
21. private cachedIcon2: image.PixelMap | undefined = undefined;

23. // activeRow 的状态更新函数（确保闪控球销毁时，activeRow的值更新为-1）
24. private activeRowChange = (value: number) => {this.activeRow = value};

26. // 判断某个布局是否可用（是否置灰）
27. private isEnabled(rowInex: number): boolean {
28. return this.activeRow === -1 || this.activeRow === rowInex;
29. }

31. build() {
32. Column({space: 12}) {
33. // 静态布局，支持标题和图标，该布局在创建后无法修改
34. Row({space: 6}) {
35. Button('STATIC').onClick( async () => {
36. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回的结果是UIAbilityContext
37. if (!this.floatingBallController) {
38. this.floatingBallController = await floatingBall.create({
39. context: this.getUIContext().getHostContext()
40. })
41. }
42. if (this.floatingBallController) {
43. // 仅当没有缓存 cachedIcon1 时才加载；有缓存时，直接使用；
44. if (!this.cachedIcon1) {
45. let pixelMap = Utils.getRawfilePixelMapSync('books.png');  // 图片尺寸有最大限制
46. if (pixelMap) {
47. this.cachedIcon1 = pixelMap;  // 把图标缓存起了
48. hilog.debug(DOMAIN, TAG, `Success to load icon PixelMap`);
49. } else {
50. hilog.error(DOMAIN, TAG, `Failed to load icon PixelMap`);
51. }
52. }
53. Utils.onClickCreateFloatingBall(this.floatingBallController,
54. floatingBall.FloatingBallTemplate.STATIC, this.activeRowChange, 'title', 'content', '#0ff77c', this.cachedIcon1)
55. this.activeRow = 0;
56. }
57. })
58. .enabled(this.isEnabled(0))
59. // 更新闪控球信息（该布局在创建后无法更新，按钮永久置灰）
60. Button('Update1').enabled(false)
61. // 关闭闪控球
62. Button('Close1').onClick(() => {
63. Utils.onClickStopFloatingBall(this.floatingBallController);
64. this.activeRow = -1;  // 关闭后恢复所有行显示
65. })
66. .enabled(this.isEnabled(0))
67. }
68. .width('100%')
69. .justifyContent(FlexAlign.Center)

71. // 普通文本布局，支持标题和内容
72. Row({space: 6}) {
73. Button('NORMAL').onClick( async () => {
74. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回的结果是UIAbilityContext
75. if (!this.floatingBallController) {
76. this.floatingBallController = await floatingBall.create({
77. context: this.getUIContext().getHostContext()
78. })
79. }
80. if (this.floatingBallController) {
81. Utils.onClickCreateFloatingBall(this.floatingBallController,
82. floatingBall.FloatingBallTemplate.NORMAL, this.activeRowChange, 'title', 'content')
83. this.activeRow = 1;
84. }
85. })
86. .enabled(this.isEnabled(1))
87. // 更新闪控球信息
88. Button('Update2').onClick(() => Utils.onClickUpdateFloatingBall(this.floatingBallController,
89. floatingBall.FloatingBallTemplate.NORMAL))
90. .enabled(this.isEnabled(1))
91. // 关闭闪控球
92. Button('Close2').onClick(() => {
93. Utils.onClickStopFloatingBall(this.floatingBallController);
94. this.activeRow = -1;  // 关闭后恢复所有行显示
95. })
96. .enabled(this.isEnabled(1))
97. }
98. .width('100%')
99. .justifyContent(FlexAlign.Center)

101. // 强调文本布局，支持标题、图标和内容
102. Row({space: 6}) {
103. Button('EMPHATIC').onClick( async () => {
104. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回的结果是UIAbilityContext
105. if (!this.floatingBallController) {
106. this.floatingBallController = await floatingBall.create({
107. context: this.getUIContext().getHostContext()
108. })
109. }
110. if (this.floatingBallController) {
111. // 仅当没有缓存 cachedIcon2 时才加载；有缓存时，直接使用；
112. if(!this.cachedIcon2) {
113. let pixelMap = Utils.getRawfilePixelMapSync('video.png');  // 图片尺寸有最大限制
114. if (pixelMap) {
115. this.cachedIcon2 = pixelMap;  // 把图标缓存起了
116. hilog.debug(DOMAIN, TAG, `Success to load icon PixelMap`);
117. } else {
118. hilog.debug(DOMAIN, TAG, `Failed to load icon PixelMap`);
119. }
120. }
121. Utils.onClickCreateFloatingBall(this.floatingBallController,
122. floatingBall.FloatingBallTemplate.EMPHATIC, this.activeRowChange, '16', 'Min', '#0ff77c', this.cachedIcon2)
123. this.activeRow = 2;
124. }
125. })
126. .enabled(this.isEnabled(2))
127. // 更新闪控球信息
128. Button('Update3').onClick(() => Utils.onClickUpdateFloatingBall(this.floatingBallController,
129. floatingBall.FloatingBallTemplate.EMPHATIC, '', 'Min', this.cachedIcon2))
130. .enabled(this.isEnabled(2))
131. // 关闭闪控球
132. Button('Close3').onClick(() => {
133. Utils.onClickStopFloatingBall(this.floatingBallController);
134. this.activeRow = -1;  // 关闭后恢复所有行显示
135. })
136. .enabled(this.isEnabled(2))
137. }
138. .width('100%')
139. .justifyContent(FlexAlign.Center)

141. // 纯文本布局，只支持标题
142. Row({space: 6}) {
143. Button('SIMPLE').onClick( async () => {
144. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回的结果是UIAbilityContext
145. if (!this.floatingBallController) {
146. this.floatingBallController = await floatingBall.create({
147. context: this.getUIContext().getHostContext()
148. })
149. }
150. if (this.floatingBallController) {
151. Utils.onClickCreateFloatingBall(this.floatingBallController,
152. floatingBall.FloatingBallTemplate.SIMPLE, this.activeRowChange, 'title')
153. this.activeRow = 3;
154. }
155. })
156. .enabled(this.isEnabled(3))
157. // 更新闪控球信息
158. Button('Update4').onClick(() => Utils.onClickUpdateFloatingBall(this.floatingBallController,
159. floatingBall.FloatingBallTemplate.SIMPLE))
160. .enabled(this.isEnabled(3))
161. // 关闭闪控球
162. Button('Close4').onClick(() => {
163. Utils.onClickStopFloatingBall(this.floatingBallController);
164. this.activeRow = -1;  // 关闭后恢复所有行显示
165. })
166. .enabled(this.isEnabled(3))
167. }
168. .width('100%')
169. .justifyContent(FlexAlign.Center)
170. }
171. .width('100%')
172. .height('100%')
173. .justifyContent(FlexAlign.Center)
174. }
175. }
```

## 示例代码

[闪控球](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/FloatingBall)
