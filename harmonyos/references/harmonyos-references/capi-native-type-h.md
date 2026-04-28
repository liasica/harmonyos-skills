---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h
title: native_type.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_type.h
category: harmonyos-references
scraped_at: 2026-04-28T08:03:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:759c8326125dac16cd99015465d8252e7f4b8df6971727d6892ee7fa29feb6ce
---

## 概述

PhonePC/2in1TabletTVWearable

提供NativeModule公共的类型定义。

**引用文件：** <arkui/native\_type.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [NativeTypeSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeTypeSample)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_Node](capi-arkui-nativemodule-arkui-node-descriptor.md) | ArkUI\_Node | 定义ArkUI native组件实例对象。 |
| [ArkUI\_ContextCallback](capi-arkui-nativemodule-arkui-contextcallback.md) | ArkUI\_ContextCallback | 事件回调类型。 |
| [ArkUI\_NumberValue](capi-arkui-nativemodule-arkui-numbervalue.md) | ArkUI\_NumberValue | ArkUI在Native侧的数字类型定义。 |
| [ARKUI\_TextPickerRangeContent](pi-arkui-nativemodule-arkui-textpickerrangecontent.md) | ARKUI\_TextPickerRangeContent | 定义单列滑动数据选择器支持的图片资源结构体。 |
| [ARKUI\_TextPickerCascadeRangeContent](i-nativemodule-arkui-textpickercascaderangecontent.md) | ARKUI\_TextPickerCascadeRangeContent | 定义多列联动滑动数据选择器的结构体。 |
| [ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md) | ArkUI\_ColorStop | 定义渐变色结构。 |
| [ArkUI\_Rect](capi-arkui-nativemodule-arkui-rect.md) | ArkUI\_Rect | 定义遮罩屏蔽区域的范围结构体。 |
| [ArkUI\_IntSize](capi-arkui-nativemodule-arkui-intsize.md) | ArkUI\_IntSize | 尺寸类型，用于描述组件的宽高。 |
| [ArkUI\_IntOffset](capi-arkui-nativemodule-arkui-intoffset.md) | ArkUI\_IntOffset | 位置，用于描述组件的位置。 |
| [ArkUI\_Margin](capi-arkui-nativemodule-arkui-margin.md) | ArkUI\_Margin | 外边距属性，用于描述组件的外边距属性。 |
| [ArkUI\_TranslationOptions](capi-arkui-nativemodule-arkui-translationoptions.md) | ArkUI\_TranslationOptions | 定义组件转场时的平移效果对象。 |
| [ArkUI\_ScaleOptions](capi-arkui-nativemodule-arkui-scaleoptions.md) | ArkUI\_ScaleOptions | 定义组件转场时的缩放效果对象。 |
| [ArkUI\_RotationOptions](capi-arkui-nativemodule-arkui-rotationoptions.md) | ArkUI\_RotationOptions | 定义组件转场时的旋转效果对象。 |
| [ArkUI\_NativeDialog](capi-arkui-nativemodule-arkui-nativedialog.md) | ArkUI\_NativeDialog | 提供ArkUI在Native侧的自定义弹窗控制器对象定义。 |
| [ArkUI\_LayoutConstraint](capi-arkui-nativemodule-arkui-layoutconstraint.md) | ArkUI\_LayoutConstraint | 布局约束，组件布局时，进行尺寸范围限制。 |
| [ArkUI\_DrawContext](capi-arkui-nativemodule-arkui-drawcontext.md) | ArkUI\_DrawContext | 定义组件绘制上下文类型结构。 |
| [ArkUI\_Node\*](capi-arkui-nativemodule-arkui-node8h.md) | ArkUI\_NodeHandle | 定义ArkUI native组件实例对象指针定义。 |
| [ArkUI\_NativeDialog\*](capi-arkui-nativemodule-arkui-nativedialog8h.md) | ArkUI\_NativeDialogHandle | 定义ArkUI在Native侧的自定义弹窗控制器对象指针。 |
| [ArkUI\_GridItemSize](capi-arkui-nativemodule-arkui-griditemsize.md) | ArkUI\_GridItemSize | 定义Grid布局选项onGetIrregularSizeByIndex回调返回值结构体。 |
| [ArkUI\_GridItemRect](capi-arkui-nativemodule-arkui-griditemrect.md) | ArkUI\_GridItemRect | 定义Grid布局选项onGetRectByIndex回调返回值结构体。 |
| [ArkUI\_GridLayoutOptions](capi-arkui-nativemodule-arkui-gridlayoutoptions.md) | ArkUI\_GridLayoutOptions | 定义Grid布局选项。 |
| [ArkUI\_WaterFlowSectionOption](pi-arkui-nativemodule-arkui-waterflowsectionoption.md) | ArkUI\_WaterFlowSectionOption | 定义[FlowItem](ts-container-flowitem.md)分组配置信息。 |
| [ArkUI\_ListItemSwipeActionItem](i-arkui-nativemodule-arkui-listitemswipeactionitem.md) | ArkUI\_ListItemSwipeActionItem | 定义ListItemSwipeActionOption方法内Item的配置信息。 |
| [ArkUI\_ListItemSwipeActionOption](arkui-nativemodule-arkui-listitemswipeactionoption.md) | ArkUI\_ListItemSwipeActionOption | 定义ListItemSwipeActionOption方法的配置信息。 |
| [ArkUI\_Context](capi-arkui-nativemodule-arkui-context.md) | ArkUI\_Context | 定义ArkUI native UI的上下文实例对象。 |
| [ArkUI\_Context\*](capi-arkui-nativemodule-arkui-context8h.md) | ArkUI\_ContextHandle | 定义ArkUI native UI的上下文实例对象指针定义。 |
| [ArkUI\_NodeContent\*](capi-arkui-nativemodule-arkui-nodecontent8h.md) | ArkUI\_NodeContentHandle | 定义ArkUI NodeContent实例在Native侧的实例对象指针定义。 |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md) | ArkUI\_AlignmentRuleOption | 指定设置在相对容器中子组件的对齐规则。 |
| [ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md) | ArkUI\_GuidelineOption | guideLine参数，用于定义guideline的id、方向和位置。 |
| [ArkUI\_BarrierOption](capi-arkui-nativemodule-arkui-barrieroption.md) | ArkUI\_BarrierOption | barrier参数，用于定义barrier的id、方向和生成时所依赖的组件。 |
| [ArkUI\_ImageAnimatorFrameInfo](pi-arkui-nativemodule-arkui-imageanimatorframeinfo.md) | ArkUI\_ImageAnimatorFrameInfo | 定义图片帧信息。 |
| [ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md) | ArkUI\_ListChildrenMainSize | 定义List的ChildrenMainSize类信息。 |
| [ArkUI\_ProgressLinearStyleOption](arkui-nativemodule-arkui-progresslinearstyleoption.md) | ArkUI\_ProgressLinearStyleOption | 定义线性进度条样式。 |
| [ArkUI\_CustomProperty](capi-arkui-nativemodule-arkui-customproperty.md) | ArkUI\_CustomProperty | 定义自定义属性的CustomProperty类信息。 |
| [ArkUI\_HostWindowInfo](capi-arkui-nativemodule-arkui-hostwindowinfo.md) | ArkUI\_HostWindowInfo | 定义窗口属性的HostWindowInfo类信息。 |
| [ArkUI\_ActiveChildrenInfo](capi-arkui-nativemodule-arkui-activechildreninfo.md) | ArkUI\_ActiveChildrenInfo | 定义ActiveChildrenInfo类信息。 |
| [ArkUI\_CrossLanguageOption](capi-arkui-nativemodule-arkui-crosslanguageoption.md) | ArkUI\_CrossLanguageOption | 定义跨语言配置项。 |
| [AbilityBase\_Want](capi-arkui-nativemodule-abilitybase-want.md) | AbilityBase\_Want | 声明元能力want结构。 |
| [ArkUI\_EmbeddedComponentOption](i-arkui-nativemodule-arkui-embeddedcomponentoption.md) | ArkUI\_EmbeddedComponentOption | 为EmbeddedComponent定义参数EmbeddedComponentOption。 |
| [ArkUI\_AccessibilityState](capi-arkui-nativemodule-arkui-accessibilitystate.md) | ArkUI\_AccessibilityState | 定义组件无障碍状态。 |
| [ArkUI\_AccessibilityValue](capi-arkui-nativemodule-arkui-accessibilityvalue.md) | ArkUI\_AccessibilityValue | 定义组件无障碍信息值。 |
| [ArkUI\_SystemFontStyleEvent](capi-arkui-nativemodule-arkui-systemfontstyleevent.md) | ArkUI\_SystemFontStyleEvent | 系统字体变更事件定义。 |
| [ArkUI\_CustomSpanMeasureInfo](api-arkui-nativemodule-arkui-customspanmeasureinfo.md) | ArkUI\_CustomSpanMeasureInfo | 自定义段落组件的测量信息。 |
| [ArkUI\_CustomSpanMetrics](capi-arkui-nativemodule-arkui-customspanmetrics.md) | ArkUI\_CustomSpanMetrics | 自定义段落组件的度量指标。 |
| [ArkUI\_CustomSpanDrawInfo](capi-arkui-nativemodule-arkui-customspandrawinfo.md) | ArkUI\_CustomSpanDrawInfo | 自定义段落组件的绘制信息。 |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md) | ArkUI\_SwiperIndicator | 定义[Swiper](ts-container-swiper.md)组件的导航指示器风格。 |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md) | ArkUI\_SwiperDigitIndicator | 定义Swiper组件的数字导航指示器风格。 |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md) | ArkUI\_SwiperArrowStyle | 定义Swiper组件的导航箭头风格。 |
| [ArkUI\_StyledString\_Descriptor](i-arkui-nativemodule-arkui-styledstring-descriptor.md) | ArkUI\_StyledString\_Descriptor | 定义文本组件支持的属性字符串的数据对象。 |
| [ArkUI\_SnapshotOptions](capi-arkui-nativemodule-arkui-snapshotoptions.md) | ArkUI\_SnapshotOptions | 定义截图的可选项。 |
| [ArkUI\_TextPickerRangeContentArray](kui-nativemodule-arkui-textpickerrangecontentarray.md) | ArkUI\_TextPickerRangeContentArray | 定义文本选择器的数据选择列表。 |
| [ArkUI\_TextCascadePickerRangeContentArray](ivemodule-arkui-textcascadepickerrangecontentarray.md) | ArkUI\_TextCascadePickerRangeContentArray | 定义多列联动数据选择器的多列联动数据选择列表。 |
| [ArkUI\_SelectionOptions](capi-arkui-nativemodule-arkui-selectionoptions.md) | ArkUI\_SelectionOptions | 定义选择操作的相关选项。 |
| [ArkUI\_VisibleAreaEventOptions](i-arkui-nativemodule-arkui-visibleareaeventoptions.md) | ArkUI\_VisibleAreaEventOptions | 可见区域变化监听的参数。 |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md) | ArkUI\_PositionEdges | 相对容器内容区边界的位置参数。 |
| [ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md) | ArkUI\_PixelRoundPolicy | 定义组件的像素取整策略结构体。 |
| [ArkUI\_ContentTransitionEffect](i-arkui-nativemodule-arkui-contenttransitioneffect.md) | ArkUI\_ContentTransitionEffect | 内容过渡效果。 |
| [ArkUI\_ShowCounterConfig](api-arkui-nativemodule-arkui-textshowcounterconfig.md) | ArkUI\_ShowCounterConfig | 定义文本输入框的计数器配置。 |
| [ArkUI\_TextContentBaseController](arkui-nativemodule-arkui-textcontentbasecontroller.md) | ArkUI\_TextContentBaseController | 定义文本内容基础控制器。 |
| [ArkUI\_TextMenuItem](capi-arkui-nativemodule-arkui-textmenuitem.md) | ArkUI\_TextMenuItem | 定义文本菜单项结构体。 |
| [ArkUI\_TextMenuItemArray](capi-arkui-nativemodule-arkui-textmenuitemarray.md) | ArkUI\_TextMenuItemArray | 定义文本菜单项数组结构体。 |
| [ArkUI\_TextEditMenuOptions](capi-arkui-nativemodule-arkui-texteditmenuoptions.md) | ArkUI\_TextEditMenuOptions | 定义文本菜单扩展项结构体。 |
| [ArkUI\_TextSelectionMenuOptions](-arkui-nativemodule-arkui-textselectionmenuoptions.md) | ArkUI\_TextSelectionMenuOptions | 定义自定义文本选择菜单结构体。 |
| [ArkUI\_SelectedDragPreviewStyle](ui-nativemodule-arkui-textselecteddragpreviewstyle.md) | ArkUI\_SelectedDragPreviewStyle | 定义选中状态下文本拖拽预览样式。 |
| [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md) | ArkUI\_MotionPathOptions | 定义路径动画的运动路径配置项。 |
| [ArkUI\_PickerIndicatorBackground](arkui-nativemodule-arkui-pickerindicatorbackground.md) | ArkUI\_PickerIndicatorBackground | 背景样式指示器的样式参数。 |
| [ArkUI\_PickerIndicatorDivider](pi-arkui-nativemodule-arkui-pickerindicatordivider.md) | ArkUI\_PickerIndicatorDivider | 分割线样式指示器的样式参数。 |
| [ArkUI\_PickerIndicatorStyle](capi-arkui-nativemodule-arkui-pickerindicatorstyle.md) | ArkUI\_PickerIndicatorStyle | 选中项指示器的样式。 |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md) | ArkUI\_TextMarqueeOptions | 定义文本跑马灯模式配置项。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_Alignment](capi-native-type-h.md#arkui_alignment) | ArkUI\_Alignment | 定义布局对齐枚举值。 |
| [ArkUI\_ImageRepeat](capi-native-type-h.md#arkui_imagerepeat) | ArkUI\_ImageRepeat | 定义图片重复铺设枚举值。 |
| [ArkUI\_FontStyle](capi-native-type-h.md#arkui_fontstyle) | ArkUI\_FontStyle | 定义字体样式枚举值。 |
| [ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight) | ArkUI\_FontWeight | 定义字体粗细/字重枚举值。 |
| [ArkUI\_TextAlignment](capi-native-type-h.md#arkui_textalignment) | ArkUI\_TextAlignment | 定义字体水平对齐样式枚举值。 |
| [ArkUI\_TextVerticalAlignment](capi-native-type-h.md#arkui_textverticalalignment) | ArkUI\_TextVerticalAlignment | 定义文本垂直对齐样式枚举值。 |
| [ArkUI\_EnterKeyType](capi-native-type-h.md#arkui_enterkeytype) | ArkUI\_EnterKeyType | 定义单行文本输入法回车键类型枚举值。 |
| [ArkUI\_TextInputType](capi-native-type-h.md#arkui_textinputtype) | ArkUI\_TextInputType | 定义单行文本输入法类型枚举值。 |
| [ArkUI\_TextAreaType](capi-native-type-h.md#arkui_textareatype) | ArkUI\_TextAreaType | 定义多行文本输入法类型枚举值。 |
| [ArkUI\_CancelButtonStyle](capi-native-type-h.md#arkui_cancelbuttonstyle) | ArkUI\_CancelButtonStyle | 定义清除按钮样式枚举值。 |
| [ArkUI\_XComponentType](capi-native-type-h.md#arkui_xcomponenttype) | ArkUI\_XComponentType | 定义XComponent类型枚举值。 |
| [ArkUI\_ProgressType](capi-native-type-h.md#arkui_progresstype) | ArkUI\_ProgressType | 定义进度条类型枚举值。 |
| [ArkUI\_TextDecorationType](capi-native-type-h.md#arkui_textdecorationtype) | ArkUI\_TextDecorationType | 定义装饰线类型枚举值。 |
| [ArkUI\_TextDecorationStyle](capi-native-type-h.md#arkui_textdecorationstyle) | ArkUI\_TextDecorationStyle | 定义装饰线样式枚举值。 |
| [ArkUI\_TextCase](capi-native-type-h.md#arkui_textcase) | ArkUI\_TextCase | 定义文本大小写枚举值。 |
| [ArkUI\_CopyOptions](capi-native-type-h.md#arkui_copyoptions) | ArkUI\_CopyOptions | 定义文本复制粘贴模式枚举值。 |
| [ArkUI\_ShadowType](capi-native-type-h.md#arkui_shadowtype) | ArkUI\_ShadowType | 定义阴影类型枚举值。 |
| [ArkUI\_DatePickerMode](capi-native-type-h.md#arkui_datepickermode) | ArkUI\_DatePickerMode | 定义日期选择器列显示模式的枚举值。 |
| [ArkUI\_TextPickerRangeType](capi-native-type-h.md#arkui_textpickerrangetype) | ArkUI\_TextPickerRangeType | 定义滑动选择文本选择器输入类型。 |
| [ArkUI\_AccessibilityCheckedState](capi-native-type-h.md#arkui_accessibilitycheckedstate) | ArkUI\_AccessibilityCheckedState | 定义无障碍复选框状态类型枚举值。 |
| [ArkUI\_AccessibilityActionType](capi-native-type-h.md#arkui_accessibilityactiontype) | ArkUI\_AccessibilityActionType | 定义无障碍操作类型。 |
| [ArkUI\_EdgeEffect](capi-native-type-h.md#arkui_edgeeffect) | ArkUI\_EdgeEffect | 定义边缘滑动效果枚举值。 |
| [ArkUI\_BarState](capi-native-type-h.md#arkui_barstate) | ArkUI\_BarState | 定义文本控制滚动条状态枚举值。 |
| [ArkUI\_EffectEdge](capi-native-type-h.md#arkui_effectedge) | ArkUI\_EffectEdge | 定义边缘效果生效边缘的方向枚举值。 |
| [ArkUI\_ScrollDirection](capi-native-type-h.md#arkui_scrolldirection) | ArkUI\_ScrollDirection | 定义[Scroll](ts-container-scroll.md)组件排列方向枚举值。 |
| [ArkUI\_ScrollSnapAlign](capi-native-type-h.md#arkui_scrollsnapalign) | ArkUI\_ScrollSnapAlign | 定义列表项滚动结束对齐效果枚举值。 |
| [ArkUI\_ScrollBarDisplayMode](capi-native-type-h.md#arkui_scrollbardisplaymode) | ArkUI\_ScrollBarDisplayMode | 定义滚动条状态枚举值。 |
| [ArkUI\_Axis](capi-native-type-h.md#arkui_axis) | ArkUI\_Axis | 定义滚动方向和List组件排列方向枚举值。 |
| [ArkUI\_StickyStyle](capi-native-type-h.md#arkui_stickystyle) | ArkUI\_StickyStyle | 定义列表是否吸顶和吸底枚举值。 |
| [ArkUI\_ContentClipMode](capi-native-type-h.md#arkui_contentclipmode) | ArkUI\_ContentClipMode | 定义滚动容器的内容层裁剪区域枚举值。 |
| [ArkUI\_WaterFlowLayoutMode](capi-native-type-h.md#arkui_waterflowlayoutmode) | ArkUI\_WaterFlowLayoutMode | 定义[WaterFlow](ts-container-waterflow.md)组件布局模式枚举值。 |
| [ArkUI\_BorderStyle](capi-native-type-h.md#arkui_borderstyle) | ArkUI\_BorderStyle | 边框线条样式枚举值。 |
| [ArkUI\_HitTestMode](capi-native-type-h.md#arkui_hittestmode) | ArkUI\_HitTestMode | 触摸测试控制枚举值。 |
| [ArkUI\_ShadowStyle](capi-native-type-h.md#arkui_shadowstyle) | ArkUI\_ShadowStyle | 阴影效果枚举值。 |
| [ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve) | ArkUI\_AnimationCurve | 动画曲线枚举值。 |
| [ArkUI\_SwiperArrow](capi-native-type-h.md#arkui_swiperarrow) | ArkUI\_SwiperArrow | Swiper导航点箭头枚举值。 |
| [ArkUI\_SwiperNestedScrollMode](capi-native-type-h.md#arkui_swipernestedscrollmode) | ArkUI\_SwiperNestedScrollMode | Swiper组件和父组件的嵌套滚动模式。 |
| [ArkUI\_PageFlipMode](capi-native-type-h.md#arkui_pageflipmode) | ArkUI\_PageFlipMode | Swiper组件鼠标滚轮翻页模式。 |
| [ArkUI\_SwiperAnimationMode](capi-native-type-h.md#arkui_swiperanimationmode) | ArkUI\_SwiperAnimationMode | Swiper组件跳转到目标index的动画模式。 |
| [ArkUI\_AccessibilityMode](capi-native-type-h.md#arkui_accessibilitymode) | ArkUI\_AccessibilityMode | 定义无障碍辅助服务模式。 |
| [ArkUI\_TextCopyOptions](capi-native-type-h.md#arkui_textcopyoptions) | ArkUI\_TextCopyOptions | 定义组件支持设置文本是否可复制粘贴。 |
| [ArkUI\_TextHeightAdaptivePolicy](capi-native-type-h.md#arkui_textheightadaptivepolicy) | ArkUI\_TextHeightAdaptivePolicy | 定义文本自适应高度的方式。 |
| [ArkUI\_ScrollNestedMode](capi-native-type-h.md#arkui_scrollnestedmode) | ArkUI\_ScrollNestedMode | 定义嵌套滚动选项。 |
| [ArkUI\_ScrollEdge](capi-native-type-h.md#arkui_scrolledge) | ArkUI\_ScrollEdge | 定义滚动到的边缘位置。 |
| [ArkUI\_ScrollAlignment](capi-native-type-h.md#arkui_scrollalignment) | ArkUI\_ScrollAlignment | 滚动到具体item时的对齐方式。 |
| [ArkUI\_ScrollState](capi-native-type-h.md#arkui_scrollstate) | ArkUI\_ScrollState | 定义当前滚动状态。 |
| [ArkUI\_SliderBlockStyle](capi-native-type-h.md#arkui_sliderblockstyle) | ArkUI\_SliderBlockStyle | 定义滑块形状。 |
| [ArkUI\_SliderDirection](capi-native-type-h.md#arkui_sliderdirection) | ArkUI\_SliderDirection | 定义滑动条滑动方向。 |
| [ArkUI\_SliderStyle](capi-native-type-h.md#arkui_sliderstyle) | ArkUI\_SliderStyle | 定义滑块与滑轨显示样式。 |
| [ArkUI\_CheckboxShape](capi-native-type-h.md#arkui_checkboxshape) | ArkUI\_CheckboxShape | 定义CheckBox组件形状。 |
| [ArkUI\_AnimationPlayMode](capi-native-type-h.md#arkui_animationplaymode) | ArkUI\_AnimationPlayMode | 定义动画播放模式。 |
| [ArkUI\_ImageSize](capi-native-type-h.md#arkui_imagesize) | ArkUI\_ImageSize | 定义图片宽高样式。 |
| [ArkUI\_AdaptiveColor](capi-native-type-h.md#arkui_adaptivecolor) | ArkUI\_AdaptiveColor | 定义取色模式。 |
| [ArkUI\_ColorMode](capi-native-type-h.md#arkui_colormode) | ArkUI\_ColorMode | 定义深浅色模式。 |
| [ArkUI\_SystemColorMode](capi-native-type-h.md#arkui_systemcolormode) | ArkUI\_SystemColorMode | 定义系统深浅色模式。 |
| [ArkUI\_BlurStyle](capi-native-type-h.md#arkui_blurstyle) | ArkUI\_BlurStyle | 定义背景模糊样式。 |
| [ArkUI\_BlurStyleActivePolicy](capi-native-type-h.md#arkui_blurstyleactivepolicy) | ArkUI\_BlurStyleActivePolicy | 定义背景模糊激活策略。 |
| [ArkUI\_VerticalAlignment](capi-native-type-h.md#arkui_verticalalignment) | ArkUI\_VerticalAlignment | 定义垂直对齐方式。 |
| [ArkUI\_HorizontalAlignment](capi-native-type-h.md#arkui_horizontalalignment) | ArkUI\_HorizontalAlignment | 定义语言方向对齐方式。 |
| [ArkUI\_TextOverflow](capi-native-type-h.md#arkui_textoverflow) | ArkUI\_TextOverflow | 定义文本超长时的显示方式。 |
| [ArkUI\_ImageSpanAlignment](capi-native-type-h.md#arkui_imagespanalignment) | ArkUI\_ImageSpanAlignment | 定义图片基于文本的对齐方式。 |
| [ArkUI\_ObjectFit](capi-native-type-h.md#arkui_objectfit) | ArkUI\_ObjectFit | 定义[Image](ts-basic-components-image.md)组件的图片填充效果。 |
| [ArkUI\_ImageInterpolation](capi-native-type-h.md#arkui_imageinterpolation) | ArkUI\_ImageInterpolation | 定义图片插值效果。用于优化图片缩放时的锯齿问题。SVG类型图源不支持该属性。 |
| [ArkUI\_DynamicRangeMode](capi-native-type-h.md#arkui_dynamicrangemode) | ArkUI\_DynamicRangeMode | 定义图像动态范围模式（例如：SDR/HDR），用于控制图像的明暗与色彩显示范围。 |
| [ArkUI\_ImageRotateOrientation](capi-native-type-h.md#arkui_imagerotateorientation) | ArkUI\_ImageRotateOrientation | 定义图像旋转方向。 |
| [ArkUI\_BlendMode](capi-native-type-h.md#arkui_blendmode) | ArkUI\_BlendMode | 混合模式枚举值。 |
| [ArkUI\_Direction](capi-native-type-h.md#arkui_direction) | ArkUI\_Direction | 设置容器元素内主轴方向上的布局枚举值。 |
| [ArkUI\_ItemAlignment](capi-native-type-h.md#arkui_itemalignment) | ArkUI\_ItemAlignment | 设置子组件在父容器交叉轴的对齐格式枚举值。 |
| [ArkUI\_ColorStrategy](capi-native-type-h.md#arkui_colorstrategy) | ArkUI\_ColorStrategy | 前景和阴影颜色的枚举值。 |
| [ArkUI\_FlexAlignment](capi-native-type-h.md#arkui_flexalignment) | ArkUI\_FlexAlignment | 定义垂直方向对齐方式。 |
| [ArkUI\_FlexDirection](capi-native-type-h.md#arkui_flexdirection) | ArkUI\_FlexDirection | 定义Flex容器的主轴方向。 |
| [ArkUI\_FlexWrap](capi-native-type-h.md#arkui_flexwrap) | ArkUI\_FlexWrap | 定义Flex行列布局模式模式。 |
| [ArkUI\_Visibility](capi-native-type-h.md#arkui_visibility) | ArkUI\_Visibility | 控制组件的显隐枚举值。 |
| [ArkUI\_CalendarAlignment](capi-native-type-h.md#arkui_calendaralignment) | ArkUI\_CalendarAlignment | 日历选择器与入口组件对齐方式。 |
| [ArkUI\_MaskType](capi-native-type-h.md#arkui_masktype) | ArkUI\_MaskType | 遮罩类型枚举。遮罩是一种用于限制组件显示区域的手段，它利用特定的形状对组件内容进行裁剪，从而实现只有遮罩区域内的内容才可见的效果。 |
| [ArkUI\_ClipType](capi-native-type-h.md#arkui_cliptype) | ArkUI\_ClipType | 裁剪类型枚举。 |
| [ArkUI\_ShapeType](capi-native-type-h.md#arkui_shapetype) | ArkUI\_ShapeType | 自定义形状。 |
| [ArkUI\_LinearGradientDirection](capi-native-type-h.md#arkui_lineargradientdirection) | ArkUI\_LinearGradientDirection | 定义渐变方向结构。 |
| [ArkUI\_WordBreak](capi-native-type-h.md#arkui_wordbreak) | ArkUI\_WordBreak | 定义文本断行规则。 |
| [ArkUI\_EllipsisMode](capi-native-type-h.md#arkui_ellipsismode) | ArkUI\_EllipsisMode | 定义文本省略位置。 |
| [ArkUI\_ImageRenderMode](capi-native-type-h.md#arkui_imagerendermode) | ArkUI\_ImageRenderMode | 定义图片渲染模式。 |
| [ArkUI\_TransitionEdge](capi-native-type-h.md#arkui_transitionedge) | ArkUI\_TransitionEdge | 定义转场从边缘滑入和滑出的效果。 |
| [ArkUI\_FinishCallbackType](capi-native-type-h.md#arkui_finishcallbacktype) | ArkUI\_FinishCallbackType | 在动画中定义[OH\_ArkUI\_AnimatorOption\_RegisterOnFinishCallback](capi-native-animate-h.md#oh_arkui_animatoroption_registeronfinishcallback)回调的类型。 |
| [ArkUI\_ListItemAlignment](capi-native-type-h.md#arkui_listitemalignment) | ArkUI\_ListItemAlignment | 交叉轴方向的布局方式。 |
| [ArkUI\_BlendApplyType](capi-native-type-h.md#arkui_blendapplytype) | ArkUI\_BlendApplyType | 指定的混合模式应用于视图的内容选项. |
| [ArkUI\_LengthMetricUnit](capi-native-type-h.md#arkui_lengthmetricunit) | ArkUI\_LengthMetricUnit | 定义组件的单位模式。 |
| [ArkUI\_TextInputContentType](capi-native-type-h.md#arkui_textinputcontenttype) | ArkUI\_TextInputContentType | 定义自动填充类型。 |
| [ArkUI\_BarrierDirection](capi-native-type-h.md#arkui_barrierdirection) | ArkUI\_BarrierDirection | 定义屏障线的方向。 |
| [ArkUI\_RelativeLayoutChainStyle](capi-native-type-h.md#arkui_relativelayoutchainstyle) | ArkUI\_RelativeLayoutChainStyle | 定义链的风格。 |
| [ArkUI\_TextInputStyle](capi-native-type-h.md#arkui_textinputstyle) | ArkUI\_TextInputStyle | 定义输入框风格。 |
| [ArkUI\_KeyboardAppearance](capi-native-type-h.md#arkui_keyboardappearance) | ArkUI\_KeyboardAppearance | 定义输入框拉起的键盘样式。 |
| [ArkUI\_TextDataDetectorType](capi-native-type-h.md#arkui_textdatadetectortype) | ArkUI\_TextDataDetectorType | 定义文本识别的实体类型。 |
| [ArkUI\_ButtonType](capi-native-type-h.md#arkui_buttontype) | ArkUI\_ButtonType | 定义按钮样式枚举值。 |
| [ArkUI\_RenderFit](capi-native-type-h.md#arkui_renderfit) | ArkUI\_RenderFit | 定义动画终态内容大小与位置的枚举值。 |
| [ArkUI\_SwiperIndicatorType](capi-native-type-h.md#arkui_swiperindicatortype) | ArkUI\_SwiperIndicatorType | 定义Swiper组件的导航指示器类型。 |
| [ArkUI\_AnimationDirection](capi-native-type-h.md#arkui_animationdirection) | ArkUI\_AnimationDirection | 动画播放方向。 |
| [ArkUI\_ListItemSwipeActionState](capi-native-type-h.md#arkui_listitemswipeactionstate) | ArkUI\_ListItemSwipeActionState | 定义[Listitem](ts-container-listitem.md#listitem10)组件[swipeAction](ts-container-listitem.md#swipeaction9)方法的显隐模式。 |
| [ArkUI\_ListItemSwipeEdgeEffect](capi-native-type-h.md#arkui_listitemswipeedgeeffect) | ArkUI\_ListItemSwipeEdgeEffect | 定义[Listitem](ts-container-listitem.md#listitem10)组件[swipeAction](ts-container-listitem.md#swipeaction9)方法的滚动模式。 |
| [ArkUI\_ListItemSwipeActionDirection](capi-native-type-h.md#arkui_listitemswipeactiondirection) | ArkUI\_ListItemSwipeActionDirection | ListItem划出菜单的展开方向。 |
| [ArkUI\_AnimationStatus](capi-native-type-h.md#arkui_animationstatus) | ArkUI\_AnimationStatus | 定义帧动画的播放状态。 |
| [ArkUI\_AnimationFillMode](capi-native-type-h.md#arkui_animationfillmode) | ArkUI\_AnimationFillMode | 定义帧动画组件在动画开始前和结束后的状态。 |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | ArkUI\_ErrorCode | 定义错误码枚举值。 |
| [ArkUI\_ScrollSource](capi-native-type-h.md#arkui_scrollsource) | ArkUI\_ScrollSource | 定义滚动来源枚举值。 |
| [ArkUI\_SafeAreaType](capi-native-type-h.md#arkui_safeareatype) | ArkUI\_SafeAreaType | 定义扩展安全区域的枚举值。 |
| [ArkUI\_SafeAreaEdge](capi-native-type-h.md#arkui_safeareaedge) | ArkUI\_SafeAreaEdge | 定义扩展安全区域的方向的枚举值。 |
| [ArkUI\_FocusMove](capi-native-type-h.md#arkui_focusmove) | ArkUI\_FocusMove | 定义焦点移动方向的枚举值。 |
| [ArkUI\_ListItemGroupArea](capi-native-type-h.md#arkui_listitemgrouparea) | ArkUI\_ListItemGroupArea | 定义ListItemGroup组件区域。 |
| [ArkUI\_KeyboardAvoidMode](capi-native-type-h.md#arkui_keyboardavoidmode) | ArkUI\_KeyboardAvoidMode | 键盘避让模式。 |
| [ArkUI\_HoverModeAreaType](capi-native-type-h.md#arkui_hovermodeareatype) | ArkUI\_HoverModeAreaType | 悬停态显示区域。 |
| [ArkUI\_ExpandMode](capi-native-type-h.md#arkui_expandmode) | ArkUI\_ExpandMode | 定义子节点展开模式枚举值。 |
| [ArkUI\_NavDestinationState](capi-native-type-h.md#arkui_navdestinationstate) | ArkUI\_NavDestinationState | 定义NavDestination组件的状态。 |
| [ArkUI\_RouterPageState](capi-native-type-h.md#arkui_routerpagestate) | ArkUI\_RouterPageState | 定义Router Page的状态。 |
| [ArkUI\_UIState](capi-native-type-h.md#arkui_uistate) | ArkUI\_UIState | 组件的UI状态枚举，用于处理状态样式。 |
| [ArkUI\_FocusWrapMode](capi-native-type-h.md#arkui_focuswrapmode) | ArkUI\_FocusWrapMode | 组件走焦换行规则。 |
| [ArkUI\_ItemFillPolicy](capi-native-type-h.md#arkui_itemfillpolicy) | ArkUI\_ItemFillPolicy | 为不同响应式断点规格指定列数。 |
| [ArkUI\_EdgeDirection](capi-native-type-h.md#arkui_edgedirection) | ArkUI\_EdgeDirection | 定义矩形边方向。 |
| [ArkUI\_CornerDirection](capi-native-type-h.md#arkui_cornerdirection) | ArkUI\_CornerDirection | 定义角度方向。 |
| [ArkUI\_LayoutPolicy](capi-native-type-h.md#arkui_layoutpolicy) | ArkUI\_LayoutPolicy | 布局策略枚举。 |
| [ArkUI\_PixelRoundCalcPolicy](capi-native-type-h.md#arkui_pixelroundcalcpolicy) | ArkUI\_PixelRoundCalcPolicy | 定义像素取整计算策略枚举。 |
| [ArkUI\_GridItemStyle](capi-native-type-h.md#arkui_griditemstyle) | ArkUI\_GridItemStyle | GridItem样式枚举。 |
| [ArkUI\_MenuPolicy](capi-native-type-h.md#arkui_menupolicy) | ArkUI\_MenuPolicy | 菜单弹出策略。 |
| [ArkUI\_ResponseRegionSupportedTool](capi-native-type-h.md#arkui_responseregionsupportedtool) | ArkUI\_ResponseRegionSupportedTool | 定义支持响应区域设置的事件工具类型。 |
| [ArkUI\_TextMenuItemId](capi-native-type-h.md#arkui_textmenuitemid) | ArkUI\_TextMenuItemId | 文本菜单项id枚举。 |
| [ArkUI\_TextSpanType](capi-native-type-h.md#arkui_textspantype) | ArkUI\_TextSpanType | 自定义文本选择菜单的文本识别类型枚举。 |
| [ArkUI\_TextResponseType](capi-native-type-h.md#arkui_textresponsetype) | ArkUI\_TextResponseType | 自定义文本选择菜单的响应类型枚举。 |
| [ArkUI\_HoverEffect](capi-native-type-h.md#arkui_hovereffect) | ArkUI\_HoverEffect | 组件被悬停时的效果。 |
| [ArkUI\_FocusPriority](capi-native-type-h.md#arkui_focuspriority) | ArkUI\_FocusPriority | 应用程序内焦点管理的优先级级别。确定UI组件在交互期间接收焦点的顺序。 |
| [ArkUI\_LayoutSafeAreaType](capi-native-type-h.md#arkui_layoutsafeareatype) | ArkUI\_LayoutSafeAreaType | 定义扩展安全区域的枚举值。 |
| [ArkUI\_LayoutSafeAreaEdge](capi-native-type-h.md#arkui_layoutsafeareaedge) | ArkUI\_LayoutSafeAreaEdge | 定义扩展安全区域的方向的枚举值。 |
| [ArkUI\_LocalizedAlignment](capi-native-type-h.md#arkui_localizedalignment) | ArkUI\_LocalizedAlignment | 定义Stack容器中子组件的对齐规则。 |
| [ArkUI\_RenderStrategy](capi-native-type-h.md#arkui_renderstrategy) | ArkUI\_RenderStrategy | 定义组件绘制圆角的模式。 |
| [ArkUI\_MarqueeStartPolicy](capi-native-type-h.md#arkui_marqueestartpolicy) | ArkUI\_MarqueeStartPolicy | 定义跑马灯启动策略枚举。 |
| [ArkUI\_MarqueeUpdatePolicy](capi-native-type-h.md#arkui_marqueeupdatepolicy) | ArkUI\_MarqueeUpdatePolicy | 定义跑马灯更新策略枚举。 |
| [ArkUI\_PickerIndicatorType](capi-native-type-h.md#arkui_pickerindicatortype) | ArkUI\_PickerIndicatorType | 选择器的选中指示器类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_LayoutConstraint\* OH\_ArkUI\_LayoutConstraint\_Create()](capi-native-type-h.md#oh_arkui_layoutconstraint_create) | - | 创建布局约束。 |
| [ArkUI\_LayoutConstraint\* OH\_ArkUI\_LayoutConstraint\_Copy(const ArkUI\_LayoutConstraint\* Constraint)](capi-native-type-h.md#oh_arkui_layoutconstraint_copy) | - | 布局约束深拷贝。 |
| [void\* OH\_ArkUI\_LayoutConstraint\_Dispose(ArkUI\_LayoutConstraint\* Constraint)](capi-native-type-h.md#oh_arkui_layoutconstraint_dispose) | - | 销毁布局约束指针。 |
| [int32\_t OH\_ArkUI\_LayoutConstraint\_GetMaxWidth(const ArkUI\_LayoutConstraint\* Constraint)](capi-native-type-h.md#oh_arkui_layoutconstraint_getmaxwidth) | - | 通过布局约束获取最大宽度，单位为px。 |
| [int32\_t OH\_ArkUI\_LayoutConstraint\_GetMinWidth(const ArkUI\_LayoutConstraint\* Constraint)](capi-native-type-h.md#oh_arkui_layoutconstraint_getminwidth) | - | 通过布局约束获取最小宽度，单位为px。 |
| [int32\_t OH\_ArkUI\_LayoutConstraint\_GetMaxHeight(const ArkUI\_LayoutConstraint\* Constraint)](capi-native-type-h.md#oh_arkui_layoutconstraint_getmaxheight) | - | 通过布局约束获取最大高度，单位为px。 |
| [int32\_t OH\_ArkUI\_LayoutConstraint\_GetMinHeight(const ArkUI\_LayoutConstraint\* Constraint)](capi-native-type-h.md#oh_arkui_layoutconstraint_getminheight) | - | 通过布局约束获取最小高度，单位为px。 |
| [int32\_t OH\_ArkUI\_LayoutConstraint\_GetPercentReferenceWidth(const ArkUI\_LayoutConstraint\* Constraint)](capi-native-type-h.md#oh_arkui_layoutconstraint_getpercentreferencewidth) | - | 通过布局约束获取宽度百分比基准。 |
| [int32\_t OH\_ArkUI\_LayoutConstraint\_GetPercentReferenceHeight(const ArkUI\_LayoutConstraint\* Constraint)](capi-native-type-h.md#oh_arkui_layoutconstraint_getpercentreferenceheight) | - | 通过布局约束获取高度百分比基准。 |
| [void OH\_ArkUI\_LayoutConstraint\_SetMaxWidth(ArkUI\_LayoutConstraint\* Constraint, int32\_t value)](capi-native-type-h.md#oh_arkui_layoutconstraint_setmaxwidth) | - | 设置最大宽度。 |
| [void OH\_ArkUI\_LayoutConstraint\_SetMinWidth(ArkUI\_LayoutConstraint\* Constraint, int32\_t value)](capi-native-type-h.md#oh_arkui_layoutconstraint_setminwidth) | - | 设置最小宽度。 |
| [void OH\_ArkUI\_LayoutConstraint\_SetMaxHeight(ArkUI\_LayoutConstraint\* Constraint, int32\_t value)](capi-native-type-h.md#oh_arkui_layoutconstraint_setmaxheight) | - | 设置最大高度。 |
| [void OH\_ArkUI\_LayoutConstraint\_SetMinHeight(ArkUI\_LayoutConstraint\* Constraint, int32\_t value)](capi-native-type-h.md#oh_arkui_layoutconstraint_setminheight) | - | 设置最小高度。 |
| [void OH\_ArkUI\_LayoutConstraint\_SetPercentReferenceWidth(ArkUI\_LayoutConstraint\* Constraint, int32\_t value)](capi-native-type-h.md#oh_arkui_layoutconstraint_setpercentreferencewidth) | - | 设置宽度百分比基准。 |
| [void OH\_ArkUI\_LayoutConstraint\_SetPercentReferenceHeight(ArkUI\_LayoutConstraint\* Constraint, int32\_t value)](capi-native-type-h.md#oh_arkui_layoutconstraint_setpercentreferenceheight) | - | 设置高度百分比基准。 |
| [void\* OH\_ArkUI\_DrawContext\_GetCanvas(ArkUI\_DrawContext\* context)](capi-native-type-h.md#oh_arkui_drawcontext_getcanvas) | - | 获取绘制canvas指针，可以转换为图形库的OH\_Drawing\_Canvas指针进行绘制。 |
| [ArkUI\_IntSize OH\_ArkUI\_DrawContext\_GetSize(ArkUI\_DrawContext\* context)](capi-native-type-h.md#oh_arkui_drawcontext_getsize) | - | 获取可绘制区域大小。 |
| [ArkUI\_WaterFlowSectionOption\* OH\_ArkUI\_WaterFlowSectionOption\_Create()](capi-native-type-h.md#oh_arkui_waterflowsectionoption_create) | - | 创建FlowItem分组配置信息。 |
| [void OH\_ArkUI\_WaterFlowSectionOption\_Dispose(ArkUI\_WaterFlowSectionOption\* option)](capi-native-type-h.md#oh_arkui_waterflowsectionoption_dispose) | - | 销毁FlowItem分组配置信息指针。 |
| [void OH\_ArkUI\_WaterFlowSectionOption\_SetSize(ArkUI\_WaterFlowSectionOption\* option, int32\_t size)](capi-native-type-h.md#oh_arkui_waterflowsectionoption_setsize) | - | 设置FlowItem分组配置信息数组长度。 |
| [int32\_t OH\_ArkUI\_WaterFlowSectionOption\_GetSize(ArkUI\_WaterFlowSectionOption\* option)](capi-native-type-h.md#oh_arkui_waterflowsectionoption_getsize) | - | 获取FlowItem分组配置信息数组长度。 |
| [void OH\_ArkUI\_WaterFlowSectionOption\_SetItemCount(ArkUI\_WaterFlowSectionOption\* option, int32\_t index, int32\_t itemCount)](capi-native-type-h.md#oh_arkui_waterflowsectionoption_setitemcount) | - | 设置分组中FlowItem数量。 |
| [int32\_t OH\_ArkUI\_WaterFlowSectionOption\_GetItemCount(ArkUI\_WaterFlowSectionOption\* option, int32\_t index)](capi-native-type-h.md#oh_arkui_waterflowsectionoption_getitemcount) | - | 通过FlowItem分组配置信息获取对应索引下的FlowItem数量。 |
| [void OH\_ArkUI\_WaterFlowSectionOption\_SetCrossCount(ArkUI\_WaterFlowSectionOption\* option, int32\_t index, int32\_t crossCount)](capi-native-type-h.md#oh_arkui_waterflowsectionoption_setcrosscount) | - | 设置布局栅格，纵向布局时为列数，横向布局时为行数。 |
| [int32\_t OH\_ArkUI\_WaterFlowSectionOption\_GetCrossCount(ArkUI\_WaterFlowSectionOption\* option, int32\_t index)](capi-native-type-h.md#oh_arkui_waterflowsectionoption_getcrosscount) | - | 通过FlowItem分组配置信息获取对应索引下的布局栅格数。 |
| [void OH\_ArkUI\_WaterFlowSectionOption\_SetColumnGap(ArkUI\_WaterFlowSectionOption\* option, int32\_t index, float columnGap)](capi-native-type-h.md#oh_arkui_waterflowsectionoption_setcolumngap) | - | 设置分组的列间距。 |
| [float OH\_ArkUI\_WaterFlowSectionOption\_GetColumnGap(ArkUI\_WaterFlowSectionOption\* option, int32\_t index)](capi-native-type-h.md#oh_arkui_waterflowsectionoption_getcolumngap) | - | 通过FlowItem分组配置信息获取对应索引下的分组的列间距。 |
| [void OH\_ArkUI\_WaterFlowSectionOption\_SetRowGap(ArkUI\_WaterFlowSectionOption\* option, int32\_t index, float rowGap)](capi-native-type-h.md#oh_arkui_waterflowsectionoption_setrowgap) | - | 设置分组的行间距。 |
| [float OH\_ArkUI\_WaterFlowSectionOption\_GetRowGap(ArkUI\_WaterFlowSectionOption\* option, int32\_t index)](capi-native-type-h.md#oh_arkui_waterflowsectionoption_getrowgap) | - | 通过FlowItem分组配置信息获取对应索引下的分组的行间距。 |
| [void OH\_ArkUI\_WaterFlowSectionOption\_SetMargin(ArkUI\_WaterFlowSectionOption\* option, int32\_t index,float marginTop, float marginRight, float marginBottom, float marginLeft)](capi-native-type-h.md#oh_arkui_waterflowsectionoption_setmargin) | - | 设置分组的外边距。 |
| [ArkUI\_Margin OH\_ArkUI\_WaterFlowSectionOption\_GetMargin(ArkUI\_WaterFlowSectionOption\* option, int32\_t index)](capi-native-type-h.md#oh_arkui_waterflowsectionoption_getmargin) | - | 通过FlowItem分组配置信息获取对应索引下的分组的外边距。 |
| [void OH\_ArkUI\_WaterFlowSectionOption\_RegisterGetItemMainSizeCallbackByIndex (ArkUI\_WaterFlowSectionOption\* option, int32\_t index, float(\*callback)(int32\_t itemIndex))](capi-native-type-h.md#oh_arkui_waterflowsectionoption_registergetitemmainsizecallbackbyindex) | - | 通过FlowItem分组配置信息根据itemIndex获取指定FlowItem的主轴大小。如需在回调中使用自定义数据，可使用[OH\_ArkUI\_WaterFlowSectionOption\_RegisterGetItemMainSizeCallbackByIndexWithUserData](capi-native-type-h.md#oh_arkui_waterflowsectionoption_registergetitemmainsizecallbackbyindexwithuserdata)。 |
| [void OH\_ArkUI\_WaterFlowSectionOption\_RegisterGetItemMainSizeCallbackByIndexWithUserData (ArkUI\_WaterFlowSectionOption\* option, int32\_t index, void\* userData, float (\*callback)(int32\_t itemIndex, void\* userData))](capi-native-type-h.md#oh_arkui_waterflowsectionoption_registergetitemmainsizecallbackbyindexwithuserdata) | - | 通过FlowItem分组配置信息根据itemIndex获取指定Item的主轴大小。与[OH\_ArkUI\_WaterFlowSectionOption\_RegisterGetItemMainSizeCallbackByIndex](capi-native-type-h.md#oh_arkui_waterflowsectionoption_registergetitemmainsizecallbackbyindex)的区别在于，该接口支持传入自定义数据userData，并在回调函数中接收该数据。 |
| [ArkUI\_GuidelineOption\* OH\_ArkUI\_GuidelineOption\_Create(int32\_t size)](capi-native-type-h.md#oh_arkui_guidelineoption_create) | - | 创建RelativeContainer容器内的辅助线信息。 |
| [void OH\_ArkUI\_GuidelineOption\_Dispose(ArkUI\_GuidelineOption\* guideline)](capi-native-type-h.md#oh_arkui_guidelineoption_dispose) | - | 销毁辅助线信息。 |
| [void OH\_ArkUI\_GuidelineOption\_SetId(ArkUI\_GuidelineOption\* guideline, const char\* value, int32\_t index)](capi-native-type-h.md#oh_arkui_guidelineoption_setid) | - | 设置辅助线的Id。 |
| [void OH\_ArkUI\_GuidelineOption\_SetDirection(ArkUI\_GuidelineOption\* guideline, ArkUI\_Axis value, int32\_t index)](capi-native-type-h.md#oh_arkui_guidelineoption_setdirection) | - | 设置辅助线的方向。 |
| [void OH\_ArkUI\_GuidelineOption\_SetPositionStart(ArkUI\_GuidelineOption\* guideline, float value, int32\_t index)](capi-native-type-h.md#oh_arkui_guidelineoption_setpositionstart) | - | 设置距离容器左侧或者顶部的距离。 |
| [void OH\_ArkUI\_GuidelineOption\_SetPositionEnd(ArkUI\_GuidelineOption\* guideline, float value, int32\_t index)](capi-native-type-h.md#oh_arkui_guidelineoption_setpositionend) | - | 设置距离容器右侧或者底部的距离。 |
| [const char\* OH\_ArkUI\_GuidelineOption\_GetId(ArkUI\_GuidelineOption\* guideline, int32\_t index)](capi-native-type-h.md#oh_arkui_guidelineoption_getid) | - | 获取辅助线的Id。 |
| [ArkUI\_Axis OH\_ArkUI\_GuidelineOption\_GetDirection(ArkUI\_GuidelineOption\* guideline, int32\_t index)](capi-native-type-h.md#oh_arkui_guidelineoption_getdirection) | - | 获取辅助线的方向。 |
| [float OH\_ArkUI\_GuidelineOption\_GetPositionStart(ArkUI\_GuidelineOption\* guideline, int32\_t index)](capi-native-type-h.md#oh_arkui_guidelineoption_getpositionstart) | - | 获取距离容器左侧或者顶部的距离。 |
| [float OH\_ArkUI\_GuidelineOption\_GetPositionEnd(ArkUI\_GuidelineOption\* guideline, int32\_t index)](capi-native-type-h.md#oh_arkui_guidelineoption_getpositionend) | - | 获取距离容器右侧或者底部的距离。 |
| [ArkUI\_BarrierOption\* OH\_ArkUI\_BarrierOption\_Create(int32\_t size)](capi-native-type-h.md#oh_arkui_barrieroption_create) | - | 创建RelativeContainer容器内的屏障信息。 |
| [void OH\_ArkUI\_BarrierOption\_Dispose(ArkUI\_BarrierOption\* barrierStyle)](capi-native-type-h.md#oh_arkui_barrieroption_dispose) | - | 销毁屏障信息。 |
| [void OH\_ArkUI\_BarrierOption\_SetId(ArkUI\_BarrierOption\* barrierStyle, const char\* value, int32\_t index)](capi-native-type-h.md#oh_arkui_barrieroption_setid) | - | 设置屏障的Id。 |
| [void OH\_ArkUI\_BarrierOption\_SetDirection(ArkUI\_BarrierOption\* barrierStyle, ArkUI\_BarrierDirection value, int32\_t index)](capi-native-type-h.md#oh_arkui_barrieroption_setdirection) | - | 设置屏障的方向。 |
| [void OH\_ArkUI\_BarrierOption\_SetReferencedId(ArkUI\_BarrierOption\* barrierStyle, const char\* value, int32\_t index)](capi-native-type-h.md#oh_arkui_barrieroption_setreferencedid) | - | 设置屏障的依赖的组件。 |
| [const char\* OH\_ArkUI\_BarrierOption\_GetId(ArkUI\_BarrierOption\* barrierStyle, int32\_t index)](capi-native-type-h.md#oh_arkui_barrieroption_getid) | - | 获取屏障的Id。 |
| [ArkUI\_BarrierDirection OH\_ArkUI\_BarrierOption\_GetDirection(ArkUI\_BarrierOption\* barrierStyle, int32\_t index)](capi-native-type-h.md#oh_arkui_barrieroption_getdirection) | - | 获取屏障的方向。 |
| [const char\* OH\_ArkUI\_BarrierOption\_GetReferencedId(ArkUI\_BarrierOption\* barrierStyle, int32\_t index , int32\_t referencedIndex)](capi-native-type-h.md#oh_arkui_barrieroption_getreferencedid) | - | 获取屏障的依赖的组件。 |
| [int32\_t OH\_ArkUI\_BarrierOption\_GetReferencedIdSize(ArkUI\_BarrierOption\* barrierStyle, int32\_t index)](capi-native-type-h.md#oh_arkui_barrieroption_getreferencedidsize) | - | 获取屏障的依赖的组件的个数。 |
| [ArkUI\_AlignmentRuleOption\* OH\_ArkUI\_AlignmentRuleOption\_Create()](capi-native-type-h.md#oh_arkui_alignmentruleoption_create) | - | 创建相对容器中子组件的对齐规则信息。 |
| [void OH\_ArkUI\_AlignmentRuleOption\_Dispose(ArkUI\_AlignmentRuleOption\* option)](capi-native-type-h.md#oh_arkui_alignmentruleoption_dispose) | - | 销毁相对容器中子组件的对齐规则信息。 |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetStart(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_HorizontalAlignment alignment)](capi-native-type-h.md#oh_arkui_alignmentruleoption_setstart) | - | 设置相对布局的左对齐方式。 |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetEnd(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_HorizontalAlignment alignment)](capi-native-type-h.md#oh_arkui_alignmentruleoption_setend) | - | 设置相对布局的右对齐方式。 |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetCenterHorizontal(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_HorizontalAlignment alignment)](capi-native-type-h.md#oh_arkui_alignmentruleoption_setcenterhorizontal) | - | 设置相对布局的横向居中对齐方式。 |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetTop(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_VerticalAlignment alignment)](capi-native-type-h.md#oh_arkui_alignmentruleoption_settop) | - | 设置相对布局的顶部对齐的方式。 |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetBottom(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_VerticalAlignment alignment)](capi-native-type-h.md#oh_arkui_alignmentruleoption_setbottom) | - | 设置相对布局的底部对齐的方式。 |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetCenterVertical(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_VerticalAlignment alignment)](capi-native-type-h.md#oh_arkui_alignmentruleoption_setcentervertical) | - | 设置相对布局的纵向居中对齐方式。 |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetBiasHorizontal(ArkUI\_AlignmentRuleOption\* option, float horizontal)](capi-native-type-h.md#oh_arkui_alignmentruleoption_setbiashorizontal) | - | 设置组件在锚点约束下的水平方向上偏移参数。 |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetBiasVertical(ArkUI\_AlignmentRuleOption\* option, float vertical)](capi-native-type-h.md#oh_arkui_alignmentruleoption_setbiasvertical) | - | 设置组件在锚点约束下的垂直方向上偏移参数。 |
| [const char\* OH\_ArkUI\_AlignmentRuleOption\_GetStartId(ArkUI\_AlignmentRuleOption\* option)](capi-native-type-h.md#oh_arkui_alignmentruleoption_getstartid) | - | 获取左对齐锚点组件的Id。 |
| [ArkUI\_HorizontalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetStartAlignment(ArkUI\_AlignmentRuleOption\* option)](capi-native-type-h.md#oh_arkui_alignmentruleoption_getstartalignment) | - | 获取左对齐方式。 |
| [const char\* OH\_ArkUI\_AlignmentRuleOption\_GetEndId(ArkUI\_AlignmentRuleOption\* option)](capi-native-type-h.md#oh_arkui_alignmentruleoption_getendid) | - | 获取右对齐锚点组件的Id。 |
| [ArkUI\_HorizontalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetEndAlignment(ArkUI\_AlignmentRuleOption\* option)](capi-native-type-h.md#oh_arkui_alignmentruleoption_getendalignment) | - | 获取右对齐方式。 |
| [const char\* OH\_ArkUI\_AlignmentRuleOption\_GetCenterIdHorizontal(ArkUI\_AlignmentRuleOption\* option)](capi-native-type-h.md#oh_arkui_alignmentruleoption_getcenteridhorizontal) | - | 获取横向居中对齐锚点组件的Id。 |
| [ArkUI\_HorizontalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetCenterAlignmentHorizontal(ArkUI\_AlignmentRuleOption\* option)](capi-native-type-h.md#oh_arkui_alignmentruleoption_getcenteralignmenthorizontal) | - | 获取横向居中对齐方式。 |
| [const char\* OH\_ArkUI\_AlignmentRuleOption\_GetTopId(ArkUI\_AlignmentRuleOption\* option)](capi-native-type-h.md#oh_arkui_alignmentruleoption_gettopid) | - | 获取顶部对齐锚点组件的Id。 |
| [ArkUI\_VerticalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetTopAlignment(ArkUI\_AlignmentRuleOption\* option)](capi-native-type-h.md#oh_arkui_alignmentruleoption_gettopalignment) | - | 获取顶部对齐的方式。 |
| [const char\* OH\_ArkUI\_AlignmentRuleOption\_GetBottomId(ArkUI\_AlignmentRuleOption\* option)](capi-native-type-h.md#oh_arkui_alignmentruleoption_getbottomid) | - | 获取底部对齐锚点组件的Id。 |
| [ArkUI\_VerticalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetBottomAlignment(ArkUI\_AlignmentRuleOption\* option)](capi-native-type-h.md#oh_arkui_alignmentruleoption_getbottomalignment) | - | 获取底部对齐的方式。 |
| [const char\* OH\_ArkUI\_AlignmentRuleOption\_GetCenterIdVertical(ArkUI\_AlignmentRuleOption\* option)](capi-native-type-h.md#oh_arkui_alignmentruleoption_getcenteridvertical) | - | 获取纵向居中对齐锚点组件的Id。 |
| [ArkUI\_VerticalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetCenterAlignmentVertical(ArkUI\_AlignmentRuleOption\* option)](capi-native-type-h.md#oh_arkui_alignmentruleoption_getcenteralignmentvertical) | - | 获取纵向居中对齐方式。 |
| [float OH\_ArkUI\_AlignmentRuleOption\_GetBiasHorizontal(ArkUI\_AlignmentRuleOption\* option)](capi-native-type-h.md#oh_arkui_alignmentruleoption_getbiashorizontal) | - | 获取水平方向上的bias值。 |
| [float OH\_ArkUI\_AlignmentRuleOption\_GetBiasVertical(ArkUI\_AlignmentRuleOption\* option)](capi-native-type-h.md#oh_arkui_alignmentruleoption_getbiasvertical) | - | 获取垂直方向上的bias值。 |
| [ArkUI\_SwiperIndicator\* OH\_ArkUI\_SwiperIndicator\_Create(ArkUI\_SwiperIndicatorType type)](capi-native-type-h.md#oh_arkui_swiperindicator_create) | - | 创建[Swiper](ts-container-swiper.md)组件的导航指示器。 |
| [void OH\_ArkUI\_SwiperIndicator\_Dispose(ArkUI\_SwiperIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperindicator_dispose) | - | 销毁Swiper组件的导航指示器指针。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetStartPosition(ArkUI\_SwiperIndicator\* indicator, float value)](capi-native-type-h.md#oh_arkui_swiperindicator_setstartposition) | - | 设置导航点距离Swiper组件左边的距离。 |
| [float OH\_ArkUI\_SwiperIndicator\_GetStartPosition(ArkUI\_SwiperIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperindicator_getstartposition) | - | 获取导航点距离Swiper组件左边的距离。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetTopPosition(ArkUI\_SwiperIndicator\* indicator, float value)](capi-native-type-h.md#oh_arkui_swiperindicator_settopposition) | - | 设置导航点距离Swiper组件顶部的距离。 |
| [float OH\_ArkUI\_SwiperIndicator\_GetTopPosition(ArkUI\_SwiperIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperindicator_gettopposition) | - | 获取导航点距离Swiper组件顶部的距离。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetEndPosition(ArkUI\_SwiperIndicator\* indicator, float value)](capi-native-type-h.md#oh_arkui_swiperindicator_setendposition) | - | 设置导航点距离Swiper组件右边的距离。 |
| [float OH\_ArkUI\_SwiperIndicator\_GetEndPosition(ArkUI\_SwiperIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperindicator_getendposition) | - | 获取导航点距离Swiper组件右边的距离。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetBottomPosition(ArkUI\_SwiperIndicator\* indicator, float value)](capi-native-type-h.md#oh_arkui_swiperindicator_setbottomposition) | - | 设置导航点距离Swiper组件底部的距离。 |
| [float OH\_ArkUI\_SwiperIndicator\_GetBottomPosition(ArkUI\_SwiperIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperindicator_getbottomposition) | - | 获取导航点距离Swiper组件底部的距离。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetIgnoreSizeOfBottom(ArkUI\_SwiperIndicator\* indicator, int32\_t ignoreSize)](capi-native-type-h.md#oh_arkui_swiperindicator_setignoresizeofbottom) | - | 设置OH\_ArkUI\_SwiperIndicator\_SetBottomPosition是否忽略导航点大小。 |
| [int32\_t OH\_ArkUI\_SwiperIndicator\_GetIgnoreSizeOfBottom(ArkUI\_SwiperIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperindicator_getignoresizeofbottom) | - | 获取OH\_ArkUI\_SwiperIndicator\_SetBottomPosition是否忽略导航点大小。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetItemWidth(ArkUI\_SwiperIndicator\* indicator, float value)](capi-native-type-h.md#oh_arkui_swiperindicator_setitemwidth) | - | 设置Swiper组件圆点导航指示器的宽。 |
| [float OH\_ArkUI\_SwiperIndicator\_GetItemWidth(ArkUI\_SwiperIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperindicator_getitemwidth) | - | 获取Swiper组件圆点导航指示器的宽。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetItemHeight(ArkUI\_SwiperIndicator\* indicator, float value)](capi-native-type-h.md#oh_arkui_swiperindicator_setitemheight) | - | 设置Swiper组件圆点导航指示器的高。 |
| [float OH\_ArkUI\_SwiperIndicator\_GetItemHeight(ArkUI\_SwiperIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperindicator_getitemheight) | - | 获取Swiper组件圆点导航指示器的高。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetSelectedItemWidth(ArkUI\_SwiperIndicator\* indicator, float value)](capi-native-type-h.md#oh_arkui_swiperindicator_setselecteditemwidth) | - | 设置被选中的Swiper组件圆点导航指示器的宽。 |
| [float OH\_ArkUI\_SwiperIndicator\_GetSelectedItemWidth(ArkUI\_SwiperIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperindicator_getselecteditemwidth) | - | 获取被选中Swiper组件圆点导航指示器的宽。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetSelectedItemHeight(ArkUI\_SwiperIndicator\* indicator, float value)](capi-native-type-h.md#oh_arkui_swiperindicator_setselecteditemheight) | - | 设置被选中的Swiper组件圆点导航指示器的高。 |
| [float OH\_ArkUI\_SwiperIndicator\_GetSelectedItemHeight(ArkUI\_SwiperIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperindicator_getselecteditemheight) | - | 获取被选中Swiper组件圆点导航指示器的高。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetMask(ArkUI\_SwiperIndicator\* indicator, int32\_t mask)](capi-native-type-h.md#oh_arkui_swiperindicator_setmask) | - | 设置是否显示Swiper组件圆点导航指示器的蒙版样式。 |
| [int32\_t OH\_ArkUI\_SwiperIndicator\_GetMask(ArkUI\_SwiperIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperindicator_getmask) | - | 获取是否显示Swiper组件圆点导航指示器的蒙版样式。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetColor(ArkUI\_SwiperIndicator\* indicator, uint32\_t color)](capi-native-type-h.md#oh_arkui_swiperindicator_setcolor) | - | 设置Swiper组件圆点导航指示器的颜色。 |
| [uint32\_t OH\_ArkUI\_SwiperIndicator\_GetColor(ArkUI\_SwiperIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperindicator_getcolor) | - | 获取Swiper组件圆点导航指示器的颜色。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetSelectedColor(ArkUI\_SwiperIndicator\* indicator, uint32\_t selectedColor)](capi-native-type-h.md#oh_arkui_swiperindicator_setselectedcolor) | - | 设置被选中Swiper组件圆点导航指示器的颜色。 |
| [uint32\_t OH\_ArkUI\_SwiperIndicator\_GetSelectedColor(ArkUI\_SwiperIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperindicator_getselectedcolor) | - | 获取被选中Swiper组件圆点导航指示器的颜色。 |
| [int32\_t OH\_ArkUI\_SwiperIndicator\_SetMaxDisplayCount(ArkUI\_SwiperIndicator\* indicator, int32\_t maxDisplayCount)](capi-native-type-h.md#oh_arkui_swiperindicator_setmaxdisplaycount) | - | 设置圆点导航点指示器样式下，导航点显示个数的最大值。 |
| [int32\_t OH\_ArkUI\_SwiperIndicator\_GetMaxDisplayCount(ArkUI\_SwiperIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperindicator_getmaxdisplaycount) | - | 获取圆点导航点指示器样式下，导航点显示个数的最大值。 |
| [ArkUI\_SwiperDigitIndicator \*OH\_ArkUI\_SwiperDigitIndicator\_Create()](capi-native-type-h.md#oh_arkui_swiperdigitindicator_create) | - | 创建Swiper组件的数字导航指示器。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_Destroy(ArkUI\_SwiperDigitIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_destroy) | - | 销毁Swiper组件的数字导航指示器指针。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetStartPosition(ArkUI\_SwiperDigitIndicator\* indicator, float value)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_setstartposition) | - | 设置数字导航指示器距离Swiper组件左边的距离，在从右至左显示的语言模式下，设置其距离Swiper组件右边的距离。 |
| [float OH\_ArkUI\_SwiperDigitIndicator\_GetStartPosition(ArkUI\_SwiperDigitIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_getstartposition) | - | 获取数字导航指示器距离Swiper组件左边的距离，在从右至左显示的语言模式下，获取其距离Swiper组件右边的距离。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetTopPosition(ArkUI\_SwiperDigitIndicator\* indicator, float value)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_settopposition) | - | 设置数字导航指示器距离Swiper组件顶部的距离。 |
| [float OH\_ArkUI\_SwiperDigitIndicator\_GetTopPosition(ArkUI\_SwiperDigitIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_gettopposition) | - | 获取数字导航指示器距离Swiper组件顶部的距离。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetEndPosition(ArkUI\_SwiperDigitIndicator\* indicator, float value)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_setendposition) | - | 设置数字导航指示器距离Swiper组件右边的距离，在从右至左显示的语言模式下，设置其距离Swiper组件左边的距离。 |
| [float OH\_ArkUI\_SwiperDigitIndicator\_GetEndPosition(ArkUI\_SwiperDigitIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_getendposition) | - | 获取数字导航指示器距离Swiper组件右边的距离，在从右至左显示的语言模式下，获取其距离Swiper组件左边的距离。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetBottomPosition(ArkUI\_SwiperDigitIndicator\* indicator, float value)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_setbottomposition) | - | 设置数字导航指示器距离Swiper组件底部的距离。 |
| [float OH\_ArkUI\_SwiperDigitIndicator\_GetBottomPosition(ArkUI\_SwiperDigitIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_getbottomposition) | - | 获取数字导航指示器距离Swiper组件底部的距离。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetFontColor(ArkUI\_SwiperDigitIndicator\* indicator, uint32\_t color)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_setfontcolor) | - | 设置Swiper组件数字导航指示器字体颜色。 |
| [uint32\_t OH\_ArkUI\_SwiperDigitIndicator\_GetFontColor(ArkUI\_SwiperDigitIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_getfontcolor) | - | 获取Swiper组件数字导航指示器字体颜色。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetSelectedFontColor(ArkUI\_SwiperDigitIndicator\* indicator, uint32\_t selectedColor)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_setselectedfontcolor) | - | 设置被选中Swiper组件数字导航指示器字体颜色。 |
| [uint32\_t OH\_ArkUI\_SwiperDigitIndicator\_GetSelectedFontColor(ArkUI\_SwiperDigitIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_getselectedfontcolor) | - | 获取被选中Swiper组件数字导航指示器字体颜色。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetFontSize(ArkUI\_SwiperDigitIndicator\* indicator, float size)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_setfontsize) | - | 设置Swiper组件数字导航指示器字体大小。 |
| [float OH\_ArkUI\_SwiperDigitIndicator\_GetFontSize(ArkUI\_SwiperDigitIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_getfontsize) | - | 获取Swiper组件数字导航指示器字体大小。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetSelectedFontSize(ArkUI\_SwiperDigitIndicator\* indicator, float size)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_setselectedfontsize) | - | 设置被选中Swiper组件数字导航指示器字体大小。 |
| [float OH\_ArkUI\_SwiperDigitIndicator\_GetSelectedFontSize(ArkUI\_SwiperDigitIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_getselectedfontsize) | - | 获取被选中Swiper组件数字导航指示器字体大小。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetFontWeight(ArkUI\_SwiperDigitIndicator \*indicator, ArkUI\_FontWeight fontWeight)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_setfontweight) | - | 设置Swiper组件数字导航指示器字体粗细属性。 |
| [ArkUI\_FontWeight OH\_ArkUI\_SwiperDigitIndicator\_GetFontWeight(ArkUI\_SwiperDigitIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_getfontweight) | - | 获取Swiper组件数字导航指示器字体粗细属性。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetSelectedFontWeight(ArkUI\_SwiperDigitIndicator \*indicator, ArkUI\_FontWeight selectedFontWeight)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_setselectedfontweight) | - | 设置被选中Swiper组件数字导航指示器字体粗细属性。 |
| [ArkUI\_FontWeight OH\_ArkUI\_SwiperDigitIndicator\_GetSelectedFontWeight(ArkUI\_SwiperDigitIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_getselectedfontweight) | - | 获取被选中Swiper组件数字导航指示器字体粗细属性。 |
| [ArkUI\_SwiperArrowStyle \*OH\_ArkUI\_SwiperArrowStyle\_Create()](capi-native-type-h.md#oh_arkui_swiperarrowstyle_create) | - | 创建Swiper组件的导航箭头。 |
| [void OH\_ArkUI\_SwiperArrowStyle\_Destroy(ArkUI\_SwiperArrowStyle\* arrowStyle)](capi-native-type-h.md#oh_arkui_swiperarrowstyle_destroy) | - | 销毁Swiper组件的导航箭头指针。 |
| [void OH\_ArkUI\_SwiperArrowStyle\_SetShowBackground(ArkUI\_SwiperArrowStyle\* arrowStyle, int32\_t showBackground)](capi-native-type-h.md#oh_arkui_swiperarrowstyle_setshowbackground) | - | 设置Swiper组件导航箭头底板是否显示。 |
| [int32\_t OH\_ArkUI\_SwiperArrowStyle\_GetShowBackground(ArkUI\_SwiperArrowStyle\* arrowStyle)](capi-native-type-h.md#oh_arkui_swiperarrowstyle_getshowbackground) | - | 获取Swiper组件导航箭头底板是否显示。 |
| [void OH\_ArkUI\_SwiperArrowStyle\_SetShowSidebarMiddle(ArkUI\_SwiperArrowStyle\* arrowStyle, int32\_t showSidebarMiddle)](capi-native-type-h.md#oh_arkui_swiperarrowstyle_setshowsidebarmiddle) | - | 设置Swiper组件导航箭头显示位置。 |
| [int32\_t OH\_ArkUI\_SwiperArrowStyle\_GetShowSidebarMiddle(ArkUI\_SwiperArrowStyle\* arrowStyle)](capi-native-type-h.md#oh_arkui_swiperarrowstyle_getshowsidebarmiddle) | - | 获取Swiper组件导航箭头显示位置。 |
| [void OH\_ArkUI\_SwiperArrowStyle\_SetBackgroundSize(ArkUI\_SwiperArrowStyle\* arrowStyle, float backgroundSize)](capi-native-type-h.md#oh_arkui_swiperarrowstyle_setbackgroundsize) | - | 设置Swiper组件导航箭头底板大小。 |
| [float OH\_ArkUI\_SwiperArrowStyle\_GetBackgroundSize(ArkUI\_SwiperArrowStyle\* arrowStyle)](capi-native-type-h.md#oh_arkui_swiperarrowstyle_getbackgroundsize) | - | 获取Swiper组件导航箭头底板大小。 |
| [void OH\_ArkUI\_SwiperArrowStyle\_SetBackgroundColor(ArkUI\_SwiperArrowStyle\* arrowStyle, uint32\_t backgroundColor)](capi-native-type-h.md#oh_arkui_swiperarrowstyle_setbackgroundcolor) | - | 设置Swiper组件导航箭头底板颜色。 |
| [uint32\_t OH\_ArkUI\_SwiperArrowStyle\_GetBackgroundColor(ArkUI\_SwiperArrowStyle\* arrowStyle)](capi-native-type-h.md#oh_arkui_swiperarrowstyle_getbackgroundcolor) | - | 获取Swiper组件导航箭头底板颜色。 |
| [void OH\_ArkUI\_SwiperArrowStyle\_SetArrowSize(ArkUI\_SwiperArrowStyle\* arrowStyle, float arrowSize)](capi-native-type-h.md#oh_arkui_swiperarrowstyle_setarrowsize) | - | 设置Swiper组件导航箭头大小。 |
| [float OH\_ArkUI\_SwiperArrowStyle\_GetArrowSize(ArkUI\_SwiperArrowStyle\* arrowStyle)](capi-native-type-h.md#oh_arkui_swiperarrowstyle_getarrowsize) | - | 获取Swiper组件导航箭头大小。 |
| [void OH\_ArkUI\_SwiperArrowStyle\_SetArrowColor(ArkUI\_SwiperArrowStyle\* arrowStyle, uint32\_t arrowColor)](capi-native-type-h.md#oh_arkui_swiperarrowstyle_setarrowcolor) | - | 设置Swiper组件导航箭头颜色。 |
| [uint32\_t OH\_ArkUI\_SwiperArrowStyle\_GetArrowColor(ArkUI\_SwiperArrowStyle\* arrowStyle)](capi-native-type-h.md#oh_arkui_swiperarrowstyle_getarrowcolor) | - | 获取Swiper组件导航箭头颜色。 |
| [void OH\_ArkUI\_SwiperIndicator\_SetSpace(ArkUI\_SwiperIndicator\* indicator, float space)](capi-native-type-h.md#oh_arkui_swiperindicator_setspace) | - | 设置导航点间距。 |
| [float OH\_ArkUI\_SwiperIndicator\_GetSpace(ArkUI\_SwiperIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperindicator_getspace) | - | 获取导航点间距。 |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetIgnoreSizeOfBottom(ArkUI\_SwiperDigitIndicator\* indicator, int32\_t ignoreSize)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_setignoresizeofbottom) | - | 设置OH\_ArkUI\_SwiperDigitIndicator\_SetBottomPosition是否忽略导航点大小。 |
| [int32\_t OH\_ArkUI\_SwiperDigitIndicator\_GetIgnoreSizeOfBottom(ArkUI\_SwiperDigitIndicator\* indicator)](capi-native-type-h.md#oh_arkui_swiperdigitindicator_getignoresizeofbottom) | - | 获取OH\_ArkUI\_SwiperDigitIndicator\_SetBottomPosition是否忽略导航点大小。 |
| [ArkUI\_ListItemSwipeActionItem\* OH\_ArkUI\_ListItemSwipeActionItem\_Create()](capi-native-type-h.md#oh_arkui_listitemswipeactionitem_create) | - | 创建ListItemSwipeActionItem接口设置的配置项。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_Dispose(ArkUI\_ListItemSwipeActionItem\* item)](capi-native-type-h.md#oh_arkui_listitemswipeactionitem_dispose) | - | 销毁ListItemSwipeActionItem实例。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetContent(ArkUI\_ListItemSwipeActionItem\* item, ArkUI\_NodeHandle node)](capi-native-type-h.md#oh_arkui_listitemswipeactionitem_setcontent) | - | 设置ListItemSwipeActionItem的布局内容。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetActionAreaDistance(ArkUI\_ListItemSwipeActionItem\* item, float distance)](capi-native-type-h.md#oh_arkui_listitemswipeactionitem_setactionareadistance) | - | 设置组件长距离滑动删除距离阈值。 |
| [float OH\_ArkUI\_ListItemSwipeActionItem\_GetActionAreaDistance(ArkUI\_ListItemSwipeActionItem\* item)](capi-native-type-h.md#oh_arkui_listitemswipeactionitem_getactionareadistance) | - | 获取组件长距离滑动删除距离阈值。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnEnterActionArea(ArkUI\_ListItemSwipeActionItem\* item, void (\*callback)())](capi-native-type-h.md#oh_arkui_listitemswipeactionitem_setonenteractionarea) | - | 设置滑动条目进入删除区域时调用的事件。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnEnterActionAreaWithUserData (ArkUI\_ListItemSwipeActionItem\* item,void\* userData, void (\*callback)(void\* userData))](capi-native-type-h.md#oh_arkui_listitemswipeactionitem_setonenteractionareawithuserdata) | - | 设置滑动条目进入删除区域时调用的事件，回调事件会传入用户自定义数据。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnAction(ArkUI\_ListItemSwipeActionItem\* item, void (\*callback)())](capi-native-type-h.md#oh_arkui_listitemswipeactionitem_setonaction) | - | 设置组件进入长距删除区后删除ListItem时调用的事件。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnActionWithUserData(ArkUI\_ListItemSwipeActionItem\* item,void\* userData, void (\*callback)(void\* userData))](capi-native-type-h.md#oh_arkui_listitemswipeactionitem_setonactionwithuserdata) | - | 设置组件进入长距删除区后删除ListItem时调用的事件，回调事件会传入用户自定义数据。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnExitActionArea(ArkUI\_ListItemSwipeActionItem\* item, void (\*callback)())](capi-native-type-h.md#oh_arkui_listitemswipeactionitem_setonexitactionarea) | - | 设置滑动条目退出删除区域时调用的事件。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnExitActionAreaWithUserData (ArkUI\_ListItemSwipeActionItem\* item,void\* userData, void (\*callback)(void\* userData))](capi-native-type-h.md#oh_arkui_listitemswipeactionitem_setonexitactionareawithuserdata) | - | 设置滑动条目退出删除区域时调用的事件，回调事件会传入用户自定义数据。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnStateChange (ArkUI\_ListItemSwipeActionItem\* item,void (\*callback)(ArkUI\_ListItemSwipeActionState swipeActionState))](capi-native-type-h.md#oh_arkui_listitemswipeactionitem_setonstatechange) | - | 设置列表项滑动状态变化时候触发的事件。 |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnStateChangeWithUserData (ArkUI\_ListItemSwipeActionItem\* item,void\* userData, void (\*callback)(ArkUI\_ListItemSwipeActionState swipeActionState, void\* userData))](capi-native-type-h.md#oh_arkui_listitemswipeactionitem_setonstatechangewithuserdata) | - | 设置列表项滑动状态变化时候触发的事件，回调事件会传入用户自定义数据。 |
| [ArkUI\_ListItemSwipeActionOption\* OH\_ArkUI\_ListItemSwipeActionOption\_Create()](capi-native-type-h.md#oh_arkui_listitemswipeactionoption_create) | - | 创建ListItemSwipeActionOption接口设置的配置项。 |
| [void OH\_ArkUI\_ListItemSwipeActionOption\_Dispose(ArkUI\_ListItemSwipeActionOption\* option)](capi-native-type-h.md#oh_arkui_listitemswipeactionoption_dispose) | - | 销毁ListItemSwipeActionOption实例。 |
| [void OH\_ArkUI\_ListItemSwipeActionOption\_SetStart(ArkUI\_ListItemSwipeActionOption\* option, ArkUI\_ListItemSwipeActionItem\* item)](capi-native-type-h.md#oh_arkui_listitemswipeactionoption_setstart) | - | 设置ListItemSwipeActionItem的左侧（垂直布局）或上方（横向布局）布局内容。 |
| [void OH\_ArkUI\_ListItemSwipeActionOption\_SetEnd(ArkUI\_ListItemSwipeActionOption\* option, ArkUI\_ListItemSwipeActionItem\* item)](capi-native-type-h.md#oh_arkui_listitemswipeactionoption_setend) | - | 设置ListItemSwipeActionItem的右侧（垂直布局）或下方（横向布局）布局内容。 |
| [void OH\_ArkUI\_ListItemSwipeActionOption\_SetEdgeEffect(ArkUI\_ListItemSwipeActionOption\* option, ArkUI\_ListItemSwipeEdgeEffect edgeEffect)](capi-native-type-h.md#oh_arkui_listitemswipeactionoption_setedgeeffect) | - | 设置边缘滑动效果。 |
| [int32\_t OH\_ArkUI\_ListItemSwipeActionOption\_GetEdgeEffect(ArkUI\_ListItemSwipeActionOption\* option)](capi-native-type-h.md#oh_arkui_listitemswipeactionoption_getedgeeffect) | - | 获取边缘滑动效果。 |
| [void OH\_ArkUI\_ListItemSwipeActionOption\_SetOnOffsetChange(ArkUI\_ListItemSwipeActionOption\* option, void (\*callback)(float offset))](capi-native-type-h.md#oh_arkui_listitemswipeactionoption_setonoffsetchange) | - | 滑动操作偏移量更改时调用的事件。 |
| [void OH\_ArkUI\_ListItemSwipeActionOption\_SetOnOffsetChangeWithUserData (ArkUI\_ListItemSwipeActionOption\* option, void\* userData, void (\*callback)(float offset, void\* userData))](capi-native-type-h.md#oh_arkui_listitemswipeactionoption_setonoffsetchangewithuserdata) | - | 滑动操作偏移量更改时调用的事件，回调事件会传入用户自定义数据。 |
| [int32\_t OH\_ArkUI\_ListItemSwipeAction\_Expand(ArkUI\_NodeHandle node, ArkUI\_ListItemSwipeActionDirection direction)](capi-native-type-h.md#oh_arkui_listitemswipeaction_expand) | - | 展开指定ListItem的划出菜单。 |
| [int32\_t OH\_ArkUI\_ListItemSwipeAction\_Collapse(ArkUI\_NodeHandle node)](capi-native-type-h.md#oh_arkui_listitemswipeaction_collapse) | - | 收起指定ListItem的划出菜单。 |
| [ArkUI\_AccessibilityState\* OH\_ArkUI\_AccessibilityState\_Create(void)](capi-native-type-h.md#oh_arkui_accessibilitystate_create) | - | 创建无障碍状态。 |
| [void OH\_ArkUI\_AccessibilityState\_Dispose(ArkUI\_AccessibilityState\* state)](capi-native-type-h.md#oh_arkui_accessibilitystate_dispose) | - | 销毁无障碍状态指针。 |
| [void OH\_ArkUI\_AccessibilityState\_SetDisabled(ArkUI\_AccessibilityState\* state, int32\_t isDisabled)](capi-native-type-h.md#oh_arkui_accessibilitystate_setdisabled) | - | 设置无障碍状态是否禁用。 |
| [int32\_t OH\_ArkUI\_AccessibilityState\_IsDisabled(ArkUI\_AccessibilityState\* state)](capi-native-type-h.md#oh_arkui_accessibilitystate_isdisabled) | - | 获取无障碍状态是否禁用。 |
| [void OH\_ArkUI\_AccessibilityState\_SetSelected(ArkUI\_AccessibilityState\* state, int32\_t isSelected)](capi-native-type-h.md#oh_arkui_accessibilitystate_setselected) | - | 设置无障碍状态是否选中。 |
| [int32\_t OH\_ArkUI\_AccessibilityState\_IsSelected(ArkUI\_AccessibilityState\* state)](capi-native-type-h.md#oh_arkui_accessibilitystate_isselected) | - | 获取无障碍状态是否选中。 |
| [void OH\_ArkUI\_AccessibilityState\_SetCheckedState(ArkUI\_AccessibilityState\* state, int32\_t checkedState)](capi-native-type-h.md#oh_arkui_accessibilitystate_setcheckedstate) | - | 设置无障碍状态复选框状态。 |
| [int32\_t OH\_ArkUI\_AccessibilityState\_GetCheckedState(ArkUI\_AccessibilityState\* state)](capi-native-type-h.md#oh_arkui_accessibilitystate_getcheckedstate) | - | 获取无障碍状态复选框状态。 |
| [ArkUI\_AccessibilityValue\* OH\_ArkUI\_AccessibilityValue\_Create(void)](capi-native-type-h.md#oh_arkui_accessibilityvalue_create) | - | 创建无障碍信息。 |
| [void OH\_ArkUI\_AccessibilityValue\_Dispose(ArkUI\_AccessibilityValue\* value)](capi-native-type-h.md#oh_arkui_accessibilityvalue_dispose) | - | 销毁无障碍信息指针。 |
| [void OH\_ArkUI\_AccessibilityValue\_SetMin(ArkUI\_AccessibilityValue\* value, int32\_t min)](capi-native-type-h.md#oh_arkui_accessibilityvalue_setmin) | - | 设置无障碍最小值信息。 |
| [int32\_t OH\_ArkUI\_AccessibilityValue\_GetMin(ArkUI\_AccessibilityValue\* value)](capi-native-type-h.md#oh_arkui_accessibilityvalue_getmin) | - | 获取无障碍最小值信息。 |
| [void OH\_ArkUI\_AccessibilityValue\_SetMax(ArkUI\_AccessibilityValue\* value, int32\_t max)](capi-native-type-h.md#oh_arkui_accessibilityvalue_setmax) | - | 设置无障碍最大值信息。 |
| [int32\_t OH\_ArkUI\_AccessibilityValue\_GetMax(ArkUI\_AccessibilityValue\* value)](capi-native-type-h.md#oh_arkui_accessibilityvalue_getmax) | - | 获取无障碍最大值信息。 |
| [void OH\_ArkUI\_AccessibilityValue\_SetCurrent(ArkUI\_AccessibilityValue\* value, int32\_t current)](capi-native-type-h.md#oh_arkui_accessibilityvalue_setcurrent) | - | 设置无障碍当前值信息。 |
| [int32\_t OH\_ArkUI\_AccessibilityValue\_GetCurrent(ArkUI\_AccessibilityValue\* value)](capi-native-type-h.md#oh_arkui_accessibilityvalue_getcurrent) | - | 获取无障碍当前值信息。 |
| [void OH\_ArkUI\_AccessibilityValue\_SetRangeMin(ArkUI\_AccessibilityValue\* value, int32\_t rangeMin)](capi-native-type-h.md#oh_arkui_accessibilityvalue_setrangemin) | - | 设置范围组件的无障碍最小值信息。 |
| [int32\_t OH\_ArkUI\_AccessibilityValue\_GetRangeMin(ArkUI\_AccessibilityValue\* value)](capi-native-type-h.md#oh_arkui_accessibilityvalue_getrangemin) | - | 获取范围组件的无障碍最小值信息。 |
| [void OH\_ArkUI\_AccessibilityValue\_SetRangeMax(ArkUI\_AccessibilityValue\* value, int32\_t rangeMax)](capi-native-type-h.md#oh_arkui_accessibilityvalue_setrangemax) | - | 设置范围组件的无障碍最大值信息。 |
| [int32\_t OH\_ArkUI\_AccessibilityValue\_GetRangeMax(ArkUI\_AccessibilityValue\* value)](capi-native-type-h.md#oh_arkui_accessibilityvalue_getrangemax) | - | 获取范围组件的无障碍最大值信息。 |
| [void OH\_ArkUI\_AccessibilityValue\_SetRangeCurrent(ArkUI\_AccessibilityValue\* value, int32\_t rangeCurrent)](capi-native-type-h.md#oh_arkui_accessibilityvalue_setrangecurrent) | - | 用于设置范围组件的无障碍当前值信息。 |
| [int32\_t OH\_ArkUI\_AccessibilityValue\_GetRangeCurrent(ArkUI\_AccessibilityValue\* value)](capi-native-type-h.md#oh_arkui_accessibilityvalue_getrangecurrent) | - | 用于获取范围组件的无障碍当前值信息。 |
| [void OH\_ArkUI\_AccessibilityValue\_SetText(ArkUI\_AccessibilityValue\* value, const char\* text)](capi-native-type-h.md#oh_arkui_accessibilityvalue_settext) | - | 设置无障碍文本描述信息。 |
| [const char\* OH\_ArkUI\_AccessibilityValue\_GetText(ArkUI\_AccessibilityValue\* value)](capi-native-type-h.md#oh_arkui_accessibilityvalue_gettext) | - | 获取无障碍文本描述信息。 |
| [ArkUI\_ImageAnimatorFrameInfo\* OH\_ArkUI\_ImageAnimatorFrameInfo\_CreateFromString(char\* src)](capi-native-type-h.md#oh_arkui_imageanimatorframeinfo_createfromstring) | - | 使用图片路径创建帧图片信息，图片格式为svg、png和jpg。 |
| [ArkUI\_ImageAnimatorFrameInfo\* OH\_ArkUI\_ImageAnimatorFrameInfo\_CreateFromDrawableDescriptor(ArkUI\_DrawableDescriptor\* drawable)](capi-native-type-h.md#oh_arkui_imageanimatorframeinfo_createfromdrawabledescriptor) | - | 使用 DrawableDescriptor 对象创建帧图片信息，图片格式为Resource和PixelMap。 |
| [void OH\_ArkUI\_ImageAnimatorFrameInfo\_Dispose(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)](capi-native-type-h.md#oh_arkui_imageanimatorframeinfo_dispose) | - | 销毁帧图片对象指针。 |
| [void OH\_ArkUI\_ImageAnimatorFrameInfo\_SetWidth(ArkUI\_ImageAnimatorFrameInfo\* imageInfo, int32\_t width)](capi-native-type-h.md#oh_arkui_imageanimatorframeinfo_setwidth) | - | 设置图片宽度。 |
| [int32\_t OH\_ArkUI\_ImageAnimatorFrameInfo\_GetWidth(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)](capi-native-type-h.md#oh_arkui_imageanimatorframeinfo_getwidth) | - | 获取图片宽度。 |
| [void OH\_ArkUI\_ImageAnimatorFrameInfo\_SetHeight(ArkUI\_ImageAnimatorFrameInfo\* imageInfo, int32\_t height)](capi-native-type-h.md#oh_arkui_imageanimatorframeinfo_setheight) | - | 设置图片高度。 |
| [int32\_t OH\_ArkUI\_ImageAnimatorFrameInfo\_GetHeight(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)](capi-native-type-h.md#oh_arkui_imageanimatorframeinfo_getheight) | - | 获取图片高度。 |
| [void OH\_ArkUI\_ImageAnimatorFrameInfo\_SetTop(ArkUI\_ImageAnimatorFrameInfo\* imageInfo, int32\_t top)](capi-native-type-h.md#oh_arkui_imageanimatorframeinfo_settop) | - | 设置图片相对于组件左上角的纵向坐标。 |
| [int32\_t OH\_ArkUI\_ImageAnimatorFrameInfo\_GetTop(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)](capi-native-type-h.md#oh_arkui_imageanimatorframeinfo_gettop) | - | 获取图片相对于组件左上角的纵向坐标。 |
| [void OH\_ArkUI\_ImageAnimatorFrameInfo\_SetLeft(ArkUI\_ImageAnimatorFrameInfo\* imageInfo, int32\_t left)](capi-native-type-h.md#oh_arkui_imageanimatorframeinfo_setleft) | - | 设置图片相对于组件左上角的横向坐标。 |
| [int32\_t OH\_ArkUI\_ImageAnimatorFrameInfo\_GetLeft(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)](capi-native-type-h.md#oh_arkui_imageanimatorframeinfo_getleft) | - | 获取图片相对于组件左上角的横向坐标。 |
| [void OH\_ArkUI\_ImageAnimatorFrameInfo\_SetDuration(ArkUI\_ImageAnimatorFrameInfo\* imageInfo, int32\_t duration)](capi-native-type-h.md#oh_arkui_imageanimatorframeinfo_setduration) | - | 设置图片的播放时长。 |
| [int32\_t OH\_ArkUI\_ImageAnimatorFrameInfo\_GetDuration(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)](capi-native-type-h.md#oh_arkui_imageanimatorframeinfo_getduration) | - | 获取图片的播放时长。 |
| [ArkUI\_ListChildrenMainSize\* OH\_ArkUI\_ListChildrenMainSizeOption\_Create()](capi-native-type-h.md#oh_arkui_listchildrenmainsizeoption_create) | - | 创建ListChildrenMainSize接口设置的配置项。 |
| [void OH\_ArkUI\_ListChildrenMainSizeOption\_Dispose(ArkUI\_ListChildrenMainSize\* option)](capi-native-type-h.md#oh_arkui_listchildrenmainsizeoption_dispose) | - | 销毁ListChildrenMainSize实例。 |
| [int32\_t OH\_ArkUI\_ListChildrenMainSizeOption\_SetDefaultMainSize(ArkUI\_ListChildrenMainSize\* option, float defaultMainSize)](capi-native-type-h.md#oh_arkui_listchildrenmainsizeoption_setdefaultmainsize) | - | 设置List组件列表项在主轴方向的默认尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。 |
| [float OH\_ArkUI\_ListChildrenMainSizeOption\_GetDefaultMainSize(ArkUI\_ListChildrenMainSize\* option)](capi-native-type-h.md#oh_arkui_listchildrenmainsizeoption_getdefaultmainsize) | - | 获取List组件的列表项在主轴方向的默认尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。 |
| [void OH\_ArkUI\_ListChildrenMainSizeOption\_Resize(ArkUI\_ListChildrenMainSize\* option, int32\_t totalSize)](capi-native-type-h.md#oh_arkui_listchildrenmainsizeoption_resize) | - | 调整List组件子项主轴尺寸数组的容量大小。 |
| [int32\_t OH\_ArkUI\_ListChildrenMainSizeOption\_Splice(ArkUI\_ListChildrenMainSize\* option, int32\_t index, int32\_t deleteCount, int32\_t addCount)](capi-native-type-h.md#oh_arkui_listchildrenmainsizeoption_splice) | - | 对List组件子项主轴尺寸数组进行大小调整。 |
| [int32\_t OH\_ArkUI\_ListChildrenMainSizeOption\_UpdateSize(ArkUI\_ListChildrenMainSize\* option, int32\_t index, float mainSize)](capi-native-type-h.md#oh_arkui_listchildrenmainsizeoption_updatesize) | - | 更新List组件子项主轴尺寸数组中指定索引位置的尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。 |
| [float OH\_ArkUI\_ListChildrenMainSizeOption\_GetMainSize(ArkUI\_ListChildrenMainSize\* option, int32\_t index)](capi-native-type-h.md#oh_arkui_listchildrenmainsizeoption_getmainsize) | - | 获取List组件子项主轴尺寸数组中指定索引位置的尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。 |
| [ArkUI\_CustomSpanMeasureInfo\* OH\_ArkUI\_CustomSpanMeasureInfo\_Create(void)](capi-native-type-h.md#oh_arkui_customspanmeasureinfo_create) | - | 创建自定义段落组件测量信息。 |
| [void OH\_ArkUI\_CustomSpanMeasureInfo\_Dispose(ArkUI\_CustomSpanMeasureInfo\* info)](capi-native-type-h.md#oh_arkui_customspanmeasureinfo_dispose) | - | 销毁自定义段落组件测量信息。 |
| [float OH\_ArkUI\_CustomSpanMeasureInfo\_GetFontSize(ArkUI\_CustomSpanMeasureInfo\* info)](capi-native-type-h.md#oh_arkui_customspanmeasureinfo_getfontsize) | - | 获取自定义段落组件的父节点Text的字体大小。 |
| [ArkUI\_CustomSpanMetrics\* OH\_ArkUI\_CustomSpanMetrics\_Create(void)](capi-native-type-h.md#oh_arkui_customspanmetrics_create) | - | 创建自定义段落组件度量信息。 |
| [void OH\_ArkUI\_CustomSpanMetrics\_Dispose(ArkUI\_CustomSpanMetrics\* metrics)](capi-native-type-h.md#oh_arkui_customspanmetrics_dispose) | - | 销毁自定义段落组件度量信息。 |
| [int32\_t OH\_ArkUI\_CustomSpanMetrics\_SetWidth(ArkUI\_CustomSpanMetrics\* metrics, float width)](capi-native-type-h.md#oh_arkui_customspanmetrics_setwidth) | - | 设置自定义段落组件的宽度。 |
| [int32\_t OH\_ArkUI\_CustomSpanMetrics\_SetHeight(ArkUI\_CustomSpanMetrics\* metrics, float height)](capi-native-type-h.md#oh_arkui_customspanmetrics_setheight) | - | 设置自定义段落组件的高度。 |
| [ArkUI\_CustomSpanDrawInfo\* OH\_ArkUI\_CustomSpanDrawInfo\_Create(void)](capi-native-type-h.md#oh_arkui_customspandrawinfo_create) | - | 创建自定义段落组件绘制信息。 |
| [void OH\_ArkUI\_CustomSpanDrawInfo\_Dispose(ArkUI\_CustomSpanDrawInfo\* info)](capi-native-type-h.md#oh_arkui_customspandrawinfo_dispose) | - | 销毁自定义段落组件绘制信息。 |
| [float OH\_ArkUI\_CustomSpanDrawInfo\_GetXOffset(ArkUI\_CustomSpanDrawInfo\* info)](capi-native-type-h.md#oh_arkui_customspandrawinfo_getxoffset) | - | 获取自定义段落组件相对于挂载组件的x轴偏移值。 |
| [float OH\_ArkUI\_CustomSpanDrawInfo\_GetLineTop(ArkUI\_CustomSpanDrawInfo\* info)](capi-native-type-h.md#oh_arkui_customspandrawinfo_getlinetop) | - | 获取自定义段落组件相对于挂载组件的上边距。 |
| [float OH\_ArkUI\_CustomSpanDrawInfo\_GetLineBottom(ArkUI\_CustomSpanDrawInfo\* info)](capi-native-type-h.md#oh_arkui_customspandrawinfo_getlinebottom) | - | 获取自定义段落组件相对于挂载组件的下边距。 |
| [float OH\_ArkUI\_CustomSpanDrawInfo\_GetBaseline(ArkUI\_CustomSpanDrawInfo\* info)](capi-native-type-h.md#oh_arkui_customspandrawinfo_getbaseline) | - | 获取自定义段落组件相对于挂载组件的基线偏移量。 |
| [void OH\_ArkUI\_CustomProperty\_Destroy(ArkUI\_CustomProperty\* handle)](capi-native-type-h.md#oh_arkui_customproperty_destroy) | - | 销毁CustomProperty实例。 |
| [const char\* OH\_ArkUI\_CustomProperty\_GetStringValue(ArkUI\_CustomProperty\* handle)](capi-native-type-h.md#oh_arkui_customproperty_getstringvalue) | - | 获取自定义属性value信息。 |
| [const char\* OH\_ArkUI\_HostWindowInfo\_GetName(ArkUI\_HostWindowInfo\* info)](capi-native-type-h.md#oh_arkui_hostwindowinfo_getname) | - | 获取HostWindowInfo对象中的窗口名称。 |
| [void OH\_ArkUI\_HostWindowInfo\_Destroy(ArkUI\_HostWindowInfo\* info)](capi-native-type-h.md#oh_arkui_hostwindowinfo_destroy) | - | 销毁HostWindowInfo对象。 |
| [void OH\_ArkUI\_ActiveChildrenInfo\_Destroy(ArkUI\_ActiveChildrenInfo\* handle)](capi-native-type-h.md#oh_arkui_activechildreninfo_destroy) | - | 销毁ActiveChildrenInfo实例。 |
| [ArkUI\_NodeHandle OH\_ArkUI\_ActiveChildrenInfo\_GetNodeByIndex(ArkUI\_ActiveChildrenInfo\* handle, int32\_t index)](capi-native-type-h.md#oh_arkui_activechildreninfo_getnodebyindex) | - | 获取ActiveChildrenInfo结构体的下标为index的子节点。 |
| [int32\_t OH\_ArkUI\_ActiveChildrenInfo\_GetCount(ArkUI\_ActiveChildrenInfo\* handle)](capi-native-type-h.md#oh_arkui_activechildreninfo_getcount) | - | 获取ActiveChildrenInfo结构体内的节点数量。 |
| [ArkUI\_ProgressLinearStyleOption\* OH\_ArkUI\_ProgressLinearStyleOption\_Create(void)](capi-native-type-h.md#oh_arkui_progresslinearstyleoption_create) | - | 创建线性进度条样式信息。 |
| [void OH\_ArkUI\_ProgressLinearStyleOption\_Destroy(ArkUI\_ProgressLinearStyleOption\* option)](capi-native-type-h.md#oh_arkui_progresslinearstyleoption_destroy) | - | 销毁线性进度条样式信息。 |
| [void OH\_ArkUI\_ProgressLinearStyleOption\_SetSmoothEffectEnabled(ArkUI\_ProgressLinearStyleOption\* option, bool enabled)](capi-native-type-h.md#oh_arkui_progresslinearstyleoption_setsmootheffectenabled) | - | 设置进度平滑动效的开关。 |
| [void OH\_ArkUI\_ProgressLinearStyleOption\_SetScanEffectEnabled(ArkUI\_ProgressLinearStyleOption\* option, bool enabled)](capi-native-type-h.md#oh_arkui_progresslinearstyleoption_setscaneffectenabled) | - | 设置扫光效果的开关。 |
| [void OH\_ArkUI\_ProgressLinearStyleOption\_SetStrokeWidth(ArkUI\_ProgressLinearStyleOption\* option, float strokeWidth)](capi-native-type-h.md#oh_arkui_progresslinearstyleoption_setstrokewidth) | - | 设置进度条宽度。 |
| [void OH\_ArkUI\_ProgressLinearStyleOption\_SetStrokeRadius(ArkUI\_ProgressLinearStyleOption\* option, float strokeRadius)](capi-native-type-h.md#oh_arkui_progresslinearstyleoption_setstrokeradius) | - | 设置进度条圆角半径。 |
| [bool OH\_ArkUI\_ProgressLinearStyleOption\_GetSmoothEffectEnabled(ArkUI\_ProgressLinearStyleOption\* option)](capi-native-type-h.md#oh_arkui_progresslinearstyleoption_getsmootheffectenabled) | - | 获取进度平滑动效的开关信息。 |
| [bool OH\_ArkUI\_ProgressLinearStyleOption\_GetScanEffectEnabled(ArkUI\_ProgressLinearStyleOption\* option)](capi-native-type-h.md#oh_arkui_progresslinearstyleoption_getscaneffectenabled) | - | 获取扫光效果的开关信息。 |
| [float OH\_ArkUI\_ProgressLinearStyleOption\_GetStrokeWidth(ArkUI\_ProgressLinearStyleOption\* option)](capi-native-type-h.md#oh_arkui_progresslinearstyleoption_getstrokewidth) | - | 获取进度条宽度。 |
| [float OH\_ArkUI\_ProgressLinearStyleOption\_GetStrokeRadius(ArkUI\_ProgressLinearStyleOption\* option)](capi-native-type-h.md#oh_arkui_progresslinearstyleoption_getstrokeradius) | - | 获取进度条圆角半径值。 |
| [ArkUI\_SnapshotOptions\* OH\_ArkUI\_CreateSnapshotOptions()](capi-native-type-h.md#oh_arkui_createsnapshotoptions) | - | 创建一个截图选项，当返回值不再使用时必须通过[OH\_ArkUI\_DestroySnapshotOptions()](capi-native-type-h.md#oh_arkui_destroysnapshotoptions)释放。 |
| [void OH\_ArkUI\_DestroySnapshotOptions(ArkUI\_SnapshotOptions\* snapshotOptions)](capi-native-type-h.md#oh_arkui_destroysnapshotoptions) | - | 销毁截图选项指针。 |
| [int32\_t OH\_ArkUI\_SnapshotOptions\_SetScale(ArkUI\_SnapshotOptions\* snapshotOptions, float scale)](capi-native-type-h.md#oh_arkui_snapshotoptions_setscale) | - | 配置截图选项中的缩放属性。 |
| [int32\_t OH\_ArkUI\_SnapshotOptions\_SetColorMode(ArkUI\_SnapshotOptions\* snapshotOptions, int32\_t colorSpace, bool isAuto)](capi-native-type-h.md#oh_arkui_snapshotoptions_setcolormode) | - | 设置截图选项中的色彩空间。 |
| [int32\_t OH\_ArkUI\_SnapshotOptions\_SetDynamicRangeMode(ArkUI\_SnapshotOptions\* snapshotOptions, int32\_t dynamicRangeMode, bool isAuto)](capi-native-type-h.md#oh_arkui_snapshotoptions_setdynamicrangemode) | - | 设置截图选项中的动态范围模式。 |
| [ArkUI\_CrossLanguageOption\* OH\_ArkUI\_CrossLanguageOption\_Create(void)](capi-native-type-h.md#oh_arkui_crosslanguageoption_create) | - | 创建跨语言配置项实例。 |
| [void OH\_ArkUI\_CrossLanguageOption\_Destroy(ArkUI\_CrossLanguageOption\* option)](capi-native-type-h.md#oh_arkui_crosslanguageoption_destroy) | - | 销毁跨语言配置项实例。 |
| [void OH\_ArkUI\_CrossLanguageOption\_SetAttributeSettingStatus(ArkUI\_CrossLanguageOption\* option, bool enabled)](capi-native-type-h.md#oh_arkui_crosslanguageoption_setattributesettingstatus) | - | 设置配置项中是否允许跨语言修改属性。 |
| [bool OH\_ArkUI\_CrossLanguageOption\_GetAttributeSettingStatus(ArkUI\_CrossLanguageOption\* option)](capi-native-type-h.md#oh_arkui_crosslanguageoption_getattributesettingstatus) | - | 获取配置项中是否允许跨语言修改属性。 |
| [ArkUI\_VisibleAreaEventOptions\* OH\_ArkUI\_VisibleAreaEventOptions\_Create()](capi-native-type-h.md#oh_arkui_visibleareaeventoptions_create) | - | 创建可见区域变化监听的参数。 |
| [void OH\_ArkUI\_VisibleAreaEventOptions\_Dispose(ArkUI\_VisibleAreaEventOptions\* option)](capi-native-type-h.md#oh_arkui_visibleareaeventoptions_dispose) | - | 销毁可见区域变化监听的参数。 |
| [int32\_t OH\_ArkUI\_VisibleAreaEventOptions\_SetRatios(ArkUI\_VisibleAreaEventOptions\* option, float\* value, int32\_t size)](capi-native-type-h.md#oh_arkui_visibleareaeventoptions_setratios) | - | 设置阈值数组。 |
| [int32\_t OH\_ArkUI\_VisibleAreaEventOptions\_SetExpectedUpdateInterval(ArkUI\_VisibleAreaEventOptions \*option, int32\_t value)](capi-native-type-h.md#oh_arkui_visibleareaeventoptions_setexpectedupdateinterval) | - | 设置预期更新间隔，单位为ms。定义了开发者期望的更新间隔。 |
| [int32\_t OH\_ArkUI\_VisibleAreaEventOptions\_SetMeasureFromViewport(ArkUI\_VisibleAreaEventOptions \*option, bool measureFromViewport)](capi-native-type-h.md#oh_arkui_visibleareaeventoptions_setmeasurefromviewport) | - | 设置可见区域计算模式。 |
| [int32\_t OH\_ArkUI\_VisibleAreaEventOptions\_GetRatios(ArkUI\_VisibleAreaEventOptions\* option, float\* value, int32\_t\* size)](capi-native-type-h.md#oh_arkui_visibleareaeventoptions_getratios) | - | 获取阈值数组。 |
| [int32\_t OH\_ArkUI\_VisibleAreaEventOptions\_GetExpectedUpdateInterval(ArkUI\_VisibleAreaEventOptions\* option)](capi-native-type-h.md#oh_arkui_visibleareaeventoptions_getexpectedupdateinterval) | - | 获取预期更新间隔。 |
| [bool OH\_ArkUI\_VisibleAreaEventOptions\_GetMeasureFromViewport(ArkUI\_VisibleAreaEventOptions\* option)](capi-native-type-h.md#oh_arkui_visibleareaeventoptions_getmeasurefromviewport) | - | 获取可见区域计算模式。 |
| [ArkUI\_TextPickerRangeContentArray\* OH\_ArkUI\_TextPickerRangeContentArray\_Create(int32\_t length)](capi-native-type-h.md#oh_arkui_textpickerrangecontentarray_create) | - | 创建TextPickerRangeContent数组的对象。 |
| [void OH\_ArkUI\_TextPickerRangeContentArray\_SetIconAtIndex(ArkUI\_TextPickerRangeContentArray\* handle, char\* icon, int32\_t index)](capi-native-type-h.md#oh_arkui_textpickerrangecontentarray_seticonatindex) | - | 设置TextPickerRangeContent数组指定位置的icon数据。 |
| [void OH\_ArkUI\_TextPickerRangeContentArray\_SetTextAtIndex(ArkUI\_TextPickerRangeContentArray\* handle, char\* text, int32\_t index)](capi-native-type-h.md#oh_arkui_textpickerrangecontentarray_settextatindex) | - | 设置TextPickerRangeContent数组指定位置的text数据。 |
| [void OH\_ArkUI\_TextPickerRangeContentArray\_Destroy(ArkUI\_TextPickerRangeContentArray\* handle)](capi-native-type-h.md#oh_arkui_textpickerrangecontentarray_destroy) | - | 删除TextPickerRangeContent数组对象。 |
| [ArkUI\_TextCascadePickerRangeContentArray\* OH\_ArkUI\_TextCascadePickerRangeContentArray\_Create(int32\_t length)](capi-native-type-h.md#oh_arkui_textcascadepickerrangecontentarray_create) | - | 创建TextCascadePickerRangeContent数组对象。 |
| [void OH\_ArkUI\_TextCascadePickerRangeContentArray\_SetTextAtIndex (ArkUI\_TextCascadePickerRangeContentArray\* handle, char\* text, int32\_t index)](capi-native-type-h.md#oh_arkui_textcascadepickerrangecontentarray_settextatindex) | - | 设置TextCascadePickerRangeContent数组指定位置的text数据。 |
| [void OH\_ArkUI\_TextCascadePickerRangeContentArray\_SetChildAtIndex (ArkUI\_TextCascadePickerRangeContentArray\* handle, ArkUI\_TextCascadePickerRangeContentArray\* child, int32\_t index)](capi-native-type-h.md#oh_arkui_textcascadepickerrangecontentarray_setchildatindex) | - | 设置TextCascadePickerRangeContent数组指定位置的child数据。 |
| [void OH\_ArkUI\_TextCascadePickerRangeContentArray\_Destroy (ArkUI\_TextCascadePickerRangeContentArray\* handle)](capi-native-type-h.md#oh_arkui_textcascadepickerrangecontentarray_destroy) | - | 删除TextCascadePickerRangeContent数组对象。 |
| [ArkUI\_EmbeddedComponentOption\* OH\_ArkUI\_EmbeddedComponentOption\_Create()](capi-native-type-h.md#oh_arkui_embeddedcomponentoption_create) | - | 创建EmbeddedComponent组件选项的对象。 |
| [void OH\_ArkUI\_EmbeddedComponentOption\_Dispose(ArkUI\_EmbeddedComponentOption\* option)](capi-native-type-h.md#oh_arkui_embeddedcomponentoption_dispose) | - | 删除EmbeddedComponent组件选项的对象。 |
| [void OH\_ArkUI\_EmbeddedComponentOption\_SetOnError (ArkUI\_EmbeddedComponentOption\* option, void (\*callback)(int32\_t code, const char\* name, const char\* message))](capi-native-type-h.md#oh_arkui_embeddedcomponentoption_setonerror) | - | 设置EmbeddedComponent组件的onError回调。EmbeddedComponent组件在运行过程中发生异常时触发本回调。 |
| [void OH\_ArkUI\_EmbeddedComponentOption\_SetOnTerminated (ArkUI\_EmbeddedComponentOption\* option, void (\*callback)(int32\_t code, AbilityBase\_Want\* want))](capi-native-type-h.md#oh_arkui_embeddedcomponentoption_setonterminated) | - | 设置EmbeddedComponent组件的onTerminated回调。EmbeddedComponent组件正常退出时触发本回调。 |
| [ArkUI\_PositionEdges\* OH\_ArkUI\_PositionEdges\_Create()](capi-native-type-h.md#oh_arkui_positionedges_create) | - | 创建PositionEdges属性对象。 |
| [ArkUI\_PositionEdges\* OH\_ArkUI\_PositionEdges\_Copy(const ArkUI\_PositionEdges\* edges)](capi-native-type-h.md#oh_arkui_positionedges_copy) | - | 深拷贝PositionEdges属性对象。 |
| [void OH\_ArkUI\_PositionEdges\_Dispose(ArkUI\_PositionEdges\* edges)](capi-native-type-h.md#oh_arkui_positionedges_dispose) | - | 销毁PositionEdges属性对象。 |
| [void OH\_ArkUI\_PositionEdges\_SetTop(ArkUI\_PositionEdges\* edges, float value)](capi-native-type-h.md#oh_arkui_positionedges_settop) | - | 设置PositionEdges属性对象的上方向值。 |
| [int32\_t OH\_ArkUI\_PositionEdges\_GetTop(ArkUI\_PositionEdges\* edges, float\* value)](capi-native-type-h.md#oh_arkui_positionedges_gettop) | - | 获取PositionEdges属性对象的上方向值。 |
| [void OH\_ArkUI\_PositionEdges\_SetLeft(ArkUI\_PositionEdges\* edges, float value)](capi-native-type-h.md#oh_arkui_positionedges_setleft) | - | 设置PositionEdges属性对象的左方向值。 |
| [int32\_t OH\_ArkUI\_PositionEdges\_GetLeft(ArkUI\_PositionEdges\* edges, float\* value)](capi-native-type-h.md#oh_arkui_positionedges_getleft) | - | 获取PositionEdges属性对象的左方向值。 |
| [void OH\_ArkUI\_PositionEdges\_SetBottom(ArkUI\_PositionEdges\* edges, float value)](capi-native-type-h.md#oh_arkui_positionedges_setbottom) | - | 设置PositionEdges属性对象的下方向值。 |
| [int32\_t OH\_ArkUI\_PositionEdges\_GetBottom(ArkUI\_PositionEdges\* edges, float\* value)](capi-native-type-h.md#oh_arkui_positionedges_getbottom) | - | 获取PositionEdges属性对象的下方向值。 |
| [void OH\_ArkUI\_PositionEdges\_SetRight(ArkUI\_PositionEdges\* edges, float value)](capi-native-type-h.md#oh_arkui_positionedges_setright) | - | 设置PositionEdges属性对象的右方向值。 |
| [int32\_t OH\_ArkUI\_PositionEdges\_GetRight(ArkUI\_PositionEdges\* edges, float\* value)](capi-native-type-h.md#oh_arkui_positionedges_getright) | - | 获取PositionEdges属性对象的右方向值。 |
| [ArkUI\_PixelRoundPolicy\* OH\_ArkUI\_PixelRoundPolicy\_Create()](capi-native-type-h.md#oh_arkui_pixelroundpolicy_create) | - | 创建PixelRoundPolicy属性对象。 |
| [void OH\_ArkUI\_PixelRoundPolicy\_Dispose(ArkUI\_PixelRoundPolicy\* policy)](capi-native-type-h.md#oh_arkui_pixelroundpolicy_dispose) | - | 释放PixelRoundPolicy属性对象。 |
| [void OH\_ArkUI\_PixelRoundPolicy\_SetTop(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy value)](capi-native-type-h.md#oh_arkui_pixelroundpolicy_settop) | - | 设置PixelRoundPolicy属性对象的上部方向值。 |
| [int32\_t OH\_ArkUI\_PixelRoundPolicy\_GetTop(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy\* value)](capi-native-type-h.md#oh_arkui_pixelroundpolicy_gettop) | - | 获取PixelRoundPolicy属性对象的上部方向值。 |
| [void OH\_ArkUI\_PixelRoundPolicy\_SetStart(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy value)](capi-native-type-h.md#oh_arkui_pixelroundpolicy_setstart) | - | 设置PixelRoundPolicy属性对象的前部方向值。 |
| [int32\_t OH\_ArkUI\_PixelRoundPolicy\_GetStart(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy\* value)](capi-native-type-h.md#oh_arkui_pixelroundpolicy_getstart) | - | 获取PixelRoundPolicy属性对象的前部方向值。 |
| [void OH\_ArkUI\_PixelRoundPolicy\_SetBottom(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy value)](capi-native-type-h.md#oh_arkui_pixelroundpolicy_setbottom) | - | 设置PixelRoundPolicy属性对象的下部方向值。 |
| [int32\_t OH\_ArkUI\_PixelRoundPolicy\_GetBottom(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy\* value)](capi-native-type-h.md#oh_arkui_pixelroundpolicy_getbottom) | - | 获取PixelRoundPolicy属性对象的下部方向值。 |
| [void OH\_ArkUI\_PixelRoundPolicy\_SetEnd(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy value)](capi-native-type-h.md#oh_arkui_pixelroundpolicy_setend) | - | 设置PixelRoundPolicy属性对象的尾部方向值。 |
| [int32\_t OH\_ArkUI\_PixelRoundPolicy\_GetEnd(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy\* value)](capi-native-type-h.md#oh_arkui_pixelroundpolicy_getend) | - | 获取PixelRoundPolicy属性对象的尾部方向值。 |
| [ArkUI\_ContentTransitionEffect\* OH\_ArkUI\_ContentTransitionEffect\_Create(int32\_t type)](capi-native-type-h.md#oh_arkui_contenttransitioneffect_create) | - | 创建ContentTransitionEffect属性对象。 |
| [ArkUI\_GridLayoutOptions\* OH\_ArkUI\_GridLayoutOptions\_Create()](capi-native-type-h.md#oh_arkui_gridlayoutoptions_create) | - | 创建Grid布局选项。 |
| [void OH\_ArkUI\_GridLayoutOptions\_Dispose(ArkUI\_GridLayoutOptions\* option)](capi-native-type-h.md#oh_arkui_gridlayoutoptions_dispose) | - | 销毁Grid布局选项。 |
| [int32\_t OH\_ArkUI\_GridLayoutOptions\_SetIrregularIndexes(ArkUI\_GridLayoutOptions\* option, uint32\_t\* irregularIndexes, int32\_t size)](capi-native-type-h.md#oh_arkui_gridlayoutoptions_setirregularindexes) | - | 设置Grid中不规则GridItem的索引数组。 |
| [int32\_t OH\_ArkUI\_GridLayoutOptions\_GetIrregularIndexes(ArkUI\_GridLayoutOptions\* option, uint32\_t\* irregularIndexes, int32\_t\* size)](capi-native-type-h.md#oh_arkui_gridlayoutoptions_getirregularindexes) | - | 获取Grid中不规则GridItem的索引数组。当不设置OH\_ArkUI\_GridLayoutOptions\_RegisterGetIrregularSizeByIndexCallback时，irregularIndexes中GridItem的默认大小为垂直滚动Grid的一整行或水平滚动Grid的一整列。 |
| [void OH\_ArkUI\_GridLayoutOptions\_RegisterGetIrregularSizeByIndexCallback(ArkUI\_GridLayoutOptions\* option, void\* userData, ArkUI\_GridItemSize(\*callback)(int32\_t itemIndex, void\* userData))](capi-native-type-h.md#oh_arkui_gridlayoutoptions_registergetirregularsizebyindexcallback) | - | Grid布局选项通过GridItem索引获取指定Item占用的行列数。 |
| [void OH\_ArkUI\_GridLayoutOptions\_RegisterGetRectByIndexCallback(ArkUI\_GridLayoutOptions\* option, void\* userData, ArkUI\_GridItemRect (\*callback)(int32\_t itemIndex, void\* userData))](capi-native-type-h.md#oh_arkui_gridlayoutoptions_registergetrectbyindexcallback) | - | Grid布局选项通过GridItem索引获取指定Item的起始行列和占用的行列数。 |
| [ArkUI\_SelectionOptions OH\_ArkUI\_SelectionOptions\_Create()](capi-native-type-h.md#oh_arkui_selectionoptions_create) | - | 创建选择选项。 |
| [void OH\_ArkUI\_SelectionOptions\_Dispose(ArkUI\_SelectionOptions\* options)](capi-native-type-h.md#oh_arkui_selectionoptions_dispose) | - | 释放选择选项对象。 |
| [void OH\_ArkUI\_SelectionOptions\_SetMenuPolicy(ArkUI\_SelectionOptions\* options, ArkUI\_MenuPolicy menuPolicy)](capi-native-type-h.md#oh_arkui_selectionoptions_setmenupolicy) | - | 设置选择选项的菜单弹出策略。 |
| [ArkUI\_MenuPolicy OH\_ArkUI\_SelectionOptions\_GetMenuPolicy(ArkUI\_SelectionOptions\* options)](capi-native-type-h.md#oh_arkui_selectionoptions_getmenupolicy) | - | 获取选择选项的菜单弹出策略。 |
| [ArkUI\_TextContentBaseController\* OH\_ArkUI\_TextContentBaseController\_Create()](capi-native-type-h.md#oh_arkui_textcontentbasecontroller_create) | - | 创建文本内容基础控制器对象。 |
| [void OH\_ArkUI\_TextContentBaseController\_Dispose(ArkUI\_TextContentBaseController\* controller)](capi-native-type-h.md#oh_arkui_textcontentbasecontroller_dispose) | - | 销毁文本内容基础控制器对象。 |
| [void OH\_ArkUI\_TextContentBaseController\_DeleteBackward(ArkUI\_TextContentBaseController\* controller)](capi-native-type-h.md#oh_arkui_textcontentbasecontroller_deletebackward) | - | 在编辑态时删除光标前字符。其他状态删除输入框组件的最后一个字符。 |
| [void OH\_ArkUI\_TextContentBaseController\_ScrollToVisible(ArkUI\_TextContentBaseController\* controller, int32\_t start, int32\_t end)](capi-native-type-h.md#oh_arkui_textcontentbasecontroller_scrolltovisible) | - | 将起始索引与结束索引传递给与其绑定的输入框组件，并将此范围内的文字滚动到可视区域。 |
| [ArkUI\_TextMenuItem\* OH\_ArkUI\_TextMenuItem\_Create()](capi-native-type-h.md#oh_arkui_textmenuitem_create) | - | 创建文本菜单项对象。 |
| [void OH\_ArkUI\_TextMenuItem\_Dispose(ArkUI\_TextMenuItem\* textMenuItem)](capi-native-type-h.md#oh_arkui_textmenuitem_dispose) | - | 释放文本菜单项对象。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_SetContent(ArkUI\_TextMenuItem\* item, const char\* content)](capi-native-type-h.md#oh_arkui_textmenuitem_setcontent) | - | 设置文本菜单项标题。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_GetContent(const ArkUI\_TextMenuItem\* item, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](capi-native-type-h.md#oh_arkui_textmenuitem_getcontent) | - | 获取文本菜单项标题。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_SetIcon(ArkUI\_TextMenuItem\* item, const char\* icon)](capi-native-type-h.md#oh_arkui_textmenuitem_seticon) | - | 设置文本菜单项图标路径。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_GetIcon(const ArkUI\_TextMenuItem\* item, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](capi-native-type-h.md#oh_arkui_textmenuitem_geticon) | - | 获取文本菜单项图标路径。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_SetLabelInfo(ArkUI\_TextMenuItem\* item, const char\* labelInfo)](capi-native-type-h.md#oh_arkui_textmenuitem_setlabelinfo) | - | 设置文本菜单项快捷键提示，例如“复制”菜单项的快捷键提示可以设置为“Ctrl+C”。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_GetLabelInfo(const ArkUI\_TextMenuItem\* item, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](capi-native-type-h.md#oh_arkui_textmenuitem_getlabelinfo) | - | 获取文本菜单项快捷键提示，例如“复制”菜单项的快捷键提示一般为“Ctrl+C”。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_SetId(ArkUI\_TextMenuItem\* item, int32\_t id)](capi-native-type-h.md#oh_arkui_textmenuitem_setid) | - | 设置文本菜单项id。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_GetId(const ArkUI\_TextMenuItem\* item, int32\_t\* id)](capi-native-type-h.md#oh_arkui_textmenuitem_getid) | - | 获取文本菜单项id。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItemArray\_GetSize(ArkUI\_TextMenuItemArray\* items, int32\_t\* size)](capi-native-type-h.md#oh_arkui_textmenuitemarray_getsize) | - | 获取文本菜单项数组大小。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItemArray\_GetItem(ArkUI\_TextMenuItemArray\* items, int32\_t index, ArkUI\_TextMenuItem\*\* item)](capi-native-type-h.md#oh_arkui_textmenuitemarray_getitem) | - | 获取文本菜单项数组中指定索引位置的文本菜单项。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItemArray\_Insert(ArkUI\_TextMenuItemArray\* items, ArkUI\_TextMenuItem\* item, int32\_t index)](capi-native-type-h.md#oh_arkui_textmenuitemarray_insert) | - | 在文本菜单项数组中指定索引位置插入一个文本菜单项。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItemArray\_Erase(ArkUI\_TextMenuItemArray\* items, int32\_t index)](capi-native-type-h.md#oh_arkui_textmenuitemarray_erase) | - | 删除文本菜单项数组中指定索引位置的文本菜单项。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItemArray\_Clear(ArkUI\_TextMenuItemArray\* items)](capi-native-type-h.md#oh_arkui_textmenuitemarray_clear) | - | 清除文本菜单项数组中所有的文本菜单项。 |
| [ArkUI\_TextEditMenuOptions\* OH\_ArkUI\_TextEditMenuOptions\_Create()](capi-native-type-h.md#oh_arkui_texteditmenuoptions_create) | - | 创建文本菜单扩展项对象。 |
| [void OH\_ArkUI\_TextEditMenuOptions\_Dispose(ArkUI\_TextEditMenuOptions\* editMenuOptions)](capi-native-type-h.md#oh_arkui_texteditmenuoptions_dispose) | - | 释放文本菜单扩展项对象。 |
| [typedef void (\*ArkUI\_TextCreateMenuCallback)(ArkUI\_TextMenuItemArray\* items, void\* userData)](capi-native-type-h.md#arkui_textcreatemenucallback) | ArkUI\_TextCreateMenuCallback | 文本菜单创建事件回调函数，在文本菜单创建时会触发此回调函数，开发者可在此函数中设置菜单数据。 |
| [typedef void (\*ArkUI\_TextPrepareMenuCallback)(ArkUI\_TextMenuItemArray\* items, void\* userData)](capi-native-type-h.md#arkui_textpreparemenucallback) | ArkUI\_TextPrepareMenuCallback | 文本菜单准备事件回调函数，当文本选择区域变化后显示菜单之前会触发此回调函数，开发者可在此函数中配置菜单数据。 |
| [typedef bool (\*ArkUI\_TextMenuItemClickCallback)(const ArkUI\_TextMenuItem\* item,int32\_t start, int32\_t end, void\* userData)](capi-native-type-h.md#arkui_textmenuitemclickcallback) | ArkUI\_TextMenuItemClickCallback | 文本菜单项点击事件回调函数，在菜单项被点击时触发此回调函数，开发者可在此函数中对系统默认处理行为进行拦截。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextEditMenuOptions\_RegisterOnCreateMenuCallback(ArkUI\_TextEditMenuOptions\* editMenuOptions, void\* userData, ArkUI\_TextCreateMenuCallback cb)](capi-native-type-h.md#oh_arkui_texteditmenuoptions_registeroncreatemenucallback) | - | 注册文本菜单创建事件回调函数。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextEditMenuOptions\_RegisterOnPrepareMenuCallback(ArkUI\_TextEditMenuOptions\* editMenuOptions, void\* userData, ArkUI\_TextPrepareMenuCallback cb)](capi-native-type-h.md#oh_arkui_texteditmenuoptions_registeronpreparemenucallback) | - | 注册文本菜单准备事件回调函数。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextEditMenuOptions\_RegisterOnMenuItemClickCallback(ArkUI\_TextEditMenuOptions\* editMenuOptions, void\* userData, ArkUI\_TextMenuItemClickCallback cb)](capi-native-type-h.md#oh_arkui_texteditmenuoptions_registeronmenuitemclickcallback) | - | 注册文本菜单项点击事件回调函数。 |
| [ArkUI\_TextSelectionMenuOptions\* OH\_ArkUI\_TextSelectionMenuOptions\_Create()](capi-native-type-h.md#oh_arkui_textselectionmenuoptions_create) | - | 创建自定义文本选择菜单对象。 |
| [void OH\_ArkUI\_TextSelectionMenuOptions\_Dispose(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions)](capi-native-type-h.md#oh_arkui_textselectionmenuoptions_dispose) | - | 释放自定义文本选择菜单对象。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_SetSpanType(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, ArkUI\_TextSpanType textSpanType)](capi-native-type-h.md#oh_arkui_textselectionmenuoptions_setspantype) | - | 设置自定义文本选择菜单的文本识别类型。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_GetSpanType(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, ArkUI\_TextSpanType\* spanType)](capi-native-type-h.md#oh_arkui_textselectionmenuoptions_getspantype) | - | 获取自定义文本选择菜单的文本识别类型。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_SetContentNode(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, ArkUI\_NodeHandle node)](capi-native-type-h.md#oh_arkui_textselectionmenuoptions_setcontentnode) | - | 设置自定义文本选择菜单的内容节点。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_GetContentNode(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, ArkUI\_NodeHandle\* node)](capi-native-type-h.md#oh_arkui_textselectionmenuoptions_getcontentnode) | - | 获取自定义文本选择菜单的内容节点。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_SetResponseType(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, ArkUI\_TextResponseType responseType)](capi-native-type-h.md#oh_arkui_textselectionmenuoptions_setresponsetype) | - | 设置自定义文本选择菜单的响应类型。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_GetResponseType(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, ArkUI\_TextResponseType\* responseType)](capi-native-type-h.md#oh_arkui_textselectionmenuoptions_getresponsetype) | - | 获取自定义文本选择菜单的响应类型。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_RegisterOnMenuShowCallback(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, void\* userData, void (\*callback)(int32\_t start, int32\_t end, void\* userData))](capi-native-type-h.md#oh_arkui_textselectionmenuoptions_registeronmenushowcallback) | - | 注册自定义文本选择菜单显示事件回调。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_RegisterOnMenuHideCallback(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, void\* userData, void (\*callback)(int32\_t start, int32\_t end, void\* userData))](capi-native-type-h.md#oh_arkui_textselectionmenuoptions_registeronmenuhidecallback) | - | 注册自定义文本选择菜单隐藏事件回调。 |
| [ArkUI\_TextMarqueeOptions\* OH\_ArkUI\_TextMarqueeOptions\_Create()](capi-native-type-h.md#oh_arkui_textmarqueeoptions_create) | - | 创建文本跑马灯模式配置项。 |
| [void OH\_ArkUI\_TextMarqueeOptions\_Dispose(ArkUI\_TextMarqueeOptions\* option)](capi-native-type-h.md#oh_arkui_textmarqueeoptions_dispose) | - | 销毁文本跑马灯模式配置项指针。 |
| [void OH\_ArkUI\_TextMarqueeOptions\_SetStart(ArkUI\_TextMarqueeOptions\* option, bool start)](capi-native-type-h.md#oh_arkui_textmarqueeoptions_setstart) | - | 设置文本跑马灯模式配置项是否播放。 |
| [bool OH\_ArkUI\_TextMarqueeOptions\_GetStart(ArkUI\_TextMarqueeOptions\* option)](capi-native-type-h.md#oh_arkui_textmarqueeoptions_getstart) | - | 获取文本跑马灯模式配置项是否播放。 |
| [void OH\_ArkUI\_TextMarqueeOptions\_SetStep(ArkUI\_TextMarqueeOptions\* option, float step)](capi-native-type-h.md#oh_arkui_textmarqueeoptions_setstep) | - | 设置文本跑马灯模式配置项的步长。 |
| [float OH\_ArkUI\_TextMarqueeOptions\_GetStep(ArkUI\_TextMarqueeOptions\* option)](capi-native-type-h.md#oh_arkui_textmarqueeoptions_getstep) | - | 获取文本跑马灯模式配置项的步长。 |
| [void OH\_ArkUI\_TextMarqueeOptions\_SetSpacing(ArkUI\_TextMarqueeOptions\* option, float spacing)](capi-native-type-h.md#oh_arkui_textmarqueeoptions_setspacing) | - | 设置文本跑马灯模式配置项的首尾间距。 |
| [float OH\_ArkUI\_TextMarqueeOptions\_GetSpacing(ArkUI\_TextMarqueeOptions\* option)](capi-native-type-h.md#oh_arkui_textmarqueeoptions_getspacing) | - | 获取文本跑马灯模式配置项的首尾间距。 |
| [void OH\_ArkUI\_TextMarqueeOptions\_SetLoop(ArkUI\_TextMarqueeOptions\* option, int32\_t loop)](capi-native-type-h.md#oh_arkui_textmarqueeoptions_setloop) | - | 设置文本跑马灯模式配置项的重复滚动的次数，小于等于零时无限循环。 |
| [int32\_t OH\_ArkUI\_TextMarqueeOptions\_GetLoop(ArkUI\_TextMarqueeOptions\* option)](capi-native-type-h.md#oh_arkui_textmarqueeoptions_getloop) | - | 获取文本跑马灯模式配置项的重复滚动的次数。 |
| [void OH\_ArkUI\_TextMarqueeOptions\_SetFromStart(ArkUI\_TextMarqueeOptions\* option, bool fromStart)](capi-native-type-h.md#oh_arkui_textmarqueeoptions_setfromstart) | - | 设置文本跑马灯模式配置项的运行方向。 |
| [bool OH\_ArkUI\_TextMarqueeOptions\_GetFromStart(ArkUI\_TextMarqueeOptions\* option)](capi-native-type-h.md#oh_arkui_textmarqueeoptions_getfromstart) | - | 获取文本跑马灯模式配置项的运行方向。 |
| [void OH\_ArkUI\_TextMarqueeOptions\_SetDelay(ArkUI\_TextMarqueeOptions\* option, int32\_t delay)](capi-native-type-h.md#oh_arkui_textmarqueeoptions_setdelay) | - | 设置文本跑马灯模式配置项的每轮滚动延迟时间。 |
| [int32\_t OH\_ArkUI\_TextMarqueeOptions\_GetDelay(ArkUI\_TextMarqueeOptions\* option)](capi-native-type-h.md#oh_arkui_textmarqueeoptions_getdelay) | - | 获取文本跑马灯模式配置项的每轮滚动延迟时间。 |
| [void OH\_ArkUI\_TextMarqueeOptions\_SetFadeout(ArkUI\_TextMarqueeOptions\* option, bool fadeout)](capi-native-type-h.md#oh_arkui_textmarqueeoptions_setfadeout) | - | 设置文本跑马灯模式配置项是否支持文字超长时的渐隐效果。当Text内容超出显示范围时，未完全展现的文字边缘将应用渐隐效果。若两端均有文字未完全显示，则两端同时应用渐隐效果。在渐隐效果开启状态下，[NODE\_CLIP](capi-native-node-h.md#arkui_nodeattributetype)属性将自动锁定为true，不允许设置为false。 |
| [bool OH\_ArkUI\_TextMarqueeOptions\_GetFadeout(ArkUI\_TextMarqueeOptions\* option)](capi-native-type-h.md#oh_arkui_textmarqueeoptions_getfadeout) | - | 获取文本跑马灯模式配置项是否支持文字超长时的渐隐效果。 |
| [void OH\_ArkUI\_TextMarqueeOptions\_SetStartPolicy(ArkUI\_TextMarqueeOptions\* option, ArkUI\_MarqueeStartPolicy startPolicy)](capi-native-type-h.md#oh_arkui_textmarqueeoptions_setstartpolicy) | - | 设置文本跑马灯模式配置项的启动策略。 |
| [ArkUI\_MarqueeStartPolicy OH\_ArkUI\_TextMarqueeOptions\_GetStartPolicy(ArkUI\_TextMarqueeOptions\* option)](capi-native-type-h.md#oh_arkui_textmarqueeoptions_getstartpolicy) | - | 获取文本跑马灯模式配置项的启动策略。 |
| [void OH\_ArkUI\_TextMarqueeOptions\_SetUpdatePolicy(ArkUI\_TextMarqueeOptions\* option, ArkUI\_MarqueeUpdatePolicy updatePolicy)](capi-native-type-h.md#oh_arkui_textmarqueeoptions_setupdatepolicy) | - | 设置文本跑马灯模式配置项的更新策略。 |
| [ArkUI\_MarqueeUpdatePolicy OH\_ArkUI\_TextMarqueeOptions\_GetUpdatePolicy(ArkUI\_TextMarqueeOptions\* option)](capi-native-type-h.md#oh_arkui_textmarqueeoptions_getupdatepolicy) | - | 获取文本跑马灯模式配置项的更新策略。 |
| [ArkUI\_PickerIndicatorStyle OH\_ArkUI\_PickerIndicatorStyle\_Create(ArkUI\_PickerIndicatorType type)](capi-native-type-h.md#oh_arkui_pickerindicatorstyle_create) | ArkUI\_PickerIndicatorStyle | 创建选中项指示器的样式实例。 |
| [void OH\_ArkUI\_PickerIndicatorStyle\_Dispose(ArkUI\_PickerIndicatorStyle\* style)](capi-native-type-h.md#oh_arkui_pickerindicatorstyle_dispose) | - | 销毁选中项指示器的样式实例。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_PickerIndicatorStyle\_ConfigureBackground(ArkUI\_PickerIndicatorStyle\* style, ArkUI\_PickerIndicatorBackground\* background)](capi-native-type-h.md#oh_arkui_pickerindicatorstyle_configurebackground) | - | 设置背景样式参数，此接口仅当选择器选中项样式枚举类型为[ARKUI\_PICKER\_INDICATOR\_BACKGROUND](capi-native-type-h.md#arkui_pickerindicatortype)时生效。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_PickerIndicatorStyle\_ConfigureDivider(ArkUI\_PickerIndicatorStyle\* style, ArkUI\_PickerIndicatorDivider\* divider)](capi-native-type-h.md#oh_arkui_pickerindicatorstyle_configuredivider) | - | 设置分割线样式参数，此接口仅当选择器选中项样式枚举类型为[ARKUI\_PICKER\_INDICATOR\_DIVIDER](capi-native-type-h.md#arkui_pickerindicatortype)时生效。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### ArkUI\_Alignment

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_Alignment
```

**描述：**

定义布局对齐枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ALIGNMENT\_TOP\_START = 0 | 顶部起始，该值为默认值。 |
| ARKUI\_ALIGNMENT\_TOP = 1 | 顶部居中。 |
| ARKUI\_ALIGNMENT\_TOP\_END = 2 | 顶部尾端。 |
| ARKUI\_ALIGNMENT\_START = 3 | 起始端纵向居中。 |
| ARKUI\_ALIGNMENT\_CENTER = 4 | 横向和纵向居中。 |
| ARKUI\_ALIGNMENT\_END = 5 | 尾端纵向居中。 |
| ARKUI\_ALIGNMENT\_BOTTOM\_START = 6 | 底部起始端。 |
| ARKUI\_ALIGNMENT\_BOTTOM = 7 | 底部横向居中。 |
| ARKUI\_ALIGNMENT\_BOTTOM\_END = 8 | 底部尾端。 |

### ArkUI\_ImageRepeat

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ImageRepeat
```

**描述：**

定义图片重复铺设枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_IMAGE\_REPEAT\_NONE = 0 | 不重复。 |
| ARKUI\_IMAGE\_REPEAT\_X = 1 | 在X轴方向重复。 |
| ARKUI\_IMAGE\_REPEAT\_Y = 2 | 在Y轴方向重复。 |
| ARKUI\_IMAGE\_REPEAT\_XY = 3 | 在X轴和Y轴方向重复。 |

### ArkUI\_FontStyle

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_FontStyle
```

**描述：**

定义字体样式枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_FONT\_STYLE\_NORMAL = 0 | 标准字体样式。 |
| ARKUI\_FONT\_STYLE\_ITALIC = 1 | 斜体字体样式。 |

### ArkUI\_FontWeight

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_FontWeight
```

**描述：**

定义字体粗细/字重枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_FONT\_WEIGHT\_W100 = 0 | 100 |
| ARKUI\_FONT\_WEIGHT\_W200 = 1 | 200 |
| ARKUI\_FONT\_WEIGHT\_W300 = 2 | 300 |
| ARKUI\_FONT\_WEIGHT\_W400 = 3 | 400 |
| ARKUI\_FONT\_WEIGHT\_W500 = 4 | 500 |
| ARKUI\_FONT\_WEIGHT\_W600 = 5 | 600 |
| ARKUI\_FONT\_WEIGHT\_W700 = 6 | 700 |
| ARKUI\_FONT\_WEIGHT\_W800 = 7 | 800 |
| ARKUI\_FONT\_WEIGHT\_W900 = 8 | 900 |
| ARKUI\_FONT\_WEIGHT\_BOLD = 9 | 字体较粗。 |
| ARKUI\_FONT\_WEIGHT\_NORMAL = 10 | 字体粗细正常。 |
| ARKUI\_FONT\_WEIGHT\_BOLDER = 11 | 字体非常粗。 |
| ARKUI\_FONT\_WEIGHT\_LIGHTER = 12 | 字体较细。 |
| ARKUI\_FONT\_WEIGHT\_MEDIUM = 13 | 字体粗细适中。 |
| ARKUI\_FONT\_WEIGHT\_REGULAR = 14 | 字体粗细正常。 |

### ArkUI\_TextAlignment

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_TextAlignment
```

**描述：**

定义字体水平对齐样式枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXT\_ALIGNMENT\_START = 0 | 水平对齐首部。 |
| ARKUI\_TEXT\_ALIGNMENT\_CENTER = 1 | 水平居中对齐。 |
| ARKUI\_TEXT\_ALIGNMENT\_END = 2 | 水平对齐尾部。 |
| ARKUI\_TEXT\_ALIGNMENT\_JUSTIFY = 3 | 双端对齐。 |
| ARKUI\_TEXT\_ALIGNMENT\_LEFT\_TO\_RIGHT = 4 | 从左到右对齐。  **起始版本：** 23 |
| ARKUI\_TEXT\_ALIGNMENT\_RIGHT\_TO\_LEFT = 5 | 从右到左对齐。  **起始版本：** 23 |

### ArkUI\_TextVerticalAlignment

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_TextVerticalAlignment
```

**描述：**

定义文本垂直对齐样式枚举值。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXT\_VERTICAL\_ALIGNMENT\_BASELINE = 0 | 基线对齐。 |
| ARKUI\_TEXT\_VERTICAL\_ALIGNMENT\_BOTTOM = 1 | 底部对齐。 |
| ARKUI\_TEXT\_VERTICAL\_ALIGNMENT\_CENTER = 2 | 居中对齐。 |
| ARKUI\_TEXT\_VERTICAL\_ALIGNMENT\_TOP = 3 | 顶部对齐。 |

### ArkUI\_TextContentAlign

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_TextContentAlign
```

**描述：**

定义文本内容区垂直对齐样式枚举值。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXT\_CONTENT\_ALIGN\_TOP = 0 | 顶部对齐。 |
| ARKUI\_TEXT\_CONTENT\_ALIGN\_CENTER = 1 | 居中对齐。 |
| ARKUI\_TEXT\_CONTENT\_ALIGN\_BOTTOM = 2 | 底部对齐。 |

### ArkUI\_TextDirection

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_TextDirection
```

**描述：**

定义文本排版方向枚举值。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXT\_DIRECTION\_LTR = 0 | 文本排版方向从左到右。 |
| ARKUI\_TEXT\_DIRECTION\_RTL = 1 | 文本排版方向从右到左。 |
| ARKUI\_TEXT\_DIRECTION\_DEFAULT = 2 | 文本排版方向遵循组件布局。 |
| ARKUI\_TEXT\_DIRECTION\_AUTO = 3 | 遵循自身实际文本内容的排版方向，如果文本为 RTL（Right-to-Left）类语言（如藏文、维吾尔文），文本排版方向为从右到左。如果为 LTR（Left-to-Right）类语言（如中文、英文），文本排版方向为从左到右。 |

### ArkUI\_EnterKeyType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_EnterKeyType
```

**描述：**

定义单行文本输入法回车键类型枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ENTER\_KEY\_TYPE\_GO = 2 | 显示为开始样式。 |
| ARKUI\_ENTER\_KEY\_TYPE\_SEARCH = 3 | 显示为搜索样式。 |
| ARKUI\_ENTER\_KEY\_TYPE\_SEND = 4 | 显示为发送样式。 |
| ARKUI\_ENTER\_KEY\_TYPE\_NEXT = 5 | 显示为下一个样式。 |
| ARKUI\_ENTER\_KEY\_TYPE\_DONE = 6 | 显示为完成样式。 |
| ARKUI\_ENTER\_KEY\_TYPE\_PREVIOUS = 7 | 显示为上一个样式。 |
| ARKUI\_ENTER\_KEY\_TYPE\_NEW\_LINE = 8 | 显示为换行样式。 |

### ArkUI\_TextInputType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_TextInputType
```

**描述：**

定义单行文本输入法类型枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXTINPUT\_TYPE\_NORMAL = 0 | 基本输入模式。 |
| ARKUI\_TEXTINPUT\_TYPE\_NUMBER = 2 | 纯数字模式。 |
| ARKUI\_TEXTINPUT\_TYPE\_PHONE\_NUMBER = 3 | 电话号码输入模式。 |
| ARKUI\_TEXTINPUT\_TYPE\_EMAIL = 5 | 邮箱地址输入模式。 |
| ARKUI\_TEXTINPUT\_TYPE\_PASSWORD = 7 | 密码输入模式。 |
| ARKUI\_TEXTINPUT\_TYPE\_NUMBER\_PASSWORD = 8 | 纯数字密码输入模式。 |
| ARKUI\_TEXTINPUT\_TYPE\_SCREEN\_LOCK\_PASSWORD = 9 | 锁屏应用密码输入模式。 |
| ARKUI\_TEXTINPUT\_TYPE\_USER\_NAME = 10 | 用户名输入模式。 |
| ARKUI\_TEXTINPUT\_TYPE\_NEW\_PASSWORD = 11 | 新密码输入模式。 |
| ARKUI\_TEXTINPUT\_TYPE\_NUMBER\_DECIMAL = 12 | 带小数点的数字输入模式。 |
| ARKUI\_TEXTINPUT\_TYPE\_ONE\_TIME\_CODE = 14 | 验证码输入模式。  **起始版本：** 20 |

### ArkUI\_TextAreaType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_TextAreaType
```

**描述：**

定义多行文本输入法类型枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXTAREA\_TYPE\_NORMAL = 0 | 基本输入模式。 |
| ARKUI\_TEXTAREA\_TYPE\_NUMBER = 2 | 纯数字模式。 |
| ARKUI\_TEXTAREA\_TYPE\_PHONE\_NUMBER = 3 | 电话号码输入模式。 |
| ARKUI\_TEXTAREA\_TYPE\_EMAIL = 5 | 邮箱地址输入模式。 |
| ARKUI\_TEXTAREA\_TYPE\_ONE\_TIME\_CODE = 14 | 验证码输入模式。  **起始版本：** 20 |

### ArkUI\_CancelButtonStyle

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_CancelButtonStyle
```

**描述：**

定义清除按钮样式枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_CANCELBUTTON\_STYLE\_CONSTANT = 0 | 清除按钮常显样式。 |
| ARKUI\_CANCELBUTTON\_STYLE\_INVISIBLE = 1 | 清除按钮常隐样式。 |
| ARKUI\_CANCELBUTTON\_STYLE\_INPUT = 2 | 清除按钮输入样式。 |

### ArkUI\_XComponentType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_XComponentType
```

**描述：**

定义XComponent类型枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_XCOMPONENT\_TYPE\_SURFACE = 0 | 用于EGL/OpenGLES和媒体数据写入，开发者定制绘制内容单独显示在屏幕上。 |
| ARKUI\_XCOMPONENT\_TYPE\_TEXTURE = 2 | 用于EGL/OpenGLES和媒体数据写入，开发者定制绘制内容和XComponent组件内容合成后展示在屏幕上。 |

### ArkUI\_ProgressType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ProgressType
```

**描述：**

定义进度条类型枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_PROGRESS\_TYPE\_LINEAR = 0 | 线性样式。 |
| ARKUI\_PROGRESS\_TYPE\_RING = 1 | 环形无刻度样式。 |
| ARKUI\_PROGRESS\_TYPE\_ECLIPSE = 2 | 圆形样式。 |
| ARKUI\_PROGRESS\_TYPE\_SCALE\_RING = 3 | 环形有刻度样式。 |
| ARKUI\_PROGRESS\_TYPE\_CAPSULE = 4 | 胶囊样式。 |

### ArkUI\_TextDecorationType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_TextDecorationType
```

**描述：**

定义装饰线类型枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXT\_DECORATION\_TYPE\_NONE = 0 | 不使用装饰线。 |
| ARKUI\_TEXT\_DECORATION\_TYPE\_UNDERLINE = 1 | 文字下划线修饰。 |
| ARKUI\_TEXT\_DECORATION\_TYPE\_OVERLINE = 2 | 文字上划线修饰。 |
| ARKUI\_TEXT\_DECORATION\_TYPE\_LINE\_THROUGH = 3 | 穿过文本的修饰线。 |

### ArkUI\_TextDecorationStyle

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_TextDecorationStyle
```

**描述：**

定义装饰线样式枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXT\_DECORATION\_STYLE\_SOLID = 0 | 单实线。 |
| ARKUI\_TEXT\_DECORATION\_STYLE\_DOUBLE = 1 | 双实线。 |
| ARKUI\_TEXT\_DECORATION\_STYLE\_DOTTED = 2 | 点线。 |
| ARKUI\_TEXT\_DECORATION\_STYLE\_DASHED = 3 | 虚线。 |
| ARKUI\_TEXT\_DECORATION\_STYLE\_WAVY = 4 | 波浪线。 |

### ArkUI\_TextCase

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_TextCase
```

**描述：**

定义文本大小写枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXT\_CASE\_NORMAL = 0 | 保持原有大小写。 |
| ARKUI\_TEXT\_CASE\_LOWER = 1 | 文本全小写。 |
| ARKUI\_TEXT\_CASE\_UPPER = 2 | 文本全大写。 |

### ArkUI\_CopyOptions

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_CopyOptions
```

**描述：**

定义文本复制粘贴模式枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_COPY\_OPTIONS\_NONE = 0 | 不支持复制。 |
| ARKUI\_COPY\_OPTIONS\_IN\_APP = 1 | 支持应用内复制。 |
| ARKUI\_COPY\_OPTIONS\_LOCAL\_DEVICE = 2 | 支持设备内复制。 |
| ARKUI\_COPY\_OPTIONS\_CROSS\_DEVICE = 3 | 支持跨设备复制。 |

### ArkUI\_ShadowType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ShadowType
```

**描述：**

定义阴影类型枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SHADOW\_TYPE\_COLOR = 0 | 彩色阴影。 |
| ARKUI\_SHADOW\_TYPE\_BLUR = 1 | 模糊阴影。 |

### ArkUI\_DatePickerMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_DatePickerMode
```

**描述：**

定义日期选择器列显示模式的枚举值。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_DATEPICKER\_MODE\_DATE = 0 | 默认值。日期列显示年、月、日三列。 |
| ARKUI\_DATEPICKER\_YEAR\_AND\_MONTH = 1 | 日期列显示年、月二列。 |
| ARKUI\_DATEPICKER\_MONTH\_AND\_DAY = 2 | 日期列显示月、日二列。 |

### ArkUI\_TextPickerRangeType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_TextPickerRangeType
```

**描述：**

定义滑动选择文本选择器输入类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXTPICKER\_RANGETYPE\_SINGLE = 0 | 单列数据选择器。 |
| ARKUI\_TEXTPICKER\_RANGETYPE\_MULTI = 1 | 多列数据选择器。 |
| ARKUI\_TEXTPICKER\_RANGETYPE\_RANGE\_CONTENT = 2 | 支持图片资源的单列数据选择器。 |
| ARKUI\_TEXTPICKER\_RANGETYPE\_CASCADE\_RANGE\_CONTENT = 3 | 支持联动的多列数据选择器。 |

### ArkUI\_AccessibilityCheckedState

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_AccessibilityCheckedState
```

**描述：**

定义无障碍复选框状态类型枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ACCESSIBILITY\_UNCHECKED = 0 | 复选框未被选中。 |
| ARKUI\_ACCESSIBILITY\_CHECKED = 1 | 复选框被选中。 |

### ArkUI\_AccessibilityActionType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_AccessibilityActionType
```

**描述：**

定义无障碍操作类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ACCESSIBILITY\_ACTION\_CLICK = 1 << 0 | 点击操作。 |
| ARKUI\_ACCESSIBILITY\_ACTION\_LONG\_CLICK = 1 << 1 | 长按操作。 |
| ARKUI\_ACCESSIBILITY\_ACTION\_CUT = 1 << 2 | 剪切操作。 |
| ARKUI\_ACCESSIBILITY\_ACTION\_COPY = 1 << 3 | 复制操作。 |
| ARKUI\_ACCESSIBILITY\_ACTION\_PASTE = 1 << 4 | 粘贴操作。 |

### ArkUI\_EdgeEffect

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_EdgeEffect
```

**描述：**

定义边缘滑动效果枚举值。Grid、Scroll、WaterFlow组件默认值为ARKUI\_EDGE\_EFFECT\_NONE，List组件默认值为ARKUI\_EDGE\_EFFECT\_SPRING。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_EDGE\_EFFECT\_SPRING = 0 | 弹性物理动效，滑动到边缘后可以根据初始速度或通过触摸事件继续滑动一段距离，松手后回弹。 |
| ARKUI\_EDGE\_EFFECT\_FADE = 1 | 阴影效果，滑动到边缘后会有圆弧状的阴影。 |
| ARKUI\_EDGE\_EFFECT\_NONE = 2 | 滑动到边缘后无效果。 |

### ArkUI\_BarState

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_BarState
```

**描述：**

定义文本控制滚动条状态枚举值。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_BAR\_STATE\_OFF = 0 | 不显示。 |
| ARKUI\_BAR\_STATE\_AUTO = 1 | 按需显示（在触摸时显示滚动条，2秒后自动消失）。 |
| ARKUI\_BAR\_STATE\_ON = 2 | 常驻显示。 |

### ArkUI\_EffectEdge

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_EffectEdge
```

**描述：**

定义边缘效果生效边缘的方向枚举值。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_EFFECT\_EDGE\_START = 1 | 起始边生效。 |
| ARKUI\_EFFECT\_EDGE\_END = 2 | 末尾边生效。 |

### ArkUI\_ScrollDirection

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ScrollDirection
```

**描述：**

定义[Scroll](ts-container-scroll.md)组件排列方向枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SCROLL\_DIRECTION\_VERTICAL = 0 | 仅支持竖直方向滚动。 |
| ARKUI\_SCROLL\_DIRECTION\_HORIZONTAL = 1 | 仅支持水平方向滚动。 |
| ARKUI\_SCROLL\_DIRECTION\_NONE = 3 | 禁止滚动。 |
| ARKUI\_SCROLL\_DIRECTION\_FREE = 4 | 自由滚动。  **起始版本：** 20 |

### ArkUI\_ScrollSnapAlign

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ScrollSnapAlign
```

**描述：**

定义列表项滚动结束对齐效果枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SCROLL\_SNAP\_ALIGN\_NONE = 0 | 默认无列表滚动对齐效果。 |
| ARKUI\_SCROLL\_SNAP\_ALIGN\_START = 1 | 视图中的第一项将在列表的开头对齐。 |
| ARKUI\_SCROLL\_SNAP\_ALIGN\_CENTER = 2 | 视图中的中间项将在列表中心对齐。 |
| ARKUI\_SCROLL\_SNAP\_ALIGN\_END = 3 | 视图中的最后一项将在列表末尾对齐。 |

### ArkUI\_ScrollBarDisplayMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ScrollBarDisplayMode
```

**描述：**

定义滚动条状态枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_OFF = 0 | 不显示。 |
| ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_AUTO = 1 | 按需显示(触摸时显示，2s后消失)。 |
| ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_ON = 2 | 常驻显示。 |

### ArkUI\_Axis

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_Axis
```

**描述：**

定义滚动方向和[List](ts-container-list.md)组件排列方向枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_AXIS\_VERTICAL = 0 | 仅支持竖直方向滚动，该值为默认值。 |
| ARKUI\_AXIS\_HORIZONTAL = 1 | 仅支持水平方向滚动。 |

### ArkUI\_StickyStyle

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_StickyStyle
```

**描述：**

定义列表是否吸顶和吸底枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_STICKY\_STYLE\_NONE = 0 | [ListItemGroup](ts-container-listitemgroup.md)的[header](ts-container-listitemgroup.md#listitemgroupoptions对象说明)不吸顶，[footer](ts-container-listitemgroup.md#listitemgroupoptions对象说明)不吸底。 |
| ARKUI\_STICKY\_STYLE\_HEADER = 1 | [ListItemGroup](ts-container-listitemgroup.md)的[header](ts-container-listitemgroup.md#listitemgroupoptions对象说明)吸顶，[footer](ts-container-listitemgroup.md#listitemgroupoptions对象说明)不吸底。 |
| ARKUI\_STICKY\_STYLE\_FOOTER = 2 | [ListItemGroup](ts-container-listitemgroup.md)的[header](ts-container-listitemgroup.md#listitemgroupoptions对象说明)不吸顶，[footer](ts-container-listitemgroup.md#listitemgroupoptions对象说明)吸底。 |
| ARKUI\_STICKY\_STYLE\_BOTH = 3 | [ListItemGroup](ts-container-listitemgroup.md)的[header](ts-container-listitemgroup.md#listitemgroupoptions对象说明)吸顶，[footer](ts-container-listitemgroup.md#listitemgroupoptions对象说明)吸底。 |

### ArkUI\_ContentClipMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ContentClipMode
```

**描述：**

定义滚动容器的内容层裁剪区域枚举值。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_CONTENT\_CLIP\_MODE\_CONTENT\_ONLY = 0 | 按内容区裁剪。 |
| ARKUI\_CONTENT\_CLIP\_MODE\_BOUNDARY = 1 | 按组件区域裁剪。 |
| ARKUI\_CONTENT\_CLIP\_MODE\_SAFE\_AREA = 2 | 按组件配置的[SafeArea](ts-universal-attributes-expand-safe-area.md)区域裁剪。 |

### ArkUI\_WaterFlowLayoutMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_WaterFlowLayoutMode
```

**描述：**

定义[WaterFlow](ts-container-waterflow.md)组件布局模式枚举值。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_WATER\_FLOW\_LAYOUT\_MODE\_ALWAYS\_TOP\_DOWN = 0 | 从上到下布局。列数切换场景需要从第一个[FlowItem](ts-container-flowitem.md)开始布局到当前显示的[FlowItem](ts-container-flowitem.md)。 |
| ARKUI\_WATER\_FLOW\_LAYOUT\_MODE\_SLIDING\_WINDOW = 1 | 移动窗口布局。列数切换场景只重新布局当前显示范围到[FlowItem](ts-container-flowitem.md)，手指向下滑动再布局从上方进入显示范围的[FlowItem](ts-container-flowitem.md)。 |

### ArkUI\_BorderStyle

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_BorderStyle
```

**描述：**

边框线条样式枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_BORDER\_STYLE\_SOLID = 0 | 显示为一条实线，该值为默认值。 |
| ARKUI\_BORDER\_STYLE\_DASHED = 1 | 显示为一系列短的方形虚线。 |
| ARKUI\_BORDER\_STYLE\_DOTTED = 2 | 显示为一系列圆点。 |

### ArkUI\_HitTestMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_HitTestMode
```

**描述：**

触摸测试控制枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_HIT\_TEST\_MODE\_DEFAULT = 0 | 默认触摸测试效果。自身及子节点响应触摸测试，但阻塞兄弟节点的触摸测试，不影响祖先节点的触摸测试。 |
| ARKUI\_HIT\_TEST\_MODE\_BLOCK = 1 | 自身响应触摸测试，阻塞子节点、兄弟节点和祖先节点的触摸测试。 |
| ARKUI\_HIT\_TEST\_MODE\_TRANSPARENT = 2 | 自身和子节点都响应触摸测试，不会阻塞兄弟节点和祖先节点的触摸测试。 |
| ARKUI\_HIT\_TEST\_MODE\_NONE = 3 | 自身不响应触摸测试，不会阻塞子节点、兄弟节点和祖先节点的触摸测试。 |
| ARKUI\_HIT\_TEST\_MODE\_BLOCK\_HIERARCHY = 4 | 自身和子节点响应触摸测试，阻止所有优先级较低的兄弟节点和父节点参与触摸测试。  **起始版本：** 20 |
| ARKUI\_HIT\_TEST\_MODE\_BLOCK\_DESCENDANTS = 5 | 自身不响应触摸测试，并且所有的后代（孩子，孙子等）也不响应触摸测试，不会影响祖先节点的触摸测试。  **起始版本：** 20 |

### ArkUI\_ShadowStyle

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ShadowStyle
```

**描述：**

阴影效果枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SHADOW\_STYLE\_OUTER\_DEFAULT\_XS = 0 | 超小阴影。 |
| ARKUI\_SHADOW\_STYLE\_OUTER\_DEFAULT\_SM = 1 | 小阴影。 |
| ARKUI\_SHADOW\_STYLE\_OUTER\_DEFAULT\_MD = 2 | 中阴影。 |
| ARKUI\_SHADOW\_STYLE\_OUTER\_DEFAULT\_LG = 3 | 大阴影。 |
| ARKUI\_SHADOW\_STYLE\_OUTER\_FLOATING\_SM = 4 | 浮动小阴影。 |
| ARKUI\_SHADOW\_STYLE\_OUTER\_FLOATING\_MD = 5 | 浮动中阴影。 |

### ArkUI\_AnimationCurve

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_AnimationCurve
```

**描述：**

动画曲线枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_CURVE\_LINEAR = 0 | 动画从头到尾的速度都是相同。 |
| ARKUI\_CURVE\_EASE = 1 | 动画以低速开始，然后加快，在结束前变慢。 |
| ARKUI\_CURVE\_EASE\_IN = 2 | 动画以低速开始。 |
| ARKUI\_CURVE\_EASE\_OUT = 3 | 动画以低速结束。 |
| ARKUI\_CURVE\_EASE\_IN\_OUT = 4 | 动画以低速开始和结束，提供平滑自然的动画过渡效果。 |
| ARKUI\_CURVE\_FAST\_OUT\_SLOW\_IN = 5 | 动画标准曲线。 |
| ARKUI\_CURVE\_LINEAR\_OUT\_SLOW\_IN = 6 | 动画减速曲线。 |
| ARKUI\_CURVE\_FAST\_OUT\_LINEAR\_IN = 7 | 动画加速曲线。 |
| ARKUI\_CURVE\_EXTREME\_DECELERATION = 8 | 动画急缓曲线。 |
| ARKUI\_CURVE\_SHARP = 9 | 动画锐利曲线。 |
| ARKUI\_CURVE\_RHYTHM = 10 | 动画节奏曲线。 |
| ARKUI\_CURVE\_SMOOTH = 11 | 动画平滑曲线。 |
| ARKUI\_CURVE\_FRICTION = 12 | 动画阻尼曲线。 |

### ArkUI\_SwiperArrow

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_SwiperArrow
```

**描述：**

Swiper导航点箭头枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SWIPER\_ARROW\_HIDE = 0 | 不显示swiper中导航点箭头。 |
| ARKUI\_SWIPER\_ARROW\_SHOW = 1 | 显示swiper中导航点箭头。 |
| ARKUI\_SWIPER\_ARROW\_SHOW\_ON\_HOVER = 2 | 在鼠标悬浮状态下显示swiper的导航点箭头。 |

### ArkUI\_SwiperNestedScrollMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_SwiperNestedScrollMode
```

**描述：**

Swiper组件和父组件的嵌套滚动模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SWIPER\_NESTED\_SRCOLL\_SELF\_ONLY = 0 | Swiper只自身滚动，不与父组件联动。 |
| ARKUI\_SWIPER\_NESTED\_SRCOLL\_SELF\_FIRST = 1 | Swiper自身先滚动，自身滚动到边缘以后父组件滚动。父组件滚动到边缘以后，如果父组件有边缘效果，则父组件触发边缘效果，否则Swiper触发边缘效果。 |

### ArkUI\_PageFlipMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_PageFlipMode
```

**描述：**

[Swiper](ts-container-swiper.md)组件鼠标滚轮翻页模式。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_PAGE\_FLIP\_MODE\_CONTINUOUS = 0 | 连续翻页模式，鼠标滚轮连续滚动时翻多页。 |
| ARKUI\_PAGE\_FLIP\_MODE\_SINGLE = 1 | 一次翻页动画结束前不响应其他鼠标滚轮事件。 |

### ArkUI\_SwiperAnimationMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_SwiperAnimationMode
```

**描述：**

Swiper组件跳转到目标页面的动画模式。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SWIPER\_NO\_ANIMATION = 0 | 无动画跳转到目标页面。 |
| ARKUI\_SWIPER\_DEFAULT\_ANIMATION = 1 | 做动画跳转到目标页面。 |
| ARKUI\_SWIPER\_FAST\_ANIMATION = 2 | 先无动画跳转到目标附近再做动画跳转到目标页面。 |

### ArkUI\_AccessibilityMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_AccessibilityMode
```

**描述：**

定义无障碍辅助服务模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ACCESSIBILITY\_MODE\_AUTO = 0 | 根据组件不同会转换为“enabled”或者“disabled”。 |
| ARKUI\_ACCESSIBILITY\_MODE\_ENABLED = 1 | 当前组件可被无障碍辅助服务所识别。 |
| ARKUI\_ACCESSIBILITY\_MODE\_DISABLED = 2 | 当前组件不可被无障碍辅助服务所识别。 |
| ARKUI\_ACCESSIBILITY\_MODE\_DISABLED\_FOR\_DESCENDANTS = 3 | 当前组件及其所有子组件不可被无障碍辅助服务所识别。 |

### ArkUI\_TextCopyOptions

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_TextCopyOptions
```

**描述：**

定义组件支持设置文本是否可复制粘贴。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXT\_COPY\_OPTIONS\_NONE = 0 | 不支持复制。 |
| ARKUI\_TEXT\_COPY\_OPTIONS\_IN\_APP = 1 | 支持应用内复制。 |
| ARKUI\_TEXT\_COPY\_OPTIONS\_LOCAL\_DEVICE = 2 | 支持设备内复制。 |
| ARKUI\_TEXT\_COPY\_OPTIONS\_CROSS\_DEVICE = 3 | 支持跨设备复制。 |

### ArkUI\_TextHeightAdaptivePolicy

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_TextHeightAdaptivePolicy
```

**描述：**

定义文本自适应高度的方式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXT\_HEIGHT\_ADAPTIVE\_POLICY\_MAX\_LINES\_FIRST = 0 | 设置文本高度自适应方式为以MaxLines优先。 |
| ARKUI\_TEXT\_HEIGHT\_ADAPTIVE\_POLICY\_MIN\_FONT\_SIZE\_FIRST = 1 | 设置文本高度自适应方式为以缩小字体优先。 |
| ARKUI\_TEXT\_HEIGHT\_ADAPTIVE\_POLICY\_LAYOUT\_CONSTRAINT\_FIRST = 2 | 设置文本高度自适应方式为以布局约束（高度）优先。 |

### ArkUI\_ScrollNestedMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ScrollNestedMode
```

**描述：**

定义嵌套滚动选项。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SCROLL\_NESTED\_MODE\_SELF\_ONLY = 0 | 只自身滚动，不与父组件联动。 |
| ARKUI\_SCROLL\_NESTED\_MODE\_SELF\_FIRST = 1 | 自身先滚动，自身滚动到边缘以后父组件滚动。父组件滚动到边缘以后，如果父组件有边缘效果，则父组件触发边缘效果，否则子组件触发边缘效果。 |
| ARKUI\_SCROLL\_NESTED\_MODE\_PARENT\_FIRST = 2 | 父组件先滚动，父组件滚动到边缘以后自身滚动。自身滚动到边缘后，如果有边缘效果，会触发自身的边缘效果，否则触发父组件的边缘效果。 |
| ARKUI\_SCROLL\_NESTED\_MODE\_PARALLEL = 3 | 自身和父组件同时滚动，自身和父组件都到达边缘以后，如果自身有边缘效果，则自身触发边缘效果，否则父组件触发边缘效果。 |

### ArkUI\_ScrollEdge

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ScrollEdge
```

**描述：**

定义滚动到的边缘位置。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SCROLL\_EDGE\_TOP = 0 | 竖直方向上边缘。 |
| ARKUI\_SCROLL\_EDGE\_BOTTOM = 1 | 竖直方向下边缘。 |
| ARKUI\_SCROLL\_EDGE\_START = 2 | 水平方向起始位置。 |
| ARKUI\_SCROLL\_EDGE\_END = 3 | 水平方向末尾位置。 |

### ArkUI\_ScrollAlignment

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ScrollAlignment
```

**描述：**

滚动到具体item时的对齐方式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SCROLL\_ALIGNMENT\_START = 0 | 首部对齐。指定item首部与容器首部对齐。 |
| ARKUI\_SCROLL\_ALIGNMENT\_CENTER = 1 | 居中对齐。指定item主轴方向居中对齐于容器。 |
| ARKUI\_SCROLL\_ALIGNMENT\_END = 2 | 尾部对齐。指定item尾部与容器尾部对齐。 |
| ARKUI\_SCROLL\_ALIGNMENT\_AUTO = 3 | 自动对齐。若指定item完全处于显示区，不做调整。否则依照滑动距离最短的原则，将指定item首部对齐或尾部对齐于容器,使指定item完全处于显示区。 |

### ArkUI\_ScrollState

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ScrollState
```

**描述：**

定义当前滚动状态。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SCROLL\_STATE\_IDLE = 0 | 空闲状态。使用控制器提供的方法控制滚动时触发，拖动滚动条滚动时触发。 |
| ARKUI\_SCROLL\_STATE\_SCROLL = 1 | 滚动状态。使用手指拖动容器滚动时触发。 |
| ARKUI\_SCROLL\_STATE\_FLING = 2 | 惯性滚动状态。快速划动松手后进行惯性滚动和划动到边缘回弹时触发。 |

### ArkUI\_SliderBlockStyle

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_SliderBlockStyle
```

**描述：**

定义滑块形状。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SLIDER\_BLOCK\_STYLE\_DEFAULT = 0 | 使用默认滑块（圆形）。 |
| ARKUI\_SLIDER\_BLOCK\_STYLE\_IMAGE = 1 | 使用图片资源作为滑块。 |
| ARKUI\_SLIDER\_BLOCK\_STYLE\_SHAPE = 2 | 使用自定义形状作为滑块。 |

### ArkUI\_SliderDirection

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_SliderDirection
```

**描述：**

定义滑动条滑动方向。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SLIDER\_DIRECTION\_VERTICAL = 0 | 方向为纵向。 |
| ARKUI\_SLIDER\_DIRECTION\_HORIZONTAL = 1 | 方向为横向。 |

### ArkUI\_SliderStyle

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_SliderStyle
```

**描述：**

定义滑块与滑轨显示样式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SLIDER\_STYLE\_OUT\_SET = 0 | 滑块在滑轨上。 |
| ARKUI\_SLIDER\_STYLE\_IN\_SET = 1 | 滑块在滑轨内。 |
| ARKUI\_SLIDER\_STYLE\_NONE = 2 | 无滑块。 |

### ArkUI\_CheckboxShape

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_CheckboxShape
```

**描述：**

定义CheckBox组件形状。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ArkUI\_CHECKBOX\_SHAPE\_CIRCLE = 0 | 圆形。 |
| ArkUI\_CHECKBOX\_SHAPE\_ROUNDED\_SQUARE = 1 | 圆角方形。 |

### ArkUI\_AnimationPlayMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_AnimationPlayMode
```

**描述：**

定义动画播放模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ANIMATION\_PLAY\_MODE\_NORMAL = 0 | 动画正向播放。 |
| ARKUI\_ANIMATION\_PLAY\_MODE\_REVERSE = 1 | 动画反向播放。 |
| ARKUI\_ANIMATION\_PLAY\_MODE\_ALTERNATE = 2 | 动画交替循环播放，在奇数次正向播放，在偶数次反向播放。 |
| ARKUI\_ANIMATION\_PLAY\_MODE\_ALTERNATE\_REVERSE = 3 | 动画反向交替循环播放，在奇数次反向播放，在偶数次正向播放。 |

### ArkUI\_ImageSize

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ImageSize
```

**描述：**

定义图片宽高样式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_IMAGE\_SIZE\_AUTO = 0 | 保持原图的比例不变。 |
| ARKUI\_IMAGE\_SIZE\_COVER = 1 | 保持宽高比进行缩小或者放大，使得图片两边都大于或等于显示边界。 |
| ARKUI\_IMAGE\_SIZE\_CONTAIN = 2 | 保持宽高比进行缩小或者放大，使得图片完全显示在显示边界内。 |

### ArkUI\_AdaptiveColor

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_AdaptiveColor
```

**描述：**

定义取色模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ADAPTIVE\_COLOR\_DEFAULT = 0 | 不使用取色模糊。 |
| ARKUI\_ADAPTIVE\_COLOR\_AVERAGE = 1 | 使用取色模糊。 |

### ArkUI\_ColorMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ColorMode
```

**描述：**

定义深浅色模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_COLOR\_MODE\_SYSTEM = 0 | 跟随系统深浅色模式。 |
| ARKUI\_COLOR\_MODE\_LIGHT = 1 | 固定使用浅色模式。 |
| ARKUI\_COLOR\_MODE\_DARK = 2 | 固定使用深色模式。 |

### ArkUI\_SystemColorMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_SystemColorMode
```

**描述：**

定义系统深浅色模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SYSTEM\_COLOR\_MODE\_LIGHT = 0 | 浅色模式。 |
| ARKUI\_SYSTEM\_COLOR\_MODE\_DARK = 1 | 深色模式。 |

### ArkUI\_BlurStyle

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_BlurStyle
```

**描述：**

定义背景模糊样式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_BLUR\_STYLE\_THIN = 0 | 轻薄材质模糊。 |
| ARKUI\_BLUR\_STYLE\_REGULAR = 1 | 普通厚度材质模糊。 |
| ARKUI\_BLUR\_STYLE\_THICK = 2 | 厚材质模糊。 |
| ARKUI\_BLUR\_STYLE\_BACKGROUND\_THIN = 3 | 近距景深模糊。 |
| ARKUI\_BLUR\_STYLE\_BACKGROUND\_REGULAR = 4 | 中距景深模糊。 |
| ARKUI\_BLUR\_STYLE\_BACKGROUND\_THICK = 5 | 远距景深模糊。 |
| ARKUI\_BLUR\_STYLE\_BACKGROUND\_ULTRA\_THICK = 6 | 超远距景深模糊。 |
| ARKUI\_BLUR\_STYLE\_NONE = 7 | 关闭模糊。 |
| ARKUI\_BLUR\_STYLE\_COMPONENT\_ULTRA\_THIN = 8 | 组件超轻薄材质模糊。 |
| ARKUI\_BLUR\_STYLE\_COMPONENT\_THIN = 9 | 组件轻薄材质模糊。 |
| ARKUI\_BLUR\_STYLE\_COMPONENT\_REGULAR = 10 | 组件普通材质模糊。 |
| ARKUI\_BLUR\_STYLE\_COMPONENT\_THICK = 11 | 组件厚材质模糊。 |
| ARKUI\_BLUR\_STYLE\_COMPONENT\_ULTRA\_THICK = 12 | 组件超厚材质模糊。 |

### ArkUI\_BlurStyleActivePolicy

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_BlurStyleActivePolicy
```

**描述：**

定义背景模糊激活策略。

**起始版本：** 19

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_BLUR\_STYLE\_ACTIVE\_POLICY\_FOLLOWS\_WINDOW\_ACTIVE\_STATE = 0 | 模糊效果跟随窗口焦点状态变化，非焦点不模糊，焦点模糊。 |
| ARKUI\_BLUR\_STYLE\_ACTIVE\_POLICY\_ALWAYS\_ACTIVE = 1 | 一直有模糊效果。 |
| ARKUI\_BLUR\_STYLE\_ACTIVE\_POLICY\_ALWAYS\_INACTIVE = 2 | 一直无模糊效果。 |

### ArkUI\_VerticalAlignment

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_VerticalAlignment
```

**描述：**

定义垂直对齐方式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_VERTICAL\_ALIGNMENT\_TOP = 0 | 顶部对齐。 |
| ARKUI\_VERTICAL\_ALIGNMENT\_CENTER = 1 | 居中对齐，默认对齐方式。 |
| ARKUI\_VERTICAL\_ALIGNMENT\_BOTTOM = 2 | 底部对齐。 |

### ArkUI\_HorizontalAlignment

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_HorizontalAlignment
```

**描述：**

定义语言方向对齐方式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_HORIZONTAL\_ALIGNMENT\_START = 0 | 按照语言方向起始端对齐。 |
| ARKUI\_HORIZONTAL\_ALIGNMENT\_CENTER = 1 | 居中对齐，默认对齐方式。 |
| ARKUI\_HORIZONTAL\_ALIGNMENT\_END = 2 | 按照语言方向末端对齐。 |

### ArkUI\_TextOverflow

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_TextOverflow
```

**描述：**

定义文本超长时的显示方式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXT\_OVERFLOW\_NONE = 0 | 文本超长时不裁剪显示。 |
| ARKUI\_TEXT\_OVERFLOW\_CLIP = 1 | 文本超长时进行裁剪显示。 |
| ARKUI\_TEXT\_OVERFLOW\_ELLIPSIS = 2 | 文本超长时显示不下的文本用省略号代替。 |
| ARKUI\_TEXT\_OVERFLOW\_MARQUEE = 3 | 文本超长时以跑马灯的方式展示。 |

### ArkUI\_ImageSpanAlignment

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ImageSpanAlignment
```

**描述：**

定义图片基于文本的对齐方式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_IMAGE\_SPAN\_ALIGNMENT\_BASELINE = 0 | 图片下边沿与文本BaseLine对齐。 |
| ARKUI\_IMAGE\_SPAN\_ALIGNMENT\_BOTTOM | 图片下边沿与文本下边沿对齐。 |
| ARKUI\_IMAGE\_SPAN\_ALIGNMENT\_CENTER | 图片中间与文本中间对齐。 |
| ARKUI\_IMAGE\_SPAN\_ALIGNMENT\_TOP | 图片上边沿与文本上边沿对齐。 |
| ARKUI\_IMAGE\_SPAN\_ALIGNMENT\_FOLLOW\_PARAGRAPH | 图片对齐方式跟随Text组件对齐方式。  **起始版本：** 20 |

### ArkUI\_ObjectFit

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ObjectFit
```

**描述：**

定义[Image](ts-basic-components-image.md)组件的图片填充效果。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_OBJECT\_FIT\_CONTAIN = 0 | 保持宽高比进行缩小或者放大，使得图片完全显示在显示边界内。 |
| ARKUI\_OBJECT\_FIT\_COVER = 1 | 保持宽高比进行缩小或者放大，使得图片两边都大于或等于显示边界。 |
| ARKUI\_OBJECT\_FIT\_AUTO = 2 | 自适应显示。 |
| ARKUI\_OBJECT\_FIT\_FILL = 3 | 不保持宽高比进行放大缩小，使得图片充满显示边界。 |
| ARKUI\_OBJECT\_FIT\_SCALE\_DOWN = 4 | 保持宽高比显示，图片缩小或者保持不变。 |
| ARKUI\_OBJECT\_FIT\_NONE = 5 | 保持原有尺寸显示。 |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_TOP\_START = 6 | 图片大小不变，在image组件中顶部起始端对齐。 |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_TOP = 7 | 图片大小不变，在image组件中顶部横向居中对齐。 |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_TOP\_END = 8 | 图片大小不变，在image组件中顶部尾端对齐。 |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_START = 9 | 图片大小不变，在image组件中起始端纵向居中对齐。 |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_CENTER = 10 | 图片大小不变，在image组件中横向和纵向居中对齐。 |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_END = 11 | 图片大小不变，在image组件中尾端纵向居中对齐。 |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_BOTTOM\_START = 12 | 图片大小不变，在image组件中底部起始端对齐。 |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_BOTTOM = 13 | 图片大小不变，在image组件中底部横向居中对齐。 |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_BOTTOM\_END = 14 | 图片大小不变，在image组件中底部尾端对齐。 |
| ARKUI\_OBJECT\_FIT\_NONE\_MATRIX = 15 | 不改变图像原始大小，需要配合[NODE\_IMAGE\_IMAGE\_MATRIX](capi-native-node-h.md#arkui_nodeattributetype)使用。  **起始版本：** 21 |

### ArkUI\_ImageInterpolation

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ImageInterpolation
```

**描述：**

定义图片插值效果。用于优化图片缩放时的锯齿问题。SVG类型图源不支持该属性。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_IMAGE\_INTERPOLATION\_NONE = 0 | 不使用图片插值。 |
| ARKUI\_IMAGE\_INTERPOLATION\_LOW = 1 | 低图片插值。 |
| ARKUI\_IMAGE\_INTERPOLATION\_MEDIUM = 2 | 中图片插值。 |
| ARKUI\_IMAGE\_INTERPOLATION\_HIGH = 3 | 高图片插值，插值质量最高。 |

### ArkUI\_DynamicRangeMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_DynamicRangeMode
```

**描述：**

定义图像动态范围模式（例如：SDR/HDR），用于控制图像的明暗与色彩显示范围。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_DYNAMIC\_RANGE\_MODE\_HIGH = 0 | 高动态范围（High Dynamic Range，简称HDR），表示图片中显示亮度（brightness）的最小值和最大值的范围，范围越大图像的亮度表达更逼近真实环境，在太亮的环境下不会产生过曝（一片白），太暗的环境下不会产生过暗的效果（一片黑）。 |
| ARKUI\_DYNAMIC\_RANGE\_MODE\_CONSTRAINT | 受限的高动态范围，包含比SDR更丰富的亮度和色彩，但不是完整的HDR，一般用于需要兼容SDR的情况。 |
| ARKUI\_DYNAMIC\_RANGE\_MODE\_STANDARD | 标准动态范围（Standard Dynamic Range，简称SDR），表示亮度范围有限，一般在0~100尼特（亮度单位）左右，明暗对比度较小，暗部容易糊成黑，亮部容易爆白。 |

### ArkUI\_ImageRotateOrientation

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ImageRotateOrientation
```

**描述：**

定义图像旋转方向。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ORIENTATION\_AUTO = 0 | 读取图片携带的EXIF元数据作为显示方向，支持旋转和镜像。EXIF（Exchangeable image file format）是专门为数码相机的照片设定的文件格式，可以记录数码照片的属性信息和拍摄数据。 |
| ARKUI\_ORIENTATION\_UP | 默认按照当前图片的像素数据进行显示，不做任何处理。 |
| ARKUI\_ORIENTATION\_RIGHT | 将当前图片顺时针旋转90度后显示。 |
| ARKUI\_ORIENTATION\_DOWN | 将当前图片顺时针旋转180度后显示。 |
| ARKUI\_ORIENTATION\_LEFT | 将当前图片顺时针旋转270度后显示。 |
| ARKUI\_ORIENTATION\_UP\_MIRRORED | 将当前图片水平翻转后显示。 |
| ARKUI\_ORIENTATION\_RIGHT\_MIRRORED | 将当前图片水平翻转再顺时针旋转90度后显示。 |
| ARKUI\_ORIENTATION\_DOWN\_MIRRORED | 将当前图片垂直翻转后显示。 |
| ARKUI\_ORIENTATION\_LEFT\_MIRRORED | 将当前图片水平翻转再顺时针旋转270度后显示。 |

### ArkUI\_BlendMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_BlendMode
```

**描述：**

混合模式枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_BLEND\_MODE\_NONE = 0 | 将上层图像直接覆盖到下层图像上，不进行任何混合操作。 |
| ARKUI\_BLEND\_MODE\_CLEAR = 1 | 将源像素覆盖的目标像素清除为完全透明。 |
| ARKUI\_BLEND\_MODE\_SRC = 2 | r = s，只显示源像素。 |
| ARKUI\_BLEND\_MODE\_DST = 3 | r = d，只显示目标像素。 |
| ARKUI\_BLEND\_MODE\_SRC\_OVER = 4 | r = s + (1 - sa) \* d，将源像素按照透明度进行混合，覆盖在目标像素上。 |
| ARKUI\_BLEND\_MODE\_DST\_OVER = 5 | r = d + (1 - da) \* s，将目标像素按照透明度进行混合，覆盖在源像素上。 |
| ARKUI\_BLEND\_MODE\_SRC\_IN = 6 | r = s \* da，只显示源像素中与目标像素重叠的部分。 |
| ARKUI\_BLEND\_MODE\_DST\_IN = 7 | r = d \* sa，只显示目标像素中与源像素重叠的部分。 |
| ARKUI\_BLEND\_MODE\_SRC\_OUT = 8 | r = s \* (1 - da)，只显示源像素中与目标像素不重叠的部分。 |
| ARKUI\_BLEND\_MODE\_DST\_OUT = 9 | r = d \* (1 - sa)，只显示目标像素中与源像素不重叠的部分。 |
| ARKUI\_BLEND\_MODE\_SRC\_ATOP = 10 | r = s \* da + d \* (1 - sa)，在源像素和目标像素重叠的地方绘制源像素，在源像素和目标像素不重叠的地方绘制目标像素。 |
| ARKUI\_BLEND\_MODE\_DST\_ATOP = 11 | r = d \* sa + s \* (1 - da)，在源像素和目标像素重叠的地方绘制目标像素，在源像素和目标像素不重叠的地方绘制源像素。 |
| ARKUI\_BLEND\_MODE\_XOR = 12 | r = s \* (1 - da) + d \* (1 - sa)，只显示源像素与目标像素不重叠的部分。 |
| ARKUI\_BLEND\_MODE\_PLUS = 13 | r = min(s + d, 1)，将源像素值与目标像素值相加，并将结果作为新的像素值。 |
| ARKUI\_BLEND\_MODE\_MODULATE = 14 | r = s \* d，将源像素与目标像素进行乘法运算，并将结果作为新的像素值。 |
| ARKUI\_BLEND\_MODE\_SCREEN = 15 | r = s + d - s \* d，将两个图像的像素值相加，然后减去它们的乘积来实现混合。 |
| ARKUI\_BLEND\_MODE\_OVERLAY = 16 | 根据目标像素来决定使用MULTIPLY混合模式还是SCREEN混合模式。 |
| ARKUI\_BLEND\_MODE\_DARKEN = 17 | rc = s + d - max(s \* da, d \* sa), ra = kSrcOver，当两个颜色重叠时，较暗的颜色会覆盖较亮的颜色。 |
| ARKUI\_BLEND\_MODE\_LIGHTEN = 18 | rc = s + d - min(s \* da, d \* sa), ra = kSrcOver，将源图像和目标图像中的像素进行比较，选取两者中较亮的像素作为最终的混合结果。 |
| ARKUI\_BLEND\_MODE\_COLOR\_DODGE = 19 | 使目标像素变得更亮来反映源像素。 |
| ARKUI\_BLEND\_MODE\_COLOR\_BURN = 20 | 使目标像素变得更暗来反映源像素。 |
| ARKUI\_BLEND\_MODE\_HARD\_LIGHT = 21 | 根据源像素的值来决定目标像素变得更亮或者更暗。根据源像素来决定使用MULTIPLY混合模式还是SCREEN混合模式。 |
| ARKUI\_BLEND\_MODE\_SOFT\_LIGHT = 22 | 根据源像素来决定使用LIGHTEN混合模式还是DARKEN混合模式。 |
| ARKUI\_BLEND\_MODE\_DIFFERENCE = 23 | rc = s + d - 2 \* (min(s \* da, d \* sa)), ra = kSrcOver，对比源像素和目标像素，亮度更高的像素减去亮度更低的像素，产生高对比度的效果。 |
| ARKUI\_BLEND\_MODE\_EXCLUSION = 24 | rc = s + d - two(s \* d), ra = kSrcOver，对比源像素和目标像素，亮度更高的像素减去亮度更低的像素，产生柔和的效果。 |
| ARKUI\_BLEND\_MODE\_MULTIPLY = 25 | r = s \* (1 - da) + d \* (1 - sa) + s \* d，将源图像与目标图像进行乘法混合，得到一张新的图像。 |
| ARKUI\_BLEND\_MODE\_HUE = 26 | 保留源图像的亮度和饱和度，但会使用目标图像的色调来替换源图像的色调。 |
| ARKUI\_BLEND\_MODE\_SATURATION = 27 | 保留目标像素的亮度和色调，但会使用源像素的饱和度来替换目标像素的饱和度。 |
| ARKUI\_BLEND\_MODE\_COLOR = 28 | 保留源像素的饱和度和色调，但会使用目标像素的亮度来替换源像素的亮度。 |
| ARKUI\_BLEND\_MODE\_LUMINOSITY = 29 | 保留目标像素的色调和饱和度，但会用源像素的亮度替换目标像素的亮度。 |

### ArkUI\_Direction

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_Direction
```

**描述：**

设置容器元素内主轴方向上的布局枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_DIRECTION\_LTR = 0 | 元素从左到右布局，该值为默认值。 |
| ARKUI\_DIRECTION\_RTL = 1 | 元素从右到左布局。 |
| ARKUI\_DIRECTION\_AUTO = 3 | 使用系统布局方向。 |

### ArkUI\_ItemAlignment

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ItemAlignment
```

**描述：**

设置子组件在父容器交叉轴的对齐格式枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ITEM\_ALIGNMENT\_AUTO = 0 | 使用[Flex](ts-container-flex.md)容器中默认配置，该值为默认值。 |
| ARKUI\_ITEM\_ALIGNMENT\_START = 1 | 元素在Flex容器中，交叉轴方向首部对齐。 |
| ARKUI\_ITEM\_ALIGNMENT\_CENTER = 2 | 元素在Flex容器中，交叉轴方向居中对齐。 |
| ARKUI\_ITEM\_ALIGNMENT\_END = 3 | 元素在Flex容器中，交叉轴方向底部对齐。 |
| ARKUI\_ITEM\_ALIGNMENT\_STRETCH = 4 | 元素在Flex容器中，交叉轴方向拉伸填充。 |
| ARKUI\_ITEM\_ALIGNMENT\_BASELINE = 5 | 元素在Flex容器中，交叉轴方向文本基线对齐。 |

### ArkUI\_ColorStrategy

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ColorStrategy
```

**描述：**

前景和阴影颜色的枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_COLOR\_STRATEGY\_INVERT = 0 | 前景色为控件背景色的反色。 |
| ARKUI\_COLOR\_STRATEGY\_AVERAGE = 1 | 控件背景阴影色为控件背景阴影区域的平均色。 |
| ARKUI\_COLOR\_STRATEGY\_PRIMARY = 2 | 控件背景阴影色为控件背景阴影区域的主色。 |

### ArkUI\_FlexAlignment

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_FlexAlignment
```

**描述：**

定义垂直方向对齐方式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_FLEX\_ALIGNMENT\_START = 1 | 主轴方向首端对齐，该值为默认值。 |
| ARKUI\_FLEX\_ALIGNMENT\_CENTER = 2 | 主轴方向中心对齐。 |
| ARKUI\_FLEX\_ALIGNMENT\_END = 3 | 主轴方向尾部对齐。 |
| ARKUI\_FLEX\_ALIGNMENT\_SPACE\_BETWEEN = 6 | [Flex](ts-container-flex.md)主轴方向均匀分配弹性元素，相邻元素之间距离相同，第一个元素行首对齐，最后的元素行尾对齐。 |
| ARKUI\_FLEX\_ALIGNMENT\_SPACE\_AROUND = 7 | Flex主轴方向均匀分配弹性元素，相邻元素之间距离相同，第一个元素到行首的距离时相邻元素间距离的一半。 |
| ARKUI\_FLEX\_ALIGNMENT\_SPACE\_EVENLY = 8 | Flex主轴方向均匀分配弹性元素，相邻元素之间距离、第一个元素到行首的距离和最后的元素到行尾的距离均相等。 |

### ArkUI\_FlexDirection

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_FlexDirection
```

**描述：**

定义[Flex](ts-container-flex.md)容器的主轴方向。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_FLEX\_DIRECTION\_ROW = 0 | 主轴与行方向一致，该值为默认值。 |
| ARKUI\_FLEX\_DIRECTION\_COLUMN = 1 | 主轴与列方向一致。 |
| ARKUI\_FLEX\_DIRECTION\_ROW\_REVERSE = 2 | 主轴与行方向相反。 |
| ARKUI\_FLEX\_DIRECTION\_COLUMN\_REVERSE = 3 | 主轴与列方向相反。 |

### ArkUI\_FlexWrap

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_FlexWrap
```

**描述：**

定义Flex行列布局模式模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_FLEX\_WRAP\_NO\_WRAP = 0 | 单行/单列布局，子项不能超出容器，该值为默认值。 |
| ARKUI\_FLEX\_WRAP\_WRAP = 1 | 多行/多列布局，子项允许超出容器。 |
| ARKUI\_FLEX\_WRAP\_WRAP\_REVERSE = 2 | 反向多行/多列布局，子项允许超出容器。 |

### ArkUI\_Visibility

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_Visibility
```

**描述：**

控制组件的显隐枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_VISIBILITY\_VISIBLE = 0 | 显示。 |
| ARKUI\_VISIBILITY\_HIDDEN = 1 | 隐藏，但参与布局进行占位。 |
| ARKUI\_VISIBILITY\_NONE = 2 | 隐藏，但不参与布局，不进行占位。 |

### ArkUI\_CalendarAlignment

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_CalendarAlignment
```

**描述：**

日历选择器与入口组件对齐方式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_CALENDAR\_ALIGNMENT\_START = 0 | 选择器和入口组件左对齐方式。 |
| ARKUI\_CALENDAR\_ALIGNMENT\_CENTER = 1 | 选择器和入口组件居中对齐方式。 |
| ARKUI\_CALENDAR\_ALIGNMENT\_END = 2 | 选择器和入口组件右对齐方式。 |

### ArkUI\_MaskType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_MaskType
```

**描述：**

遮罩类型枚举。遮罩是一种用于限制组件显示区域的手段，它利用特定的形状对组件内容进行裁剪，从而实现只有遮罩区域内的内容才可见的效果。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_MASK\_TYPE\_RECTANGLE = 0 | 矩形类型。 |
| ARKUI\_MASK\_TYPE\_CIRCLE = 1 | 圆形类型。 |
| ARKUI\_MASK\_TYPE\_ELLIPSE = 2 | 椭圆形类型。 |
| ARKUI\_MASK\_TYPE\_PATH = 3 | 路径类型。 |
| ARKUI\_MASK\_TYPE\_PROGRESS = 4 | 进度类型。 |

### ArkUI\_ClipType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ClipType
```

**描述：**

裁剪类型枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_CLIP\_TYPE\_RECTANGLE = 0 | 矩形类型。 |
| ARKUI\_CLIP\_TYPE\_CIRCLE = 1 | 圆形类型。 |
| ARKUI\_CLIP\_TYPE\_ELLIPSE = 2 | 椭圆形类型。 |
| ARKUI\_CLIP\_TYPE\_PATH = 3 | 路径类型。 |

### ArkUI\_ShapeType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ShapeType
```

**描述：**

自定义形状。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SHAPE\_TYPE\_RECTANGLE = 0 | 矩形类型。 |
| ARKUI\_SHAPE\_TYPE\_CIRCLE = 1 | 圆形类型。 |
| ARKUI\_SHAPE\_TYPE\_ELLIPSE = 2 | 椭圆形类型。 |
| ARKUI\_SHAPE\_TYPE\_PATH = 3 | 路径类型。 |

### ArkUI\_LinearGradientDirection

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_LinearGradientDirection
```

**描述：**

定义渐变方向结构。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_LEFT = 0 | 向左渐变。 |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_TOP = 1 | 向上渐变。 |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_RIGHT = 2 | 向右渐变。 |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_BOTTOM = 3 | 向下渐变。 |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_LEFT\_TOP = 4 | 向左上渐变。 |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_LEFT\_BOTTOM = 5 | 向左下渐变。 |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_RIGHT\_TOP = 6 | 向右上渐变。 |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_RIGHT\_BOTTOM = 7 | 向右下渐变。 |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_NONE = 8 | 不渐变。 |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM = 9 | 自定义渐变方向. |

### ArkUI\_WordBreak

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_WordBreak
```

**描述：**

定义文本断行规则。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_WORD\_BREAK\_NORMAL = 0 | CJK(中文、日文、韩文)文本可以在任意2个字符间断行，而Non-CJK文本（如英文等）只能在空白符处断行。 |
| ARKUI\_WORD\_BREAK\_BREAK\_ALL | 对于Non-CJK的文本，可在任意2个字符间断行。CJK(中文、日文、韩文)文本可以在任意2个字符间断行。 |
| ARKUI\_WORD\_BREAK\_BREAK\_WORD | 对于Non-CJK的文本可在任意2个字符间断行，一行文本中有断行破发点（如空白符）时，优先按破发点换行。对于CJK的文本，换行效果与NORMAL效果保持一致。 |
| ARKUI\_WORD\_BREAK\_HYPHENATION | 对于Non-CJK的文本，可以按照音节断行。对于CJK的文本，换行效果与NORMAL效果保持一致。  **起始版本：** 18 |

### ArkUI\_EllipsisMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_EllipsisMode
```

**描述：**

定义文本省略位置。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ELLIPSIS\_MODE\_START = 0 | 省略行首内容。 |
| ARKUI\_ELLIPSIS\_MODE\_CENTER | 省略行中内容。 |
| ARKUI\_ELLIPSIS\_MODE\_END | 省略行末内容。 |

### ArkUI\_ImageRenderMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ImageRenderMode
```

**描述：**

定义图片渲染模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_IMAGE\_RENDER\_MODE\_ORIGINAL = 0 | 原色渲染模式。 |
| ARKUI\_IMAGE\_RENDER\_MODE\_TEMPLATE = 1 | 黑白渲染模式。 |

### ArkUI\_TransitionEdge

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_TransitionEdge
```

**描述：**

定义转场从边缘滑入和滑出的效果。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TRANSITION\_EDGE\_TOP = 0 | 转场从窗口的上边缘滑入和滑出。 |
| ARKUI\_TRANSITION\_EDGE\_BOTTOM = 1 | 转场从窗口的下边缘滑入和滑出。 |
| ARKUI\_TRANSITION\_EDGE\_START = 2 | 转场从窗口的左边缘滑入和滑出。 |
| ARKUI\_TRANSITION\_EDGE\_END = 3 | 转场从窗口的右边缘滑入和滑出。 |

### ArkUI\_FinishCallbackType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_FinishCallbackType
```

**描述：**

在动画中定义[OH\_ArkUI\_AnimatorOption\_RegisterOnFinishCallback](capi-native-animate-h.md#oh_arkui_animatoroption_registeronfinishcallback)回调的类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_FINISH\_CALLBACK\_REMOVED = 0 | 当整个动画结束并立即删除时，将触发回调。 |
| ARKUI\_FINISH\_CALLBACK\_LOGICALLY = 1 | 当动画在逻辑上处于下降状态，但可能仍处于其长尾状态时，将触发回调。长尾状态是指动画即将完全停止前的残余变化过程，此时动画的数值变化已非常微小，接近目标值。 |

### ArkUI\_ListItemAlignment

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ListItemAlignment
```

**描述：**

交叉轴方向的布局方式，默认值为ARKUI\_LIST\_ITEM\_ALIGNMENT\_START。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LIST\_ITEM\_ALIGNMENT\_START = 0 | [ListItem](ts-container-listitem.md#listitem10)在List中，交叉轴方向首部对齐。 |
| ARKUI\_LIST\_ITEM\_ALIGNMENT\_CENTER = 1 | ListItem在List中，交叉轴方向居中对齐。 |
| ARKUI\_LIST\_ITEM\_ALIGNMENT\_END = 2 | ListItem在List中，交叉轴方向尾部对齐。 |

### ArkUI\_BlendApplyType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_BlendApplyType
```

**描述：**

指定的混合模式应用于视图的内容选项.

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| BLEND\_APPLY\_TYPE\_FAST = 0 | 在目标图像上按顺序混合视图的内容. |
| BLEND\_APPLY\_TYPE\_OFFSCREEN = 1 | 将此组件和子组件内容绘制到离屏画布上，然后整体进行混合. |

### ArkUI\_LengthMetricUnit

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_LengthMetricUnit
```

**描述：**

定义组件的单位模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LENGTH\_METRIC\_UNIT\_DEFAULT = -1 | 默认，字体类单位为fp，非字体类单位为vp。 |
| ARKUI\_LENGTH\_METRIC\_UNIT\_PX = 0 | 单位为px。 |
| ARKUI\_LENGTH\_METRIC\_UNIT\_VP = 1 | 单位为vp。 |
| ARKUI\_LENGTH\_METRIC\_UNIT\_FP = 2 | 单位为fp。 |

### ArkUI\_TextInputContentType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_TextInputContentType
```

**描述：**

定义自动填充类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_USER\_NAME = 0 | 【用户名】在已启用密码保险箱的情况下，支持用户名的自动保存和自动填充。 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_PASSWORD | 【密码】在已启用密码保险箱的情况下，支持密码的自动保存和自动填充。 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_NEW\_PASSWORD | 【新密码】在已启用密码保险箱的情况下，支持自动生成新密码。 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_FULL\_STREET\_ADDRESS | 【详细地址】在已启用情景化自动填充的情况下，支持详细地址的自动保存和自动填充。 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_HOUSE\_NUMBER | 【门牌号】在已启用情景化自动填充的情况下，支持门牌号的自动保存和自动填充。 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_DISTRICT\_ADDRESS | 【区/县】在已启用情景化自动填充的情况下，支持区/县的自动保存和自动填充。 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_CITY\_ADDRESS | 【市】在已启用情景化自动填充的情况下，支持市的自动保存和自动填充。 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_PROVINCE\_ADDRESS | 【省】在已启用情景化自动填充的情况下，支持省的自动保存和自动填充。 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_COUNTRY\_ADDRESS | 【国家】在已启用情景化自动填充的情况下，支持国家的自动保存和自动填充。 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_PERSON\_FULL\_NAME | 【姓名】在已启用情景化自动填充的情况下，支持姓名的自动保存和自动填充。 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_PERSON\_LAST\_NAME | 【姓氏】在已启用情景化自动填充的情况下，支持姓氏的自动保存和自动填充。 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_PERSON\_FIRST\_NAME | 【名字】在已启用情景化自动填充的情况下，支持名字的自动保存和自动填充。 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_PHONE\_NUMBER | 【手机号】在已启用情景化自动填充的情况下，支持手机号的自动保存和自动填充。 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_PHONE\_COUNTRY\_CODE | 【国家代码】在已启用情景化自动填充的情况下，支持国家代码的自动保存和自动填充。 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_FULL\_PHONE\_NUMBER | 【包含国家代码的手机号】在已启用情景化自动填充的情况下，支持包含国家代码的手机号的自动保存和自动填充。 |
| ARKUI\_TEXTINPUT\_CONTENT\_EMAIL\_ADDRESS | 【邮箱地址】在已启用情景化自动填充的情况下，支持邮箱地址的自动保存和自动填充。 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_BANK\_CARD\_NUMBER | 【银行卡号】在已启用情景化自动填充的情况下，支持银行卡号的自动保存和自动填充。 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_ID\_CARD\_NUMBER | 【身份证号】在已启用情景化自动填充的情况下，支持身份证号的自动保存和自动填充。 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_NICKNAME | 【昵称】在已启用情景化自动填充的情况下，支持昵称的自动保存和自动填充。 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_DETAIL\_INFO\_WITHOUT\_STREET | 【无街道地址】在已启用情景化自动填充的情况下，支持无街道地址的自动保存和自动填充。 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_FORMAT\_ADDRESS | 【标准地址】在已启用情景化自动填充的情况下，支持标准地址的自动保存和自动填充。 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_PASSPORT\_NUMBER | 【护照号】在已启用情景化自动填充的情况下，支持护照号的自动保存和自动填充。  **起始版本：** 18 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_VALIDITY | 【护照有效期】在已启用情景化自动填充的情况下，支持护照有效期的自动保存和自动填充。  **起始版本：** 18 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_ISSUE\_AT | 【护照签发地】在已启用情景化自动填充的情况下，支持护照签发地的自动保存和自动填充。  **起始版本：** 18 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_ORGANIZATION | 【发票抬头名称】在已启用情景化自动填充的情况下，支持发票抬头名称的自动保存和自动填充。  **起始版本：** 18 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_TAX\_ID | 【税号】在已启用情景化自动填充的情况下，支持税号的自动保存和自动填充。  **起始版本：** 18 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_ADDRESS\_CITY\_AND\_STATE | 【所在地区】在已启用情景化自动填充的情况下，支持所在地区的自动保存和自动填充。  **起始版本：** 18 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_FLIGHT\_NUMBER | 【航班号】暂不支持自动保存和自动填充。  **起始版本：** 18 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_LICENSE\_NUMBER | 【驾驶证号】暂不支持自动保存和自动填充。  **起始版本：** 18 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_LICENSE\_FILE\_NUMBER | 【驾驶证档案编号】暂不支持自动保存和自动填充。  **起始版本：** 18 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_LICENSE\_PLATE | 【车牌号】在已启用情景化自动填充的情况下，支持车牌号的自动保存和自动填充。  **起始版本：** 18 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_ENGINE\_NUMBER | 【行驶证发动机号】暂不支持自动保存和自动填充。  **起始版本：** 18 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_LICENSE\_CHASSIS\_NUMBER | 【车牌识别号】暂不支持自动保存和自动填充。  **起始版本：** 18 |

### ArkUI\_BarrierDirection

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_BarrierDirection
```

**描述：**

定义屏障线的方向。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_BARRIER\_DIRECTION\_START = 0 | 屏障在其所有[referencedId](ts-container-relativecontainer.md#barrierstyle12对象说明)的最左侧，该值为默认值。 |
| ARKUI\_BARRIER\_DIRECTION\_END = 1 | 屏障在其所有referencedId的最右侧。 |
| ARKUI\_BARRIER\_DIRECTION\_TOP = 2 | 屏障在其所有referencedId的最上方。 |
| ARKUI\_BARRIER\_DIRECTION\_BOTTOM = 3 | 屏障在其所有referencedId的最下方。 |

### ArkUI\_RelativeLayoutChainStyle

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_RelativeLayoutChainStyle
```

**描述：**

定义链的风格。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_RELATIVE\_LAYOUT\_CHAIN\_STYLE\_SPREAD = 0 | 组件在约束锚点间均匀分布，该值为默认值。 |
| ARKUI\_RELATIVE\_LAYOUT\_CHAIN\_STYLE\_SPREAD\_INSIDE = 1 | 除首尾2个子组件的其他组件在约束锚点间均匀分布。 |
| ARKUI\_RELATIVE\_LAYOUT\_CHAIN\_STYLE\_PACKED = 2 | 链内子组件无间隙。 |

### ArkUI\_TextInputStyle

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_TextInputStyle
```

**描述：**

定义输入框风格。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXTINPUT\_STYLE\_DEFAULT = 0 | 默认风格，光标宽1.5vp，光标高度与文本选中底板高度和字体大小相关。 |
| ARKUI\_TEXTINPUT\_STYLE\_INLINE | 内联输入风格。文本选中底板高度与输入框高度相同。 |

### ArkUI\_KeyboardAppearance

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_KeyboardAppearance
```

**描述：**

定义输入框拉起的键盘样式。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_KEYBOARD\_APPEARANCE\_NONE\_IMMERSIVE = 0 | 默认模式，不使用沉浸式样式。 |
| ARKUI\_KEYBOARD\_APPEARANCE\_IMMERSIVE = 1 | 沉浸式模式，由系统决定采用的样式。 |
| ARKUI\_KEYBOARD\_APPEARANCE\_LIGHT\_IMMERSIVE = 2 | 浅色沉浸式样式。 |
| ARKUI\_KEYBOARD\_APPEARANCE\_DARK\_IMMERSIVE = 3 | 深色沉浸式样式。 |

### ArkUI\_TextDataDetectorType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_TextDataDetectorType
```

**描述：**

定义文本识别的实体类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXT\_DATA\_DETECTOR\_TYPE\_PHONE\_NUMBER = 0 | 电话号码。 |
| ARKUI\_TEXT\_DATA\_DETECTOR\_TYPE\_URL | 链接。 |
| ARKUI\_TEXT\_DATA\_DETECTOR\_TYPE\_EMAIL | 邮箱。 |
| ARKUI\_TEXT\_DATA\_DETECTOR\_TYPE\_ADDRESS | 地址。 |

### ArkUI\_ButtonType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ButtonType
```

**描述：**

定义按钮样式枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_BUTTON\_TYPE\_NORMAL = 0 | 普通按钮，默认不带圆角。 |
| ARKUI\_BUTTON\_TYPE\_CAPSULE = 1 | 胶囊型按钮，圆角默认为高度的一半。 |
| ARKUI\_BUTTON\_TYPE\_CIRCLE = 2 | 圆形按钮。 |
| ARKUI\_BUTTON\_ROUNDED\_RECTANGLE = 8 | 圆角矩形按钮。  **起始版本：** 19 |

### ArkUI\_RenderFit

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_RenderFit
```

**描述：**

定义动画终态内容大小与位置的枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_RENDER\_FIT\_CENTER = 0 | 保持动画终态的内容大小，并且内容始终与组件保持中心对齐。 |
| ARKUI\_RENDER\_FIT\_TOP = 1 | 保持动画终态的内容大小，并且内容始终与组件保持顶部中心对齐。 |
| ARKUI\_RENDER\_FIT\_BOTTOM = 2 | 保持动画终态的内容大小，并且内容始终与组件保持底部中心对齐。 |
| ARKUI\_RENDER\_FIT\_LEFT = 3 | 保持动画终态的内容大小，并且内容始终与组件保持左侧对齐。 |
| ARKUI\_RENDER\_FIT\_RIGHT = 4 | 保持动画终态的内容大小，并且内容始终与组件保持右侧对齐。 |
| ARKUI\_RENDER\_FIT\_TOP\_LEFT = 5 | 保持动画终态的内容大小，并且内容始终与组件保持左上角对齐。 |
| ARKUI\_RENDER\_FIT\_TOP\_RIGHT = 6 | 保持动画终态的内容大小，并且内容始终与组件保持右上角对齐。 |
| ARKUI\_RENDER\_FIT\_BOTTOM\_LEFT = 7 | 保持动画终态的内容大小，并且内容始终与组件保持左下角对齐。 |
| ARKUI\_RENDER\_FIT\_BOTTOM\_RIGHT = 8 | 保持动画终态的内容大小，并且内容始终与组件保持右下角对齐。 |
| ARKUI\_RENDER\_FIT\_RESIZE\_FILL = 9 | 不考虑动画终态内容的宽高比，并且内容始终缩放到组件的大小。 |
| ARKUI\_RENDER\_FIT\_RESIZE\_CONTAIN = 10 | 保持动画终态内容的宽高比进行缩小或放大，使内容完整显示在组件内，且与组件保持中心对齐。 |
| ARKUI\_RENDER\_FIT\_RESIZE\_CONTAIN\_TOP\_LEFT = 11 | 保持动画终态内容的宽高比进行缩小或放大，使内容完整显示在组件内。当组件宽方向有剩余时，内容与组件保持左侧对齐，当组件高方向有剩余时，内容与组件保持顶部对齐。 |
| ARKUI\_RENDER\_FIT\_RESIZE\_CONTAIN\_BOTTOM\_RIGHT = 12 | 保持动画终态内容的宽高比进行缩小或放大，使内容完整显示在组件内。当组件宽方向有剩余时，内容与组件保持右侧对齐，当组件高方向有剩余时，内容与组件保持底部对齐。 |
| ARKUI\_RENDER\_FIT\_RESIZE\_COVER = 13 | 保持动画终态内容的宽高比进行缩小或放大，使内容两边都大于或等于组件两边，且与组件保持中心对齐，显示内容的中间部分。 |
| ARKUI\_RENDER\_FIT\_RESIZE\_COVER\_TOP\_LEFT = 14 | 保持动画终态内容的宽高比进行缩小或放大，使内容的两边都恰好大于或等于组件两边。当内容宽方向有剩余时，内容与组件保持左侧对齐，显示内容的左侧部分。当内容高方向有剩余时，内容与组件保持顶部对齐，显示内容的顶侧部分。 |
| ARKUI\_RENDER\_FIT\_RESIZE\_COVER\_BOTTOM\_RIGHT = 15 | 保持动画终态内容的宽高比进行缩小或放大，使内容的两边都恰好大于或等于组件两边。当内容宽方向有剩余时，内容与组件保持右侧对齐，显示内容的右侧部分。当内容高方向有剩余时，内容与组件保持底部对齐，显示内容的底侧部分。 |

### ArkUI\_SwiperIndicatorType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_SwiperIndicatorType
```

**描述：**

定义Swiper组件的导航指示器类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SWIPER\_INDICATOR\_TYPE\_DOT = 0 | 圆点指示器类型。 |
| ARKUI\_SWIPER\_INDICATOR\_TYPE\_DIGIT = 1 | 数字指示器类型。 |

### ArkUI\_AnimationDirection

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_AnimationDirection
```

**描述：**

动画播放方向。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ANIMATION\_DIRECTION\_NORMAL = 0 | 动画正向循环播放。 |
| ARKUI\_ANIMATION\_DIRECTION\_REVERSE = 1 | 动画反向循环播放。 |
| ARKUI\_ANIMATION\_DIRECTION\_ALTERNATE = 2 | 动画交替循环播放，在奇数次正向播放，在偶数次反向播放。 |
| ARKUI\_ANIMATION\_DIRECTION\_ALTERNATE\_REVERSE = 3 | 动画反向交替循环播放，在奇数次反向播放，在偶数次正向播放。 |

### ArkUI\_ListItemSwipeActionState

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ListItemSwipeActionState
```

**描述：**

定义[Listitem](ts-container-listitem.md#listitem10)组件[SwipeAction](ts-container-listitem.md#swipeaction9)方法的显隐模式，默认值为ARKUI\_LIST\_ITEM\_SWIPE\_ACTION\_STATE\_COLLAPSED。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LIST\_ITEM\_SWIPE\_ACTION\_STATE\_COLLAPSED = 0 | 收起状态，当ListItem与主轴方向相反滑动时操作项处于隐藏状态。 |
| ARKUI\_LIST\_ITEM\_SWIPE\_ACTION\_STATE\_EXPANDED = 1 | 收起状态，当ListItem与主轴方向相反滑动时操作项处于显示状态。 |
| ARKUI\_LIST\_ITEM\_SWIPE\_ACTION\_STATE\_ACTIONING = 2 | 长距离状态，当ListItem进入长距删除区后删除ListItem的状态。 |

### ArkUI\_ListItemSwipeEdgeEffect

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ListItemSwipeEdgeEffect
```

**描述：**

定义Listitem组件[swipeAction](ts-container-listitem.md#swipeaction9)方法的滚动模式，默认值为ARKUI\_LIST\_ITEM\_SWIPE\_EDGE\_EFFECT\_SPRING。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LIST\_ITEM\_SWIPE\_EDGE\_EFFECT\_SPRING = 0 | ListItem划动距离超过划出组件大小后可以继续划动。 |
| ARKUI\_LIST\_ITEM\_SWIPE\_EDGE\_EFFECT\_NONE = 1 | ListItem划动距离不能超过划出组件大小。 |

### ArkUI\_ListItemSwipeActionDirection

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ListItemSwipeActionDirection
```

**描述：**

ListItem划出菜单的展开方向。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LIST\_ITEM\_SWIPE\_ACTION\_DIRECTION\_START = 0 | 当列表方向是垂直方向时，LTR模式下表示ListItem的左边，RTL模式下表示ListItem的右边。当列表是水平方向时，表示ListItem的上边。 |
| ARKUI\_LIST\_ITEM\_SWIPE\_ACTION\_DIRECTION\_END = 1 | 当列表方向是垂直方向时，LTR模式下表示ListItem的右边，RTL模式下表示ListItem的左边。当列表是水平方向时，表示ListItem的下边。 |

### ArkUI\_AnimationStatus

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_AnimationStatus
```

**描述：**

定义帧动画的播放状态。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ANIMATION\_STATUS\_INITIAL = 0 | 动画初始状态。 |
| ARKUI\_ANIMATION\_STATUS\_RUNNING = 1 | 动画处于播放状态。 |
| ARKUI\_ANIMATION\_STATUS\_PAUSED = 2 | 动画处于暂停状态。 |
| ARKUI\_ANIMATION\_STATUS\_STOPPED = 3 | 动画处于停止状态。 |

### ArkUI\_AnimationFillMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_AnimationFillMode
```

**描述：**

定义帧动画组件在动画开始前和结束后的状态。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ANIMATION\_FILL\_MODE\_NONE = 0 | 动画未执行时不会将任何样式应用于目标，动画播放完成之后恢复初始默认状态。 |
| ARKUI\_ANIMATION\_FILL\_MODE\_FORWARDS = 1 | 目标将保留动画执行期间最后一个关键帧的状态。 |
| ARKUI\_ANIMATION\_FILL\_MODE\_BACKWARDS = 2 | 动画将在应用于目标时立即应用第一个关键帧中定义的值，并在[delay](capi-native-animate-h.md#oh_arkui_animateoption_setdelay)期间保留此值。 |
| ARKUI\_ANIMATION\_FILL\_MODE\_BOTH = 3 | 动画将遵循[ARKUI\_ANIMATION\_FILL\_MODE\_FORWARDS](capi-native-type-h.md#arkui_animationfillmode)和[ARKUI\_ANIMATION\_FILL\_MODE\_BACKWARDS](capi-native-type-h.md#arkui_animationfillmode)的规则，从而在两个方向上扩展动画属性。 |

### ArkUI\_ErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ErrorCode
```

**描述：**

定义错误码枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ERROR\_CODE\_NO\_ERROR = 0 | 无错误。 |
| ARKUI\_ERROR\_CODE\_PARAM\_INVALID = 401 | 参数错误。 |
| ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR = 500 | 接口初始化错误。  **起始版本：** 18 |
| ARKUI\_ERROR\_CODE\_INTERNAL\_ERROR = 100001 | 出现内部错误，例如内部环境错误导致失败，或者由于内部执行失败导致操作失败。  **起始版本：** 15 |
| ARKUI\_ERROR\_CODE\_PARAM\_ERROR = 100023 | 参数错误。错误码的详细介绍请参见[100023 参数错误](errorcode-node.md#section100023-参数错误)。  **起始版本：** 21 |
| ARKUI\_ERROR\_CODE\_XCOMPONENT\_STATE\_INVALID = 103501 | 当前XComponent状态异常，方法调用失败。错误码的详细介绍请参见[XComponent组件错误码](errorcode-xcomponent.md)。  **起始版本：** 19 |
| ARKUI\_ERROR\_CODE\_ATTRIBUTE\_OR\_EVENT\_NOT\_SUPPORTED = 106102 | 组件不支持特定的属性或者事件。错误码的详细介绍请参见[交互事件错误码](errorcode-event.md)。 |
| ARKUI\_ERROR\_CODE\_NOT\_SUPPROTED\_FOR\_ARKTS\_NODE = 106103 | 不支持对ArkTS创建的节点执行对应的操作。错误码的详细介绍请参见[106103 对应的操作不支持ArkTS创建的节点](errorcode-node.md#section106103-对应的操作不支持arkts创建的节点)。 |
| ARKUI\_ERROR\_CODE\_ADAPTER\_NOT\_BOUND = 106104 | 懒加载适配器未绑定到组件上。错误码的详细介绍请参见[106104 适配器未绑定](errorcode-nodeadapter.md#section106104-适配器未绑定)。 |
| ERROR\_CODE\_NATIVE\_IMPL\_NODE\_ADAPTER\_EXIST = 106105 | 适配器已存在。错误码的详细介绍请参见[106105 适配器已存在](errorcode-nodeadapter.md#section106105-适配器已存在)。 |
| ARKUI\_ERROR\_CODE\_CHILD\_NODE\_EXIST = 106106 | 对应节点已存在子节点，无法添加适配器。错误码的详细介绍请参见[106106 子节点已存在](errorcode-nodeadapter.md#section106106-子节点已存在)。 |
| ARKUI\_ERROR\_CODE\_NODE\_EVENT\_PARAM\_INDEX\_OUT\_OF\_RANGE = 106107 | 组件事件中参数长度超限。错误码的详细介绍请参见[106107 参数下标越界](errorcode-nodeadapter.md#section106107-参数下标越界)。 |
| ARKUI\_ERROR\_CODE\_NODE\_EVENT\_PARAM\_INVALID = 106108 | 组件事件中不存在该数据。错误码的详细介绍请参见[106108 数据不存在](errorcode-nodeadapter.md#section106108-数据不存在)。 |
| ARKUI\_ERROR\_CODE\_NODE\_EVENT\_NO\_RETURN = 106109 | 组件事件不支持返回值。错误码的详细介绍请参见[106109 不支持返回值](errorcode-nodeadapter.md#section106109-不支持返回值)。 |
| ARKUI\_ERROR\_CODE\_NODE\_UNSUPPORTED\_EVENT\_TYPE = 106110 | 暂不支持该事件类型。错误码的详细介绍请参见[106110 暂不支持该事件类型](errorcode-nodeadapter.md#section106110-暂不支持该事件类型)。  **起始版本：** 21 |
| ARKUI\_ERROR\_CODE\_NODE\_INDEX\_INVALID = 106200 | 传入的索引值非法。  错误码的详细介绍请参见[106200 传入的索引值非法](errorcode-router.md#section106200-传入的索引值非法)。 |
| ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED = 106201 | 查询路由导航信息失败。  错误码的详细介绍请参见[106201 查询路由导航信息失败](errorcode-router.md#section106201-查询路由导航信息失败)。 |
| ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR = 106202 | 传入的buffer size异常（数据过大）。  错误码的详细介绍请参见[106202 传入的buffer size异常](errorcode-router.md#section106202-传入的buffer-size异常)。 |
| ARKUI\_ERROR\_CODE\_NODE\_NOT\_ON\_MAIN\_TREE = 106203 | 传入的节点未挂载到组件树上。错误码的详细介绍请参见[106203 传入的节点未挂载到组件树上](errorcode-node.md#section106203-传入的节点未挂载到组件树上)。  **起始版本：** 15 |
| ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD = 106204 | 不支持在非UI线程操作传入的节点。错误码的详细介绍请参见[106204 不支持在非UI线程操作传入的节点](errorcode-node.md#section106204-不支持在非ui线程操作传入的节点)。  **起始版本：** 22 |
| ARKUI\_ERROR\_CODE\_FORCE\_DARK\_CONFIG\_INVALID = 106205 | 反色能力入参错误。错误码的详细介绍请参见[106205 反色能力入参错误](errorcode-force-dark.md#section106205-反色能力入参错误)。  **起始版本：** 20 |
| ARKUI\_ERROR\_CODE\_NODE\_IS\_ADOPTED = 106206 | 节点已被接纳为附属节点。错误码的详细介绍请参见[106206 节点已被接纳为附属节点](errorcode-adopt.md#section106206-节点已被接纳为附属节点)。  **起始版本：** 22 |
| ARKUI\_ERROR\_CODE\_NODE\_HAS\_PARENT = 106207 | 被接纳的节点已有父节点。错误码的详细介绍请参见[106207 被接纳的附属节点已有父节点](errorcode-adopt.md#section106207-被接纳的附属节点已有父节点)。  **起始版本：** 22 |
| ARKUI\_ERROR\_CODE\_NODE\_CAN\_NOT\_BE\_ADOPTED = 106208 | 节点无法被接纳为附属节点。错误码的详细介绍请参见[106208 节点无法被接纳为附属节点](errorcode-adopt.md#section106208-节点无法被接纳为附属节点)。  **起始版本：** 22 |
| ARKUI\_ERROR\_CODE\_NODE\_CAN\_NOT\_ADOPT\_TO = 106209 | 节点无法接纳其他节点。错误码的详细介绍请参见[106209 节点无法接纳其他节点](errorcode-adopt.md#section106209-节点无法接纳其他节点)。  **起始版本：** 22 |
| ARKUI\_ERROR\_CODE\_NODE\_IS\_NOT\_IN\_ADOPTED\_CHILDREN = 106210 | 节点不是被目标节点接纳的附属节点。错误码的详细介绍请参见[106210 节点不是被目标节点接纳的附属节点](errorcode-adopt.md#section106210-节点不是被目标节点接纳的附属节点)。  **起始版本：** 22 |
| ARKUI\_ERROR\_CODE\_NOT\_CUSTOM\_NODE = 106401 | 当前节点不是自定义节点。错误码的详细介绍请参见[渲染节点错误码](errorcode-node-render.md)。  **起始版本：** 20 |
| ARKUI\_ERROR\_CODE\_CHILD\_EXISTED = 106402 | 当前节点已存在子节点。错误码的详细介绍请参见[渲染节点错误码](errorcode-node-render.md)。  **起始版本：** 20 |
| ARKUI\_ERROR\_CODE\_RENDER\_PARENT\_EXISTED = 106403 | 当前渲染节点存在父组件。错误码的详细介绍请参见[渲染节点错误码](errorcode-node-render.md)。  **起始版本：** 20 |
| ARKUI\_ERROR\_CODE\_RENDER\_CHILD\_NOT\_EXIST = 106404 | 未找到对应的渲染子节点。错误码的详细介绍请参见[渲染节点错误码](errorcode-node-render.md)。  **起始版本：** 20 |
| ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE = 106405 | 参数值超出范围。错误码的详细介绍请参见[渲染节点错误码](errorcode-node-render.md)。  **起始版本：** 20 |
| ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE = 106406 | 当前渲染节点从[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)中获取。错误码的详细介绍请参见[106406 当前渲染节点从FrameNode中获取](errorcode-node-render.md#section106406-当前渲染节点从framenode中获取)。  **起始版本：** 22 |
| ARKUI\_ERROR\_CODE\_RENDER\_HAS\_INVALID\_FRAME\_NODE = 106407 | 当前渲染节点从[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)中获取且该[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)已被取消接纳为附属节点或销毁。错误码的详细介绍请参见[106407 当前渲染节点从FrameNode中获取且该FrameNode已被取消接纳为附属节点或销毁](errorcode-node-render.md#section106407-当前渲染节点从framenode中获取且该framenode已被取消接纳为附属节点或销毁)。  **起始版本：** 22 |
| ARKUI\_ERROR\_CODE\_RENDER\_NOT\_ADOPTED\_NODE = 106408 | 当前节点不处于被接纳状态。错误码的详细介绍请参见[106408 当前节点不处于被接纳状态](errorcode-node-render.md#section106408-当前节点不处于被接纳状态)。  **起始版本：** 22 |
| ARKUI\_ERROR\_CODE\_FOCUS\_NON\_FOCUSABLE = 150001 | 当前节点无法获得焦点。错误码的详细介绍请参见[150001 节点无法获得焦点](errorcode-focus.md#section150001-节点无法获得焦点)。  **起始版本：** 15 |
| ARKUI\_ERROR\_CODE\_FOCUS\_NON\_FOCUSABLE\_ANCESTOR = 150002 | 当前节点对应的祖先节点中存在无法获焦节点。错误码的详细介绍请参见[150002 祖先节点无法获得焦点](errorcode-focus.md#section150002-祖先节点无法获得焦点)。  **起始版本：** 15 |
| ARKUI\_ERROR\_CODE\_FOCUS\_NON\_EXISTENT = 150003 | 当前节点不存在。错误码的详细介绍请参见[150003 节点不存在](errorcode-focus.md#section150003-节点不存在)。  **起始版本：** 15 |
| ARKUI\_ERROR\_CODE\_COMPONENT\_SNAPSHOT\_TIMEOUT = 160002 | 截图超时。错误码的详细介绍请参见[截图错误码](errorcode-snapshot.md)。  **起始版本：** 15 |
| ARKUI\_ERROR\_CODE\_COMPONENT\_SNAPSHOT\_MODE\_NOT\_SUPPORTED = 160003 | 截图选项不支持的色彩空间或动态范围模式。错误码的详细介绍请参见[截图错误码](errorcode-snapshot.md)。  **起始版本：** 23 |
| ARKUI\_ERROR\_CODE\_COMPONENT\_SNAPSHOT\_AUTO\_NOT\_SUPPORTED = 160004 | 离屏节点截图不支持色彩空间或动态范围模式的isAuto参数设置为true。错误码的详细介绍请参见[截图错误码](errorcode-snapshot.md)。  **起始版本：** 23 |
| ARKUI\_ERROR\_CODE\_NON\_SCROLLABLE\_CONTAINER = 180001 | 非滚动类容器。错误码的详细介绍请参见[交互事件错误码](errorcode-event.md)。 |
| ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_NOT\_ENOUGH = 180002 | 存储区大小不足。错误码的详细介绍请参见[交互事件错误码](errorcode-event.md)。 |
| ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT = 180003 | 该事件不是克隆事件。错误码的详细介绍请参见[交互事件错误码](errorcode-event.md)。  **起始版本：** 15 |
| ARKUI\_ERROR\_CODE\_POST\_CLONED\_COMPONENT\_STATUS\_ABNORMAL = 180004 | 组件状态异常。错误码的详细介绍请参见[交互事件错误码](errorcode-event.md)。  **起始版本：** 15 |
| ARKUI\_ERROR\_CODE\_POST\_CLONED\_NO\_COMPONENT\_HIT\_TO\_RESPOND\_TO\_THE\_EVENT = 180005 | 未命中可响应事件的组件。错误码的详细介绍请参见[交互事件错误码](errorcode-event.md)。  **起始版本：** 15 |
| ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED = 180006 | 接口不支持此输入事件类型。  **起始版本：** 20 |
| ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING = 180101 | 无效的属性字符串。错误码的详细介绍请参见[属性字符串错误码](errorcode-styled-string.md)。  **起始版本：** 14 |
| ARKUI\_ERROR\_CODE\_UI\_CONTEXT\_INVALID = 190001 | 无效的UIContext对象。错误码的详细介绍请参见[UI上下文错误码](errorcode-uicontext.md)。  **起始版本：** 18 |
| ARKUI\_ERROR\_CODE\_CALLBACK\_INVALID = 190002 | 无效的回调函数。错误码的详细介绍请参见[UI上下文错误码](errorcode-uicontext.md)。  **起始版本：** 18 |
| ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED = 180102 | 不支持手势识别器类型。错误码的详细介绍请参见[交互事件错误码](errorcode-event.md)。  **起始版本：** 18 |
| ARKUI\_ERROR\_CODE\_DRAG\_DROP\_OPERATION\_NOT\_ALLOWED = 190004 | 当前阶段不允许该操作。错误码的详细介绍请参见[拖拽事件错误码](errorcode-drag-event.md)。  **起始版本：** 19 |

### ArkUI\_ScrollSource

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ScrollSource
```

**描述：**

定义滚动来源枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SCROLL\_SOURCE\_DRAG = 0 | 手指拖动。 |
| ARKUI\_SCROLL\_SOURCE\_FLING = 1 | 手指拖动后的惯性滚动。 |
| ARKUI\_SCROLL\_SOURCE\_EDGE\_EFFECT = 2 | 在过界时执行[EdgeEffect.Spring](ts-appendix-enums.md#edgeeffect)边缘特效。 |
| ARKUI\_SCROLL\_SOURCE\_OTHER\_USER\_INPUT = 3 | 除了拖动以外的其他用户输入，如鼠标滚轮、键盘事件等。 |
| ARKUI\_SCROLL\_SOURCE\_SCROLL\_BAR = 4 | 拖动滚动条。 |
| ARKUI\_SCROLL\_SOURCE\_SCROLL\_BAR\_FLING = 5 | 拖动滚动条后的惯性滚动。 |
| ARKUI\_SCROLL\_SOURCE\_SCROLLER = 6 | 滚动控制器引起的无动画的滚动。 |
| ARKUI\_SCROLL\_SOURCE\_ANIMATION = 7 | 滚动控制器引起的带动画的滚动。 |

### ArkUI\_SafeAreaType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_SafeAreaType
```

**描述：**

定义扩展安全区域的枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SAFE\_AREA\_TYPE\_SYSTEM = 1 | 系统默认非安全区域，包括状态栏、导航栏，该值为默认值。 |
| ARKUI\_SAFE\_AREA\_TYPE\_CUTOUT = 1 << 1 | 设备的非安全区域，例如刘海屏或挖孔屏区域。 |
| ARKUI\_SAFE\_AREA\_TYPE\_KEYBOARD = 1 << 2 | 软键盘区域。 |

### ArkUI\_SafeAreaEdge

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_SafeAreaEdge
```

**描述：**

定义扩展安全区域的方向的枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SAFE\_AREA\_EDGE\_TOP = 1 | 上方区域，该值为默认值。 |
| ARKUI\_SAFE\_AREA\_EDGE\_BOTTOM = 1 << 1 | 下方区域。 |
| ARKUI\_SAFE\_AREA\_EDGE\_START = 1 << 2 | 前部区域。 |
| ARKUI\_SAFE\_AREA\_EDGE\_END = 1 << 3 | 尾部区域。 |

### ArkUI\_FocusMove

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_FocusMove
```

**描述：**

定义焦点移动方向的枚举值。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_FOCUS\_MOVE\_FORWARD = 0 | 向前移动焦点。 |
| ARKUI\_FOCUS\_MOVE\_BACKWARD = 1 | 向后移动焦点。 |
| ARKUI\_FOCUS\_MOVE\_UP = 2 | 向上移动焦点。 |
| ARKUI\_FOCUS\_MOVE\_DOWN = 3 | 向下移动焦点。 |
| ARKUI\_FOCUS\_MOVE\_LEFT = 4 | 向左移动焦点。 |
| ARKUI\_FOCUS\_MOVE\_RIGHT = 5 | 向右移动焦点。 |

### ArkUI\_ListItemGroupArea

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ListItemGroupArea
```

**描述：**

定义[ListItemGroup](ts-container-listitemgroup.md)组件区域，默认值为ARKUI\_LIST\_ITEM\_GROUP\_AREA\_OUTSIDE。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LIST\_ITEM\_GROUP\_AREA\_OUTSIDE = 0 | ListItemGroup区域外。 |
| ARKUI\_LIST\_ITEM\_SWIPE\_AREA\_NONE = 1 | ListItemGroup没有[header](ts-container-listitemgroup.md#listitemgroupoptions对象说明)、[footer](ts-container-listitemgroup.md#listitemgroupoptions对象说明)和[ListItem](ts-container-listitem.md#listitem10)时的区域。 |
| ARKUI\_LIST\_ITEM\_SWIPE\_AREA\_ITEM = 2 | ListItemGroup的ListItem区域。 |
| ARKUI\_LIST\_ITEM\_SWIPE\_AREA\_HEADER = 3 | ListItemGroup的header区域。 |
| ARKUI\_LIST\_ITEM\_SWIPE\_AREA\_FOOTER = 4 | ListItemGroup的footer区域。 |

### ArkUI\_KeyboardAvoidMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_KeyboardAvoidMode
```

**描述：**

键盘避让模式。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_KEYBOARD\_AVOID\_MODE\_DEFAULT = 0 | 默认避让软键盘并在到达极限高度之后进行高度压缩。 |
| ARKUI\_KEYBOARD\_AVOID\_MODE\_NONE = 1 | 不避让键盘。 |

### ArkUI\_HoverModeAreaType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_HoverModeAreaType
```

**描述：**

悬停态显示区域。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_HOVER\_MODE\_AREA\_TYPE\_TOP = 0 | 上半屏。 |
| ARKUI\_HOVER\_MODE\_AREA\_TYPE\_BOTTOM = 1 | 下半屏。 |

### ArkUI\_ExpandMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ExpandMode
```

**描述：**

定义子节点展开模式枚举值。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_NOT\_EXPAND = 0 | 不展开。 |
| ARKUI\_EXPAND = 1 | 展开。 |
| ARKUI\_LAZY\_EXPAND = 2 | 懒展开，按需展开当前节点的子节点，节点展开条件可以参考[LazyForEach：数据懒加载](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)。 |

### ArkUI\_NavDestinationState

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_NavDestinationState
```

**描述：**

定义[NavDestination](ts-basic-components-navdestination.md)组件的状态。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_SHOW = 0 | NavDestination组件显示。 |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_HIDE = 1 | NavDestination组件隐藏。 |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_APPEAR = 2 | NavDestination从组件树上挂载。 |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_DISAPPEAR = 3 | NavDestination从组件树上卸载。 |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_WILL\_SHOW = 4 | NavDestination组件显示之前。 |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_WILL\_HIDE = 5 | NavDestination组件隐藏之前。 |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_WILL\_APPEAR = 6 | NavDestination挂载到组件树之前。 |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_WILL\_DISAPPEAR = 7 | NavDestination从组件树上卸载之前。 |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_BACK\_PRESS = 100 | NavDestination从组件返回。 |

### ArkUI\_RouterPageState

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_RouterPageState
```

**描述：**

定义[Router Page](arkts-apis-uicontext-router.md)（路由页面）的状态。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ROUTER\_PAGE\_STATE\_ABOUT\_TO\_APPEAR = 0 | Router Page即将创建。 |
| ARKUI\_ROUTER\_PAGE\_STATE\_ABOUT\_TO\_DISAPPEAR = 1 | Router Page即将销毁。 |
| ARKUI\_ROUTER\_PAGE\_STATE\_ON\_SHOW = 2 | Router Page显示。 |
| ARKUI\_ROUTER\_PAGE\_STATE\_ON\_HIDE = 3 | Router Page隐藏。 |
| ARKUI\_ROUTER\_PAGE\_STATE\_ON\_BACK\_PRESS = 4 | Router Page返回时。 |

### ArkUI\_UIState

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_UIState
```

**描述：**

组件的UI状态枚举，用于处理状态样式。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| UI\_STATE\_NORMAL = 0 | 正常状态。 |
| UI\_STATE\_PRESSED = 1 << 0 | 按压状态。 |
| UI\_STATE\_FOCUSED = 1 << 1 | 获焦状态。 |
| UI\_STATE\_DISABLED = 1 << 2 | 禁用状态。 |
| UI\_STATE\_SELECTED = 1 << 3 | 选中状态，此状态仅由某些特定类型的组件支持，分别是Checkbox、Radio、Toggle、List、Grid和MenuItem。 |

### ArkUI\_FocusWrapMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_FocusWrapMode
```

**描述：**

组件走焦换行规则。Grid、List组件默认值为ARKUI\_FOCUS\_WRAP\_MODE\_DEFAULT。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_FOCUS\_WRAP\_MODE\_DEFAULT = 0 | 默认规则，使用方向键走焦不换行。 |
| ARKUI\_FOCUS\_WRAP\_WITH\_ARROW = 1 | 使用方向键走焦自动换行。 |

### ArkUI\_ItemFillPolicy

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ItemFillPolicy
```

**描述：**

为不同响应式[断点规格](../harmonyos-guides/arkts-layout-development-grid-layout.md#栅格容器断点)指定列数。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ITEMFILLPOLICY\_NONE = -1 | 没有设置响应式断点规格。 |
| ARKUI\_ITEMFILLPOLICY\_DEFAULT = 0 | 针对List和Swiper组件：在组件宽度属于sm及更小的断点区间时显示1列，属于md断点区间时显示2列，属于lg及更大的断点区间时显示3列。  针对Grid和WaterFlow组件：在组件宽度属于sm及更小的断点区间时显示2列，属于md断点区间时显示3列，属于lg及更大的断点区间时显示5列。 |
| ARKUI\_ITEMFILLPOLICY\_SM1MD2LG3 = 1 | 在组件宽度属于sm及更小的断点区间时显示1列，属于md断点区间时显示2列，属于lg及更大的断点区间时显示3列。 |
| ARKUI\_ITEMFILLPOLICY\_SM2MD3LG5 = 2 | 在组件宽度属于sm及更小的断点区间时显示2列，属于md断点区间时显示3列，属于lg及更大的断点区间时显示5列。 |

### ArkUI\_ScrollSnapAnimationSpeed

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ScrollSnapAnimationSpeed
```

**描述：**

列表限位滚动动画速度。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SCROLL\_SNAP\_ANIMATION\_NORMAL = 0 | 限位滚动动画速度正常。 |
| ARKUI\_SCROLL\_SNAP\_ANIMATION\_SLOW = 1 | 限位滚动动画速度慢。 |

### ArkUI\_EdgeDirection

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_EdgeDirection
```

**描述：**

定义矩形边方向。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_EDGE\_DIRECTION\_ALL = 0 | 设置四个方向的内容。 |
| ARKUI\_EDGE\_DIRECTION\_LEFT = 1 << 0 | 设置左侧方向内容。 |
| ARKUI\_EDGE\_DIRECTION\_RIGHT = 1 << 1 | 设置右侧方向内容。 |
| ARKUI\_EDGE\_DIRECTION\_TOP = 1 << 2 | 设置上侧方向内容。 |
| ARKUI\_EDGE\_DIRECTION\_BOTTOM = 1 << 3 | 设置下侧方向内容。 |

### ArkUI\_CornerDirection

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_CornerDirection
```

**描述：**

定义角度方向。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_CORNER\_DIRECTION\_ALL = 0 | 设置四个角度方向的内容。 |
| ARKUI\_CORNER\_DIRECTION\_TOP\_LEFT = 1 << 0 | 设置左上侧方向内容。 |
| ARKUI\_CORNER\_DIRECTION\_TOP\_RIGHT = 1 << 1 | 设置右上侧方向内容。 |
| ARKUI\_CORNER\_DIRECTION\_BOTTOM\_LEFT = 1 << 2 | 设置左下侧方向内容。 |
| ARKUI\_CORNER\_DIRECTION\_BOTTOM\_RIGHT = 1 << 3 | 设置右下侧方向容。 |

### ArkUI\_LayoutPolicy

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_LayoutPolicy
```

**描述：**

定义布局策略枚举。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LAYOUTPOLICY\_MATCHPARENT = 0 | 组件自适应父组件布局。 |
| ARKUI\_LAYOUTPOLICY\_WRAPCONTENT = 1 | 组件自适应子组件（内容），且其大小受父组件内容区大小约束。 |
| ARKUI\_LAYOUTPOLICY\_FIXATIDEALSIZE = 2 | 组件自适应子组件（内容），且其大小不受父组件内容区大小约束。 |

### ArkUI\_PixelRoundCalcPolicy

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_PixelRoundCalcPolicy
```

**描述：**

定义像素取整计算策略枚举。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_PIXELROUNDCALCPOLICY\_NOFORCEROUND = 0 | 非取整计算。 |
| ARKUI\_PIXELROUNDCALCPOLICY\_FORCECEIL = 1 | 向上取整计算。 |
| ARKUI\_PIXELROUNDCALCPOLICY\_FORCEFLOOR = 2 | 向下取整计算。 |

### ArkUI\_GridItemAlignment

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_GridItemAlignment
```

**描述：**

[GridItem](ts-container-griditem.md)对齐方式枚举。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| GRID\_ITEM\_ALIGNMENT\_DEFAULT = 0 | Grid的默认对齐方式。 |
| GRID\_ITEM\_ALIGNMENT\_STRETCH = 1 | 以一行中的最高的GridItem作为其他GridItem的高度。 |

### ArkUI\_GridItemStyle

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_GridItemStyle
```

**描述：**

GridItem样式枚举。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| GRID\_ITEM\_STYLE\_NONE = 0 | 无样式。 |
| GRID\_ITEM\_STYLE\_PLAIN = 1 | 显示Hover、Press态样式。 |

### ArkUI\_HoverEffect

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_HoverEffect
```

**描述：**

组件被悬停时的效果。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_HOVER\_EFFECT\_AUTO = 0 | 默认效果。 |
| ARKUI\_HOVER\_EFFECT\_SCALE | 缩放效果。 |
| ARKUI\_HOVER\_EFFECT\_HIGHLIGHT | 高亮效果。 |
| ARKUI\_HOVER\_EFFECT\_NONE | 无效果。 |

### ArkUI\_FocusPriority

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_FocusPriority
```

**描述：**

应用程序内焦点管理的优先级级别。确定UI组件在交互期间接收焦点的顺序。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_FOCUS\_PRIORITY\_AUTO = 0 | 默认优先级。 |
| ARKUI\_FOCUS\_PRIORITY\_PRIOR = 2000 | 容器内优先获焦的优先级。 |
| ARKUI\_FOCUS\_PRIORITY\_PREVIOUS = 3000 | 上一次容器整体失焦时获焦节点的优先级。 |

### ArkUI\_MenuPolicy

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_MenuPolicy
```

**描述：**

菜单弹出策略。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_MENU\_POLICY\_DEFAULT = 0 | 根据底层默认逻辑确定是否弹出菜单。 |
| ARKUI\_MENU\_POLICY\_HIDE = 1 | 不弹出菜单。 |
| ARKUI\_MENU\_POLICY\_SHOW = 2 | 弹出菜单。 |

### ArkUI\_ResponseRegionSupportedTool

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ResponseRegionSupportedTool
```

**描述：**

定义支持响应区域设置的事件工具类型。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_RESPONSE\_REGIN\_SUPPORTED\_TOOL\_ALL = 0 | 所有输入工具类型。 |
| ARKUI\_RESPONSE\_REGIN\_SUPPORTED\_TOOL\_FINGER = 1 | 手指类型。 |
| ARKUI\_RESPONSE\_REGIN\_SUPPORTED\_TOOL\_PEN = 2 | 手写笔类型。 |
| ARKUI\_RESPONSE\_REGIN\_SUPPORTED\_TOOL\_MOUSE = 3 | 鼠标类型。 |

### ArkUI\_TextMenuItemId

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_TextMenuItemId
```

**描述**

文本菜单项id枚举。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_CUT = 0 | 裁剪。 |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_COPY = 1 | 复制。 |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_PASTE = 2 | 粘贴。 |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_SELECT\_ALL = 3 | 全选。 |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_COLLABORATION\_SERVICE = 4 | 互通服务。例如跨设备交互，包括跨设备的相机访问等能力。 |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_CAMERA\_INPUT = 5 | 拍摄输入。 |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_AI\_WRITER = 6 | AI帮写。该菜单项依赖大模型能力，否则不生效。 |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_TRANSLATE = 7 | 翻译。对选中的文本提供翻译服务。 |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_SEARCH = 8 | 搜索。对选中的文本提供搜索服务，拉起浏览器搜索选中文本内容。 |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_SHARE = 9 | 分享。对选中的文本提供分享服务，拉起分享窗口分享选中文本内容。 |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_URL = 10 | 打开链接。对选中的URL提供跳转服务，拉起浏览器搜索或者应用页面。 |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_EMAIL = 11 | 新建邮件。对选中的邮箱地址提供跳转服务，拉起邮箱应用。 |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_PHONE\_NUMBER = 12 | 呼叫。对选中的电话号码跳转服务，拉起电话拨号页面。 |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_ADDRESS = 13 | 导航前往。对选中的地址提供跳转服务，拉起地图应用。 |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_DATA\_TIME = 14 | 新建日程。对选中的日期和时间提供跳转服务，拉起新建日程页面。 |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_ASK\_AI = 15 | 问问AI。对选中的文本提供AI问询能力。 |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_APP\_RESERVED\_BEGIN = 10000 | 应用自定义菜单项起始id，除了系统内置的菜单项id，应用还可以自定义菜单项id。 |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_APP\_RESERVED\_END = 20000 | 应用自定义菜单项结束id，除了系统内置的菜单项id，应用还可以自定义菜单项id。 |

### ArkUI\_TextSpanType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_TextSpanType
```

**描述**

自定义文本选择菜单的文本识别类型枚举。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXT\_SPAN\_TYPE\_TEXT = 0 | 选中文本内容为文字类型。 |
| ARKUI\_TEXT\_SPAN\_TYPE\_IMAGE = 1 | 选中文本内容为图像类型。 |
| ARKUI\_TEXT\_SPAN\_TYPE\_MIXED = 2 | 选中文本内容为图文混合类型。 |
| ARKUI\_TEXT\_SPAN\_TYPE\_DEFAULT = 3 | 如果设置为此类型且设置了其他类型时，选中文本后会显示与选中文本内容类型对应的菜单。如果设置为此类型但其他类型未设置时，选中文本后会显示此类型对应的菜单。例如，同时设置了文本识别类型为ARKUI\_TEXT\_SPAN\_TYPE\_TEXT、ARKUI\_TEXT\_SPAN\_TYPE\_DEFAULT的两个菜单，此时选中文本内容为文字类型会触发ARKUI\_TEXT\_SPAN\_TYPE\_TEXT对应的菜单弹出，选中文本内容为图像类型则会触发ARKUI\_TEXT\_SPAN\_TYPE\_DEFAULT对应的菜单弹出。 |

### ArkUI\_TextResponseType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_TextResponseType
```

**描述**

自定义文本选择菜单的响应类型枚举。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXT\_RESPONSE\_TYPE\_RIGHT\_CLICK = 0 | 通过鼠标右键触发菜单弹出。 |
| ARKUI\_TEXT\_RESPONSE\_TYPE\_LONG\_PRESS = 1 | 通过长按触发菜单弹出。 |
| ARKUI\_TEXT\_RESPONSE\_TYPE\_SELECT = 2 | 通过鼠标选中触发菜单弹出。 |
| ARKUI\_TEXT\_RESPONSE\_TYPE\_DEFAULT = 3 | 如果设置为此类型且设置了其他类型时，触发其他类型的操作会显示对应类型的菜单。如果设置为此类型但其他类型未设置时，触发其他类型的操作会显示此类型对应的菜单。例如，同时设置了响应类型为ARKUI\_TEXT\_RESPONSE\_TYPE\_RIGHT\_CLICK、ARKUI\_TEXT\_RESPONSE\_TYPE\_DEFAULT的两个菜单，此时通过鼠标右键会触发ARKUI\_TEXT\_RESPONSE\_TYPE\_RIGHT\_CLICK对应的菜单弹出，长按则会触发ARKUI\_TEXT\_RESPONSE\_TYPE\_DEFAULT对应的菜单弹出。 |

### ArkUI\_MarqueeStartPolicy

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_MarqueeStartPolicy
```

**描述：**

定义跑马灯启动策略枚举。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_MARQUEESTARTPOLICY\_DEFAULT = 0 | 默认持续滚动。 |
| ARKUI\_MARQUEESTARTPOLICY\_ONFOCUS = 1 | 获焦以及鼠标悬浮时开始滚动。 |

### ArkUI\_MarqueeUpdatePolicy

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_MarqueeUpdatePolicy
```

**描述：**

定义跑马灯更新策略枚举。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_MARQUEEUPDATEPOLICY\_DEFAULT = 0 | 跑马灯组件属性更新后，从开始位置，运行跑马灯效果。 |
| ARKUI\_MARQUEEUPDATEPOLICY\_PRESERVEPOSITION = 1 | 跑马灯组件属性更新后，保持当前位置，运行跑马灯效果。 |

### ArkUI\_LayoutSafeAreaType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_LayoutSafeAreaType
```

**描述：**

定义扩展安全区域的枚举值。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LAYOUT\_SAFE\_AREA\_TYPE\_SYSTEM = 1 | 系统默认非安全区域，包括状态栏、导航栏。 |

### ArkUI\_LayoutSafeAreaEdge

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_LayoutSafeAreaEdge
```

**描述：**

定义扩展安全区域的方向的枚举值。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_TOP = 1 | 上方区域。 |
| ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_BOTTOM = 1 << 1 | 下方区域。 |
| ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_START = 1 << 2 | 前部区域。 |
| ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_END = 1 << 3 | 尾部区域。 |
| ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_VERTICAL = ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_TOP | ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_BOTTOM = 3 | 垂直区域。 |
| ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_HORIZONTAL = ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_START | ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_END = 12 | 水平区域。 |
| ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_ALL = ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_VERTICAL | ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_HORIZONTAL = 15 | 全部区域。 |

### ArkUI\_LocalizedAlignment

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_LocalizedAlignment
```

**描述：**

定义Stack容器中子组件的对齐规则。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LOCALIZED\_ALIGNMENT\_TOP\_START = 0 | 顶部起始。 |
| ARKUI\_LOCALIZED\_ALIGNMENT\_TOP = 1 | 顶部居中。 |
| ARKUI\_LOCALIZED\_ALIGNMENT\_TOP\_END = 2 | 顶部尾端。 |
| ARKUI\_LOCALIZED\_ALIGNMENT\_START = 3 | 起始端纵向居中。 |
| ARKUI\_LOCALIZED\_ALIGNMENT\_CENTER = 4 | 横向和纵向居中。 |
| ARKUI\_LOCALIZED\_ALIGNMENT\_END = 5 | 尾端纵向居中。 |
| ARKUI\_LOCALIZED\_ALIGNMENT\_BOTTOM\_START = 6 | 底部起始端。 |
| ARKUI\_LOCALIZED\_ALIGNMENT\_BOTTOM = 7 | 底部横向居中。 |
| ARKUI\_LOCALIZED\_ALIGNMENT\_BOTTOM\_END = 8 | 底部尾端。 |

### ArkUI\_RenderStrategy

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_RenderStrategy
```

**描述：**

定义组件绘制圆角的模式。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_RENDERSTRATEGY\_FAST = 0 | 在线绘制模式。 |
| ARKUI\_RENDERSTRATEGY\_OFFSCREEN = 1 | 离屏绘制模式。 |

### ArkUI\_PickerIndicatorType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_PickerIndicatorType
```

**描述**

选择器的选中指示器类型。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_PICKER\_INDICATOR\_BACKGROUND = 0 | 背景样式。 |
| ARKUI\_PICKER\_INDICATOR\_DIVIDER = 1 | 分割线样式。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_ArkUI\_LayoutConstraint\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_LayoutConstraint* OH_ArkUI_LayoutConstraint_Create()
```

**描述：**

创建布局约束。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_LayoutConstraint](capi-arkui-nativemodule-arkui-layoutconstraint.md)\* | 创建布局约束的指针。 |

### OH\_ArkUI\_LayoutConstraint\_Copy()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_LayoutConstraint* OH_ArkUI_LayoutConstraint_Copy(const ArkUI_LayoutConstraint* Constraint)
```

**描述：**

布局约束深拷贝。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_LayoutConstraint](capi-arkui-nativemodule-arkui-layoutconstraint.md)\* Constraint | 布局约束的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_LayoutConstraint](capi-arkui-nativemodule-arkui-layoutconstraint.md)\* | 新的布局约束指针。 |

### OH\_ArkUI\_LayoutConstraint\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void* OH_ArkUI_LayoutConstraint_Dispose(ArkUI_LayoutConstraint* Constraint)
```

**描述：**

销毁布局约束指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_LayoutConstraint](capi-arkui-nativemodule-arkui-layoutconstraint.md)\* Constraint | 布局约束的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| void\* | 空指针。 |

### OH\_ArkUI\_LayoutConstraint\_GetMaxWidth()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_LayoutConstraint_GetMaxWidth(const ArkUI_LayoutConstraint* Constraint)
```

**描述：**

通过布局约束获取最大宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_LayoutConstraint](capi-arkui-nativemodule-arkui-layoutconstraint.md)\* Constraint | 布局约束的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 最大宽度，单位为px。 |

### OH\_ArkUI\_LayoutConstraint\_GetMinWidth()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_LayoutConstraint_GetMinWidth(const ArkUI_LayoutConstraint* Constraint)
```

**描述：**

通过布局约束获取最小宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_LayoutConstraint](capi-arkui-nativemodule-arkui-layoutconstraint.md)\* Constraint | 布局约束的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 最小宽度，单位为px。 |

### OH\_ArkUI\_LayoutConstraint\_GetMaxHeight()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_LayoutConstraint_GetMaxHeight(const ArkUI_LayoutConstraint* Constraint)
```

**描述：**

通过布局约束获取最大高度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_LayoutConstraint](capi-arkui-nativemodule-arkui-layoutconstraint.md)\* Constraint | 布局约束的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 最大高度，单位为px。 |

### OH\_ArkUI\_LayoutConstraint\_GetMinHeight()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_LayoutConstraint_GetMinHeight(const ArkUI_LayoutConstraint* Constraint)
```

**描述：**

通过布局约束获取最小高度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_LayoutConstraint](capi-arkui-nativemodule-arkui-layoutconstraint.md)\* Constraint | 布局约束的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 最小高度，单位为px。 |

### OH\_ArkUI\_LayoutConstraint\_GetPercentReferenceWidth()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_LayoutConstraint_GetPercentReferenceWidth(const ArkUI_LayoutConstraint* Constraint)
```

**描述：**

通过布局约束获取宽度百分比基准。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_LayoutConstraint](capi-arkui-nativemodule-arkui-layoutconstraint.md)\* Constraint | 布局约束的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 宽度百分比基准。 |

### OH\_ArkUI\_LayoutConstraint\_GetPercentReferenceHeight()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_LayoutConstraint_GetPercentReferenceHeight(const ArkUI_LayoutConstraint* Constraint)
```

**描述：**

通过布局约束获取高度百分比基准。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_LayoutConstraint](capi-arkui-nativemodule-arkui-layoutconstraint.md)\* Constraint | 布局约束的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 高度百分比基准。 |

### OH\_ArkUI\_LayoutConstraint\_SetMaxWidth()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_LayoutConstraint_SetMaxWidth(ArkUI_LayoutConstraint* Constraint, int32_t value)
```

**描述：**

设置最大宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_LayoutConstraint](capi-arkui-nativemodule-arkui-layoutconstraint.md)\* Constraint | 布局约束的指针。 |
| int32\_t value | 最大宽度，单位为px，取值范围：[0, +∞)。 |

### OH\_ArkUI\_LayoutConstraint\_SetMinWidth()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_LayoutConstraint_SetMinWidth(ArkUI_LayoutConstraint* Constraint, int32_t value)
```

**描述：**

设置最小宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_LayoutConstraint](capi-arkui-nativemodule-arkui-layoutconstraint.md)\* Constraint | 布局约束的指针。 |
| int32\_t value | 最小宽度，单位为px，取值范围：[0, +∞)。 |

### OH\_ArkUI\_LayoutConstraint\_SetMaxHeight()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_LayoutConstraint_SetMaxHeight(ArkUI_LayoutConstraint* Constraint, int32_t value)
```

**描述：**

设置最大高度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_LayoutConstraint](capi-arkui-nativemodule-arkui-layoutconstraint.md)\* Constraint | 布局约束的指针。 |
| int32\_t value | 最大高度，单位为px，取值范围：[0, +∞)。 |

### OH\_ArkUI\_LayoutConstraint\_SetMinHeight()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_LayoutConstraint_SetMinHeight(ArkUI_LayoutConstraint* Constraint, int32_t value)
```

**描述：**

设置最小高度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_LayoutConstraint](capi-arkui-nativemodule-arkui-layoutconstraint.md)\* Constraint | 布局约束的指针。 |
| int32\_t value | 最小高度，单位为px，取值范围：[0, +∞)。 |

### OH\_ArkUI\_LayoutConstraint\_SetPercentReferenceWidth()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_LayoutConstraint_SetPercentReferenceWidth(ArkUI_LayoutConstraint* Constraint, int32_t value)
```

**描述：**

设置宽度百分比基准。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_LayoutConstraint](capi-arkui-nativemodule-arkui-layoutconstraint.md)\* Constraint | 布局约束的指针。 |
| int32\_t value | 宽度百分比基准，取值范围：[0, +∞)。 |

### OH\_ArkUI\_LayoutConstraint\_SetPercentReferenceHeight()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_LayoutConstraint_SetPercentReferenceHeight(ArkUI_LayoutConstraint* Constraint, int32_t value)
```

**描述：**

设置高度百分比基准。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_LayoutConstraint](capi-arkui-nativemodule-arkui-layoutconstraint.md)\* Constraint | 布局约束的指针。 |
| int32\_t value | 高度百分比基准，取值范围：[0, +∞)。 |

### OH\_ArkUI\_DrawContext\_GetCanvas()

PhonePC/2in1TabletTVWearable

```
1. void* OH_ArkUI_DrawContext_GetCanvas(ArkUI_DrawContext* context)
```

**描述：**

获取绘制canvas指针，可以转换为图形库的[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)指针进行绘制。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawContext](capi-arkui-nativemodule-arkui-drawcontext.md)\* context | 绘制上下文。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| void\* | 用于绘制的canvas指针。 |

### OH\_ArkUI\_DrawContext\_GetSize()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_IntSize OH_ArkUI_DrawContext_GetSize(ArkUI_DrawContext* context)
```

**描述：**

获取可绘制区域大小。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawContext](capi-arkui-nativemodule-arkui-drawcontext.md)\* context | 绘制上下文。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_IntSize](capi-arkui-nativemodule-arkui-intsize.md) | 可绘制区域大小。 |

### OH\_ArkUI\_WaterFlowSectionOption\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_WaterFlowSectionOption* OH_ArkUI_WaterFlowSectionOption_Create()
```

**描述：**

创建[FlowItem](ts-container-flowitem.md)分组配置信息。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_WaterFlowSectionOption](pi-arkui-nativemodule-arkui-waterflowsectionoption.md)\* | [FlowItem](ts-container-flowitem.md)分组配置信息。 |

### OH\_ArkUI\_WaterFlowSectionOption\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_WaterFlowSectionOption_Dispose(ArkUI_WaterFlowSectionOption* option)
```

**描述：**

销毁[FlowItem](ts-container-flowitem.md)分组配置信息指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_WaterFlowSectionOption](pi-arkui-nativemodule-arkui-waterflowsectionoption.md)\* option | [FlowItem](ts-container-flowitem.md)分组配置信息。 |

### OH\_ArkUI\_WaterFlowSectionOption\_SetSize()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_WaterFlowSectionOption_SetSize(ArkUI_WaterFlowSectionOption* option,int32_t size)
```

**描述：**

设置FlowItem分组配置信息数组长度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_WaterFlowSectionOption](pi-arkui-nativemodule-arkui-waterflowsectionoption.md)\* option | FlowItem分组配置信息。 |
| int32\_t size | 数组长度。 |

### OH\_ArkUI\_WaterFlowSectionOption\_GetSize()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_WaterFlowSectionOption_GetSize(ArkUI_WaterFlowSectionOption* option)
```

**描述：**

获取[FlowItem](ts-container-flowitem.md)分组配置信息数组长度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_WaterFlowSectionOption](pi-arkui-nativemodule-arkui-waterflowsectionoption.md)\* option | FlowItem分组配置信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 数组长度。如果返回-1，则返回失败。失败的原因可能是option参数异常，如空指针。 |

### OH\_ArkUI\_WaterFlowSectionOption\_SetItemCount()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_WaterFlowSectionOption_SetItemCount(ArkUI_WaterFlowSectionOption* option,int32_t index, int32_t itemCount)
```

**描述：**

设置分组中[FlowItem](ts-container-flowitem.md)数量。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_WaterFlowSectionOption](pi-arkui-nativemodule-arkui-waterflowsectionoption.md)\* option | [FlowItem](ts-container-flowitem.md)分组配置信息。 |
| int32\_t index | 分组配置信息数组索引值。 |
| int32\_t itemCount | 分组中[FlowItem](ts-container-flowitem.md)数量。 |

### OH\_ArkUI\_WaterFlowSectionOption\_GetItemCount()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_WaterFlowSectionOption_GetItemCount(ArkUI_WaterFlowSectionOption* option, int32_t index)
```

**描述：**

通过[FlowItem](ts-container-flowitem.md)分组配置信息获取对应索引下的[FlowItem](ts-container-flowitem.md)数量。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_WaterFlowSectionOption](pi-arkui-nativemodule-arkui-waterflowsectionoption.md)\* option | [FlowItem](ts-container-flowitem.md)分组配置信息。 |
| int32\_t index | 分组配置信息数组索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 分组中FlowItem数量。 |

### OH\_ArkUI\_WaterFlowSectionOption\_SetCrossCount()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_WaterFlowSectionOption_SetCrossCount(ArkUI_WaterFlowSectionOption* option,int32_t index, int32_t crossCount)
```

**描述：**

设置布局栅格，纵向布局时为列数，横向布局时为行数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_WaterFlowSectionOption](pi-arkui-nativemodule-arkui-waterflowsectionoption.md)\* option | FlowItem分组配置信息。 |
| int32\_t index | 分组配置信息数组索引值。 |
| int32\_t crossCount | 布局栅格数量。 |

### OH\_ArkUI\_WaterFlowSectionOption\_GetCrossCount()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_WaterFlowSectionOption_GetCrossCount(ArkUI_WaterFlowSectionOption* option, int32_t index)
```

**描述：**

通过[FlowItem](ts-container-flowitem.md)分组配置信息获取对应索引下的布局栅格数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_WaterFlowSectionOption](pi-arkui-nativemodule-arkui-waterflowsectionoption.md)\* option | FlowItem分组配置信息。 |
| int32\_t index | 分组配置信息数组索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 布局栅格数量。 |

### OH\_ArkUI\_WaterFlowSectionOption\_SetColumnGap()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_WaterFlowSectionOption_SetColumnGap(ArkUI_WaterFlowSectionOption* option,int32_t index, float columnGap)
```

**描述：**

设置分组的列间距。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_WaterFlowSectionOption](pi-arkui-nativemodule-arkui-waterflowsectionoption.md)\* option | FlowItem分组配置信息。 |
| int32\_t index | 分组配置信息数组索引值。 |
| float columnGap | 列间距。单位：vp。 |

### OH\_ArkUI\_WaterFlowSectionOption\_GetColumnGap()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_WaterFlowSectionOption_GetColumnGap(ArkUI_WaterFlowSectionOption* option, int32_t index)
```

**描述：**

通过FlowItem分组配置信息获取对应索引下的分组的列间距。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_WaterFlowSectionOption](pi-arkui-nativemodule-arkui-waterflowsectionoption.md)\* option | FlowItem分组配置信息。 |
| int32\_t index | 分组配置信息数组索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 列间距。单位：vp。 |

### OH\_ArkUI\_WaterFlowSectionOption\_SetRowGap()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_WaterFlowSectionOption_SetRowGap(ArkUI_WaterFlowSectionOption* option,int32_t index, float rowGap)
```

**描述：**

设置FlowItem分组的行间距。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_WaterFlowSectionOption](pi-arkui-nativemodule-arkui-waterflowsectionoption.md)\* option | FlowItem分组配置信息。 |
| int32\_t index | FlowItem分组配置信息数组索引值。 |
| float rowGap | 行间距。单位：vp。 |

### OH\_ArkUI\_WaterFlowSectionOption\_GetRowGap()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_WaterFlowSectionOption_GetRowGap(ArkUI_WaterFlowSectionOption* option, int32_t index)
```

**描述：**

通过[FlowItem](ts-container-flowitem.md)分组配置信息获取对应索引下的分组的行间距。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_WaterFlowSectionOption](pi-arkui-nativemodule-arkui-waterflowsectionoption.md)\* option | [FlowItem](ts-container-flowitem.md)分组配置信息。 |
| int32\_t index | 分组配置信息数组索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 行间距。单位：vp。 |

### OH\_ArkUI\_WaterFlowSectionOption\_SetMargin()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_WaterFlowSectionOption_SetMargin(ArkUI_WaterFlowSectionOption* option, int32_t index,float marginTop, float marginRight, float marginBottom, float marginLeft)
```

**描述：**

设置分组的外边距。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_WaterFlowSectionOption](pi-arkui-nativemodule-arkui-waterflowsectionoption.md)\* option | [FlowItem](ts-container-flowitem.md)分组配置信息。 |
| int32\_t index | 分组配置信息数组索引值。 |
| float marginTop | [FlowItem](ts-container-flowitem.md)上外边距。 |
| float marginRight | [FlowItem](ts-container-flowitem.md)右外边距。 |
| float marginBottom | [FlowItem](ts-container-flowitem.md)下外边距。 |
| float marginLeft | [FlowItem](ts-container-flowitem.md)左外边距。 |

### OH\_ArkUI\_WaterFlowSectionOption\_GetMargin()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_Margin OH_ArkUI_WaterFlowSectionOption_GetMargin(ArkUI_WaterFlowSectionOption* option, int32_t index)
```

**描述：**

通过[FlowItem](ts-container-flowitem.md)分组配置信息获取对应索引下的分组的外边距。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_WaterFlowSectionOption](pi-arkui-nativemodule-arkui-waterflowsectionoption.md)\* option | [FlowItem](ts-container-flowitem.md)分组配置信息。 |
| int32\_t index | 分组配置信息数组索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_Margin](capi-arkui-nativemodule-arkui-margin.md) | 外边距。单位：vp。 |

### OH\_ArkUI\_WaterFlowSectionOption\_RegisterGetItemMainSizeCallbackByIndex()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_WaterFlowSectionOption_RegisterGetItemMainSizeCallbackByIndex(ArkUI_WaterFlowSectionOption* option,int32_t index, float(*callback)(int32_t itemIndex))
```

**描述：**

通过[FlowItem](ts-container-flowitem.md)分组配置信息根据itemIndex获取指定FlowItem的主轴大小。如需在回调中使用自定义数据，可使用[OH\_ArkUI\_WaterFlowSectionOption\_RegisterGetItemMainSizeCallbackByIndexWithUserData](capi-native-type-h.md#oh_arkui_waterflowsectionoption_registergetitemmainsizecallbackbyindexwithuserdata)。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_WaterFlowSectionOption](pi-arkui-nativemodule-arkui-waterflowsectionoption.md)\* option | [FlowItem](ts-container-flowitem.md)分组配置信息。 |
| int32\_t index | 分组配置信息数组索引值。 |
| callback | 根据index获取指定Item的主轴大小。itemIndex：[FlowItem](ts-container-flowitem.md)索引值。 |

### OH\_ArkUI\_WaterFlowSectionOption\_RegisterGetItemMainSizeCallbackByIndexWithUserData()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_WaterFlowSectionOption_RegisterGetItemMainSizeCallbackByIndexWithUserData(ArkUI_WaterFlowSectionOption* option, int32_t index, void* userData,float (*callback)(int32_t itemIndex, void* userData))
```

**描述：**

通过[FlowItem](ts-container-flowitem.md)分组配置信息根据itemIndex获取指定Item的主轴大小。与[OH\_ArkUI\_WaterFlowSectionOption\_RegisterGetItemMainSizeCallbackByIndex](capi-native-type-h.md#oh_arkui_waterflowsectionoption_registergetitemmainsizecallbackbyindex)的区别在于，该接口支持传入自定义数据userData，并在回调函数中接收该数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_WaterFlowSectionOption](pi-arkui-nativemodule-arkui-waterflowsectionoption.md)\* option | [FlowItem](ts-container-flowitem.md)分组配置信息。 |
| int32\_t index | 分组配置信息数组索引值。 |
| void\* userData | 用户自定义数据指针，将在回调函数中回传给用户。 |
| callback | 根据index获取指定Item的主轴大小。itemIndex：[FlowItem](ts-container-flowitem.md)索引值；userData：用户自定义数据。 |

### OH\_ArkUI\_GuidelineOption\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_GuidelineOption* OH_ArkUI_GuidelineOption_Create(int32_t size)
```

**描述：**

创建[RelativeContainer](ts-container-relativecontainer.md)容器内的辅助线信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t size | 辅助线数量，取值范围：[0, +∞)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md)\* | 辅助线信息。 |

### OH\_ArkUI\_GuidelineOption\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_GuidelineOption_Dispose(ArkUI_GuidelineOption* guideline)
```

**描述：**

销毁辅助线信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md)\* guideline | 辅助线信息。 |

### OH\_ArkUI\_GuidelineOption\_SetId()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_GuidelineOption_SetId(ArkUI_GuidelineOption* guideline, const char* value, int32_t index)
```

**描述：**

设置辅助线的Id。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md)\* guideline | 辅助线信息。 |
| const char\* value | id，必须是唯一的并且不可与容器内组件重名。 |
| int32\_t index | 辅助线索引值。 |

### OH\_ArkUI\_GuidelineOption\_SetDirection()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_GuidelineOption_SetDirection(ArkUI_GuidelineOption* guideline, ArkUI_Axis value, int32_t index)
```

**描述：**

设置辅助线的方向。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md)\* guideline | 辅助线信息。 |
| [ArkUI\_Axis](capi-native-type-h.md#arkui_axis) value | 方向。 |
| int32\_t index | 辅助线索引值。 |

### OH\_ArkUI\_GuidelineOption\_SetPositionStart()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_GuidelineOption_SetPositionStart(ArkUI_GuidelineOption* guideline, float value, int32_t index)
```

**描述：**

设置距离容器左侧或者顶部的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md)\* guideline | 辅助线信息。 |
| float value | 距离容器左侧或者顶部的距离，单位vp。 |
| int32\_t index | 辅助线索引值。 |

### OH\_ArkUI\_GuidelineOption\_SetPositionEnd()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_GuidelineOption_SetPositionEnd(ArkUI_GuidelineOption* guideline, float value, int32_t index)
```

**描述：**

设置距离容器右侧或者底部的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md)\* guideline | 辅助线信息。 |
| float value | 距离容器右侧或者底部的距离，单位vp。 |
| int32\_t index | 辅助线索引值。 |

### OH\_ArkUI\_GuidelineOption\_GetId()

PhonePC/2in1TabletTVWearable

```
1. const char* OH_ArkUI_GuidelineOption_GetId(ArkUI_GuidelineOption* guideline, int32_t index)
```

**描述：**

获取辅助线的Id。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md)\* guideline | 辅助线信息。 |
| int32\_t index | 辅助线索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | Id。 |

### OH\_ArkUI\_GuidelineOption\_GetDirection()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_Axis OH_ArkUI_GuidelineOption_GetDirection(ArkUI_GuidelineOption* guideline, int32_t index)
```

**描述：**

获取辅助线的方向。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md)\* guideline | 辅助线信息。 |
| int32\_t index | 辅助线索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_Axis](capi-native-type-h.md#arkui_axis) | 方向。 |

### OH\_ArkUI\_GuidelineOption\_GetPositionStart()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_GuidelineOption_GetPositionStart(ArkUI_GuidelineOption* guideline, int32_t index)
```

**描述：**

获取辅助线距离容器左侧或者顶部的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md)\* guideline | 辅助线信息。 |
| int32\_t index | 辅助线索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 辅助线距离容器左侧或者顶部的距离。单位为vp。 |

### OH\_ArkUI\_GuidelineOption\_GetPositionEnd()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_GuidelineOption_GetPositionEnd(ArkUI_GuidelineOption* guideline, int32_t index)
```

**描述：**

获取辅助线距离容器右侧或者底部的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md)\* guideline | 辅助线信息。 |
| int32\_t index | 辅助线索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 辅助线距离容器右侧或者底部的距离。单位为vp。 |

### OH\_ArkUI\_BarrierOption\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_BarrierOption* OH_ArkUI_BarrierOption_Create(int32_t size)
```

**描述：**

创建RelativeContainer容器内的屏障信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t size | 屏障数量，取值范围：[0, +∞)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_BarrierOption](capi-arkui-nativemodule-arkui-barrieroption.md)\* | 屏障信息。 |

### OH\_ArkUI\_BarrierOption\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_BarrierOption_Dispose(ArkUI_BarrierOption* barrierStyle)
```

**描述：**

销毁屏障信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_BarrierOption](capi-arkui-nativemodule-arkui-barrieroption.md)\* barrierStyle | 屏障信息。 |

### OH\_ArkUI\_BarrierOption\_SetId()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_BarrierOption_SetId(ArkUI_BarrierOption* barrierStyle, const char* value, int32_t index)
```

**描述：**

设置屏障的Id。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_BarrierOption](capi-arkui-nativemodule-arkui-barrieroption.md)\* barrierStyle | 屏障信息。 |
| const char\* value | id，必须是唯一的并且不可与容器内组件重名。 |
| int32\_t index | 屏障索引值。 |

### OH\_ArkUI\_BarrierOption\_SetDirection()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_BarrierOption_SetDirection(ArkUI_BarrierOption* barrierStyle, ArkUI_BarrierDirection value, int32_t index)
```

**描述：**

设置屏障的方向。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_BarrierOption](capi-arkui-nativemodule-arkui-barrieroption.md)\* barrierStyle | 屏障信息。 |
| [ArkUI\_BarrierDirection](capi-native-type-h.md#arkui_barrierdirection) value | 方向。 |
| int32\_t index | 屏障索引值。 |

### OH\_ArkUI\_BarrierOption\_SetReferencedId()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_BarrierOption_SetReferencedId(ArkUI_BarrierOption* barrierStyle, const char* value, int32_t index)
```

**描述：**

设置屏障的依赖的组件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_BarrierOption](capi-arkui-nativemodule-arkui-barrieroption.md)\* barrierStyle | 屏障信息。 |
| const char\* value | 依赖的组件的Id。 |
| int32\_t index | 屏障索引值。 |

### OH\_ArkUI\_BarrierOption\_GetId()

PhonePC/2in1TabletTVWearable

```
1. const char* OH_ArkUI_BarrierOption_GetId(ArkUI_BarrierOption* barrierStyle, int32_t index)
```

**描述：**

获取屏障的Id。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_BarrierOption](capi-arkui-nativemodule-arkui-barrieroption.md)\* barrierStyle | 屏障信息。 |
| int32\_t index | 屏障索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 屏障的Id。 |

### OH\_ArkUI\_BarrierOption\_GetDirection()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_BarrierDirection OH_ArkUI_BarrierOption_GetDirection(ArkUI_BarrierOption* barrierStyle, int32_t index)
```

**描述：**

获取屏障的方向。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_BarrierOption](capi-arkui-nativemodule-arkui-barrieroption.md)\* barrierStyle | 屏障信息。 |
| int32\_t index | 屏障索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_BarrierDirection](capi-native-type-h.md#arkui_barrierdirection) | 屏障的方向。 |

### OH\_ArkUI\_BarrierOption\_GetReferencedId()

PhonePC/2in1TabletTVWearable

```
1. const char* OH_ArkUI_BarrierOption_GetReferencedId(ArkUI_BarrierOption* barrierStyle, int32_t index , int32_t referencedIndex)
```

**描述：**

获取屏障的依赖的组件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_BarrierOption](capi-arkui-nativemodule-arkui-barrieroption.md)\* barrierStyle | 屏障信息。 |
| int32\_t index | 屏障索引值。 |
| int32\_t referencedIndex | 依赖的组件Id索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 屏障的依赖的组件。 |

### OH\_ArkUI\_BarrierOption\_GetReferencedIdSize()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_BarrierOption_GetReferencedIdSize(ArkUI_BarrierOption* barrierStyle, int32_t index)
```

**描述：**

获取屏障的依赖的组件的个数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_BarrierOption](capi-arkui-nativemodule-arkui-barrieroption.md)\* barrierStyle | 屏障信息。 |
| int32\_t index | 屏障索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 屏障的依赖的组件的个数。 |

### OH\_ArkUI\_AlignmentRuleOption\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_AlignmentRuleOption* OH_ArkUI_AlignmentRuleOption_Create()
```

**描述：**

创建相对容器中子组件的对齐规则信息。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* | 对齐规则信息。 |

### OH\_ArkUI\_AlignmentRuleOption\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AlignmentRuleOption_Dispose(ArkUI_AlignmentRuleOption* option)
```

**描述：**

销毁相对容器中子组件的对齐规则信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

### OH\_ArkUI\_AlignmentRuleOption\_SetStart()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AlignmentRuleOption_SetStart(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_HorizontalAlignment alignment)
```

**描述：**

设置相对布局的左对齐方式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |
| const char\* id | 锚点的组件的id值。 |
| [ArkUI\_HorizontalAlignment](capi-native-type-h.md#arkui_horizontalalignment) alignment | 相对于锚点组件的对齐方式。 |

### OH\_ArkUI\_AlignmentRuleOption\_SetEnd()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AlignmentRuleOption_SetEnd(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_HorizontalAlignment alignment)
```

**描述：**

设置相对布局的右对齐方式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |
| const char\* id | 锚点的组件的id值。 |
| [ArkUI\_HorizontalAlignment](capi-native-type-h.md#arkui_horizontalalignment) alignment | 相对于锚点组件的对齐方式。 |

### OH\_ArkUI\_AlignmentRuleOption\_SetCenterHorizontal()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AlignmentRuleOption_SetCenterHorizontal(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_HorizontalAlignment alignment)
```

**描述：**

设置相对布局的横向居中对齐方式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |
| const char\* id | 锚点的组件的id值。 |
| [ArkUI\_HorizontalAlignment](capi-native-type-h.md#arkui_horizontalalignment) alignment | 相对于锚点组件的对齐方式 |

### OH\_ArkUI\_AlignmentRuleOption\_SetTop()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AlignmentRuleOption_SetTop(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_VerticalAlignment alignment)
```

**描述：**

设置相对布局的顶部对齐的方式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |
| const char\* id | 锚点的组件的id值。 |
| [ArkUI\_VerticalAlignment](capi-native-type-h.md#arkui_verticalalignment) alignment | 相对于锚点组件的对齐方式 |

### OH\_ArkUI\_AlignmentRuleOption\_SetBottom()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AlignmentRuleOption_SetBottom(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_VerticalAlignment alignment)
```

**描述：**

设置相对布局的底部对齐的方式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |
| const char\* id | 锚点的组件的id值。 |
| [ArkUI\_VerticalAlignment](capi-native-type-h.md#arkui_verticalalignment) alignment | 相对于锚点组件的对齐方式 |

### OH\_ArkUI\_AlignmentRuleOption\_SetCenterVertical()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AlignmentRuleOption_SetCenterVertical(ArkUI_AlignmentRuleOption* option, const char* id, ArkUI_VerticalAlignment alignment)
```

**描述：**

设置相对布局的纵向居中对齐方式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |
| const char\* id | 锚点的组件的id值。 |
| [ArkUI\_VerticalAlignment](capi-native-type-h.md#arkui_verticalalignment) alignment | 相对于锚点组件的对齐方式。 |

### OH\_ArkUI\_AlignmentRuleOption\_SetBiasHorizontal()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AlignmentRuleOption_SetBiasHorizontal(ArkUI_AlignmentRuleOption* option, float horizontal)
```

**描述：**

设置组件在锚点约束下的水平方向上偏移参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |
| float horizontal | 水平方向上的bias值。 |

### OH\_ArkUI\_AlignmentRuleOption\_SetBiasVertical()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AlignmentRuleOption_SetBiasVertical(ArkUI_AlignmentRuleOption* option, float vertical)
```

**描述：**

设置组件在锚点约束下的垂直方向上偏移参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |
| float vertical | 垂直方向上的bias值。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetStartId()

PhonePC/2in1TabletTVWearable

```
1. const char* OH_ArkUI_AlignmentRuleOption_GetStartId(ArkUI_AlignmentRuleOption* option)
```

**描述：**

获取左对齐锚点组件的Id。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 左对齐锚点组件的Id。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetStartAlignment()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_HorizontalAlignment OH_ArkUI_AlignmentRuleOption_GetStartAlignment(ArkUI_AlignmentRuleOption* option)
```

**描述：**

获取左对齐方式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_HorizontalAlignment](capi-native-type-h.md#arkui_horizontalalignment) | 参数的对齐方式。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetEndId()

PhonePC/2in1TabletTVWearable

```
1. const char* OH_ArkUI_AlignmentRuleOption_GetEndId(ArkUI_AlignmentRuleOption* option)
```

**描述：**

获取右对齐锚点组件的Id。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 右对齐锚点组件的Id。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetEndAlignment()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_HorizontalAlignment OH_ArkUI_AlignmentRuleOption_GetEndAlignment(ArkUI_AlignmentRuleOption* option)
```

**描述：**

获取右对齐方式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_HorizontalAlignment](capi-native-type-h.md#arkui_horizontalalignment) | 右对齐方式。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetCenterIdHorizontal()

PhonePC/2in1TabletTVWearable

```
1. const char* OH_ArkUI_AlignmentRuleOption_GetCenterIdHorizontal(ArkUI_AlignmentRuleOption* option)
```

**描述：**

获取横向居中对齐锚点组件的Id。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 横向居中对齐锚点组件的Id。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetCenterAlignmentHorizontal()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_HorizontalAlignment OH_ArkUI_AlignmentRuleOption_GetCenterAlignmentHorizontal(ArkUI_AlignmentRuleOption* option)
```

**描述：**

获取横向居中对齐方式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_HorizontalAlignment](capi-native-type-h.md#arkui_horizontalalignment) | 横向居中对齐方式。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetTopId()

PhonePC/2in1TabletTVWearable

```
1. const char* OH_ArkUI_AlignmentRuleOption_GetTopId(ArkUI_AlignmentRuleOption* option)
```

**描述：**

获取顶部对齐锚点组件的Id。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 顶部对齐锚点组件的Id。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetTopAlignment()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_VerticalAlignment OH_ArkUI_AlignmentRuleOption_GetTopAlignment(ArkUI_AlignmentRuleOption* option)
```

**描述：**

获取顶部对齐的方式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_VerticalAlignment](capi-native-type-h.md#arkui_verticalalignment) | 顶部对齐的方式。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetBottomId()

PhonePC/2in1TabletTVWearable

```
1. const char* OH_ArkUI_AlignmentRuleOption_GetBottomId(ArkUI_AlignmentRuleOption* option)
```

**描述：**

获取底部对齐锚点组件的Id。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 底部对齐锚点组件的Id。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetBottomAlignment()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_VerticalAlignment OH_ArkUI_AlignmentRuleOption_GetBottomAlignment(ArkUI_AlignmentRuleOption* option)
```

**描述：**

获取底部对齐的方式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_VerticalAlignment](capi-native-type-h.md#arkui_verticalalignment) | 底部对齐的方式。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetCenterIdVertical()

PhonePC/2in1TabletTVWearable

```
1. const char* OH_ArkUI_AlignmentRuleOption_GetCenterIdVertical(ArkUI_AlignmentRuleOption* option)
```

**描述：**

获取纵向居中对齐锚点组件的Id。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 纵向居中对齐锚点组件的Id。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetCenterAlignmentVertical()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_VerticalAlignment OH_ArkUI_AlignmentRuleOption_GetCenterAlignmentVertical(ArkUI_AlignmentRuleOption* option)
```

**描述：**

获取纵向居中对齐方式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_VerticalAlignment](capi-native-type-h.md#arkui_verticalalignment) | 纵向居中对齐方式。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetBiasHorizontal()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_AlignmentRuleOption_GetBiasHorizontal(ArkUI_AlignmentRuleOption* option)
```

**描述：**

获取水平方向上的bias值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 水平方向上的bias值。 |

### OH\_ArkUI\_AlignmentRuleOption\_GetBiasVertical()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_AlignmentRuleOption_GetBiasVertical(ArkUI_AlignmentRuleOption* option)
```

**描述：**

获取垂直方向上的bias值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)\* option | 相对容器中子组件的对齐规则信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 垂直方向上的bias值。 |

### OH\_ArkUI\_SwiperIndicator\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_SwiperIndicator* OH_ArkUI_SwiperIndicator_Create(ArkUI_SwiperIndicatorType type)
```

**描述：**

创建Swiper组件的导航指示器。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicatorType](capi-native-type-h.md#arkui_swiperindicatortype) type | 导航指示器的类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* | 导航指示器对象指针。 |

### OH\_ArkUI\_SwiperIndicator\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperIndicator_Dispose(ArkUI_SwiperIndicator* indicator)
```

**描述：**

销毁Swiper组件的导航指示器指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

### OH\_ArkUI\_SwiperIndicator\_SetStartPosition()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperIndicator_SetStartPosition(ArkUI_SwiperIndicator* indicator, float value)
```

**描述：**

设置导航点距离Swiper组件左边的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| float value | 导航点距离Swiper组件左边的距离。默认值：0，单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_GetStartPosition()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_SwiperIndicator_GetStartPosition(ArkUI_SwiperIndicator* indicator)
```

**描述：**

获取导航点距离Swiper组件左边的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 导航点距离Swiper组件左边的距离。单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_SetTopPosition()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperIndicator_SetTopPosition(ArkUI_SwiperIndicator* indicator, float value)
```

**描述：**

设置导航点距离Swiper组件顶部的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| float value | 导航点距离Swiper组件顶部的距离。默认值：0，单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_GetTopPosition()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_SwiperIndicator_GetTopPosition(ArkUI_SwiperIndicator* indicator)
```

**描述：**

获取导航点距离Swiper组件顶部的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 导航点距离Swiper组件顶部的距离。单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_SetEndPosition()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperIndicator_SetEndPosition(ArkUI_SwiperIndicator* indicator, float value)
```

**描述：**

设置导航点距离Swiper组件右边的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| float value | 导航点距离Swiper组件右边的距离。默认值：0，单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_GetEndPosition()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_SwiperIndicator_GetEndPosition(ArkUI_SwiperIndicator* indicator)
```

**描述：**

获取导航点距离Swiper组件右边的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 导航点距离Swiper组件右边的距离。单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_SetBottomPosition()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperIndicator_SetBottomPosition(ArkUI_SwiperIndicator* indicator, float value)
```

**描述：**

设置导航点距离Swiper组件底部的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| float value | 导航点距离Swiper组件底部的距离。默认值：0，单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_GetBottomPosition()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_SwiperIndicator_GetBottomPosition(ArkUI_SwiperIndicator* indicator)
```

**描述：**

获取导航点距离Swiper组件底部的距离。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 导航点距离Swiper组件底部的距离。单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_SetIgnoreSizeOfBottom()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperIndicator_SetIgnoreSizeOfBottom(ArkUI_SwiperIndicator* indicator, int32_t ignoreSize)
```

**描述：**

设置OH\_ArkUI\_SwiperIndicator\_SetBottomPosition是否忽略导航点大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| int32\_t ignoreSize | 是否忽略导航点大小。1表示忽略导航点大小，0表示不忽略，默认值0。 |

### OH\_ArkUI\_SwiperIndicator\_GetIgnoreSizeOfBottom()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_SwiperIndicator_GetIgnoreSizeOfBottom(ArkUI_SwiperIndicator* indicator)
```

**描述：**

获取OH\_ArkUI\_SwiperIndicator\_SetBottomPosition是否忽略导航点大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 是否忽略导航点大小。 |

### OH\_ArkUI\_SwiperIndicator\_SetItemWidth()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperIndicator_SetItemWidth(ArkUI_SwiperIndicator* indicator, float value)
```

**描述：**

设置Swiper组件圆点导航指示器的宽。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| float value | 圆点导航指示器的宽。默认值：12，单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_GetItemWidth()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_SwiperIndicator_GetItemWidth(ArkUI_SwiperIndicator* indicator)
```

**描述：**

获取Swiper组件圆点导航指示器的宽。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 圆点导航指示器的宽。单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_SetItemHeight()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperIndicator_SetItemHeight(ArkUI_SwiperIndicator* indicator, float value)
```

**描述：**

设置Swiper组件圆点导航指示器的高。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| float value | 圆点导航指示器的高。默认值：6，单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_GetItemHeight()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_SwiperIndicator_GetItemHeight(ArkUI_SwiperIndicator* indicator)
```

**描述：**

获取Swiper组件圆点导航指示器的高。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 圆点导航指示器的高。单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_SetSelectedItemWidth()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperIndicator_SetSelectedItemWidth(ArkUI_SwiperIndicator* indicator, float value)
```

**描述：**

设置被选中的Swiper组件圆点导航指示器的宽。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| float value | 圆点导航指示器的宽。默认值：12，单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_GetSelectedItemWidth()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_SwiperIndicator_GetSelectedItemWidth(ArkUI_SwiperIndicator* indicator)
```

**描述：**

获取被选中Swiper组件圆点导航指示器的宽。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 圆点导航指示器的宽。单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_SetSelectedItemHeight()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperIndicator_SetSelectedItemHeight(ArkUI_SwiperIndicator* indicator, float value)
```

**描述：**

设置被选中的Swiper组件圆点导航指示器的高。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| float value | 圆点导航指示器的高。默认值：6，单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_GetSelectedItemHeight()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_SwiperIndicator_GetSelectedItemHeight(ArkUI_SwiperIndicator* indicator)
```

**描述：**

获取被选中Swiper组件圆点导航指示器的高。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 圆点导航指示器的高。单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_SetMask()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperIndicator_SetMask(ArkUI_SwiperIndicator* indicator, int32_t mask)
```

**描述：**

设置是否显示Swiper组件圆点导航指示器的蒙版样式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| int32\_t mask | 是否显示蒙版样式，1表示显示，0表示不显示。  默认值：0 |

### OH\_ArkUI\_SwiperIndicator\_GetMask()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_SwiperIndicator_GetMask(ArkUI_SwiperIndicator* indicator)
```

**描述：**

获取是否显示Swiper组件圆点导航指示器的蒙版样式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回1表示显示圆点导航指示器的蒙版样式，返回0表示不显示。 |

### OH\_ArkUI\_SwiperIndicator\_SetColor()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperIndicator_SetColor(ArkUI_SwiperIndicator* indicator, uint32_t color)
```

**描述：**

设置Swiper组件圆点导航指示器的颜色。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| uint32\_t color | 颜色类型，0xargb格式，形如 0xFFFF0000 表示红色。  默认值：'#1A182431'，浅灰色。 |

### OH\_ArkUI\_SwiperIndicator\_GetColor()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_ArkUI_SwiperIndicator_GetColor(ArkUI_SwiperIndicator* indicator)
```

**描述：**

获取Swiper组件圆点导航指示器的颜色。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 颜色类型，0xargb格式，形如 0xFFFF0000 表示红色。 |

### OH\_ArkUI\_SwiperIndicator\_SetSelectedColor()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperIndicator_SetSelectedColor(ArkUI_SwiperIndicator* indicator, uint32_t selectedColor)
```

**描述：**

设置被选中Swiper组件圆点导航指示器的颜色。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| uint32\_t selectedColor | 颜色类型，0xargb格式，形如0xFFFF0000表示红色。  默认值：'#007DFF'，蓝色。 |

### OH\_ArkUI\_SwiperIndicator\_GetSelectedColor()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_ArkUI_SwiperIndicator_GetSelectedColor(ArkUI_SwiperIndicator* indicator)
```

**描述：**

获取被选中Swiper组件圆点导航指示器的颜色。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 颜色类型，0xargb格式，形如 0xFFFF0000 表示红色。 |

### OH\_ArkUI\_SwiperIndicator\_SetMaxDisplayCount()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_SwiperIndicator_SetMaxDisplayCount(ArkUI_SwiperIndicator* indicator, int32_t maxDisplayCount)
```

**描述：**

设置圆点导航点指示器样式下，导航点显示个数的最大值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| int32\_t maxDisplayCount | 导航点显示个数最大值，有效取值范围[6, 9]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 如果maxDisplayCount设置范围错误, 返回错误码。 |

### OH\_ArkUI\_SwiperIndicator\_GetMaxDisplayCount()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_SwiperIndicator_GetMaxDisplayCount(ArkUI_SwiperIndicator* indicator)
```

**描述：**

获取圆点导航点指示器样式下，导航点显示个数的最大值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 导航点显示个数最大值，有效取值范围[6, 9]。 |

### OH\_ArkUI\_SwiperDigitIndicator\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_SwiperDigitIndicator *OH_ArkUI_SwiperDigitIndicator_Create()
```

**描述：**

创建Swiper组件的数字导航指示器。

**起始版本：** 19

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md) \* | 数字导航指示器对象指针。 |

### OH\_ArkUI\_SwiperDigitIndicator\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperDigitIndicator_Destroy(ArkUI_SwiperDigitIndicator* indicator)
```

**描述：**

销毁Swiper组件的数字导航指示器指针。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |

### OH\_ArkUI\_SwiperDigitIndicator\_SetStartPosition()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperDigitIndicator_SetStartPosition(ArkUI_SwiperDigitIndicator* indicator, float value)
```

**描述：**

设置数字导航指示器距离Swiper组件左边的距离。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |
| float value | 数字导航指示器距离Swiper组件左边的距离，在从左至右显示的语言模式下，设置距离Swiper组件左边的距离；在从右至左显示的语言模式下，设置距离Swiper组件右边的距离。  默认值：0  单位：vp |

### OH\_ArkUI\_SwiperDigitIndicator\_GetStartPosition()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_SwiperDigitIndicator_GetStartPosition(ArkUI_SwiperDigitIndicator* indicator)
```

**描述：**

获取数字导航指示器距离Swiper组件左边的距离。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 数字导航指示器距离Swiper组件左边的距离，在从左至右显示的语言模式下，返回距离Swiper组件左边的距离；在从右至左显示的语言模式下，返回距离Swiper组件右边的距离。  单位：vp |

### OH\_ArkUI\_SwiperDigitIndicator\_SetTopPosition()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperDigitIndicator_SetTopPosition(ArkUI_SwiperDigitIndicator* indicator, float value)
```

**描述：**

设置数字导航指示器距离Swiper组件顶部的距离。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |
| float value | 数字导航指示器距离Swiper组件顶部的距离。默认值：0，单位：vp。 |

### OH\_ArkUI\_SwiperDigitIndicator\_GetTopPosition()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_SwiperDigitIndicator_GetTopPosition(ArkUI_SwiperDigitIndicator* indicator)
```

**描述：**

获取数字导航指示器距离Swiper组件顶部的距离。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 数字导航指示器距离Swiper组件顶部的距离。单位：vp。 |

### OH\_ArkUI\_SwiperDigitIndicator\_SetEndPosition()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperDigitIndicator_SetEndPosition(ArkUI_SwiperDigitIndicator* indicator, float value)
```

**描述：**

设置数字导航指示器距离Swiper组件右边的距离。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |
| float value | 数字导航指示器距离Swiper组件右边的距离。在从左至右显示的语言模式下，设置距离Swiper组件右边的距离；在从右至左显示的语言模式下，设置距离Swiper组件左边的距离。  默认值：0  单位：vp |

### OH\_ArkUI\_SwiperDigitIndicator\_GetEndPosition()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_SwiperDigitIndicator_GetEndPosition(ArkUI_SwiperDigitIndicator* indicator)
```

**描述：**

获取数字导航指示器距离Swiper组件右边的距离。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 数字导航指示器距离Swiper组件右边的距离。在从左至右显示的语言模式下，返回距离Swiper组件右边的距离；在从右至左显示的语言模式下，返回距离Swiper组件左边的距离。  单位：vp |

### OH\_ArkUI\_SwiperDigitIndicator\_SetBottomPosition()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperDigitIndicator_SetBottomPosition(ArkUI_SwiperDigitIndicator* indicator, float value)
```

**描述：**

设置数字导航指示器距离Swiper组件底部的距离。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |
| float value | 数字导航指示器距离Swiper组件底部的距离。默认值：0，单位：vp。 |

### OH\_ArkUI\_SwiperDigitIndicator\_GetBottomPosition()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_SwiperDigitIndicator_GetBottomPosition(ArkUI_SwiperDigitIndicator* indicator)
```

**描述：**

获取数字导航指示器距离Swiper组件底部的距离。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 数字导航指示器距离Swiper组件底部的距离。单位：vp。 |

### OH\_ArkUI\_SwiperDigitIndicator\_SetFontColor()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperDigitIndicator_SetFontColor(ArkUI_SwiperDigitIndicator* indicator, uint32_t color)
```

**描述：**

设置Swiper组件数字导航指示器字体颜色。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |
| uint32\_t color | 颜色类型，0xargb格式，形如 0xFFFF0000 表示红色。默认值：0xFF182431。 |

### OH\_ArkUI\_SwiperDigitIndicator\_GetFontColor()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_ArkUI_SwiperDigitIndicator_GetFontColor(ArkUI_SwiperDigitIndicator* indicator)
```

**描述：**

获取Swiper组件数字导航指示器字体颜色。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 颜色类型，0xargb格式，形如 0xFFFF0000 表示红色。 |

### OH\_ArkUI\_SwiperDigitIndicator\_SetSelectedFontColor()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperDigitIndicator_SetSelectedFontColor(ArkUI_SwiperDigitIndicator* indicator, uint32_t selectedColor)
```

**描述：**

设置被选中Swiper组件数字导航指示器字体颜色。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |
| uint32\_t selectedColor | 颜色类型，0xargb格式，形如 0xFFFF0000 表示红色。默认值：0xFF182431。 |

### OH\_ArkUI\_SwiperDigitIndicator\_GetSelectedFontColor()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_ArkUI_SwiperDigitIndicator_GetSelectedFontColor(ArkUI_SwiperDigitIndicator* indicator)
```

**描述：**

获取被选中Swiper组件数字导航指示器字体颜色。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 颜色类型，0xargb格式，形如 0xFFFF0000 表示红色。 |

### OH\_ArkUI\_SwiperDigitIndicator\_SetFontSize()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperDigitIndicator_SetFontSize(ArkUI_SwiperDigitIndicator* indicator, float size)
```

**描述：**

设置Swiper组件数字导航指示器字体大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |
| float size | 字体大小数值，单位为fp。  默认值：14 |

### OH\_ArkUI\_SwiperDigitIndicator\_GetFontSize()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_SwiperDigitIndicator_GetFontSize(ArkUI_SwiperDigitIndicator* indicator)
```

**描述：**

获取Swiper组件数字导航指示器字体大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 字体大小数值，单位为fp。 |

### OH\_ArkUI\_SwiperDigitIndicator\_SetSelectedFontSize()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperDigitIndicator_SetSelectedFontSize(ArkUI_SwiperDigitIndicator* indicator, float size)
```

**描述：**

设置被选中Swiper组件数字导航指示器字体大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |
| float size | 字体大小数值，单位为fp。  默认值：14 |

### OH\_ArkUI\_SwiperDigitIndicator\_GetSelectedFontSize()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_SwiperDigitIndicator_GetSelectedFontSize(ArkUI_SwiperDigitIndicator* indicator)
```

**描述：**

获取被选中Swiper组件数字导航指示器字体大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 字体大小数值，单位为fp。 |

### OH\_ArkUI\_SwiperDigitIndicator\_SetFontWeight()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperDigitIndicator_SetFontWeight(ArkUI_SwiperDigitIndicator *indicator, ArkUI_FontWeight fontWeight)
```

**描述：**

设置Swiper组件数字导航指示器字体粗细属性。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md) \*indicator | 数字导航指示器对象指针。 |
| [ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight) fontWeight | 字体粗细样式[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)。 |

### OH\_ArkUI\_SwiperDigitIndicator\_GetFontWeight()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_FontWeight OH_ArkUI_SwiperDigitIndicator_GetFontWeight(ArkUI_SwiperDigitIndicator* indicator)
```

**描述：**

获取Swiper组件数字导航指示器字体粗细属性。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight) | 字体粗细样式[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)。 |

### OH\_ArkUI\_SwiperDigitIndicator\_SetSelectedFontWeight()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperDigitIndicator_SetSelectedFontWeight(ArkUI_SwiperDigitIndicator *indicator, ArkUI_FontWeight selectedFontWeight)
```

**描述：**

设置被选中Swiper组件数字导航指示器字体粗细属性。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md) \*indicator | 数字导航指示器对象指针。 |
| [ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight) selectedFontWeight | 字体粗细样式[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)。 |

### OH\_ArkUI\_SwiperDigitIndicator\_GetSelectedFontWeight()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_FontWeight OH_ArkUI_SwiperDigitIndicator_GetSelectedFontWeight(ArkUI_SwiperDigitIndicator* indicator)
```

**描述：**

获取被选中Swiper组件数字导航指示器字体粗细属性。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 数字导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight) | 字体粗细样式[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)。 |

### OH\_ArkUI\_SwiperArrowStyle\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_SwiperArrowStyle *OH_ArkUI_SwiperArrowStyle_Create()
```

**描述：**

创建Swiper组件的导航箭头。

**起始版本：** 19

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md) \* | 导航箭头对象指针。 |

### OH\_ArkUI\_SwiperArrowStyle\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperArrowStyle_Destroy(ArkUI_SwiperArrowStyle* arrowStyle)
```

**描述：**

销毁Swiper组件的导航箭头指针。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |

### OH\_ArkUI\_SwiperArrowStyle\_SetShowBackground()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperArrowStyle_SetShowBackground(ArkUI_SwiperArrowStyle* arrowStyle, int32_t showBackground)
```

**描述：**

设置Swiper组件导航箭头底板是否显示。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |
| int32\_t showBackground | 导航箭头底板是否显示，0：不显示，1：显示，默认值：0。 |

### OH\_ArkUI\_SwiperArrowStyle\_GetShowBackground()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_SwiperArrowStyle_GetShowBackground(ArkUI_SwiperArrowStyle* arrowStyle)
```

**描述：**

获取Swiper组件导航箭头底板是否显示。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 导航箭头底板是否显示，0：不显示，1：显示。 |

### OH\_ArkUI\_SwiperArrowStyle\_SetShowSidebarMiddle()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperArrowStyle_SetShowSidebarMiddle(ArkUI_SwiperArrowStyle* arrowStyle, int32_t showSidebarMiddle)
```

**描述：**

设置Swiper组件导航箭头显示位置。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |
| int32\_t showSidebarMiddle | 导航箭头显示位置，0：显示在导航指示器两侧，1：显示在Swiper组件两侧，默认值：0。 |

### OH\_ArkUI\_SwiperArrowStyle\_GetShowSidebarMiddle()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_SwiperArrowStyle_GetShowSidebarMiddle(ArkUI_SwiperArrowStyle* arrowStyle)
```

**描述：**

获取Swiper组件导航箭头显示位置。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 导航箭头显示位置，0：显示在导航指示器两侧，1：显示在Swiper组件两侧。 |

### OH\_ArkUI\_SwiperArrowStyle\_SetBackgroundSize()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperArrowStyle_SetBackgroundSize(ArkUI_SwiperArrowStyle* arrowStyle, float backgroundSize)
```

**描述：**

设置Swiper组件导航箭头底板大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |
| float backgroundSize | 导航箭头底板大小，单位：vp。默认值：显示在导航指示器两侧24vp，显示在Swiper两侧32vp。 |

### OH\_ArkUI\_SwiperArrowStyle\_GetBackgroundSize()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_SwiperArrowStyle_GetBackgroundSize(ArkUI_SwiperArrowStyle* arrowStyle)
```

**描述：**

获取Swiper组件导航箭头底板大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 导航箭头底板大小，单位：vp。 |

### OH\_ArkUI\_SwiperArrowStyle\_SetBackgroundColor()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperArrowStyle_SetBackgroundColor(ArkUI_SwiperArrowStyle* arrowStyle, uint32_t backgroundColor)
```

**描述：**

设置Swiper组件导航箭头底板颜色。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |
| uint32\_t backgroundColor | 导航箭头底板颜色，0xargb格式，形如 0xFFFF0000 表示红色。默认值：显示在导航指示器两侧为0x00000000，显示在Swiper两侧为0x19182431。 |

### OH\_ArkUI\_SwiperArrowStyle\_GetBackgroundColor()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_ArkUI_SwiperArrowStyle_GetBackgroundColor(ArkUI_SwiperArrowStyle* arrowStyle)
```

**描述：**

获取Swiper组件导航箭头底板颜色。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 导航箭头底板颜色，0xargb格式，形如 0xFFFF0000 表示红色。 |

### OH\_ArkUI\_SwiperArrowStyle\_SetArrowSize()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperArrowStyle_SetArrowSize(ArkUI_SwiperArrowStyle* arrowStyle, float arrowSize)
```

**描述：**

设置Swiper组件导航箭头大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |
| float arrowSize | 导航箭头大小，单位：vp。  默认值：显示在导航指示器两侧18vp，显示在Swiper两侧24vp。显示导航箭头底板时，arrowSize固定为[backgroundSize](capi-native-type-h.md#oh_arkui_swiperarrowstyle_setbackgroundsize)的3/4。 |

### OH\_ArkUI\_SwiperArrowStyle\_GetArrowSize()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_SwiperArrowStyle_GetArrowSize(ArkUI_SwiperArrowStyle* arrowStyle)
```

**描述：**

获取Swiper组件导航箭头大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 导航箭头大小，单位：vp。 |

### OH\_ArkUI\_SwiperArrowStyle\_SetArrowColor()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperArrowStyle_SetArrowColor(ArkUI_SwiperArrowStyle* arrowStyle, uint32_t arrowColor)
```

**描述：**

设置Swiper组件导航箭头颜色。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |
| uint32\_t arrowColor | 导航箭头颜色，0xargb格式，形如0xFFFF0000表示红色。  默认值：'#182431'，深蓝色。 |

### OH\_ArkUI\_SwiperArrowStyle\_GetArrowColor()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_ArkUI_SwiperArrowStyle_GetArrowColor(ArkUI_SwiperArrowStyle* arrowStyle)
```

**描述：**

获取Swiper组件导航箭头颜色。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)\* arrowStyle | 导航箭头对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 导航箭头颜色，0xargb格式，形如 0xFFFF0000 表示红色。 |

### OH\_ArkUI\_SwiperIndicator\_SetSpace()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperIndicator_SetSpace(ArkUI_SwiperIndicator* indicator, float space)
```

**描述：**

设置导航点间距。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |
| float space | 导航点间距。默认值：8，单位：vp。 |

### OH\_ArkUI\_SwiperIndicator\_GetSpace()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_SwiperIndicator_GetSpace(ArkUI_SwiperIndicator* indicator)
```

**描述：**

获取导航点间距。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 导航点间距。单位：vp。 |

### OH\_ArkUI\_SwiperDigitIndicator\_SetIgnoreSizeOfBottom()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SwiperDigitIndicator_SetIgnoreSizeOfBottom(ArkUI_SwiperDigitIndicator* indicator, int32_t ignoreSize)
```

**描述：**

设置OH\_ArkUI\_SwiperDigitIndicator\_SetBottomPosition是否忽略导航点大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 导航指示器对象指针。 |
| int32\_t ignoreSize | 是否忽略导航点大小。1表示忽略导航点大小，0表示不忽略，默认值0。 |

### OH\_ArkUI\_SwiperDigitIndicator\_GetIgnoreSizeOfBottom()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_SwiperDigitIndicator_GetIgnoreSizeOfBottom(ArkUI_SwiperDigitIndicator* indicator)
```

**描述：**

获取OH\_ArkUI\_SwiperDigitIndicator\_SetBottomPosition是否忽略导航点大小。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)\* indicator | 导航指示器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回1表示忽略导航点大小，返回0表示不忽略。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ListItemSwipeActionItem* OH_ArkUI_ListItemSwipeActionItem_Create()
```

**描述：**

创建ListItemSwipeActionItem接口设置的配置项。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](i-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* | ListItemSwipeActionItem配置项实例。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ListItemSwipeActionItem_Dispose(ArkUI_ListItemSwipeActionItem* item)
```

**描述：**

销毁ListItemSwipeActionItem实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](i-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | 要销毁的ListItemSwipeActionItem实例。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_SetContent()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ListItemSwipeActionItem_SetContent(ArkUI_ListItemSwipeActionItem* item, ArkUI_NodeHandle node)
```

**描述：**

设置ListItemSwipeActionItem的布局内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](i-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 布局信息。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_SetActionAreaDistance()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ListItemSwipeActionItem_SetActionAreaDistance(ArkUI_ListItemSwipeActionItem* item, float distance)
```

**描述：**

设置组件长距离滑动删除距离阈值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](i-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |
| float distance | 组件长距离滑动删除距离阈值，单位vp。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_GetActionAreaDistance()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_ListItemSwipeActionItem_GetActionAreaDistance(ArkUI_ListItemSwipeActionItem* item)
```

**描述：**

获取组件长距离滑动删除距离阈值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](i-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 组件长距离滑动删除距离阈值，单位vp，异常时返回值：0。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_SetOnEnterActionArea()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ListItemSwipeActionItem_SetOnEnterActionArea(ArkUI_ListItemSwipeActionItem* item, void (*callback)())
```

**描述：**

设置滑动条目进入删除区域时调用的事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](i-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |
| callback | 回调事件。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_SetOnEnterActionAreaWithUserData()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ListItemSwipeActionItem_SetOnEnterActionAreaWithUserData(ArkUI_ListItemSwipeActionItem* item,void* userData, void (*callback)(void* userData))
```

**描述：**

设置滑动条目进入删除区域时调用的事件，回调事件会传入用户自定义数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](i-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |
| void\* userData | 用户自定义数据。 |
| callback | 回调事件。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_SetOnAction()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ListItemSwipeActionItem_SetOnAction(ArkUI_ListItemSwipeActionItem* item, void (*callback)())
```

**描述：**

设置组件进入长距删除区后删除[ListItem](ts-container-listitem.md)时调用的事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](i-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |
| callback | 回调事件。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_SetOnActionWithUserData()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ListItemSwipeActionItem_SetOnActionWithUserData(ArkUI_ListItemSwipeActionItem* item,void* userData, void (*callback)(void* userData))
```

**描述：**

设置组件进入长距删除区后删除ListItem时调用的事件，回调事件会传入用户自定义数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](i-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |
| void\* userData | 用户自定义数据。 |
| callback | 回调事件。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_SetOnExitActionArea()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ListItemSwipeActionItem_SetOnExitActionArea(ArkUI_ListItemSwipeActionItem* item, void (*callback)())
```

**描述：**

设置滑动条目退出删除区域时调用的事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](i-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |
| callback | 回调事件。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_SetOnExitActionAreaWithUserData()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ListItemSwipeActionItem_SetOnExitActionAreaWithUserData(ArkUI_ListItemSwipeActionItem* item,void* userData, void (*callback)(void* userData))
```

**描述：**

设置滑动条目退出删除区域时调用的事件，回调事件会传入用户自定义数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](i-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |
| void\* userData | 用户自定义数据。 |
| callback | 回调事件。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_SetOnStateChange()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ListItemSwipeActionItem_SetOnStateChange(ArkUI_ListItemSwipeActionItem* item,void (*callback)(ArkUI_ListItemSwipeActionState swipeActionState))
```

**描述：**

设置列表项滑动状态变化时候触发的事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](i-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |
| callback | 回调事件。传入参数为swipeActionState，表示列表项滑动状态。 |

### OH\_ArkUI\_ListItemSwipeActionItem\_SetOnStateChangeWithUserData()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ListItemSwipeActionItem_SetOnStateChangeWithUserData(ArkUI_ListItemSwipeActionItem* item,void* userData, void (*callback)(ArkUI_ListItemSwipeActionState swipeActionState, void* userData))
```

**描述：**

设置列表项滑动状态变化时候触发的事件，回调事件会传入用户自定义数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionItem](i-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | ListItemSwipeActionItem实例。 |
| void\* userData | 用户自定义数据。 |
| callback | 回调事件。传入参数为swipeActionState，表示列表项滑动状态。 |

### OH\_ArkUI\_ListItemSwipeActionOption\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ListItemSwipeActionOption* OH_ArkUI_ListItemSwipeActionOption_Create()
```

**描述：**

创建ListItemSwipeActionOption接口设置的配置项。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionOption](arkui-nativemodule-arkui-listitemswipeactionoption.md)\* | ListItemSwipeActionOption配置项实例。 |

### OH\_ArkUI\_ListItemSwipeActionOption\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ListItemSwipeActionOption_Dispose(ArkUI_ListItemSwipeActionOption* option)
```

**描述：**

销毁ListItemSwipeActionOption实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionOption](arkui-nativemodule-arkui-listitemswipeactionoption.md)\* option | 要销毁的ListItemSwipeActionOption实例。 |

### OH\_ArkUI\_ListItemSwipeActionOption\_SetStart()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ListItemSwipeActionOption_SetStart(ArkUI_ListItemSwipeActionOption* option, ArkUI_ListItemSwipeActionItem* item)
```

**描述：**

设置ListItemSwipeActionItem的左侧（垂直布局）或上方（横向布局）布局内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionOption](arkui-nativemodule-arkui-listitemswipeactionoption.md)\* option | ListItemSwipeActionItem实例。 |
| [ArkUI\_ListItemSwipeActionItem](i-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | 布局信息。 |

### OH\_ArkUI\_ListItemSwipeActionOption\_SetEnd()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ListItemSwipeActionOption_SetEnd(ArkUI_ListItemSwipeActionOption* option,ArkUI_ListItemSwipeActionItem* item)
```

**描述：**

设置ListItemSwipeActionItem的右侧（垂直布局）或下方（横向布局）布局内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionOption](arkui-nativemodule-arkui-listitemswipeactionoption.md)\* option | ListItemSwipeActionItem实例。 |
| [ArkUI\_ListItemSwipeActionItem](i-arkui-nativemodule-arkui-listitemswipeactionitem.md)\* item | 布局信息。 |

### OH\_ArkUI\_ListItemSwipeActionOption\_SetEdgeEffect()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ListItemSwipeActionOption_SetEdgeEffect(ArkUI_ListItemSwipeActionOption* option,ArkUI_ListItemSwipeEdgeEffect edgeEffect)
```

**描述：**

设置边缘滑动效果。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionOption](arkui-nativemodule-arkui-listitemswipeactionoption.md)\* option | ListItemSwipeActionItem实例。 |
| [ArkUI\_ListItemSwipeEdgeEffect](capi-native-type-h.md#arkui_listitemswipeedgeeffect) edgeEffect | 边缘滑动效果。 |

### OH\_ArkUI\_ListItemSwipeActionOption\_GetEdgeEffect()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_ListItemSwipeActionOption_GetEdgeEffect(ArkUI_ListItemSwipeActionOption* option)
```

**描述：**

获取边缘滑动效果。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionOption](arkui-nativemodule-arkui-listitemswipeactionoption.md)\* option | ListItemSwipeActionItem实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 边缘滑动效果。默认返回值：[ARKUI\_LIST\_ITEM\_SWIPE\_EDGE\_EFFECT\_SPRING](capi-native-type-h.md#arkui_listitemswipeedgeeffect)。 |

### OH\_ArkUI\_ListItemSwipeActionOption\_SetOnOffsetChange()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ListItemSwipeActionOption_SetOnOffsetChange(ArkUI_ListItemSwipeActionOption* option,void (*callback)(float offset))
```

**描述：**

滑动操作偏移量更改时调用的事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionOption](arkui-nativemodule-arkui-listitemswipeactionoption.md)\* option | ListItemSwipeActionItem实例。 |
| callback | 回调事件。offset 滑动偏移量，单位vp。 |

### OH\_ArkUI\_ListItemSwipeActionOption\_SetOnOffsetChangeWithUserData()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ListItemSwipeActionOption_SetOnOffsetChangeWithUserData(ArkUI_ListItemSwipeActionOption* option,void* userData, void (*callback)(float offset, void* userData))
```

**描述：**

滑动操作偏移量更改时调用的事件，回调事件会传入用户自定义数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListItemSwipeActionOption](arkui-nativemodule-arkui-listitemswipeactionoption.md)\* option | ListItemSwipeActionItem实例。 |
| void\* userData | 用户自定义数据。 |
| callback | 回调事件。offset 滑动偏移量，单位vp。 |

### OH\_ArkUI\_ListItemSwipeAction\_Expand()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_ListItemSwipeAction_Expand(ArkUI_NodeHandle node, ArkUI_ListItemSwipeActionDirection direction)
```

**描述：**

展开指定ListItem的划出菜单。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | ListItem节点对象。 |
| [ArkUI\_ListItemSwipeActionDirection](capi-native-type-h.md#arkui_listitemswipeactiondirection) direction | ListItem划出菜单的展开方向。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_ERROR](capi-native-type-h.md#arkui_errorcode) 传入的节点对象类型错误。  [ARKUI\_ERROR\_CODE\_NODE\_NOT\_ON\_MAIN\_TREE](capi-native-type-h.md#arkui_errorcode) 传入的节点未挂载到组件树上。 |

说明

* 如果List组件NODE\_LIST\_CACHED\_COUNT属性设置显示预加载ListItem，List显示区域外已预加载完成的ListItem支持展开，否则List显示区域外节点不支持展开。

### OH\_ArkUI\_ListItemSwipeAction\_Collapse()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_ListItemSwipeAction_Collapse(ArkUI_NodeHandle node)
```

**描述：**

收起指定ListItem的划出菜单。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | ListItem节点对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_ERROR](capi-native-type-h.md#arkui_errorcode) 传入的节点对象类型错误。  [ARKUI\_ERROR\_CODE\_NODE\_NOT\_ON\_MAIN\_TREE](capi-native-type-h.md#arkui_errorcode) 传入的节点未挂载到组件树上。 |

### OH\_ArkUI\_AccessibilityState\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_AccessibilityState* OH_ArkUI_AccessibilityState_Create(void)
```

**描述：**

创建无障碍状态。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_AccessibilityState](capi-arkui-nativemodule-arkui-accessibilitystate.md)\* | 无障碍状态对象指针。如果对象返回空指针，表示创建失败，失败的可能原因是应用地址空间满。 |

### OH\_ArkUI\_AccessibilityState\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AccessibilityState_Dispose(ArkUI_AccessibilityState* state)
```

**描述：**

销毁无障碍状态指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityState](capi-arkui-nativemodule-arkui-accessibilitystate.md)\* state | 无障碍状态对象指针。 |

### OH\_ArkUI\_AccessibilityState\_SetDisabled()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AccessibilityState_SetDisabled(ArkUI_AccessibilityState* state, int32_t isDisabled)
```

**描述：**

设置无障碍状态是否禁用。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityState](capi-arkui-nativemodule-arkui-accessibilitystate.md)\* state | 无障碍状态对象指针。 |
| int32\_t isDisabled | 无障碍状态是否禁用， 1表示禁用，0表示不禁用，默认为0。 |

### OH\_ArkUI\_AccessibilityState\_IsDisabled()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityState_IsDisabled(ArkUI_AccessibilityState* state)
```

**描述：**

获取无障碍状态是否禁用。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityState](capi-arkui-nativemodule-arkui-accessibilitystate.md)\* state | 无障碍状态对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 是否禁用， 1表示禁用，0表示未禁用，默认为0;  若state为空，返回默认值。 |

### OH\_ArkUI\_AccessibilityState\_SetSelected()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AccessibilityState_SetSelected(ArkUI_AccessibilityState* state, int32_t isSelected)
```

**描述：**

设置无障碍状态是否选中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityState](capi-arkui-nativemodule-arkui-accessibilitystate.md)\* state | 无障碍状态对象指针。 |
| int32\_t isSelected | 是否被选中， 1表示选中，0表示未选中，默认为0。 |

### OH\_ArkUI\_AccessibilityState\_IsSelected()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityState_IsSelected(ArkUI_AccessibilityState* state)
```

**描述：**

获取无障碍状态是否选中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityState](capi-arkui-nativemodule-arkui-accessibilitystate.md)\* state | 无障碍状态对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 是否被选中， 1表示选中，0表示未选中，默认为0;  若state为空，返回默认值。 |

### OH\_ArkUI\_AccessibilityState\_SetCheckedState()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AccessibilityState_SetCheckedState(ArkUI_AccessibilityState* state, int32_t checkedState)
```

**描述：**

设置无障碍状态复选框状态。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityState](capi-arkui-nativemodule-arkui-accessibilitystate.md)\* state | 无障碍状态对象指针。 |
| int32\_t checkedState | 复选框状态，参数类型[ArkUI\_AccessibilityCheckedState](capi-native-type-h.md#arkui_accessibilitycheckedstate), 默认值：ARKUI\_ACCESSIBILITY\_UNCHECKED。 |

### OH\_ArkUI\_AccessibilityState\_GetCheckedState()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityState_GetCheckedState(ArkUI_AccessibilityState* state)
```

**描述：**

获取无障碍状态复选框状态。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityState](capi-arkui-nativemodule-arkui-accessibilitystate.md)\* state | 无障碍状态对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 复选框状态，参数类型[ArkUI\_AccessibilityCheckedState](capi-native-type-h.md#arkui_accessibilitycheckedstate), 默认值：ARKUI\_ACCESSIBILITY\_UNCHECKED;  若函数参数异常，返回默认值。 |

### OH\_ArkUI\_AccessibilityValue\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_AccessibilityValue* OH_ArkUI_AccessibilityValue_Create(void)
```

**描述：**

创建无障碍信息。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_AccessibilityValue](capi-arkui-nativemodule-arkui-accessibilityvalue.md)\* | 无障碍信息对象指针。 |

### OH\_ArkUI\_AccessibilityValue\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AccessibilityValue_Dispose(ArkUI_AccessibilityValue* value)
```

**描述：**

销毁无障碍信息指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityValue](capi-arkui-nativemodule-arkui-accessibilityvalue.md)\* value | 无障碍信息对象指针。 |

### OH\_ArkUI\_AccessibilityValue\_SetMin()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AccessibilityValue_SetMin(ArkUI_AccessibilityValue* value, int32_t min)
```

**描述：**

设置无障碍最小值信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityValue](capi-arkui-nativemodule-arkui-accessibilityvalue.md)\* value | 无障碍信息对象指针。 |
| int32\_t min | 基于范围组件的最小值, 默认为-1。 |

### OH\_ArkUI\_AccessibilityValue\_GetMin()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityValue_GetMin(ArkUI_AccessibilityValue* value)
```

**描述：**

获取无障碍最小值信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityValue](capi-arkui-nativemodule-arkui-accessibilityvalue.md)\* value | 无障碍信息对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 基于范围组件的最小值, 默认为-1;  若函数参数异常，返回-1。 |

### OH\_ArkUI\_AccessibilityValue\_SetMax()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AccessibilityValue_SetMax(ArkUI_AccessibilityValue* value, int32_t max)
```

**描述：**

设置无障碍最大值信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityValue](capi-arkui-nativemodule-arkui-accessibilityvalue.md)\* value | 无障碍信息对象指针。 |
| int32\_t max | 基于范围组件的最大值, 默认为-1。 |

### OH\_ArkUI\_AccessibilityValue\_GetMax()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityValue_GetMax(ArkUI_AccessibilityValue* value)
```

**描述：**

获取无障碍最大值信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityValue](capi-arkui-nativemodule-arkui-accessibilityvalue.md)\* value | 无障碍信息对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 基于范围组件的最大值, 默认为-1;  若函数参数异常，返回-1。 |

### OH\_ArkUI\_AccessibilityValue\_SetCurrent()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AccessibilityValue_SetCurrent(ArkUI_AccessibilityValue* value, int32_t current)
```

**描述：**

设置无障碍当前值信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityValue](capi-arkui-nativemodule-arkui-accessibilityvalue.md)\* value | 无障碍信息对象指针。 |
| int32\_t current | 基于范围组件的当前值, 默认为-1。 |

### OH\_ArkUI\_AccessibilityValue\_GetCurrent()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityValue_GetCurrent(ArkUI_AccessibilityValue* value)
```

**描述：**

获取无障碍当前值信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityValue](capi-arkui-nativemodule-arkui-accessibilityvalue.md)\* value | 无障碍信息对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 基于范围组件的当前值, 默认为-1;  若函数参数异常，返回-1。 |

### OH\_ArkUI\_AccessibilityValue\_SetRangeMin()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AccessibilityValue_SetRangeMin(ArkUI_AccessibilityValue* value, int32_t rangeMin)
```

**描述：**

设置范围组件的无障碍最小值信息。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityValue](capi-arkui-nativemodule-arkui-accessibilityvalue.md)\* value | 需要设置最小值的范围组件无障碍信息对象指针。 |
| int32\_t rangeMin | 基于范围组件的最小值, 默认为-1。 |

### OH\_ArkUI\_AccessibilityValue\_GetRangeMin()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityValue_GetRangeMin(ArkUI_AccessibilityValue* value)
```

**描述：**

获取范围组件的无障碍最小值信息。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityValue](capi-arkui-nativemodule-arkui-accessibilityvalue.md)\* value | 需要获取最小值的范围组件无障碍信息对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 基于范围组件的最小值, 默认为-1;  若函数参数异常，返回-1。 |

### OH\_ArkUI\_AccessibilityValue\_SetRangeMax()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AccessibilityValue_SetRangeMax(ArkUI_AccessibilityValue* value, int32_t rangeMax)
```

**描述：**

设置范围组件的无障碍最大值信息。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityValue](capi-arkui-nativemodule-arkui-accessibilityvalue.md)\* value | 需要设置最大值的范围组件无障碍信息对象指针。 |
| int32\_t rangeMax | 基于范围组件的最大值, 默认为-1。 |

### OH\_ArkUI\_AccessibilityValue\_GetRangeMax()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityValue_GetRangeMax(ArkUI_AccessibilityValue* value)
```

**描述：**

获取范围组件的无障碍最大值信息。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityValue](capi-arkui-nativemodule-arkui-accessibilityvalue.md)\* value | 需要获取最小值的范围组件无障碍信息对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 基于范围组件的最大值, 默认为-1;  若函数参数异常，返回-1。 |

### OH\_ArkUI\_AccessibilityValue\_SetRangeCurrent()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AccessibilityValue_SetRangeCurrent(ArkUI_AccessibilityValue* value, int32_t rangeCurrent)
```

**描述：**

用于设置范围组件的无障碍当前值信息。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityValue](capi-arkui-nativemodule-arkui-accessibilityvalue.md)\* value | 需要设置当前值的范围组件无障碍信息对象指针。 |
| int32\_t rangeCurrent | 基于范围组件的当前值, 默认为-1。 |

### OH\_ArkUI\_AccessibilityValue\_GetRangeCurrent()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityValue_GetRangeCurrent(ArkUI_AccessibilityValue* value)
```

**描述：**

用于获取范围组件的无障碍当前值信息。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityValue](capi-arkui-nativemodule-arkui-accessibilityvalue.md)\* value | 需要获取当前值的范围组件无障碍信息对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 基于范围组件的当前值, 默认为-1;  若函数参数异常，返回-1。 |

### OH\_ArkUI\_AccessibilityValue\_SetText()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_AccessibilityValue_SetText(ArkUI_AccessibilityValue* value, const char* text)
```

**描述：**

设置无障碍文本描述信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityValue](capi-arkui-nativemodule-arkui-accessibilityvalue.md)\* value | 无障碍信息对象指针。 |
| const char\* text | 组件的文本描述信息, 默认为空字符串。 |

### OH\_ArkUI\_AccessibilityValue\_GetText()

PhonePC/2in1TabletTVWearable

```
1. const char* OH_ArkUI_AccessibilityValue_GetText(ArkUI_AccessibilityValue* value)
```

**描述：**

获取无障碍文本描述信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityValue](capi-arkui-nativemodule-arkui-accessibilityvalue.md)\* value | 无障碍信息对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 组件的文本描述信息, 默认为空字符串;  若函数参数异常，返回空指针。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_CreateFromString()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ImageAnimatorFrameInfo* OH_ArkUI_ImageAnimatorFrameInfo_CreateFromString(char* src)
```

**描述：**

使用图片路径创建帧图片信息，图片格式为svg、png和jpg。支持应用沙箱内的相对路径和绝对路径。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\* src | 图片路径，支持应用沙箱内的相对路径或绝对路径。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](pi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* | 帧图片对象指针。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_CreateFromDrawableDescriptor()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ImageAnimatorFrameInfo* OH_ArkUI_ImageAnimatorFrameInfo_CreateFromDrawableDescriptor(ArkUI_DrawableDescriptor* drawable)
```

**描述：**

使用[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)对象创建帧图片信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)\* drawable | 使用PixelMap创建的ArkUI\_DrawableDescriptor对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](pi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* | 帧图片对象指针。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ImageAnimatorFrameInfo_Dispose(ArkUI_ImageAnimatorFrameInfo* imageInfo)
```

**描述：**

销毁帧图片对象指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](pi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_SetWidth()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ImageAnimatorFrameInfo_SetWidth(ArkUI_ImageAnimatorFrameInfo* imageInfo, int32_t width)
```

**描述：**

设置图片宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](pi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |
| int32\_t width | 图片宽度，单位为px。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_GetWidth()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_ImageAnimatorFrameInfo_GetWidth(ArkUI_ImageAnimatorFrameInfo* imageInfo)
```

**描述：**

获取图片宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](pi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 图片宽度，单位为px，imageInfo为空指针时返回0。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_SetHeight()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ImageAnimatorFrameInfo_SetHeight(ArkUI_ImageAnimatorFrameInfo* imageInfo, int32_t height)
```

**描述：**

设置图片高度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](pi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |
| int32\_t height | 图片高度，单位为px。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_GetHeight()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_ImageAnimatorFrameInfo_GetHeight(ArkUI_ImageAnimatorFrameInfo* imageInfo)
```

**描述：**

获取图片高度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](pi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 图片高度，单位为px，imageInfo为空指针时返回0。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_SetTop()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ImageAnimatorFrameInfo_SetTop(ArkUI_ImageAnimatorFrameInfo* imageInfo, int32_t top)
```

**描述：**

设置图片相对于组件左上角的纵向坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](pi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |
| int32\_t top | 图片相对于组件左上角的纵向坐标，单位为px。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_GetTop()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_ImageAnimatorFrameInfo_GetTop(ArkUI_ImageAnimatorFrameInfo* imageInfo)
```

**描述：**

获取图片相对于组件左上角的纵向坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](pi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 图片相对于组件左上角的纵向坐标，单位为px，imageInfo为空指针时返回0。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_SetLeft()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ImageAnimatorFrameInfo_SetLeft(ArkUI_ImageAnimatorFrameInfo* imageInfo, int32_t left)
```

**描述：**

设置图片相对于组件左上角的横向坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](pi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |
| int32\_t left | 图片相对于组件左上角的横向坐标，单位为px。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_GetLeft()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_ImageAnimatorFrameInfo_GetLeft(ArkUI_ImageAnimatorFrameInfo* imageInfo)
```

**描述：**

获取图片相对于组件左上角的横向坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](pi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 图片相对于组件左上角的横向坐标，单位为px，imageInfo为空指针时返回0。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_SetDuration()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ImageAnimatorFrameInfo_SetDuration(ArkUI_ImageAnimatorFrameInfo* imageInfo, int32_t duration)
```

**描述：**

设置图片的播放时长。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](pi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |
| int32\_t duration | 图片的播放时长，单位为ms。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_GetDuration()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_ImageAnimatorFrameInfo_GetDuration(ArkUI_ImageAnimatorFrameInfo* imageInfo)
```

**描述：**

获取图片的播放时长。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](pi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 图片的播放时长，单位为毫秒，imageInfo为空指针时返回0。 |

### OH\_ArkUI\_ListChildrenMainSizeOption\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ListChildrenMainSize* OH_ArkUI_ListChildrenMainSizeOption_Create()
```

**描述：**

创建ListChildrenMainSize接口设置的配置项。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)\* | ListChildrenMainSize配置项实例。 |

### OH\_ArkUI\_ListChildrenMainSizeOption\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ListChildrenMainSizeOption_Dispose(ArkUI_ListChildrenMainSize* option)
```

**描述：**

销毁ListChildrenMainSize实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)\* option | 要销毁的ListChildrenMainSize实例。 |

### OH\_ArkUI\_ListChildrenMainSizeOption\_SetDefaultMainSize()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_ListChildrenMainSizeOption_SetDefaultMainSize(ArkUI_ListChildrenMainSize* option, float defaultMainSize)
```

**描述：**

设置[List](ts-container-list.md)组件列表项在主轴方向的默认尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)\* option | ListChildrenMainSize实例。 |
| float defaultMainSize | 列表项在主轴方向的默认尺寸值，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ListChildrenMainSizeOption\_GetDefaultMainSize()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_ListChildrenMainSizeOption_GetDefaultMainSize(ArkUI_ListChildrenMainSize* option)
```

**描述：**

获取[List](ts-container-list.md)组件的列表项在主轴方向的默认尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)\* option | ListChildrenMainSize实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 列表项在主轴方向的默认尺寸值，默认为0，单位为[vp](ts-types.md#vp10)，option为空指针时返回-1。 |

### OH\_ArkUI\_ListChildrenMainSizeOption\_Resize()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ListChildrenMainSizeOption_Resize(ArkUI_ListChildrenMainSize* option, int32_t totalSize)
```

**描述：**

调整[List](ts-container-list.md)组件子项主轴尺寸数组的容量大小。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)\* option | ListChildrenMainSize实例。 |
| int32\_t totalSize | 目标数组容量大小。 |

### OH\_ArkUI\_ListChildrenMainSizeOption\_Splice()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_ListChildrenMainSizeOption_Splice(ArkUI_ListChildrenMainSize* option, int32_t index, int32_t deleteCount, int32_t addCount)
```

**描述：**

对[List](ts-container-list.md)组件子项主轴尺寸数组进行大小调整。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)\* option | ListChildrenMainSize实例。 |
| int32\_t index | 操作起始索引位置。 |
| int32\_t deleteCount | 从起始位置开始删除的元素数量。 |
| int32\_t addCount | 从起始位置开始新增的元素数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ListChildrenMainSizeOption\_UpdateSize()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_ListChildrenMainSizeOption_UpdateSize(ArkUI_ListChildrenMainSize* option, int32_t index, float mainSize)
```

**描述：**

更新[List](ts-container-list.md)组件子项主轴尺寸数组中指定索引位置的尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)\* option | ListChildrenMainSize实例。 |
| int32\_t index | 目标元素的数组索引位置。 |
| float mainSize | 要设置的主轴尺寸值，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ListChildrenMainSizeOption\_GetMainSize()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_ListChildrenMainSizeOption_GetMainSize(ArkUI_ListChildrenMainSize* option, int32_t index)
```

**描述：**

获取[List](ts-container-list.md)组件子项主轴尺寸数组中指定索引位置的尺寸。主轴方向为纵向时表示高度，为横向时表示宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)\* option | ListChildrenMainSize实例。 |
| int32\_t index | 目标元素的数组索引位置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 数组具体位置的值。若函数参数异常，返回-1。 |

### OH\_ArkUI\_CustomSpanMeasureInfo\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_CustomSpanMeasureInfo* OH_ArkUI_CustomSpanMeasureInfo_Create(void)
```

**描述：**

创建自定义段落组件测量信息。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CustomSpanMeasureInfo](api-arkui-nativemodule-arkui-customspanmeasureinfo.md)\* | CustomSpanMeasureInfo实例。  如果返回空指针，可能是因为内存不足。 |

### OH\_ArkUI\_CustomSpanMeasureInfo\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_CustomSpanMeasureInfo_Dispose(ArkUI_CustomSpanMeasureInfo* info)
```

**描述：**

销毁自定义段落组件测量信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomSpanMeasureInfo](api-arkui-nativemodule-arkui-customspanmeasureinfo.md)\* info | 自定义段落组件测量信息指针。 |

### OH\_ArkUI\_CustomSpanMeasureInfo\_GetFontSize()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_CustomSpanMeasureInfo_GetFontSize(ArkUI_CustomSpanMeasureInfo* info)
```

**描述：**

获取自定义段落组件的父节点Text的字体大小。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomSpanMeasureInfo](api-arkui-nativemodule-arkui-customspanmeasureinfo.md)\* info | 自定义段落组件测量信息指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 父节点Text的字体大小，单位为fp。若函数参数异常，返回0.0f。  异常返回原因：传入参数验证失败，参数不能为空。 |

### OH\_ArkUI\_CustomSpanMetrics\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_CustomSpanMetrics* OH_ArkUI_CustomSpanMetrics_Create(void)
```

**描述：**

创建自定义段落组件度量信息。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CustomSpanMetrics](capi-arkui-nativemodule-arkui-customspanmetrics.md)\* | CustomSpanMetrics实例。  如果返回空指针，可能是因为内存不足。 |

### OH\_ArkUI\_CustomSpanMetrics\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_CustomSpanMetrics_Dispose(ArkUI_CustomSpanMetrics* metrics)
```

**描述：**

销毁自定义段落组件度量信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomSpanMetrics](capi-arkui-nativemodule-arkui-customspanmetrics.md)\* metrics | CustomSpanMetrics实例。 |

### OH\_ArkUI\_CustomSpanMetrics\_SetWidth()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomSpanMetrics_SetWidth(ArkUI_CustomSpanMetrics* metrics, float width)
```

**描述：**

设置自定义段落组件的宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomSpanMetrics](capi-arkui-nativemodule-arkui-customspanmetrics.md)\* metrics | CustomSpanMetrics实例。 |
| float width | 宽度大小，单位为vp。默认值为0.0f，负值与默认值效果一致。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  异常原因：传入参数验证失败，参数不能为空。 |

### OH\_ArkUI\_CustomSpanMetrics\_SetHeight()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomSpanMetrics_SetHeight(ArkUI_CustomSpanMetrics* metrics, float height)
```

**描述：**

设置自定义段落组件的高度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomSpanMetrics](capi-arkui-nativemodule-arkui-customspanmetrics.md)\* metrics | CustomSpanMetrics实例。 |
| float height | 高度大小，单位为vp。默认值为0.0f，负值与默认值效果一致。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  异常原因：传入参数验证失败，参数不能为空。 |

### OH\_ArkUI\_CustomSpanDrawInfo\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_CustomSpanDrawInfo* OH_ArkUI_CustomSpanDrawInfo_Create(void)
```

**描述：**

创建自定义段落组件绘制信息。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CustomSpanDrawInfo](capi-arkui-nativemodule-arkui-customspandrawinfo.md)\* | CustomSpanDrawInfo实例。  如果返回空指针，可能是因为内存不足。 |

### OH\_ArkUI\_CustomSpanDrawInfo\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_CustomSpanDrawInfo_Dispose(ArkUI_CustomSpanDrawInfo* info)
```

**描述：**

销毁自定义段落组件绘制信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomSpanDrawInfo](capi-arkui-nativemodule-arkui-customspandrawinfo.md)\* info | 自定义段落组件绘制信息指针。 |

### OH\_ArkUI\_CustomSpanDrawInfo\_GetXOffset()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_CustomSpanDrawInfo_GetXOffset(ArkUI_CustomSpanDrawInfo* info)
```

**描述：**

获取自定义段落组件相对于挂载组件的x轴偏移值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomSpanDrawInfo](capi-arkui-nativemodule-arkui-customspandrawinfo.md)\* info | 自定义段落组件绘制信息指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | x轴偏移值，单位为px。若函数参数异常，返回0.0f。  异常返回原因：传入参数验证失败，参数不能为空。 |

### OH\_ArkUI\_CustomSpanDrawInfo\_GetLineTop()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_CustomSpanDrawInfo_GetLineTop(ArkUI_CustomSpanDrawInfo* info)
```

**描述：**

获取自定义段落组件相对于挂载组件的上边距。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomSpanDrawInfo](capi-arkui-nativemodule-arkui-customspandrawinfo.md)\* info | 自定义段落组件绘制信息指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 上边距值，单位为px。若函数参数异常，返回0.0f。  异常返回原因：传入参数验证失败，参数不能为空。 |

### OH\_ArkUI\_CustomSpanDrawInfo\_GetLineBottom()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_CustomSpanDrawInfo_GetLineBottom(ArkUI_CustomSpanDrawInfo* info)
```

**描述：**

获取自定义段落组件相对于挂载组件的下边距。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomSpanDrawInfo](capi-arkui-nativemodule-arkui-customspandrawinfo.md)\* info | 自定义段落组件绘制信息指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 下边距值，单位为px。若函数参数异常，返回0.0f。  异常返回原因：传入参数验证失败，参数不能为空。 |

### OH\_ArkUI\_CustomSpanDrawInfo\_GetBaseline()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_CustomSpanDrawInfo_GetBaseline(ArkUI_CustomSpanDrawInfo* info)
```

**描述：**

获取自定义段落组件相对于挂载组件的基线偏移量。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomSpanDrawInfo](capi-arkui-nativemodule-arkui-customspandrawinfo.md)\* info | 自定义段落组件绘制信息指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 基线偏移量值，单位为px。若函数参数异常，返回0.0f。  异常返回原因：传入参数验证失败，参数不能为空。 |

### OH\_ArkUI\_CustomProperty\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_CustomProperty_Destroy(ArkUI_CustomProperty* handle)
```

**描述：**

销毁[ArkUI\_CustomProperty](capi-arkui-nativemodule-arkui-customproperty.md)实例。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomProperty](capi-arkui-nativemodule-arkui-customproperty.md)\* handle | 要销毁的实例。 |

### OH\_ArkUI\_CustomProperty\_GetStringValue()

PhonePC/2in1TabletTVWearable

```
1. const char* OH_ArkUI_CustomProperty_GetStringValue(ArkUI_CustomProperty* handle)
```

**描述：**

获取自定义属性对象的value信息。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomProperty](capi-arkui-nativemodule-arkui-customproperty.md)\* handle | 自定义属性对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 自定义属性对象的value信息。 |

### OH\_ArkUI\_HostWindowInfo\_GetName()

PhonePC/2in1TabletTVWearable

```
1. const char* OH_ArkUI_HostWindowInfo_GetName(ArkUI_HostWindowInfo* info)
```

**描述：**

获取[ArkUI\_HostWindowInfo](capi-arkui-nativemodule-arkui-hostwindowinfo.md)对象中的窗口名称。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_HostWindowInfo](capi-arkui-nativemodule-arkui-hostwindowinfo.md)\* info | HostWindowInfo对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | [ArkUI\_HostWindowInfo](capi-arkui-nativemodule-arkui-hostwindowinfo.md)对象中的窗口名称。 |

### OH\_ArkUI\_HostWindowInfo\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_HostWindowInfo_Destroy(ArkUI_HostWindowInfo* info)
```

**描述：**

销毁[ArkUI\_HostWindowInfo](capi-arkui-nativemodule-arkui-hostwindowinfo.md)对象。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_HostWindowInfo](capi-arkui-nativemodule-arkui-hostwindowinfo.md)\* info | 要销毁的[ArkUI\_HostWindowInfo](capi-arkui-nativemodule-arkui-hostwindowinfo.md)对象。 |

### OH\_ArkUI\_ActiveChildrenInfo\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ActiveChildrenInfo_Destroy(ArkUI_ActiveChildrenInfo* handle)
```

**描述：**

销毁[ArkUI\_ActiveChildrenInfo](capi-arkui-nativemodule-arkui-activechildreninfo.md)实例。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ActiveChildrenInfo](capi-arkui-nativemodule-arkui-activechildreninfo.md)\* handle | 要销毁的[ArkUI\_ActiveChildrenInfo](capi-arkui-nativemodule-arkui-activechildreninfo.md)实例。 |

### OH\_ArkUI\_ActiveChildrenInfo\_GetNodeByIndex()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_NodeHandle OH_ArkUI_ActiveChildrenInfo_GetNodeByIndex(ArkUI_ActiveChildrenInfo* handle, int32_t index)
```

**描述：**

获取[ArkUI\_ActiveChildrenInfo](capi-arkui-nativemodule-arkui-activechildreninfo.md)结构体的下标为index的子节点。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ActiveChildrenInfo](capi-arkui-nativemodule-arkui-activechildreninfo.md)\* handle | 要获取信息的[ArkUI\_ActiveChildrenInfo](capi-arkui-nativemodule-arkui-activechildreninfo.md)实例。 |
| int32\_t index | 子节点的下标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) | 下标对应的子节点指针，异常时返回nullptr。 |

### OH\_ArkUI\_ActiveChildrenInfo\_GetCount()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_ActiveChildrenInfo_GetCount(ArkUI_ActiveChildrenInfo* handle)
```

**描述：**

获取[ArkUI\_ActiveChildrenInfo](capi-arkui-nativemodule-arkui-activechildreninfo.md)结构体内的节点数量。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ActiveChildrenInfo](capi-arkui-nativemodule-arkui-activechildreninfo.md)\* handle | 要获取信息的[ArkUI\_ActiveChildrenInfo](capi-arkui-nativemodule-arkui-activechildreninfo.md)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 子节点数量，默认值0. |

### OH\_ArkUI\_ProgressLinearStyleOption\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ProgressLinearStyleOption* OH_ArkUI_ProgressLinearStyleOption_Create(void)
```

**描述：**

创建线性进度条样式信息。

**起始版本：** 15

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ProgressLinearStyleOption](arkui-nativemodule-arkui-progresslinearstyleoption.md)\* | ProgressLinearStyleOption实例。  如果返回空指针，可能是因为内存不足。 |

### OH\_ArkUI\_ProgressLinearStyleOption\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ProgressLinearStyleOption_Destroy(ArkUI_ProgressLinearStyleOption* option)
```

**描述：**

销毁线性进度条样式信息。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ProgressLinearStyleOption](arkui-nativemodule-arkui-progresslinearstyleoption.md)\* option | 线性进度条样式信息。 |

### OH\_ArkUI\_ProgressLinearStyleOption\_SetSmoothEffectEnabled()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ProgressLinearStyleOption_SetSmoothEffectEnabled(ArkUI_ProgressLinearStyleOption* option, bool enabled)
```

**描述：**

设置进度平滑动效的开关。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ProgressLinearStyleOption](arkui-nativemodule-arkui-progresslinearstyleoption.md)\* option | 线性进度条样式信息。 |
| bool enabled | 进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值。  true：表示开启进度平滑动效。  false：表示关闭进度平滑动效。  默认值：true。 |

### OH\_ArkUI\_ProgressLinearStyleOption\_SetScanEffectEnabled()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ProgressLinearStyleOption_SetScanEffectEnabled(ArkUI_ProgressLinearStyleOption* option, bool enabled)
```

**描述：**

设置扫光效果的开关。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ProgressLinearStyleOption](arkui-nativemodule-arkui-progresslinearstyleoption.md)\* option | 线性进度条样式信息。 |
| bool enabled | 扫光效果的开关。  true：表示开启扫光效果。  false：表示关闭扫光效果。  默认值：false。 |

### OH\_ArkUI\_ProgressLinearStyleOption\_SetStrokeWidth()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ProgressLinearStyleOption_SetStrokeWidth(ArkUI_ProgressLinearStyleOption* option, float strokeWidth)
```

**描述：**

设置进度条宽度。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ProgressLinearStyleOption](arkui-nativemodule-arkui-progresslinearstyleoption.md)\* option | 线性进度条样式信息。 |
| float strokeWidth | 进度条宽度值（不支持百分比设置），单位为vp，默认值：4.0vp。 |

### OH\_ArkUI\_ProgressLinearStyleOption\_SetStrokeRadius()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ProgressLinearStyleOption_SetStrokeRadius(ArkUI_ProgressLinearStyleOption* option, float strokeRadius)
```

**描述：**

设置进度条圆角半径。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ProgressLinearStyleOption](arkui-nativemodule-arkui-progresslinearstyleoption.md)\* option | 线性进度条样式信息。 |
| float strokeRadius | 进度条圆角半径值，单位为vp，取值范围[0, strokeWidth/2]。默认值：strokeWidth/2。 |

### OH\_ArkUI\_ProgressLinearStyleOption\_GetSmoothEffectEnabled()

PhonePC/2in1TabletTVWearable

```
1. bool OH_ArkUI_ProgressLinearStyleOption_GetSmoothEffectEnabled(ArkUI_ProgressLinearStyleOption* option)
```

**描述：**

获取进度平滑动效的开关信息。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ProgressLinearStyleOption](arkui-nativemodule-arkui-progresslinearstyleoption.md)\* option | 线性进度条样式信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 是否开启平滑动效。  true：表示开启进度平滑动效。  false：表示关闭进度平滑动效。  默认值：true。 |

### OH\_ArkUI\_ProgressLinearStyleOption\_GetScanEffectEnabled()

PhonePC/2in1TabletTVWearable

```
1. bool OH_ArkUI_ProgressLinearStyleOption_GetScanEffectEnabled(ArkUI_ProgressLinearStyleOption* option)
```

**描述：**

获取扫光效果的开关信息。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ProgressLinearStyleOption](arkui-nativemodule-arkui-progresslinearstyleoption.md)\* option | 线性进度条样式信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 是否开启扫光效果。  true：表示开启扫光效果。  false：表示关闭扫光效果。  默认值：false。 |

### OH\_ArkUI\_ProgressLinearStyleOption\_GetStrokeWidth()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_ProgressLinearStyleOption_GetStrokeWidth(ArkUI_ProgressLinearStyleOption* option)
```

**描述：**

获取进度条宽度。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ProgressLinearStyleOption](arkui-nativemodule-arkui-progresslinearstyleoption.md)\* option | 线性进度条样式信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 进度条宽度值，单位为vp。 |

### OH\_ArkUI\_ProgressLinearStyleOption\_GetStrokeRadius()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_ProgressLinearStyleOption_GetStrokeRadius(ArkUI_ProgressLinearStyleOption* option)
```

**描述：**

获取进度条圆角半径值。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ProgressLinearStyleOption](arkui-nativemodule-arkui-progresslinearstyleoption.md)\* option | 线性进度条样式信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 进度条圆角半径值，单位为vp。 |

### OH\_ArkUI\_CreateSnapshotOptions()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_SnapshotOptions* OH_ArkUI_CreateSnapshotOptions()
```

**描述：**

创建一个截图选项，当返回值不再使用时必须通过[OH\_ArkUI\_DestroySnapshotOptions()](capi-native-type-h.md#oh_arkui_destroysnapshotoptions)释放。

**起始版本：** 15

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_SnapshotOptions](capi-arkui-nativemodule-arkui-snapshotoptions.md)\* | 返回指向创建的截图选项对象的指针。如果对象返回空指针，则表示创建失败，失败的原因可能是地址空间已满。 |

### OH\_ArkUI\_DestroySnapshotOptions()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_DestroySnapshotOptions(ArkUI_SnapshotOptions* snapshotOptions)
```

**描述：**

销毁截图选项指针。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SnapshotOptions](capi-arkui-nativemodule-arkui-snapshotoptions.md)\* snapshotOptions | 截图选项。 |

### OH\_ArkUI\_SnapshotOptions\_SetScale()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_SnapshotOptions_SetScale(ArkUI_SnapshotOptions* snapshotOptions, float scale)
```

**描述：**

配置截图选项中的缩放属性。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SnapshotOptions](capi-arkui-nativemodule-arkui-snapshotoptions.md)\* snapshotOptions | 截图选项。 |
| float scale | 缩放值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  异常原因：传入参数验证失败，参数不能为空。 |

### OH\_ArkUI\_SnapshotOptions\_SetColorMode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_SnapshotOptions_SetColorMode(ArkUI_SnapshotOptions* snapshotOptions, int32_t colorSpace, bool isAuto)
```

**描述：**

设置截图选项中的色彩空间。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SnapshotOptions](capi-arkui-nativemodule-arkui-snapshotoptions.md)\* snapshotOptions | 截图选项指针。 |
| int32\_t colorSpace | 指定截图使用的色彩空间。  如果知道需要截图的组件使用的色彩空间，可以通过colorSpace参数指定，并将isAuto设置为false，以达到预期的截图效果。  支持的取值为：3（RGB色域为Display P3类型）、4（RGB色域为SRGB类型）、27（RGB色域为DISPLAY BT2020类型）。  默认值：4  仅当isAuto设置为false，该参数设置生效。 |
| bool isAuto | 是否由系统自动决定所使用的色彩空间。  true表示系统自动决定所使用的色彩空间。在不确定组件使用的色彩空间时，建议将isAuto设置为true，让系统根据实际情况自动决定使用的色彩空间。  false表示使用通过colorSpace字段设置的色彩空间类型进行截图。  默认值：false |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SnapshotOptions\_SetDynamicRangeMode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_SnapshotOptions_SetDynamicRangeMode(ArkUI_SnapshotOptions* snapshotOptions, int32_t dynamicRangeMode, bool isAuto)
```

**描述：**

设置截图选项中的动态范围模式。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SnapshotOptions](capi-arkui-nativemodule-arkui-snapshotoptions.md)\* snapshotOptions | 截图选项指针。 |
| int32\_t dynamicRangeMode | 指定截图使用的动态范围模式。  如果知道截图对象使用的动态范围模式，可通过dynamicRangeMode参数指定动态范围模式，并将isAuto设置为false，以达到预期的截图效果。  支持的取值为：[ArkUI\_DynamicRangeMode](capi-native-type-h.md#arkui_dynamicrangemode)枚举值。  默认值：ARKUI\_DYNAMIC\_RANGE\_MODE\_STANDARD  仅当isAuto设置为false，该参数设置生效。 |
| bool isAuto | 是否由系统自动决定所使用的动态范围模式。  true表示系统自动决定所使用的动态范围模式。在不确定组件使用的动态范围模式时，建议将isAuto设置为true，让系统根据实际情况自动决定使用的动态范围模式。  false表示使用通过dynamicRangeMode字段设置的动态范围模式进行截图。  默认值：false |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CrossLanguageOption\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_CrossLanguageOption* OH_ArkUI_CrossLanguageOption_Create(void)
```

**描述：**

创建跨语言配置项实例。

**起始版本：** 15

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CrossLanguageOption](capi-arkui-nativemodule-arkui-crosslanguageoption.md)\* | 返回跨语言实例。如果对象返回空指针，则表示创建失败，失败的原因可能是地址空间已满。 |

### OH\_ArkUI\_CrossLanguageOption\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_CrossLanguageOption_Destroy(ArkUI_CrossLanguageOption* option)
```

**描述：**

销毁跨语言配置项实例。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CrossLanguageOption](capi-arkui-nativemodule-arkui-crosslanguageoption.md)\* option | 要销毁的跨语言配置项实例。 |

### OH\_ArkUI\_CrossLanguageOption\_SetAttributeSettingStatus()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_CrossLanguageOption_SetAttributeSettingStatus(ArkUI_CrossLanguageOption* option, bool enabled)
```

**描述：**

设置配置项中是否允许跨语言修改属性。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CrossLanguageOption](capi-arkui-nativemodule-arkui-crosslanguageoption.md)\* option | 跨语言配置项实例。 |
| bool enabled | 是否允许跨语言修改属性。true表示允许跨语言修改属性，false表示不允许跨语言修改属性，默认值：false。 |

### OH\_ArkUI\_CrossLanguageOption\_GetAttributeSettingStatus()

PhonePC/2in1TabletTVWearable

```
1. bool OH_ArkUI_CrossLanguageOption_GetAttributeSettingStatus(ArkUI_CrossLanguageOption* option)
```

**描述：**

获取配置项中是否允许跨语言修改属性。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CrossLanguageOption](capi-arkui-nativemodule-arkui-crosslanguageoption.md)\* option | 跨语言配置项实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 是否允许跨语言修改属性。true表示允许跨语言修改属性，false表示不允许跨语言修改属性。 |

### OH\_ArkUI\_VisibleAreaEventOptions\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_VisibleAreaEventOptions* OH_ArkUI_VisibleAreaEventOptions_Create()
```

**描述：**

创建可见区域变化监听的参数。

**起始版本：** 17

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_VisibleAreaEventOptions](i-arkui-nativemodule-arkui-visibleareaeventoptions.md)\* | 可见区域变化监听的参数。 |

### OH\_ArkUI\_VisibleAreaEventOptions\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_VisibleAreaEventOptions_Dispose(ArkUI_VisibleAreaEventOptions* option)
```

**描述：**

销毁可见区域变化监听的参数。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_VisibleAreaEventOptions](i-arkui-nativemodule-arkui-visibleareaeventoptions.md)\* option | 需要销毁的实例。 |

### OH\_ArkUI\_VisibleAreaEventOptions\_SetRatios()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_VisibleAreaEventOptions_SetRatios(ArkUI_VisibleAreaEventOptions* option, float* value, int32_t size)
```

**描述：**

设置阈值数组。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_VisibleAreaEventOptions](i-arkui-nativemodule-arkui-visibleareaeventoptions.md)\* option | 可见区域变化监听的参数实例。 |
| float\* value | 阈值数组。其中每个元素代表组件可见面积（即组件在屏幕显示区的面积，只计算父组件内的面积，超出父组件部分不会计算）与组件自身面积的比值。每个阈值的取值范围为[0.0, 1.0]，如果开发者设置的阈值超出该范围，则会实际取值0.0或1.0。 |
| int32\_t size | 阈值数组大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  异常原因：传入参数验证失败，参数不能为空。 |

### OH\_ArkUI\_VisibleAreaEventOptions\_SetExpectedUpdateInterval()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_VisibleAreaEventOptions_SetExpectedUpdateInterval(ArkUI_VisibleAreaEventOptions *option, int32_t value)
```

**描述：**

设置预期更新间隔，单位为ms。定义了开发者期望的更新间隔。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_VisibleAreaEventOptions](i-arkui-nativemodule-arkui-visibleareaeventoptions.md) \*option | 可见区域变化监听的参数实例。 |
| int32\_t value | 预期更新间隔，单位为ms。定义了开发者期望的更新间隔。默认值：1000。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  异常原因：传入参数验证失败，参数不能为空。 |

### OH\_ArkUI\_VisibleAreaEventOptions\_SetMeasureFromViewport()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_VisibleAreaEventOptions_SetMeasureFromViewport(ArkUI_VisibleAreaEventOptions* option, bool measureFromViewport)
```

**描述：**

设置可见区域计算模式。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_VisibleAreaEventOptions](i-arkui-nativemodule-arkui-visibleareaeventoptions.md)\* option | 可见区域变化监听的参数实例。 |
| bool measureFromViewport | 设置可见区域计算模式。  当measureFromViewport设置为true时，系统在计算该组件的可见区域时，会考虑父组件的NODE\_CLIP属性设置。如果父组件的NODE\_CLIP为false，则认为其内的子组件可以超出其区域进行显示，因此超出父组件的区域也将被视为可见区域纳入计算；如果父组件的NODE\_CLIP设置为true，则组件超出父组件的区域会被裁剪，无法显示，因此会被视为不可见区域进行计算。而当measureFromViewport设置为false时，则不考虑NODE\_CLIP的影响，直接将组件超出父组件的部分视为不可见区域。  默认值：false |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  异常原因：传入参数验证失败，参数不能为空。 |

### OH\_ArkUI\_VisibleAreaEventOptions\_GetRatios()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_VisibleAreaEventOptions_GetRatios(ArkUI_VisibleAreaEventOptions* option, float* value, int32_t* size)
```

**描述：**

获取阈值数组。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_VisibleAreaEventOptions](i-arkui-nativemodule-arkui-visibleareaeventoptions.md)\* option | 可见区域变化监听的参数实例。 |
| float\* value | 阈值数组。 |
| int32\_t\* size | 阈值数组大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-native-type-h.md#arkui_errorcode) 数组大小不够。  异常原因：传入参数验证失败，参数不能为空。 |

### OH\_ArkUI\_VisibleAreaEventOptions\_GetExpectedUpdateInterval()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_VisibleAreaEventOptions_GetExpectedUpdateInterval(ArkUI_VisibleAreaEventOptions* option)
```

**描述：**

获取预期更新间隔。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_VisibleAreaEventOptions](i-arkui-nativemodule-arkui-visibleareaeventoptions.md)\* option | 可见区域变化监听的参数实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 预期更新间隔，单位为ms。定义了开发者期望的更新间隔。默认值：1000。 |

### OH\_ArkUI\_VisibleAreaEventOptions\_GetMeasureFromViewport()

PhonePC/2in1TabletTVWearable

```
1. bool OH_ArkUI_VisibleAreaEventOptions_GetMeasureFromViewport(ArkUI_VisibleAreaEventOptions* option)
```

**描述：**

获取可见区域计算模式。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_VisibleAreaEventOptions](i-arkui-nativemodule-arkui-visibleareaeventoptions.md)\* option | 可见区域变化监听的参数实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 获取可见区域计算模式。  当measureFromViewport设置为true时，系统在计算该组件的可见区域时，会考虑父组件的NODE\_CLIP属性设置。如果父组件的NODE\_CLIP为false，则认为其内的子组件可以超出其区域进行显示，因此超出父组件的区域也将被视为可见区域纳入计算；如果父组件的NODE\_CLIP设置为true，则组件超出父组件的区域会被裁剪，无法显示，因此会被视为不可见区域进行计算。而当measureFromViewport设置为false时，则不考虑NODE\_CLIP的影响，直接将组件超出父组件的部分视为不可见区域。  默认值：false |

### OH\_ArkUI\_TextPickerRangeContentArray\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_TextPickerRangeContentArray* OH_ArkUI_TextPickerRangeContentArray_Create(int32_t length)
```

**描述：**

创建[TextPickerRangeContent](kui-nativemodule-arkui-textpickerrangecontentarray.md)数组的对象。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t length | 指定TextPickerRangeContent数组的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_TextPickerRangeContentArray](kui-nativemodule-arkui-textpickerrangecontentarray.md)\* | 返回指向TextPickerRangeContent空数组的指针。 |

### OH\_ArkUI\_TextPickerRangeContentArray\_SetIconAtIndex()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextPickerRangeContentArray_SetIconAtIndex(ArkUI_TextPickerRangeContentArray* handle, char* icon, int32_t index)
```

**描述：**

设置TextPickerRangeContent数组指定位置的icon数据。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextPickerRangeContentArray](kui-nativemodule-arkui-textpickerrangecontentarray.md)\* handle | 指向TextPickerRangeContent数组的指针。 |
| char\* icon | 图标路径。 |
| int32\_t index | 数组索引，从0开始。 |

### OH\_ArkUI\_TextPickerRangeContentArray\_SetTextAtIndex()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextPickerRangeContentArray_SetTextAtIndex(ArkUI_TextPickerRangeContentArray* handle, char* text, int32_t index)
```

**描述：**

设置TextPickerRangeContent数组指定位置的text数据。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextPickerRangeContentArray](kui-nativemodule-arkui-textpickerrangecontentarray.md)\* handle | 指向TextPickerRangeContent数组的指针。 |
| char\* text | 文本内容。 |
| int32\_t index | 数组位置，从0开始。 |

### OH\_ArkUI\_TextPickerRangeContentArray\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextPickerRangeContentArray_Destroy(ArkUI_TextPickerRangeContentArray* handle)
```

**描述：**

删除TextPickerRangeContent数组对象。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextPickerRangeContentArray](kui-nativemodule-arkui-textpickerrangecontentarray.md)\* handle | 指向TextPickerRangeContent数组的指针。 |

### OH\_ArkUI\_TextCascadePickerRangeContentArray\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_TextCascadePickerRangeContentArray* OH_ArkUI_TextCascadePickerRangeContentArray_Create(int32_t length)
```

**描述：**

创建[TextCascadePickerRangeContent](ivemodule-arkui-textcascadepickerrangecontentarray.md)数组对象。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t length | 指向TextPickerRangeContent数组的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_TextCascadePickerRangeContentArray](ivemodule-arkui-textcascadepickerrangecontentarray.md)\* | 返回指向TextCascadePickerRangeContent空数组的指针。 |

### OH\_ArkUI\_TextCascadePickerRangeContentArray\_SetTextAtIndex()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextCascadePickerRangeContentArray_SetTextAtIndex(ArkUI_TextCascadePickerRangeContentArray* handle, char* text, int32_t index)
```

**描述：**

设置TextCascadePickerRangeContent数组指定位置的text数据。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextCascadePickerRangeContentArray](ivemodule-arkui-textcascadepickerrangecontentarray.md)\* handle | 指向TextCascadePickerRangeContentHandle的指针。 |
| char\* text | 文本内容。 |
| int32\_t index | 数组位置，从0开始。 |

### OH\_ArkUI\_TextCascadePickerRangeContentArray\_SetChildAtIndex()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextCascadePickerRangeContentArray_SetChildAtIndex(ArkUI_TextCascadePickerRangeContentArray* handle, ArkUI_TextCascadePickerRangeContentArray* child, int32_t index)
```

**描述：**

设置TextCascadePickerRangeContent数组指定位置的child数据。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextCascadePickerRangeContentArray](ivemodule-arkui-textcascadepickerrangecontentarray.md)\* handle | 指向TextCascadePickerRangeContentHandle的指针。 |
| [ArkUI\_TextCascadePickerRangeContentArray](ivemodule-arkui-textcascadepickerrangecontentarray.md)\* child | 子节点数组指针。 |
| int32\_t index | 数组位置，从0开始。 |

### OH\_ArkUI\_TextCascadePickerRangeContentArray\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextCascadePickerRangeContentArray_Destroy(ArkUI_TextCascadePickerRangeContentArray* handle)
```

**描述：**

删除TextCascadePickerRangeContent数组对象。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextCascadePickerRangeContentArray](ivemodule-arkui-textcascadepickerrangecontentarray.md)\* handle | 指向TextCascadePickerRangeContentHandle的指针。 |

### OH\_ArkUI\_EmbeddedComponentOption\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_EmbeddedComponentOption* OH_ArkUI_EmbeddedComponentOption_Create()
```

**描述：**

创建EmbeddedComponent组件选项的对象。

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_EmbeddedComponentOption](i-arkui-nativemodule-arkui-embeddedcomponentoption.md)\* | 返回指向EmbeddedComponent组件选项的对象的指针。 |

### OH\_ArkUI\_EmbeddedComponentOption\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_EmbeddedComponentOption_Dispose(ArkUI_EmbeddedComponentOption* option)
```

**描述：**

删除EmbeddedComponent组件选项的对象。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_EmbeddedComponentOption](i-arkui-nativemodule-arkui-embeddedcomponentoption.md)\* option | 要销毁的EmbeddedComponent组件选项的对象的指针。 |

### OH\_ArkUI\_EmbeddedComponentOption\_SetOnError()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_EmbeddedComponentOption_SetOnError(ArkUI_EmbeddedComponentOption* option, void (*callback)(int32_t code, const char* name, const char* message))
```

**描述：**

设置EmbeddedComponent组件的[onError](ts-container-embedded-component.md#onerror)回调。EmbeddedComponent组件在运行过程中发生异常时触发本回调。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_EmbeddedComponentOption](i-arkui-nativemodule-arkui-embeddedcomponentoption.md)\* option | EmbeddedComponent组件选项的对象的指针。 |
| void (\*callback)(int32\_t code, const char\* name, const char\* message) | 开发者自定义回调函数。  - code：接口调用失败返回的错误码信息。错误码的详细介绍请参考[UIExtension错误码](errorcode-uiextension.md)。  - name：接口调用失败返回的名称信息。  - message：接口调用失败返回的详细信息。 |

### OH\_ArkUI\_EmbeddedComponentOption\_SetOnTerminated()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_EmbeddedComponentOption_SetOnTerminated(ArkUI_EmbeddedComponentOption* option, void (*callback)(int32_t code, AbilityBase_Want* want))
```

**描述：**

设置EmbeddedComponent组件的[onTerminated](ts-container-embedded-component.md#onterminated)回调。EmbeddedComponent组件正常退出时触发本回调。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_EmbeddedComponentOption](i-arkui-nativemodule-arkui-embeddedcomponentoption.md)\* option | EmbeddedComponent组件选项的对象的指针。 |
| void (\*callback)(int32\_t code, [AbilityBase\_Want](capi-arkui-nativemodule-abilitybase-want.md)\* want) | 开发者自定义回调函数。  - code：被拉起[EmbeddedUIExtensionAbility](js-apis-app-ability-embeddeduiextensionability.md)退出时返回的结果码。若EmbeddedUIExtensionAbility通过调用[terminateSelfWithResult](js-apis-app-ability-uiextensioncontentsession.md#terminateselfwithresult)退出，结果码为EmbeddedUIExtensionAbility设置的值。若EmbeddedUIExtensionAbility通过调用[terminateSelf](js-apis-app-ability-uiextensioncontentsession.md#terminateself)退出，结果码为默认值"0"。  - want：被拉起EmbeddedUIExtensionAbility退出时返回的数据。 |

### OH\_ArkUI\_PositionEdges\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_PositionEdges* OH_ArkUI_PositionEdges_Create()
```

**描述：**

创建PositionEdges属性对象。

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* | 指向PositionEdges对象的指针。 |

### OH\_ArkUI\_PositionEdges\_Copy()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_PositionEdges* OH_ArkUI_PositionEdges_Copy(const ArkUI_PositionEdges* edges)
```

**描述：**

深拷贝PositionEdges属性对象。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* edges | 指向PositionEdges对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* | 指向新PositionEdges对象的指针。 |

### OH\_ArkUI\_PositionEdges\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_PositionEdges_Dispose(ArkUI_PositionEdges* edges)
```

**描述：**

销毁PositionEdges属性对象。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* edges | 指向PositionEdges对象的指针。 |

### OH\_ArkUI\_PositionEdges\_SetTop()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_PositionEdges_SetTop(ArkUI_PositionEdges* edges, float value)
```

**描述：**

设置PositionEdges属性对象的上方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* edges | 指向PositionEdges对象的指针。 |
| float value | PositionEdges对应方向的值，单位vp。 |

### OH\_ArkUI\_PositionEdges\_GetTop()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_PositionEdges_GetTop(ArkUI_PositionEdges* edges, float* value)
```

**描述：**

获取PositionEdges属性对象的上方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* edges | 指向PositionEdges对象的指针。 |
| float\* value | PositionEdges对应方向的值，单位vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数无效。 |

### OH\_ArkUI\_PositionEdges\_SetLeft()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_PositionEdges_SetLeft(ArkUI_PositionEdges* edges, float value)
```

**描述：**

设置PositionEdges属性对象的左方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* edges | 指向PositionEdges对象的指针。 |
| float value | PositionEdges对应方向的值，单位vp。 |

### OH\_ArkUI\_PositionEdges\_GetLeft()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_PositionEdges_GetLeft(ArkUI_PositionEdges* edges, float* value)
```

**描述：**

获取PositionEdges属性对象的左方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* edges | 指向PositionEdges对象的指针。 |
| float\* value | PositionEdges对应方向的值，单位vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数无效。 |

### OH\_ArkUI\_PositionEdges\_SetBottom()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_PositionEdges_SetBottom(ArkUI_PositionEdges* edges, float value)
```

**描述：**

设置PositionEdges属性对象的下方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* edges | 指向PositionEdges对象的指针。 |
| float value | PositionEdges对应方向的值，单位vp。 |

### OH\_ArkUI\_PositionEdges\_GetBottom()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_PositionEdges_GetBottom(ArkUI_PositionEdges* edges, float* value)
```

**描述：**

获取PositionEdges属性对象的下方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* edges | 指向PositionEdges对象的指针。 |
| float\* value | PositionEdges对应方向的值，单位vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数无效。 |

### OH\_ArkUI\_PositionEdges\_SetRight()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_PositionEdges_SetRight(ArkUI_PositionEdges* edges, float value)
```

**描述：**

设置PositionEdges属性对象的右方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* edges | 指向PositionEdges对象的指针。 |
| float value | PositionEdges对应方向的值，单位vp。 |

### OH\_ArkUI\_PositionEdges\_GetRight()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_PositionEdges_GetRight(ArkUI_PositionEdges* edges, float* value)
```

**描述：**

获取PositionEdges属性对象的右方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)\* edges | 指向PositionEdges对象的指针。 |
| float\* value | PositionEdges对应方向的值，单位vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数无效。 |

### OH\_ArkUI\_PixelRoundPolicy\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_PixelRoundPolicy* OH_ArkUI_PixelRoundPolicy_Create()
```

**描述：**

创建PixelRoundPolicy属性对象。

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)\* | 指向PixelRoundPolicy对象的指针。 |

### OH\_ArkUI\_PixelRoundPolicy\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_PixelRoundPolicy_Dispose(ArkUI_PixelRoundPolicy* policy)
```

**描述：**

释放PixelRoundPolicy属性对象。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)\* policy | 指向要释放的PixelRoundPolicy对象的指针。 |

### OH\_ArkUI\_PixelRoundPolicy\_SetTop()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_PixelRoundPolicy_SetTop(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value)
```

**描述：**

设置PixelRoundPolicy属性对象的上部方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)\* policy | 指向PixelRoundPolicy对象的指针。 |
| [ArkUI\_PixelRoundCalcPolicy](capi-native-type-h.md#arkui_pixelroundcalcpolicy) value | PixelRoundPolicy对应方向的取整策略。 |

### OH\_ArkUI\_PixelRoundPolicy\_GetTop()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_PixelRoundPolicy_GetTop(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value)
```

**描述：**

获取PixelRoundPolicy属性对象的上部方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)\* policy | 指向PixelRoundPolicy对象的指针。 |
| [ArkUI\_PixelRoundCalcPolicy](capi-native-type-h.md#arkui_pixelroundcalcpolicy)\* value | PixelRoundPolicy对应方向的取整策略。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数无效。 |

### OH\_ArkUI\_PixelRoundPolicy\_SetStart()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_PixelRoundPolicy_SetStart(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value)
```

**描述：**

设置PixelRoundPolicy属性对象的前部方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)\* policy | 指向PixelRoundPolicy对象的指针。 |
| [ArkUI\_PixelRoundCalcPolicy](capi-native-type-h.md#arkui_pixelroundcalcpolicy) value | PixelRoundPolicy对应方向的取整策略。 |

### OH\_ArkUI\_PixelRoundPolicy\_GetStart()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_PixelRoundPolicy_GetStart(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value)
```

**描述：**

获取PixelRoundPolicy属性对象的前部方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)\* policy | 指向PixelRoundPolicy对象的指针。 |
| [ArkUI\_PixelRoundCalcPolicy](capi-native-type-h.md#arkui_pixelroundcalcpolicy)\* value | PixelRoundPolicy对应方向的取整策略。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数无效。 |

### OH\_ArkUI\_PixelRoundPolicy\_SetBottom()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_PixelRoundPolicy_SetBottom(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value)
```

**描述：**

设置PixelRoundPolicy属性对象的下部方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)\* policy | 指向PixelRoundPolicy对象的指针。 |
| [ArkUI\_PixelRoundCalcPolicy](capi-native-type-h.md#arkui_pixelroundcalcpolicy) value | PixelRoundPolicy对应方向的取整策略。 |

### OH\_ArkUI\_PixelRoundPolicy\_GetBottom()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_PixelRoundPolicy_GetBottom(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value)
```

**描述：**

获取PixelRoundPolicy属性对象的下部方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)\* policy | 指向PixelRoundPolicy对象的指针。 |
| [ArkUI\_PixelRoundCalcPolicy](capi-native-type-h.md#arkui_pixelroundcalcpolicy)\* value | PixelRoundPolicy对应方向的取整策略。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数无效。 |

### OH\_ArkUI\_PixelRoundPolicy\_SetEnd()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_PixelRoundPolicy_SetEnd(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy value)
```

**描述：**

设置PixelRoundPolicy属性对象的尾部方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)\* policy | 指向PixelRoundPolicy对象的指针。 |
| [ArkUI\_PixelRoundCalcPolicy](capi-native-type-h.md#arkui_pixelroundcalcpolicy) value | PixelRoundPolicy对应方向的取整策略。 |

### OH\_ArkUI\_PixelRoundPolicy\_GetEnd()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_PixelRoundPolicy_GetEnd(ArkUI_PixelRoundPolicy* policy, ArkUI_PixelRoundCalcPolicy* value)
```

**描述：**

获取PixelRoundPolicy属性对象的尾部方向值。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)\* policy | 指向PixelRoundPolicy对象的指针。 |
| [ArkUI\_PixelRoundCalcPolicy](capi-native-type-h.md#arkui_pixelroundcalcpolicy)\* value | PixelRoundPolicy对应方向的取整策略。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数无效。 |

### OH\_ArkUI\_ContentTransitionEffect\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ContentTransitionEffect* OH_ArkUI_ContentTransitionEffect_Create(int32_t type)
```

**描述：**

创建ContentTransitionEffect属性对象。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t type | 指定动效的转场方式。值为0表示无动效转场，值为1时表示淡入淡出动效转场。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ContentTransitionEffect](i-arkui-nativemodule-arkui-contenttransitioneffect.md)\* | 指向ContentTransitionEffect对象的指针。 |

### OH\_ArkUI\_GridLayoutOptions\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_GridLayoutOptions* OH_ArkUI_GridLayoutOptions_Create()
```

**描述：**

创建Grid布局选项。

**起始版本：** 22

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_GridLayoutOptions](capi-arkui-nativemodule-arkui-gridlayoutoptions.md)\* | Grid布局选项。 |

### OH\_ArkUI\_GridLayoutOptions\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_GridLayoutOptions_Dispose(ArkUI_GridLayoutOptions* option)
```

**描述：**

销毁Grid布局选项。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GridLayoutOptions](capi-arkui-nativemodule-arkui-gridlayoutoptions.md)\* option | Grid布局选项。 |

### OH\_ArkUI\_GridLayoutOptions\_SetIrregularIndexes()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_GridLayoutOptions_SetIrregularIndexes(ArkUI_GridLayoutOptions* option, uint32_t* irregularIndexes, int32_t size)
```

**描述：**

设置Grid中不规则GridItem的索引数组。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GridLayoutOptions](capi-arkui-nativemodule-arkui-gridlayoutoptions.md)\* option | Grid布局选项。 |
| uint32\_t\* irregularIndexes | GridItem索引数组。 |
| int32\_t size | GridItem索引数组大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  异常原因：传入参数验证失败，参数不能为空。 |

### OH\_ArkUI\_GridLayoutOptions\_GetIrregularIndexes()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_GridLayoutOptions_GetIrregularIndexes(ArkUI_GridLayoutOptions* option, uint32_t* irregularIndexes, int32_t* size)
```

**描述：**

获取Grid中不规则GridItem的索引数组。当不设置OH\_ArkUI\_GridLayoutOptions\_RegisterGetIrregularSizeByIndexCallback时，irregularIndexes中GridItem的默认大小为垂直滚动Grid的一整行或水平滚动Grid的一整列。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GridLayoutOptions](capi-arkui-nativemodule-arkui-gridlayoutoptions.md)\* option | Grid布局选项。 |
| uint32\_t\* irregularIndexes | GridItem索引数组。 |
| int32\_t size | GridItem索引数组大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-native-type-h.md#arkui_errorcode) 数组大小不够。  异常原因：传入参数验证失败，参数不能为空。 |

### OH\_ArkUI\_GridLayoutOptions\_RegisterGetIrregularSizeByIndexCallback()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_GridLayoutOptions_RegisterGetIrregularSizeByIndexCallback(ArkUI_GridLayoutOptions* option, void* userData, ArkUI_GridItemSize (*callback)(int32_t itemIndex, void* userData))
```

**描述：**

Grid布局选项通过GridItem索引获取指定Item占用的行列数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GridLayoutOptions](capi-arkui-nativemodule-arkui-gridlayoutoptions.md)\* option | Grid布局选项。 |
| void\* userData | 用户自定义数据。 |
| ArkUI\_GridItemSize (\*callback)(int32\_t itemIndex, void\* userData) | 根据index获取指定Item占用的行列数。  itemIndex：GridItem索引值，取值范围来自[OH\_ArkUI\_GridLayoutOptions\_SetIrregularIndexes](capi-native-type-h.md#oh_arkui_gridlayoutoptions_setirregularindexes)。 |

### OH\_ArkUI\_GridLayoutOptions\_RegisterGetRectByIndexCallback()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_GridLayoutOptions_RegisterGetRectByIndexCallback(ArkUI_GridLayoutOptions* option, void* userData, ArkUI_GridItemRect (*callback)(int32_t itemIndex, void* userData))
```

**描述：**

Grid布局选项通过GridItem索引获取指定Item的起始行列和占用的行列数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_GridLayoutOptions](capi-arkui-nativemodule-arkui-gridlayoutoptions.md)\* option | Grid布局选项。 |
| void\* userData | 用户自定义数据。 |
| ArkUI\_GridItemRect (\*callback)(int32\_t itemIndex, void\* userData) | 根据index获取指定Item的起始行列和占用的行列数。  itemIndex：GridItem索引值。 |

### OH\_ArkUI\_ShowCounterConfig\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ShowCounterConfig* OH_ArkUI_ShowCounterConfig_Create()
```

**描述：**

创建文本输入框计数器的配置对象。

**起始版本：** 22

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ShowCounterConfig](api-arkui-nativemodule-arkui-textshowcounterconfig.md)\* | 指向文本输入框计数器的配置对象的指针。 |

### OH\_ArkUI\_ShowCounterConfig\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ShowCounterConfig_Dispose(ArkUI_ShowCounterConfig* config)
```

**描述：**

销毁文本输入框计数器的配置对象。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ShowCounterConfig](api-arkui-nativemodule-arkui-textshowcounterconfig.md)\* config | 销毁文本输入框计数器的配置对象。 |

### OH\_ArkUI\_ShowCounterConfig\_SetCounterTextColor()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ShowCounterConfig_SetCounterTextColor(ArkUI_ShowCounterConfig* config, uint32_t color)
```

**描述：**

设置文本输入框未达到最大字符数时计数器的颜色。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ShowCounterConfig](api-arkui-nativemodule-arkui-textshowcounterconfig.md)\* config | 指向文本输入框计数器的配置对象指针。 |
| uint32\_t color | 文本输入框未达到最大字符数时计数器的颜色，格式为0xARGB。 |

### OH\_ArkUI\_ShowCounterConfig\_SetCounterTextOverflowColor()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_ShowCounterConfig_SetCounterTextOverflowColor(ArkUI_ShowCounterConfig* config, uint32_t color)
```

**描述：**

设置文本输入框超出最大字符数时计数器的颜色。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ShowCounterConfig](api-arkui-nativemodule-arkui-textshowcounterconfig.md)\* config | 指向文本输入框计数器的配置对象指针。 |
| uint32\_t color | 文本输入框超出最大字符数时计数器的颜色，格式为0xARGB。 |

### OH\_ArkUI\_ShowCounterConfig\_GetCounterTextColor()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_ArkUI_ShowCounterConfig_GetCounterTextColor(ArkUI_ShowCounterConfig* config)
```

**描述：**

获取文本输入框未达到最大字符数时计数器的颜色。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ShowCounterConfig](api-arkui-nativemodule-arkui-textshowcounterconfig.md)\* config | 指向文本输入框计数器的配置对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 返回文本输入框未达到最大字符数时计数器的颜色，格式为0xARGB，如果未通过[OH\_ArkUI\_ShowCounterConfig\_SetCounterTextColor](capi-native-type-h.md#oh_arkui_showcounterconfig_setcountertextcolor)接口设置计数器颜色，则返回0。 |

### OH\_ArkUI\_ShowCounterConfig\_GetCounterTextOverflowColor()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_ArkUI_ShowCounterConfig_GetCounterTextOverflowColor(ArkUI_ShowCounterConfig* config)
```

**描述：**

获取文本输入框超出最大字符数时计数器的颜色。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ShowCounterConfig](api-arkui-nativemodule-arkui-textshowcounterconfig.md)\* config | 指向文本输入框计数器的配置对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 返回文本输入框超出最大字符数时计数器的颜色，格式为0xARGB，如果未通过[OH\_ArkUI\_ShowCounterConfig\_SetCounterTextOverflowColor](capi-native-type-h.md#oh_arkui_showcounterconfig_setcountertextoverflowcolor)接口设置计数器颜色，则返回0。 |

### OH\_ArkUI\_SelectionOptions\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_SelectionOptions OH_ArkUI_SelectionOptions_Create()
```

**描述：**

创建选择选项。

**起始版本：** 23

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_SelectionOptions](capi-arkui-nativemodule-arkui-selectionoptions.md)\* | 指向选择选项对象的指针。 |

### OH\_ArkUI\_SelectionOptions\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SelectionOptions_Dispose(ArkUI_SelectionOptions* options)
```

**描述：**

释放选择选项对象。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SelectionOptions](capi-arkui-nativemodule-arkui-selectionoptions.md)\* options | 指向待释放的选择选项对象的指针。 |

### OH\_ArkUI\_SelectionOptions\_SetMenuPolicy()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SelectionOptions_SetMenuPolicy(ArkUI_SelectionOptions* options, ArkUI_MenuPolicy menuPolicy)
```

**描述：**

设置选择选项的菜单弹出策略。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SelectionOptions](capi-arkui-nativemodule-arkui-selectionoptions.md)\* options | 指向选择选项对象的指针。 |
| [ArkUI\_MenuPolicy](capi-native-type-h.md#arkui_menupolicy)  menuPolicy | 菜单弹出策略。 |

### OH\_ArkUI\_SelectionOptions\_GetMenuPolicy()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_MenuPolicy  OH_ArkUI_SelectionOptions_GetMenuPolicy(ArkUI_SelectionOptions* options)
```

**描述：**

获取选择选项的菜单弹出策略。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SelectionOptions](capi-arkui-nativemodule-arkui-selectionoptions.md)\* options | 指向选择选项对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_MenuPolicy](capi-native-type-h.md#arkui_menupolicy) | 菜单弹出策略。 |

### OH\_ArkUI\_TextContentBaseController\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_TextContentBaseController* OH_ArkUI_TextContentBaseController_Create()
```

**描述：**

创建文本内容基础控制器对象。

**起始版本：** 23

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_TextContentBaseController](arkui-nativemodule-arkui-textcontentbasecontroller.md)\* | 指向控制器对象的指针。 |

### OH\_ArkUI\_TextContentBaseController\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextContentBaseController_Dispose(ArkUI_TextContentBaseController* controller)
```

**描述：**

销毁文本内容基础控制器对象。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextContentBaseController](arkui-nativemodule-arkui-textcontentbasecontroller.md)\* controller | 待销毁的控制器对象指针。 |

### OH\_ArkUI\_TextContentBaseController\_DeleteBackward()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextContentBaseController_DeleteBackward(ArkUI_TextContentBaseController* controller)
```

**描述：**

在编辑态时删除光标前字符。其他状态删除输入框组件的最后一个字符。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextContentBaseController](arkui-nativemodule-arkui-textcontentbasecontroller.md)\* controller | 待修改的配置对象指针。 |

### OH\_ArkUI\_TextContentBaseController\_ScrollToVisible()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextContentBaseController_ScrollToVisible(ArkUI_TextContentBaseController* controller, int32_t start, int32_t end)
```

**描述：**

将起始索引与结束索引传递给与其绑定的输入框组件，并将此范围内的文字滚动到可视区域。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextContentBaseController](arkui-nativemodule-arkui-textcontentbasecontroller.md)\* controller | 待修改的配置对象指针。  通过此controller将起始索引与结束索引传递给与其绑定的输入框组件并进行滚动操作。 |
| int32\_t start | 起始文字索引值。  起始索引应小于等于结束索引，否则接口调用无效。取值范围[0, 输入框文本总长度]，起始索引小于0视为0，大于总长度视为总长度。 |
| int32\_t end | 结束文字索引值。  结束索引应大于等于起始索引，否则接口调用无效。取值范围[0, 输入框文本总长度]，结束索引小于0视为0，大于总长度视为总长度。 |

### OH\_ArkUI\_TextMenuItem\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_TextMenuItem* OH_ArkUI_TextMenuItem_Create()
```

**描述**

创建文本菜单项对象。

**起始版本：** 22

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_TextMenuItem](capi-arkui-nativemodule-arkui-textmenuitem.md)\* | 指向ArkUI\_TextMenuItem对象的指针。 |

### OH\_ArkUI\_TextMenuItem\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextMenuItem_Dispose(ArkUI_TextMenuItem* textMenuItem)
```

**描述**

释放文本菜单项对象。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMenuItem](capi-arkui-nativemodule-arkui-textmenuitem.md)\* textMenuItem | 指向ArkUI\_TextMenuItem对象的指针。 |

### OH\_ArkUI\_TextMenuItem\_SetContent()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextMenuItem_SetContent(ArkUI_TextMenuItem* item, const char* content)
```

**描述**

设置文本菜单项标题。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMenuItem](capi-arkui-nativemodule-arkui-textmenuitem.md)\* item | 指向ArkUI\_TextMenuItem对象的指针。 |
| const char\* content | 文本菜单项标题，默认为空字符串。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextMenuItem\_GetContent()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextMenuItem_GetContent(const ArkUI_TextMenuItem* item, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取文本菜单项标题。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_TextMenuItem](capi-arkui-nativemodule-arkui-textmenuitem.md)\* item | 指向ArkUI\_TextMenuItem对象的指针。 |
| char\* buffer | 缓冲区，由开发者创建分配内存，用于存储文本菜单项标题信息。 |
| int32\_t bufferSize | 缓冲区大小。 |
| int32\_t\* writeLength | 返回值为[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode)时表示实际写入缓冲区的长度。  返回值为[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-native-type-h.md#arkui_errorcode)时表示字符串完整写入缓冲区所需要的最小长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-native-type-h.md#arkui_errorcode) 缓冲区大小不足。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextMenuItem\_SetIcon()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextMenuItem_SetIcon(ArkUI_TextMenuItem* item, const char* icon)
```

**描述**

设置文本菜单项图标路径。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMenuItem](capi-arkui-nativemodule-arkui-textmenuitem.md)\* item | 指向ArkUI\_TextMenuItem对象的指针。 |
| const char\* icon | 文本菜单项图标路径，默认空字符串。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextMenuItem\_GetIcon()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextMenuItem_GetIcon(const ArkUI_TextMenuItem* item, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取文本菜单项图标路径。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_TextMenuItem](capi-arkui-nativemodule-arkui-textmenuitem.md)\* item | 指向ArkUI\_TextMenuItem对象的指针。 |
| char\* buffer | 缓冲区，由开发者创建分配内存，用于存储文本菜单项图标路径信息。 |
| int32\_t bufferSize | 缓冲区大小。 |
| int32\_t\* writeLength | 返回值为[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode)时表示实际写入缓冲区的长度。  返回值为[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-native-type-h.md#arkui_errorcode)时表示字符串完整写入缓冲区所需要的最小长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-native-type-h.md#arkui_errorcode) 缓冲区大小不足。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextMenuItem\_SetLabelInfo()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextMenuItem_SetLabelInfo(ArkUI_TextMenuItem* item, const char* labelInfo)
```

**描述**

设置文本菜单项快捷键提示，例如“复制”菜单项的快捷键提示可以设置为“Ctrl+C”。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMenuItem](capi-arkui-nativemodule-arkui-textmenuitem.md)\* item | 指向ArkUI\_TextMenuItem对象的指针。 |
| const char\* labelInfo | 文本菜单项快捷键提示，默认空字符串。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextMenuItem\_GetLabelInfo()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextMenuItem_GetLabelInfo(const ArkUI_TextMenuItem* item, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取文本菜单项快捷键提示，例如“复制”菜单项的快捷键提示一般为“Ctrl+C”。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_TextMenuItem](capi-arkui-nativemodule-arkui-textmenuitem.md)\* item | 指向ArkUI\_TextMenuItem对象的指针。 |
| char\* buffer | 缓冲区，由开发者创建分配内存，用于存储文本菜单项快捷键提示信息。 |
| int32\_t bufferSize | 缓冲区大小。 |
| int32\_t\* writeLength | 返回值为[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode)时表示实际写入缓冲区的长度。  返回值为[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-native-type-h.md#arkui_errorcode)时表示字符串完整写入缓冲区所需要的最小长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-native-type-h.md#arkui_errorcode) 缓冲区大小不足。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextMenuItem\_SetId()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextMenuItem_SetId(ArkUI_TextMenuItem* item, int32_t id)
```

**描述**

设置文本菜单项id。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMenuItem](capi-arkui-nativemodule-arkui-textmenuitem.md)\* item | 指向ArkUI\_TextMenuItem对象的指针。 |
| int32\_t id | 文本菜单项id。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextMenuItem\_GetId()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextMenuItem_GetId(const ArkUI_TextMenuItem* item, int32_t* id)
```

**描述**

获取文本菜单项id。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_TextMenuItem](capi-arkui-nativemodule-arkui-textmenuitem.md)\* item | 指向ArkUI\_TextMenuItem对象的指针。 |
| int32\_t\* id | 文本菜单项id。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextMenuItemArray\_GetSize()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_GetSize(ArkUI_TextMenuItemArray* items, int32_t* size)
```

**描述**

获取文本菜单项数组大小。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMenuItemArray](capi-arkui-nativemodule-arkui-textmenuitemarray.md)\* items | 指向ArkUI\_TextMenuItemArray对象的指针。 |
| int32\_t\* size | 文本菜单项数组大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextMenuItemArray\_GetItem()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_GetItem(ArkUI_TextMenuItemArray* items, int32_t index, ArkUI_TextMenuItem** item)
```

**描述**

获取文本菜单项数组中指定索引位置的文本菜单项。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMenuItemArray](capi-arkui-nativemodule-arkui-textmenuitemarray.md)\* items | 指向ArkUI\_TextMenuItemArray对象的指针。 |
| int32\_t index | 指定索引位置。 |
| [ArkUI\_TextMenuItem](capi-arkui-nativemodule-arkui-textmenuitem.md)\*\* item | 指向ArkUI\_TextMenuItem对象的二级指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextMenuItemArray\_Insert()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_Insert(ArkUI_TextMenuItemArray* items, ArkUI_TextMenuItem* item, int32_t index)
```

**描述**

在文本菜单项数组中指定索引位置插入一个文本菜单项。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMenuItemArray](capi-arkui-nativemodule-arkui-textmenuitemarray.md)\* items | 指向ArkUI\_TextMenuItemArray对象的指针。 |
| [ArkUI\_TextMenuItem](capi-arkui-nativemodule-arkui-textmenuitem.md)\* item | 指向ArkUI\_TextMenuItem对象的指针。 |
| int32\_t index | 要插入文本菜单项的索引位置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextMenuItemArray\_Erase()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_Erase(ArkUI_TextMenuItemArray* items, int32_t index)
```

**描述**

删除文本菜单项数组中指定索引位置的文本菜单项。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMenuItemArray](capi-arkui-nativemodule-arkui-textmenuitemarray.md)\* items | 指向ArkUI\_TextMenuItemArray对象的指针。 |
| int32\_t index | 要删除的文本菜单项索引位置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextMenuItemArray\_Clear()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_Clear(ArkUI_TextMenuItemArray* items)
```

**描述**

清除文本菜单项数组中所有的文本菜单项。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMenuItemArray](capi-arkui-nativemodule-arkui-textmenuitemarray.md)\* items | 指向ArkUI\_TextMenuItemArray对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextEditMenuOptions\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_TextEditMenuOptions* OH_ArkUI_TextEditMenuOptions_Create()
```

**描述**

创建文本菜单扩展项对象。

**起始版本：** 22

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_TextEditMenuOptions](capi-arkui-nativemodule-arkui-texteditmenuoptions.md)\* editMenuOptions | 指向ArkUI\_TextEditMenuOptions对象的指针。 |

### OH\_ArkUI\_TextEditMenuOptions\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextEditMenuOptions_Dispose(ArkUI_TextEditMenuOptions* editMenuOptions)
```

**描述**

释放文本菜单扩展项对象。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextEditMenuOptions](capi-arkui-nativemodule-arkui-texteditmenuoptions.md)\* editMenuOptions | 指向ArkUI\_TextEditMenuOptions对象的指针。 |

### ArkUI\_TextCreateMenuCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*ArkUI_TextCreateMenuCallback)(ArkUI_TextMenuItemArray* items, void* userData)
```

**描述**

文本菜单创建事件回调函数，在文本菜单创建时会触发此回调函数，开发者可在此函数中设置菜单数据。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMenuItemArray](capi-arkui-nativemodule-arkui-textmenuitemarray.md)\* items | 指向ArkUI\_TextMenuItemArray对象的指针，该数组对象由系统内部创建并释放，在回调函数中开发者可以调用[OH\_ArkUI\_TextMenuItemArray\_Insert](capi-native-type-h.md#oh_arkui_textmenuitemarray_insert)，[OH\_ArkUI\_TextMenuItemArray\_Erase](capi-native-type-h.md#oh_arkui_textmenuitemarray_erase)进行数组修改。 |
| void\* userData | 用户自定义数据。 |

### ArkUI\_TextPrepareMenuCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*ArkUI_TextPrepareMenuCallback)(ArkUI_TextMenuItemArray* items, void* userData)
```

**描述**

文本菜单准备事件回调函数，当文本选择区域变化后显示菜单之前会触发此回调函数，开发者可在此函数中配置菜单数据。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMenuItemArray](capi-arkui-nativemodule-arkui-textmenuitemarray.md)\* items | 指向ArkUI\_TextMenuItemArray对象的指针，该数组对象由系统内部创建并释放，在回调函数中开发者可以调用[OH\_ArkUI\_TextMenuItemArray\_Insert](capi-native-type-h.md#oh_arkui_textmenuitemarray_insert)，[OH\_ArkUI\_TextMenuItemArray\_Erase](capi-native-type-h.md#oh_arkui_textmenuitemarray_erase)进行数组修改。 |
| void\* userData | 用户自定义数据。 |

### ArkUI\_TextMenuItemClickCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef bool (*ArkUI_TextMenuItemClickCallback)(const ArkUI_TextMenuItem* item,int32_t start, int32_t end, void* userData)
```

**描述**

文本菜单项点击事件回调函数，在菜单项被点击时触发此回调函数，开发者可在此函数中对系统默认处理行为进行拦截。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_TextMenuItem](capi-arkui-nativemodule-arkui-textmenuitem.md)\* item | 指向ArkUI\_TextMenuItem对象的指针，表示被点击的文本菜单项。 |
| int32\_t start | 选中文本起始索引。 |
| int32\_t end | 选中文本结束索引。 |
| void\* userData | 用户自定义数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 是否拦截系统默认处理行为。  true：拦截系统默认处理行为，如点击“粘贴”、“复制”等文本菜单项时不再执行系统系统默认处理行为，仅执行开发者自定义处理行为。  false：不拦截系统默认处理行为，如点击“粘贴”、“复制”等文本菜单项时先执行开发者自定义处理行为，再执行系统默认处理行为。 |

### OH\_ArkUI\_TextEditMenuOptions\_RegisterOnCreateMenuCallback()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextEditMenuOptions_RegisterOnCreateMenuCallback(ArkUI_TextEditMenuOptions* editMenuOptions, void* userData, ArkUI_TextCreateMenuCallback cb)
```

**描述**

注册文本菜单创建事件回调函数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextEditMenuOptions](capi-arkui-nativemodule-arkui-texteditmenuoptions.md)\* editMenuOptions | 指向ArkUI\_TextEditMenuOptions对象的指针。 |
| void\* userData | 用户自定义数据。 |
| [ArkUI\_TextCreateMenuCallback](capi-native-type-h.md#arkui_textcreatemenucallback) cb | 文本菜单创建事件回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextEditMenuOptions\_RegisterOnPrepareMenuCallback()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextEditMenuOptions_RegisterOnPrepareMenuCallback(ArkUI_TextEditMenuOptions* editMenuOptions, void* userData, ArkUI_TextPrepareMenuCallback cb)
```

**描述**

注册文本菜单准备事件回调函数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextEditMenuOptions](capi-arkui-nativemodule-arkui-texteditmenuoptions.md)\* editMenuOptions | 指向ArkUI\_TextEditMenuOptions对象的指针。 |
| void\* userData | 用户自定义数据。 |
| [ArkUI\_TextPrepareMenuCallback](capi-native-type-h.md#arkui_textpreparemenucallback) cb | 文本菜单准备事件回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextEditMenuOptions\_RegisterOnMenuItemClickCallback()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextEditMenuOptions_RegisterOnMenuItemClickCallback(ArkUI_TextEditMenuOptions* editMenuOptions, void* userData, ArkUI_TextMenuItemClickCallback cb)
```

**描述**

注册文本菜单项点击事件回调函数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextEditMenuOptions](capi-arkui-nativemodule-arkui-texteditmenuoptions.md)\* editMenuOptions | 指向ArkUI\_TextEditMenuOptions对象的指针。 |
| void\* userData | 用户自定义数据。 |
| [ArkUI\_TextMenuItemClickCallback](capi-native-type-h.md#arkui_textmenuitemclickcallback) cb | 文本菜单项点击事件回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextSelectionMenuOptions\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_TextSelectionMenuOptions* OH_ArkUI_TextSelectionMenuOptions_Create();
```

**描述**

创建自定义文本选择菜单对象。

**起始版本：** 22

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_TextSelectionMenuOptions](-arkui-nativemodule-arkui-textselectionmenuoptions.md)\* | 指向ArkUI\_TextSelectionMenuOptions对象的指针。 |

### OH\_ArkUI\_TextSelectionMenuOptions\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextSelectionMenuOptions_Dispose(ArkUI_TextSelectionMenuOptions* selectionMenuOptions)
```

**描述**

释放自定义文本选择菜单对象。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextSelectionMenuOptions](-arkui-nativemodule-arkui-textselectionmenuoptions.md)\* selectionMenuOptions | 指向ArkUI\_TextSelectionMenuOptions对象的指针。 |

### OH\_ArkUI\_TextSelectionMenuOptions\_SetSpanType()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_SetSpanType(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_TextSpanType textSpanType)
```

**描述**

设置自定义文本选择菜单的文本识别类型。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextSelectionMenuOptions](-arkui-nativemodule-arkui-textselectionmenuoptions.md)\* selectionMenuOptions | 指向ArkUI\_TextSelectionMenuOptions对象的指针。 |
| [ArkUI\_TextSpanType](capi-native-type-h.md#arkui_textspantype) textSpanType | 自定义文本选择菜单的文本识别类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextSelectionMenuOptions\_GetSpanType()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_GetSpanType(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_TextSpanType* spanType)
```

**描述**

获取自定义文本选择菜单的文本识别类型。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextSelectionMenuOptions](-arkui-nativemodule-arkui-textselectionmenuoptions.md)\* selectionMenuOptions | 指向ArkUI\_TextSelectionMenuOptions对象的指针。 |
| [ArkUI\_TextSpanType](capi-native-type-h.md#arkui_textspantype)\* spanType | 自定义文本选择菜单的文本识别类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextSelectionMenuOptions\_SetContentNode()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_SetContentNode(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_NodeHandle node)
```

**描述**

设置自定义文本选择菜单的内容节点。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextSelectionMenuOptions](-arkui-nativemodule-arkui-textselectionmenuoptions.md)\* selectionMenuOptions | 指向ArkUI\_TextSelectionMenuOptions对象的指针。 |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 自定义文本选择菜单的内容节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextSelectionMenuOptions\_GetContentNode()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_GetContentNode(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_NodeHandle* node)
```

**描述**

获取自定义文本选择菜单的内容节点。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextSelectionMenuOptions](-arkui-nativemodule-arkui-textselectionmenuoptions.md)\* selectionMenuOptions | 指向ArkUI\_TextSelectionMenuOptions对象的指针。 |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)\* node | 自定义文本选择菜单的内容节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextSelectionMenuOptions\_SetResponseType()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_SetResponseType(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_TextResponseType responseType)
```

**描述**

设置自定义文本选择菜单的响应类型。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextSelectionMenuOptions](-arkui-nativemodule-arkui-textselectionmenuoptions.md)\* selectionMenuOptions | 指向ArkUI\_TextSelectionMenuOptions对象的指针。 |
| [ArkUI\_TextResponseType](capi-native-type-h.md#arkui_textresponsetype) responseType | 自定义文本选择菜单的响应类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextSelectionMenuOptions\_GetResponseType()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_GetResponseType(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_TextResponseType* responseType)
```

**描述**

获取自定义文本选择菜单的响应类型。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextSelectionMenuOptions](-arkui-nativemodule-arkui-textselectionmenuoptions.md)\* selectionMenuOptions | 指向ArkUI\_TextSelectionMenuOptions对象的指针。 |
| [ArkUI\_TextResponseType](capi-native-type-h.md#arkui_textresponsetype)\* responseType | 自定义文本选择菜单的响应类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextSelectionMenuOptions\_RegisterOnMenuShowCallback()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_RegisterOnMenuShowCallback(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, void* userData, void (*callback)(int32_t start, int32_t end, void* userData))
```

**描述**

注册自定义文本选择菜单显示事件回调。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextSelectionMenuOptions](-arkui-nativemodule-arkui-textselectionmenuoptions.md)\* selectionMenuOptions | 指向ArkUI\_TextSelectionMenuOptions对象的指针。 |
| void\* userData | 用户自定义数据，取任意值。设置后，会通过callback回调回传回来。 |
| void (\*callback)(int32\_t start, int32\_t end, void\* userData) | 自定义文本选择菜单显示事件回调。  start：选中文本的起始位置。  end：选中文本的结束位置。  userData：用户自定义数据，对应OH\_ArkUI\_TextSelectionMenuOptions\_RegisterOnMenuShowCallback接口的入参userData。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextSelectionMenuOptions\_RegisterOnMenuHideCallback()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_RegisterOnMenuHideCallback(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, void* userData, void (*callback)(int32_t start, int32_t end, void* userData))
```

**描述**

注册自定义文本选择菜单隐藏事件回调。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextSelectionMenuOptions](-arkui-nativemodule-arkui-textselectionmenuoptions.md)\* selectionMenuOptions | 指向ArkUI\_TextSelectionMenuOptions对象的指针。 |
| void\* userData | 用户自定义数据，取任意值。设置后，会通过callback回调回传回来。 |
| void (\*callback)(int32\_t start, int32\_t end, void\* userData) | 自定义文本选择菜单隐藏事件回调。  start：选中文本的起始位置。  end：选中文本的结束位置。  userData：用户自定义数据，对应OH\_ArkUI\_TextSelectionMenuOptions\_RegisterOnMenuHideCallback接口的入参userData。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextMarqueeOptions\_Create

PhonePC/2in1TabletTVWearable

```
1. ArkUI_TextMarqueeOptions* OH_ArkUI_TextMarqueeOptions_Create()
```

**描述：**

创建文本跑马灯模式配置项。

**起始版本：** 23

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* | 创建文本跑马灯模式配置项的对象指针。 |

### OH\_ArkUI\_TextMarqueeOptions\_Dispose

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextMarqueeOptions_Dispose(ArkUI_TextMarqueeOptions* option)
```

**描述：**

销毁文本跑马灯模式配置项指针。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 需要销毁的文本跑马灯模式配置项对象指针。 |

### OH\_ArkUI\_TextMarqueeOptions\_SetStart

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextMarqueeOptions_SetStart(ArkUI_TextMarqueeOptions* option, bool start)
```

**描述：**

设置文本跑马灯模式配置项是否播放。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |
| bool start | 是否播放。true表示播放，false表示不播放。 |

### OH\_ArkUI\_TextMarqueeOptions\_GetStart

PhonePC/2in1TabletTVWearable

```
1. bool OH_ArkUI_TextMarqueeOptions_GetStart(ArkUI_TextMarqueeOptions* option)
```

**描述：**

获取文本跑马灯模式配置项是否播放。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 是否播放。true表示播放，false表示不播放。 |

### OH\_ArkUI\_TextMarqueeOptions\_SetStep

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextMarqueeOptions_SetStep(ArkUI_TextMarqueeOptions* option, float step)
```

**描述：**

设置文本跑马灯模式配置项的步长。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |
| float step | 步长。单位：vp。 |

### OH\_ArkUI\_TextMarqueeOptions\_GetStep

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_TextMarqueeOptions_GetStep(ArkUI_TextMarqueeOptions* option)
```

**描述：**

获取文本跑马灯模式配置项的步长。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 步长。单位：vp。 |

### OH\_ArkUI\_TextMarqueeOptions\_SetSpacing

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextMarqueeOptions_SetSpacing(ArkUI_TextMarqueeOptions* option, float spacing)
```

**描述：**

设置文本跑马灯模式配置项的首尾间距。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |
| float spacing | 首尾间距。单位：vp。 |

### OH\_ArkUI\_TextMarqueeOptions\_GetSpacing

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_TextMarqueeOptions_GetSpacing(ArkUI_TextMarqueeOptions* option)
```

**描述：**

获取文本跑马灯模式配置项的首尾间距。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 首尾间距。单位：vp。 |

### OH\_ArkUI\_TextMarqueeOptions\_SetLoop

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextMarqueeOptions_SetLoop(ArkUI_TextMarqueeOptions* option, int32_t loop)
```

**描述：**

设置文本跑马灯模式配置项的重复滚动的次数，小于等于零时无限循环。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |
| int32\_t loop | 设置的重复滚动的次数。 |

### OH\_ArkUI\_TextMarqueeOptions\_GetLoop

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_TextMarqueeOptions_GetLoop(ArkUI_TextMarqueeOptions* option)
```

**描述：**

获取文本跑马灯模式配置项的重复滚动的次数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 重复滚动的次数。 |

### OH\_ArkUI\_TextMarqueeOptions\_SetFromStart

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextMarqueeOptions_SetFromStart(ArkUI_TextMarqueeOptions* option, bool fromStart)
```

**描述：**

设置文本跑马灯模式配置项的运行方向。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |
| bool fromStart | 跑马灯运行方向。true表示从头开始滚动，false表示反向滚动。 |

### OH\_ArkUI\_TextMarqueeOptions\_GetFromStart

PhonePC/2in1TabletTVWearable

```
1. bool OH_ArkUI_TextMarqueeOptions_GetFromStart(ArkUI_TextMarqueeOptions* option)
```

**描述：**

获取文本跑马灯模式配置项的运行方向。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 跑马灯运行方向。true表示从头开始滚动，false表示反向滚动。 |

### OH\_ArkUI\_TextMarqueeOptions\_SetDelay

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextMarqueeOptions_SetDelay(ArkUI_TextMarqueeOptions* option, int32_t delay)
```

**描述：**

设置文本跑马灯模式配置项的每轮滚动延迟时间。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |
| int32\_t delay | 每轮滚动延迟时间，单位为毫秒。 |

### OH\_ArkUI\_TextMarqueeOptions\_GetDelay

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_TextMarqueeOptions_GetDelay(ArkUI_TextMarqueeOptions* option)
```

**描述：**

获取文本跑马灯模式配置项的每轮滚动延迟时间。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回每轮滚动延迟时间，单位为毫秒。 |

### OH\_ArkUI\_TextMarqueeOptions\_SetFadeout

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextMarqueeOptions_SetFadeout(ArkUI_TextMarqueeOptions* option, bool fadeout)
```

**描述：**

设置文本跑马灯模式配置项是否支持文字超长时的渐隐效果。当Text内容超出显示范围时，未完全展现的文字边缘将应用渐隐效果。

若两端均有文字未完全显示，则两端同时应用渐隐效果。

在渐隐效果开启状态下，[NODE\_CLIP](capi-native-node-h.md#arkui_nodeattributetype)属性将自动锁定为true，不允许设置为false。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |
| bool fadeout | 跑马灯是否支持文字超长时的渐隐效果。  true表示支持渐隐效果，false表示不支持渐隐效果。 |

### OH\_ArkUI\_TextMarqueeOptions\_GetFadeout

PhonePC/2in1TabletTVWearable

```
1. bool OH_ArkUI_TextMarqueeOptions_GetFadeout(ArkUI_TextMarqueeOptions* option)
```

**描述：**

获取文本跑马灯模式配置项是否支持文字超长时的渐隐效果。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 是否支持文字超长时的渐隐效果。 |

### OH\_ArkUI\_TextMarqueeOptions\_SetStartPolicy

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextMarqueeOptions_SetStartPolicy(ArkUI_TextMarqueeOptions* option, ArkUI_MarqueeStartPolicy startPolicy)
```

**描述：**

设置文本跑马灯模式配置项的启动策略。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |
| [ArkUI\_MarqueeStartPolicy](capi-native-type-h.md#arkui_marqueestartpolicy) startPolicy | 启动策略。 |

### OH\_ArkUI\_TextMarqueeOptions\_GetStartPolicy

PhonePC/2in1TabletTVWearable

```
1. ArkUI_MarqueeStartPolicy OH_ArkUI_TextMarqueeOptions_GetStartPolicy(ArkUI_TextMarqueeOptions* option)
```

**描述：**

获取文本跑马灯模式配置项的启动策略。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI\_MarqueeStartPolicy | 启动策略。 |

### OH\_ArkUI\_TextMarqueeOptions\_SetUpdatePolicy

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_TextMarqueeOptions_SetUpdatePolicy(ArkUI_TextMarqueeOptions* option,
2. ArkUI_MarqueeUpdatePolicy updatePolicy)
```

**描述：**

设置文本跑马灯模式配置项的更新策略。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |
| [ArkUI\_MarqueeUpdatePolicy](capi-native-type-h.md#arkui_marqueeupdatepolicy) updatePolicy | 更新策略。 |

### OH\_ArkUI\_TextMarqueeOptions\_GetUpdatePolicy

PhonePC/2in1TabletTVWearable

```
1. ArkUI_MarqueeUpdatePolicy OH_ArkUI_TextMarqueeOptions_GetUpdatePolicy(ArkUI_TextMarqueeOptions* option)
```

**描述：**

获取文本跑马灯模式配置项的更新策略。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)\* option | 文本跑马灯模式配置项。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_MarqueeUpdatePolicy](capi-native-type-h.md#arkui_marqueeupdatepolicy) | 更新策略。 |

### OH\_ArkUI\_SelectedDragPreviewStyle\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_SelectedDragPreviewStyle* OH_ArkUI_SelectedDragPreviewStyle_Create();
```

**描述**

创建选中状态下拖拽文本预览样式对象。

**起始版本：** 23

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_SelectedDragPreviewStyle](ui-nativemodule-arkui-textselecteddragpreviewstyle.md)\* | 指向ArkUI\_SelectedDragPreviewStyle对象的指针。 |

### OH\_ArkUI\_SelectedDragPreviewStyle\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SelectedDragPreviewStyle_Dispose(ArkUI_SelectedDragPreviewStyle* config)
```

**描述**

销毁选中状态下拖拽文本预览样式对象。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SelectedDragPreviewStyle](ui-nativemodule-arkui-textselecteddragpreviewstyle.md)\* config | 指向ArkUI\_SelectedDragPreviewStyle对象的指针。 |

### OH\_ArkUI\_SelectedDragPreviewStyle\_SetColor()

PhonePC/2in1TabletTVWearable

```
1. void  OH_ArkUI_SelectedDragPreviewStyle_SetColor(ArkUI_SelectedDragPreviewStyle* config, uint32_t color);
```

**描述**

设置选中态拖拽文本预览样式的背景色。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SelectedDragPreviewStyle](ui-nativemodule-arkui-textselecteddragpreviewstyle.md)\* config | 指向ArkUI\_SelectedDragPreviewStyle对象的指针。 |
| uint32\_t color | 选中态拖拽文本预览样式的的背景，格式为RGBA。 |

### OH\_ArkUI\_SelectedDragPreviewStyle\_GetColor()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_ArkUI_SelectedDragPreviewStyle_GetColor(ArkUI_SelectedDragPreviewStyle* config)
```

**描述**

获取选中态拖拽文本预览样式的背景色。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_SelectedDragPreviewStyle](ui-nativemodule-arkui-textselecteddragpreviewstyle.md)\* config | 指向ArkUI\_SelectedDragPreviewStyle对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t color | 选中态拖拽文本预览样式的的背景，格式为RGBA。 |

### OH\_ArkUI\_MotionPathOptions\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_MotionPathOptions* OH_ArkUI_MotionPathOptions_Create()
```

**描述：**

创建路径动画的运动路径配置项。

**起始版本：** 23

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)\* | 指向路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)的指针。  新建的[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)对象中，路径动画的运动路径path值为空字符串，路径动画起点进度from值为0，路径动画终点进度to值为1，组件是否沿路径旋转rotatable值为false。 |

### OH\_ArkUI\_MotionPathOptions\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_MotionPathOptions_Dispose(ArkUI_MotionPathOptions* options)
```

**描述：**

销毁路径动画的运动路径配置项。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)\* options | 指向路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)的指针。 |

### OH\_ArkUI\_MotionPathOptions\_SetPath()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_SetPath(ArkUI_MotionPathOptions* options, const char* svgPath)
```

**描述：**

设置路径动画的运动路径。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)\* options | 指向路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)的指针。 |
| const char\* svgPath | 路径动画的运动路径字符串。  该路径支持使用"start"和"end"作为起点和终点的占位符，例如："Mstart.x start.y L50 50 Lend.x end.y Z"。路径字符串格式请参考[绘制路径](../harmonyos-guides/ui-js-components-svg-path.md)。若设置为空字符串，等效于未设置路径动画。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_MotionPathOptions\_GetPath()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_GetPath(const ArkUI_MotionPathOptions* options, char* svgPathBuffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述：**

获取路径动画的运动路径配置项中存储的运动路径字符串。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)\* options | 指向路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)的指针。 |
| char\* svgPathBuffer | 存储运动路径字符串的缓冲区指针。 |
| const int32\_t bufferSize | svgPathBuffer参数的缓冲区大小。 |
| int32\_t\* writeLength | 返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode)时，表示实际写入缓冲区的字符串长度。  返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode)时，表示如果为入参异常，writeLength不会被赋值，如果为拷贝异常，writeLength为可容纳目标字符串的最小缓冲区大小。  返回[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-native-type-h.md#arkui_errorcode)时，表示可容纳目标字符串的最小缓冲区大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-native-type-h.md#arkui_errorcode) 缓冲区大小不足。 |

### OH\_ArkUI\_MotionPathOptions\_SetFrom()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_SetFrom(ArkUI_MotionPathOptions* options, const float from)
```

**描述：**

设置路径动画起点进度。进度指已移动路径长度与总路径长度的比值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)\* options | 指向路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)的指针。 |
| const float from | 路径动画的起点进度，取值范围为[0.0, 1.0]，且需满足from小于或等于终点进度to，否则将返回[ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-native-type-h.md#arkui_errorcode)错误码。  to的含义参考[OH\_ArkUI\_MotionPathOptions\_SetTo](capi-native-type-h.md#oh_arkui_motionpathoptions_setto)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-native-type-h.md#arkui_errorcode) from超出[0.0, 1.0]范围，或from大于终点进度to。 |

### OH\_ArkUI\_MotionPathOptions\_GetFrom()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_GetFrom(const ArkUI_MotionPathOptions* options, float* from)
```

**描述：**

获取路径动画的运动路径配置项中的路径动画起点进度。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)\* options | 指向路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)的指针。 |
| float\* from | 用于接收路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)中起点进度值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_MotionPathOptions\_SetTo()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_SetTo(ArkUI_MotionPathOptions* options, const float to)
```

**描述：**

设置路径动画终点进度。进度指已移动路径长度与总路径长度的比值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)\* options | 指向路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)的指针。 |
| const float to | 路径动画的终点进度，取值范围为[0.0, 1.0]，且需满足to大或等于起点进度from；否则将返回[ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-native-type-h.md#arkui_errorcode)错误码。  from的含义参考[OH\_ArkUI\_MotionPathOptions\_SetFrom](capi-native-type-h.md#oh_arkui_motionpathoptions_setfrom)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-native-type-h.md#arkui_errorcode) to超出[0.0, 1.0]范围，或to小于起点进度from。 |

### OH\_ArkUI\_MotionPathOptions\_GetTo()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_GetTo(const ArkUI_MotionPathOptions* options, float* to)
```

**描述：**

获取路径动画的运动路径配置项中的路径动画终点进度。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)\* options | 指向路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)的指针。 |
| float\* to | 用于接收路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)中终点进度值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_MotionPathOptions\_SetRotatable()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_SetRotatable(ArkUI_MotionPathOptions* options, const bool rotatable)
```

**描述：**

设置组件是否沿运动路径旋转。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)\* options | 指向路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)的指针。 |
| const bool rotatable | 组件是否沿路径旋转。true表示组件沿路径旋转；false表示组件不沿路径旋转。默认值：false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_MotionPathOptions\_GetRotatable()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_GetRotatable(const ArkUI_MotionPathOptions* options, bool* rotatable)
```

**描述：**

获取组件是否沿运动路径旋转。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)\* options | 指向路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)的指针。 |
| bool\* rotatable | 用于接收路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)中rotatable参数值的指针，表示组件是否沿路径旋转。  true表示组件沿路径旋转；false表示组件不沿路径旋转。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_PickerIndicatorStyle\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_PickerIndicatorStyle* OH_ArkUI_PickerIndicatorStyle_Create(ArkUI_PickerIndicatorType type)
```

**描述**

创建选中项指示器的样式实例。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PickerIndicatorType](capi-native-type-h.md#arkui_pickerindicatortype) type | 选择器选中项样式枚举类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_PickerIndicatorStyle](capi-arkui-nativemodule-arkui-pickerindicatorstyle.md)\* | [ArkUI\_PickerIndicatorStyle](capi-arkui-nativemodule-arkui-pickerindicatorstyle.md)实例。如果返回空指针，表示创建失败，失败原因可是地址空间已满或类型不支持。 |

### OH\_ArkUI\_PickerIndicatorStyle\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_PickerIndicatorStyle_Dispose(ArkUI_PickerIndicatorStyle* style)
```

**描述**

销毁选中项指示器的样式实例。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PickerIndicatorStyle](capi-arkui-nativemodule-arkui-pickerindicatorstyle.md)\* style | 要销毁的[ArkUI\_PickerIndicatorStyle](capi-arkui-nativemodule-arkui-pickerindicatorstyle.md)实例。 |

### OH\_ArkUI\_PickerIndicatorStyle\_ConfigureBackground()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_PickerIndicatorStyle_ConfigureBackground(ArkUI_PickerIndicatorStyle* style, ArkUI_PickerIndicatorBackground* background)
```

**描述**

设置背景样式参数，此接口仅当选择器选中项样式枚举类型为[ARKUI\_PICKER\_INDICATOR\_BACKGROUND](capi-native-type-h.md#arkui_pickerindicatortype)时生效。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PickerIndicatorStyle](capi-arkui-nativemodule-arkui-pickerindicatorstyle.md)\* style | 选中项指示器样式[ArkUI\_PickerIndicatorStyle](capi-arkui-nativemodule-arkui-pickerindicatorstyle.md)的实例。 |
| [ArkUI\_PickerIndicatorBackground](arkui-nativemodule-arkui-pickerindicatorbackground.md)\* background | 背景样式参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_PickerIndicatorStyle\_ConfigureDivider()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_PickerIndicatorStyle_ConfigureDivider(ArkUI_PickerIndicatorStyle* style, ArkUI_PickerIndicatorDivider* divider)
```

**描述**

设置分割线样式参数，此接口仅当选择器选中项样式枚举类型为[ARKUI\_PICKER\_INDICATOR\_DIVIDER](capi-native-type-h.md#arkui_pickerindicatortype)时生效。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PickerIndicatorStyle](capi-arkui-nativemodule-arkui-pickerindicatorstyle.md)\* style | 选中项指示器样式[ArkUI\_PickerIndicatorStyle](capi-arkui-nativemodule-arkui-pickerindicatorstyle.md)的实例。 |
| [ArkUI\_PickerIndicatorDivider](pi-arkui-nativemodule-arkui-pickerindicatordivider.md)\* divider | 分割线样式参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |
