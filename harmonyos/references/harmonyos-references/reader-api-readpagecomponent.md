---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/reader-api-readpagecomponent
title: ReadPageComponent（阅读页组件）
breadcrumb: API参考 > 应用服务 > Reader Kit（阅读服务） > ArkTS组件 > ReadPageComponent（阅读页组件）
category: harmonyos-references
scraped_at: 2026-09-02T15:03:08+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:44a42170726a235ea576db871800a6dbcd31c8c03f3e5b89dd872f0789c2827d
---

本模块提供ReadPageComponent组件，HarmonyOS应用通过集成该组件可快速构建书籍阅读功能。

**起始版本：** 5.0.4(16)

## 导入模块

```typescript
import { ReadPageComponent } from '@kit.ReaderKit';
```

## ReadPageComponent

阅读页组件，支持对书籍排版内容的显示、多种翻页交互和翻页动效，以及翻页阅读过程中阅读器所需要的进度、行为感知能力。

**说明** 

* 支持根据阅读排版设置[ReaderSetting](reader-read-core.md#readersetting)对书籍内容进行按页进行排版、渲染。
* 支持适配不同的设备屏幕尺寸（Phone、PC/2in1、Tablet，包括横竖屏适配），并在此基础上支持通过点击、滑动的方式进行阅读交互，支持仿真、横滑翻页方式（包括翻页过程动效）。
* 支持排版结果通知能力，打开书籍或者触发翻页后按页提供当前页的排版结果信息[PageDataInfo](reader-read-core.md#pagedatainfo)。

**装饰器类型：** @Component

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

**参数：**

| 参数名 | 类型 | 装饰器类型 | 说明 |
| --- | --- | --- | --- |
| controller | readerCore.[ReaderComponentController](reader-read-core.md#readercomponentcontroller) | - | ReadPageComponent控制器。 |
| readerCallback | AsyncCallback<readerCore.[ReaderComponentController](reader-read-core.md#readercomponentcontroller)> | - | 回调函数。 |

### build

build(): void

用于创建ReadPageComponent对象的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

**示例：**

```typescript
import { bookParser, readerCore, ReadPageComponent } from '@kit.ReaderKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Reader {
  private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();

  aboutToAppear(): void {
    this.init();
  }

  private async init() {
    // 通过提前导入到应用沙箱目录中的书籍文件，初始化书籍解析器
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let filePath: string = `${context.filesDir}/abc.epub`;
    let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
    let spineList: bookParser.SpineItem[] = bookParserHandler.getSpineList();
    let spineIndex: number = spineList[0].index;
    let domPos: string = '';

    await this.readerComponentController.init(context);
    this.readerComponentController.registerBookParser(bookParserHandler);
    await this.readerComponentController.startPlay(spineIndex || 0, domPos);
    hilog.info(0x0000, 'testTag', `startPlay succeeded`);
  }

  aboutToDisappear(): void {
    this.readerComponentController.releaseBook();
  }

  build() {
    Stack() {
      ReadPageComponent({
        controller: this.readerComponentController,
        readerCallback: (err: BusinessError, data: readerCore.ReaderComponentController) => {
          this.readerComponentController = data;
        }
      })
    }.width('100%').height('100%').onClick(() => {
      // 支持在此实现点击拉起菜单栏功能
    })
  }
}
```
