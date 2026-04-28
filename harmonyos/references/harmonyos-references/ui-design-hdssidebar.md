---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdssidebar
title: HdsSideBar
breadcrumb: API参考 > 应用框架 > UI Design Kit（UI设计套件） > ArkTS组件 > HdsSideBar
category: harmonyos-references
scraped_at: 2026-04-28T08:06:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1113f7c1cd30b10956a64748bd52bdb86864d6aae59ebc195a19809820d0a23c
---

本模块支持显示和隐藏的侧边栏容器，并且可以自定义侧边栏和内容区。

**起始版本：** 6.0.0(20)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { HdsSideBar } from '@kit.UIDesignKit';
```

## 接口

PhonePC/2in1TabletTV

HdsSideBar({contentAreaMask?: boolean, isShowSideBar?: boolean, $isShowSideBar?: Callback<boolean>, minSideBarWidth?: Length, maxSideBarWidth?: Length, minContentWidth?: Length, sideBarColor?: ResourceColor, contentColor?: ResourceColor, sideBarWidth?: Length, autoHide?: boolean, isSideBarBlur?: boolean, sideBarPosition?: sideBarPosition, onChange?: Callback<boolean>, sideBarPanelBuilder: CustomBuilder, contentPanelBuilder: CustomBuilder, sideBarContainerType?: SideBarContainerType, scaleContentEnabled?: boolean, swipeEnabled?: boolean})

**装饰器类型：** @ComponentV2

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| contentAreaMask | boolean | 否 | @Param | 设置HdsSideBar组件侧边栏悬浮显示的场景下内容区是否有蒙层。  true：内容区有蒙层。false：内容区没有蒙层。  默认值：true。 |
| isShowSideBar | boolean | 否 | @Param | 设置HdsSideBar组件是否显示侧边栏。  true：显示侧边栏。  false：不显示侧边栏。  默认值：true。 |
| $isShowSideBar | [Callback](ts-types.md#callback12)<boolean> | 否 | @Event | HdsSideBar组件侧边栏控制按钮点击后，是否显示侧边栏的回调。 |
| minSideBarWidth | [Length](ts-types.md#length) | 否 | @Param | 设置HdsSideBar组件侧边栏的最小宽度。  默认值：200vp。 |
| maxSideBarWidth | [Length](ts-types.md#length) | 否 | @Param | 设置HdsSideBar组件侧边栏的最大宽度。  默认值：280vp。 |
| minContentWidth | [Length](ts-types.md#length) | 否 | @Param | 设置HdsSideBar组件内容区可显示的最小宽度。  默认值：360vp。 |
| sideBarColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | @Param | 设置HdsSideBar组件侧边栏区的背景颜色。  默认值：Color.Transparent。 |
| contentColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | @Param | 设置HdsSideBar组件内容区的背景颜色。  默认值：Color.Transparent。 |
| sideBarWidth | [Length](ts-types.md#length) | 否 | @Param | 设置HdsSideBar组件侧边栏的宽度。  默认值：240vp。 |
| autoHide | boolean | 否 | @Param | 设置HdsSideBar组件侧边栏拖拽到小于最小宽度后，是否自动隐藏。  true：会自动隐藏。  false：不会自动隐藏。  默认值：true。 |
| isSideBarBlur | boolean | 否 | @Param | 设置HdsSideBar组件窗口获焦时侧边栏是否有模糊效果。  true：窗口获焦时HdsSideBar组件侧边栏会有模糊效果，失焦时没有模糊效果。  false：窗口始终没有模糊效果。  默认值：true。 |
| sideBarPosition | [SideBarPosition](ts-container-sidebarcontainer.md#sidebarposition9枚举说明) | 否 | @Param | 设置HdsSideBar组件侧边栏显示位置。  默认值：SideBarPosition.Start，侧边栏位于容器左侧。 |
| onChange | [Callback](ts-types.md#callback12)<boolean> | 否 | @Param | 当HdsSideBar组件侧边栏的状态在显示和隐藏之间切换时触发回调。  触发该事件的条件：  1. showSideBar属性值变换时。  2. showSideBar属性自适应行为变化时。  3. 分割线拖拽触发autoHide时。  true表示显示侧边栏，false表示隐藏侧边栏。 |
| sideBarPanelBuilder | [CustomBuilder](ts-types.md#custombuilder8) | 是 | @Require  @BuilderParam | 设置HdsSideBar组件侧边栏的子组件。 |
| contentPanelBuilder | [CustomBuilder](ts-types.md#custombuilder8) | 是 | @Require  @BuilderParam | 设置HdsSideBar组件内容区的子组件。 |
| sideBarContainerType | [SideBarContainerType](ts-container-sidebarcontainer.md#sidebarcontainertype枚举说明) | 否 | @Param | 设置HdsSideBar组件侧边栏的显示类型。  默认值：SideBarContainerType.AUTO，侧边栏嵌入到组件内，和内容区并列显示。 |
| scaleContentEnabled | boolean | 否 | @Param | 设置侧边栏展开内容区是否为缩放样式。  true：侧边栏展开内容区为缩放样式。  false：侧边栏展开内容区为平移样式。  默认值：true。  **起始版本**：6.1.0(23) |
| swipeEnabled | boolean | 否 | @Param | 设置侧边栏抽屉是否可跟随滑动手势展开关闭。  true：侧边栏抽屉跟随滑动手势展开关闭。  false：侧边栏抽屉不跟随滑动手势展开关闭。  默认值：false。  **起始版本**：6.1.0(23)  **说明**：  swipeEnabled仅在平移场景下（scaleContentEnabled为false）生效，其他场景下不支持侧滑手势。 |

## build

PhonePC/2in1TabletTV

build(): void

struct的默认构造函数，无法直接调用此方法。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：** 6.0.0(20)

## 示例

PhonePC/2in1TabletTV

HdsSideBar提供侧边栏可以显示和隐藏的侧边栏容器，可以自定义侧边栏区和内容区。

```
1. import { HdsSideBar } from '@kit.UIDesignKit';

3. @Entry
4. @ComponentV2
5. struct Index {
6. @Local isShowSidebar: boolean = true;

8. //左侧侧边栏区
9. @Builder
10. SideBarPanelBuilder() {
11. Column() {
12. Text('左侧侧边栏区')
13. }
14. .width('100%')
15. .height('100%')
16. .margin(40)
17. }

19. //右侧内容区
20. @Builder
21. ContentPanelBuilder() {
22. Text('右侧内容区')
23. .margin(40)
24. }

26. @BuilderParam contentBuilder: () => void = this.ContentPanelBuilder
27. @BuilderParam sideBarBuilder: () => void = this.SideBarPanelBuilder

29. @Builder
30. build() {
31. Stack({ alignContent: Alignment.TopStart }) {
32. Button() {
33. SymbolGlyph(this.isShowSidebar ? $r('sys.symbol.open_sidebar') : $r('sys.symbol.close_sidebar'))
34. .fontWeight(FontWeight.Normal)
35. .fontSize($r('sys.float.ohos_id_text_size_headline7'))
36. .fontColor([$r('sys.color.ohos_id_color_titlebar_icon')])
37. .hitTestBehavior(HitTestMode.None)
38. }
39. .id('side_bar_button')
40. .backgroundColor($r('sys.color.ohos_id_color_button_normal'))
41. .height(30)
42. .width(30)
43. .onClick(() => {
44. this.isShowSidebar = !this.isShowSidebar;
45. })
46. .zIndex(1)
47. .margin({ top: 10, left: 10 })

49. HdsSideBar({
50. sideBarPanelBuilder: (): void => {
51. this.sideBarBuilder()
52. },
53. contentPanelBuilder: (): void => {
54. this.contentBuilder()
55. },
56. sideBarContainerType: SideBarContainerType.Overlay,
57. maxSideBarWidth: 100,
58. isShowSideBar: this.isShowSidebar,
59. $isShowSideBar: (isShowSidebar: boolean) => {
60. this.isShowSidebar = !isShowSidebar
61. },
62. })
63. }
64. }
65. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/MkqcLJVRSgOpQIYcglp5Hg/zh-cn_image_0000002583440571.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000639Z&HW-CC-Expire=86400&HW-CC-Sign=C73DCDD6EEEAAB4030A5DB33469E311BC4AADE3C1829866662DFF866A2E9AB0A)
