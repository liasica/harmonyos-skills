---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-creation
title: 创建ArkTS卡片
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > 创建ArkTS卡片
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:18+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:0931b80d8babb23ea4b98a1a0521a16836dbf5afb08fb159c6e42255b761556e
---

ArkTS卡片有两种创建卡片包的方式。开发者在开发过程中任选其一即可。

方式一：卡片和应用共包方式，创建步骤请参考[共包方式创建卡片](arkts-ui-widget-creation.md#方式一共包方式创建卡片)，此时卡片UI和应用代码在一个module内，最终编译产物也在同一个HAP包内。

方式二：独立卡片包方式，创建步骤请参考[独立包方式创建卡片](arkts-ui-widget-creation.md#方式二独立包方式创建卡片)，此时卡片UI和应用代码在不同module内，最终编译产物分为卡片包和应用包。从API version 20开始支持。

ArkTS卡片创建完成，在开发卡片过程中，支持对卡片进行[实时预览](ide-service-widget.md#section18171652015)。

## 方式一：共包方式创建卡片

### 创建步骤

**1. 新建工程**

在DevEco Studio中，选择创建Application或Atomic Service工程，这两种都支持创建卡片。工程创建指导具体请参考[创建一个新的工程](ide-create-new-project.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/QPlVbTX1QKmN4JnR8u8XtQ/zh-cn_image_0000002788467196.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=19086A1002E574519EA6556E8086096B62A864B129C61EBD7A4A2C637F174BEA)

**说明** 

基于不同版本的DevEco Studio，请以实际界面为准。

**2. 新建卡片**

在已有的应用工程中，右键新建ArkTS卡片，具体操作如下。

* 选中entry目录单击右键选择【New】->【Service Widget】->【Dynamic Widget】。在API 10及以上 Stage模型的工程中，开发者可通过Service Widget菜单直接选择创建动态卡片（Dynamic Widget）或静态卡片（Static Widget）。创建卡片后，也可在卡片的[form\_config.json配置文件](arkts-ui-widget-configuration.md#配置文件字段说明)中，通过isDynamic参数修改卡片类型：isDynamic置空或赋值为“true”，则该卡片为[动态卡片](arkts-form-overview.md#动态卡片)；isDynamic赋值为"false"，则该卡片为[静态卡片](arkts-form-overview.md#静态卡片)。静态卡片和动态卡片切换之后用户交互实现也需要修改，具体参考ArkTS卡片概述中的[动态卡片](arkts-form-overview.md#动态卡片)和[静态卡片](arkts-form-overview.md#静态卡片)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/zuE8Ro8vQcqsZ78e1Tz4mw/zh-cn_image_0000002817506685.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=14DFD99ED03974132EFE9A5D65979555FA08BDC3F3DF567186FDBB775E33BED7)
* 选择模板后，点击【Next】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/AWGOZGfSRx67O6PiHSeEMQ/zh-cn_image_0000002788307254.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=CEFBFCA55AE1A7F6AAD2DAC8549CC3FADD21F4A2CE116DEF73B703325455467B)
* 在选择卡片的开发语言类型（Language）时，选择ArkTS选项。选择卡片支持的外观规格（Support dimension）时，选择期望的卡片尺寸，然后选择默认的外观规格（Default dimension），最后点击“Finish”，即可完成ArkTS卡片创建。详细的卡片外观规格可参考[form\_config.json](arkts-ui-widget-configuration.md#配置文件字段说明)配置文件，后续也可以在form\_config.json配置文件中修改卡片规格。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/Zp_vigO9TwuFlJKsccuWxQ/zh-cn_image_0000002817426617.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A7B9BB410D34781EFB69A6B7E48946294B0464994C40148782E0B2698412E3F)

  建议根据实际使用场景命名卡片名称，ArkTS卡片创建完成后，工程中会新增如下卡片相关文件：卡片生命周期管理文件（EntryFormAbility.ets）、卡片页面文件（WidgetCard.ets）和卡片配置文件（form\_config.json）。填写卡片配置之后点击【Finish】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/qj22JyDHSwWUwVRbo1_nIw/zh-cn_image_0000002788467198.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=23BDF6633EDA3F4B33601DBA1CFD7FB935DBA70D1D9BD027DE804D94A3F259DD)

### 工程结构介绍

**图1** ArkTS卡片工程目录、相关模块

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/l1FzYY0ZQs-l5K9OVS3tMg/zh-cn_image_0000002817506687.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=736E4007CF2723656F8EAFA08F565E183F3C60E31321106BA925AD7F0F96E417)

* [FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)：卡片扩展模块，提供卡片创建、销毁、刷新等生命周期回调。
* [FormExtensionContext](../harmonyos-references/js-apis-inner-application-formextensioncontext.md)：FormExtensionAbility的上下文环境，提供FormExtensionAbility具有的接口和能力。
* [formProvider](../harmonyos-references/js-apis-app-form-formprovider.md)：提供了获取卡片信息、更新卡片、设置卡片更新时间等能力。
* [formInfo](../harmonyos-references/js-apis-app-form-forminfo.md)：提供了卡片信息和状态等相关类型和枚举。
* [formBindingData](../harmonyos-references/js-apis-app-form-formbindingdata.md)：提供卡片数据绑定的能力，包括FormBindingData对象的创建、相关信息的描述。
* [页面布局（WidgetCard.ets）](arkts-ui-widget-page-overview.md)：基于ArkUI提供卡片UI开发能力。

  + [ArkTS卡片通用能力](arkts-ui-widget-page-overview.md#arkts卡片支持的页面能力)：提供了能在ArkTS卡片中使用的组件、属性和API。
  + [ArkTS卡片特有能力](arkts-ui-widget-event-overview.md)：postCardAction用于卡片内部和提供方应用间的交互，仅在卡片中可以调用。
* [卡片配置](arkts-ui-widget-configuration.md)：包含FormExtensionAbility的配置和卡片的配置。

  + 在[module.json5配置文件](module-configuration-file.md)中的extensionAbilities标签下，配置FormExtensionAbility相关信息。
  + 在resources/base/profile/目录下的[form\_config.json](arkts-ui-widget-configuration.md#配置文件字段说明)配置文件中，配置卡片（WidgetCard.ets）相关信息。

## 方式二：独立包方式创建卡片

### 创建步骤

**1. 新建工程**

在DevEco Studio中，选择创建Application或Atomic Service工程，这两种都支持创建卡片。工程创建指导具体请参考[创建一个新的工程](ide-create-new-project.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/548j8zkGS22YMdPcbMUlIw/zh-cn_image_0000002788467196.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=62929E9C598EFB81B62AE68DFC7E17CDDCD5EC159F1486FEC5A9137F99C9756D)

**说明** 

基于不同版本的DevEco Studio，请以实际界面为准。

**2. 新建卡片**

* 选中entry目录单击右键选择【New】->【Service Widget】->【Dynamic Widget(Standalone)】。在Service Widget菜单可直接选择创建独立包的动态卡片（Dynamic Widget(standalone)）或静态卡片（Static Widget(standalone)）。创建服务卡片后，也可以在卡片的[form\_config.json配置文件](arkts-ui-widget-configuration.md#配置文件字段说明)中，通过isDynamic参数修改卡片类型：isDynamic置空或赋值为“true”，则该卡片为[动态卡片](arkts-form-overview.md#动态卡片)；isDynamic赋值为"false"，则该卡片为[静态卡片](arkts-form-overview.md#静态卡片)。静态卡片和动态卡片切换之后用户交互实现也需要修改，具体参考ArkTS卡片概述中的[动态卡片](arkts-form-overview.md#动态卡片)和[静态卡片](arkts-form-overview.md#静态卡片)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/7Zm0AQUlSUmeWW-2B9_cXQ/zh-cn_image_0000002788307256.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=43C4D33F0D64C126472F7DC73AF7B3FA6FBBF0D9DAB0B620446967C422B0961E)
* 选择模板后，点击【Next】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/t06cOHRiS-WZZxoPySf8Hw/zh-cn_image_0000002788307254.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=19F1D8E06F14B6E802E46FFFCFE635CBB815E8145587CE1E43151C66DFF3AA9F)
* 填写卡片配置之后点击【Finish】。卡片创建成功后，entry包中包含应用和卡片后端能力；library包中包含卡片UI侧能力。entry模块下的module.json5配置文件中的formWidgetModule字段需关联library模块，library模块下的module.json5配置文件中的formExtensionModule字段需关联entry模块，以实现卡片包和应用包相互关联。创建完成后，会自动生成配置文件并配置，后续也可以按照[卡片配置文件](arkts-ui-widget-configuration.md)修改配置。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/Cp5REoebQp2QVD4yBku-kA/zh-cn_image_0000002817426619.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=2AB7AC53D341F090C718D2A0926E0F196857FC6CB76702707D5A1AE92A235531)

### 工程结构介绍

独立卡片包与卡片共包方式创建卡片，仅工程结构存在差异，生成的文件是一致的，各文件具体内容请参考[共包方式工程结构介绍](arkts-ui-widget-creation.md#工程结构介绍)。

**图2** 独立卡片包工程目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/cKNygNMCRHS4Ki7M5SBaTw/zh-cn_image_0000002788467200.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB95E7C6768606A667639338040C49F3C3A501C73D3EA9770C22A2F914108D81)

**说明** 

独立卡片包中应用包和卡片包为2个独立模块，因此需要关注同时安装的应用包和卡片包版本号一致。
