---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-guidelines-albumpicker
title: 使用AlbumPicker组件访问相册列表
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 使用AlbumPicker组件访问相册列表
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d671289231a74d0fb775be456026d1076c11556bb6cd2c96262542558ce234c9
---

开发者可以在布局中嵌入AlbumPickerComponent组件，通过此组件，应用无需申请权限，即可访问公共目录中的相册列表。

需配合[使用PhotoPicker组件访问图片/视频](component-guidelines-photoviewpicker.md)一起使用，用户通过AlbumPickerComponent组件选择对应相册并通知PhotoPickerComponent组件刷新成对应相册的图片和视频。

界面效果如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/ydV754GrRcqPptA4ClK6PQ/zh-cn_image_0000002583438651.png?HW-CC-KV=V1&HW-CC-Date=20260427T234634Z&HW-CC-Expire=86400&HW-CC-Sign=6C0FA5629E1CF2BF052153B26F4C3826EB7A4C65101D56993CA7BB3FE432AFC6)

## 开发步骤

1. 导入相册组件模块文件。

   ```
   1. import {
   2. AlbumPickerComponent,
   3. AlbumPickerOptions,
   4. AlbumInfo,
   5. PickerColorMode,
   6. PickerController,
   7. DataType
   8. } from '@kit.MediaLibraryKit';
   ```
2. 创建相册组件配置选项实例（AlbumPickerOptions）。

   通过AlbumPickerOptions，开发者可配置相册页主题颜色，详见[AlbumPickerOptions API参考](../harmonyos-references/ohos-file-albumpickercomponent.md#albumpickeroptions)。

   ```
   1. // 用于相册组件初始化时设置参数信息。
   2. albumOptions: AlbumPickerOptions = new AlbumPickerOptions();
   3. pickerController: PickerController = new PickerController();
   ```
3. 初始化组件配置选项实例（AlbumPickerOptions）。

   ```
   1. /**
   2. * 设置相册页颜色模式， 默认AUTO。
   3. * AUTO：跟随系统的模式，LIGHT：浅色模式，DARK：深色模式。
   4. */
   5. this.albumOptions.themeColorMode = PickerColorMode.AUTO;
   ```
4. 创建[AlbumPickerComponent](../harmonyos-references/ohos-file-albumpickercomponent.md#albumpickercomponent)组件。

   ```
   1. AlbumPickerComponent({
   2. // 设置组件选择选项实例。
   3. albumPickerOptions: this.albumOptions,

   5. /**
   6. *相册被选中回调，返回相册信息。
   7. * AlbumInfo（uri）
   8. */
   9. onAlbumClick: (albumInfo: AlbumInfo): boolean => this.onAlbumClick(albumInfo),
   10. })
   ```
5. 与PhotoPicker组件联动，将相册URI给到应用，根据相册URI更新PhotoPicker组件宫格页内容。

   ```
   1. private onAlbumClick(albumInfo: AlbumInfo): boolean {
   2. if (albumInfo?.uri) {
   3. // 根据相册url更新宫格页内容。
   4. this.pickerController.setData(DataType.SET_ALBUM_URI, albumInfo.uri);
   5. }
   6. return true;
   7. }
   ```

## 完整示例

```
1. import {
2. PhotoPickerComponent,
3. AlbumPickerComponent,
4. AlbumPickerOptions,
5. AlbumInfo,
6. PickerColorMode,
7. PickerController,
8. DataType
9. } from '@kit.MediaLibraryKit';

11. @Entry
12. @Component
13. struct AlbumPage {
14. @State pickerController: PickerController = new PickerController();
15. @State Width: string = '100%';
16. @State Height: string = '100%';
17. @State isShowAlbum: boolean = false;
18. @State fontColor: string = '#182431222'
19. @State selectedFontColor: string = '#007DFF'
20. @State currentIndex: number = 0
21. private controller: TabsController = new TabsController();
22. albumOptions = new AlbumPickerOptions();
23. albumOptions1 = new AlbumPickerOptions();
24. albumOptions2 = new AlbumPickerOptions();

26. /**
27. *相册被选中回调，返回相册信息
28. * AlbumInfo（uri）
29. */
30. private onAlbumClick(albumInfo: AlbumInfo): boolean {
31. this.isShowAlbum = false;
32. if (albumInfo?.uri) {
33. //  根据相册url更新宫格页内容。
34. this.pickerController.setData(DataType.SET_ALBUM_URI, albumInfo.uri);
35. }
36. return true;
37. }

39. aboutToAppear() {
40. /**
41. * 设置相册页颜色模式， 默认AUTO。
42. * AUTO：跟随系统的模式， LIGHT：浅色模式， DARK：深色模式
43. */
44. this.albumOptions.themeColorMode = PickerColorMode.AUTO;
45. this.albumOptions1.themeColorMode = PickerColorMode.LIGHT;
46. this.albumOptions2.themeColorMode = PickerColorMode.DARK;
47. }

49. // 设置导航栏的样式
50. @Builder
51. tabBuilder(index: number, name: string) {
52. Column() {
53. Text(name)
54. .fontColor(this.currentIndex === index ? this.selectedFontColor : this.fontColor)
55. .fontSize(16)
56. .fontWeight(this.currentIndex === index ? 500 : 400)
57. .lineHeight(22)
58. .margin({ top: 17, bottom: 7 })
59. Divider()
60. .strokeWidth(2)
61. .color('#007DFF')
62. .opacity(this.currentIndex === index ? 1 : 0)
63. }.width('100%')
64. }

66. build() {
67. Stack() {
68. Column() {
69. Row() {
70. Button("全部相册").width('95%').height('5%').onClick(() => {
71. this.isShowAlbum = true;
72. })
73. }.margin({ top: 40 })
74. Column() {
75. PhotoPickerComponent({
76. pickerController: this.pickerController,
77. }).height(this.Height).width(this.Width)
78. }.width('100%').height('100%').alignItems(HorizontalAlign.Center).visibility(this.isShowAlbum ? Visibility.None: Visibility.Visible)
79. }

81. if (this.isShowAlbum) {
82. Row() {
83. Column() {
84. /**
85. * 使用3个组件,以便更好展示不同效果。
86. * 需要注意的是切换tab会导致AlbumPickerComponent覆盖在PhotoPickerComponent上导致点击事件失效，
87. * 设置PhotoPickerComponent不可见可以规避点击失效。
88. */
89. Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
90. TabContent() {
91. AlbumPickerComponent({
92. albumPickerOptions: this.albumOptions,
93. onAlbumClick: (albumInfo: AlbumInfo): boolean => this.onAlbumClick(albumInfo),
94. }).height('100%').width('100%')
95. }.tabBar(this.tabBuilder(0, '系统'))
96. TabContent() {
97. AlbumPickerComponent({
98. albumPickerOptions: this.albumOptions1,
99. onAlbumClick: (albumInfo: AlbumInfo): boolean => this.onAlbumClick(albumInfo),
100. }).height('100%').width('100%')
101. }.tabBar(this.tabBuilder(1, '浅色'))

103. TabContent() {
104. AlbumPickerComponent({
105. albumPickerOptions: this.albumOptions2,
106. onAlbumClick: (albumInfo: AlbumInfo): boolean => this.onAlbumClick(albumInfo),
107. }).height('100%').width('100%')
108. }.tabBar(this.tabBuilder(2, '深色'))
109. }
110. .vertical(false)
111. .barMode(BarMode.Fixed)
112. .barWidth('100%')
113. .barHeight(56)
114. .animationDuration(100)
115. .onChange((index: number) => {
116. this.currentIndex = index;
117. })
118. .width('100%')
119. .height('100%')
120. .backgroundColor('#F1F3F5')
121. }.width('100%').height('100%').justifyContent(FlexAlign.Center).alignItems(HorizontalAlign.Center)
122. }
123. .margin({ top: 40 })
124. }
125. }
126. }
127. }
```
