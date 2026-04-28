---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkui-suggest-use-effectkit-blur
title: @performance/hp-arkui-suggest-use-effectkit-blur
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-suggest-use-effectkit-blur
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:08+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:d346548f5794abcc9be2f721221072e63e3d1c4cfeb799bfee2367f90d338f19
---

建议使用effectKit.createEffect实现模糊效果。

通用丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-suggest-use-effectkit-blur": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // 导入图片处理模块
2. import image from '@ohos.multimedia.image';
3. // 导入图像效果模块
4. import effectKit from '@ohos.effectKit';

6. @Entry
7. @Component
8. struct MyComponent {
9. // 是否显示全屏模态页面。静态模糊用
10. @State isShowStaticBlur: boolean = false;
11. // PixelMap实例
12. @State pixelMap: image.PixelMap | undefined = undefined;
13. // ImageSource实例
14. imgSource: image.ImageSource | undefined = undefined;

16. // 静态模糊
17. async staticBlur() {
18. // 获取resourceManager对象
19. let resourceMgr = this.getUIContext()?.getHostContext()?.resourceManager;
20. // 获rawfile目录下的图片
21. const fileData = await resourceMgr?.getRawFileContent('startIcon.png');
22. // 创建实例
23. let buffer = fileData?.buffer.slice(0);
24. if (buffer) {
25. // 创建图片源实例
26. this.imgSource = image.createImageSource(buffer);
27. }
28. // 创建像素的属性
29. let opts: image.InitializationOptions = {
30. // 是否可编辑
31. editable: true,
32. // 像素格式。3表示RGBA_8888
33. pixelFormat: 3,
34. // 创建图片大小
35. size: {
36. height: 4,
37. width: 6
38. }
39. };
40. // 创建PixelMap
41. await this.imgSource?.createPixelMap(opts).then((pixelMap: image.PixelMap) => {
42. // 模糊半径
43. const blurRadius = 1;
44. // 创建Filter实例
45. let headFilter = effectKit.createEffect(pixelMap);
46. if (headFilter != null) {
47. // 设置静态模糊。将模糊效果添加到效果链表中
48. headFilter.blur(blurRadius);
49. // 获取已添加链表效果的源图像的image.PixelMap
50. headFilter.getEffectPixelMap().then((pixelMap: image.PixelMap) => {
51. this.pixelMap = pixelMap;
52. });
53. }
54. })
55. }

57. // 图片设置静态模糊的模态页面
58. @Builder
59. staticBlurBuilder() {
60. Stack() {
61. Image(this.pixelMap)
62. .width('100%')
63. .height('100%')
64. .objectFit(ImageFit.Fill)
65. Button('close')
66. .fontSize(20)
67. .onClick(() => {
68. this.isShowStaticBlur = false;
69. })
70. }
71. .width('100%')
72. .height('100%')
73. }

75. build() {
76. Column({ space: 10 }) {
77. Button('静态模糊')
78. .onClick(() => {
79. this.isShowStaticBlur = true;
80. // 设置静态模糊
81. this.staticBlur();
82. })
83. .bindContentCover(this.isShowStaticBlur, this.staticBlurBuilder(), {
84. // 全屏模态转场类型。上下切换动画
85. modalTransition: ModalTransition.DEFAULT
86. })
87. }
88. .width('100%')
89. .height('100%')
90. .justifyContent(FlexAlign.Center)
91. }
92. }
```

## 反例

```
1. @Entry
2. @Component
3. struct MyComponent {
4. build() {
5. Column({ space: 10 }) {
6. // 对image进行模糊，未使用effectKit.createEffect
7. Text('Image blur').fontSize(15).fontColor(0xCCCCCC).width('90%')
8. Image('resources/base/media/sss001.jpg')
9. .blur(1)
10. .border({ width: 1 })
11. .borderStyle(BorderStyle.Dashed)
12. .aspectRatio(1)
13. .width('90%')
14. .height(40)

16. // 对背景进行模糊，未使用effectKit.createEffect
17. Text('backdropBlur').fontSize(15).fontColor(0xCCCCCC).width('90%')
18. Text()
19. .width('90%')
20. .height(40)
21. .fontSize(16)
22. .backdropBlur(3)
23. .backgroundImage('/pages/attrs/image/image.jpg')
24. .backgroundImageSize({ width: 1200, height: 160 })
25. }.width('100%').margin({ top: 5 })
26. }
27. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
