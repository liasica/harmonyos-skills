---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-codegenie-service-widget
title: 万能卡片生成
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 万能卡片生成
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:39+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:f9e2d1b7d573f78034da8f2c01ea9632bc69d79d08623be530f07f5ddc610949
---

基于AI大模型理解开发者的卡片需求信息，通过对话式的交互智能生成HarmonyOS万能卡片工程。

## 使用约束

1. 建议从以下维度描述卡片需求：

   |  |  |  |  |
   | --- | --- | --- | --- |
   | **序号** | **建议描述维度** | **说明** | **举例** |
   | 1 | 卡片用途 | 卡片的用途/业务场景，比如电商购物、娱乐、生活服务类等。 | 例如“电商购物卡片”、“娱乐类卡片”。 |
   | 2 | 卡片功能 | 卡片包含的组件，如图标、标题、按钮等。  组件的状态信息，如图标主题、标题内容、按钮显示的文字等。 | 例如“新品上市主标题”、“商品搜索按钮”、“热门电影子板块入口”等。 |
   | 3 | 卡片尺寸 | HarmonyOS官网提供的四种卡片尺寸：1\*2（微卡片）、2\*2（小卡片）、2\*4（中卡片）、4\*4（大卡片）。  卡片尺寸为非必选项，AI会根据前两个维度描述的信息，智能选择效果最佳的尺寸。 | 例如“2\*2尺寸的卡片”、“中卡片”等。 |
2. 当前不支持在生成卡片预览图后，继续描述需求进行增量修改。

## 万能卡片生成

1. 点击页面右侧菜单栏CodeGenie图标完成登录后，可以通过如下两种方式进入卡片生成窗口。在窗口输入万能卡片的需求，并点击发送，根据模型提示进行多轮交互，不断完善需求。

   * 在对话区域输入"/"调出命令，选择**Service Widget**。从DevEco Studio 6.1.0 Beta2版本开始不支持。
   * 在输入框左下角的下拉框选择**Service Widget**。DevEco Studio 6.0.1 Beta1版本新增。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/P9sFwN-tQMiVntS3uqX5bQ/zh-cn_image_0000002808886407.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=0B29E8A56BF4F09FF2443B5EAF8782D2C5BB9E429B0EB7B6AB263C723556C444)
2. 需求描述完成后，可以根据提示信息进一步细化卡片尺寸、用途、展示元素等，以及预览卡片效果图。生成效果示例**：**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/-eMlVvDhRbiyTIQC8nOoMA/zh-cn_image_0000002779566734.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=C5EA6D1579ED43BC5BB31E5932E8D73CA033C5F14E20E831CFED7D80685E8737 "点击放大")

## 万能卡片保存

1. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/qbQMbpdXTqeWl7pYOwSQNw/zh-cn_image_0000002808766323.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=76284B7C62712370107B3167D842BB4B02CB90D940A71718FFE3400EFB7DB255)，可查看生成卡片的UI代码、配置信息和下载静态资源文件。
2. 保存卡片工程有两种方式：

   方式一：使用代码/配置查看窗口的“复制”、“插入”或“创建文件”等按钮，手动保存卡片代码和配置信息。

   方式二：点击“保存工程”按钮，自动保存卡片工程，卡片代码、配置、静态资源文件等会自动保存到工程对应目录中。默认勾选保存逻辑代码，逻辑代码用于配置卡片事件及卡片数据等信息，具体请参考[自定义配置逻辑代码](ide-codegenie-service-widget.md#section17840955102711)。

   **流程示例：**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/siZ5d_dXTOG-DacsTS2Jag/zh-cn_image_0000002808766321.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=695BDA79AB4CC137A0D67146FEE68CCFADC789A3C2164CDB0B08F760AA290A17 "点击放大")

   工程保存完成后，工程中会新增如下卡片相关文件：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/WgbyVgaXQDKGRXOnGDcwNQ/zh-cn_image_0000002779566736.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=7CA32D756599FBABB9D7ACD5BC3BFE1C068D95A75AE56E096F21FA8936FA4691 "点击放大")

## 自定义配置逻辑代码

逻辑代码包含实现卡片数据交互和卡片事件两类。

* 卡片数据交互：触发卡片页面刷新。应用工程生成的卡片数据交互，可通过数据库或网络请求两种方式来触发卡片页面刷新；对于元服务工程生成的卡片，数据交互为通过网络请求方式触发卡片页面刷新。
* 卡片事件：使用router事件跳转到指定的UIAbility、使用call事件拉起UIAbility到后台、使用message事件刷新卡片内容。

### 目录结构

在module > src > main > ets 路径下， formcommon目录用于存放生成卡片的逻辑代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/l8G_VaQGTX-5AD8Kic20Ng/zh-cn_image_0000002808766313.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=B78ABBEC8AE24F9EA22B28C55D634EF37A0534BB256317CBB20C6D507F2FD9F7 "点击放大")

* formsetting：存放用户可配置的文件。
  + formsetting > formdbsetting：自定义配置以数据库方式进行卡片刷新的相关参数。
    - formdbsetting > formdbinfo：存放包含卡片信息的Info.ets文件，可在Info.ets文件中，添加卡片刷新所需要的具体的数据，后续会读取该文件并将数据存入数据库中。
    - UserSettings.ets：可以自定义卡片刷新时从数据库获取数据的规则、数据解析规则、message内容刷新规则。
  + formsetting > formhttpsetting：自定义配置以网络请求方式进行卡片刷新的相关参数。
    - formhttpsetting > formhttpinfo：存放包含卡片信息的Info.ets文件，可在Info.ets文件中添加获取卡片刷新数据的URL。
    - UserSettings.ets：可以自定义卡片刷新时从URL获取数据的规则、数据解析规则、message内容刷新规则。

    **说明** 

    如需使用网络请求方式刷新卡片页面，需在EntryFormAbility.ets文件中将FormDbUpdate的接口注释掉，并将启用FormHttpUpdate接口。
  + formsetting > FormAction.ets：配置卡片事件。
* utils：存放工具类的目录，用户不可修改，如果修改再次生成逻辑代码时utils目录会被刷新。

### 自定义配置卡片事件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/022fx11QQJKjG_mgovr-Mg/zh-cn_image_0000002808886393.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=CEC6AF76542DC3E5EA088B0C23FC20F1F45EBC44944A82D3A5726AB31C250EA8)

1. 在FormAction.ets文件中，配置触发卡片router事件时具体的页面分发规则。

2. 在EntryAbility.ets文件的onWindowStageCreate方法中，会插入页面分发接口的调用，示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/_UhlVVWfTbqN19PiGUQJmg/zh-cn_image_0000002808886403.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C4065B01A374F8E9A627172D708DFB8BB64EAE23681C3E5B95B75EF8FFC2B2C)

此接口默认插入到方法开头，开发者可根据当前工程onWindowStageCreate逻辑来将此接口移动至合适的位置，保证页面能正常跳转。
