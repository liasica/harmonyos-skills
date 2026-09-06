---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-immersive-light-sense-component-adaptation
title: 组件适配沉浸光感
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 沉浸光感 > 沉浸光感开发指导 > 组件适配沉浸光感
category: harmonyos-guides
scraped_at: 2026-09-07T06:01:32+08:00
doc_updated_at: 2026-09-06
content_hash: sha256:46b74ad95aa013ef8b40e99a36c405750f8347201aed36ddd16a85cd0d222666
---

本文按导航类、弹窗类、按钮与选择类、其余组件四大场景分类，系统介绍各组件如何通过应用级开关与组件级配置开启沉浸光感，涵盖沉浸光感的视觉效果、设置方法及适配要点，帮助开发者快速完成沉浸光感的组件适配。

## 导航类组件

导航类组件包括Navigation标题栏、底部页签、索引条，是页面导航与内容定位的辅助元素，通常固定在页面顶部或底部。沉浸光感为导航类组件赋予了通透的悬浮质感，让导航栏在滚动内容之上呈现轻盈的分层效果，内容透过材质层自然渗透，建立导航区域与内容之间的视觉层次。导航类组件通常使用较薄的材质样式（ULTRA\_THIN或THIN），在保持背景通透的同时避免过度遮挡内容。

### Navigation标题栏

Navigation标题栏支持通过应用级开启、组件级开启方式开启沉浸光感。

应用级开启：应用级开关处于[ENABLE](../harmonyos-references/arkts-apis-uimaterial.md#materialstate)模式下，Navigation标题栏默认开启沉浸光感，沉浸式系统材质样式默认取值为ULTRA\_THIN；在非ENABLE模式下，沉浸光感不生效。

组件级开启：Navigation标题栏支持通过[NavigationTitleOptions](../harmonyos-references/ts-basic-components-navigation.md#navigationtitleoptions11)中的systemMaterial字段设置沉浸光感效果。

* 推荐将沉浸光感限定在顶部标题栏等需要凸显的局部区域，控制使用面积与层数，详见[沉浸光感功耗优化](arkts-immersive-light-sense-constraints.md)。
* 沉浸光感针对标题栏生效的范围是：返回键、非自定义Menu。
* systemMaterial为undefined时，[MaterialState](../harmonyos-references/arkts-apis-uimaterial.md#materialstate)开关配置为DEFAULT时标题栏无材质效果；配置为ENABLE时标题栏生效系统默认的沉浸式材质效果。
* 建议设置沉浸光感时，使用[barStyle](../harmonyos-references/ts-basic-components-navigation.md#navigationtitleoptions11)为STACK样式，以便Navigation内容区延伸至标题栏区域，获得沉浸光感的最佳体验。

组件开启沉浸光感的效果请参见[示例20（设置systemMaterial开启标题栏材质效果）](../harmonyos-references/ts-basic-components-navigation.md#示例20设置systemmaterial开启标题栏材质效果)。

### 底部页签（Tabs）

底部页签支持通过应用级开启、组件级开启方式开启沉浸光感。

应用级开启：应用级开关处于[ENABLE](../harmonyos-references/arkts-apis-uimaterial.md#materialstate)模式下，底部页签不会默认开启沉浸光感；设置[barFloatingStyle](../harmonyos-references/ts-container-tabs.md#barfloatingstyle)属性并生效底部页签的悬浮样式时，底部页签默认开启沉浸光感，沉浸式系统材质样式默认取值为THIN。

组件级开启：底部页签支持通过[barFloatingStyle](../harmonyos-references/ts-container-tabs.md#barfloatingstyle)属性中[FloatingTabBarStyle](../harmonyos-references/ts-container-tabs.md#floatingtabbarstyle)的systemMaterial字段，设置TabBar背板的沉浸光感效果。

* 悬浮样式仅在[barOverlap](../harmonyos-references/ts-container-tabs.md#baroverlap10)为true、[vertical](../harmonyos-references/ts-container-tabs.md#vertical)为false、[barPosition](../harmonyos-references/ts-container-tabs.md#barposition9)为BarPosition.End时生效，三个条件需同时满足，否则systemMaterial设置不生效。
* 设置悬浮材质后，不建议再通过[barBackgroundColor](../harmonyos-references/ts-container-tabs.md#barbackgroundcolor10)、[barBackgroundBlurStyle](../harmonyos-references/ts-container-tabs.md#barbackgroundblurstyle11)为TabBar设置背景色或背景模糊，避免遮挡材质效果。
* TabContent不支持设置沉浸光感。

组件开启沉浸光感的效果请参见[示例24（TabBar悬浮样式）](../harmonyos-references/ts-container-tabs.md#示例24tabbar悬浮样式)。

### 索引条（AlphabetIndexer）

索引条支持通过应用级开启、组件级开启方式开启沉浸光感。

应用级开启：应用级开关处于[ENABLE](../harmonyos-references/arkts-apis-uimaterial.md#materialstate)模式下，索引条默认开启沉浸光感，沉浸式系统材质样式默认取值为THICK。

组件级开启：索引条参数[popupBackground](../harmonyos-references/ts-container-alphabet-indexer.md#popupbackground)和[popupBackgroundBlurStyle](../harmonyos-references/ts-container-alphabet-indexer.md#popupbackgroundblurstyle12)均未主动设置（或参数value传入undefined）时，提示弹窗默认开启沉浸光感，默认材质样式为THICK；也可通过[systemMaterial](../harmonyos-references/ts-universal-attributes-image-effect.md#systemmaterial)属性主动设置沉浸光感效果。

* 高算力、中算力设备默认显示为沉浸光感THICK样式，低算力设备不显示沉浸光感效果，显示为白色背景。
* popupBackground、popupBackgroundBlurStyle属性和沉浸光感能力互斥。主动设置popupBackground或popupBackgroundBlurStyle后无沉浸光感效果。

组件开启沉浸光感的效果请参见[示例3（设置提示弹窗背景模糊材质）](../harmonyos-references/ts-container-alphabet-indexer.md#示例3设置提示弹窗背景模糊材质)。

## 弹窗类组件

弹窗类组件包括Toast、Popup、Tips、Menu和Dialog（包含AlertDialog、CustomDialog、bindSheet及各类PickerDialog），是浮层元素，在内容之上建立视觉层次。沉浸光感为弹窗类组件赋予了核心价值：沉浸式系统材质让弹窗背景呈现轻盈通透的质感，底层内容透过材质层自然渗透，配合折射、高光、阴影等多层效果，使弹窗在内容之上建立清晰的视觉层次；沉浸式空间动效为弹窗和菜单的弹出过程增添形变、流光等动态表现，使弹出过程灵动自然。弹窗类组件通常使用较厚的材质样式（THICK或ULTRA\_THICK），以获得更强的背景模糊效果，确保弹窗内容与背景内容之间有清晰的视觉分离。

### 即时反馈（Toast）

Toast支持通过应用级开启、组件级开启方式开启沉浸光感。

应用级开启：应用级开关处于[ENABLE](../harmonyos-references/arkts-apis-uimaterial.md#materialstate)模式下，Toast默认开启沉浸光感，沉浸式系统材质样式默认取值为THICK。

组件级开启：Toast支持通过[ShowToastOptions](../harmonyos-references/js-apis-promptaction.md#showtoastoptions)中的systemMaterial字段设置沉浸光感效果。

沉浸光感开启后，如果已主动设置[ShowToastOptions](../harmonyos-references/js-apis-promptaction.md#showtoastoptions)中的backgroundBlurStyle或backgroundColor，则不呈现沉浸光感效果，否则沉浸式系统材质样式ImmersiveStyle默认取值为ImmersiveStyle.THICK。具体请参考[Dialog或Toast组件默认没有材质效果](arkts-immersive-light-sense-faq.md#dialog或toast组件默认没有材质效果)。

组件开启沉浸光感的效果请参见[showToast](../harmonyos-references/arkts-apis-uicontext-promptaction.md#showtoast)。

### 气泡提示（Popup和Tips）

Popup和Tips支持通过应用级开启、组件级开启方式开启沉浸光感。

应用级开启：应用级开关处于[ENABLE](../harmonyos-references/arkts-apis-uimaterial.md#materialstate)模式下，气泡提示不会默认开启沉浸光感。

组件级开启：气泡支持通过[PopupOptions](../harmonyos-references/ts-universal-attributes-popup.md#popupoptions类型说明)中的systemMaterial字段设置沉浸光感效果；悬浮提示通过[TipsOptions](../harmonyos-references/ts-universal-attributes-tips.md#tipsoptions类型说明)中的systemMaterial字段设置。

组件开启沉浸光感的效果请参见[示例9（设置Popup的沉浸光感视觉效果）](../harmonyos-references/ts-universal-attributes-popup.md#示例9设置popup的沉浸光感视觉效果)和[示例3（设置悬浮气泡的沉浸光感视效）](../harmonyos-references/ts-universal-attributes-tips.md#示例3设置悬浮气泡的沉浸光感视效)。

### 菜单（Menu）

菜单支持通过应用级开启、组件级开启方式开启沉浸光感。

应用级开启：应用级开关处于[ENABLE](../harmonyos-references/arkts-apis-uimaterial.md#materialstate)模式下，菜单默认开启沉浸光感，沉浸式系统材质样式默认取值为THICK。

组件级开启：菜单支持通过[ContextMenuOptions](../harmonyos-references/ts-universal-attributes-menu.md#contextmenuoptions10)中的systemMaterial字段设置沉浸光感效果。

组件开启沉浸光感的效果请参见[示例24（设置菜单的沉浸光感）](../harmonyos-references/ts-universal-attributes-menu.md#示例24设置菜单的沉浸光感)。

### 弹出框（Dialog）

弹出框支持通过应用级开启、组件级开启方式开启沉浸光感。

应用级开启：应用级开关处于[ENABLE](../harmonyos-references/arkts-apis-uimaterial.md#materialstate)模式下，弹出框默认开启沉浸光感，沉浸式系统材质样式默认取值为ULTRA\_THICK。

组件级开启：弹出框支持通过弹出框options参数中的systemMaterial字段设置沉浸光感效果，如[CustomDialogControllerOptions](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)、[AlertDialogParam](../harmonyos-references/ts-methods-alert-dialog-box.md#alertdialogparam对象说明)、[ActionSheetOptions](../harmonyos-references/ts-methods-action-sheet.md#actionsheetoptions对象说明)、[SheetOptions](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions)等。

* 沉浸光感开启后，如果已主动设置背景色、背景模糊等自定义样式属性，则不呈现沉浸光感效果，否则沉浸式系统材质样式ImmersiveStyle默认取值为ImmersiveStyle.ULTRA\_THICK。具体请参考[Dialog或Toast组件默认没有材质效果](arkts-immersive-light-sense-faq.md#dialog或toast组件默认没有材质效果)。
* 大面积的弹出框开启沉浸光感效果，会带来更多的动效绘制开销，不建议开启。详见[控制弹窗尺寸](arkts-immersive-light-sense-constraints.md#控制弹窗尺寸)中的尺寸建议。
* [CalendarPicker](../harmonyos-references/ts-basic-components-calendarpicker.md)组件拉起的弹出框目前暂不支持开启沉浸光感效果，通过通用属性设置的沉浸光感效果会体现在CalendarPicker组件本身。
* [DatePicker](../harmonyos-references/ts-basic-components-datepicker.md)、[TextPicker](../harmonyos-references/ts-basic-components-textpicker.md)、[TimePicker](../harmonyos-references/ts-basic-components-timepicker.md)组件沉浸光感效果同CustomDialog相同。

组件开启沉浸光感的效果请参见[示例9（设置弹窗的沉浸光感效果）](../harmonyos-references/ts-methods-alert-dialog-box.md#示例9设置弹窗的沉浸光感效果)、[示例14（设置弹窗的沉浸光感效果）](../harmonyos-references/ts-methods-custom-dialog-box.md#示例14设置弹窗的沉浸光感效果)、[示例9（设置弹窗的沉浸光感效果）](../harmonyos-references/ts-methods-action-sheet.md#示例9设置弹窗的沉浸光感效果)和[示例10（半模态设置系统材质）](../harmonyos-references/ts-universal-attributes-sheet-transition.md#示例10半模态设置系统材质)。

## 按钮与选择类组件

按钮与选择类组件包括Button、Select、Toggle、Slider、ChipGroup和SegmentButton，是内嵌于内容流中的交互元素，用户通过它们进行选择和操作。沉浸光感为选择类组件提供了细腻的交互反馈与通透的视觉质感：沉浸式系统材质通常使用较薄的材质样式（ULTRA\_THIN或THIN），在保持组件背景通透的同时，通过[ImmersiveOptions](../harmonyos-references/arkts-apis-uimaterial.md#immersiveoptions)中的交互形变（interactive）和点光源（lightEffect）为按压、触摸等操作提供灵动的视觉反馈，替代组件默认的按压态和悬浮态效果。

### 按钮（Button）

按钮支持通过应用级开启、组件级开启方式开启沉浸光感。

应用级开启：应用级开关处于[ENABLE](../harmonyos-references/arkts-apis-uimaterial.md#materialstate)模式下，按钮不会默认开启沉浸光感。

组件级开启：按钮支持通过[systemMaterial](../harmonyos-references/ts-universal-attributes-image-effect.md#systemmaterial)属性为[Button](../harmonyos-references/ts-basic-components-button.md)组件设置沉浸光感效果。

* 材质样式为THIN或ULTRA\_THIN时，[fontColor](../harmonyos-references/ts-basic-components-button.md#fontcolor)使用系统预定义的可反色颜色资源，可随材质自动反色。
* 当沉浸光感启用了光感交互反馈效果（[lightEffect](../harmonyos-references/arkts-apis-uimaterial.md#immersiveoptions)）时，按钮默认的点击态和悬浮态视觉反馈不再展示，由材质的光感交互反馈效果替代。
* 配置沉浸光感但未设置[buttonStyle](../harmonyos-references/ts-basic-components-button.md#buttonstyle11)、[backgroundColor](../harmonyos-references/ts-universal-attributes-background.md#backgroundcolor)等颜色相关属性且未设置材质颜色时，默认生效Button主题色的材质样式。

组件开启沉浸光感的效果请参见[示例9（设置按钮的沉浸光感效果）](../harmonyos-references/ts-basic-components-button.md#示例9设置按钮的沉浸光感效果)。

### 下拉按钮（Select）

下拉按钮支持通过应用级开启、组件级开启方式开启沉浸光感。

应用级开启：应用级开关处于[ENABLE](../harmonyos-references/arkts-apis-uimaterial.md#materialstate)模式下，下拉按钮与下拉菜单默认开启沉浸光感。下拉按钮沉浸式系统材质样式默认取值为ULTRA\_THIN，并默认开启交互形变（[interactive](../harmonyos-references/arkts-apis-uimaterial.md#immersiveoptions)）与光感交互反馈（[lightEffect](../harmonyos-references/arkts-apis-uimaterial.md#immersiveoptions)）；下拉菜单沉浸式系统材质样式默认取值为THICK。

组件级开启：下拉按钮支持通过[systemMaterial](../harmonyos-references/ts-universal-attributes-image-effect.md#systemmaterial)属性设置沉浸光感效果；下拉菜单通过独立的[menuSystemMaterial](../harmonyos-references/ts-basic-components-select.md#menusystemmaterial)接口设置沉浸光感效果。

* 下拉按钮与下拉菜单的沉浸光感相互独立，可分别开启或关闭；如需单独关闭沉浸光感，应设置[uiMaterial.Material.empty](../harmonyos-references/arkts-apis-uimaterial.md#empty)，而非将systemMaterial设置为undefined。
* 当下拉按钮的沉浸光感启用了光感交互反馈效果（[lightEffect](../harmonyos-references/arkts-apis-uimaterial.md#immersiveoptions)）时，下拉按钮默认的按压态和悬浮态视觉反馈不再展示，由材质的光感交互反馈效果替代。

组件开启沉浸光感的效果请参见[示例11（设置Select和下拉菜单沉浸光感效果）](../harmonyos-references/ts-basic-components-select.md#示例11设置select和下拉菜单沉浸光感效果)。

### 开关（Toggle）

开关支持通过应用级开启、组件级开启方式开启沉浸光感。

应用级开启：应用级开关处于[ENABLE](../harmonyos-references/arkts-apis-uimaterial.md#materialstate)模式下，Toggle默认开启沉浸光感。

组件级开启：开关支持通过[systemMaterial](../harmonyos-references/ts-universal-attributes-image-effect.md#systemmaterial)属性设置沉浸光感效果。

* 不同[ToggleType](../harmonyos-references/ts-basic-components-toggle.md#toggletype枚举说明)下沉浸光感效果存在差异：
  + ToggleType.Checkbox：当前未适配沉浸光感效果，设置后无沉浸光感效果。
  + ToggleType.Switch：传入的材质参数仅作为开启沉浸光感的开关标记，不影响实际视觉效果，实际使用组件内部预设的视觉参数，主要影响滑块大小、滑块样式、阴影等；材质效果随设备算力档位变化。
  + ToggleType.Button：效果与[Button](../harmonyos-references/ts-basic-components-button.md)组件设置沉浸光感相同，主要影响背景颜色、边框、阴影等视觉属性。

组件开启沉浸光感的效果请参见[示例4（Toggle沉浸光感效果）](../harmonyos-references/ts-basic-components-toggle.md#示例4toggle沉浸光感效果)。

### 滑动条（Slider）

滑动条支持通过应用级开启、组件级开启方式开启沉浸光感。

应用级开启：应用级开关处于[ENABLE](../harmonyos-references/arkts-apis-uimaterial.md#materialstate)模式下，滑动条默认开启沉浸光感。

组件级开启：滑动条支持通过[systemMaterial](../harmonyos-references/ts-universal-attributes-image-effect.md#systemmaterial)属性设置沉浸光感效果。

* 传入的材质参数仅作为开启沉浸光感的开关标记，不影响实际视觉效果，实际使用组件内部预设的视觉参数，主要影响滑块大小、滑块样式、阴影等；传入undefined时沉浸光感不生效，恢复为原先的Slider样式。
* 沉浸光感的交互反馈效果仅在滑块形状为[SliderBlockType](../harmonyos-references/ts-basic-components-slider.md#sliderblocktype10枚举说明).DEFAULT且[SliderStyle](../harmonyos-references/ts-basic-components-slider.md#sliderstyle枚举说明)不为NONE时生效。

组件开启沉浸光感的效果请参见[示例10（设置滑动条的沉浸光感效果）](../harmonyos-references/ts-basic-components-slider.md#示例10设置滑动条的沉浸光感效果)。

### 子页签（ChipGroup）

子页签支持通过应用级开启、组件级开启方式开启沉浸光感。

应用级开启：应用级开关处于[ENABLE](../harmonyos-references/arkts-apis-uimaterial.md#materialstate)模式下，子页签默认开启沉浸光感，沉浸式系统材质样式默认取值为ULTRA\_THIN。

组件级开启：子页签支持通过[ChipGroup](../harmonyos-references/ohos-arkui-advanced-chipgroup.md)的backgroundSystemMaterial、selectedBackgroundSystemMaterial（选中状态）和iconBackgroundSystemMaterial（图标）字段设置沉浸光感效果。

需要文字、图标颜色随材质自动反色时，颜色应使用系统预定义的可反色颜色资源（如$r('sys.color.font\_primary')），硬编码颜色值不会触发自动反色，详见[设置沉浸式系统材质反色](arkts-immersive-light-sense-common-capability.md#设置沉浸式系统材质反色)。

组件开启沉浸光感的效果请参见[示例6（设置系统材质样式）](../harmonyos-references/ohos-arkui-advanced-chipgroup.md#示例6设置系统材质样式)和[示例7（设置组件选中状态的系统材质样式）](../harmonyos-references/ohos-arkui-advanced-chipgroup.md#示例7设置组件选中状态的系统材质样式)。

### 操作块（SegmentButton）

操作块支持通过应用级开启、组件级开启方式开启沉浸光感。

应用级开启：应用级开关处于[ENABLE](../harmonyos-references/arkts-apis-uimaterial.md#materialstate)模式下，操作块默认开启沉浸光感，沉浸式系统材质样式默认取值为THIN。

组件级开启：[SegmentButton](../harmonyos-references/ohos-arkui-advanced-segmentbutton.md)支持通过SegmentButtonOptions中的backgroundSystemMaterial字段设置沉浸光感效果；[SegmentButtonV2](../harmonyos-references/ohos-arkui-advanced-segmentbuttonv2.md)通过各类分段按钮options参数中的backgroundSystemMaterial字段设置。

* SegmentButton的胶囊类多选分段按钮（[SegmentButtonOptions](../harmonyos-references/ohos-arkui-advanced-segmentbutton.md#segmentbuttonoptions)的type为“capsule”且[SegmentButtonOptions](../harmonyos-references/ohos-arkui-advanced-segmentbutton.md#segmentbuttonoptions)的multiply为true）不支持backgroundSystemMaterial，设置后不生效。
* SegmentButtonV2开启沉浸光感后，支持选中项背景跟随手指拖拽，否则不支持跟随手指拖拽。
* 设置自动反色时，即colorInvert为true，如果SegmentButton中的fontColor、selectedFontColor，或SegmentButtonV2中的itemFontColor、itemSelectedFontColor、itemIconFillColor、itemSelectedIconFillColor等使用支持反色的系统资源，颜色自动适配到材质背景色的反色。

组件开启沉浸光感的效果请参见[示例8（设置背景板材质）](../harmonyos-references/ohos-arkui-advanced-segmentbutton.md#示例8设置背景板材质)和[示例6（设置背景板材质）](../harmonyos-references/ohos-arkui-advanced-segmentbuttonv2.md#示例6设置背景板材质)。

## 其余组件

其余组件均支持通用属性[systemMaterial](../harmonyos-references/ts-universal-attributes-image-effect.md#systemmaterial)设置沉浸式系统材质，跟随通用属性的生效规则呈现效果，例如[布局容器](arkts-layout-development-overview.md)、[滚动容器](arkts-list-grid-development-overview.md)。生效区域为Navigation/NavDestination标题栏，或横向Tab中barPosition为BarPosition.End的底部TabBar。开启后的常见问题请参考[沉浸光感常见问题](arkts-immersive-light-sense-faq.md)。
