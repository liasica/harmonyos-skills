---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/components-based-on-uniform-data-structure
title: 基于标准化数据结构的控件 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 标准化数据定义 > 基于标准化数据结构的控件 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:275565d1907c09ce7e94e061c873292c1b254dc1567e056a3734a30cd96a5af8
---

## 场景介绍

我们提供了部分标准化数据结构的预置卡片，当需要展示标准化数据结构数据时，可以直接引用提供的预置卡片，快捷地展示数据。

## 内容卡片控件

在需要展示内容（标题、描述、图片、应用信息）并在点击后跳转至对应来源时，可以使用内容卡片快速的展示信息。开发者只需要调用[ContentFormCard](../harmonyos-references/js-apis-data-udmfcomponents.md#contentformcard)接口，传入[ContentForm](../harmonyos-references/js-apis-data-uniformdatastruct.md#contentform14)数据、卡片宽高、点击事件回调函数即可获得良好的展示效果。

从API version 20开始，支持使用[内容卡片控件](../harmonyos-references/js-apis-data-udmfcomponents.md)。

### 接口说明

以下为内容卡片接口介绍：

| 接口名称 | 描述 |
| --- | --- |
| ContentFormCard({contentFormData: uniformDataStruct.ContentForm, formType: FormType, formWidth?: number, formHeight?: number, handleOnClick?: Function}) | 按照固定的样式展示传入的内容卡片数据，并在点击操作时，执行回调函数，并跳转至配置的页面。 |

### 开发示例

```
1. // 1. 导入需要的模块
2. import { ContentFormCard, FormType, uniformDataStruct } from '@kit.ArkData';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Entry
6. @Component
7. struct Index {
8. @State contentForm: uniformDataStruct.ContentForm = {
9. uniformDataType: 'general.content-form',
10. title: ''
11. };
12. @State startToShow: boolean = false;

14. aboutToAppear(): void {
15. // 2. 初始化数据
16. this.initData();
17. }

19. async initData() {
20. let context = this.getUIContext().getHostContext();
21. if (!context) {
22. return;
23. }
24. try {
25. let appIcon = await context.resourceManager.getMediaContent($r('app.media.startIcon').id);
26. let thumbImage = await context.resourceManager.getMediaContent($r('app.media.foreground').id);
27. this.contentForm = {
28. uniformDataType: 'general.content-form',
29. title: 'Content form title',
30. thumbData: appIcon,
31. description: 'Content form description',
32. appIcon: thumbImage,
33. appName: 'com.test.demo'
34. };
35. } catch (err) {
36. hilog.error(0xFF00, '[Sample_Udmf]', 'Init data error');
37. }
38. }

40. build() {
41. Column() {
42. Button('show card').fontSize(30)
43. .onClick(() => {
44. // 3. 点击后startToShow变为true，页面重新渲染
45. this.startToShow = true;
46. })
47. if (this.startToShow) {
48. // 4. 使用内容卡片，传入对应的参数
49. ContentFormCard({
50. contentFormData: this.contentForm,
51. formType: FormType.TYPE_SMALL,
52. formWidth: 220,
53. formHeight: 100,
54. handleOnClick: () => {
55. hilog.info(0xFF00, '[Sample_Udmf]', 'Clicked card');
56. }
57. })
58. }
59. }
60. .height('100%')
61. .width('100%')
62. .justifyContent(FlexAlign.Center)
63. }
64. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/Udmf/ContentForm/entry/src/main/ets/pages/Index.ets#L16-L81)
