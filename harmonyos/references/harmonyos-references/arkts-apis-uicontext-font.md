---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-font
title: Class (Font)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (Font)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:49+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:931b919594f9e296ba2636793a05e10fa637cf5c322683b069095ccd8c1a6017
---

Font用于管理自定义字体和系统字体信息，支持注册自定义字体、获取系统字体列表、查询字体详细信息等功能，适用于需要在应用中使用自定义字体或查询系统字体资源的场景。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 10开始支持。
* 以下API需先使用UIContext中的[getFont()](arkts-apis-uicontext-uicontext.md#getfont)方法获取到Font对象，再通过该对象调用对应方法。
* 推荐使用字体引擎的[loadFontSync](js-apis-graphics-text.md#loadfontsync)接口注册自定义字体。

## registerFont

registerFont(options: font.FontOptions): void

在字体管理中注册自定义字体。

推荐使用字体引擎的[loadFontSync](js-apis-graphics-text.md#loadfontsync)接口注册自定义字体。

该接口的字体注册过程为异步，不支持并发调用。由于注册是异步完成的，建议在页面初始化阶段（如aboutToAppear）提前调用，以确保字体在使用前已注册完成。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [font.FontOptions](js-apis-font.md#fontoptions) | 是 | 注册的自定义字体信息。  **说明：**  设置注册字体文件的路径，读取系统沙箱路径内的资源时，建议使用file://路径前缀的字符串，需要确保沙箱目录路径下的文件存在并且有可读权限。 |

**示例：**

```ts
// xxx.ets
import { Font } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  private uiContext: UIContext = this.getUIContext();
  private font: Font = this.uiContext.getFont();

  aboutToAppear() {
    this.font.registerFont({
      familyName: 'medium',
      familySrc: '/font/medium.ttf' // font文件夹与pages目录同级
    });
  }

  build() {
    Column() {
      Text(this.message)
        .align(Alignment.Center)
        .fontSize(20)
        .fontFamily('medium') // medium：已注册的自定义字体名称。需先调用registerFont注册字体后，才能使用该字体名称。
    }.width('100%')
  }
}
```

## getSystemFontList

getSystemFontList(): Array<string>

获取系统支持的字体名称列表。

该接口仅在PC/2in1设备上生效，在其他设备上返回空数组。

推荐使用[getSystemFontFullNamesByType](js-apis-graphics-text.md#textgetsystemfontfullnamesbytype14)接口获取系统最新支持的字体列表数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 系统支持的字体名称列表，返回的名称可用于getFontByName方法查询对应字体的详细信息。 |

**示例：**

```ts
// xxx.ets
import { Font } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private uiContext: UIContext = this.getUIContext();
  private font: Font = this.uiContext.getFont();
  fontList: Array<string> = new Array<string>();

  build() {
    Column() {
      Button("getSystemFontList")
        .width('60%')
        .height('6%')
        .onClick(() => {
          this.fontList = this.font.getSystemFontList();
          console.info('getSystemFontList', JSON.stringify(this.fontList));
        })
    }.width('100%')
  }
}
```

## getFontByName

getFontByName(fontName: string): font.FontInfo

根据传入的系统字体名称获取系统字体的相关信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fontName | string | 是 | 系统的字体名，可通过[getSystemFontList()](arkts-apis-uicontext-font.md#getsystemfontlist)方法获取支持的字体名称列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [font.FontInfo](js-apis-font.md#fontinfo10) | 字体的详细信息。  如果查询不到字体，返回undefined。 |

**示例：**

```ts
// xxx.ets
import { Font, font } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private uiContext: UIContext = this.getUIContext();
  private font: Font = this.uiContext.getFont();
  fontInfo: font.FontInfo = this.font.getFontByName('');

  build() {
    Column() {
      Button("getFontByName")
        .width('60%')
        .height('6%')
        .onClick(() => {
          this.fontInfo = this.font.getFontByName('HarmonyOS Sans Italic');
          console.info("getFontByName(): path = " + this.fontInfo.path);
          console.info("getFontByName(): postScriptName = " + this.fontInfo.postScriptName);
          console.info("getFontByName(): fullName = " + this.fontInfo.fullName);
          console.info("getFontByName(): family = " + this.fontInfo.family);
          console.info("getFontByName(): subfamily = " + this.fontInfo.subfamily);
          console.info("getFontByName(): weight = " + this.fontInfo.weight);
          console.info("getFontByName(): width = " + this.fontInfo.width);
          console.info("getFontByName(): italic = " + this.fontInfo.italic);
          console.info("getFontByName(): monoSpace = " + this.fontInfo.monoSpace);
          console.info("getFontByName(): symbolic = " + this.fontInfo.symbolic);
        })
    }.width('100%')
  }
}
```
