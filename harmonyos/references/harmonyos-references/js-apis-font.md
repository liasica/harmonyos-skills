---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-font
title: @ohos.font (注册自定义字体)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.font (注册自定义字体)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b543924334ab348211470de868583acf292a399df6d403122770704e3bd2439e
---

本模块提供注册自定义字体。

说明

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的地方使用，参见[UIContext](arkts-apis-uicontext-uicontext.md)说明。
* 推荐使用字体引擎的[loadFontSync](js-apis-graphics-text.md#loadfontsync)接口注册自定义字体。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { font } from '@kit.ArkUI';
```

## font.registerFont(deprecated)

PhonePC/2in1TabletTVWearable

registerFont(options: FontOptions): void

在字体管理中注册自定义字体。

该接口为异步接口，不支持并发调用。

说明

* 从API version 9开始支持，从API version 18开始废弃，建议使用[registerFont](arkts-apis-uicontext-font.md#registerfont)替代。registerFont需要先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getFont](arkts-apis-uicontext-uicontext.md#getfont)方法获取[Font](arkts-apis-uicontext-font.md)对象，然后通过该对象进行调用。且直接使用registerFont可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getFont](arkts-apis-uicontext-uicontext.md#getfont)方法获取当前UI上下文关联的[Font](arkts-apis-uicontext-font.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [FontOptions](js-apis-font.md#fontoptions) | 是 | 注册的自定义字体信息。 |

## FontOptions

PhonePC/2in1TabletTVWearable

注册的自定义字体信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| familyName | string | [Resource](ts-types.md#resource)10+ | 否 | 否 | 设置注册的字体名称。 |
| familySrc | string | [Resource](ts-types.md#resource)10+ | 否 | 否 | 设置注册字体文件的路径。  **说明：**  读取系统沙箱路径内的资源时，建议使用file://路径前缀的字符串，需要确保沙箱目录路径下的文件存在并且有可读权限。 |

说明

直接使用font可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题，推荐通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getFont](arkts-apis-uicontext-uicontext.md#getfont)方法获取当前UI上下文关联的[Font](arkts-apis-uicontext-font.md)对象。

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct FontExample {
5. @State message: string = 'Hello World';
6. // iconFont示例，假设0000为指定icon的Unicode，实际需要开发者从注册的iconFont的ttf文件里面获取Unicode
7. @State unicode: string = '\u0000';
8. @State codePoint: string = String.fromCharCode(0x0000);
9. private uiContext: UIContext = this.getUIContext();

11. aboutToAppear() {
12. // familyName和familySrc都支持系统Resource
13. this.uiContext.getFont().registerFont({
14. // 建议使用 this.getUIContext().getFont().registerFont()接口
15. // 'app.string.font_name'和'app.string.font_src'仅作示例，请替换为实际使用资源字符串
16. familyName: $r('app.string.font_name'),
17. familySrc: $r('app.string.font_src')
18. })

20. // familySrc支持RawFile
21. this.uiContext.getFont().registerFont({
22. familyName: 'mediumRawFile',
23. familySrc: $rawfile('font/medium.ttf')// 'font/medium.ttf'仅作示例，请替换为实际使用资源字体文件
24. })

26. // 注册iconFont
27. this.uiContext.getFont().registerFont({
28. familyName: 'iconFont',
29. familySrc: '/font/iconFont.ttf'
30. })

32. // familyName和familySrc都支持string
33. this.uiContext.getFont().registerFont({
34. familyName: 'medium',
35. familySrc: '/font/medium.ttf' // font文件夹与pages目录同级
36. })
37. }

39. build() {
40. Column() {
41. Text(this.message)
42. .align(Alignment.Center)
43. .fontSize(20)
44. .fontFamily('medium') // medium：注册自定义字体的名字（$r('app.string.mediumFamilyName')、'mediumRawFile'等已注册字体也能正常使用）

46. // 使用iconFont的两种方式
47. Text(this.unicode)
48. .align(Alignment.Center)
49. .fontSize(20)
50. .fontFamily('iconFont')
51. Text(this.codePoint)
52. .align(Alignment.Center)
53. .fontSize(20)
54. .fontFamily('iconFont')
55. }.width('100%')
56. }
57. }
```

说明

应用若需全局使用自定义字体，请在EntryAbility.ets文件的[onWindowStageCreate](js-apis-app-ability-uiability.md#onwindowstagecreate)生命周期中，通过[windowStage.loadContent](arkts-apis-window-window.md#loadcontent9)回调注册。

在HSP工程中，不推荐采用相对路径的方式注册自定义字体，详见[通过$r访问HSP中的资源](../harmonyos-guides/in-app-hsp.md)。

## font.getSystemFontList(deprecated)

PhonePC/2in1TabletTVWearable

getSystemFontList(): Array<string>

获取系统字体列表。

该接口仅在PC/2in1设备上生效，在其他设备上返回空数组。

推荐使用[getSystemFontFullNamesByType](js-apis-graphics-text.md#textgetsystemfontfullnamesbytype14)接口获取系统最新支持的字体列表数据。

说明

* 从API version 10开始支持，从API version 18开始废弃，建议使用[getSystemFontList](arkts-apis-uicontext-font.md#getsystemfontlist)替代。getSystemFontList需要先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getFont](arkts-apis-uicontext-uicontext.md#getfont)方法获取[Font](arkts-apis-uicontext-font.md)对象，然后通过该对象进行调用。且直接使用getSystemFontList可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getFont](arkts-apis-uicontext-uicontext.md#getfont)方法获取当前UI上下文关联的[Font](arkts-apis-uicontext-font.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 系统的字体名列表。 |

说明

直接使用font可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题，推荐通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getFont](arkts-apis-uicontext-uicontext.md#getfont)方法获取当前UI上下文关联的[Font](arkts-apis-uicontext-font.md)对象。

**示例：**

```
1. // xxx.ets
2. import { font } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct FontExample {
7. fontList: Array<string> = new Array<string>();

9. build() {
10. Column() {
11. Button("getSystemFontList")
12. .width('60%')
13. .height('6%')
14. .onClick(() => {
15. this.fontList = font.getSystemFontList(); // 建议使用 this.getUIContext().getFont().getSystemFontList()接口
16. })
17. }.width('100%')
18. }
19. }
```

## font.getFontByName(deprecated)

PhonePC/2in1TabletTVWearable

getFontByName(fontName: string): FontInfo

根据传入的系统字体名称获取系统字体的相关信息。

说明

* 从API version 10开始支持，从API version 18开始废弃，建议使用[getFontByName](arkts-apis-uicontext-font.md#getfontbyname)替代。getFontByName需要先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getFont](arkts-apis-uicontext-uicontext.md#getfont)方法获取[Font](arkts-apis-uicontext-font.md)对象，然后通过该对象进行调用。且直接使用getFontByName可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getFont](arkts-apis-uicontext-uicontext.md#getfont)方法获取当前UI上下文关联的[Font](arkts-apis-uicontext-font.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fontName | string | 是 | 系统的字体名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FontInfo | 字体的详细信息。 |

## FontInfo10+

PhonePC/2in1TabletTVWearable

字体的详细信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| path | string | 否 | 否 | 系统字体的文件路径。 |
| postScriptName | string | 否 | 否 | 系统字体的postScript名称。 |
| fullName | string | 否 | 否 | 系统字体的名称。 |
| family | string | 否 | 否 | 系统字体的字体家族。 |
| subfamily | string | 否 | 否 | 系统字体的子字体家族。 |
| weight | number | 否 | 否 | 系统字体的字重。  取值范围：[100,900]，取值间隔为100，分别对应[FontWeight](js-apis-graphics-text.md#fontweight)枚举中的值。  默认值：100 |
| width | number | 否 | 否 | 系统字体的宽度。  取值范围：[1,9]，取值间隔为1，分别对应[FontWidth](js-apis-graphics-text.md#fontwidth)枚举中的值。 |
| italic | boolean | 否 | 否 | 系统字体是否倾斜。  默认值：false  值为true，表示斜体字体，值为false，表示非斜体字体。 |
| monoSpace | boolean | 否 | 否 | 系统字体是否等宽。  默认值：false  值为true，表示等宽字体，值为false，表示非等宽字体。 |
| symbolic | boolean | 否 | 否 | 系统字体是否支持符号字体。  默认值：false  值为true，表示支持符号字体，值为false，表示不支持符号字体。 |

**示例：**

说明

直接使用font可能导致实例不明确的问题，推荐通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getFont](arkts-apis-uicontext-uicontext.md#getfont)方法获取当前UI上下文关联的[Font](arkts-apis-uicontext-font.md)对象。

```
1. // xxx.ets
2. import { font } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct FontExample {
7. fontList: Array<string> = new Array<string>();
8. uiFont = this.getUIContext().getFont();
9. fontInfo: font.FontInfo = this.uiFont.getFontByName(''); // 建议使用 this.getUIContext().getFont().getFontByName()接口

11. build() {
12. Column() {
13. Button("getFontByName")
14. .onClick(() => {
15. this.fontInfo =
16. this.uiFont.getFontByName('HarmonyOS Sans Italic');
17. console.info("getFontByName(): path = " + this.fontInfo.path);
18. console.info("getFontByName(): postScriptName = " + this.fontInfo.postScriptName);
19. console.info("getFontByName(): fullName = " + this.fontInfo.fullName);
20. console.info("getFontByName(): family = " + this.fontInfo.family);
21. console.info("getFontByName(): subfamily = " + this.fontInfo.subfamily);
22. console.info("getFontByName(): weight = " + this.fontInfo.weight);
23. console.info("getFontByName(): width = " + this.fontInfo.width);
24. console.info("getFontByName(): italic = " + this.fontInfo.italic);
25. console.info("getFontByName(): monoSpace = " + this.fontInfo.monoSpace);
26. console.info("getFontByName(): symbolic = " + this.fontInfo.symbolic);
27. })
28. }.width('100%')
29. }
30. }
```

## font.getUIFontConfig11+

PhonePC/2in1TabletTVWearable

getUIFontConfig() : UIFontConfig

获取系统字体配置文件的UI字体配置信息。

该接口仅支持获取配置文件内的信息以及当UI上下文不明确时可能返回undefined，如果想要获取全量的字体配置信息，推荐使用字体引擎的[getSystemFontFullNamesByType](js-apis-graphics-text.md#textgetsystemfontfullnamesbytype14)接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UIFontConfig](js-apis-font.md#uifontconfig11) | 系统的UI字体配置信息。 |

## UIFontConfig11+

PhonePC/2in1TabletTVWearable

系统的UI字体配置信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontDir | Array<string> | 否 | 否 | 系统字体文件所在的路径。 |
| generic | Array<[UIFontGenericInfo](js-apis-font.md#uifontgenericinfo11)> | 否 | 否 | 系统所支持的通用字体集列表。 |
| fallbackGroups | Array<[UIFontFallbackGroupInfo](js-apis-font.md#uifontfallbackgroupinfo11)> | 否 | 否 | 备用字体集。 |

## UIFontGenericInfo11+

PhonePC/2in1TabletTVWearable

系统所支持的通用字体集列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| family | string | 否 | 否 | 字体集名，字体文件中指定的"family"值。 |
| alias | Array<[UIFontAliasInfo](js-apis-font.md#uifontaliasinfo11)> | 否 | 否 | 别名列表。 |
| adjust | Array<[UIFontAdjustInfo](js-apis-font.md#uifontadjustinfo11)> | 否 | 否 | 字体原本的weight值对应需显示的值。 |

## UIFontFallbackGroupInfo11+

PhonePC/2in1TabletTVWearable

备用字体集。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontSetName | string | 否 | 否 | 备用字体集所对应的字体集名称。 |
| fallback | Array<[UIFontFallbackInfo](js-apis-font.md#uifontfallbackinfo11)> | 否 | 否 | 表示以下列表为该字体集的备用字体，如果fontSetName为""，表示可以作为所有字体集的备用字体。 |

## UIFontAliasInfo11+

PhonePC/2in1TabletTVWearable

别名列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 别名名称。 |
| weight | number | 否 | 否 | 当weight>0时表示此字体集只包含所指定weight的字体，当weight=0时，表示此字体集包含所有字体。  可返回的值有0、100、400、700、900。 |

## UIFontAdjustInfo11+

PhonePC/2in1TabletTVWearable

字体原本的weight值和显示实际值的映射列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| weight | number | 否 | 否 | 字体原本的weight值。  可返回的值有50、80、100、200。 |
| to | number | 否 | 否 | 字体在应用中显示的weight值。  可返回的值有100、400、700、900。 |

## UIFontFallbackInfo11+

PhonePC/2in1TabletTVWearable

该字体集的备用字体。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| language | string | 否 | 否 | 字体集所支持的语言类型，语言格式为bcp47。 |
| family | string | 否 | 否 | 字体集名，字体文件中指定的"family"值。 |

**示例：**

```
1. // xxx.ets
2. import { font } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct FontExample {
7. build() {
8. Column() {
9. Button("getUIFontConfig")
10. .width('60%')
11. .height('6%')
12. .margin(50)
13. .onClick(() => {
14. let fontConfig = font.getUIFontConfig();
15. console.info("font-dir -----------" + String(fontConfig.fontDir.length));
16. for (let i = 0; i < fontConfig.fontDir.length; i++) {
17. console.info(fontConfig.fontDir[i]);
18. }
19. console.info("generic-------------" + String(fontConfig.generic.length));
20. for (let i = 0; i < fontConfig.generic.length; i++) {
21. console.info("family:" + fontConfig.generic[i].family);
22. for (let j = 0; j < fontConfig.generic[i].alias.length; j++) {
23. console.info(fontConfig.generic[i].alias[j].name + " " + fontConfig.generic[i].alias[j].weight);
24. }
25. for (let j = 0; j < fontConfig.generic[i].adjust.length; j++) {
26. console.info(fontConfig.generic[i].adjust[j].weight + " " + fontConfig.generic[i].adjust[j].to);
27. }
28. }
29. console.info("fallback------------" + String(fontConfig.fallbackGroups.length));
30. for (let i = 0; i < fontConfig.fallbackGroups.length; i++) {
31. console.info("fontSetName:" + fontConfig.fallbackGroups[i].fontSetName);
32. for (let j = 0; j < fontConfig.fallbackGroups[i].fallback.length; j++) {
33. console.info("language:" + fontConfig.fallbackGroups[i].fallback[j].language + " family:" +
34. fontConfig.fallbackGroups[i].fallback[j].family);
35. }
36. }
37. })
38. }.width('100%')
39. }
40. }
```
