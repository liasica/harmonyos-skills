---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-purax-guide
title: 阔折叠/阔直板应用开发
breadcrumb: 最佳实践 > 多端设备体验提升 > 手机 > 阔折叠/阔直板应用开发
category: best-practices
scraped_at: 2026-09-10T06:30:10+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:00e2e9673f6803f0c0ad35e1b23abdd4dca3caee1198045cb4f6b35b55aabbd2
---

## 概述

阔折叠设备主要包含Pura X和Pura X Max两款产品，阔直板设备主要包含Pura X View。

阔折叠有以下特点：

1. 设备屏幕尺寸可变，具有不同大小和形态的窗口。需要针对不同的应用窗口尺寸，做响应式的页面布局适配。
   * 折叠时，Pura X外屏为小方形屏。Pura X Max外屏屏幕尺寸较直板机宽度更宽、高度更矮。
   * 展开后，Pura X内屏屏幕接近于直板机，较直板机宽度更宽、高度更矮。Pura X Max内屏屏幕尺寸接近于平板，对内容的展示面积增大。
2. 具有特殊的折叠状态和交互事件。包含三种状态：折叠态、展开态和悬停态。需保障不同状态下的应用体验一致性（如开合连续性）。
   * 展开态：阔折叠完全展开后的形态。有更大的屏幕尺寸，可充分显示应用内容。
   * 折叠态：阔折叠折叠后的形态。折叠后屏幕尺寸变小。
   * 悬停态：阔折叠处于完全展开和折叠的中间状态，可平稳放置。
3. 设备的折叠态和展开态均配置相机：Pura X折叠时仅配有前置相机，展开时配有前置相机和后置相机；Pura X Max折叠和展开时均配有前置相机和后置相机。在不同折叠状态下，可用相机和相机的位置会发生变化。开发相机功能时需考虑摄像头切换与预览流重置。

阔直板有以下特点：

1. 原生竖屏采用宽屏形态，相较于传统瘦长直板机，横向可视范围更广、信息承载量更大，在影音、阅读、办公等场景中体验优势显著。
2. 设备圆角增大，顶部避让区变大，视觉上状态栏/页面整体下移。应用需重点关注窗口沉浸适配逻辑，并针对四边圆角带来的界面遮挡问题进行差异化适配。

| 产品名称 | 示意图 |
| --- | --- |
| **Pura X** |  |
| **Pura X Max** |  |
| **Pura X View** |  |

**说明** 

* 本文聚焦于阔折叠/阔直板应用的体验提升开发指导。如需多设备开发的基础通用能力指导，请参考“[一次开发，多端部署概览](bpta-multi-device-overview.md)”系列文章。
* 阔形屏的推荐布局，请参考文章“屏幕类型布局场景-[阔形屏](bpta-multi-device-screen-layout.md#section1584317473553)”。

## 产品硬件说明

### 屏幕规格信息

本章节介绍阔折叠和阔直板的屏幕规格信息，以Pura X、Pura X Max和Pura X View产品的常用屏幕形态为例：

| 产品名称 | 设备形态 | 屏幕比例（高宽比） | 屏幕规格信息(宽\*高) | 示意图 |
| --- | --- | --- | --- | --- |
| **Pura X** | 折叠态(横向) | 1:1 | 分辨率(vp)(向下取整)：326\*326 |  |
| 分辨率(px)：980\*980 |
| 横纵断点(横向\*纵向)：sm\*md |
| 展开态(竖向) | 16:10 | 分辨率(vp)(向下取整)：440\*707 |  |
| 分辨率(px)：1320\*2120 |
| 横纵断点(横向\*纵向)：sm\*lg |
| **Pura X Max** | 折叠态(竖向) | 14:10 | 分辨率(vp)(向下取整)：459\*672 |  |
| 分辨率(px)：1264\*1848 |
| 横纵断点(横向\*纵向)：sm\*lg |
| 展开态(横向) | 10:14 | 分辨率(vp)(向下取整)：939\*664 |  |
| 分辨率(px)：2584\*1828 |
| 横纵断点(横向\*纵向)：lg\*sm |
| **Pura X View** | / | 16:9.5 | 分辨率(vp)(向下取整)：440\*744 |  |
| 分辨率(px)：1320\*2232 |
| 横纵断点(横向\*纵向)：sm\*lg |

### 相机硬件信息

本章节介绍阔折叠的相机硬件信息。以Pura X和Pura X Max产品的相机为例：Pura X折叠态配置一个前置相机，展开态配置一个前置相机和后置相机。Pura X Max折叠态和展开态均配置一个前置相机和后置相机。

| 产品名称 | 设备形态 | 相机硬件信息 | | 示意图 |
| --- | --- | --- | --- | --- |
| **Pura X** | 折叠态(横向) | 前置相机安装镜头角度 | 270度 |  |
| 前置相机拍摄预览流旋转角度 | 180度 |
| 展开态(竖向) | 后置相机镜头安装角度 | 90度 |  |
| 后置相机预览流旋转角度 | 90度 |
| 前置相机镜头安装角度 | 270度 |
| 前置相机预览流旋转角度 | 270度 |
| **Pura X Max** | 折叠态(竖向) | 后置相机镜头安装角度 | 90度 |  |
| 后置相机预览流旋转角度 | 90度 |
| 前置相机镜头安装角度 | 270度 |
| 前置相机预览流旋转角度 | 270度 |
| 展开态(横向) | 后置相机镜头安装角度 | 90度 |  |
| 后置相机预览流旋转角度 | 0度 |
| 前置相机镜头安装角度 | 270度 |
| 前置相机预览流旋转角度 | 180度 |

**说明** 

* 相机预览流旋转角度=(镜头安装角度+屏幕旋转角度)%360，在设备状态改变后（如横竖屏旋转）需要重置相机预览流，更多相机硬件差异和开发详情可参考[相机硬件差异](bpta-multi-device-camera.md)。
* 阔直板相机硬件信息与普通直板机/Pura X Max折叠态一致。

### 设备折叠能力

阔折叠具备独特的折叠功能，在不同折叠状态下展现出不同的特性。

通过[display.isFoldable()](../harmonyos-references/js-apis-display.md#displayisfoldable10)接口可判断设备是否支持折叠，若支持则返回true，否则返回false。通过[display.getFoldStatus()](../harmonyos-references/js-apis-display.md#displaygetfoldstatus10)接口可获取折叠设备当前的折叠状态，返回结果可参考[FoldStatus](../harmonyos-references/js-apis-display.md#foldstatus10)。下表以Pura X Max产品为例，展示了阔折叠的折叠状态和属性。

|  | 折叠态 | 悬停态 | 展开态 |
| --- | --- | --- | --- |
| **示意图** |  |  |  |
| **isFoldable** | true | | |
| **FoldStatus** | FOLD\_STATUS\_FOLDED | FOLD\_STATUS\_HALF\_FOLDED | FOLD\_STATUS\_EXPANDED |

## 创新与体验提升

### 滑动隐藏

以Pura X Max产品为例，该产品外屏高度小于直板机，在用户滑动浏览内容时，自动隐藏底部导航栏与顶部标题栏，可最大化可视区域，提升有效信息的呈现面积。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/vyPOm-ZBRj2Qn0eOCnTEJg/zh-cn_image_0000002585466452.gif "点击放大")

将导航栏与标题栏的高度、透明度设为变量，通过监听滑动动作并根据交互实时改变变量值，即可达到预期效果。详细实现可参考小方形屏[布局设计与实现](bpta-multi-device-screen-layout.md#section13926555601)的沉浸式浏览章节。

### 交互跟手

以Pura X Max产品为例，该产品展开态横屏时横向断点为lg，纵向断点为sm，提供更宽广的显示视野和更强的信息承载能力。在布局设计与实现上，建议充分利用其横向空间优势：

* 内容展示：推荐使用分栏布局（如二分栏、三分栏）或重复布局（如瀑布流、多列网格），以清晰展示层级关系并提升信息密度。
* 图文排版：针对图文混排场景，可将竖屏的上下排布调整为左右布局，让页面视觉效果更美观，内容展示也更为高效。

具体的布局设计与实现细节，可参考[大屏横屏](bpta-multi-device-screen-layout.md#section6493354468)相关规范。

为了提升横屏使用交互体验，建议适配系统全新交互能力，通过接入智感握姿、跟手弹框和跟手半模态等新特性，让用户操作更快捷、高效。

**1.智感握姿**：系统提供感知用户当前握持手信息的能力，应用可依据获取的手部信息，自适应调整核心交互组件的显示位置，有效提升用户单手操作便捷性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/XayVB-GpTwCXAtB2AyV32Q/zh-cn_image_0000002585626390.gif "点击放大")

通过订阅握持手状态变化感知事件[motion.on('holdingHandChanged')](../harmonyos-references/js-apis-awareness-motion.md#motiononholdinghandchanged-20)，获取到握持手信息后，更改组件的显示位置。

**2.跟手弹框**：设备展开状态下，屏幕中间的弹窗组件手指不易触达。采用跟手式弹出设计，让弹窗在点击位置就近唤起，可降低操作难度，提升交互效率。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/MzIG4Y7DTQmd3RGvNHCRvw/zh-cn_image_0000002615986115.png "点击放大")

构建UI布局时，可通过条件表达式判断：当横向断点为sm时，使用普通居中弹框；否则，使用跟手弹框[PopoverDialog](../harmonyos-references/ohos-arkui-advanced-dialog.md#popoverdialog14)，提升大屏设备的操作效率。

**3.跟手半模态**.：横屏设备可根据业务需要，灵活选用跟手半模态窗口或居中半模态窗口。

使用[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)绑定半模态转场时，设置半模态属性preferType为SheetType.POPUP（请参考[SheetType枚举说明](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheettype11枚举说明)）。设置该属性后，窗口宽度小于600vp的设备将默认显示底部弹窗，其他设备则自动适配为跟手弹窗。

### 悬停态适配

以Pura X Max产品为例，该产品悬停态支持设备平稳放置于桌面，实现免手持体验，常用于视频通话、视频播放、拍照、听歌等不需要频繁交互的场景。这种状态下，应用需要对中间折痕区域进行避让，并对上下两个界面进行悬停态布局适配。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/PG5gRjl_RjCrg-eWfRSKUQ/zh-cn_image_0000002616066279.png "点击放大")

### 开合适配

开合连续指应用在屏幕形态与窗口状态切换时，保持页面内容连贯，延续任务进度与运行状态。支持用户快速接续切换前的操作，打造流畅的切换体验。例如阔折叠设备在折叠态与展开态相互切换时，应用页面内容保持不变、状态无缝接续，保障使用体验不受影响。具体实现方案，可参考[开合连续](bpta-multi-device-screen-diff.md#section16541144511135)章节。

### 悬浮组件

以Pura X Max产品为例，该产品外屏高度小于直板机，实现界面布局时需着重考虑提升显示效率。

借助[HdsTabs(底部页签)](../harmonyos-references/ui-design-hdstabs.md)组件的[barFloatingStyle](../harmonyos-references/ui-design-hdstabs.md#barfloatingstyle)属性实现悬浮导航栏，并通过悬浮材质参数[SystemMaterialParams](../harmonyos-references/ui-design-hdstabs.md#systemmaterialparams)配置透明磨砂材质效果，能有效提升可视区域面积。此外，为增强界面的可玩性与功能延展性，可接入[HdsTabsMiniBar](../harmonyos-references/ui-design-hdstabs.md#hdstabsminibar)组件，在导航区增设一个可扩展迷你标签栏。该组件可在不占用过多空间的前提下，提供额外的导航维度或快捷功能入口，丰富用户交互路径，进一步提升界面操作的灵活性和趣味性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/59MDZW4OTKqd7EF-voc1Sg/zh-cn_image_0000002585466534.gif "点击放大")

### 视频自适应沉浸

以Pura X Max产品为例，该产品外屏高度小于直板机，为避免视频播放画面出现异常拉伸、过度裁剪等问题，可通过自适应沉浸全屏播放方案，精简界面元素、减少视觉干扰，让用户聚焦视频画面，有效提升观看体验。具体实现方案，可参考[视频适配不同尺寸屏幕](bpta-multi-device-screen-diff.md#section1452572513130)章节。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/ir6eHIBpQzWYcQdR22VgeQ/zh-cn_image_0000002585626472.gif "点击放大")

### 全景多窗

[全景多窗](../harmonyos-guides/multi-window-intro.md#全景多窗)旨在帮助用户高效处理多个任务。通过全景多窗，用户可以突破物理屏幕局限，在同一屏幕内并行运行多款应用，实现应用间快捷切换，提升操作效率。以Pura X Max产品为例，该产品展开态横屏状态下拥有更大的显示视野，具备更强的信息展示与内容承载能力。该产品可依托全景多窗能力，充分利用大屏空间优势，最高支持三个窗口同屏并行运行，助力用户一边浏览资讯、一边编辑内容、一边沟通办公，多任务同步处理、互不冲突，实现办公、娱乐、日常操作一站式协同。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/brKYGmlfSsuvyW334NCSNw/zh-cn_image_0000002615986189.png "点击放大")

### 手写笔适配

阔折叠设备的交互方式为触控屏，常见的操作有点击、双击、长按、拖拽、滑动等，应用可根据这些操作进行功能适配，详情可参考[多设备交互](bpta-multi-interaction.md)。

除了触控屏交互，部分阔折叠产品（如Pura X Max）还搭载手写笔，支持无感连接与低延迟传输，开盒即用，适用于全局批注、提笔速记及按键遥控等功能场景，实现流畅自然的书写与交互体验。通过系统提供的[Pen Kit简介](../harmonyos-guides/pen-introduction.md)能力，开发者可灵活接入手写套件、全局取色、一笔成形等接口，提升书写交互的扩展性与创作效率。

### 圆角遮挡适配

以Pura X View产品为例，游戏类应用横屏布局时，需要关注四边圆角变大导致的视野或按钮遮挡问题，如下图所示。推荐使用display.[getRoundedCorner](../harmonyos-references/js-apis-display.md#getroundedcorner23)()方法获取屏幕的圆角信息。应用需要结合UI布局局部遮挡的情况，调整视野/按钮控件与屏幕边缘的边距，避免因圆角变大导致的布局截断。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/Ovvdvud2RByLdl6zq5wUNA/zh-cn_image_0000002717779986.png "点击放大")

## 设备常见适配问题

### 截断/留白/重叠

**应用启动页面未铺满屏幕或出现异常布局**

问题描述：在阔折叠展开态或阔直板启动应用时，应用的启动页面未铺满整个屏幕，出现白屏区域或者启动页面被截断。

解决方案：应用需要[配置增强启动页](../harmonyos-guides/launch-page-config.md#配置增强启动页)，配置后启动页面中的背景、图片和图标等资源能根据窗口大小自适应填充，保证启动页面在不同设备形态上正常显示，配置中各标签的说明可参考[startWindow标签](../harmonyos-guides/module-configuration-file.md#startwindow标签)。

**应用弹框有截断/留白**

问题描述：应用弹窗在普通直板机上正常显示，在阔折叠/阔直板上出现截断/留白。

解决方案：阔折叠外屏/阔直板的竖向高度小于直板机，实现弹框时建议使用如下几种实现方式：

1. 使用[自适应布局](bpta-multi-device-adaptive-layout.md)实现弹框布局，当容器组件尺寸发生变化时，可自动适应调整宽高。
2. 使用[constraintSize](../harmonyos-references/ts-universal-attributes-size.md#constraintsize)约束弹框高度最大不超过父组件的90%，避免弹框内容截断。

**应用页面有截断/留白**

问题描述：应用页面在普通直板机上正常显示，在阔折叠/阔直板上出现截断/留白。

解决方案：阔直板和阔折叠的不同形态，对应不同的窗口尺寸。建议采用响应式布局适配不同窗口尺寸，并随窗口尺寸变化动态调整页面布局，详情可参考[页面适配不同尺寸屏幕](bpta-multi-device-screen-diff.md#section103508214132)。

**应用页面布局与状态栏重叠**

问题描述：Pura X View圆角增大导致状态栏高度变高。应用若通过硬编码固定高度的方式避让顶部状态栏，可能出现页面布局与状态栏重叠异常。

解决方案：通过组件级或窗口级沉浸方案实现窗口沉浸式，并通过系统接口获取避让区域的高度进行避让，详细开发指导请参考[实现沉浸式效果](bpta-multi-device-window-immersive.md#section180431120426)和[避让处理](bpta-multi-device-window-immersive.md#section1014820221441)。

### 异常旋转

**设备形态切换应用启动显示异常**

问题描述：以 Pura X Max 为例，在折叠态冷启动应用并退出至后台，将设备展开再热启动该应用，页面会先以竖屏样式展示，再自动切换为横屏显示。

可能原因：应用将折叠态窗口旋转策略配置为portrait，展开态配置为auto\_rotation\_restricted。应用在折叠态后台运行时，页面维持竖屏窗口状态；设备展开后应用会先保留原有竖屏样式，再响应设备形态变更，触发旋转策略切换为横屏展示。

解决方案：应用可使用[跟随桌面的旋转策略](bpta-multi-device-window-direction.md#section3434202623320)，通过修改module.json5配置文件中的orientation属性为FOLLOW\_DESKTOP解决该问题。

### 相机开发

**外屏相机功能异常**

问题描述：以Pura X为例，外屏相机页面的开发，可能出现以下问题：

1. 相机页面布局异常。
2. 设备形态切换后预览画面拉伸/压缩。
3. 预览画面黑屏。
4. 拍摄照片显示角度异常。

解决方案：

1. 针对不同屏幕尺寸的横向断点适配多套相机页面布局。详情请参考[通过断点实现多套页面布局](bpta-multi-device-camera.md#section181143569262)。
2. 调整XComponent组件Surface区域的宽高比，使其与预览流旋转后的宽高比保持一致。详情请参考[设置多设备上相机预览画面比例](bpta-multi-device-camera.md#section882216138497)。
3. 监听设备形态切换导致的窗口尺寸变更，重新选择可用相机并生成预览流。详情请参考[选择相机设备](bpta-multi-device-camera.md#section13854163154917)。
4. 正确配置拍照的旋转角度。详情请参考[设置拍照旋转角度](bpta-multi-device-camera.md#section0752024124911)。
