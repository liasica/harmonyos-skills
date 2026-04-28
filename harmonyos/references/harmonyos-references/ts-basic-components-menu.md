---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-menu
title: Menu
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 菜单 > Menu
category: harmonyos-references
scraped_at: 2026-04-28T08:02:15+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f46b1454b3b73286a11e8d9f1e97e13cd6fbf636488c6b6ae7e77b13dcfdf489
---

以垂直列表形式显示的菜单。

说明

* 该组件从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* Menu组件需和[bindMenu](ts-universal-attributes-menu.md#bindmenu)或[bindContextMenu](ts-universal-attributes-menu.md#bindcontextmenu8)方法配合使用，不支持作为普通组件单独使用。

## 子组件

PhonePC/2in1TabletTVWearable

包含[MenuItem](ts-basic-components-menuitem.md)、[MenuItemGroup](ts-basic-components-menuitemgroup.md)子组件。

## 接口

PhonePC/2in1TabletTVWearable

Menu()

作为菜单的固定容器，无参数。

说明

* 菜单和菜单项宽度计算规则：

  + 布局过程中，期望每个菜单项的宽度一致。若子组件设置了宽度，则以[尺寸计算规则](ts-universal-attributes-size.md#constraintsize)为准。
  + Menu不设置宽度的情况：Menu会对子组件MenuItem、MenuItemGroup设置默认2栅格的宽度，若菜单项内容区比2栅格宽，则会自适应撑开。
  + Menu设置宽度的情况：Menu会对子组件MenuItem、MenuItemGroup设置减去padding后的固定宽度。
  + Menu支持设置的最小宽度为64vp。
* Menu不支持的通用属性：[outline](ts-universal-attributes-outline.md)下的属性、[shadow](ts-universal-attributes-image-effect.md#shadow)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### font10+

PhonePC/2in1TabletTVWearable

font(value: Font)

统一设置Menu中所有文本的尺寸。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](ts-types.md#font) | 是 | Menu中所有文本的尺寸。  默认值：  {  size: 16,  family: 'HarmonyOS Sans',  weight: FontWeight.Medium,  style: FontStyle.Normal  } |

### fontColor10+

PhonePC/2in1TabletTVWearable

fontColor(value: ResourceColor)

统一设置Menu中所有文本的颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | Menu中所有文本的颜色。 |

### radius10+

PhonePC/2in1TabletTVWearable

radius(value: Dimension | BorderRadiuses)

设置Menu边框圆角半径。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](ts-types.md#dimension10) | [BorderRadiuses](ts-types.md#borderradiuses9) | 是 | Menu边框圆角半径。  默认值：2in1设备上默认值为8vp，其他设备上默认值为20vp。  从API version 12开始，当水平方向两个圆角半径之和的最大值大于菜单宽度，或垂直方向两个圆角半径之和的最大值大于菜单高度时，菜单四个圆角均采用菜单默认圆角半径值。  当设置Dimension类型且传参为异常值时，菜单圆角取默认值。  当设置BorderRadiuses类型且传参为异常值时，菜单默认没有圆角。 |

### menuItemDivider12+

PhonePC/2in1TabletTVWearable

menuItemDivider(options: DividerStyleOptions | undefined)

设置menuItem分割线样式，不设置该属性则不展示分割线。

startMargin + endMargin 超过组件宽度后startMargin和endMargin会被置0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DividerStyleOptions](ts-types.md#dividerstyleoptions12) | undefined | 是 | 设置menuItem分割线样式。  -strokeWidth：分割线的线宽。  -color：分割线的颜色。  -startMargin：分割线与menuItem侧边起始端的距离。  -endMargin：分割线与menuItem侧边结束端的距离。  -mode：分割线的模式，默认值为FLOATING\_ABOVE\_MENU。 |

### menuItemGroupDivider12+

PhonePC/2in1TabletTVWearable

menuItemGroupDivider(options: DividerStyleOptions | undefined)

设置menuItemGroup上下分割线的样式，不设置该属性则默认展示分割线。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DividerStyleOptions](ts-types.md#dividerstyleoptions12) | undefined | 是 | 设置menuItemGroup顶部和底部分割线样式。  -strokeWidth：分割线的线宽，默认值是1px。  -color：分割线的颜色，默认值是 #33000000。  -startMargin：分割线与menuItemGroup侧边起始端的距离，默认为16vp，单位为vp。  -endMargin：分割线与menuItemGroup侧边结束端的距离，默认为16vp，单位为vp。  -mode：分割线的模式，默认值为FLOATING\_ABOVE\_MENU。 |

### subMenuExpandingMode12+

PhonePC/2in1TabletTVWearable

subMenuExpandingMode(mode: SubMenuExpandingMode)

设置Menu子菜单展开样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SubMenuExpandingMode](ts-basic-components-menu.md#submenuexpandingmode12枚举说明) | 是 | Menu子菜单展开样式。  默认值：SubMenuExpandingMode.SIDE\_EXPAND |

### subMenuExpandSymbol20+

PhonePC/2in1TabletTVWearable

subMenuExpandSymbol(symbol: SymbolGlyphModifier)

设置Menu子菜单展开符号。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| symbol | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md) | 是 | Menu子菜单展开符号。  1、子菜单的展开样式为SubMenuExpandingMode.SIDE\_EXPAND时，不显示展开符号。  2、子菜单的展开样式为SubMenuExpandingMode.EMBEDDED\_EXPAND时，展开时展开符号会顺时针旋转180°。  默认值：$r('sys.symbol.chevron\_down').fontSize('24vp')  3、子菜单的展开样式为SubMenuExpandingMode.STACK\_EXPAND时，展开时展开符号会顺时针旋转90°。  默认值：$r('sys.symbol.chevron\_forward').fontSize('20vp').padding('2vp') |

### fontSize(deprecated)

PhonePC/2in1TabletTVWearable

fontSize(value: Length)

统一设置Menu中所有文本的尺寸。

说明

从API version 9开始支持，从API version 10开始废弃，建议使用[font](ts-basic-components-menu.md#font10)代替。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | Menu中所有文本的尺寸，Length为number类型时，使用fp单位。不支持设置百分比。 |

## SubMenuExpandingMode12+枚举说明

PhonePC/2in1TabletTVWearable

Menu子菜单展开样式枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SIDE\_EXPAND | 0 | 默认展开样式，子菜单位于同一平面侧边展开。 |
| EMBEDDED\_EXPAND | 1 | 直接展开样式，子菜单嵌于主菜单内展开。 |
| STACK\_EXPAND | 2 | 堆叠样式，子菜单浮于主菜单上方展开。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置多级菜单）

该示例通过配置MenuItem中的builder参数实现多级菜单。

```
1. @Entry
2. @Component
3. struct Index {
4. @State select: boolean = true;
5. // $r('app.media.xxx')需要替换为开发者所需的图像资源文件。
6. private iconStr: ResourceStr = $r("app.media.view_list_filled");
7. private iconStr2: ResourceStr = $r("app.media.arrow_right_filled");

9. @Builder
10. SubMenu() {
11. Menu() {
12. MenuItem({ content: "复制", labelInfo: "Ctrl+C" })
13. MenuItem({ content: "粘贴", labelInfo: "Ctrl+V" })
14. }
15. }

17. @Builder
18. MyMenu(){
19. Menu() {
20. MenuItem({ startIcon: $r("app.media.icon"), content: "菜单选项" })
21. MenuItem({ startIcon: $r("app.media.icon"), content: "菜单选项" })
22. .enabled(false)
23. MenuItem({
24. startIcon: this.iconStr,
25. content: "菜单选项",
26. endIcon: this.iconStr2,
27. builder: ():void=>this.SubMenu()
28. })
29. MenuItemGroup({ header: '小标题' }) {
30. MenuItem({
31. startIcon: this.iconStr,
32. content: "菜单选项",
33. endIcon: this.iconStr2,
34. builder: ():void=>this.SubMenu()
35. })
36. MenuItem({
37. startIcon: $r("app.media.app_icon"),
38. content: "菜单选项",
39. endIcon: this.iconStr2,
40. builder: ():void=>this.SubMenu()
41. })
42. }
43. MenuItem({
44. startIcon: this.iconStr,
45. content: "菜单选项",
46. })
47. }
48. }

50. build() {
51. Row() {
52. Column() {
53. Text('click to show menu')
54. .fontSize(50)
55. .fontWeight(FontWeight.Bold)
56. }
57. .bindMenu(this.MyMenu)
58. .width('100%')
59. }
60. .height('100%')
61. }
62. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/84Z3uhJRTxuTfdqxBXmISQ/zh-cn_image_0000002552960020.png?HW-CC-KV=V1&HW-CC-Date=20260428T000213Z&HW-CC-Expire=86400&HW-CC-Sign=75DF07411AD0C579C7CDD3F573B6707A5BE19AC97D72B1E4ABE2DB95EC9C0B47)

### 示例2（设置symbol类型图标）

该示例通过配置symbolStartIcon、symbolEndIcon实现symbol类型图标的菜单。

```
1. // xxx.ets
2. import { SymbolGlyphModifier } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Index {
7. @State startIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_mic')).fontSize('24vp');
8. @State endIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_trash')).fontSize('24vp');
9. @State selectIconModifier: SymbolGlyphModifier =
10. new SymbolGlyphModifier($r('sys.symbol.checkmark')).fontSize('24vp');
11. @State select: boolean = true;

13. @Builder
14. SubMenu() {
15. Menu() {
16. MenuItem({ content: "复制", labelInfo: "Ctrl+C" })
17. MenuItem({ content: "粘贴", labelInfo: "Ctrl+V" })
18. }
19. }

21. @Builder
22. MyMenu() {
23. Menu() {
24. MenuItem({ symbolStartIcon: this.startIconModifier, content: "菜单选项" })
25. MenuItem({ symbolStartIcon: this.startIconModifier, content: "菜单选项" })
26. .enabled(false)
27. MenuItem({
28. symbolStartIcon: this.startIconModifier,
29. content: "菜单选项",
30. symbolEndIcon: this.endIconModifier,
31. builder: (): void => this.SubMenu()
32. })
33. MenuItemGroup({ header: '小标题' }) {
34. MenuItem({
35. symbolStartIcon: this.startIconModifier,
36. content: "菜单选项",
37. symbolEndIcon: this.endIconModifier,
38. builder: (): void => this.SubMenu()
39. })
40. MenuItem({
41. symbolStartIcon: this.startIconModifier,
42. content: "菜单选项",
43. symbolEndIcon: this.endIconModifier,
44. builder: (): void => this.SubMenu()
45. })
46. }
47. MenuItem({
48. content: "菜单选项",
49. }).selected(this.select).selectIcon(this.selectIconModifier)
50. }
51. }

53. build() {
54. Row() {
55. Column() {
56. Text('click to show menu')
57. .fontSize(50)
58. .fontWeight(FontWeight.Bold)
59. }
60. .bindMenu(this.MyMenu)
61. .width('100%')
62. }
63. .height('100%')
64. }
65. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/SThdkg6NS6qQE2j2j820fQ/zh-cn_image_0000002583480021.png?HW-CC-KV=V1&HW-CC-Date=20260428T000213Z&HW-CC-Expire=86400&HW-CC-Sign=EF3DC8E4120C24881765EC1111AE853EA200BBD0E0C9465559646C7B1753959F)

### 示例3（设置Menu子菜单展开符号）

该示例通过配置subMenuExpandSymbol实现对Menu子菜单展开符号配置颜色。

```
1. import { SymbolGlyphModifier } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State startIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_star'))
7. @State endIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_mic'))
8. @State expandSymbolModifier: SymbolGlyphModifier =
9. new SymbolGlyphModifier($r('sys.symbol.chevron_down')).fontColor([Color.Red]).fontSize('24vp')

11. @Builder
12. SubMenu() {
13. Menu() {
14. MenuItem({
15. symbolStartIcon: this.startIconModifier,
16. content: "图标"
17. })
18. MenuItem({
19. symbolStartIcon: this.startIconModifier,
20. content: "列表"
21. })
22. }.backgroundColor(Color.Grey)
23. }

25. @Builder
26. MyMenu() {
27. Menu() {
28. MenuItem({
29. symbolStartIcon: this.startIconModifier,
30. symbolEndIcon: this.endIconModifier,
31. content: "新建文件夹",
32. builder: (): void => this.SubMenu(),
33. })
34. MenuItem({
35. symbolStartIcon: this.startIconModifier,
36. content: "排序方式",
37. builder: (): void => this.SubMenu(),
38. })
39. MenuItem({
40. symbolStartIcon: this.startIconModifier,
41. content: "查看方式",
42. builder: (): void => this.SubMenu(),
43. })
44. }
45. .subMenuExpandingMode(SubMenuExpandingMode.EMBEDDED_EXPAND)
46. .backgroundColor(Color.Grey)
47. .subMenuExpandSymbol(this.expandSymbolModifier)
48. }

50. build() {
51. Button('click to show menu')
52. .position({ top: 40, left: 40 })
53. .bindMenu(this.MyMenu)
54. }
55. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/H_Y20dqHT062u4jLXxSg7Q/zh-cn_image_0000002552800372.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000213Z&HW-CC-Expire=86400&HW-CC-Sign=BBBCDE1072D5552437E223F4DB885C7F5AA2AF264292465C17CF1131FF241701)

### 示例4（设置分割线样式）

该示例通过设置menuItemGroupDivider属性实现分割线样式。

```
1. import { LengthMetrics } from '@kit.ArkUI'

3. @Entry
4. @Component
5. struct Index {

7. @Builder
8. MyMenu() {
9. Menu() {
10. MenuItem({ content: "Item Content" })
11. MenuItem({ content: "Item Content" })
12. MenuItem({ content: "Item Content" })
13. MenuItemGroup() {
14. MenuItem({ content: "Group Child" })
15. MenuItem({ content: "Group Child" })
16. }
17. MenuItem({ content: "Item Content" })
18. }
19. .menuItemDivider({
20. strokeWidth: LengthMetrics.vp(5),
21. color: '#d5d5d5',
22. mode: DividerMode.EMBEDDED_IN_MENU
23. })
24. .menuItemGroupDivider({
25. strokeWidth: LengthMetrics.vp(5),
26. color: '#707070',
27. mode: DividerMode.EMBEDDED_IN_MENU
28. })
29. }

31. build() {
32. RelativeContainer() {
33. Button("show menu")
34. .bindMenu(this.MyMenu())
35. }
36. .height('100%')
37. .width('100%')
38. }
39. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/1X7NlF9wSXWJkUaV-0GeoA/zh-cn_image_0000002583440067.png?HW-CC-KV=V1&HW-CC-Date=20260428T000213Z&HW-CC-Expire=86400&HW-CC-Sign=9485716A42BA9BDB01FC5EEC10691B4E28BB7B43DF050F696178ECA50C87D84B)
