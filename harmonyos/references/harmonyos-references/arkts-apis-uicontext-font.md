---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-font
title: Class (Font)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (Font)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3e38a98879afb5b061f2248b96b355de7829eb3003e5b5d9c865791733549fb1
---

注册自定义字体的信息。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 10开始支持。
* 以下API需先使用UIContext中的[getFont()](arkts-apis-uicontext-uicontext.md#getfont)方法获取到Font对象，再通过该对象调用对应方法。
* 推荐使用字体引擎的[loadFontSync](js-apis-graphics-text.md#loadfontsync)接口注册自定义字体。

## registerFont

PhonePC/2in1TabletTVWearable

registerFont(options: font.FontOptions): void

在字体管理中注册自定义字体。

该接口为异步接口，不支持并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [font.FontOptions](js-apis-font.md#fontoptions) | 是 | 注册的自定义字体信息。  **说明：**  设置注册字体文件的路径，读取系统沙箱路径内的资源时，建议使用file://路径前缀的字符串，需要确保沙箱目录路径下的文件存在并且有可读权限。 |

**示例：**

```
1. // xxx.ets
2. import { Font } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'Hello World';
8. private uiContext: UIContext = this.getUIContext();
9. private font: Font = this.uiContext.getFont();

11. aboutToAppear() {
12. this.font.registerFont({
13. familyName: 'medium',
14. familySrc: '/font/medium.ttf' // font文件夹与pages目录同级
15. })
16. }

18. build() {
19. Column() {
20. Text(this.message)
21. .align(Alignment.Center)
22. .fontSize(20)
23. .fontFamily('medium') // medium：注册自定义字体的名字（$r('app.string.mediumFamilyName')、'mediumRawFile'等已注册字体也能正常使用）
24. }.width('100%')
25. }
26. }
```

## getSystemFontList

PhonePC/2in1TabletTVWearable

getSystemFontList(): Array<string>

获取系统支持的字体名称列表。

该接口仅在PC/2in1设备上生效，在其他设备上返回空数组。

推荐使用[getSystemFontFullNamesByType](js-apis-graphics-text.md#textgetsystemfontfullnamesbytype14)接口获取系统最新支持的字体列表数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 系统的字体名列表。 |

**示例：**

```
1. // xxx.ets
2. import { Font } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Index {
7. private uiContext: UIContext = this.getUIContext();
8. private font: Font = this.uiContext.getFont();
9. fontList: Array<string> = new Array<string>();

11. build() {
12. Column() {
13. Button("getSystemFontList")
14. .width('60%')
15. .height('6%')
16. .onClick(() => {
17. this.fontList = this.font.getSystemFontList();
18. console.info('getSystemFontList', JSON.stringify(this.fontList))
19. })
20. }.width('100%')
21. }
22. }
```

## getFontByName

PhonePC/2in1TabletTVWearable

getFontByName(fontName: string): font.FontInfo

根据传入的系统字体名称获取系统字体的相关信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fontName | string | 是 | 系统的字体名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [font.FontInfo](js-apis-font.md#fontinfo10) | 字体的详细信息。  如果查询不到字体，返回undefined。 |

**示例：**

```
1. // xxx.ets
2. import { Font, font } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Index {
7. private uiContext: UIContext = this.getUIContext();
8. private font: Font = this.uiContext.getFont();
9. fontInfo: font.FontInfo = this.font.getFontByName('');

11. build() {
12. Column() {
13. Button("getFontByName")
14. .width('60%')
15. .height('6%')
16. .onClick(() => {
17. this.fontInfo = this.font.getFontByName('HarmonyOS Sans Italic');
18. console.info("getFontByName(): path = " + this.fontInfo.path);
19. console.info("getFontByName(): postScriptName = " + this.fontInfo.postScriptName);
20. console.info("getFontByName(): fullName = " + this.fontInfo.fullName);
21. console.info("getFontByName(): family = " + this.fontInfo.family);
22. console.info("getFontByName(): subfamily = " + this.fontInfo.subfamily);
23. console.info("getFontByName(): weight = " + this.fontInfo.weight);
24. console.info("getFontByName(): width = " + this.fontInfo.width);
25. console.info("getFontByName(): italic = " + this.fontInfo.italic);
26. console.info("getFontByName(): monoSpace = " + this.fontInfo.monoSpace);
27. console.info("getFontByName(): symbolic = " + this.fontInfo.symbolic);
28. })
29. }.width('100%')
30. }
31. }
```
