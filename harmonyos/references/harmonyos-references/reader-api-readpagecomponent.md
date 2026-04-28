---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/reader-api-readpagecomponent
title: ReadPageComponent（阅读页组件）
breadcrumb: API参考 > 应用服务 > Reader Kit（阅读服务） > ArkTS组件 > ReadPageComponent（阅读页组件）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f51e1ec155b32caa3d1078530003f2d8e548874b7241bc2e0a95956838ac5dbf
---

本模块提供ReadPageComponent组件，HarmonyOS应用通过集成该组件可快速构建书籍阅读功能。

**起始版本：** 5.0.4(16)

## 导入模块

PhonePC/2in1Tablet

```
1. import { ReadPageComponent } from '@kit.ReaderKit';
```

## ReadPageComponent

PhonePC/2in1Tablet

阅读页组件，支持对书籍排版内容的显示、多种翻页交互和翻页动效，以及翻页阅读过程中阅读器所需要的进度、行为感知能力。

说明

* 支持根据阅读排版设置[ReaderSetting](reader-read-core.md#readersetting)对书籍内容进行按页进行排版、渲染。
* 支持适配不同的设备屏幕尺寸（Phone、PC/2in1、Tablet，包括横竖屏适配），并在此基础上支持通过点击、滑动的方式进行阅读交互，支持仿真、横滑翻页方式（包括翻页过程动效）。
* 支持排版结果通知能力，打开书籍或者触发翻页后按页提供当前页的排版结果信息[PageDataInfo](reader-read-core.md#pagedatainfo)。

**装饰器类型：** @Component

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

**参数：**

| 参数名 | 类型 | 装饰器类型 | 说明 |
| --- | --- | --- | --- |
| controller | [ReaderComponentController](reader-read-core.md#readercomponentcontroller) | \_ | ReadPageComponent控制器。 |
| readerCallback | AsyncCallback<readerCore.[ReaderComponentController](reader-read-core.md#readercomponentcontroller)> | \_ | 回调函数。 |

### build

PhonePC/2in1Tablet

build(): void

用于创建ReadPageComponent对象的构造函数。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

**示例：**

```
1. import { bookParser, readerCore, ReadPageComponent } from '@kit.ReaderKit';
2. import { common } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct Reader {
9. private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();

11. aboutToAppear(): void {
12. this.init();
13. }

15. private async init() {
16. // 通过提前导入到应用沙箱目录中的书籍文件，初始化书籍解析器
17. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
18. let filePath: string = `${context.filesDir}/abc.epub`;
19. let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
20. let spineList: bookParser.SpineItem[] = bookParserHandler.getSpineList();
21. let spineIndex: number = spineList[0].index;
22. let domPos: string = '';

24. await this.readerComponentController.init(context);
25. this.readerComponentController.registerBookParser(bookParserHandler);
26. this.readerComponentController.startPlay(spineIndex || 0, domPos);
27. hilog.info(0x0000, 'testTag', `startPlay succeeded`);
28. }

30. aboutToDisappear(): void {
31. this.readerComponentController.releaseBook();
32. }

34. build() {
35. Stack() {
36. ReadPageComponent({
37. controller: this.readerComponentController,
38. readerCallback: (err: BusinessError, data: readerCore.ReaderComponentController) => {
39. this.readerComponentController = data;
40. }
41. })
42. }.width('100%').height('100%').onClick(() => {
43. // 支持在此实现点击拉起菜单栏功能
44. })
45. }
46. }
```
