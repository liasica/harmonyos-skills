---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-more-features
title: 更多的扩展能力
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 使用模拟器运行应用 > 使用模拟器 > 更多的扩展能力
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:60573732753d33b9564effcf3df5fa45d38e4251bf1fdbf9a7d85e39f1b98780
---

模拟器支持电池、GPS、虚拟传感器等扩展能力，具体使用方式参考以下介绍。点击模拟器菜单栏的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/1CAEe0BSS-qHHRj-Z1YrHA/zh-cn_image_0000002808884821.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=EAA25424632EAFA2A59833749CA5AFF02BFB42A179FD053D5D012A2885DF0797)，打开扩展菜单栏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/o8pagNsoRfa9-StBu2tiDA/zh-cn_image_0000002808764795.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C10CCB9AFDF797CDC1965D58A4962C98B93ABC41C469546204C79DAAD41F34C4 "点击放大")

## 电池

模拟器可以模拟不同电池状态。在扩展菜单栏上点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/mN6jO-dcTNKM8N2OPHleEg/zh-cn_image_0000002779565158.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=258F4CF69B0F302C1325F3DE51D94C647350F55E410F12D87F4391B2E92A0F1B)打开电池模拟界面。在该界面，可以手动输入或拖动滑块来改变电量百分比，也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/3SbiSUYpTyysbzzhBzcpHQ/zh-cn_image_0000002779405260.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=DBC3F9BD9843A1C32C5610B1568225F9E221B4DB7DA141113B7F2A59696B9EF7)切换电池的充电/放电状态。电池具有以下三种充电状态：

* ENABLE：开启充电按钮，此时正在充电且电量未充满。
* NONE：关闭充电按钮，此时停止充电。
* FULL：开启充电按钮，且电量为100%，电量已充满。

在应用中，可以通过[@ohos.batteryInfo](../harmonyos-references/js-apis-battery-info.md)模块查询模拟器的剩余电量以及充电状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/e7aOUuM1S2qde8f6fIeoVg/zh-cn_image_0000002808764771.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C3A1322AECC898F6B9C14F074C6344CEAC1413DD06073A9BBC34C2149D7F2B40 "点击放大")

## GPS定位

模拟器可以模拟设备所处的位置。您可以打开扩展菜单，并点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/rKu6xvUsSW-MuuU2kIzI3A/zh-cn_image_0000002779405226.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3F2D94E85614A712E7270E96FF90583215985A31C9D3CEB2ED5DCF3455D1E06D)进行位置信息的设置。模拟器提供以下方式的GPS位置模拟：

* 手动设置：在该界面，可以手动输入所处位置的经度、纬度、海拔以及方位角，也可以通过点击城市下拉框，快速定位到所选城市。
* 导入：在导入界面可以注入一段时间内的连续位置信息。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/c8Ld9zR3T6CUMwNa8qZZyA/zh-cn_image_0000002779405234.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=B7BD7F68FC9702B53E19B5990D33FAB6CA0FF285B4F01B46F556E2ACE93789A8)导入本地的GPX文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/gslmBqJDRf6-kF_wFDTbqw/zh-cn_image_0000002779565222.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=85952721A0D20EB23DA7A1B3656C80CAF403D9E661C0E949B4E22792C28D29EE)即可开始模拟GPX文件中的轨迹。此外，还可以选择不同回放速率来改变移动的速度。
* 场景模拟：如果没有本地的GPX文件，可以在场景模拟界面使用预置的GPX文件。模拟器预置了户外跑步、户外骑行、驾驶导航三种场景的GPX文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/HgZ4ncRBS32jYcJ4uqrW1A/zh-cn_image_0000002808884861.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=ABA41B65E3EC03FC369E3293C8FA692140636B77B64BF582D58107A5C0CC80F0)即可开始轨迹模拟。

  **说明** 

  场景模拟功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

在应用中，您可以通过[@ohos.geoLocationManager](../harmonyos-references/js-apis-geolocationmanager.md)模块获取模拟器的位置信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/9xrrYtCfQFamfO9LKo032w/zh-cn_image_0000002808884837.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=109181FDD2EB381FAC06C00D8CBA228F9DDE5283A133B2C11BDBD73E7EEE8FB6 "点击放大")

## 虚拟传感器

模拟器提供了虚拟传感器来模拟硬件传感器的能力。在扩展菜单上点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/RpqiUR75S_GtedUwKK41WA/zh-cn_image_0000002779565132.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=94F841E0E8F09DDC0EFBECC82608ECD62C667E8AAA574AE963003F1228D45EF8)打开虚拟传感器界面。在该界面，可以调节不同的传感器来测试应用，使用[@ohos.sensor](../harmonyos-references/js-apis-sensor.md)模块监听传感器值的变化。模拟器提供以下虚拟传感器：

* 计步传感器：用于测量步数，对应的SensorId为PEDOMETER。
* 环境光传感器：用于测量光照强度，对应的SensorId为AMBIENT\_LIGHT。
* 心率传感器：用于测量心率，对应的SensorId为HEART\_RATE。从DevEco Studio 6.1.0 Beta1版本开始，Wearable设备支持心率传感器。

可以拖动滑动条或者直接在文本框输入来改变不同传感器的值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/E2hj3aq_REertx2lbUryew/zh-cn_image_0000002779405240.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D94BB8D4687845EC69D2CEC41C4746863EB6DD2A2E4F8EB36E41D8CA7377F34C "点击放大")

## 网络

模拟器的网络功能支持配置代理服务器和DNS地址，打开扩展菜单栏，并点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/6573_9fMTq2fIxCbNt6odQ/zh-cn_image_0000002808884807.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=578F9884BB9EB0713A44F42D623656E95A5A722777E515E843E036ECBAA70DB0)打开网络界面。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/2N1gI9oETACLrEhcWWw0Rw/zh-cn_image_0000002808884901.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E4CD869DA7EDC82F6C9D7B6EC87F4B3CE51AC0F24DD4D9E5E2A6F31A5E822484 "点击放大")

## 摇一摇

模拟器可以模拟用户对设备的摇一摇操作。点击工具栏上的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/RjOXQvqgQhGaCv0LdyvTEg/zh-cn_image_0000002779565142.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1092F2B02C62477C8E2CF799E0277995E4266D6BC2EC730D35CB4C83AD18F4D3)，可以模拟时长为1s的摇一摇操作。应用可以通过[@ohos.sensor](../harmonyos-references/js-apis-sensor.md)模块监听加速度传感器变化，当加速度传感器的变化量达到设定阈值时，触发摇一摇对应的业务逻辑。

**说明** 

仅phone和tablet类型的设备支持摇一摇。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/7lsEVpRpT5WVlXnuJlme4A/zh-cn_image_0000002808764733.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C140027CD45DCC60408F658EB479974E679A34A5B47FAFBF81ED17FFB64C98A "点击放大")

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

1. 在模拟器扩展菜单栏上点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/TWah0IKARqO9WiVKooBYbQ/zh-cn_image_0000002808764723.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=65B3D523250350D4A8078027782ADFD0F344AFC8C00D6DB1B38FAA7247D9000D)打开虚拟相机页面，上传一张符合规格要求的图片作为预置图片，上传后图片会被裁剪至720p。上传图片的规格要求请参考界面提示。
2. 在应用中正常调用相机拍照接口，拉起摄像头时，相机预览界面会显示预置的图片。执行拍照操作，应用获取到的即为预置图片，并保存到应用指定的输出路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/QMquLKA_RAK67dEydnCEqg/zh-cn_image_0000002808764755.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=30798F9A6A4E38D1CD526BD5C29670671799A1BD1671CEEFEF018FF3CF9842D0)

## 表冠

穿戴模拟器可以模拟表冠功能。

* 鼠标单击表冠：根据当前所在页面，单击后跳转到表盘或桌面。
* 鼠标双击表冠：进入多任务管理界面。
* 在屏幕上使用鼠标滚轮：模拟表冠旋转。从26.0.0版本开始，在表冠区域使用鼠标滚轮，也可模拟表冠旋转功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/849f7WvKQT6x7NoYArQOmw/zh-cn_image_0000002808764707.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=204B939542B07BC00ABA3BDFA0ADAAFC18E16FB8479595AEDC425AEDA51A3830 "点击放大")

## 设置

模拟器支持设置主题、语言和截屏保存路径。打开扩展菜单栏，并点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/o6MVE9oUSjOQkyqoHOuyMg/zh-cn_image_0000002779405250.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8436D557825F87BDA5A65978D0DF34383B83104563C26C5631FA9352FF94354B)打开设置面板。

* **主题****：**支持Light和Dark两种主题。
* **语言：**
  + **界面语言：**设置模拟器工具栏的语言。从DevEco Studio 6.1.0 Beta2版本开始，设置界面语言后，对所有模拟器都生效。
  + **OS语言：**从DevEco Studio 6.1.0 Beta2版本开始，支持设置模拟器镜像中的语言。此处的OS语言设置和模拟器的**设置 > 系统**中的语言设置效果相同。

  首次启动模拟器时，会根据当前计算机的系统语言，对模拟器的界面语言和OS语言进行初始化。如果计算机的系统语言不在模拟器的支持范围内，则模拟器语言默认使用英文。

  如需重置OS语言，可通过**Wipe User Data**进行清除重置。界面语言不支持重置，只能再次修改。
* **截屏保存路径：**设置模拟器工具栏的截屏功能对应的图片保存路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/4Obcw-0tQ4Ogq1X9I0eITA/zh-cn_image_0000002779405264.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2FA7B26CC2E82C243EA7BC17457F68C722C33BD143DC11EEC2E5FD879FC4D3C)

## 多屏

从DevEco Studio 6.0.0 Beta1版本开始，模拟器支持使用多屏能力，基于同一个镜像创建不同分辨率、DPI的多屏幕模拟器，满足开发者快速测试不同分辨率、DPI场景下的UI布局等需求。

### 使用约束

* 模拟器旋转功能和多屏功能互斥，不能同时使用。
* 多屏状态下扩展屏不支持使用画中画功能、不支持鼠标滚轮操作。
* Phone类型的模拟器支持多屏能力。
* 从DevEco Studio 6.0.1 Beta1版本开始，新增Tablet类型的模拟器支持多屏能力。
* 从26.0.0版本开始，新增Car类型的模拟器支持多屏能力，具体请参考[Car设备多屏能力](ide-emulator-more-features.md#section5710121118389)。

### 添加屏幕

1. 启动模拟器，点击工具栏的多屏按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/BfnaP4y3TluGTaMkxDfgqA/zh-cn_image_0000002779565230.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=BAF929D1AE6E7A0B5CD1BCD235E8A8F6DEA355A30305BE17B3935D76011FE44D)，打开多屏界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/UFL3fRyETtGLBYfUCwfoog/zh-cn_image_0000002779565184.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=41CB1916234F12E8AAA055D6BBA867C37DB61A55A2A2AE343D830111B381956E "点击放大")
2. 点击**添加**，可以选择Mate系列、Pura系列、Nova系列等产品型号，点击**应用**即可添加对应的屏幕。

   默认情况下，所有的屏幕是整体拖动和缩放的，如需单独拖动和缩放单个屏幕，请勾选界面上的**每个副屏在独立窗口中显示**，并点击**应用**按钮。从DevEco Studio 6.0.1 Beta1版本开始支持。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/-Y5JFH08T8CjWznzjPCoyA/zh-cn_image_0000002779565190.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3D2411D5CA03A188279336D919F97D00C3BE5955DD79CD593C88D0A3FDF76DC3 "点击放大")
3. 如需在多个屏幕上同时启动应用，请按界面提示，将module.json5中的launchType字段配置为multiton，具体请参考[UIAbility组件启动模式](uiability-launch-type.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/QCkpQZVrTGyb89zCkJRvKg/zh-cn_image_0000002808884879.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=111F837F12A8C492DF24A247E9A5B58CC7F4B0A607843F2AC03E9499331B8F63 "点击放大")

### 修改屏幕参数

如需自定义屏幕分辨率、DPI或尺寸，可以在多屏界面上直接修改屏幕参数，取值范围参考界面提示，修改后点击**应用**。

* **Width**：宽度，单位为px。
* **Height**：高度，单位为px。
* **DPI**：像素密度，DPI 越高，UI组件占用的像素点越多，从而提供更精细的显示效果。
* **Size：**屏幕的对角线长度，单位为inch。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/1yYiI5OHR_S7xuJbpPY4JA/zh-cn_image_0000002808764741.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3F4B9136E7E4484EE1A8C097A6ED8720BBBD54B9C3E900D11BF5E0CE2DE94F3C "点击放大")

### 使用扩展屏

* 点击扩展屏，再点击模拟器工具栏返回按键![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/fCRXzJ_6T_a_ZWfCf5m79Q/zh-cn_image_0000002808764763.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=9AFB41F98026335B263B77D5D0A65BA8B18CA221384F77C92B42D1AB91588F33)，即可返回上一级目录。按键主屏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/o84fe0fwR521nvW1-w9zmA/zh-cn_image_0000002808764713.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=475012AAD30CE66308C46EF1F0A918B90C146EDC8BC2FC7DBE6707DC896FA7B4)和最近![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/YMWrNlqSSFmD9b38MTrYiA/zh-cn_image_0000002779405210.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1BA8E09B71D2390CE06C6BC10D8B4E49E988C9AD0F24AA1D6F1A3EBB9820D8F)暂不支持在扩展屏上使用。
* 从扩展屏底部上滑，可直接清除应用。

### 删除屏幕

点击多屏界面上的删除按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/jquE4byoRte4U0aIx9_VPQ/zh-cn_image_0000002808884903.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=865912B648D564006F418F89136556E9A5009050BE0484C3F64B800FB5B2B37C)，再点击**应用**，即可删除一块屏幕。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/QCfyz130RCKrq0JoeFSoTQ/zh-cn_image_0000002779565138.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=9AB9C9AB53B3CA744D46236E4D91E0B45B095CE8355789B5D285B6D19362FE4F "点击放大")

### 使用HiCar能力

从26.0.1版本开始，Phone模拟器支持HiCar投屏能力，通过多屏界面，可模拟手机接入车机后的开发场景，支撑应用适配HiCar模式。

**使用约束**

* 仅直板机品类可使用HiCar能力，且不可与添加副屏功能共用。
* 仅支持一块HiCar屏幕，随主屏整体拖动和缩放。
* HiCar状态下不可使用旋转功能，扩展屏不支持画中画功能、不支持鼠标滚轮操作。

**添加HiCar屏幕**

1. 启动模拟器，点击工具栏的多屏按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/m1wAm_0qRU2ff2qaaFqiyQ/zh-cn_image_0000002808884907.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A40980D3CD6D7215087E74259EA5CA24181F8C7DA261D06B58301B182DDE9ED0)，打开多屏界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/Nkn98u4gRxmM5dOUVhVNcg/zh-cn_image_0000002779405162.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=30FB8DB2B815797F692E1C0C244341035AAF9A4CACE9154B3D16A869EB2C66E8 "点击放大")
2. 选择HiCar模式，点击**添加**，可选择添加默认HiCar屏幕或自定义屏幕参数，可以在多屏界面上直接修改屏幕参数，取值范围参考界面提示，修改后点击**应用**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/pKWdVqDjREeEvKctYCctPg/zh-cn_image_0000002779565198.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=B1C816B729AE2675311087317D4F930C628E3E948F7E1334FEC3289850813D24)
3. HiCar屏创建成功后，即可进行应用调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/DFcmVYtQR9i0juRRu3e93w/zh-cn_image_0000002779405170.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=890128CFFFFDA06F9BF4C8A3339692EC14D772ED86759739226597A0F18FC3E2 "点击放大")

### Car设备多屏能力

从26.0.0版本开始，Car模拟器支持多屏能力，通过添加副屏，可模拟驾驶舱主屏幕和副驾驶屏幕的场景。

在创建Car模拟器时，支持新增或删除屏幕，具体操作方式请参考[创建模拟器](ide-emulator-create.md)。新增屏幕后，启动模拟器会自动展示副屏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/cegXMdScTg6GznfKXfIzaQ/zh-cn_image_0000002779405192.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=980177AAA69EC199A66125469087A08C9A3A93B1739F8E737A7FF1CE5D5AE570)

Car模拟器的每个屏幕对应一个独立用户，主屏与副屏的操作相互独立。例如安装、调试、卸载应用，主屏和副屏都需要独立操作。

* 安装应用：可以通过拖拽安装的方式同时安装主屏和副屏，或使用[hdc命令](hdc.md#安装应用文件)分别安装，通过-u参数指定用户，主屏是100，副屏是101。
* 调试应用：调试时默认对主屏进行调试，如需调试副屏，需要单独进行[attach调试](ide-debug-arkts-attach.md)。

新增屏幕后，如果使用时不需要展示副屏，可点击模拟器工具栏多屏按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/0rn9yZ_kR6ujAjNfxX54IQ/zh-cn_image_0000002779565152.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=B493533F3553C6820739A7B6A379577EE3BA3CA77FCC1833BE97ED6146D58540)，将对应屏幕去勾选并点击**应用**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/WW5q1zSzRV-n15ba4buOaA/zh-cn_image_0000002808884869.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E79187CEA1509B337529A06E977E1103DCF0943F65124CCE127AC6F0176DC5F)

Car模拟器支持两种布局方式，书页式层叠布局和平铺式布局，可通过工具栏多屏按钮进行切换，切换后点击**应用**。

书页式层叠布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/r3MEK-EVQY-CRA-gmJQkOw/zh-cn_image_0000002808884799.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=617776723453CACB52942B0BA043B9DE071F8B6AB36F1A3C85784C4FCCAD07E8)

平铺式布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/D-UZse6GSNug6QMXW-jRFg/zh-cn_image_0000002779565240.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A179EB0536CD1BED19096E65DE1C438B08E8E07D3427D58722ADCAF4610BA5B5)
