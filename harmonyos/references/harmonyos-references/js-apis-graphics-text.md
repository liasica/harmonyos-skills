---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-graphics-text
title: @ohos.graphics.text (文本模块)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.text (文本模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4d0f419b517ea870522b7fb21484260d4409e5255615cd415b81378f32a6ecb9
---

本模块提供一系列用于文本布局和字体管理的编程接口。文本布局相关的接口旨在提供高质量的排版，包括字符到字形的转换、字距调整、换行、对齐、文本测量等。字体管理接口提供字体注册、字体描述符、字体集管理等功能。

该模块提供以下创建复杂样式的文本段落的常用类：

* [TextStyle](js-apis-graphics-text.md#textstyle)：文本样式，控制文本的字体类型、大小、间距等属性。
* [FontCollection](js-apis-graphics-text.md#fontcollection)：字体集，控制各种不同的字体。
* [FontDescriptor](js-apis-graphics-text.md#fontdescriptor14)：字体描述符信息。
* [ParagraphStyle](js-apis-graphics-text.md#paragraphstyle)：段落样式，控制整个段落的断行策略、断词策略等属性。
* [ParagraphBuilder](js-apis-graphics-text.md#paragraphbuilder)：段落生成器，控制生成不同的段落对象。
* [Paragraph](js-apis-graphics-text.md#paragraph)：段落，由ParagraphBuilder类调用[build()](js-apis-graphics-text.md#build)接口构建而成。
* [LineTypeset](js-apis-graphics-text.md#linetypeset18)：行排版器，由ParagraphBuilder类调用[buildLineTypeset()](js-apis-graphics-text.md#buildlinetypeset18)接口构建而成。
* [TextLine](js-apis-graphics-text.md#textline)：以行为单位的段落文本的载体，由Paragraph类调用[getTextLines()](js-apis-graphics-text.md#gettextlines)接口获取。
* [Run](js-apis-graphics-text.md#run)：文本排版单元，由TextLine类调用[getGlyphRuns()](js-apis-graphics-text.md#getglyphruns)接口获取。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { text } from '@kit.ArkGraphics2D'
```

## text.setTextHighContrast20+

PhonePC/2in1TabletTVWearable

setTextHighContrast(action: TextHighContrast): void

用于设置文字渲染高对比度模式。

该接口设置后整个进程都会生效，进程内所有页面共用相同模式。

可调用此接口设置，也可通过系统设置界面中**高对比度文字配置开关**进行开启/关闭。使用此接口设置开启/关闭文字渲染高对比度配置的优先级高于系统开关设置。

该接口针对应用的文字自绘制场景不生效。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | [TextHighContrast](js-apis-graphics-text.md#texthighcontrast20) | 是 | 文字渲染高对比度模式。 |

**示例：**

```
1. text.setTextHighContrast(text.TextHighContrast.TEXT_APP_DISABLE_HIGH_CONTRAST)
```

## text.setTextUndefinedGlyphDisplay20+

PhonePC/2in1TabletTVWearable

setTextUndefinedGlyphDisplay(noGlyphShow: TextUndefinedGlyphDisplay): void

设置字符映射到.notdef（未定义）字形时要使用的字形类型。

影响此调用后呈现的所有文本。

此配置会影响显示字体中未定义字符的方式：

* 默认行为遵循字体的内部.notdef字形设计。
* 开启后将强制使缺失字形的字符以豆腐块形式显示。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| noGlyphShow | [TextUndefinedGlyphDisplay](js-apis-graphics-text.md#textundefinedglyphdisplay20) | 是 | 无法塑形字符的显示方式。 |

**示例：**

```
1. text.setTextUndefinedGlyphDisplay(text.TextUndefinedGlyphDisplay.USE_TOFU)
```

## text.matchFontDescriptors18+

PhonePC/2in1TabletTVWearable

matchFontDescriptors(desc: FontDescriptor): Promise<Array<FontDescriptor>>

根据指定的字体描述符返回所有符合要求的系统字体描述符，使用Promise异步回调。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| desc | [FontDescriptor](js-apis-graphics-text.md#fontdescriptor14) | 是 | 指定需要用来做匹配的字体描述符。如果不指定任何字段，则返回系统的所有字体描述符。如果填写了指定字段，则按照指定字段进行匹配。如果匹配失败，返回空数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[FontDescriptor](js-apis-graphics-text.md#fontdescriptor14)>> | Promise对象，返回所有匹配到的系统字体描述符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'
2. import { BusinessError } from '@kit.BasicServicesKit'

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. Button("font descriptor")
11. .fontSize(30)
12. .fontWeight(FontWeight.Bold)
13. .width(300)
14. .height(80)
15. .onClick(() => {
16. console.info(`Get font descriptor start`)
17. let promise = text.matchFontDescriptors({
18. weight: text.FontWeight.W400,
19. })
20. promise.then((data) => {
21. console.info(`Font descriptor array size: ${data.length}`);
22. console.info(`Font descriptor result: ${JSON.stringify(data)}`)
23. }).catch((error: BusinessError) => {
24. console.error(`Failed to match the font descriptor, error: ${JSON.stringify(error)}`);
25. });
26. })
27. }
28. .width('100%')
29. }
30. .height('100%')
31. }
32. }
```

## text.getSystemFontFullNamesByType14+

PhonePC/2in1TabletTVWearable

getSystemFontFullNamesByType(fontType: SystemFontType): Promise<Array<string>>

根据字体类型返回该类型对应的所有字体的字体名称，使用Promise异步回调。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fontType | [SystemFontType](js-apis-graphics-text.md#systemfonttype14) | 是 | 指定的字体类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回相应字体类型的所有字体的fullName。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'
2. import { BusinessError } from '@kit.BasicServicesKit'

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. Button("get font list")
11. .fontSize(30)
12. .fontWeight(FontWeight.Bold)
13. .width(300)
14. .height(80)
15. .onClick(() => {
16. let fontType:text.SystemFontType = text.SystemFontType.GENERIC
17. let promise = text.getSystemFontFullNamesByType(fontType)
18. promise.then((data) => {
19. console.info(`then font list size: ${data.length}`)
20. data.forEach((fontItem) => {
21. console.info(fontItem)
22. })
23. }).catch((error: BusinessError) => {
24. console.error(`Failed to get font fullNames by type, error: ${JSON.stringify(error)}`);
25. });
26. })
27. }
28. .width('100%')
29. }
30. .height('100%')
31. }
32. }
```

## text.getFontDescriptorByFullName14+

PhonePC/2in1TabletTVWearable

getFontDescriptorByFullName(fullName: string, fontType: SystemFontType): Promise<FontDescriptor>

根据字体名称和类型获取字体描述符，使用Promise异步回调。

字体描述符是描述字体特征的数据结构，包含字体外观和属性的详细信息。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fullName | string | 是 | 指定的字体名称。可以使用[getSystemFontFullNamesByType](js-apis-graphics-text.md#textgetsystemfontfullnamesbytype14)获取。 |
| fontType | [SystemFontType](js-apis-graphics-text.md#systemfonttype14) | 是 | 指定的字体类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FontDescriptor](js-apis-graphics-text.md#fontdescriptor14)> | Promise对象，返回指定的字体描述符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'
2. import { BusinessError } from '@kit.BasicServicesKit'

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. Button("get fontDescriptor")
11. .fontSize(30)
12. .fontWeight(FontWeight.Bold)
13. .width(300)
14. .height(80)
15. .onClick(() => {
16. let fontType:text.SystemFontType = text.SystemFontType.GENERIC
17. let promise = text.getFontDescriptorByFullName("HarmonyOS Sans", fontType)
18. promise.then((fontDescriptor) => {
19. console.info(`desc: ${JSON.stringify(fontDescriptor)}`)
20. }).catch((error: BusinessError) => {
21. console.error(`Failed to get fontDescriptor by fullName, error: ${JSON.stringify(error)}`);
22. });
23. })
24. }
25. .width('100%')
26. }
27. .height('100%')
28. }
29. }
```

## text.getFontDescriptorsFromPath22+

PhonePC/2in1TabletTVWearable

getFontDescriptorsFromPath(path: string | Resource): Promise<Array<FontDescriptor>>

根据字体文件路径获取字体描述符数组。使用Promise异步回调。

说明

* 如果字体文件未找到、字体文件路径无效、字体文件无权限或者文件非字体格式，返回空数组。
* [FontDescriptor](js-apis-graphics-text.md#fontdescriptor14)中的weight字段并不精准对应字体文件内部的字重数值，而是将字体文件中的实际字重四舍五入映射到[FontWeight](js-apis-graphics-text.md#fontweight)枚举值后的结果。例如，字体文件字重350会映射为400，对应枚举为W400。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | [Resource](ts-types.md#resource) | 是 | 需要查询的字体文件的路径，应为 "file:// + 字体文件绝对路径" 或 $rawfile("工程中resources/rawfile目录下的文件名称")。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[FontDescriptor](js-apis-graphics-text.md#fontdescriptor14)>> | Promise对象，返回所有的字体描述符。如果找不到字体文件、路径无效、无权限或非字体文件，则返回空数组。 |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'

3. @Entry
4. @Component
5. struct GetFontDescriptorsFromPathTest {
6. build() {
7. Column({ space: 10 }) {
8. Button("get fontDescriptors")
9. .onClick(async () => {
10. let promise = text.getFontDescriptorsFromPath("file:///system/fonts/NotoSansCJK-Regular.ttc")
11. promise.then((fontFullDescriptors) => {
12. for (let index = 0; index < fontFullDescriptors.length; index++) {
13. console.info("Path:" + fontFullDescriptors[index].path +
14. "\npostScriptName:" + fontFullDescriptors[index].postScriptName +
15. "\nfullName:" + fontFullDescriptors[index].fullName +
16. "\nfamilyName:" + fontFullDescriptors[index].fontFamily +
17. "\nfontSubName:" + fontFullDescriptors[index].fontSubfamily +
18. "\nweight:" + fontFullDescriptors[index].weight +
19. "\nwidth:" + fontFullDescriptors[index].width +
20. "\nitalic:" + fontFullDescriptors[index].italic +
21. "\nmonoSpace:" + fontFullDescriptors[index].monoSpace +
22. "\nsymbolic:" + fontFullDescriptors[index].symbolic)
23. }
24. })
25. })
26. }.width("100%")
27. .height("100%")
28. .justifyContent(FlexAlign.Center)
29. }
30. }
```

## text.getFontUnicodeSet23+

PhonePC/2in1TabletTVWearable

getFontUnicodeSet(path: string | Resource, index: number): Promise<Array<number>>

根据字体文件路径获取字体unicode数组。使用Promise异步回调。

如果字体文件未找到、字体文件路径无效、字体文件无权限或者文件非字体格式，返回空数组。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | [Resource](ts-types.md#resource) | 是 | 需要查询的字体文件的路径，应为 "file:// + 字体文件绝对路径" 或 $rawfile("工程中resources/rawfile目录下的文件名称")。 |
| index | number | 是 | 字体文件格式为ttc/otc时，指定加载的字体索引。非ttc/otc格式文件索引值只能指定为0。如果该参数非法，将返回空数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，返回字体文件持有的unicode码。 |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'

3. @Entry
4. @Component
5. struct GetFontUnicodeSetTest {
6. build() {
7. Column({ space: 10 }) {
8. Button("get fontUnicode")
9. .onClick(async () => {
10. let promise = text.getFontUnicodeSet("file:///system/fonts/HMSymbolVF.ttf", 0)
11. promise.then((unicodeSet) => {
12. for (let index = 0; index < unicodeSet.length; index++) {
13. console.info(unicodeSet[index].toString())
14. }
15. })
16. })
17. }.width("100%")
18. .height("100%")
19. .justifyContent(FlexAlign.Center)
20. }
21. }
```

## text.getFontCount23+

PhonePC/2in1TabletTVWearable

getFontCount(path: string | Resource): number

根据字体文件路径获取包含的字体文件数。

如果字体文件未找到、字体文件路径无效、字体文件无权限或者文件非字体格式，返回0。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | [Resource](ts-types.md#resource) | 是 | 需要查询的字体文件的路径，应为 "file:// + 字体文件绝对路径" 或 $rawfile("工程中resources/rawfile目录下的文件名称")。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 包含字体数量。 |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'

3. @Entry
4. @Component
5. struct GetFontCountTest {
6. build() {
7. Column({ space: 10 }) {
8. Button("get fontCount")
9. .onClick(() => {
10. let fontCount = text.getFontCount("file:///system/fonts/NotoSansCJK-Regular.ttc")
11. console.info("file count: " + fontCount)
12. })
13. }.width("100%")
14. .height("100%")
15. .justifyContent(FlexAlign.Center)
16. }
17. }
```

## text.getFontPathsByType23+

PhonePC/2in1TabletTVWearable

getFontPathsByType(fontType: SystemFontType): Array<string>

获取指定字体类型的所有字体文件路径。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fontType | [SystemFontType](js-apis-graphics-text.md#systemfonttype14) | 是 | 指定的字体类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 字体文件路径列表。 |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'

3. @Entry
4. @Component
5. struct GetFontPathsByTypeTest {
6. build() {
7. Column({ space: 10 }) {
8. Button("get font path")
9. .onClick(() => {
10. let fontList = text.getFontPathsByType(text.SystemFontType.ALL)
11. console.info("file count: " + fontList.length)
12. for (let index = 0; index < fontList.length; index++) {
13. console.info("file path: " + fontList[index])
14. }
15. })
16. }.width("100%")
17. .height("100%")
18. .justifyContent(FlexAlign.Center)
19. }
20. }
```

## text.isFontSupported23+

PhonePC/2in1TabletTVWearable

isFontSupported(fontURL: string | Resource): boolean

检查系统是否支持指定的字体文件。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fontURL | string | [Resource](ts-types.md#resource) | 是 | 需要检查的字体文件的路径，应为 "file:// + 字体文件绝对路径" 或 "rawfile/目录or文件名"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 系统是否支持指定的字体文件。返回true表示支持，返回false表示不支持。 |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'

3. @Entry
4. @Component
5. struct isFontSupportedTest {
6. build() {
7. Column({ space: 10 }) {
8. Button("is font supported")
9. .onClick(() => {
10. let filePath = "file:///system/fonts/NotoSansCJK-Regular.ttc"
11. let isSupported = text.isFontSupported(filePath)
12. console.info("is font supported: " + isSupported)
13. })
14. }.width("100%")
15. .height("100%")
16. .justifyContent(FlexAlign.Center)
17. }
18. }
```

## TextHighContrast20+

PhonePC/2in1TabletTVWearable

文字渲染高对比度配置类型枚举。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TEXT\_FOLLOW\_SYSTEM\_HIGH\_CONTRAST | 0 | 跟随系统设置中的高对比度文字配置。 |
| TEXT\_APP\_DISABLE\_HIGH\_CONTRAST | 1 | 关闭APP的文字渲染高对比度配置，该模式的优先级要高于系统设置中的高对比度文字配置。 |
| TEXT\_APP\_ENABLE\_HIGH\_CONTRAST | 2 | 开启APP的文字渲染高对比度配置，该模式的优先级要高于系统设置中的高对比度文字配置。 |

## TextUndefinedGlyphDisplay20+

PhonePC/2in1TabletTVWearable

文本未定义字形时的显示方式枚举。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USE\_DEFAULT | 0 | 使用字体的内部.notdef字形。遵循字体的内部.notdef字形设计，可以是空框、空格或自定义符号。 |
| USE\_TOFU | 1 | 总是用显式的豆腐块替换未定义的字形，覆盖字体的默认行为。用于调试缺失字符或强制一致的缺失符号显示。 |

## TextAlign

PhonePC/2in1TabletTVWearable

文本对齐方式枚举。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEFT | 0 | 文本靠左对齐。 |
| RIGHT | 1 | 文本靠右对齐。 |
| CENTER | 2 | 文本居中对齐。 |
| JUSTIFY | 3 | 文本两侧对齐，对最后一行无效。 |
| START | 4 | 基于文本的方向[TextDirection](js-apis-graphics-text.md#textdirection)，文本靠开头方向对齐。 |
| END | 5 | 基于文本的方向[TextDirection](js-apis-graphics-text.md#textdirection)，文本以结束方向对齐。 |

## TextVerticalAlign20+

PhonePC/2in1TabletTVWearable

文本垂直对齐方式枚举。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BASELINE | 0 | 文本基线对齐。 |
| BOTTOM | 1 | 文本底部对齐。 |
| CENTER | 2 | 文本居中对齐。 |
| TOP | 3 | 文本顶部对齐。 |

## TextDirection

PhonePC/2in1TabletTVWearable

文本排版方向枚举。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RTL | 0 | 文本从右到左排版。 |
| LTR | 1 | 文本从左到右排版。 |

## BreakStrategy

PhonePC/2in1TabletTVWearable

断行策略枚举。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GREEDY | 0 | 尽可能将当前行填满，不会自动添加连词符。 |
| HIGH\_QUALITY | 1 | 布局优化，必要时会自动添加连词符。 |
| BALANCED | 2 | 保证一个段落的每一行的宽度相同，必要时会添加连词符。 |

## WordBreak

PhonePC/2in1TabletTVWearable

断词策略枚举。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 默认的换行规则。依据各自语言的规则，允许在字间发生换行。 |
| BREAK\_ALL | 1 | 对于Non-CJK（非中文，日文，韩文）文本允许在任意字符内发生换行。该值适合包含一些非亚洲文本的亚洲文本，比如使连续的英文字符断行。 |
| BREAK\_WORD | 2 | 对于Non-CJK的文本可在任意2个字符间断行，一行文本中有断行破发点（如空白符）时，优先按破发点换行，保障单词优先完整显示。若整一行文本均无断行破发点时，则在任意2个字符间断行。对于CJK与NORMAL效果一致。 |
| BREAK\_HYPHEN18+ | 3 | 每行末尾单词尝试通过连字符“-”进行断行，若无法添加连字符“-”，则跟BREAK\_WORD保持一致。  使用此断词策略时，需与[TextStyle](js-apis-graphics-text.md#textstyle)中locale属性配合使用，通过locale定义语言环境共同作用影响断词效果。 |

## Decoration

PhonePC/2in1TabletTVWearable

文本装饰线。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| textDecoration | [TextDecorationType](js-apis-graphics-text.md#textdecorationtype) | 否 | 是 | 装饰线类型，默认为NONE。 |
| color | [common2D.Color](js-apis-graphics-common2d.md#color) | 否 | 是 | 装饰线颜色，默认为跟随文本颜色。 |
| decorationStyle | [TextDecorationStyle](js-apis-graphics-text.md#textdecorationstyle) | 否 | 是 | 装饰线样式，默认为SOLID。 |
| decorationThicknessScale | number | 否 | 是 | 装饰线粗细系数，浮点数，默认为1.0。如果设置的值小于等于0，则不会绘制装饰线。 |

## TextDecorationType

PhonePC/2in1TabletTVWearable

装饰线类型枚举。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 无装饰线。 |
| UNDERLINE | 1 | 下划线。 |
| OVERLINE | 2 | 上划线。 |
| LINE\_THROUGH | 4 | 删除线。 |

## TextDecorationStyle

PhonePC/2in1TabletTVWearable

装饰线样式枚举。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SOLID | 0 | 实线。 |
| DOUBLE | 1 | 双层线。 |
| DOTTED | 2 | 点状线。 |
| DASHED | 3 | 虚线。 |
| WAVY | 4 | 波浪线。 |

## FontWeight

PhonePC/2in1TabletTVWearable

字重枚举。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| W100 | 0 | 100字重。 |
| W200 | 1 | 200字重。 |
| W300 | 2 | 300字重。 |
| W400 | 3 | 400字重。 |
| W500 | 4 | 500字重。 |
| W600 | 5 | 600字重。 |
| W700 | 6 | 700字重。 |
| W800 | 7 | 800字重。 |
| W900 | 8 | 900字重。 |

## FontWidth

PhonePC/2in1TabletTVWearable

字体宽度的枚举。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ULTRA\_CONDENSED | 1 | 超窄字宽。 |
| EXTRA\_CONDENSED | 2 | 特窄字宽。 |
| CONDENSED | 3 | 窄的字宽。 |
| SEMI\_CONDENSED | 4 | 半窄字宽。 |
| NORMAL | 5 | 常规字宽。 |
| SEMI\_EXPANDED | 6 | 半宽字宽。 |
| EXPANDED | 7 | 宽的字宽。 |
| EXTRA\_EXPANDED | 8 | 特宽字宽。 |
| ULTRA\_EXPANDED | 9 | 超宽的字宽。 |

## FontStyle

PhonePC/2in1TabletTVWearable

字体样式枚举。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 常规样式。 |
| ITALIC | 1 | 斜体。如果当前字体没有可用的斜体版本，会选用倾斜体替代。 |
| OBLIQUE | 2 | 倾斜体。如果当前字体没有可用的倾斜体版本，会选用斜体替代。 |

## TextHeightBehavior

PhonePC/2in1TabletTVWearable

文本高度修饰符模式枚举。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALL | 0x0 | 高度修饰符设置为段落中第一行上升、最后一行下降。 |
| DISABLE\_FIRST\_ASCENT | 0x1 | 高度修饰符设置为禁止段落中第一行上升。 |
| DISABLE\_LAST\_ASCENT | 0x2 | 高度修饰符设置为禁止段落中最后一行下降。 |
| DISABLE\_ALL | 0x1 | 0x2 | 高度修饰符设置为禁止段落中第一行上升、最后一行下降。 |

## TextBaseline

PhonePC/2in1TabletTVWearable

文本基线类型枚举。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALPHABETIC | 0 | 用于拉丁字母的文本基线对齐。 |
| IDEOGRAPHIC | 1 | 用于CJK（中文，日文，韩文）的文本基线对齐。 |

## EllipsisMode

PhonePC/2in1TabletTVWearable

省略号类型枚举。

EllipsisMode.START和EllipsisMode.MIDDLE仅在单行超长文本生效。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| START | 0 | 开头省略号，只在[ParagraphStyle](js-apis-graphics-text.md#paragraphstyle)中设置maxLines为1时生效。 |
| MIDDLE | 1 | 中间省略号，只在[ParagraphStyle](js-apis-graphics-text.md#paragraphstyle)中设置maxLines为1时生效。 |
| END | 2 | 末尾省略号。 |

## TextShadow

PhonePC/2in1TabletTVWearable

字体阴影。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [common2D.Color](js-apis-graphics-common2d.md#color) | 否 | 是 | 字体阴影的颜色，默认为黑色Color(255, 0, 0, 0)。 |
| point | [common2D.Point](js-apis-graphics-common2d.md#point12) | 否 | 是 | 字体阴影基于当前文本的偏移位置，横、纵坐标要大于等于零。 |
| blurRadius | number | 否 | 是 | 模糊半径，浮点数，默认为0.0px。 |

## RectStyle

PhonePC/2in1TabletTVWearable

矩形框样式。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [common2D.Color](js-apis-graphics-common2d.md#color) | 否 | 否 | 矩形框的颜色。 |
| leftTopRadius | number | 否 | 否 | 矩形框的左上半径。 |
| rightTopRadius | number | 否 | 否 | 矩形框的右上半径。 |
| rightBottomRadius | number | 否 | 否 | 矩形框的右下半径。 |
| leftBottomRadius | number | 否 | 否 | 矩形框的左下半径。 |

## FontFeature

PhonePC/2in1TabletTVWearable

文本字体特征。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 字体特征键值对中的关键字标识的字符串。 |
| value | number | 否 | 否 | 字体特征键值对的值。 |

## FontVariation

PhonePC/2in1TabletTVWearable

可变字体属性。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| axis | string | 否 | 否 | 可变字体属性键值对中的关键字标识的字符串。 |
| value | number | 否 | 否 | 可变字体属性键值对的值。 |

## TextBadgeType20+

PhonePC/2in1TabletTVWearable

文本上下标枚举。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TEXT\_BADGE\_NONE | 0 | 不使能上下标。 |
| TEXT\_SUPERSCRIPT | 1 | 使能上标。 |
| TEXT\_SUBSCRIPT | 2 | 使能下标。 |

## LineHeightStyle21+

PhonePC/2in1TabletTVWearable

行高缩放基数枚举。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FONT\_SIZE | 0 | 以字号大小作为缩放基数。最终行高为[TextStyle](js-apis-graphics-text.md#textstyle).fontSize \* [TextStyle](js-apis-graphics-text.md#textstyle).heightScale。 |
| FONT\_HEIGHT | 1 | 以字形高度作为缩放基数。最终行高为塑形后字形高度 \* [TextStyle](js-apis-graphics-text.md#textstyle).heightScale。 |

## TextStyle

PhonePC/2in1TabletTVWearable

文本样式。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| decoration | [Decoration](js-apis-graphics-text.md#decoration) | 否 | 是 | 装饰线设置，默认不使用装饰线。 |
| color | [common2D.Color](js-apis-graphics-common2d.md#color) | 否 | 是 | 文字颜色，默认为白色。 |
| fontWeight | [FontWeight](js-apis-graphics-text.md#fontweight) | 否 | 是 | 字重，默认为W400。 目前只有系统默认字体支持字重的调节，其他字体设置字重值小于semi-bold（即W600）时字体粗细无变化，当设置字重值大于等于semi-bold（即W600）时可能会触发伪加粗效果。 |
| fontWidth21+ | [FontWidth](js-apis-graphics-text.md#fontwidth) | 否 | 是 | 字体宽度，默认为NORMAL。 |
| fontStyle | [FontStyle](js-apis-graphics-text.md#fontstyle) | 否 | 是 | 字体样式，默认为常规样式。 |
| baseline | [TextBaseline](js-apis-graphics-text.md#textbaseline) | 否 | 是 | 文本基线类型，默认为ALPHABETIC。 |
| fontFamilies | Array<string> | 否 | 是 | 字体家族名称列表，默认为空，匹配系统字体。 |
| fontSize | number | 否 | 是 | 字体大小，浮点数，默认为14.0，单位为px。 |
| letterSpacing | number | 否 | 是 | 字符间距，正数拉开字符距离，若是负数则拉近字符距离，浮点数，默认为0.0，单位为物理像素px。 |
| wordSpacing | number | 否 | 是 | 单词间距，浮点数，默认为0.0，单位为px。 |
| heightScale | number | 否 | 是 | 行高缩放倍数，浮点数，默认为1.0，heightOnly为true时生效。 |
| heightOnly | boolean | 否 | 是 | true表示根据字体大小和heightScale设置文本框的高度，false表示根据行高和行距，默认为false。 |
| halfLeading | boolean | 否 | 是 | true表示将行间距平分至行的顶部与底部，false则不平分，默认为false。 |
| ellipsis | string | 否 | 是 | 省略号文本，表示省略号生效后使用该字段值替换省略号部分。 |
| ellipsisMode | [EllipsisMode](js-apis-graphics-text.md#ellipsismode) | 否 | 是 | 省略号类型，默认为END，行尾省略号。 |
| locale | string | 否 | 是 | 语言类型，例如'en-Latn'代表英文(拉丁文字)，'zh-Hans'代表简体中文，'zh-Hant'代表繁体中文。支持language-script格式的两段式语言标签，language遵循ISO 639-1规范，script遵循ISO 15924规范。未指定locale或者设置为空字符串或为undefined时，默认locale为'zh-Hans'。 |
| baselineShift | number | 否 | 是 | 文本下划线的偏移距离，浮点数，默认为0.0px。 |
| fontFeatures | Array<[FontFeature](js-apis-graphics-text.md#fontfeature)> | 否 | 是 | 文本字体特征数组。 |
| fontVariations | Array<[FontVariation](js-apis-graphics-text.md#fontvariation)> | 否 | 是 | 可变字体属性数组。 |
| textShadows | Array<[TextShadow](js-apis-graphics-text.md#textshadow)> | 否 | 是 | 文本阴影数组。 |
| backgroundRect | [RectStyle](js-apis-graphics-text.md#rectstyle) | 否 | 是 | 文本矩形框样式。 |
| badgeType20+ | [TextBadgeType](js-apis-graphics-text.md#textbadgetype20) | 否 | 是 | 设置文本排版时是否使能上标或下标。TEXT\_SUPERSCRIPT表示使能上标，TEXT\_SUBSCRIPT表示使能下标，默认值为TEXT\_BADGE\_NONE表示不使能。 |
| lineHeightMaximum21+ | number | 否 | 是 | 行高上限。若同时应用行高缩放，行高上限在[TextStyle](js-apis-graphics-text.md#textstyle).heightScale大于0时生效。取值为正数浮点数，默认值为Number.MAX\_VALUE。 |
| lineHeightMinimum21+ | number | 否 | 是 | 行高下限。若同时应用行高缩放，行高下限在[TextStyle](js-apis-graphics-text.md#textstyle).heightScale大于0时生效。取值范围为非负浮点数，默认值为0。 |
| lineHeightStyle21+ | [LineHeightStyle](js-apis-graphics-text.md#lineheightstyle21) | 否 | 是 | 行高缩放基数样式。默认为FONT\_SIZE。 |

## StrutStyle

PhonePC/2in1TabletTVWearable

支柱样式，用于控制绘制文本的行间距、基线对齐方式以及其他与行高相关的属性，默认不开启。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontFamilies | Array<string> | 否 | 是 | 字体家族名称列表，默认为空，匹配系统字体。 |
| fontStyle | [FontStyle](js-apis-graphics-text.md#fontstyle) | 否 | 是 | 字体样式，默认为常规样式。 |
| fontWidth | [FontWidth](js-apis-graphics-text.md#fontwidth) | 否 | 是 | 字体宽度，默认为NORMAL。 |
| fontWeight | [FontWeight](js-apis-graphics-text.md#fontweight) | 否 | 是 | 字重，默认为W400。系统默认字体支持字重调节，其他字体设置字重值小于W600时无变化，大于等于W600时可能触发伪加粗效果。 |
| fontSize | number | 否 | 是 | 字体大小，浮点数，默认14.0，单位物理像素px。 |
| height | number | 否 | 是 | 行高缩放倍数，浮点数，默认为1.0。 |
| leading | number | 否 | 是 | 以自定义行距应用于支柱的行距，浮点数，默认为-1.0。 |
| forceHeight | boolean | 否 | 是 | 是否所有行都将使用支柱的高度，true表示使用，false表示不使用，默认为false。 |
| enabled | boolean | 否 | 是 | 是否启用支柱样式，true表示使用，false表示不使用，默认为false。 |
| heightOverride | boolean | 否 | 是 | 是否覆盖高度，true表示覆盖，false表示不覆盖，默认为false。 |
| halfLeading | boolean | 否 | 是 | true表示将行间距平分至行的顶部与底部，false则不平分，默认为false。 |

## FontDescriptor14+

PhonePC/2in1TabletTVWearable

字体描述符信息。

**系统能力**：SystemCapability.Graphics.Drawing

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| path | string | 否 | 是 | 字体绝对路径，可取遵循系统限制的任意字符串，默认为空字符串。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| postScriptName | string | 否 | 是 | 字体唯一标识名称，可取任意字符串，默认为空字符串。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| fullName | string | 否 | 是 | 字体名称，可取任意字符串，默认为空字符串。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| fontFamily | string | 否 | 是 | 字体家族，可取任意字符串，默认为空字符串。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| fontSubfamily | string | 否 | 是 | 子字体家族，可取任意字符串，默认为空字符串。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| weight | [FontWeight](js-apis-graphics-text.md#fontweight) | 否 | 是 | 字体字重，默认值为0。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| width | number | 否 | 是 | 字体宽度，取值范围1-9整数，默认值为0。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| italic | number | 否 | 是 | 是否是斜体字体，0表示非斜体，1表示斜体，默认值为0。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| monoSpace | boolean | 否 | 是 | 是否是等宽字体，true表示等宽，false表示非等宽，默认值为false。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| symbolic | boolean | 否 | 是 | 是否支持符号，true表示支持，false表示不支持，默认值为false。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| localPostscriptName23+ | string | 否 | 是 | 根据系统语言配置提取字体唯一标识，字体文件中若无当前语言对应配置则取“en”对应信息。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| localFullName23+ | string | 否 | 是 | 根据系统语言配置提取字体全名，字体文件中若无当前语言对应配置则取“en”对应信息。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| localFamilyName23+ | string | 否 | 是 | 根据系统语言配置提取字体家族名称，字体文件中若无当前语言对应配置则取“en”对应信息。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| localSubFamilyName23+ | string | 否 | 是 | 根据系统语言配置提取子字体家族名称，字体文件中若无当前语言对应配置则取“en”对应信息。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| version23+ | string | 否 | 是 | 字体版本，可取任意字符串，默认为空字符串。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| manufacture23+ | string | 否 | 是 | 字体制造商信息，可取任意字符串，默认为空字符串。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| copyright23+ | string | 否 | 是 | 字体版权信息，可取任意字符串，默认为空字符串。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| trademark23+ | string | 否 | 是 | 字体商标信息，可取任意字符串，默认为空字符串。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| license23+ | string | 否 | 是 | 字体许可证信息，可取任意字符串，默认为空字符串。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| index23+ | number | 否 | 是 | 字体索引，字体文件为ttc类型时有效，ttf类型统一为0。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |

## FontCollection

PhonePC/2in1TabletTVWearable

字体集。

### getGlobalInstance

PhonePC/2in1TabletTVWearable

static getGlobalInstance(): FontCollection

获取应用全局FontCollection实例。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FontCollection](js-apis-graphics-text.md#fontcollection) | FontCollection对象。 |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'

3. function textFunc() {
4. let fontCollection = text.FontCollection.getGlobalInstance();
5. }

7. @Entry
8. @Component
9. struct Index {
10. fun: Function = textFunc;
11. build() {
12. Column() {
13. Button().onClick(() => {
14. this.fun();
15. })
16. }
17. }
18. }
```

### getLocalInstance22+

PhonePC/2in1TabletTVWearable

static getLocalInstance(): FontCollection

获取本地FontCollection实例，推荐卡片场景使用。

**卡片能力：** 从API version 22开始，该接口支持在ArkTS卡片中使用。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FontCollection](js-apis-graphics-text.md#fontcollection) | FontCollection对象。 |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'
2. let fontCollection = text.FontCollection.getLocalInstance();
```

### loadFontSync

PhonePC/2in1TabletTVWearable

loadFontSync(name: string, path: string | Resource): void

同步接口，加载自定义字体。其中参数name对应的值需要在[TextStyle](js-apis-graphics-text.md#textstyle)中的fontFamilies属性配置，才能显示自定义字体效果。支持的字体文件格式包含：ttf、otf。

**卡片能力：** 从API version 22开始，该接口支持在ArkTS卡片中使用。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 加载字体后，调用该字体所使用的名称。 |
| path | string | [Resource](ts-types.md#resource) | 是 | 需要导入的字体文件的路径，应为 "file:// + 字体文件绝对路径" 或 "rawfile/目录or文件名"。 |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'

3. let fontCollection: text.FontCollection = new text.FontCollection();

5. @Entry
6. @Component
7. struct RenderTest {
8. LoadFontSyncTest() {
9. fontCollection.loadFontSync('Clock_01', 'file:///system/fonts/HarmonyClock_01.ttf')
10. let fontFamilies: Array<string> = ["Clock_01"]
11. let myTextStyle: text.TextStyle = {
12. fontFamilies: fontFamilies
13. };
14. let myParagraphStyle: text.ParagraphStyle = {
15. textStyle: myTextStyle,
16. }
17. let paragraphBuilder: text.ParagraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

19. let textData = "测试 loadFontSync 加载字体HarmonyClock_01.ttf";
20. paragraphBuilder.addText(textData);
21. let paragraph: text.Paragraph = paragraphBuilder.build();
22. paragraph.layoutSync(600);
23. }

25. aboutToAppear() {
26. this.LoadFontSyncTest();
27. }

29. build() {
30. }
31. }
```

### loadFont18+

PhonePC/2in1TabletTVWearable

loadFont(name: string, path: string | Resource): Promise<void>

加载自定义字体。使用Promise异步回调。其中参数name对应的值需要在[TextStyle](js-apis-graphics-text.md#textstyle)中的fontFamilies属性配置，才能显示自定义字体效果，支持的字体文件格式包含：ttf、otf。

**卡片能力：** 从API version 22开始，该接口支持在ArkTS卡片中使用。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 加载字体后，调用该字体所使用的别名，可填写任意字符串，可使用该别名指定并使用该字体。 |
| path | string | [Resource](ts-types.md#resource) | 是 | 需要加载的字体文件的路径，支持两种格式： "file:// + 字体文件绝对路径" 或 "rawfile/目录or文件名"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'

3. let fontCollection: text.FontCollection = new text.FontCollection();

5. @Entry
6. @Component
7. struct RenderTest {
8. async loadFontPromise() {
9. fontCollection.loadFont('testName', 'file:///system/fonts/a.ttf').then((data) => {
10. console.info(`Succeeded in doing loadFont ${JSON.stringify(data)} `);
11. }).catch((error: Error) => {
12. console.error(`Failed to do loadFont, error: ${JSON.stringify(error)} message: ${error.message}`);
13. });
14. }

16. aboutToAppear() {
17. this.loadFontPromise();
18. }

20. build() {
21. }
22. }
```

### loadFontSyncWithCheck23+

PhonePC/2in1TabletTVWearable

loadFontSyncWithCheck(name: string, path: string | Resource, index?: number): void

同步接口，加载自定义字体。其中参数name对应的值需要在[TextStyle](js-apis-graphics-text.md#textstyle)中的fontFamilies属性配置，才能显示自定义字体效果。支持的字体文件格式包含：ttf、otf、ttc。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 加载字体成功后，该字体对应的名称，可填写任意字符串，可使用该名称指定并使用该字体。 |
| path | string | [Resource](ts-types.md#resource) | 是 | 需要加载的字体文件的路径，支持两种格式： "file:// + 字体文件绝对路径" 或 $rawfile("字体文件路径")。 |
| index | number | 否 | 字体文件格式为ttc时，指定加载的字体索引。默认为0：表示加载ttc的第一个字体。  非ttc格式文件索引值无意义，若指定索引，只能为0。 |

**错误码：**

以下错误码的详细介绍请参见[图形绘制与显示错误码](errorcode-drawing.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 25900001 | Parameter error. |
| 25900002 | File not found. |
| 25900003 | Failed to open the file. |
| 25900004 | File seek failed. |
| 25900005 | Failed to get the file size. |
| 25900006 | Failed to read the file. |
| 25900007 | Empty file. |
| 25900008 | Corrupt file. |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'

3. let fc: text.FontCollection = text.FontCollection.getGlobalInstance();

5. @Entry
6. @Component
7. struct Index {
8. message: string = 'Hello World';
9. fontFamily: string = 'family';

11. build() {
12. RelativeContainer() {
13. Text(this.message)
14. .fontFamily(this.fontFamily)
15. .fontSize(50)
16. .fontWeight(FontWeight.Bold)
17. .alignRules({
18. center: { anchor: '__container__', align: VerticalAlign.Center },
19. middle: { anchor: '__container__', align: HorizontalAlign.Center }
20. })
21. .onClick(() => {
22. fc.loadFontSyncWithCheck(this.fontFamily, 'file:///system/fonts/NotoSansCJK-Regular.ttc', 1);
23. try {
24. fc.loadFontSyncWithCheck(this.fontFamily, '/system/fonts/NotoSansCJK-Regular.ttc', 1);
25. } catch (e) {
26. console.error(`Failed to do loadFontWithCheck, error: ${JSON.stringify(e)} message: ${e.message}`);
27. }
28. })
29. }
30. .height('100%')
31. .width('100%')
32. }
33. }
```

### loadFontWithCheck23+

PhonePC/2in1TabletTVWearable

loadFontWithCheck(name: string, path: string | Resource, index?: number): Promise<void>

加载自定义字体，使用Promise异步回调。其中参数name对应的值需要在[TextStyle](js-apis-graphics-text.md#textstyle)中的fontFamilies属性配置，才能显示自定义字体效果，支持的字体文件格式包含：ttf、otf、ttc。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 加载字体成功后，该字体对应的名称，可填写任意字符串，可使用该名称指定并使用该字体。 |
| path | string | [Resource](ts-types.md#resource) | 是 | 需要加载的字体文件的路径，支持两种格式： "file:// + 字体文件绝对路径" 或 $rawfile("字体文件路径")。 |
| index | number | 否 | 字体文件格式为ttc时，指定加载的字体索引。默认为0：表示加载ttc的第一个字体。  非ttc格式文件索引值无意义，若指定索引，只能为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[图形绘制与显示错误码](errorcode-drawing.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 25900001 | Parameter error. |
| 25900002 | File not found. |
| 25900003 | Failed to open the file. |
| 25900004 | File seek failed. |
| 25900005 | Failed to get the file size. |
| 25900006 | Failed to read the file. |
| 25900007 | Empty file. |
| 25900008 | Corrupt file. |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'

3. let fc: text.FontCollection = text.FontCollection.getGlobalInstance();

5. @Entry
6. @Component
7. struct Index {
8. message: string = 'Hello World';
9. fontFamily: string = 'family';

11. build() {
12. RelativeContainer() {
13. Text(this.message)
14. .fontFamily(this.fontFamily)
15. .fontSize(50)
16. .fontWeight(FontWeight.Bold)
17. .alignRules({
18. center: { anchor: '__container__', align: VerticalAlign.Center },
19. middle: { anchor: '__container__', align: HorizontalAlign.Center }
20. })
21. .onClick(() => {
22. fc.loadFontWithCheck(this.fontFamily, 'file:///system/fonts/NotoSansCJK-Regular.ttc', 1).then((data) => {
23. console.info(`Succeeded in doing loadFontWithCheck ${JSON.stringify(data)} `);
24. }).catch((error: Error) => {
25. console.error(`Failed to do loadFontWithCheck, error: ${JSON.stringify(error)} message: ${error.message}`);
26. });
27. fc.loadFontWithCheck(this.fontFamily, '/system/fonts/NotoSansCJK-Regular.ttc', 1).then((data) => {
28. console.info(`Succeeded in doing loadFontWithCheck ${JSON.stringify(data)} `);
29. }).catch((error: Error) => {
30. console.error(`Failed to do loadFontWithCheck, error: ${JSON.stringify(error)} message: ${error.message}`);
31. });
32. })
33. }
34. .height('100%')
35. .width('100%')
36. }
37. }
```

### unloadFontSync20+

PhonePC/2in1TabletTVWearable

unloadFontSync(name: string): void

卸载指定的自定义字体，此接口为同步接口。

使用此接口卸载字体别名所对应的自定义字体后，对应的自定义字体将不再可用。

所有使用该字体别名的排版对象都应该被销毁重建。

* 卸载不存在的字体别名不会产生任何效果且不会抛出错误。
* 此操作仅影响后续字体使用。
* 卸载正在使用的字体可能导致文本渲染异常（如乱码或字形缺失）。

**卡片能力：** 从API version 22开始，该接口支持在ArkTS卡片中使用。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 需要取消注册的字体别名，与加载字体时使用的别名相同。 |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'

3. @Entry
4. @Component
5. struct UnloadFontSyncTest {
6. private fc: text.FontCollection = text.FontCollection.getGlobalInstance();
7. @State content: string = "默认字体"

9. build() {
10. Column({ space: 10 }) {
11. Text(this.content)
12. .fontFamily("custom")
13. Button("load font")
14. .onClick(() => {
15. this.fc.loadFontSync("custom", "file:///system/fonts/NotoSansCJK-Regular.ttc")
16. this.content = "自定义字体"
17. })
18. Button("unload font")
19. .onClick(() => {
20. this.fc.unloadFontSync("custom")
21. this.content = "默认字体"
22. })
23. }.width("100%")
24. .height("100%")
25. .justifyContent(FlexAlign.Center)
26. }
27. }
```

### unloadFont20+

PhonePC/2in1TabletTVWearable

unloadFont(name: string): Promise<void>

卸载指定的自定义字体。使用Promise异步回调。

使用此接口卸载字体别名所对应的自定义字体后，对应的自定义字体将不再可用。

所有使用该字体别名的排版对象都应该被销毁重建。

* 卸载不存在的字体别名不会产生任何效果且不会抛出错误。
* 此操作仅影响后续字体使用。
* 卸载正在使用的字体可能导致文本渲染异常（如乱码或字形缺失）。

**卡片能力：** 从API version 22开始，该接口支持在ArkTS卡片中使用。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 需要卸载的字体的别名，与加载字体时使用的别名相同。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'

3. @Entry
4. @Component
5. struct UnloadFontTest {
6. private fc: text.FontCollection = text.FontCollection.getGlobalInstance();
7. @State content: string = "默认字体"

9. build() {
10. Column({ space: 10 }) {
11. Text(this.content)
12. .fontFamily("custom")
13. Button("load font")
14. .onClick(async () => {
15. await this.fc.loadFont("custom", "file:///system/fonts/NotoSansCJK-Regular.ttc")
16. this.content = "自定义字体"
17. })
18. Button("unload font")
19. .onClick(async () => {
20. await this.fc.unloadFont("custom")
21. this.content = "默认字体"
22. })
23. }.width("100%")
24. .height("100%")
25. .justifyContent(FlexAlign.Center)
26. }
27. }
```

### clearCaches

PhonePC/2in1TabletTVWearable

clearCaches(): void

清理字体排版缓存（字体排版缓存本身设有内存上限和清理机制，所占内存有限，如无内存要求，不建议清理）。

**卡片能力：** 从API version 22开始，该接口支持在ArkTS卡片中使用。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Column() {
8. Button().onClick(() => {
9. text.FontCollection.getGlobalInstance().clearCaches();
10. })
11. }
12. }
13. }
```

## ParagraphStyle

PhonePC/2in1TabletTVWearable

段落样式。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| textStyle | [TextStyle](js-apis-graphics-text.md#textstyle) | 否 | 是 | 作用于整个段落的文本样式，默认为初始的文本样式。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| textDirection | [TextDirection](js-apis-graphics-text.md#textdirection) | 否 | 是 | 文本方向，默认为LTR。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| align | [TextAlign](js-apis-graphics-text.md#textalign) | 否 | 是 | 文本对齐方式，默认为START。若同时配置tab属性，制表符对齐方式将失效。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| wordBreak | [WordBreak](js-apis-graphics-text.md#wordbreak) | 否 | 是 | 断词类型，默认为BREAK\_WORD。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| maxLines | number | 否 | 是 | 最大行数限制，整数，默认为1e9。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| breakStrategy | [BreakStrategy](js-apis-graphics-text.md#breakstrategy) | 否 | 是 | 断行策略，默认为GREEDY。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| strutStyle | [StrutStyle](js-apis-graphics-text.md#strutstyle) | 否 | 是 | 支柱样式，默认为初始的StrutStyle。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| textHeightBehavior | [TextHeightBehavior](js-apis-graphics-text.md#textheightbehavior) | 否 | 是 | 文本高度修饰符模式，默认为ALL。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| tab18+ | [TextTab](js-apis-graphics-text.md#texttab18) | 否 | 是 | 表示段落中文本制表符后的文本对齐方式及位置，默认将制表符替换为一个空格。此参数与文本对齐方式（align属性）或省略号样式（[TextStyle](js-apis-graphics-text.md#textstyle)中的ellipsis属性）共同配置时无效。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| trailingSpaceOptimized20+ | boolean | 否 | 是 | 表示文本排版时行尾空格是否参与对齐计算。true表示行尾空格不参与计算，false表示行尾空格参与计算，默认值为false。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| autoSpace20+ | boolean | 否 | 是 | 设置文本排版时是否使能自动间距。true表示使能自动间距，则会在文本排版时自动调整CJK（中文字符、日文字符、韩文字符）与西文（拉丁字母、西里尔字母、希腊字母）、CJK与数字、CJK与版权符号、版权符号与数字、版权符号与西文之间的间距。false表示不使能自动间距，默认值为false。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| verticalAlign20+ | [TextVerticalAlign](js-apis-graphics-text.md#textverticalalign20) | 否 | 是 | 文本垂直对齐方式，开启行高缩放（即设置[TextStyle](js-apis-graphics-text.md#textstyle)的heightScale）或行内不同字号（即设置[TextStyle](js-apis-graphics-text.md#textstyle)的fontSize）文本混排时生效。若行内有上下标文本（即设置[TextStyle](js-apis-graphics-text.md#textstyle)的badgeType属性文本），上下标文本将与普通文本一样参与垂直对齐。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| lineSpacing21+ | number | 否 | 是 | 行间距，默认值为0。lineSpacing不受[TextStyle](js-apis-graphics-text.md#textstyle)中lineHeightMaximum和lineHeightMinimum限制。尾行默认添加行间距，可通过设置[TextStyle](js-apis-graphics-text.md#textstyle).textHeightBehavior为DISABLE\_ALL或DISABLE\_LAST\_ASCENT禁用尾行行间距。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| compressHeadPunctuation23+ | boolean | 否 | 是 | 设置文本排版时是否使能行首标点压缩。true表示使能行首标点压缩，false表示不使能行首标点压缩，默认值为false。  **说明：**  1. 需要字体文件支持[FontFeature](js-apis-graphics-text.md#fontfeature)中的"ss08"特性，否则无法压缩。  2. 在行首标点压缩范围内的标点才在本特性作用范围内。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| includeFontPadding23+ | boolean | 否 | 是 | 设置文本排版时是否使能首尾行padding。true表示使能首尾行padding，false表示不使能首尾行padding，默认值为false。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| fallbackLineSpacing23+ | boolean | 否 | 是 | 设置文本排版时是否使能行高回退，当设置的行高小于实际行高时，将行高回退为实际行高。true表示使能行高回退，false表示不使能行高回退，默认值为false。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

行首压缩的标点范围:

| 标点 | Unicode码位 | Unicode名称 |
| --- | --- | --- |
| 「 | U+300C | LEFT CORNER BRACKET |
| 『 | U+300E | LEFT WHITE CORNER BRACKET |
| " | U+201C | LEFT DOUBLE QUOTATION MARK |
| ' | U+2018 | LEFT SINGLE QUOTATION MARK |
| （ | U+FF08 | FULLWIDTH LEFT PARENTHESIS |
| 《 | U+300A | LEFT DOUBLE ANGLE BRACKET |
| 〈 | U+3008 | LEFT ANGLE BRACKET |
| 【 | U+3010 | LEFT BLACK LENTICULAR BRACKET |
| 〖 | U+3016 | LEFT WHITE LENTICULAR BRACKET |
| 〔 | U+3014 | LEFT TORTOISE SHELL BRACKET |
| ［ | U+FF3B | FULLWIDTH LEFT SQUARE BRACKET |
| ｛ | U+FF5B | FULLWIDTH LEFT CURLY BRACKET |

## PlaceholderAlignment

PhonePC/2in1TabletTVWearable

占位符相对于周围文本的纵向对齐方式。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OFFSET\_AT\_BASELINE | 0 | 基线与文本基线对齐。 |
| ABOVE\_BASELINE | 1 | 底部与文本基线对齐。 |
| BELOW\_BASELINE | 2 | 顶部与文本基线对齐。 |
| TOP\_OF\_ROW\_BOX | 3 | 顶部与文本顶部对齐。 |
| BOTTOM\_OF\_ROW\_BOX | 4 | 底部与文本底部对齐。 |
| CENTER\_OF\_ROW\_BOX | 5 | 居中对齐。 |
| FOLLOW\_PARAGRAPH20+ | 6 | 跟随文本排版对齐。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/zXpags02QfKhAiqHpGz6jg/zh-cn_image_0000002583480893.png?HW-CC-KV=V1&HW-CC-Date=20260428T001443Z&HW-CC-Expire=86400&HW-CC-Sign=6F87C05F2F817F74AD3331BC86BB8D84839151BF65A0FCE16FC1FB1CCCA96320)

说明

示意图展示了后三种对齐方式，前三种对齐方式类似，比较位置是文本基线，即绿色线条部分。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/UDpGmrl5QCODOMNTmPNucQ/zh-cn_image_0000002552801244.png?HW-CC-KV=V1&HW-CC-Date=20260428T001443Z&HW-CC-Expire=86400&HW-CC-Sign=B3D351483A88594F1D1232799D457A572CFB8900D52EA89B75007B0BC200F872)

## PlaceholderSpan

PhonePC/2in1TabletTVWearable

描述占位符样式。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 否 | 否 | 占位符的宽度，浮点数，单位为物理像素px。 |
| height | number | 否 | 否 | 占位符的高度，浮点数，单位为物理像素px。 |
| align | [PlaceholderAlignment](js-apis-graphics-text.md#placeholderalignment) | 否 | 否 | 相对于周围文本的纵向对齐方式。 |
| baseline | [TextBaseline](js-apis-graphics-text.md#textbaseline) | 否 | 否 | 基线类型。 |
| baselineOffset | number | 否 | 否 | 基线偏移量，浮点数，单位为物理像素px。 |

## Range

PhonePC/2in1TabletTVWearable

描述左闭右开区间。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | number | 否 | 否 | 区间左侧端点索引，整数。 |
| end | number | 否 | 否 | 区间右侧端点索引，整数。 |

## Paragraph

PhonePC/2in1TabletTVWearable

保存文本内容及样式的载体，支持排版与绘制操作。

下列API示例中都需先使用[ParagraphBuilder](js-apis-graphics-text.md#paragraphbuilder)类的[build()](js-apis-graphics-text.md#build)接口获取到Paragraph对象实例，再通过此实例调用对应方法。

### layoutSync

PhonePC/2in1TabletTVWearable

layoutSync(width: number): void

进行排版并计算所有字形位置。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 单行的最大宽度，浮点数，单位为物理像素px。 |

**示例：**

```
1. paragraph.layoutSync(100);
```

### layout18+

PhonePC/2in1TabletTVWearable

layout(width: number): Promise<void>

进行排版并计算所有字形位置，使用Promise异步回调。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 单行的最大宽度，浮点数，单位为物理像素px。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例：**

```
1. import { drawing, text } from '@kit.ArkGraphics2D'
2. import { image } from '@kit.ImageKit'

4. let textStyle: text.TextStyle = {
5. color: {
6. alpha: 255,
7. red: 255,
8. green: 0,
9. blue: 0
10. },
11. fontSize: 30,
12. };
13. let paragraphStyle: text.ParagraphStyle = {
14. textStyle: textStyle,
15. };
16. let fontCollection: text.FontCollection = new text.FontCollection();
17. let paragraphBuilder = new text.ParagraphBuilder(paragraphStyle, fontCollection);
18. // 添加文本字符串
19. paragraphBuilder.addText("test");
20. // 生成排版对象
21. let paragraph = paragraphBuilder.build();

23. function textFunc(pixelmap: PixelMap) {
24. // 通过图片对象构造画布
25. let canvas = new drawing.Canvas(pixelmap);
26. // 进行绘制文本字符串
27. paragraph.paint(canvas, 100, 10);
28. }

30. @Entry
31. @Component
32. struct Index {
33. @State pixelmap?: PixelMap = undefined;
34. fun: Function = textFunc;

36. async prepareLayoutPromise() {
37. // 排版对象进行布局计算
38. paragraph.layout(200).then((data) => {
39. console.info(`Succeeded in doing layout,  ${JSON.stringify(data)}`);
40. }).catch((error: Error) => {
41. console.error(`Failed to do layout, error: ${JSON.stringify(error)} message: ${error.message}`);
42. });
43. }

45. aboutToAppear() {
46. this.prepareLayoutPromise();
47. }

49. build() {
50. Column() {
51. Image(this.pixelmap).width(200).height(200);
52. Button("layout")
53. .width(100)
54. .height(50)
55. .onClick(() => {
56. const color: ArrayBuffer = new ArrayBuffer(160000);
57. let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 } }
58. if (this.pixelmap == undefined) {
59. // 构造图片对象
60. this.pixelmap = image.createPixelMapSync(color, opts);
61. }
62. // 进行绘制文字
63. this.fun(this.pixelmap);
64. })
65. }
66. }
67. }
```

说明

示意图展示了点击按钮后layout接口示例代码的运行结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/1QICujteS8O7y2ZXk7_boQ/zh-cn_image_0000002583440939.png?HW-CC-KV=V1&HW-CC-Date=20260428T001443Z&HW-CC-Expire=86400&HW-CC-Sign=CC56576DC4E2E12817E1139DF75F4DF378B0ED91A90BC82FD822DA3CE53A3716)

### paint

PhonePC/2in1TabletTVWearable

paint(canvas: drawing.Canvas, x: number, y: number): void

在画布上以 (x, y) 为左上角绘制文本。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| canvas | [drawing.Canvas](arkts-apis-graphics-drawing-canvas.md) | 是 | 绘制的目标画布。 |
| x | number | 是 | 绘制的左上角位置的横坐标，浮点数。 |
| y | number | 是 | 绘制的左上角位置的纵坐标，浮点数。 |

**示例：**

```
1. const color: ArrayBuffer = new ArrayBuffer(160000);
2. let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 } }
3. let pixelMap: image.PixelMap = image.createPixelMapSync(color, opts);
4. let canvas = new drawing.Canvas(pixelMap);
5. paragraph.paint(canvas, 0, 0);
```

### paintOnPath

PhonePC/2in1TabletTVWearable

paintOnPath(canvas: drawing.Canvas, path: drawing.Path, hOffset: number, vOffset: number): void

在画布上沿路径绘制文本。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| canvas | [drawing.Canvas](arkts-apis-graphics-drawing-canvas.md) | 是 | 绘制的目标画布。 |
| path | [drawing.Path](arkts-apis-graphics-drawing-path.md) | 是 | 确认文字位置的路径。 |
| hOffset | number | 是 | 沿路径方向偏置，从路径起点向前为正，向后为负。 |
| vOffset | number | 是 | 沿路径垂直方向偏置，沿路径方向左侧为负，右侧为正。 |

**示例：**

```
1. const color: ArrayBuffer = new ArrayBuffer(160000);
2. let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 } }
3. let pixelMap: image.PixelMap = image.createPixelMapSync(color, opts);
4. let canvas = new drawing.Canvas(pixelMap);
5. let path = new drawing.Path();
6. path.arcTo(20, 20, 180, 180, 180, 90);
7. paragraph.paintOnPath(canvas, path, 0, 0);
```

### getMaxWidth

PhonePC/2in1TabletTVWearable

getMaxWidth(): number

获取文本最大行宽。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 最大的行宽，浮点数，单位为物理像素px。 |

**示例：**

```
1. let maxWidth = paragraph.getMaxWidth();
```

### getHeight

PhonePC/2in1TabletTVWearable

getHeight(): number

获取文本总高度。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 总高度，浮点数，单位为物理像素px。 |

**示例：**

```
1. let height = paragraph.getHeight();
```

### getLongestLine

PhonePC/2in1TabletTVWearable

getLongestLine(): number

获取文本最长行宽。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 最长一行的宽度，浮点数，单位为物理像素px。 |

**示例：**

```
1. let longestLine = paragraph.getLongestLine();
```

### getLongestLineWithIndent13+

PhonePC/2in1TabletTVWearable

getLongestLineWithIndent(): number

获取文本最长一行的宽度（包含缩进），建议向上取整。文本内容为空时返回0。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 最长一行的宽度（该宽度包含当前行缩进的宽度），浮点数，单位为物理像素px。 |

**示例：**

```
1. let longestLineWithIndent = paragraph.getLongestLineWithIndent();
```

### getMinIntrinsicWidth

PhonePC/2in1TabletTVWearable

getMinIntrinsicWidth(): number

获取段落最小固有宽度。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 该段落所占水平空间的最小固有宽度，浮点数，单位为物理像素px。 |

**示例：**

```
1. let minIntrinsicWidth = paragraph.getMinIntrinsicWidth();
```

### getMaxIntrinsicWidth

PhonePC/2in1TabletTVWearable

getMaxIntrinsicWidth(): number

获取段落最大固有宽度。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 该段落所占水平空间的最大固有宽度，浮点数，单位为物理像素px。 |

**示例：**

```
1. let maxIntrinsicWidth = paragraph.getMaxIntrinsicWidth();
```

### getAlphabeticBaseline

PhonePC/2in1TabletTVWearable

getAlphabeticBaseline(): number

获取拉丁字母基线位置。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 拉丁字母下的基线位置，浮点数，单位为物理像素px。 |

**示例：**

```
1. let alphabeticBaseline = paragraph.getAlphabeticBaseline();
```

### getIdeographicBaseline

PhonePC/2in1TabletTVWearable

getIdeographicBaseline(): number

获取表意字（如CJK（中文，日文，韩文））下的基线位置。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取表意字下的基线位置，浮点数，单位为物理像素px。 |

**示例：**

```
1. let ideographicBaseline = paragraph.getIdeographicBaseline();
```

### getRectsForRange

PhonePC/2in1TabletTVWearable

getRectsForRange(range: Range, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>

获取给定的矩形区域宽度以及矩形区域高度的规格下，文本中该区间范围内的字符所占的矩形区域。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | [Range](js-apis-graphics-text.md#range) | 是 | 需要获取的区域的文本区间。 |
| widthStyle | [RectWidthStyle](js-apis-graphics-text.md#rectwidthstyle) | 是 | 返回的矩形区域的宽度的规格。 |
| heightStyle | [RectHeightStyle](js-apis-graphics-text.md#rectheightstyle) | 是 | 返回的矩形区域的高度的规格。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[TextBox](js-apis-graphics-text.md#textbox)> | 矩形区域数组。 |

**示例：**

```
1. let range: text.Range = { start: 0, end: 1};
2. let rects = paragraph.getRectsForRange(range, text.RectWidthStyle.TIGHT, text.RectHeightStyle.TIGHT);
```

### getRectsForPlaceholders

PhonePC/2in1TabletTVWearable

getRectsForPlaceholders(): Array<TextBox>

获取文本中所有占位符所占的矩形区域。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[TextBox](js-apis-graphics-text.md#textbox)> | 矩形区域数组。 |

**示例：**

```
1. let placeholderRects = paragraph.getRectsForPlaceholders();
```

### getGlyphPositionAtCoordinate

PhonePC/2in1TabletTVWearable

getGlyphPositionAtCoordinate(x: number, y: number): PositionWithAffinity

获取与给定坐标最接近的字形位置信息。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 横坐标，浮点数。 |
| y | number | 是 | 纵坐标，浮点数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PositionWithAffinity](js-apis-graphics-text.md#positionwithaffinity) | 字形位置信息。 |

**示例：**

```
1. let positionWithAffinity = paragraph.getGlyphPositionAtCoordinate(0, 0);
```

### getWordBoundary

PhonePC/2in1TabletTVWearable

getWordBoundary(offset: number): Range

返回给定offset的字形所在单词的索引区间。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 字形的偏移量，整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Range](js-apis-graphics-text.md#range) | 单词的索引区间。 |

**示例：**

```
1. let wordRange = paragraph.getWordBoundary(0);
```

### getLineCount

PhonePC/2in1TabletTVWearable

getLineCount(): number

返回文本行数。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 文本行数量，整数。 |

**示例：**

```
1. let lineCount = paragraph.getLineCount();
```

### getLineHeight

PhonePC/2in1TabletTVWearable

getLineHeight(line: number): number

返回指定行的行高。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| line | number | 是 | 文本行索引，整数，范围为0~getLineCount()-1。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 行高。 |

**示例：**

```
1. let lineHeight = paragraph.getLineHeight(0);
```

### getLineWidth

PhonePC/2in1TabletTVWearable

getLineWidth(line: number): number

返回指定行的行宽。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| line | number | 是 | 文本行索引，整数，范围为0~getLineCount()-1。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 行宽。 |

**示例：**

```
1. let lineWidth = paragraph.getLineWidth(0);
```

### didExceedMaxLines

PhonePC/2in1TabletTVWearable

didExceedMaxLines(): boolean

返回段落是否超过最大行数。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示段落超出了最大行限制，false则表示没有超出最大行限制。 |

**示例：**

```
1. let didExceed = paragraph.didExceedMaxLines();
```

### getTextLines

PhonePC/2in1TabletTVWearable

getTextLines(): Array<TextLine>

返回所有的文本行。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[TextLine](js-apis-graphics-text.md#textline)> | 文本行载体数组。 |

**示例：**

```
1. let lines = paragraph.getTextLines();
```

### getActualTextRange

PhonePC/2in1TabletTVWearable

getActualTextRange(lineNumber: number, includeSpaces: boolean): Range

获取指定行的实际可见文本范围，不包括溢出的省略号。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lineNumber | number | 是 | 要获取文本范围的行索引，行索引从0开始。该接口只能获取已有行的边界，即输入行索引从0开始。最大行索引为文本行数量-1，文本行数量可通过[getLineCount](js-apis-graphics-text.md#getlinecount)接口获取。 |
| includeSpaces | boolean | 是 | 表示是否应包含空白字符。true表示包含空白字符，false表示不包含空白字符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Range](js-apis-graphics-text.md#range) | 返回对应行数的实际文本范围。如果行索引非法，返回的start和end均为0。 |

**示例：**

```
1. let rang = paragraph.getActualTextRange(0, true);
```

### getLineMetrics

PhonePC/2in1TabletTVWearable

getLineMetrics(): Array<LineMetrics>

获取文本行的行度量数组。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[LineMetrics](js-apis-graphics-text.md#linemetrics)> | 文本行的行度量数组。 |

**示例：**

```
1. let arrLineMetric =  paragraph.getLineMetrics();
```

### getLineMetrics

PhonePC/2in1TabletTVWearable

getLineMetrics(lineNumber: number): LineMetrics | undefined

获取特定行号的行度量信息。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lineNumber | number | 是 | 要查询度量信息的行的编号，行号从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LineMetrics](js-apis-graphics-text.md#linemetrics) | undefined | 如果指定的行号有效且度量信息存在，则返回一个包含该行度量数据的LineMetrics对象；如果行号无效或无法获取度量信息，则返回undefined。 |

**示例：**

```
1. let lineMetrics =  paragraph.getLineMetrics(0);
```

### updateColor20+

PhonePC/2in1TabletTVWearable

updateColor(color: common2D.Color): void;

更新整个文本段落的颜色。如果当前装饰线未设置颜色，使用该接口也会同时更新装饰线的颜色。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [common2D.Color](js-apis-graphics-common2d.md#color) | 是 | 更新后的字体色。 |

**示例：**

```
1. paragraph.updateColor({ alpha: 255, red: 255, green: 0, blue: 0 });
```

### updateDecoration20+

PhonePC/2in1TabletTVWearable

updateDecoration(decoration: Decoration): void;

更新整个文本段落的装饰线。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| decoration | [Decoration](js-apis-graphics-text.md#decoration) | 是 | 更新后的装饰线。 |

**示例：**

```
1. paragraph.updateDecoration({
2. textDecoration: text.TextDecorationType.OVERLINE,
3. color: { alpha: 255, red: 255, green: 0, blue: 0 },
4. decorationStyle: text.TextDecorationStyle.WAVY,
5. decorationThicknessScale: 2.0,
6. });
```

## LineTypeset18+

PhonePC/2in1TabletTVWearable

保存着文本内容以及样式的载体，可以用于计算单行排版信息。

下列API示例中都需先使用[ParagraphBuilder](js-apis-graphics-text.md#paragraphbuilder)类的[buildLineTypeset()](js-apis-graphics-text.md#buildlinetypeset18)接口获取到LineTypeset对象实例，再通过此实例调用对应方法。

### getLineBreak18+

PhonePC/2in1TabletTVWearable

getLineBreak(startIndex: number, width: number): number

计算在限定宽度下，从指定位置开始可以排版的字符数。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startIndex | number | 是 | 开始计算排版的起始位置（包括起始位置）。取值范围需要为[0,文本字符总数）的整数，参数非法时抛出异常。 |
| width | number | 是 | 可用于排版的宽度，大于0的浮点数，单位为物理像素px。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回在限定排版宽度下，从指定位置开始可排版的字符总数，取值为整数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3. Parameter verification failed. |

**示例：**

```
1. let startIndex = 0;
2. let width = 100.0;
3. let count = lineTypeset.getLineBreak(startIndex, width);
```

### createLine18+

PhonePC/2in1TabletTVWearable

createLine(startIndex: number, count: number): TextLine

根据指定的排版区间生成文本行对象。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startIndex | number | 是 | 开始计算排版的起始位置，整数，取值范围为[0, 文本字符总数)。 |
| count | number | 是 | 从指定起始位置开始进行排版的字符个数，取值为[0,文本字符总数)的整数，startIndex和count之和不能大于文本字符总数。当count为0时，表示排版区间为[startIndex, 文本结尾]。可以先使用[getLineBreak](js-apis-graphics-text.md#getlinebreak18)获取合理的排版字符总数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextLine](js-apis-graphics-text.md#textline) | 根据文本区间字符生成的TextLine对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3. Parameter verification failed. |

**示例：**

```
1. let startIndex = 0;
2. let width = 100.0;
3. let count = lineTypeset.getLineBreak(startIndex, width);
4. let line : text.TextLine = lineTypeset.createLine(startIndex, count);
```

## RunMetrics

PhonePC/2in1TabletTVWearable

描述文本行中连续文本块的布局信息和度量数据。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| textStyle | [TextStyle](js-apis-graphics-text.md#textstyle) | 否 | 否 | 字体的样式信息。 |
| fontMetrics | [drawing.FontMetrics](arkts-apis-graphics-drawing-i.md#fontmetrics) | 否 | 否 | 字体度量信息。 |

## LineMetrics

PhonePC/2in1TabletTVWearable

描述文本布局中单行文字的度量信息。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| startIndex | number | 否 | 否 | 文本缓冲区中该行开始的索引位置。 |
| endIndex | number | 否 | 否 | 文本缓冲区中该行结束的索引位置。 |
| ascent | number | 否 | 否 | 文字上升高度，即从基线到字符顶部的距离。 |
| descent | number | 否 | 否 | 文字下降高度，即从基线到字符底部的距离。 |
| height | number | 否 | 否 | 当前行的高度，计算方式为 Math.round(ascent + descent) |
| width | number | 否 | 否 | 行的宽度。 |
| left | number | 否 | 否 | 行的左边缘位置。右边缘可通过 left+width 计算得出。 |
| baseline | number | 否 | 否 | 该行基线相对于段落顶部的 Y 坐标位置。 |
| lineNumber | number | 否 | 否 | 行号，从0开始计数。 |
| topHeight | number | 否 | 否 | 从顶部到当前行的高度。 |
| runMetrics | Map<number, [RunMetrics](js-apis-graphics-text.md#runmetrics)> | 否 | 否 | 文本索引范围与关联的字体度量信息之间的映射。 |

## TextBox

PhonePC/2in1TabletTVWearable

文本矩形区域。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rect | [common2D.Rect](js-apis-graphics-common2d.md#rect) | 否 | 否 | 矩形区域信息。 |
| direction | [TextDirection](js-apis-graphics-text.md#textdirection) | 否 | 否 | 文本方向。 |

## PositionWithAffinity

PhonePC/2in1TabletTVWearable

位置和亲和度。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| position | number | 否 | 否 | 字形相对于段落的索引，整数。 |
| affinity | [Affinity](js-apis-graphics-text.md#affinity) | 否 | 否 | 位置亲和度。 |

## RectWidthStyle

PhonePC/2in1TabletTVWearable

矩形区域宽度规格枚举。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TIGHT | 0 | 不设置letterSpacing时，与字形紧贴，否则包含letterSpacing的宽度。 |
| MAX | 1 | 扩展宽度，以匹配所有行上最宽矩形的位置。 |

## RectHeightStyle

PhonePC/2in1TabletTVWearable

矩形区域高度规格枚举。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TIGHT | 0 | 与字形紧贴。 |
| MAX | 1 | 扩展高度，以匹配所有行上最高矩形的位置。 |
| INCLUDE\_LINE\_SPACE\_MIDDLE | 2 | 每个矩形的顶部和底部将覆盖行上方和行下方的一半空间。 |
| INCLUDE\_LINE\_SPACE\_TOP | 3 | 行间距将被添加到矩形的顶部。 |
| INCLUDE\_LINE\_SPACE\_BOTTOM | 4 | 行间距将被添加到矩形的底部。 |
| STRUT | 5 | 高度按照文本的样式设置。 |

## Affinity

PhonePC/2in1TabletTVWearable

位置亲和度枚举。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UPSTREAM | 0 | 该位置与文本位置的前一位有关联。 |
| DOWNSTREAM | 1 | 该位置与文本位置的后一位有关联。 |

## ParagraphBuilder

PhonePC/2in1TabletTVWearable

段落生成器。

### constructor

PhonePC/2in1TabletTVWearable

constructor(paragraphStyle: ParagraphStyle, fontCollection: FontCollection)

ParagraphBuilder对象的构造函数。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| paragraphStyle | [ParagraphStyle](js-apis-graphics-text.md#paragraphstyle) | 是 | 段落样式。 |
| fontCollection | [FontCollection](js-apis-graphics-text.md#fontcollection) | 是 | 字体集。 |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'

3. function textFunc() {
4. let myTextStyle: text.TextStyle = {
5. color: { alpha: 255, red: 255, green: 0, blue: 0 },
6. fontSize: 33,
7. };
8. let myParagraphStyle: text.ParagraphStyle = {
9. textStyle: myTextStyle,
10. align: text.TextAlign.END,
11. };
12. let fontCollection = new text.FontCollection();
13. let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
14. }

16. @Entry
17. @Component
18. struct Index {
19. fun: Function = textFunc;
20. build() {
21. Column() {
22. Button().onClick(() => {
23. this.fun();
24. })
25. }
26. }
27. }
```

### pushStyle

PhonePC/2in1TabletTVWearable

pushStyle(textStyle: TextStyle): void

更新当前文本块的样式。

说明

更新当前文本块的样式，之后添加文字均采用该样式。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| textStyle | [TextStyle](js-apis-graphics-text.md#textstyle) | 是 | 包含了对文本的各种视觉属性的定义，如字体、字号、颜色、字重、字间距、行距、装饰（如下划线、删除线）、文本阴影等。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D'
2. import { text } from '@kit.ArkGraphics2D'
3. import { common2D } from '@kit.ArkGraphics2D'
4. import { image } from '@kit.ImageKit'

6. function textFunc() {
7. let myTextStyle: text.TextStyle = {
8. color: { alpha: 255, red: 255, green: 0, blue: 0 },
9. fontSize: 33,
10. };
11. let myParagraphStyle: text.ParagraphStyle = {
12. textStyle: myTextStyle,
13. align: text.TextAlign.CENTER,
14. };
15. let fontCollection = new text.FontCollection();
16. let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
17. paragraphBuilder.pushStyle(myTextStyle);
18. }

20. @Entry
21. @Component
22. struct Index {
23. fun: Function = textFunc;
24. build() {
25. Column() {
26. Button().onClick(() => {
27. this.fun();
28. })
29. }
30. }
31. }
```

### popStyle

PhonePC/2in1TabletTVWearable

popStyle(): void

弹出当前文本样式。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D'
2. import { text } from '@kit.ArkGraphics2D'
3. import { common2D } from '@kit.ArkGraphics2D'
4. import { image } from '@kit.ImageKit'

6. function textFunc() {
7. let myTextStyle: text.TextStyle = {
8. color: { alpha: 255, red: 255, green: 0, blue: 0 },
9. fontSize: 33,
10. };
11. let myParagraphStyle: text.ParagraphStyle = {
12. textStyle: myTextStyle,
13. align: text.TextAlign.END,
14. };
15. let fontCollection = new text.FontCollection();
16. let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
17. paragraphBuilder.pushStyle(myTextStyle);
18. paragraphBuilder.popStyle();
19. }

21. @Entry
22. @Component
23. struct Index {
24. fun: Function = textFunc;
25. build() {
26. Column() {
27. Button().onClick(() => {
28. this.fun();
29. })
30. }
31. }
32. }
```

### addText

PhonePC/2in1TabletTVWearable

addText(text: string): void

向正在构建的文本段落中插入具体的文本字符串。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 段落中插入的具体文本字符串，传入非法Unicode时会显示�。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D'
2. import { text } from '@kit.ArkGraphics2D'
3. import { common2D } from '@kit.ArkGraphics2D'
4. import { image } from '@kit.ImageKit'

6. function textFunc() {
7. let myTextStyle: text.TextStyle = {
8. color: { alpha: 255, red: 255, green: 0, blue: 0 },
9. fontSize: 33,
10. };
11. let myParagraphStyle: text.ParagraphStyle = {
12. textStyle: myTextStyle,
13. align: text.TextAlign.END,
14. };
15. let fontCollection = new text.FontCollection();
16. let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
17. paragraphBuilder.addText("123666");
18. }

20. @Entry
21. @Component
22. struct Index {
23. fun: Function = textFunc;
24. build() {
25. Column() {
26. Button().onClick(() => {
27. this.fun();
28. })
29. }
30. }
31. }
```

### addPlaceholder

PhonePC/2in1TabletTVWearable

addPlaceholder(placeholderSpan: PlaceholderSpan): void

用于构建文本段落时插入占位符。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| placeholderSpan | [PlaceholderSpan](js-apis-graphics-text.md#placeholderspan) | 是 | 定义了占位符的尺寸、对齐方式、基线类型以及基线偏移量。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D'
2. import { text } from '@kit.ArkGraphics2D'
3. import { common2D } from '@kit.ArkGraphics2D'
4. import { image } from '@kit.ImageKit'

6. function textFunc() {
7. let myParagraphStyle: text.ParagraphStyle = {
8. align: text.TextAlign.END,
9. };
10. let myPlaceholderSpan: text.PlaceholderSpan = {
11. width: 100,
12. height: 100,
13. align: text.PlaceholderAlignment.ABOVE_BASELINE,
14. baseline: text.TextBaseline.ALPHABETIC,
15. baselineOffset: 100
16. };
17. let fontCollection = new text.FontCollection();
18. let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
19. paragraphBuilder.addPlaceholder(myPlaceholderSpan);
20. }

22. @Entry
23. @Component
24. struct Index {
25. fun: Function = textFunc;
26. build() {
27. Column() {
28. Button().onClick(() => {
29. this.fun();
30. })
31. }
32. }
33. }
```

### build

PhonePC/2in1TabletTVWearable

build(): Paragraph

用于构建段落，生成可用于后续排版渲染的段落对象。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Paragraph](js-apis-graphics-text.md#paragraph) | 可用于后续渲染的 Paragraph 对象。 |

**示例：**

```
1. import { drawing, text, common2D } from '@kit.ArkGraphics2D'
2. import { image } from '@kit.ImageKit'

4. function textFunc() {
5. let myTextStyle: text.TextStyle = {
6. color : {alpha: 255, red: 255, green: 0, blue: 0},
7. fontSize : 20,
8. };
9. let myParagraphStyle: text.ParagraphStyle = {
10. textStyle : myTextStyle,
11. };
12. let fontCollection = new text.FontCollection();
13. let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
14. paragraphBuilder.addText("123456789");
15. let paragraph = paragraphBuilder.build();
16. paragraph.layoutSync(200);
17. }

19. @Entry
20. @Component
21. struct Index {
22. fun: Function = textFunc;
23. build() {
24. Column() {
25. Button().onClick(() => {
26. this.fun();
27. })
28. }
29. }
30. }
```

### buildLineTypeset18+

PhonePC/2in1TabletTVWearable

buildLineTypeset(): LineTypeset

构建行排版器。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LineTypeset](js-apis-graphics-text.md#linetypeset18) | 可用于后续渲染的LineTypeset对象。 |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'

3. function test() {
4. let myParagraphStyle: text.ParagraphStyle = {
5. align: text.TextAlign.JUSTIFY,
6. };
7. let fontCollection = new text.FontCollection();
8. let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
9. paragraphBuilder.addText("123456789");
10. let lineTypeset = paragraphBuilder.buildLineTypeset();
11. }

13. @Entry
14. @Component
15. struct Index {
16. fun: Function = test;
17. build() {
18. Column() {
19. Button().onClick(() => {
20. this.fun();
21. })
22. }
23. }
24. }
```

### addSymbol

PhonePC/2in1TabletTVWearable

addSymbol(symbolId: number): void

向正在构建的文本段落中插入具体符号。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| symbolId | number | 是 | 要设置的symbol码位，十六进制，当前支持的取值范围为：0xF0000-0xF0C97。可设置的symbol码位（即列表视图下的unicode值）请见[主题图标库](https://developer.huawei.com/consumer/cn/design/harmonyos-symbol/)。 |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'

3. function textFunc() {
4. let myTextStyle: text.TextStyle = {
5. color: { alpha: 255, red: 255, green: 0, blue: 0 },
6. fontSize: 33,
7. };
8. let myParagraphStyle: text.ParagraphStyle = {
9. textStyle: myTextStyle,
10. align: text.TextAlign.END,
11. };
12. let fontCollection = new text.FontCollection();
13. let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
14. paragraphBuilder.addSymbol(0xF0000);
15. let paragraph = paragraphBuilder.build();
16. }

18. @Entry
19. @Component
20. struct Index {
21. fun: Function = textFunc;
22. build() {
23. Column() {
24. Button().onClick(() => {
25. this.fun();
26. })
27. }
28. }
29. }
```

## TypographicBounds18+

PhonePC/2in1TabletTVWearable

文本行的排版边界。文本行排版边界与排版字体、排版字号有关，与字符本身无关，例如字符串为" a b "，'a'字符前面有1个空格，'b'字符后面有1个空格，排版边界就包括行首和末尾空格的边界。例如字符串为"j"或"E"，排版边界相同，即与字符本身无关。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ascent | number | 否 | 否 | 文本行的上升高度，浮点数。 |
| descent | number | 否 | 否 | 文本行的下降高度，浮点数。 |
| leading | number | 否 | 否 | 文本行的行间距，浮点数。 |
| width | number | 否 | 否 | 排版边界的总宽度，浮点数。 |

说明

示意图展示了ascent、descent、leading、top、baseline、bottom、next line top的含义。width为文本行排版包括左右空格的宽度。ascent为文本行上升高度最高点，descent为文本行下降高度最低点，leading为文本行间距，top为文本行的最高点，baseline为字符基线，bottom为文本行的最低点，next line top为下一个文本行的最高点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/uTDa6AzmQPKgQsHQ2SQb6g/zh-cn_image_0000002552960894.png?HW-CC-KV=V1&HW-CC-Date=20260428T001443Z&HW-CC-Expire=86400&HW-CC-Sign=F2E050A234A0800B18C46828AE7796F45382248CF8E5EED90339BE4BC87EA649)

示意图展示了字符串为" a b "的排版边界。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/gmR46MqZQrajHkpaQxCVjg/zh-cn_image_0000002583480895.png?HW-CC-KV=V1&HW-CC-Date=20260428T001443Z&HW-CC-Expire=86400&HW-CC-Sign=2386321D024EFD33C26F595CFA72DB00B3E96BAFCEB57F67E918D94062DD3F72)

示意图展示了字符串为"j"或"E"的排版边界。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/fJGDHPcpR6uyv1_Y1iJswA/zh-cn_image_0000002552801246.png?HW-CC-KV=V1&HW-CC-Date=20260428T001443Z&HW-CC-Expire=86400&HW-CC-Sign=9EE20D24EC50366D1EE3B1E2EB02614B9418B12C088777658BDD807C217FA7B1)

## CaretOffsetsCallback18+

PhonePC/2in1TabletTVWearable

type CaretOffsetsCallback = (offset: number, index: number, leadingEdge: boolean) => boolean

将文本行中每个字符的偏移量和索引值作为参数的回调方法。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 文本行中每个字符的偏移量，浮点数。 |
| index | number | 是 | 文本行中每个字符的索引值，整数。 |
| leadingEdge | boolean | 是 | 光标是否位于字符的前缘，true表示位于字符前缘，即偏移量不包含该字符宽度，false表示位于字符后缘，即偏移量包含该字符宽度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示是否停止调用该回调函数，true表示停止调用该回调函数，false表示继续调用该回调函数。 |

## TextLine

PhonePC/2in1TabletTVWearable

描述段落基础文本行结构的载体。

下列API示例中都需先使用[Paragraph](js-apis-graphics-text.md#paragraph)类的[getTextLines()](js-apis-graphics-text.md#gettextlines)接口或者[LineTypeset](js-apis-graphics-text.md#linetypeset18)类的[createLine()](js-apis-graphics-text.md#createline18)接口获取到TextLine对象实例，再通过此实例调用对应方法。

### getGlyphCount

PhonePC/2in1TabletTVWearable

getGlyphCount(): number

获取文本行中字形的数量。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 该文本行中字形数量，整数。 |

**示例：**

```
1. let glyphCount = lines[0].getGlyphCount();
```

### getTextRange

PhonePC/2in1TabletTVWearable

getTextRange(): Range

获取该行文本在整个段落文本中的索引区间。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Range](js-apis-graphics-text.md#range) | 该行文本在整个段落文本中的索引区间。 |

**示例：**

```
1. let textRange = lines[0].getTextRange();
```

### getGlyphRuns

PhonePC/2in1TabletTVWearable

getGlyphRuns(): Array<Run>

获取文本行的排版单元数组。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[Run](js-apis-graphics-text.md#run)> | 该文本行中的文本排版单元数组。 |

**示例：**

```
1. let runs = lines[0].getGlyphRuns();
```

### paint

PhonePC/2in1TabletTVWearable

paint(canvas: drawing.Canvas, x: number, y: number): void

在画布上以坐标点(x, y)为左上角位置绘制该文本行。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| canvas | [drawing.Canvas](arkts-apis-graphics-drawing-canvas.md) | 是 | 绘制的目标canvas。 |
| x | number | 是 | 绘制的左上角位置的横坐标，浮点数。 |
| y | number | 是 | 绘制的左上角位置的纵坐标，浮点数。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D'
2. import { text } from '@kit.ArkGraphics2D'
3. import { common2D } from '@kit.ArkGraphics2D'
4. import { image } from '@kit.ImageKit'

6. function textFunc(pixelmap: PixelMap) {
7. let canvas = new drawing.Canvas(pixelmap);
8. lines[0].paint(canvas, 0, 0);
9. }

11. @Entry
12. @Component
13. struct Index {
14. @State pixelmap?: PixelMap = undefined;
15. fun: Function = textFunc;
16. build() {
17. Column() {
18. Image(this.pixelmap).width(200).height(200);
19. Button().onClick(() => {
20. if (this.pixelmap == undefined) {
21. const color: ArrayBuffer = new ArrayBuffer(160000);
22. let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 } }
23. this.pixelmap = image.createPixelMapSync(color, opts);
24. }
25. this.fun(this.pixelmap);
26. })
27. }
28. }
29. }
```

### createTruncatedLine18+

PhonePC/2in1TabletTVWearable

createTruncatedLine(width: number, ellipsisMode: EllipsisMode, ellipsis: string): TextLine

创建一个截断的文本行对象。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 截断后的行宽度，浮点数。 |
| ellipsisMode | [EllipsisMode](js-apis-graphics-text.md#ellipsismode) | 是 | 截断的类型，当前仅支持头部截断START和尾部截断END。 |
| ellipsis | string | 是 | 截断的标记字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextLine](js-apis-graphics-text.md#textline) | 截断的文本行对象。 |

**示例：**

```
1. import { drawing, text, common2D } from '@kit.ArkGraphics2D'
2. import { image } from '@kit.ImageKit'

4. function textFunc(pixelmap: PixelMap) {
5. let canvas = new drawing.Canvas(pixelmap);
6. let truncatedTextLine = lines[0].createTruncatedLine(100, text.EllipsisMode.START, "...");
7. truncatedTextLine.paint(canvas, 0, 100);
8. }

10. @Entry
11. @Component
12. struct Index {
13. @State pixelmap?: PixelMap = undefined;
14. fun: Function = textFunc;
15. build() {
16. Column() {
17. Image(this.pixelmap).width(200).height(200);
18. Button().onClick(() => {
19. if (this.pixelmap == undefined) {
20. const color: ArrayBuffer = new ArrayBuffer(160000);
21. let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 } }
22. this.pixelmap = image.createPixelMapSync(color, opts);
23. }
24. this.fun(this.pixelmap);
25. })
26. }
27. }
28. }
```

### getTypographicBounds18+

PhonePC/2in1TabletTVWearable

getTypographicBounds(): TypographicBounds

获取文本行的排版边界。文本行排版边界与排版字体、排版字号有关，与字符本身无关。例如字符串为" a b "，'a'字符前面有1个空格，'b'字符后面有1个空格，排版边界就包括行首和末尾空格的边界。例如字符串为"j"或"E"，排版边界相同，即与字符本身无关。

说明

示意图展示了字符串为" a b "的排版边界。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/6meJMaeDR8u8UlVcr6ur8w/zh-cn_image_0000002583480895.png?HW-CC-KV=V1&HW-CC-Date=20260428T001443Z&HW-CC-Expire=86400&HW-CC-Sign=93B6F51D13496A70387949724556D212A98AC8EA1D177B9AC3362F8C0A346157)

示意图展示了字符串为"j"或"E"的排版边界。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/GZGoy77ES66b_GrniteEew/zh-cn_image_0000002552801246.png?HW-CC-KV=V1&HW-CC-Date=20260428T001443Z&HW-CC-Expire=86400&HW-CC-Sign=C9D1086B79F5DF89B1A993A9BF79ACE4FB2647B3B49703D5DD5544559A79C4B1)

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TypographicBounds](js-apis-graphics-text.md#typographicbounds18) | 文本行的排版边界。 |

**示例：**

```
1. let bounds = lines[0].getTypographicBounds();
2. console.info('textLine ascent:' + bounds.ascent + ', descent:' + bounds.descent + ', leading:' + bounds.leading + ', width:' + bounds.width);
```

### getImageBounds18+

PhonePC/2in1TabletTVWearable

getImageBounds(): common2D.Rect

获取文本行的图像边界。文本行图像边界与排版字体、排版字号、字符本身都有关，相当于视觉边界。例如字符串为" a b "，'a'字符前面有1个空格，'b'字符后面有1个空格，用户在界面上只能看到"a b"，图像边界即为不包括带行首和末尾空格的边界。例如字符串为"j"或"E"，视觉边界不同，即与字符本身有关，"j"字符串的视觉边界宽度小于"E"字符串的视觉边界宽度，"j"字符串的视觉边界高度大于"E"字符串的视觉边界高度。

说明

示意图展示了字符串为" a b "的图像边界。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/3D3026QvQ62J7M_kCx_R3g/zh-cn_image_0000002583440941.png?HW-CC-KV=V1&HW-CC-Date=20260428T001443Z&HW-CC-Expire=86400&HW-CC-Sign=5C4F4EFEDCE4374E1C9DDDC17412F0A7368BCFDD92F057BEFE582B54D41A91B3)

示意图展示了字符串为"j"或"E"的图像边界。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/1kBohErrQnOsuiH-XNFKCg/zh-cn_image_0000002552960896.png?HW-CC-KV=V1&HW-CC-Date=20260428T001443Z&HW-CC-Expire=86400&HW-CC-Sign=F6BCFC54D3AC01B18B49431868721F572493DA73FD0A1DB6A188F2A581C3AC2D)

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [common2D.Rect](js-apis-graphics-common2d.md#rect) | 文本行的图像边界。 |

**示例：**

```
1. let imageBounds = lines[0].getImageBounds();
```

### getTrailingSpaceWidth18+

PhonePC/2in1TabletTVWearable

getTrailingSpaceWidth(): number

获取文本行尾部空白字符的宽度。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 文本行尾部空白字符的宽度，浮点数。 |

**示例：**

```
1. let trailingSpaceWidth = lines[0].getTrailingSpaceWidth();
```

### getStringIndexForPosition18+

PhonePC/2in1TabletTVWearable

getStringIndexForPosition(point: common2D.Point): number

获取给定位置在原始字符串中的字符索引。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | [common2D.Point](js-apis-graphics-common2d.md#point12) | 是 | 要查找索引的位置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 给定位置在文本行中对应的字符串索引，整数。 |

**示例：**

```
1. let point : common2D.Point = { x: 15.0, y: 2.0 };
2. let index = lines[0].getStringIndexForPosition(point);
```

### getOffsetForStringIndex18+

PhonePC/2in1TabletTVWearable

getOffsetForStringIndex(index: number): number

获取文本行中给定字符串索引处的偏移量。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 要获取偏移量的字符串索引，整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 给定字符串索引处的偏移量，浮点数。 |

**示例：**

```
1. let offset = lines[0].getOffsetForStringIndex(3);
```

### enumerateCaretOffsets18+

PhonePC/2in1TabletTVWearable

enumerateCaretOffsets(callback: CaretOffsetsCallback): void

枚举文本行中每个字符的偏移量和索引值。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [CaretOffsetsCallback](js-apis-graphics-text.md#caretoffsetscallback18) | 是 | 用户自定义函数。回调方法参数包括文本行中每个字符的偏移量和索引值。 |

**示例：**

```
1. function callback(offset: number, index: number, leadingEdge: boolean): boolean {
2. console.info('textLine: offset: ' + offset + ', index: ' + index + ', leadingEdge: ' + leadingEdge);
3. return index > 50;
4. }
5. lines[0].enumerateCaretOffsets(callback);
```

### getAlignmentOffset18+

PhonePC/2in1TabletTVWearable

getAlignmentOffset(alignmentFactor: number, alignmentWidth: number): number

获取文本行根据对齐因子和对齐宽度计算的对齐所需偏移量。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alignmentFactor | number | 是 | 对齐因子，即对齐的程度，浮点数。小于等于0.0表示左对齐，大于0.0小于0.5表示偏左对齐，0.5表示居中对齐，大于0.5小于1.0表示偏右对齐，大于等于1.0表示右对齐。 |
| alignmentWidth | number | 是 | 对齐宽度，即文本行的宽度，浮点数。小于文本行的实际宽度时，返回0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 计算得到的对齐所需偏移量，浮点数。 |

**示例：**

```
1. let alignmentOffset = lines[0].getAlignmentOffset(0.5, 500);
```

## Run

PhonePC/2in1TabletTVWearable

文本排版单元。

下列API示例中都需先使用[TextLine](js-apis-graphics-text.md#textline)类的[getGlyphRuns()](js-apis-graphics-text.md#getglyphruns)接口获取Run对象实例，再通过此实例调用对应方法。

### getGlyphCount

PhonePC/2in1TabletTVWearable

getGlyphCount(): number

获取该排版单元中字形的数量。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 该排版单元中字形数量，整数。 |

**示例：**

```
1. let glyphs = runs[0].getGlyphCount();
```

### getGlyphs

PhonePC/2in1TabletTVWearable

getGlyphs(): Array<number>

获取该排版单元中每个字符的字形序号。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<number> | 该排版单元中每个字符对应的字形序号。 |

**示例：**

```
1. let glyph = runs[0].getGlyphs();
```

### getGlyphs18+

PhonePC/2in1TabletTVWearable

getGlyphs(range: Range): Array<number>

获取该排版单元指定范围内每个字符的字形序号。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | [Range](js-apis-graphics-text.md#range) | 是 | 要获取的字形序号范围，range.start表示范围开始的位置，range.end表示范围的长度，如果长度是0表示从范围range.start开始获取到渲染块结束。当range.end、range.start为负数，或者传入null、undefined时，该方法将返回undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<number> | 该排版单元中每个字符对应的字形序号。 |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'

3. function textFunc() {
4. let glyphs = runs[0].getGlyphs(); // 获取渲染块全部字形序号
5. let glyphsRange = runs[0].getGlyphs({start:1, end:2}); // 获取渲染块从起始位置1开始，长度为2范围内的字形序号
6. glyphsRange = runs[0].getGlyphs({start:-1, end:2}); // -1是非法参数，将返回undefined
7. glyphsRange = runs[0].getGlyphs({start:0, end:-10}); // -10是非法参数，将返回undefined
8. let glyphsNull = runs[0].getGlyphs(null); // null是非法参数，将返回undefined
9. let glyphsUndefined = runs[0].getGlyphs(undefined); // undefined是非法参数，将返回undefined
10. }

12. @Entry
13. @Component
14. struct Index {
15. fun: Function = textFunc;
16. build() {
17. Column() {
18. Button().onClick(() => {
19. this.fun();
20. })
21. }
22. }
23. }
```

### getPositions

PhonePC/2in1TabletTVWearable

getPositions(): Array<common2D.Point>

获取该排版单元中每个字形相对于每行的字形位置。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[common2D.Point](js-apis-graphics-common2d.md#point12)> | 该排版单元中每个字形相对于每行的字形位置。 |

**示例：**

```
1. let positions = runs[0].getPositions();
```

### getPositions18+

PhonePC/2in1TabletTVWearable

getPositions(range: Range): Array<common2D.Point>

获取该排版单元指定范围内每个字形相对于每行的字形位置数组。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | [Range](js-apis-graphics-text.md#range) | 是 | 要获取的字形位置范围，range.start表示范围开始的位置，range.end表示范围的长度，如果长度是0表示从范围range.start开始获取到渲染块结束。当range.end、range.start为负数，或者传入null、undefined时，该方法将返回undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[common2D.Point](js-apis-graphics-common2d.md#point12)> | 该排版单元中每个字形相对于每行的字形位置。 |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'

3. function textFunc() {
4. let positions = runs[0].getPositions(); // 获取渲染块全部字形位置
5. let positionsRange = runs[0].getPositions({start:1, end:2}); // 获取渲染块从起始位置1开始, 长度为2范围内的字形位置
6. positionsRange = runs[0].getPositions({start:-1, end:2}); // -1是非法参数，将返回undefined
7. positionsRange = runs[0].getPositions({start:0, end:-10}); // -10是非法参数，将返回undefined
8. let positionsNull = runs[0].getPositions(null); // null是非法参数，将返回undefined
9. let positionsUndefined = runs[0].getPositions(undefined); // undefined是非法参数，将返回undefined
10. }

12. @Entry
13. @Component
14. struct Index {
15. fun: Function = textFunc;
16. build() {
17. Column() {
18. Button().onClick(() => {
19. this.fun();
20. })
21. }
22. }
23. }
```

### getOffsets

PhonePC/2in1TabletTVWearable

getOffsets(): Array<common2D.Point>

获取该排版单元中每个字形的索引偏移量。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[common2D.Point](js-apis-graphics-common2d.md#point12)> | 该排版单元中每个字形相对于其索引的偏移量。 |

**示例：**

```
1. let offsets = runs[0].getOffsets();
```

### getFont

PhonePC/2in1TabletTVWearable

getFont(): drawing.Font

获取排版单元的字体属性对象。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [drawing.Font](arkts-apis-graphics-drawing-font.md) | 该排版单元的字体属性对象实例。 |

**示例：**

```
1. let font = runs[0].getFont();
```

### paint

PhonePC/2in1TabletTVWearable

paint(canvas: drawing.Canvas, x: number, y: number): void

在画布上以(x, y)为左上角位置绘制排版单元。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| canvas | [drawing.Canvas](arkts-apis-graphics-drawing-canvas.md) | 是 | 绘制的目标 canvas。 |
| x | number | 是 | 绘制的左上角位置的横坐标，浮点数。 |
| y | number | 是 | 绘制的左上角位置的纵坐标。浮点数。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D'
2. import { text } from '@kit.ArkGraphics2D'
3. import { common2D } from '@kit.ArkGraphics2D'
4. import { image } from '@kit.ImageKit'

6. function textFunc(pixelmap: PixelMap) {
7. let canvas = new drawing.Canvas(pixelmap);
8. runs[0].paint(canvas, 0, 0);
9. }

11. @Entry
12. @Component
13. struct Index {
14. @State pixelmap?: PixelMap = undefined;
15. fun: Function = textFunc;
16. build() {
17. Column() {
18. Image(this.pixelmap).width(200).height(200);
19. Button().onClick(() => {
20. if (this.pixelmap == undefined) {
21. const color: ArrayBuffer = new ArrayBuffer(160000);
22. let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 } }
23. this.pixelmap = image.createPixelMapSync(color, opts);
24. }
25. this.fun(this.pixelmap);
26. })
27. }
28. }
29. }
```

### getStringRange18+

PhonePC/2in1TabletTVWearable

getStringRange(): Range

获取排版单元生成字形的字符范围。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Range](js-apis-graphics-text.md#range) | 排版单元生成字形的字符范围，Range类型中的start表示字符范围的开始位置，该位置是相对于整个段落的索引，Range类型中的end表示字符范围的长度。 |

**示例：**

```
1. let runStringRange = runs[0].getStringRange();
2. let location = runStringRange.start;
3. let length = runStringRange.end;
```

### getStringIndices18+

PhonePC/2in1TabletTVWearable

getStringIndices(range?: Range): Array<number>

获取排版单元指定范围内字形的字符索引，该索引是相对于整个段落的偏移。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | [Range](js-apis-graphics-text.md#range) | 否 | 要获取的字符索引范围，range.start表示范围开始的位置，range.end表示范围的长度，如果长度是0表示从范围range.start开始获取到渲染块结束。当range.end、range.start为负数，或者传入null、undefined时，该方法将返回undefined。不传该参数时，默认获取整个渲染块。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<number> | 返回每个字符的索引。 |

**示例：**

```
1. import { text } from '@kit.ArkGraphics2D'

3. function textFunc() {
4. let indices = runs[0].getStringIndices(); // 获取渲染块全部字符索引
5. let indicesRange = runs[0].getStringIndices({start:1, end:2}); // 获取渲染块从起始位置1开始, 长度为2范围内的字符索引
6. indicesRange = runs[0].getStringIndices({start:-1, end:2}); // -1是非法参数，将返回undefined
7. indicesRange = runs[0].getStringIndices({start:0, end:-10}); // -10是非法参数，将返回undefined
8. let indicesNull = runs[0].getStringIndices(null); // null是非法参数，将返回undefined
9. let indicesUndefined = runs[0].getStringIndices(undefined); // undefined是非法参数，将返回undefined
10. }

12. @Entry
13. @Component
14. struct Index {
15. fun: Function = textFunc;
16. build() {
17. Column() {
18. Button().onClick(() => {
19. this.fun();
20. })
21. }
22. }
23. }
```

### getImageBounds18+

PhonePC/2in1TabletTVWearable

getImageBounds(): common2D.Rect

获取该排版单元的图像边界，图像边界与排版字体、排版字号、字符本身都有关，相当于视觉边界，例如字符串为" a b "，'a'字符前面有1个空格，'b'字符后面有1个空格，用户在界面上只能看到"a b"，图像边界即为不包括带行首和末尾空格的边界。

说明

示意图展示了字符串为" a b "的图像边界。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/do5YWyCeTo2sy6gJ9qGxug/zh-cn_image_0000002583440941.png?HW-CC-KV=V1&HW-CC-Date=20260428T001443Z&HW-CC-Expire=86400&HW-CC-Sign=27A2F2C476A2A4A93E19C6431EAE21A2E1CE95320B572C7854B887A3A94793E2)

示意图展示了字符串为"j"或"E"的图像边界。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/q2ycpidvQlWGUwI0RsC9Ng/zh-cn_image_0000002552960896.png?HW-CC-KV=V1&HW-CC-Date=20260428T001443Z&HW-CC-Expire=86400&HW-CC-Sign=461120C00C41D85EA58DE1AD3200B9D5AA4337439C2ABFC26C0CE1A0913C74BB)

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [common2D.Rect](js-apis-graphics-common2d.md#rect) | 该排版单元的图像边界。 |

**示例：**

```
1. let bounds = runs[0].getImageBounds();
```

### getTypographicBounds18+

PhonePC/2in1TabletTVWearable

getTypographicBounds(): TypographicBounds

获取该排版单元的排版边界，排版边界与排版字体、排版字号有关，与字符本身无关，例如字符串为" a b "，'a'字符前面有1个空格，'b'字符后面有1个空格，排版边界就包括行首和末尾空格的边界。

说明

示意图展示了字符串为" a b "的排版边界。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/wIAOUph2R1eq4t22iem_Ww/zh-cn_image_0000002583480895.png?HW-CC-KV=V1&HW-CC-Date=20260428T001443Z&HW-CC-Expire=86400&HW-CC-Sign=C3EB1CD84D4D9681E194C26E661EE2FEF7897C896D20B2D5764E117D90BB6B87)

示意图展示了字符串为"j"或"E"的排版边界。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/dZQFoKGGRYWdRUVVa5PSbA/zh-cn_image_0000002552801246.png?HW-CC-KV=V1&HW-CC-Date=20260428T001443Z&HW-CC-Expire=86400&HW-CC-Sign=F70C46C4278C3E60668549F95CC430CB2E79DD3739D8F20381A9661F26CE4007)

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TypographicBounds](js-apis-graphics-text.md#typographicbounds18) | 该排版单元的排版边界。 |

**示例：**

```
1. let typographicBounds = runs[0].getTypographicBounds();
```

### getTextDirection20+

PhonePC/2in1TabletTVWearable

getTextDirection(): TextDirection

获取该排版单元的文本方向。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextDirection](js-apis-graphics-text.md#textdirection) | 返回该排版单元的文本方向。 |

**示例：**

```
1. let textDirection = runs[0].getTextDirection();
```

### getAdvances20+

PhonePC/2in1TabletTVWearable

getAdvances(range: Range): Array<common2D.Point>

获取该排版单元指定范围内每个字形的字形宽度数组。

**系统能力**：SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | [Range](js-apis-graphics-text.md#range) | 是 | 要获取的字形位置范围。range.start表示范围开始的位置，range.end表示范围的长度。如果长度是0表示从range.start开始获取到渲染块结束。当range.end、range.start为负数，或者传入null、undefined时，该方法将返回undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[common2D.Point](js-apis-graphics-common2d.md#point12)> | 返回该排版单元中每个字形相对于水平方向的字形宽度数组。其中，[common2D.Point](js-apis-graphics-common2d.md#point12)中的x值代表每个字形相对于水平方向的字形宽度，y值为保留字段，默认返回0。 |

**示例：**

```
1. let advancesRange = runs[0].getAdvances({start:1, end:2}); // 获取渲染块从起始位置1开始, 长度为2范围内的字形宽度
2. advancesRange = runs[0].getAdvances({start:-1, end:2}); // -1是非法参数，将返回undefined
3. advancesRange = runs[0].getAdvances({start:0, end:-10}); // -10是非法参数，将返回undefined
4. let advancesNull = runs[0].getAdvances(null); // null是非法参数，将返回undefined
```

## TextTab18+

PhonePC/2in1TabletTVWearable

段落风格的文本制表符，储存了对齐方式和位置。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| alignment | [TextAlign](js-apis-graphics-text.md#textalign) | 否 | 否 | 段落中制表符之后的文本对齐方式，支持设置[TextAlign](js-apis-graphics-text.md#textalign)的LEFT左对齐、RIGHT右对齐和CENTER居中对齐方式，其他枚举值为左对齐，默认为左对齐。 |
| location | number | 否 | 否 | 制表符之后的文本对齐位置，浮点数，单位为物理像素px，最小值为1.0，当该值小于1.0时，该制表符会被替换为一个空格。 |

**示例：**

alignment为CENTER，location为200，文本为"12/t345"：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/_KGj8lDWTme1ZIGvI8Fzvg/zh-cn_image_0000002583480897.png?HW-CC-KV=V1&HW-CC-Date=20260428T001443Z&HW-CC-Expire=86400&HW-CC-Sign=A3C95FA46914FF33A57642C70436567F494B0C056B071697BB7E9629E4925AA6)

alignment为LEFT，location为100，文本为"abccccccccc/tdef"：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/ysnWZY58QYaQFn2pJBG2PQ/zh-cn_image_0000002552801248.png?HW-CC-KV=V1&HW-CC-Date=20260428T001443Z&HW-CC-Expire=86400&HW-CC-Sign=BD273186D3AF6FBEDCAB084AA1D3A6FF3691EC900747D99F490DFA4506897B37)

alignment为RIGHT，location为100，文本为"aabcdef/tg hi/tjkl/tmno/tp qr"：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/OpDH_paeT5WMgZpKAw4FmQ/zh-cn_image_0000002583440943.png?HW-CC-KV=V1&HW-CC-Date=20260428T001443Z&HW-CC-Expire=86400&HW-CC-Sign=B33E550896E5C85E3FD38A996F3F92ABEACBE1576A2AF7BB2D74E226363D7D7F)

## SystemFontType14+

PhonePC/2in1TabletTVWearable

字体类型枚举，通过位或运算可实现组合类型。

**系统能力：** SystemCapability.Graphics.Drawing

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALL | 1 << 0 | 所有字体类型，包括系统字体类型、风格字体类型和用户已安装字体类型。 |
| GENERIC | 1 << 1 | 系统字体类型。 |
| STYLISH | 1 << 2 | 风格字体类型。风格字体类型是专为2in1设备设计的字体类型。 |
| INSTALLED | 1 << 3 | 用户已安装的字体类型。 |
| CUSTOMIZED18+ | 1 << 4 | 自定义字体类型。 |
