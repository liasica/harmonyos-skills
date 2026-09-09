---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-matext-guide
title: 三折叠应用开发
breadcrumb: 最佳实践 > 多端设备体验提升 > 手机 > 三折叠应用开发
category: best-practices
scraped_at: 2026-09-10T06:30:09+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:4fe29118952e606c215417259639260af622e32e1c6a01c4b7cda2210152fc78
---

## 概述

华为推出的“三折叠”旗舰折叠手机，拥有三块可联动显示的屏幕，且三块屏幕均可折叠。相对于直板机，三折叠设备有以下明显特点：

* 设备屏幕尺寸可变，具有不同大小和形态的UX界面。
* 具有特殊的折叠状态和交互事件。三折叠具备折叠的能力，共有9种折叠状态，具体描述可以参考[设备折叠能力](bpta-matext-guide.md#section15762231134610)章节。
* 不同折叠状态下，相机的可用状态及位置会发生变化。

三折叠主要产品为Mate XT、MateXTs及Mate XT 2：

* Mate XT、Mate XTs常用的三种使用状态分别为：单屏态（F态）、双屏态（M态）和三屏态（G态）。
* Mate XT 2新增多个折叠形态，常用状态分别为：单屏态（F态、N态）、双屏态（LM态、RM态）和三屏态（G态）。

| 产品名称 | 示意图 |
| --- | --- |
| **Mate XT** |  |
| **Mate XT 2** |  |

**说明** 

本文聚焦于三折叠应用的体验提升开发指导。如需多设备开发的基础通用能力指导，请参考“[一次开发，多端部署概览](bpta-multi-device-overview.md)”系列文章。

## 产品硬件说明

### 屏幕规格信息

本章节以Mate XTs和Mate XT 2的常用屏幕形态为例，介绍三折叠的屏幕规格信息：

| 产品名称 | 设备形态 | 屏幕规格信息(宽\*高) | 示意图 |
| --- | --- | --- | --- |
| **Mate XTs** | 单屏态（F态）(竖向) | 分辨率(vp)(向下取整)：350\*776 |  |
| 分辨率(px)：1008\*2232 |
| 横纵断点(横向\*纵向)：sm\*lg |
| 双屏态（M态）(竖向) | 分辨率(vp)(向下取整)：712\*776 |  |
| 分辨率(px)：2048\*2232 |
| 横纵断点(横向\*纵向)：md\*md |
| 三屏态（G态）(横向） | 分辨率(vp)(向下取整)：1107\*776 |  |
| 分辨率(px)：3184\*2232 |
| 横纵断点(横向\*纵向)：lg\*sm |
| **Mate XT** **2** | 单屏态（F）(竖向) | 分辨率(vp)(向下取整)：380\*814 |  |
| 分辨率(px)：1140\*2442 |
| 横纵断点(横向\*纵向)：sm\*lg |
| 单屏态（N）(竖向) | 分辨率(vp)(向下取整)：378\*744 |  |
| 分辨率(px)：1136\*2232 |
| 横纵断点(横向\*纵向)：sm\*lg |
| 双屏态（LM）(竖向) | 分辨率(vp)(向下取整)：709\*744 |  |
| 分辨率(px)：2128\*2232 |
| 横纵断点(横向\*纵向)：md\*md |
| 双屏态（RM）(竖向) | 分辨率(vp)(向下取整)：682\*744 |  |
| 分辨率(px)：2048\*2232 |
| 横纵断点(横向\*纵向)：md\*md |
| 三屏态（G态）(横向） | 分辨率(vp)(向下取整)：1061\*744 |  |
| 分辨率(px)：3184\*2232 |
| 横纵断点(横向\*纵向)：lg\*sm |

### 相机硬件信息

本章节介绍三折叠的相机硬件信息。以Mate XTs和Mate XT 2的相机为例：各形态下均配置一个前置相机和一个后置相机。

| 产品名称 | 设备形态 | 相机硬件信息 | | 示意图 |
| --- | --- | --- | --- | --- |
| **Mate XTs** | 单屏态（F态）(竖向) | 后置相机安装镜头角度 | 90度 |  |
| 后置相机预览流旋转角度 | 90度 |
| 前置相机安装镜头角度 | 270度 |
| 前置相机预览流旋转角度 | 270度 |
| 双屏态（M态）(竖向) | 后置相机安装镜头角度 | 90度 |  |
| 后置相机预览流旋转角度 | 90度 |
| 前置相机安装镜头角度 | 270度 |
| 前置相机预览流旋转角度 | 270度 |
| 三屏态（G态）(横向） | 后置相机安装镜头角度 | 90度 |  |
| 后置相机预览流旋转角度 | 90度 |
| 前置相机安装镜头角度 | 270度 |
| 前置相机预览流旋转角度 | 270度 |
| **Mate XT 2** | 单屏态（F态）(竖向) | 后置相机安装镜头角度 | 90度 |  |
| 后置相机预览流旋转角度 | 90度 |
| 前置相机安装镜头角度 | 270度 |
| 前置相机预览流旋转角度 | 270度 |
| 单屏态（N态）(竖向) | 后置相机安装镜头角度 | 90度 |  |
| 后置相机预览流旋转角度 | 90度 |
| 前置相机安装镜头角度 | 270度 |
| 前置相机预览流旋转角度 | 270度 |
| 双屏态（LM）(竖向) | 后置相机安装镜头角度 | 90度 |  |
| 后置相机预览流旋转角度 | 90度 |
| 前置相机安装镜头角度 | 270度 |
| 前置相机预览流旋转角度 | 270度 |
| 双屏态（RM）(竖向) | 后置相机安装镜头角度 | 90度 |  |
| 后置相机预览流旋转角度 | 90度 |
| 前置相机安装镜头角度 | 270度 |
| 前置相机预览流旋转角度 | 270度 |
| 三屏态（G态）(横向） | 后置相机安装镜头角度 | 90度 |  |
| 后置相机预览流旋转角度 | 90度 |
| 前置相机安装镜头角度 | 270度 |
| 前置相机预览流旋转角度 | 270度 |

相机预览流旋转角度=(镜头安装角度+屏幕旋转角度)%360，在设备状态改变后（如横竖屏旋转）需要重置相机预览流，更多相机硬件差异和开发详情可参考[相机硬件差异](bpta-multi-device-camera.md)。

**说明** 

Mate XTs的双屏态（M态）及Mate XT 2的RM态下，前置相机功能可用，但由于设备开合角度和用户位置的限制，成像效果或使用体验可能不理想，因此不推荐在该状态下使用前置相机。

### 设备折叠能力

三折叠屏拥有9种折叠状态，在不同折叠状态下展现出不同的特性；可将其理解为左右两块双折叠屏组合而成，左右两块折叠屏各自包含3种折叠状态（折叠态/展开态/半折态），整体即为3×3=9种折叠状态。

通过[display.getFoldStatus()](../harmonyos-references/js-apis-display.md#displaygetfoldstatus10)接口可获取折叠设备当前的折叠状态，返回结果可参考[FoldStatus](../harmonyos-references/js-apis-display.md#foldstatus10)。通过[display.getFoldDisplayMode()](../harmonyos-references/js-apis-display.md#displaygetfolddisplaymode10)接口可获取折叠设备当前的屏幕显示模式，返回结果可参考[FoldDisplayMode](../harmonyos-references/js-apis-display.md#folddisplaymode10)。下表以Mate XTs产品为例，展示了三折叠的折叠状态和属性。

| [FoldStatus](../harmonyos-references/js-apis-display.md#foldstatus10) | [FoldDisplayMode](../harmonyos-references/js-apis-display.md#folddisplaymode10) | 效果图 |
| --- | --- | --- |
| FOLD\_STATUS\_EXPANDED | FOLD\_DISPLAY\_MODE\_FULL |  |
| FOLD\_STATUS\_FOLDED | FOLD\_DISPLAY\_MODE\_MAIN |  |
| FOLD\_STATUS\_HALF\_FOLDED | FOLD\_DISPLAY\_MODE\_FULL |  |
| FOLD\_STATUS\_EXPANDED\_WITH\_SECOND\_EXPANDED | FOLD\_DISPLAY\_MODE\_FULL |  |
| FOLD\_STATUS\_EXPANDED\_WITH\_SECOND\_HALF\_FOLDED | FOLD\_DISPLAY\_MODE\_FULL |  |
| FOLD\_STATUS\_FOLDED\_WITH\_SECOND\_EXPANDED | FOLD\_DISPLAY\_MODE\_MAIN |  |
| FOLD\_STATUS\_FOLDED\_WITH\_SECOND\_HALF\_FOLDED | FOLD\_DISPLAY\_MODE\_MAIN |  |
| FOLD\_STATUS\_HALF\_FOLDED\_WITH\_SECOND\_EXPANDED | FOLD\_DISPLAY\_MODE\_FULL |  |
| FOLD\_STATUS\_HALF\_FOLDED\_WITH\_SECOND\_HALF\_FOLDED | FOLD\_DISPLAY\_MODE\_FULL |  |

**说明** 

* 布局适配应优先基于响应式断点，而非设备折叠状态。统一通过横纵向[断点](bpta-multi-device-responsive-layout.md#section1532120147301)判断页面布局，确保在不同屏幕状态下实现一致的响应式表现。切勿直接以设备折叠状态作为布局判断依据，避免因设备差异导致显示异常（如Pura X的FOLD\_STATUS\_EXPANDED状态对应的是展开态，为直板机布局；而三折叠的FOLD\_STATUS\_EXPANDED状态对应的是双屏态，应为大方形屏布局）。
* 仅悬停态等特殊场景可针对性优化，此类场景可借助折叠状态实现专属布局设计，效果可参考[典型悬停适配案例](../design-guides/foldable-0000002352875141.md#section12307164615117)。

## 创新与体验提升

### 交互跟手

三折叠的双屏态和三屏态拥有更宽广的显示视野，信息承载量更大，用户可操作范围也更广。为进一步提升双屏态和三屏态下的使用体验，建议适配系统全新交互能力，通过接入智感握姿、跟手弹窗和跟手半模态等新特性，让用户操作更快捷、高效。

1. **智感握姿**：系统提供感知用户当前握持手信息的能力，应用可依据获取的手部信息，自适应调整核心交互组件的显示位置，有效提升用户单手操作便捷性。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/7u6cVsTETlm4lkNItFAPwg/zh-cn_image_0000002585626656.png "点击放大")

   通过订阅握持手状态变化感知事件[motion.on('holdingHandChanged')](../harmonyos-references/js-apis-awareness-motion.md#motiononholdinghandchanged-20)，获取到握持手信息后，更改组件的显示位置。
2. **跟手弹框**：为了减少用户操作路径过长的情况，在双屏态和三屏态可通过跟手弹窗进行展示，弹出框的弹出位置离手更近，以便用户能够快速操作。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/3FMWl0EeTaGCaeR-Qv9_mw/zh-cn_image_0000002615986371.png "点击放大")

   构建UI布局时，可通过条件表达式判断：当横向断点为sm时，使用普通居中弹框；否则，使用跟手弹框[PopoverDialog](../harmonyos-references/ohos-arkui-advanced-dialog.md#popoverdialog14)，提升大屏设备的操作效率。
3. **跟手半模态**：在单屏态，半模态窗口通常从屏幕底部弹出；在双屏态，建议窗口居中显示；而在三屏态，可以考虑跟手半模态窗口或者居中半模态窗口显示，具体根据业务需要选择。

   使用[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)绑定半模态转场时，设置半模态属性preferType为[SheetType](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheettype11枚举说明).POPUP。设置该属性后，窗口宽度小于600vp的设备将默认显示底部弹窗，其他设备则自动适配为跟手弹窗。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/fibUFkT_Qry9aPJIfJKFvw/zh-cn_image_0000002616066471.png "点击放大")

### 悬停态适配

Mate XT系列在双屏态下可切换至悬停态。悬停态支持设备平稳放置于桌面，实现免手持体验，常用于视频通话、视频播放、拍照、听歌等不需要频繁交互的场景。这种状态下，应用需要对中间折痕区域进行避让，并对上下两个界面进行悬停态布局适配。悬停态的实现方案可参考[折叠屏悬停态](bpta-folded-hover.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/NiVaSJQvTbOxL-jf8LvMaQ/zh-cn_image_0000002585466742.png "点击放大")

**说明** 

说明：由于硬件形态存在差异，Mate XT 2不支持悬停态。

### 开合适配

开合连续指应用在屏幕形态与窗口状态切换时，保持页面内容连贯，延续任务进度与运行状态。支持用户快速接续切换前的操作，打造流畅的切换体验。例如三折叠设备在单屏态、双屏态和三屏态之间切换时，应用页面内容保持不变、状态无缝接续，保障使用体验不受影响。具体实现方案，可参考[开合连续](bpta-multi-device-screen-diff.md#section16541144511135)章节。

### 悬浮组件

三折叠设备具备单屏、双屏、三屏三种形态，借助[HdsTabs (底部页签)](../harmonyos-references/ui-design-hdstabs.md)组件的[barFloatingStyle](../harmonyos-references/ui-design-hdstabs.md#barfloatingstyle)属性实现悬浮导航栏，可适配各类形态切换场景，充分释放屏幕可视区域；通过悬浮材质参数[SystemMaterialParams](../harmonyos-references/ui-design-hdstabs.md#systemmaterialparams)配置透明磨砂材质效果，提升界面通透感，适配沉浸式浏览体验。搭配[HdsTabsMiniBar](../harmonyos-references/ui-design-hdstabs.md#hdstabsminibar)可扩展迷你标签栏，拓展多维度快捷入口，适配双屏态和三屏态的分区操作，同时保障单屏、双屏、三屏形态下交互逻辑统一，降低用户切换成本，有效提升操作效率与使用体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/OjcC-tSkS6OC58LIoxR1gw/zh-cn_image_0000002585626678.png "点击放大")

### 视频自适应沉浸

三折叠设备具备单屏、双屏、三屏三种形态，为避免视频播放画面在形态切换时出现拉伸、裁剪、显示比例错乱等问题，可采用自适应沉浸全屏播放方案，精简界面元素、减少视觉干扰，让用户聚焦视频画面，充分利用大屏开阔视野，有效提升观看体验。具体实现方案，可参考[视频适配不同尺寸屏幕](bpta-multi-device-screen-diff.md#section1452572513130)章节。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/5SlzZ-3NR762LMrxE0QvIg/zh-cn_image_0000002615986397.gif "点击放大")

### 手写笔适配

三折叠的交互方式主要为触控屏，常见的操作有点击、双击、长按、拖拽等，应用可根据这些操作进行功能适配，详情可参考[多设备交互](bpta-multi-interaction.md)。

Mate XTs及Mate XT 2产品搭载手写笔，支持无感连接与低延迟传输，开盒即用，适用于全局批注、提笔速记及按键遥控等功能场景，实现流畅自然的书写与交互体验。系统提供的[Pen Kit](../harmonyos-guides/pen-introduction.md)能力，可助力开发者灵活接入手写套件、全局取色、一笔成形等接口，提升书写交互的扩展性与创作效率。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/3CYxLOwgTbSOCHstt_DFjQ/zh-cn_image_0000002616066493.png "点击放大")

### 键鼠适配

除触控屏交互外，三折叠还支持外接键鼠进行交互。以Mate XTs产品为例，键鼠交互事件的适配应包含：

* 鼠标悬浮效果：三折叠设备中，应用内可交互UI组件建议适配鼠标悬浮效果。开发方案请参考[交互归一](bpta-multi-interaction.md#section088812013815)进行适配。
* 键盘快捷键：应用需支持常用快捷键响应，提升用户操作效率。开发方案请参考[交互归一](bpta-multi-interaction.md#section088812013815)进行适配。

**说明** 

外接键盘时，系统默认提供ESC按键事件，若应用未监听ESC事件，则返回上一页。onKeyEvent事件是默认冒泡的，在其回调方法中，若按键事件已完成处理，建议返回true完成事件消费，避免事件继续向上冒泡，造成上层节点重复响应，导致按键事件被触发多次。

### 焦点导航

三折叠设备接入键盘与应用程序进行间接交互时，建议将页面中可操作元素设置为可获焦状态，并配置获焦视觉效果，清晰指示当前焦点位置，以保证交互体验。开发方案请参考[焦点事件](bpta-multi-interaction.md#section168661941154220)。

**说明** 

通常情况下，三折叠设备以触控交互为主，可通过[交互归一](bpta-multi-interaction.md#section088812013815)完成基础适配；当外接键鼠时，可额外适配鼠标悬浮效果、键盘快捷键及焦点导航，完善多输入方式的操作体验。

### 全景多窗

[全景多窗](../harmonyos-guides/multi-window-intro.md#全景多窗)旨在帮助用户高效处理多个任务。通过全景多窗，用户可以突破物理屏幕局限，在同一屏幕内并行运行多款应用，实现应用间快捷切换，提升操作效率。以Mate XTs产品为例，该产品三屏态横屏状态下拥有更大的显示视野，具备更强的信息展示与内容承载能力。可依托全景多窗能力，充分利用大屏空间优势，最高支持三个窗口同屏并行运行，助力用户一边浏览资讯、一边编辑内容、一边沟通办公，多任务同步处理、互不冲突，实现办公、娱乐、日常操作一站式协同。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/9yHEUi80TNOJN_lPuQ2CAw/zh-cn_image_0000002585466754.png "点击放大")

## 设备常见适配问题

### 截断/留白

**平板布局正常，但是三折叠G态布局异常**

问题描述：应用页面在平板上显示正常，但在三折叠G态下出现图片过大、字体偏大、画面拉伸/压缩、界面留白等布局异常。

可能原因：开发者使用“deviceType === tablet”作为lg断点布局的判断条件，仅适配了平板设备，导致三折叠三屏态无法匹配正确布局，出现显示异常。

解决方案：UX布局应依据窗口尺寸与窗口形状判断，而非物理设备类型。同一套UX布局需在不同设备的相同尺寸窗口下保持一致：三折叠三屏态与平板布局保持一致，双屏态与双折叠展开态布局保持一致，单屏态与直板机布局保持一致。建议使用断点方案替代设备形态接口，实现统一的UX布局判断逻辑，详细说明可参考[断点](bpta-multi-device-responsive-layout.md#section1532120147301)。

**说明** 

三折叠不同折叠状态下展示的页面布局，统一使用一多横向断点进行判断。下列方式不推荐作为判断UX布局的条件：

1. deviceInfo.deviceType：通过设备类型区分UX布局，会导致同一种UX布局无法实现一次开发、多设备适配。
2. display.isFoldable、display.getFoldStatus、display.getFoldDisplayMode等折叠状态接口：该类接口无法区分双折叠、小折叠、阔折叠与三折叠设备，扩展性较差。多数折叠屏开合过程中出现的布局异常，均是直接以折叠状态、折叠显示模式作为布局判断条件所致；不同折叠屏即便处于同一折叠状态，屏幕实际属性差异较大，若共用一套布局易引发显示问题。

**展开态应用启动页面未铺满屏幕，出现异常布局**

问题描述：在折叠屏展开态启动应用时，应用的启动页面未铺满整个屏幕，出现白屏区域或者启动页被截断。

可能原因：应用未配置增强启动页。

解决方案：应用需要[配置增强启动页](../harmonyos-guides/launch-page-config.md#配置增强启动页)，配置后启动页面中的背景、图片和图标等资源能根据窗口大小自适应填充，保证启动页面在不同设备形态上正常显示，配置中各标签的说明可参考[startWindow标签](../harmonyos-guides/module-configuration-file.md#startwindow标签)。

### 异常旋转

**三折叠G态仅支持竖屏，无法旋转**

问题描述：三折叠设备在G态下，页面仅支持竖屏展示，无法旋转。

可能原因：开发者通过判断双折叠设备的折叠状态为FoldStatus.FOLD\_STATUS\_EXPANDED（展开态）时开启旋转支持，其余状态默认竖屏；但三折叠G态对应的折叠状态为FoldStatus.FOLD\_STATUS\_EXPANDED\_WITH\_SECOND\_EXPANDED，与双折叠判定逻辑不匹配，因此无法触发旋转，仅能竖屏显示。

解决方案：应用可使用[跟随桌面的旋转策略](bpta-multi-device-window-direction.md#section3434202623320)，通过修改module.json5配置文件中的orientation属性为FOLLOW\_DESKTOP解决该问题。

**折叠开合过程导致屏幕显示方向变化**

问题描述：三折叠设备在默认使用、未主动旋转屏幕的情况下，进行折叠开合操作时，屏幕显示方向会自动发生改变。

可能原因：三折叠设备在不同折叠形态下，即便屏幕旋转角度一致，系统对显示方向的定义也存在差异。

解决方案：开发时需留意三折叠不同折叠状态下默认显示方向的差异，避免因方向判断错误，而引发页面布局或功能异常。

| **三折叠屏幕折叠状态** | 单屏态(F态) | 双屏态(M态) | 三屏态(G态) |
| --- | --- | --- | --- |
| **效果图(充电口朝下)** |  |  |  |
| **屏幕旋转角度([Display](../harmonyos-references/js-apis-display.md#display).rotation)** | 0 | 0 | 0 |
| **屏幕显示方向([Orientation](../harmonyos-references/js-apis-display.md#orientation10))** | PORTRAIT竖屏 | PORTRAIT竖屏 | LANDSCAPE\_INVERTED反向横屏 |
