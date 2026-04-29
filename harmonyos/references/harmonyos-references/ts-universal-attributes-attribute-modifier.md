---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier
title: 动态属性设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 动态属性与自定义 > 动态属性设置
category: harmonyos-references
scraped_at: 2026-04-29T13:51:31+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:dbb870e3798a6b574410fe9eff34c85fbc26ba6248f71e37421064fa70c52ead
---

动态设置组件的属性，支持开发者在属性设置时使用if/else语法，且根据需要使用多态样式设置属性。

说明

* 从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 在attributeModifier中设置的属性尽量不要与其他方法设置的属性相同，避免在页面刷新时attributeModifier不生效。
* 对于仅需根据条件设置组件单一属性的简单场景，可以使用[三目表达式](../harmonyos-guides/arkts-declarative-ui-description.md#配置属性)（如.width(isFullScreen ? 200 : 100)）。
* 从API version 20开始，attributeModifier支持自定义组件。

## attributeModifier

PhonePC/2in1TabletTVWearable

attributeModifier(modifier: AttributeModifier<T>): T

动态设置组件的属性方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier<T>](ts-universal-attributes-attribute-modifier.md#attributemodifiert) | 是 | 在当前组件上，动态设置属性方法，支持使用if/else语法。  modifier：属性修改器，开发者需要自定义class实现AttributeModifier接口。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## AttributeModifier<T>

PhonePC/2in1TabletTVWearable

开发者需要自定义class实现AttributeModifier接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

说明

在以下回调函数中，当对instance对象的同一个属性重复设置相同的值或对象时，不会触发该属性的更新。

### applyNormalAttribute

PhonePC/2in1TabletTVWearable

applyNormalAttribute?(instance: T): void

组件普通状态时的样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instance | T | 是 | 组件的属性类，用来标识进行属性设置的组件的类型，比如[Button](ts-basic-components-button.md)组件的[ButtonAttribute](ts-basic-components-button.md#属性)，[Text](ts-basic-components-text.md)组件的[TextAttribute](ts-basic-components-text.md#属性)等。 |

### applyPressedAttribute

PhonePC/2in1TabletTVWearable

applyPressedAttribute?(instance: T): void

组件按压状态的样式。参考[示例2（组件绑定Modifier实现按压态效果）](ts-universal-attributes-attribute-modifier.md#示例2组件绑定modifier实现按压态效果)、[示例8（自定义组件绑定Modifier实现按压态效果）](ts-universal-attributes-attribute-modifier.md#示例8自定义组件绑定modifier实现按压态效果)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instance | T | 是 | 组件的属性类，用来标识进行属性设置的组件的类型，比如[Button](ts-basic-components-button.md)组件的[ButtonAttribute](ts-basic-components-button.md#属性)，[Text](ts-basic-components-text.md)组件的[TextAttribute](ts-basic-components-text.md#属性)等。 |

### applyFocusedAttribute

PhonePC/2in1TabletTVWearable

applyFocusedAttribute?(instance: T): void

组件获焦状态的样式。参考[示例5（组件绑定Modifier获焦样式）](ts-universal-attributes-attribute-modifier.md#示例5组件绑定modifier获焦样式)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instance | T | 是 | 组件的属性类，用来标识进行属性设置的组件的类型，比如[Button](ts-basic-components-button.md)组件的[ButtonAttribute](ts-basic-components-button.md#属性)，[Text](ts-basic-components-text.md)组件的[TextAttribute](ts-basic-components-text.md#属性)等。 |

### applyDisabledAttribute

PhonePC/2in1TabletTVWearable

applyDisabledAttribute?(instance: T): void

组件禁用状态的样式。参考[示例6（组件绑定modifier禁用状态的样式）](ts-universal-attributes-attribute-modifier.md#示例6组件绑定modifier禁用状态的样式)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instance | T | 是 | 组件的属性类，用来标识进行属性设置的组件的类型，比如[Button](ts-basic-components-button.md)组件的[ButtonAttribute](ts-basic-components-button.md#属性)，[Text](ts-basic-components-text.md)组件的[TextAttribute](ts-basic-components-text.md#属性)等。 |

### applySelectedAttribute

PhonePC/2in1TabletTVWearable

applySelectedAttribute?(instance: T): void

组件选中状态的样式。

开发者可根据需要自定义实现这些方法，通过传入的参数识别组件类型，对instance设置属性，支持使用if/else语法进行动态设置。参考[示例7（组件绑定modifier选中状态样式）](ts-universal-attributes-attribute-modifier.md#示例7组件绑定modifier选中状态样式)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instance | T | 是 | 组件的属性类，用来标识进行属性设置的组件的类型，比如[Button](ts-basic-components-button.md)组件的[ButtonAttribute](ts-basic-components-button.md#属性)，[Text](ts-basic-components-text.md)组件的[TextAttribute](ts-basic-components-text.md#属性)等。 |

**instance参数支持范围：**

[AlphabetIndexerAttribute](ts-container-alphabet-indexer.md#属性)、[BadgeAttribute](ts-container-badge.md#属性)、[BlankAttribute](ts-basic-components-blank.md#属性)、[ButtonAttribute](ts-basic-components-button.md#属性)、[CalendarPickerAttribute](ts-basic-components-calendarpicker.md#属性)、[CanvasAttribute](ts-components-canvas-canvas.md#属性)、[CheckboxAttribute](ts-basic-components-checkbox.md#属性)、[CheckboxGroupAttribute](ts-basic-components-checkboxgroup.md#属性)、[CircleAttribute](ts-drawing-components-circle.md#属性)、[ColumnAttribute](ts-container-column.md#属性)、[ColumnSplitAttribute](ts-container-columnsplit.md#属性)、[CommonAttribute](ts-component-general-attributes.md)、[CounterAttribute](ts-container-counter.md#属性)、[DataPanelAttribute](ts-basic-components-datapanel.md#属性)、[DatePickerAttribute](ts-basic-components-datepicker.md#属性)、[DividerAttribute](ts-basic-components-divider.md#属性)、[EllipseAttribute](ts-drawing-components-ellipse.md#属性)、[FlexAttribute](ts-container-flex.md#属性)、[FlowItemAttribute](ts-container-flowitem.md#属性)、[FormLinkAttribute](ts-container-formlink.md#属性)、[GaugeAttribute](ts-basic-components-gauge.md#属性)、[GridAttribute](ts-container-grid.md#属性)、[GridColAttribute](ts-container-gridcol.md#属性)、[GridItemAttribute](ts-container-griditem.md#属性)、[GridRowAttribute](ts-container-gridrow.md#属性)、[HyperlinkAttribute](ts-container-hyperlink.md#属性)、[IndicatorComponentAttribute](ts-swiper-components-indicator.md#属性)、[ImageAttribute](ts-basic-components-image.md#属性)、[ImageAnimatorAttribute](ts-basic-components-imageanimator.md#属性)、[ImageSpanAttribute](ts-basic-components-imagespan.md#属性)、[ContainerSpanAttribute](ts-basic-components-containerspan.md#属性)、[LineAttribute](ts-drawing-components-line.md#属性)、[ListAttribute](ts-container-list.md#属性)、[ListItemAttribute](ts-container-listitem.md#属性)、[ListItemGroupAttribute](ts-container-listitemgroup.md#属性)、[LoadingProgressAttribute](ts-basic-components-loadingprogress.md#属性)、[MarqueeAttribute](ts-basic-components-marquee.md#属性)、[MenuAttribute](ts-basic-components-menu.md#属性)、[MenuItemAttribute](ts-basic-components-menuitem.md#属性)、[MenuItemGroupAttribute](ts-basic-components-menuitemgroup.md)、[NavDestinationAttribute](ts-basic-components-navdestination.md#属性)、[NavigationAttribute](ts-basic-components-navigation.md#属性)、[NavigatorAttribute](ts-container-navigator.md#属性)、[NavRouterAttribute](ts-basic-components-navrouter.md#属性)、[PanelAttribute](ts-container-panel.md#属性)、[PathAttribute](ts-drawing-components-path.md#属性)、[PatternLockAttribute](ts-basic-components-patternlock.md#属性)、[PolygonAttribute](ts-drawing-components-polygon.md#属性)、[PolylineAttribute](ts-drawing-components-polyline.md#属性)、[ProgressAttribute](ts-basic-components-progress.md#属性)、[QRCodeAttribute](ts-basic-components-qrcode.md#属性)、[RadioAttribute](ts-basic-components-radio.md#属性)、[RatingAttribute](ts-basic-components-rating.md#属性)、[RectAttribute](ts-drawing-components-rect.md#属性)、[RefreshAttribute](ts-container-refresh.md#属性)、[RelativeContainerAttribute](ts-container-relativecontainer.md#属性)、[RichEditorAttribute](ts-basic-components-richeditor.md#属性)、[RichTextAttribute](ts-basic-components-richtext.md#属性)、[RowAttribute](ts-container-row.md#属性)、[RowSplitAttribute](ts-container-rowsplit.md#属性)、[ScrollAttribute](ts-container-scroll.md#属性)、[ScrollBarAttribute](ts-basic-components-scrollbar.md#属性)、[SearchAttribute](ts-basic-components-search.md#属性)、[SelectAttribute](ts-basic-components-select.md#属性)、[ShapeAttribute](ts-drawing-components-shape.md#属性)、[SideBarContainerAttribute](ts-container-sidebarcontainer.md#属性)、[SliderAttribute](ts-basic-components-slider.md#属性)、[SpanAttribute](ts-basic-components-span.md#属性)、[SymbolSpanAttribute](ts-basic-components-symbolspan.md#属性)、[StackAttribute](ts-container-stack.md#属性)、[StepperAttribute](ts-basic-components-stepper.md#属性)、[StepperItemAttribute](ts-basic-components-stepperitem.md#属性)、[SwiperAttribute](ts-container-swiper.md#属性)、[SymbolGlyphAttribute](ts-basic-components-symbolglyph.md#属性)、[TabContentAttribute](ts-container-tabcontent.md#属性)、[TabsAttribute](ts-container-tabs.md#属性)、[TextAttribute](ts-basic-components-text.md#属性)、[TextAreaAttribute](ts-basic-components-textarea.md#属性)、[TextClockAttribute](ts-basic-components-textclock.md#属性)、[TextInputAttribute](ts-basic-components-textinput.md#属性)、[TextPickerAttribute](ts-basic-components-textpicker.md#属性)、[TextTimerAttribute](ts-basic-components-texttimer.md#属性)、[TimePickerAttribute](ts-basic-components-timepicker.md#属性)、[ToggleAttribute](ts-basic-components-toggle.md#属性)、[VideoAttribute](ts-media-components-video.md#属性)、[WaterFlowAttribute](ts-container-waterflow.md#属性)、[XComponentAttribute](ts-basic-components-xcomponent.md#属性)、[ParticleAttribute](ts-particle-animation.md#属性)、[UIPickerComponentAttribute](ts-container-ui-picker-component.md#属性)22+。

说明

* StepperAttribute从API version 22开始废弃，建议使用SwiperAttribute替代。
* StepperItemAttribute从API version 22开始废弃，建议使用SwiperAttribute替代。
* NavigatorAttribute从API version 20开始废弃，建议使用NavigationAttribute替代。
* NavRouterAttribute从API version 20开始废弃，建议使用NavigationAttribute替代。
* PanelAttribute从API version 20开始废弃，推荐使用通用属性bindSheet。

**属性支持范围：**

1. 不支持入参或者返回值为[CustomBuilder](ts-types.md#custombuilder8)的属性。
2. 不支持入参为[modifier](../harmonyos-guides/arkts-user-defined-modifier.md)类型的属性，具体为以下属性方法：[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)，[drawModifier](ts-universal-attributes-draw-modifier.md)和[gestureModifier](ts-universal-attributes-gesture-modifier.md)。
3. 不支持[animation](ts-animatorproperty.md)属性。
4. 不支持[gesture](../harmonyos-guides/arkts-gesture-events-binding.md)类型的属性。
5. 不支持[stateStyles](ts-universal-attributes-polymorphic-style.md)属性。
6. 不支持已废弃属性。

不支持或者未实现的属性在使用时会抛出"Method not implemented."、"is not callable"、"Builder is not supported."等异常信息。具体Modifier支持范围可参考[属性或事件对attributemodifier的支持情况](../harmonyos-guides/arkts-user-defined-extension-attributemodifier.md#属性或事件对attributemodifier的支持情况)。

## 自定义Modifier

PhonePC/2in1TabletTVWearable

从API version 12开始，开发者可使用自定义Modifier构建组件并配置属性，通过此自定义的Modifier可调用所封装组件的属性和样式接口。

**自定义Modifier支持范围：**

CommonModifier、ColumnModifier、ColumnSplitModifier、RowModifier、RowSplitModifier、SideBarContainerModifier、BlankModifier、DividerModifier、GridColModifier、GridRowModifier、NavDestinationModifier、NavigatorModifier、StackModifier、NavigationModifier、NavRouterModifier、StepperItemModifier、StepperModifier20+、TabsModifier、GridModifier、GridItemModifier、ListModifier、ListItemModifier、ListItemGroupModifier、ScrollModifier、SwiperModifier、WaterFlowModifier、ButtonModifier、CounterModifier、TextPickerModifier、TimePickerModifier、ToggleModifier、CalendarPickerModifier、CheckboxModifier、CheckboxGroupModifier、DatePickerModifier、RadioModifier、RatingModifier、SelectModifier、SliderModifier、PatternLockModifier、SpanModifier、SymbolSpanModifier、ContainerSpanModifier、RichEditorModifier、RefreshModifier、SearchModifier、TextAreaModifier、TextModifier、TextInputModifier、ImageSpanModifier、ImageAnimatorModifier、ImageModifier、VideoModifier、DataPanelModifier、GaugeModifier、LoadingProgressModifier、MarqueeModifier、ProgressModifier、QRCodeModifier、TextClockModifier、TextTimerModifier、LineModifier、PathModifier、PolygonModifier、PolylineModifier、RectModifier、ShapeModifier、AlphabetIndexerModifier、FormComponentModifier、HyperlinkModifier、MenuModifier、MenuItemModifier、PanelModifier、SymbolGlyphModifier、ParticleModifier、UIPickerComponentModifier22+。

未暴露的组件Modifier可以使用CommonModifier。

说明

* StepperModifier从API version 22开始废弃，建议使用SwiperModifier替代。
* StepperItemModifier从API version 22开始废弃，建议使用SwiperModifier替代。
* NavigatorModifier从API version 20开始废弃，建议使用NavigationModifier替代。
* NavRouterModifier从API version 20开始废弃，建议使用NavigationModifier替代。
* PanelModifier从API version 20开始废弃，推荐使用通用属性bindSheet。

**注意事项**

1. 设置自定义Modifier给一个组件，该组件对应属性生效。
2. 自定义Modifier属性值变化，组件对应属性也会变化。自定义Modifier类型为基类，构造的对象为子类对象，使用时要通过as进行类型断言为子类。
3. 一个自定义Modifier设置给两个组件，Modifier属性变化的时候对两个组件同时生效。
4. 一个Modifier设置了属性A和属性B，再设置属性C和属性D，4个属性同时在组件上生效。
5. 自定义Modifier不支持@State标注的状态数据的变化感知，见[示例3（自定义Modifier不支持感知@State装饰的状态数据变化）](ts-universal-attributes-attribute-modifier.md#示例3自定义modifier不支持感知state装饰的状态数据变化)。
6. 多次通过attributeModifier设置属性时，生效的属性为所有属性的并集，相同属性按照设置顺序生效。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（组件绑定Modifier切换背景颜色）

该示例通过Button绑定Modifier实现了点击切换背景颜色的效果。

```
1. // xxx.ets
2. // 设置Button组件属性的自定义AttributeModifier
3. class MyButtonModifier implements AttributeModifier<ButtonAttribute> {
4. public isDark: boolean = false;

6. applyNormalAttribute(instance: ButtonAttribute): void {
7. if (this.isDark) {
8. instance.backgroundColor(Color.Black);
9. } else {
10. instance.backgroundColor(Color.Red);
11. }
12. }
13. }

15. @Entry
16. @Component
17. struct attributeDemo {
18. @State modifier: MyButtonModifier = new MyButtonModifier();

20. build() {
21. Row() {
22. Column() {
23. Button("Button")
24. .attributeModifier(this.modifier)
25. .onClick(() => {
26. this.modifier.isDark = !this.modifier.isDark;
27. })
28. }
29. .width('100%')
30. }
31. .height('100%')
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/_TNJnVPQQDuArOjm6nzFKw/zh-cn_image_0000002558766094.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055129Z&HW-CC-Expire=86400&HW-CC-Sign=477EB92A4818FF6271A526391D3CB7D4022809083EF10DD9E2E0A2AB4B232416)

### 示例2（组件绑定Modifier实现按压态效果）

该示例通过Button绑定Modifier实现了按压态的效果。如果配合状态管理V2使用，详情见：[Modifier与makeObserved](../harmonyos-guides/arkts-v1-v2-migration-inner-object.md#modifier)。

```
1. // xxx.ets
2. // 设置Button组件属性的自定义AttributeModifier
3. class MyButtonModifier implements AttributeModifier<ButtonAttribute> {
4. applyNormalAttribute(instance: ButtonAttribute): void {
5. instance.backgroundColor(Color.Black);
6. }

8. applyPressedAttribute(instance: ButtonAttribute): void {
9. instance.backgroundColor(Color.Red);
10. }
11. }

13. @Entry
14. @Component
15. struct attributePressedDemo {
16. @State modifier: MyButtonModifier = new MyButtonModifier();

18. build() {
19. Row() {
20. Column() {
21. Button("Button")
22. .attributeModifier(this.modifier)
23. }
24. .width('100%')
25. }
26. .height('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/4kACcR0kS6mM_RN4Q9iGiA/zh-cn_image_0000002558766094.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055129Z&HW-CC-Expire=86400&HW-CC-Sign=91F382221F5D62B53152AC1797033CF08CA4BD0783B065FCE1772B401B8F4535)

### 示例3（自定义Modifier不支持感知@State装饰的状态数据变化）

该示例通过状态数据设置自定义Modifier的宽度，自定义Modifier不支持感知@State装饰的状态数据变化，点击按钮后宽度不发生改变。

```
1. import { CommonModifier } from "@kit.ArkUI";

3. const TEST_TAG: string = "AttributeModifier";

5. // 设置通用组件属性的自定义AttributeModifier
6. class MyModifier extends CommonModifier {
7. applyNormalAttribute(instance: CommonAttribute): void {
8. super.applyNormalAttribute?.(instance);
9. }
10. }

12. @Component
13. struct MyImage1 {
14. @Link modifier: CommonModifier;

16. build() {
17. Image($r("app.media.startIcon")).attributeModifier(this.modifier as MyModifier)
18. }
19. }

21. @Entry
22. @Component
23. struct Index {
24. index: number = 0;
25. @State width1: number = 100;
26. @State height1: number = 100;
27. @State myModifier: CommonModifier = new MyModifier().width(this.width1).height(this.height1).margin(10);

29. build() {
30. Column() {
31. Button($r("app.string.EntryAbility_label"))
32. .margin(10)
33. .onClick(() => {
34. console.info(TEST_TAG, "onClick");
35. this.index++;
36. if (this.index % 2 === 1) {
37. this.width1 = 10;
38. console.info(TEST_TAG, "setGroup1");
39. } else {
40. this.height1 = 10;
41. console.info(TEST_TAG, "setGroup2");
42. }
43. })
44. MyImage1({ modifier: this.myModifier })
45. }
46. .width('100%')
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/5Ff0i2kkSdCAclqRaxoSlg/zh-cn_image_0000002558606436.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055129Z&HW-CC-Expire=86400&HW-CC-Sign=89DBC7376BA90DD93E06B004B8DD2E2A3EC1F8D86E1188881F8D6AD053189652)

### 示例4（Modifier和自定义Modifier的属性同时生效）

该示例通过自定义Modifier设置了width和height，点击按钮时设置[borderStyle](ts-appendix-enums.md#borderstyle)和[borderWidth](ts-universal-attributes-border.md#borderwidth)，点击后4个属性同时生效。

```
1. import { CommonModifier } from "@kit.ArkUI";

3. const TEST_TAG: string = "AttributeModifier";

5. // 设置通用组件属性的自定义AttributeModifier
6. class MyModifier extends CommonModifier {
7. applyNormalAttribute(instance: CommonAttribute): void {
8. super.applyNormalAttribute?.(instance);
9. }

11. public setGroup1(): void {
12. this.borderStyle(BorderStyle.Dotted);
13. this.borderWidth(8);
14. }

16. public setGroup2(): void {
17. this.borderStyle(BorderStyle.Dashed);
18. this.borderWidth(8);
19. }
20. }

22. @Component
23. struct MyImage1 {
24. @Link modifier: CommonModifier;

26. build() {
27. Image($r("app.media.startIcon")).attributeModifier(this.modifier as MyModifier)
28. }
29. }

31. @Entry
32. @Component
33. struct Index {
34. @State myModifier: CommonModifier = new MyModifier().width(100).height(100).margin(10);
35. index: number = 0;

37. build() {
38. Column() {
39. Button($r("app.string.EntryAbility_label"))
40. .margin(10)
41. .onClick(() => {
42. console.info(TEST_TAG, "onClick");
43. this.index++;
44. if (this.index % 2 === 1) {
45. (this.myModifier as MyModifier).setGroup1();
46. console.info(TEST_TAG, "setGroup1");
47. } else {
48. (this.myModifier as MyModifier).setGroup2();
49. console.info(TEST_TAG, "setGroup2");
50. }
51. })
52. MyImage1({ modifier: this.myModifier })
53. }
54. .width('100%')
55. }
56. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/ItYamWpUQXmNBNFPLQoryQ/zh-cn_image_0000002589325963.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055129Z&HW-CC-Expire=86400&HW-CC-Sign=711226CA85B013C11953413AE654DC7DDCA84762CD526DD1DA212DFF8AB2A208)

### 示例5（组件绑定Modifier获焦样式）

该示例通过Button绑定Modifier实现了组件在获得焦点时的样式效果。点击Button2后，Button会显示获得焦点后的样式。

```
1. // 设置Button组件属性的自定义AttributeModifier
2. class MyButtonModifier implements AttributeModifier<ButtonAttribute> {

4. applyNormalAttribute(instance: ButtonAttribute): void {
5. instance.backgroundColor(Color.Blue);
6. }
7. applyFocusedAttribute(instance: ButtonAttribute): void {
8. instance.backgroundColor(Color.Green);
9. }
10. }

12. @Entry
13. @Component
14. struct attributeDemo {
15. @State modifier: MyButtonModifier = new MyButtonModifier();
16. @State isDisable: boolean = true;

18. build() {
19. Row() {
20. Column() {
21. Button("Button")
22. .attributeModifier(this.modifier)
23. .enabled(this.isDisable)
24. .id("app")
25. Divider().vertical(false).strokeWidth(15).color(Color.Transparent)
26. Button("Button2")
27. .onClick(() => {
28. this.getUIContext().getFocusController().activate(true);
29. this.getUIContext().getFocusController().requestFocus("app");
30. })
31. }
32. .width('100%')
33. }
34. .height('100%')
35. }
36. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/siyo_mmnQAWy1-tipwXwdQ/zh-cn_image_0000002589245905.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055129Z&HW-CC-Expire=86400&HW-CC-Sign=4C8A2583454CCA77D41AC5A8D49B70DE374DF58CACE205593538CC3D4BC40026)

### 示例6（组件绑定Modifier禁用状态的样式）

该示例通过Button绑定Modifier实现了组件禁用时的样式效果。点击Button2后，Button会显示禁用状态的样式。

```
1. // 设置Button组件属性的自定义AttributeModifier
2. class MyButtonModifier implements AttributeModifier<ButtonAttribute> {
3. applyDisabledAttribute(instance: ButtonAttribute): void {
4. instance.width(200);
5. }
6. }

8. @Entry
9. @Component
10. struct attributeDemo {
11. @State modifier: MyButtonModifier = new MyButtonModifier();
12. @State isDisable: boolean = true;

14. build() {
15. Row() {
16. Column() {
17. Button("Button")
18. .attributeModifier(this.modifier)
19. .enabled(this.isDisable)
20. Divider().vertical(false).strokeWidth(15).color(Color.Transparent)
21. Button("Button2")
22. .onClick(() => {
23. this.isDisable = !this.isDisable;
24. })
25. }
26. .width('100%')
27. }
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/WTNdLlqhSGezWpsfDM-vWA/zh-cn_image_0000002558766096.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055129Z&HW-CC-Expire=86400&HW-CC-Sign=1E312D7C2BF3CFB07C0AC5FF794C937061FCC54A2E34C33BA56FA19801CE0603)

### 示例7（组件绑定Modifier选中状态样式）

该示例通过Radio绑定Modifier实现了展示组件选中时样式的效果。

```
1. // 设置Radio组件属性的自定义AttributeModifier
2. class MyRadioModifier implements AttributeModifier<RadioAttribute> {
3. applyNormalAttribute(instance: RadioAttribute): void {
4. instance.backgroundColor(Color.Blue);
5. }

7. applySelectedAttribute(instance: RadioAttribute): void {
8. instance.backgroundColor(Color.Red);
9. instance.borderWidth(2);
10. }
11. }

13. @Entry
14. @Component
15. struct attributeDemo {
16. @State modifier: MyRadioModifier = new MyRadioModifier();
17. @State value: boolean = false;
18. @State value2: boolean = false;

20. build() {
21. Row() {
22. Column() {
23. Radio({ value: 'Radio1', group: 'radioGroup1' })
24. .checked(this.value)
25. .height(50)
26. .width(50)
27. .borderWidth(0)
28. .borderRadius(30)
29. .onClick(() => {
30. this.value = !this.value;
31. })
32. .attributeModifier(this.modifier)
33. }
34. .width('100%')
35. }
36. .height('100%')
37. }
38. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/BSDXvl3NSZeH4uSpASATDQ/zh-cn_image_0000002558606438.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055129Z&HW-CC-Expire=86400&HW-CC-Sign=BC19D17F975DDC0AE972EAC4AAFE0B7EC455E4EDC97A7872956532818BD9E5E8)

### 示例8（自定义组件绑定Modifier实现按压态效果）

该示例通过Common（自定义）绑定Modifier实现了按压态的效果。

```
1. // xxx.ets
2. // 设置自定义组件属性的自定义AttributeModifier
3. class CustomModifier implements AttributeModifier<CommonAttribute> {
4. applyNormalAttribute(instance: CommonAttribute): void {
5. instance.backgroundColor(Color.Blue)
6. }

8. applyPressedAttribute(instance: CommonAttribute): void {
9. instance.backgroundColor(Color.Gray)
10. }
11. }

13. @Entry
14. @Component
15. struct attributePressedDemo {
16. @State modifier: CustomModifier = new CustomModifier()

18. build() {
19. Row() {
20. Column() {
21. ChildComponent()
22. .attributeModifier(this.modifier)
23. }
24. .width('100%')
25. }
26. .height('100%')
27. }
28. }

30. // 自定义组件
31. @Component
32. struct ChildComponent {
33. build() {
34. Text("common")
35. .fontColor(Color.White)
36. .fontSize(28)
37. .textAlign(TextAlign.Center)
38. .width('35%')
39. .height('10%')
40. }
41. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/FGkMXorKTHCDaiLHI54bmA/zh-cn_image_0000002589325965.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055129Z&HW-CC-Expire=86400&HW-CC-Sign=8EC9EFF584C041E0100AD699DBFAFA0D8266679F71E86D1C7ADB1A0DCBDD6D61)
