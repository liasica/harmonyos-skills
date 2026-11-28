---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-more-features
title: 更多的扩展能力
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 使用模拟器运行应用 > 使用模拟器 > 更多的扩展能力
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:38+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:bcf90dc9cf5d25893904929abafb370df5902525f662798288568bbf25e2e88d
---

模拟器支持电池、GPS、虚拟传感器等扩展能力，具体使用方式参考以下介绍。点击模拟器菜单栏的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/gL6G_pR1QTytkEQV_prqhg/zh-cn_image_0000002808884821.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=10AA2A46D40FFA26285CBB9C639F2C52EF6BCFAD23DE706CC776516CB0C0241B)，打开扩展菜单栏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/G9IaWoYYSY-nzvKx2DO_oA/zh-cn_image_0000002808764795.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=66DE476E3BF31C2638F195B8E92105FD0C1DEA6C82058E564D93A8AC0F820CDB "点击放大")

## 电池

模拟器可以模拟不同电池状态。在扩展菜单栏上点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/8qGE-gchQROt4LOf9Fz-Wg/zh-cn_image_0000002779565158.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=2926E4CAF0962D0F88327CACB9D9C35161D9F432AAE80035E6B976A2C9AA5055)打开电池模拟界面。在该界面，可以手动输入或拖动滑块来改变电量百分比，也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/eMeVNjwRSaiZX8TjHCikJQ/zh-cn_image_0000002779405260.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=2CF1297EE448A70328DDE98B73BA8A356CE5D99CAAAA2FD70FD3189198E6D316)切换电池的充电/放电状态。电池具有以下三种充电状态：

* ENABLE：开启充电按钮，此时正在充电且电量未充满。
* NONE：关闭充电按钮，此时停止充电。
* FULL：开启充电按钮，且电量为100%，电量已充满。

在应用中，可以通过[@ohos.batteryInfo](../harmonyos-references/js-apis-battery-info.md)模块查询模拟器的剩余电量以及充电状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/VdwBYqN8S52Cqsh5B0METQ/zh-cn_image_0000002808764771.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=020945611132B5B086223716C5D6DF4D229DD3EC672F0E9846F6D8CC34767377 "点击放大")

## GPS定位

模拟器可以模拟设备所处的位置。您可以打开扩展菜单，并点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/Q6jVJ6LFTLmJA2rHwOvp5g/zh-cn_image_0000002779405226.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=A2F33B872C98AD7ADCF1744043C03E8DBDA9D3BB23F6376C239123BEB501E7D4)进行位置信息的设置。模拟器提供以下方式的GPS位置模拟：

* 手动设置：在该界面，可以手动输入所处位置的经度、纬度、海拔以及方位角，也可以通过点击城市下拉框，快速定位到所选城市。
* 导入：在导入界面可以注入一段时间内的连续位置信息。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/dqPeoeg2TH-oziZ3HonRfw/zh-cn_image_0000002779405234.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=86563E444BDB30DD6AD1677CAFD1E64B8FAC5C96FCAABEDB33C6C57791654830)导入本地的GPX文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/HXH64a9TQp2AHvHmtU8yLg/zh-cn_image_0000002779565222.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=947DA948072556218C1C93A9BAFCA873F6049A687F64BFA387D144BDFD7354BA)即可开始模拟GPX文件中的轨迹。此外，还可以选择不同回放速率来改变移动的速度。
* 场景模拟：如果没有本地的GPX文件，可以在场景模拟界面使用预置的GPX文件。模拟器预置了户外跑步、户外骑行、驾驶导航三种场景的GPX文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/pCljYOgBTU6bRyFG69bR2Q/zh-cn_image_0000002808884861.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4C940BD808178AC061758BF08AFEFD0E51E7342E4EFD431EC9D3C25E4601832)即可开始轨迹模拟。

  **说明** 

  场景模拟功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

在应用中，您可以通过[@ohos.geoLocationManager](../harmonyos-references/js-apis-geolocationmanager.md)模块获取模拟器的位置信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/yZwVUKUtSu6gdbPpi9x-hQ/zh-cn_image_0000002808884837.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C29E63FA87B7BBDB89A678AB97E596FD583DCA122FD1EE229EBAD5CF79D7AAC "点击放大")

## 虚拟传感器

模拟器提供了虚拟传感器来模拟硬件传感器的能力。在扩展菜单上点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/CWzga6S6T1KrvdSQt1ijIw/zh-cn_image_0000002779565132.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=864B4C6B7B4338D2518F55BDD8A1030A07C625831A500C123E712970AD93D234)打开虚拟传感器界面。在该界面，可以调节不同的传感器来测试应用，使用[@ohos.sensor](../harmonyos-references/js-apis-sensor.md)模块监听传感器值的变化。模拟器提供以下虚拟传感器：

* 计步传感器：用于测量步数，对应的SensorId为PEDOMETER。
* 环境光传感器：用于测量光照强度，对应的SensorId为AMBIENT\_LIGHT。
* 心率传感器：用于测量心率，对应的SensorId为HEART\_RATE。从DevEco Studio 6.1.0 Beta1版本开始，Wearable设备支持心率传感器。

可以拖动滑动条或者直接在文本框输入来改变不同传感器的值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/dMoXpOBLQxSAV0jv1bv45Q/zh-cn_image_0000002779405240.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=C1FC5DA6EEC969E43D7F569197C2BB5F4C4B6F04D1E9F01175AD78B527447333 "点击放大")

## 网络

模拟器的网络功能支持配置代理服务器和DNS地址，打开扩展菜单栏，并点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/-XOP_wlzRU6s_i32rT9XFA/zh-cn_image_0000002808884807.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=093E69E24E773764F2923562E382135D7503BE81BBD85E82F8F57A5F232D4483)打开网络界面。

**说明** 

代理和DNS设置不可同时使用。

**代理设置**

模拟器可以将网络请求代理到代理服务器，利用代理服务器请求目标服务器。从而满足以下开发场景：

* 开发者处于内网环境，希望通过设置代理的方式访问外网；
* 开发者已经在DevEco Studio上配置了网络代理，不希望在模拟器上重复配置代理；
* 开发者需要将网络请求代理到三方抓包工具，方便查看请求信息。

模拟器提供以下三种代理模式：

* **使用DevEco Studio代理：**读取并应用[DevEco Studio上的网络代理配置](ide-environment-config.md#section10369436568)。

  **说明** 

  使用DevEco Studio代理时，模拟器不支持以下能力：

  + 不支持**自动检测代理（Auto-detect proxy settings）和SOCKS代理**，会自动切换到无代理模式；
  + 不支持**HTTP代理**下的**No proxy for**功能。
* **无代理：**不使用代理，即发送网络请求时会直接请求目标服务器。
* **手工配置代理：**配置代理服务器的信息，将网络请求代理到代理服务器上。

配置代理后，可以点击**Check Connection**对当前的代理配置进行校验，并点击**Apply**按钮进行保存。在发起https请求时，需要安装网站的数字证书，请参考[使用模拟器发起HTTPS请求时如何安装数字证书](../harmonyos-faqs/network-kit-faq-0005.md)。

**DNS设置**

从DevEco Studio 6.1.0 Beta2版本开始，新增DNS设置功能，开发者可以手动设置DNS服务器用于域名解析，设置后点击**Apply**提交。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/zSATXcVOSfi2CW-_dZcUKw/zh-cn_image_0000002808884901.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=86CA1589A14768E79697E790B544F790BCAA8801F1968BBD43D03396C2999382 "点击放大")

## 摇一摇

模拟器可以模拟用户对设备的摇一摇操作。点击工具栏上的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/7_bwsP9oTm-bAR1I9nu20Q/zh-cn_image_0000002779565142.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=F93DEB25490E402A1960F622417EF6C1B8C084B5A7C3A8F814D0D10281ADDFCA)，可以模拟时长为1s的摇一摇操作。应用可以通过[@ohos.sensor](../harmonyos-references/js-apis-sensor.md)模块监听加速度传感器变化，当加速度传感器的变化量达到设定阈值时，触发摇一摇对应的业务逻辑。

**说明** 

仅phone和tablet类型的设备支持摇一摇。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/xIf2gfvQRGuj_M3yvCzwSA/zh-cn_image_0000002808764733.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=257DAAE143A4A2773B0CB513F95C193F612D50793F67630D024DF4468E1C5BB1 "点击放大")

## 音频输入

模拟器支持Audio Kit（音频服务）提供的音频输入能力，可以使用本地计算机上的麦克风设备向模拟器中传输音频数据。使用步骤如下：

1. 首先，请确保本地计算机已连接上麦克风设备。
2. 应用调用Audio Kit提供的API接口（如AudioCapturer、OHAudio）开始接收音频数据。
3. 使用本地麦克风进行语音输入。

模拟器上的应用在调用相关API时，推荐使用如下格式的音频流信息格式，以保证清晰流畅的音质。

| 音频流信息 | 推荐值 |
| --- | --- |
| samplingRate（采样率） | 48000Hz |
| channels（通道数） | 2 |
| sampleFormat（采样格式） | 带符号的16位整数 |
| encodingType（编码格式） | PCM编码 |

## 摄像头

从DevEco Studio 5.1.0 Release版本开始，模拟器支持调用本地计算机摄像头。例如，通过调用Camera Kit（相机服务）提供的接口，可以在模拟器上实现拍照和预览功能；通过Scan Kit（统一扫码服务），在API 20及以上版本的模拟器上实现扫码功能，等等。其他依赖摄像头能力的Kit，请参考对应Kit简介中的模拟器支持情况。

模拟器调用摄像头的开发步骤如下：

1. 请确保本地计算机上存在可用的摄像头。从26.0.0版本开始，支持通过USB外接摄像头，仅支持720p规格的摄像头设备。
2. 应用调用对应Kit提供的API接口，通过电脑摄像头实现预览、拍照、扫码等功能。

**说明** 

* 使用模拟器开发相机时，[相机配置信息](../harmonyos-references/arkts-apis-camera-i.md#profile)请使用：RGBA\_8888格式、1280 \* 720分辨率。
* 使用USB外接摄像头时，如使用过程中插拔了USB，需要在模拟器中清理应用重新启动才可重新识别USB摄像头。

对于缺少摄像头的场景，从26.0.0版本开始，模拟器提供虚拟相机功能。通过加载预置图片作为相机输入源，开发者可在无摄像头的环境中完整模拟相机拍照流程，完成相机相关的应用开发与调试。

1. 在模拟器扩展菜单栏上点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/I07vhRihSbahw-_k2qnvPQ/zh-cn_image_0000002808764723.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5E6B8B6C434101C5A1987C2106E795CF628C521107864860B7184EBE39270A4)打开虚拟相机页面，上传一张符合规格要求的图片作为预置图片，上传后图片会被裁剪至720p。上传图片的规格要求请参考界面提示。
2. 在应用中正常调用相机拍照接口，拉起摄像头时，相机预览界面会显示预置的图片。执行拍照操作，应用获取到的即为预置图片，并保存到应用指定的输出路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/AD4IJ-kWQh6u7sI_TPKIfg/zh-cn_image_0000002808764755.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C59764D24FCD6E9EE6AB8ABE263BBD7B11B2102F102007DFBC4077745061F64)

## 表冠

穿戴模拟器可以模拟表冠功能。

* 鼠标单击表冠：根据当前所在页面，单击后跳转到表盘或桌面。
* 鼠标双击表冠：进入多任务管理界面。
* 在屏幕上使用鼠标滚轮：模拟表冠旋转。从26.0.0版本开始，在表冠区域使用鼠标滚轮，也可模拟表冠旋转功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/pA-OCoGzQBautEb2kalmBQ/zh-cn_image_0000002808764707.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC11749C2C606F79259A7A71097BABB6BAE877A3473D666693D3ADCF3BD4FFC1 "点击放大")

## 设置

模拟器支持设置主题、语言和截屏保存路径。打开扩展菜单栏，并点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/Nu4MAdFHTJm18EMegE7_fg/zh-cn_image_0000002779405250.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=B217AF75373F7332D6ED05C8041C6CE24C0A0D307283CEDA20112642ABF6DCD8)打开设置面板。

* **主题****：**支持Light和Dark两种主题。
* **语言：**
  + **界面语言：**设置模拟器工具栏的语言。从DevEco Studio 6.1.0 Beta2版本开始，设置界面语言后，对所有模拟器都生效。
  + **OS语言：**从DevEco Studio 6.1.0 Beta2版本开始，支持设置模拟器镜像中的语言。此处的OS语言设置和模拟器的**设置 > 系统**中的语言设置效果相同。

  首次启动模拟器时，会根据当前计算机的系统语言，对模拟器的界面语言和OS语言进行初始化。如果计算机的系统语言不在模拟器的支持范围内，则模拟器语言默认使用英文。

  如需重置OS语言，可通过**Wipe User Data**进行清除重置。界面语言不支持重置，只能再次修改。
* **截屏保存路径：**设置模拟器工具栏的截屏功能对应的图片保存路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/ha_H-mAARnSQ4_qEUEsz2w/zh-cn_image_0000002779405264.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=3884D292BBDE3004A875A235A463C3BA73C6BDC3162F63BAF0A69B3897D5EE11)

## 多屏

从DevEco Studio 6.0.0 Beta1版本开始，模拟器支持使用多屏能力，基于同一个镜像创建不同分辨率、DPI的多屏幕模拟器，满足开发者快速测试不同分辨率、DPI场景下的UI布局等需求。

### 使用约束

* 模拟器旋转功能和多屏功能互斥，不能同时使用。
* 多屏状态下扩展屏不支持使用画中画功能、不支持鼠标滚轮操作。
* Phone类型的模拟器支持多屏能力。
* 从DevEco Studio 6.0.1 Beta1版本开始，新增Tablet类型的模拟器支持多屏能力。
* 从26.0.0版本开始，新增Car类型的模拟器支持多屏能力，具体请参考[Car设备多屏能力](ide-emulator-more-features.md#section5710121118389)。

### 添加屏幕

1. 启动模拟器，点击工具栏的多屏按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/X1XX2RNATpqsYx7iiTHang/zh-cn_image_0000002779565230.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=82DB847B99CBB3DFF204821E4248F8BED65B2B8617271FCDBFB52EEF22387DF6)，打开多屏界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/sfc3m2cgRSmMvGD1O3GVmA/zh-cn_image_0000002779565184.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD3A1D475F64A2380EA3981F113BB208BA2F187AD5FED01974E2D8F9470E35BA "点击放大")
2. 点击**添加**，可以选择Mate系列、Pura系列、Nova系列等产品型号，点击**应用**即可添加对应的屏幕。

   默认情况下，所有的屏幕是整体拖动和缩放的，如需单独拖动和缩放单个屏幕，请勾选界面上的**每个副屏在独立窗口中显示**，并点击**应用**按钮。从DevEco Studio 6.0.1 Beta1版本开始支持。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/zJax0hduRSmaS7dlzhuwjA/zh-cn_image_0000002779565190.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=30505317B789057AC164368EBCD0F5375582087FC7006AC6E6C6A6FC110D7E26 "点击放大")
3. 如需在多个屏幕上同时启动应用，请按界面提示，将module.json5中的launchType字段配置为multiton，具体请参考[UIAbility组件启动模式](uiability-launch-type.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/EhiRZyDQSUOx9gCeT2O9gA/zh-cn_image_0000002808884879.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=3EDCD562134DBEF24C57321B70E7D9643C7677FC8C8A3C5716C48B2109AB1163 "点击放大")

### 修改屏幕参数

如需自定义屏幕分辨率、DPI或尺寸，可以在多屏界面上直接修改屏幕参数，取值范围参考界面提示，修改后点击**应用**。

* **Width**：宽度，单位为px。
* **Height**：高度，单位为px。
* **DPI**：像素密度，DPI 越高，UI组件占用的像素点越多，从而提供更精细的显示效果。
* **Size：**屏幕的对角线长度，单位为inch。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/E8uuqX8ZRLi4aX2-eqRr4A/zh-cn_image_0000002808764741.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=11FA1552FC19BEC775836D61DC45F46E86F80F4E507DBE66A937FEB5CB5C5016 "点击放大")

### 使用扩展屏

* 点击扩展屏，再点击模拟器工具栏返回按键![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/YtdLeU7ZQSWdDiiAwIStSQ/zh-cn_image_0000002808764763.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=37658584191FBEAD8065CC4128CABED8EF767DC340CA155F2A441382DFC89E5E)，即可返回上一级目录。按键主屏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/MakW31YoSNKn76Q-wKxZRw/zh-cn_image_0000002808764713.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=615FBF6EF1F2A2BECDA884D5EE25500BE9722D4BF1C083B5A1C3B2CE83898621)和最近![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/NbfRsKhLSvWSR3Xa82fQtw/zh-cn_image_0000002779405210.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=0742123E429F57BC9FF572A47146BBC2C5A472AAED416B2C4D7DAB074D12931A)暂不支持在扩展屏上使用。
* 从扩展屏底部上滑，可直接清除应用。

### 删除屏幕

点击多屏界面上的删除按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/LNvjrmXWRTKUMv_lMRnolQ/zh-cn_image_0000002808884903.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E122E89EAECF024DC3DAA2C00B3DC14BFE422CAA21A6D6895EA1C13168C29B9)，再点击**应用**，即可删除一块屏幕。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/DfwmW0PKQUO5fVV23oFk-w/zh-cn_image_0000002779565138.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=E086B3B06F6BB32F502E45313EDDB8CA7833B7462D6201DC0073F0FD26F7BCCB "点击放大")

### 使用HiCar能力

从26.0.1版本开始，Phone模拟器支持HiCar投屏能力，通过多屏界面，可模拟手机接入车机后的开发场景，支撑应用适配HiCar模式。

**使用约束**

* 仅直板机品类可使用HiCar能力，且不可与添加副屏功能共用。
* 仅支持一块HiCar屏幕，随主屏整体拖动和缩放。
* HiCar状态下不可使用旋转功能，扩展屏不支持画中画功能、不支持鼠标滚轮操作。

**添加HiCar屏幕**

1. 启动模拟器，点击工具栏的多屏按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/btVQXNVbRG2Mb3JKLhfMCg/zh-cn_image_0000002808884907.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=2D8C4542E7562AD7971411186FEB62FF51C277E0690D2D43ED1879539780F7D7)，打开多屏界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/TG_PrIm1S2WEpSIoCpniPQ/zh-cn_image_0000002779405162.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=9243D6E99DA849E1D787D581C9DDFA7AADA081A4A762CD63AB4399701A1C6340 "点击放大")
2. 选择HiCar模式，点击**添加**，可选择添加默认HiCar屏幕或自定义屏幕参数，可以在多屏界面上直接修改屏幕参数，取值范围参考界面提示，修改后点击**应用**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/f4dliXytSu-ggZc2p2fxiA/zh-cn_image_0000002779565198.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E7659DD5E3021E57B0F9ECE7C490E17B9E1B2CD47EE9449ED98227974EDDB7A)
3. HiCar屏创建成功后，即可进行应用调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/fz3zPDbhSBOfmo8aoZUrYw/zh-cn_image_0000002779405170.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=3A886CC7F33F7264F2BD98C9883B8D524D211A1EF6D4A19DD9D587BF52B1DE12 "点击放大")

### Car设备多屏能力

从26.0.0版本开始，Car模拟器支持多屏能力，通过添加副屏，可模拟驾驶舱主屏幕和副驾驶屏幕的场景。

在创建Car模拟器时，支持新增或删除屏幕，具体操作方式请参考[创建模拟器](ide-emulator-create.md)。新增屏幕后，启动模拟器会自动展示副屏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/e2YuuHl-QbSUnjHe7P6YaA/zh-cn_image_0000002779405192.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA60164C8505DB8ACEB7BDCAE9232CF8C3BA125B553DC4659024F29333CE2238)

Car模拟器的每个屏幕对应一个独立用户，主屏与副屏的操作相互独立。例如安装、调试、卸载应用，主屏和副屏都需要独立操作。

* 安装应用：可以通过拖拽安装的方式同时安装主屏和副屏，或使用[hdc命令](hdc.md#安装应用文件)分别安装，通过-u参数指定用户，主屏是100，副屏是101。
* 调试应用：调试时默认对主屏进行调试，如需调试副屏，需要单独进行[attach调试](ide-debug-arkts-attach.md)。

新增屏幕后，如果使用时不需要展示副屏，可点击模拟器工具栏多屏按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/ZYKasumjT3O29V3U12DVwg/zh-cn_image_0000002779565152.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=76A1F098C4151BBA87126185AD3B4926DF89E5D77FAEAACDB39F4963828459F5)，将对应屏幕去勾选并点击**应用**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/5Rcpcwb8R16idl4u2IF0cQ/zh-cn_image_0000002808884869.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=235A0255D884B8100D18FF1746140CE33ED3982BDF5DD3A6AB4A35A0F72CA5BF)

Car模拟器支持两种布局方式，书页式层叠布局和平铺式布局，可通过工具栏多屏按钮进行切换，切换后点击**应用**。

书页式层叠布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/KEQl2eP2Q2a_Acwh6hpRHA/zh-cn_image_0000002808884799.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=58CF0144D5970F9BFA68C9219F6162F23ADD21CBD6C28FC2C117647580295107)

平铺式布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/f6lhbQgEQ8qM6e8qK4nZ2A/zh-cn_image_0000002779565240.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=07851C8A2D7549B67D9AF5EC82947A96736488734F2AABBD938216AFA18AEDF2)
