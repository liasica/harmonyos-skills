---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-app-icon-configuration
title: 应用图标配置与开发
breadcrumb: 最佳实践 > 应用框架 > 程序包结构 > 应用图标配置与开发
category: best-practices
scraped_at: 2026-04-28T08:20:09+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:3c0b9d489dc9932708ca28038f886364fab30fd17becd949a8799075b74b91e2
---

## 概述

应用图标是由图形、文字和色彩组合而成的视觉符号，用于标识应用程序的特征，可在设备桌面、应用列表、应用商店等界面呈现，帮助用户快速识别、区分并启动对应的应用。

根据组成结构的不同，应用图标可分为单层图标和分层图标。

* 单层图标：支持解码为[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)的图片。
* 分层图标：由前景图和背景图组成的JSON格式图标资源。
  + 前景图：通常是应用图标的主体部分，例如应用的主要图形、Logo或文字，需为透明的PNG格式。
  + 背景图：用于与前景图叠加形成完整的应用图标，需为纯色，不能含有透明像素。

本文旨在帮助开发者了解应用图标的配置与常见开发场景，主要内容包括：

* [使用DevEco Studio生成图标](bpta-app-icon-configuration.md#section2728125612346)：使用DevEco Studio将分层图标生成为单层图标，或者将单层图标生成为元服务图标。
* [配置不同场景下的图标](bpta-app-icon-configuration.md#section1878513210537)：介绍应用图标与启动页图标的使用场景及配置方法。
* [开发场景](bpta-app-icon-configuration.md#section686420451402)：应用图标主要开发场景有[动态切换应用图标](bpta-app-icon-configuration.md#section0642329412)与[应用内展示应用图标](bpta-app-icon-configuration.md#section65292247411)。
* [上架AppGallery Connect时的图标规范](bpta-app-icon-configuration.md#section1470095312575)：介绍应用上架时软件包中应用图标应满足的标准，以及上传至AppGallery Connect平台的应用图标需遵循的规范，旨在帮助开发者了解相关要求，缩短应用审核与上架时间。

在开始阅读之前，建议开发者先了解[应用图标](../design-guides/application-icon-0000001953444009.md)和[应用开发准备](../harmonyos-guides/application-dev-overview.md)。

注意

在应用图标设计阶段，建议开发者依据[通用应用UX体验标准](../design-guides/ux-guidelines-general-0000001760708152.md)与[上架AppGallery Connect时的图标规范](bpta-app-icon-configuration.md#section1470095312575)，准备相应格式的图标资源。

## 使用DevEco Studio生成图标

### 生成单层图标

若开发者需将分层图标生成为单层图标，可使用DevEco Studio的Image Asset功能，具体操作可参考[生成单层图标](../harmonyos-guides/ide-apply-generated-icon.md)。

说明

发布应用时，phone-xxxldpi/media（设备类型为phone时生成）目录下的icon.png（216\*216px）图片可用于在AppGallery Connect上传应用图标。

### 生成元服务图标

当创建的工程为元服务时，可使用元服务图标生成能力，具体操作可参考[生成元服务图标](../atomic-guides/atomic-service-icon-generation.md)。

## 配置不同场景下的图标

### 配置应用图标

应用图标通常在下列场景中使用：

* 在设备桌面展示当前应用。
* 在设置应用的应用列表中展示当前应用。
* 在通知栏中展示发出消息通知的应用。

效果图如下：

| 设备桌面 | 应用列表 | 通知栏 |
| --- | --- | --- |
|  |  |  |

应用图标可通过配置单层图标或配置分层图标两种方式进行配置，具体操作可参考[配置单层图标和应用名称](../harmonyos-guides/layered-image.md#配置单层图标和应用名称)与[配置分层图标和应用名称](../harmonyos-guides/layered-image.md#配置分层图标和应用名称)。

注意

轻量级智能穿戴应用在entry/src/main/config.json文件的abilities标签下配置icon和label字段。相关要求请查看[轻量级智能穿戴应用配置应用图标](bpta-app-icon-configuration.md#li15169114820415)。

### 配置启动页图标

启动页是在应用进程没有运行或应用内容没有加载完成前展示的页面，承载了应用展示品牌特性的功能，用于向用户展示产品独特的标识，并加强用户对产品的认知。启动页主要使用场景如下：

* 应用在没有后台进程的情况下启动，会先展示启动页。
* 应用仍处于启动页阶段时退出到后台，多任务中会展示该应用的启动页。
* 应用主动销毁且系统未生成快照时，会在退出动效展示启动页。例如：使用[killAllProcesses()](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextkillallprocesses14)接口终止应用的所有进程。

| 应用冷启动 | 启动页阶段退出到后台 | 应用主动销毁 |
| --- | --- | --- |
|  |  |  |

开发者可通过配置简单启动页和配置增强启动页两种方式配置启动页图标。

* 配置简单启动页

  在module.json5文件的[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)下配置startWindowIcon（启动页图标）和startWindowBackground（启动页背景颜色）字段。[生成单层图标](bpta-app-icon-configuration.md#section1982161535013)时，会生成icon.png和icon\_startwindow.png图标，其中icon\_startwindow.png图标可用于配置startWindowIcon字段，startWindowBackground字段的值建议在resources/base/element目录下的color.json文件中配置。

  ```
  1. "startWindowIcon": "$media:icon_startwindow",
  2. "startWindowBackground": "$color:start_window_background",
  ```
* 配置增强启动页

  从API version 19开始，支持使用startWindow字段配置增强启动页。步骤如下：

  1. 在resources/base/media目录下添加以下文件：
     1. icon\_startwindow.png：增强启动页的图标资源文件。
     2. illustration.png：增强启动页的插画资源文件，startWindowAppIcon字段与startWindowIllustration字段同时配置时，仅展示图标资源。
     3. brand.png：增强启动页的品牌标识资源文件。
     4. bgImage.png：增强启动页的背景图片资源文件。
  2. 在resources/base/profile目录下创建start\_window.json文件。

     ```
     1. {
     2. "startWindowType": "REQUIRED_SHOW",
     3. "startWindowColorModeType": "FOLLOW_SYSTEM",
     4. "startWindowAppIcon": "$media:icon_startwindow",
     5. "startWindowIllustration": "$media:illustration",
     6. "startWindowBrandingImage": "$media:brand",
     7. "startWindowBackgroundColor": "$color:start_window_background",
     8. "startWindowBackgroundImage": "$media:bgImage",
     9. "startWindowBackgroundImageFit": "Contain"
     10. }
     ```
  3. 在module.json5文件的abilities标签下配置startWindow字段。

     ```
     1. "startWindow": "$profile:start_window",
     ```

  若开发者需要了解相关字段配置要求和增强启动页示意图，请查看[配置增强启动页](../harmonyos-guides/launch-page-config.md#配置增强启动页)。

## 开发场景

### 动态切换应用图标

通过图标管理服务，开发者可以在不升级应用版本的情况下，在应用侧实现动态切换应用图标。例如：元宵节、中秋节、圣诞节等节日时，在应用图标中加入对应节日元素（如灯笼、月饼、圣诞树）。开发步骤可分为两步：

* 在AppGallery Connect动态管理应用图标
  1. 使用图标管理服务前，请向运营人员发送邮件[申请开通服务](../harmonyos-guides/appgallery-appinfo-manage.md#section474611326316)。
  2. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，点击“APP与元服务”查看已上架应用列表，在应用列表选择已开通图标管理服务的应用进入应用信息页面，选择“分发>服务>图标管理”进入图标管理页面。
  3. 在图标管理页面可进行[创建图标](../harmonyos-guides/appgallery-appinfo-manage.md#section1680884411110)、[编辑和更新图标](../harmonyos-guides/appgallery-appinfo-manage.md#section1080916448112)和[删除图标](../harmonyos-guides/appgallery-appinfo-manage.md#section15809944141118)。
* 使用AppGallery Kit实现应用图标动态切换
  1. 调用[queryDynamicIcons()](../harmonyos-references/appgallery-appinfomanager.md#section887383520415)接口查询动态图标信息。
  2. 调用[selectDynamicIcon()](../harmonyos-references/appgallery-appinfomanager.md#section16502191111574)接口通过图标ID切换动态图标。
  3. 调用[disableDynamicIcon()](../harmonyos-references/appgallery-appinfomanager.md#section984175210392)接口恢复默认图标。

  详细开发步骤可参考[实现应用图标动态切换](../harmonyos-guides/appgallery-appinfo-use.md)。

### 应用内展示应用图标

UI Design Kit提供了应用图标处理能力，支持单层图标和双层图标，开发者可使用[hdsDrawable](../harmonyos-references/ui-design-hdsdrawable.md)模块处理应用图标并获取处理后的图标数据对象。以下是一些典型的应用场景：

* 在应用列表中展示应用图标。例如：设置应用的应用列表。
* 在应用详情页展示应用图标。例如：应用版本信息页面。

下面以在应用列表中展示应用图标为例介绍应用内展示应用图标的开发步骤。

* 展示分层图标
  1. 在entry/src/main/resources/base/media目录下添加前景图和背景图，并在该目录下配置分层图标资源文件（如drawable.json）。

     ```
     1. {
     2. "layered-image":
     3. {
     4. "background" : "$media:background",
     5. "foreground" : "$media:foreground"
     6. }
     7. }
     ```
  2. 通过[getDrawableDescriptor()](../harmonyos-references/js-apis-resource-manager.md#getdrawabledescriptor10)接口获取原始分层图标信息，并调用[getHdsLayeredIcon()](../harmonyos-references/ui-design-hdsdrawable.md#section156601033183215)接口、[getHdsLayeredIconAsync()](../harmonyos-references/ui-design-hdsdrawable.md#section5196826193012)接口或[getHdsLayeredIcons()](../harmonyos-references/ui-design-hdsdrawable.md#section712131324710)接口获取处理后的PixelMap对象。
  3. 使用[List](../harmonyos-references/ts-container-list.md)组件和[Image](../harmonyos-references/ts-basic-components-image.md)组件展示带图标的应用列表。

  示例代码可参考[分层图标处理开发实例](../harmonyos-guides/ui-design-layered-process.md#section1817964534718)。
* 展示单层图标
  1. 在entry/src/main/resources/base/media目录下配置单层图标资源文件（如normal\_icon.png）。
  2. 通过[getDrawableDescriptor()](../harmonyos-references/js-apis-resource-manager.md#getdrawabledescriptor10)接口获取原始单层图标信息，并调用[getHdsIcon()](../harmonyos-references/ui-design-hdsdrawable.md#section11716322123212)接口、[getHdsIconAsync()](../harmonyos-references/ui-design-hdsdrawable.md#section343192618556)接口或[getHdsIcons()](../harmonyos-references/ui-design-hdsdrawable.md#section12429174135913)接口获取处理后的PixelMap对象。
  3. 使用[List](../harmonyos-references/ts-container-list.md)组件和[Image](../harmonyos-references/ts-basic-components-image.md)组件展示带图标的应用列表。

  示例代码可参考[单层图标处理开发实例](../harmonyos-guides/ui-design-normal-process.md#section048218555616)。

## 上架AppGallery Connect时的图标规范

在AppGallery上架应用或元服务时需要上传软件包和应用图标。请开发者在软件包中正确预置图标资源，确保图标符合UX体验标准和审核标准。

* 软件包中图标规范
  + 应用图标资源使用PNG格式，不同设备上的应用图标资源应满足[多平台图标资源规格](../design-guides/application-icon-0000001953444009.md#section357075123214)。
  + 应用图标资源不允许自行裁剪圆角，不允许在资源内添加内间距。
  + 应用图标显示正常，无明显的模糊、拉伸、压缩、锯齿等情况。
  + 轻量级智能穿戴应用开发时需要配置的应用图标与智能穿戴应用不同，如下表：

    | 文件名 | 资源分层 | 资源形状 | 资源尺寸 | 典型使用场景 |
    | --- | --- | --- | --- | --- |
    | icon.png | 单层 | 圆形 | 104\*104px | Launcher |
    | icon\_small.png | 单层 | 圆形 | 92\*92px | 权限管理 |
* AppGallery Connect平台规范
  + 上传至AppGallery Connect的应用图标资源需满足[素材规范](../app/agc-help-app-visual-asset-spec-0000002277607976.md)。
  + 上传的应用图标必须与软件包中的应用图标一致。
  + 应用图标应符合实际功能、用途，不能包含误导性、不相关、不恰当的信息。详细介绍请查看[应用信息](../app/50104-01.md)。

## 常见问题

### 验证应用图标是否符合规范的方法

开发者可使用以下三种方法验证应用图标是否符合规范：

* 使用DevEco Testing进行[UX基础质量测试](../harmonyos-guides/specialized-testing.md#section189671819225)。
  1. 参考[DevEco Testing快速上手](../harmonyos-guides/get-familiar.md)下载最新版本的DevEco Testing并完成相关环境准备。
  2. 打开DevEco Testing，选择专项测试的UX基础质量测试。
  3. 在测试规则中选择应用图标，并选择测试时长后创建测试任务。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/FJYXCuBfRkKk0vcNNbv7qg/zh-cn_image_0000002548106143.png?HW-CC-KV=V1&HW-CC-Date=20260428T002006Z&HW-CC-Expire=86400&HW-CC-Sign=4E73B2955ABC4EF803F2745B435260FF475EE0C0F204D884E8928AF83424B3A3)
* 使用DevEco Testing的[上架预检](../harmonyos-guides/publish-testing.md)服务。
* 使用AppGallery Connect平台的云测试服务进行[UX测试](../app/agc-help-cloudtest-uxtest-0000002289534109.md)。

### 在app.json5文件或module.json5文件中配置图标后不生效

**问题现象**

1. 在entry/src/main/resources/base/media目录下预置应用图标资源，并完成前景图与背景图配置，但应用实际显示的图标与module.json5文件中配置的图标资源不一致。
2. 在app.json5文件中配置了应用图标资源，但实际显示的是module.json5文件中配置的应用图标。

**可能原因**

1. 当module.json5文件中未配置UIAbility或skills标签下的entities未配置“entity.system.home”或actions未配置“ohos.want.action.home”时，app.json5文件中配置的应用图标生效。
2. 当AppScope/resource目录与entry/src/main/resources目录存在同名文件时，在编译构建过程中，AppScope下的资源会与entry模块下的资源合并，且entry/src/main/resources目录下的同名资源文件会被覆盖。此时会显示module.json5文件中配置的被覆盖后的应用图标。
3. 当module.json5文件中正确配置UIAbility且模块中的图标资源文件与AppScope中的图标资源文件名称不同时，根据[配置优先级和生成策略](../harmonyos-guides/layered-image.md#配置优先级和生成策略)，将显示module.json5文件中配置的应用图标。

**解决方案**

1. 当需要显示app.json5文件中配置的应用图标时，若模块使用的API不依赖module.json5文件的icon和label字段，可以不配置module.json5文件中对应字段，或者模块中图标资源与AppScope中图标资源保持一致。
2. 当需要显示module.json5文件中配置的应用图标时，可以修改AppScope中的图标资源文件名称（如修改分层图标资源文件为app\_layered\_image.json，并修改前景图名称为app\_foreground.png、背景图名称修改为app\_background.png）。

   app.json5文件：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/pD0-SirySjWAitmkd80MbA/zh-cn_image_0000002548066135.png?HW-CC-KV=V1&HW-CC-Date=20260428T002006Z&HW-CC-Expire=86400&HW-CC-Sign=2B486C41897432F7837CF61702ABD48F868848E735B941B506B20012FDBE603C)

   module.json5文件的abilities标签：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/DDQXGFQLTqicL0u6pc52Sw/zh-cn_image_0000002516546242.png?HW-CC-KV=V1&HW-CC-Date=20260428T002006Z&HW-CC-Expire=86400&HW-CC-Sign=39ACB2F97DE175D8536D396549481DC95782BA18E74AFD28F1CD3CF6A4DBA3B5)
