---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-more-features
title: 更多的扩展能力
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 使用模拟器运行应用 > 使用模拟器 > 更多的扩展能力
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:58+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a80299bf684a7e23eebce6b85c60dbb17c4e80d433c19276f5732d472fde4452
---

模拟器支持电池、GPS、虚拟传感器等扩展能力，具体使用方式参考以下介绍。点击模拟器菜单栏的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/_BXyLrdeS8GeBIwSz3faRg/zh-cn_image_0000002808884821.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=D9FA3BB7EABE22C69660577E68C9D6B42CD007863D54E51F220DA72FFA3F8843)，打开扩展菜单栏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/cjMPmMhSRgifqIt3Z57prw/zh-cn_image_0000002808764795.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=79E6E27F72D115C9523908387B0338322954A2CBF464EF70182D7CE52C326723 "点击放大")

## 电池

模拟器可以模拟不同电池状态。在扩展菜单栏上点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/2Ew_iBhSR9-AlRAEXZbL5g/zh-cn_image_0000002779565158.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=1718619DAD7960199CE1352801E0C4A13B8982DA02FD31FD53D7F3CD5D286E1A)打开电池模拟界面。在该界面，可以手动输入或拖动滑块来改变电量百分比，也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/vKnaD6rlSDiepCIIaeLPdQ/zh-cn_image_0000002779405260.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=2374F51B77405CAA0AD33B6F73F983DFFE3D8AF8074A52ECC7FE3E2ECBEB58D1)切换电池的充电/放电状态。电池具有以下三种充电状态：

* ENABLE：开启充电按钮，此时正在充电且电量未充满。
* NONE：关闭充电按钮，此时停止充电。
* FULL：开启充电按钮，且电量为100%，电量已充满。

在应用中，可以通过[@ohos.batteryInfo](../harmonyos-references/js-apis-battery-info.md)模块查询模拟器的剩余电量以及充电状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/q2v3bGyFSL6ww5owQLYIaA/zh-cn_image_0000002808764771.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=6C834CED31B03AB3CDC931B635B841FB90EEEDD2453C15BF131D5A7EA3DF4342 "点击放大")

## GPS定位

模拟器可以模拟设备所处的位置。您可以打开扩展菜单，并点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/_AP3uATeS_6eQA73jdkONw/zh-cn_image_0000002779405226.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=5449D72387FEC5CA00A427331958AB36BC991C0CF0ADFDAC3874753F087B0569)进行位置信息的设置。模拟器提供以下方式的GPS位置模拟：

* 手动设置：在该界面，可以手动输入所处位置的经度、纬度、海拔以及方位角，也可以通过点击城市下拉框，快速定位到所选城市。
* 导入：在导入界面可以注入一段时间内的连续位置信息。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/rE6SeoGRQKuoZF752FFVTA/zh-cn_image_0000002779405234.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=A70CCD6761C6864E41D7D41C4FCD56F1874CBF224DEE3C2961E1D83D0D10D7B4)导入本地的GPX文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/ws5gts6cSnypK1J1Lo-Bag/zh-cn_image_0000002779565222.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=3ED0E1FD75E3D4B6EC81658CF8E3B3E54EFC70081E1891305D1DD34AA5A3FEAF)即可开始模拟GPX文件中的轨迹。此外，还可以选择不同回放速率来改变移动的速度。
* 场景模拟：如果没有本地的GPX文件，可以在场景模拟界面使用预置的GPX文件。模拟器预置了户外跑步、户外骑行、驾驶导航三种场景的GPX文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/-g2xn84TSlyplZTW3j1VIw/zh-cn_image_0000002808884861.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=A013FEDE642C06C851959A13436FAC5347DA51FB7F567B97BB88C61437D56C03)即可开始轨迹模拟。

  **说明** 

  场景模拟功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

在应用中，您可以通过[@ohos.geoLocationManager](../harmonyos-references/js-apis-geolocationmanager.md)模块获取模拟器的位置信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/cFSPQmE9SROH8bB_OmvUnA/zh-cn_image_0000002808884837.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=75EA7D7DF0659DA88C93555C01BB87CB6001D0884A9CABCD9B6DBFFBDBC76499 "点击放大")

## 虚拟传感器

模拟器提供了虚拟传感器来模拟硬件传感器的能力。在扩展菜单上点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/Uu8PGj1GQDuBYtMMmcSAog/zh-cn_image_0000002779565132.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B5E27DD6F1A311BE8500045C5635A65E3972FD07C63E7EBFEB8B2AC57A1181E)打开虚拟传感器界面。在该界面，可以调节不同的传感器来测试应用，使用[@ohos.sensor](../harmonyos-references/js-apis-sensor.md)模块监听传感器值的变化。模拟器提供以下虚拟传感器：

* 计步传感器：用于测量步数，对应的SensorId为PEDOMETER。
* 环境光传感器：用于测量光照强度，对应的SensorId为AMBIENT\_LIGHT。
* 心率传感器：用于测量心率，对应的SensorId为HEART\_RATE。从DevEco Studio 6.1.0 Beta1版本开始，Wearable设备支持心率传感器。

可以拖动滑动条或者直接在文本框输入来改变不同传感器的值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/lGM7TOJySY6SostaPZnWhw/zh-cn_image_0000002779405240.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=7939E6FA9A46ADDCCD6143E29191BD7B04362064E5EF895C91508DA9FA2C4444 "点击放大")

## 网络

模拟器的网络功能支持配置代理服务器和DNS地址，打开扩展菜单栏，并点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/U4csm-eCTKCD5QuN5sE6xA/zh-cn_image_0000002808884807.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=B4788A11B460AC5E4400E9EAE0A22DBAE0DAB3A1BD462C3E3FFCEC2699C51E35)打开网络界面。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/qfemUbeYSIidOwvRn4-zug/zh-cn_image_0000002808884901.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=316C101CE536EF0D3B29A7259B12C5A3424E8668F5C4F53C47EF1C78E1FA7173 "点击放大")

## 摇一摇

模拟器可以模拟用户对设备的摇一摇操作。点击工具栏上的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/ucSnm4VnScyTZJ6KZilNeQ/zh-cn_image_0000002779565142.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=B064FE42574259C26A5C9092B7FD639FF4EFA5852AF0FB4A8A44CDB7619F6126)，可以模拟时长为1s的摇一摇操作。应用可以通过[@ohos.sensor](../harmonyos-references/js-apis-sensor.md)模块监听加速度传感器变化，当加速度传感器的变化量达到设定阈值时，触发摇一摇对应的业务逻辑。

**说明** 

仅phone和tablet类型的设备支持摇一摇。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/FDPm78atTdC7oVONUTBipQ/zh-cn_image_0000002808764733.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=B9D5A7468F50574B77A880019EF0ECFD7CAA927D0FC1461AB48C27684CFDAD2C "点击放大")

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

1. 在模拟器扩展菜单栏上点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/52f5TZYOQHaMH60UuwuVAQ/zh-cn_image_0000002808764723.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=B2B0D80ED8BBE56FC8821B926125B6B22FD1E554FC566EFA986969810F6BE62C)打开虚拟相机页面，上传一张符合规格要求的图片作为预置图片，上传后图片会被裁剪至720p。上传图片的规格要求请参考界面提示。
2. 在应用中正常调用相机拍照接口，拉起摄像头时，相机预览界面会显示预置的图片。执行拍照操作，应用获取到的即为预置图片，并保存到应用指定的输出路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/hL5PcKFtQTi84vjJdrei-A/zh-cn_image_0000002808764755.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=1D70F0FDFC4699BBD025E2EF5346C4CA275F60B63407687DA5FEA65C94589F66)

## 表冠

穿戴模拟器可以模拟表冠功能。

* 鼠标单击表冠：根据当前所在页面，单击后跳转到表盘或桌面。
* 鼠标双击表冠：进入多任务管理界面。
* 在屏幕上使用鼠标滚轮：模拟表冠旋转。从26.0.0版本开始，在表冠区域使用鼠标滚轮，也可模拟表冠旋转功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/S7SN209uTtGcVvquYyLLYA/zh-cn_image_0000002808764707.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=889EE5D28070CC135443AA4CF75173004DEE5F360CD80DD0414350B5BA2AE8C0 "点击放大")

## 设置

模拟器支持设置主题、语言和截屏保存路径。打开扩展菜单栏，并点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/JyAww2xiQXOGMEx-xsygIw/zh-cn_image_0000002779405250.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=383FDAAED35E62CD040B3C4A065CCD53BD7C10B45773380264ECE90D9CC24EA4)打开设置面板。

* **主题****：**支持Light和Dark两种主题。
* **语言：**
  + **界面语言：**设置模拟器工具栏的语言。从DevEco Studio 6.1.0 Beta2版本开始，设置界面语言后，对所有模拟器都生效。
  + **OS语言：**从DevEco Studio 6.1.0 Beta2版本开始，支持设置模拟器镜像中的语言。此处的OS语言设置和模拟器的**设置 > 系统**中的语言设置效果相同。

  首次启动模拟器时，会根据当前计算机的系统语言，对模拟器的界面语言和OS语言进行初始化。如果计算机的系统语言不在模拟器的支持范围内，则模拟器语言默认使用英文。

  如需重置OS语言，可通过**Wipe User Data**进行清除重置。界面语言不支持重置，只能再次修改。
* **截屏保存路径：**设置模拟器工具栏的截屏功能对应的图片保存路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/HLH1v5RKT4-6sB0zgTlYCA/zh-cn_image_0000002779405264.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=330B4E0E0CEB58D2E8E9BAB8E12C83A958D44FBB743465BB597CDE95758B7933)

## 多屏

从DevEco Studio 6.0.0 Beta1版本开始，模拟器支持使用多屏能力，基于同一个镜像创建不同分辨率、DPI的多屏幕模拟器，满足开发者快速测试不同分辨率、DPI场景下的UI布局等需求。

### 使用约束

* 模拟器旋转功能和多屏功能互斥，不能同时使用。
* 多屏状态下扩展屏不支持使用画中画功能、不支持鼠标滚轮操作。
* Phone类型的模拟器支持多屏能力。
* 从DevEco Studio 6.0.1 Beta1版本开始，新增Tablet类型的模拟器支持多屏能力。
* 从26.0.0版本开始，新增Car类型的模拟器支持多屏能力，具体请参考[Car设备多屏能力](ide-emulator-more-features.md#section5710121118389)。

### 添加屏幕

1. 启动模拟器，点击工具栏的多屏按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/e5XSJ45HTpqgC9C39c1pOQ/zh-cn_image_0000002779565230.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=B71C155CD6A4E1082516A7674198D6D1CFEB16DD92636E2AA100B89A0FE5F6EA)，打开多屏界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/qiKo_nG-Tkqnx3wEtNAjbA/zh-cn_image_0000002779565184.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3769E6B2B47C9A8F29DC8EAAA955E8D464FD735206AAFEE0F7D8EA64BB9BE4E "点击放大")
2. 点击**添加**，可以选择Mate系列、Pura系列、Nova系列等产品型号，点击**应用**即可添加对应的屏幕。

   默认情况下，所有的屏幕是整体拖动和缩放的，如需单独拖动和缩放单个屏幕，请勾选界面上的**每个副屏在独立窗口中显示**，并点击**应用**按钮。从DevEco Studio 6.0.1 Beta1版本开始支持。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/_1yE1TvHQVSrhP-1FffrjQ/zh-cn_image_0000002779565190.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E529B75466A245E63212E6E831BAD4243BC509A3547588AA60F4CAF481C59D5 "点击放大")
3. 如需在多个屏幕上同时启动应用，请按界面提示，将module.json5中的launchType字段配置为multiton，具体请参考[UIAbility组件启动模式](uiability-launch-type.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/uPoYZbmJSeqmagIX7UeH2Q/zh-cn_image_0000002808884879.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=2679BB098029AB8E1641CF170728E15CBC42B1D83744EE3225A2309CFE9AB1E2 "点击放大")

### 修改屏幕参数

如需自定义屏幕分辨率、DPI或尺寸，可以在多屏界面上直接修改屏幕参数，取值范围参考界面提示，修改后点击**应用**。

* **Width**：宽度，单位为px。
* **Height**：高度，单位为px。
* **DPI**：像素密度，DPI 越高，UI组件占用的像素点越多，从而提供更精细的显示效果。
* **Size：**屏幕的对角线长度，单位为inch。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/6LtM8HBOQJOJHnDku3xDhA/zh-cn_image_0000002808764741.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=E41278B09849F41F1FB1AC64000F4D272F90C2A56189F393B9EF3D01CC589075 "点击放大")

### 使用扩展屏

* 点击扩展屏，再点击模拟器工具栏返回按键![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/X8cNkqmNRM2FIk48FYkPZg/zh-cn_image_0000002808764763.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=8FFFE94497DC12444CDF88E20A1C4699D76EF1A1DD6B5427256EA177808D091C)，即可返回上一级目录。按键主屏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/HMt168A-ScqwfzFq7U-QxA/zh-cn_image_0000002808764713.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=5893D83B270C24D02E8E5A966D33F985F551F7BCBEFECE58224F23EB9320941F)和最近![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/LDjHwRLbRQOFqr6BY3l3gg/zh-cn_image_0000002779405210.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=047ABD8CD855DF9E31370A514C15B585B6C9DACB59844756B20C6441DA75DCA9)暂不支持在扩展屏上使用。
* 从扩展屏底部上滑，可直接清除应用。

### 删除屏幕

点击多屏界面上的删除按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/WHZIeDJBShav4T5YwkJ0Ew/zh-cn_image_0000002808884903.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A170610EC3E610A4D9E2D786748B1EF660B2F21249FCB3BFDA791F42CFBB621)，再点击**应用**，即可删除一块屏幕。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/KKKzZNLtSpe4-z4eZHz19Q/zh-cn_image_0000002779565138.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=DBFBF23B8BE69A44B8B14D7B9EB8E281256B39106745EB351181BB46DFA5FE60 "点击放大")

### 使用HiCar能力

从26.0.1版本开始，Phone模拟器支持HiCar投屏能力，通过多屏界面，可模拟手机接入车机后的开发场景，支撑应用适配HiCar模式。

**使用约束**

* 仅直板机品类可使用HiCar能力，且不可与添加副屏功能共用。
* 仅支持一块HiCar屏幕，随主屏整体拖动和缩放。
* HiCar状态下不可使用旋转功能，扩展屏不支持画中画功能、不支持鼠标滚轮操作。

**添加HiCar屏幕**

1. 启动模拟器，点击工具栏的多屏按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/bvCs2Pl-S0WCogKNoTXiDA/zh-cn_image_0000002808884907.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=1F89153C1A8BF2673F8990A39882163C41DD94437FABED8343F00421D19FE17D)，打开多屏界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/yd-uTGUISt6dv_fwo1zsmQ/zh-cn_image_0000002779405162.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=58A278B588A337A5378EE2CA474F1AC1FB4267DDE250735DCCBA3CA8C160BA00 "点击放大")
2. 选择HiCar模式，点击**添加**，可选择添加默认HiCar屏幕或自定义屏幕参数，可以在多屏界面上直接修改屏幕参数，取值范围参考界面提示，修改后点击**应用**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/1jnAesfxRO6c_eO1mmUo8Q/zh-cn_image_0000002779565198.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=FBC0A64867258A599DD46D3181CDD2F4E8AF78E45C2AF06F693F05D41B84182F)
3. HiCar屏创建成功后，即可进行应用调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/th21LdFWSauw3hAU3af9Vg/zh-cn_image_0000002779405170.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF4218CDB0CECEA3A34868BB6D3832D06D9983E94C73FC556FC77230F1FC4EE0 "点击放大")

### Car设备多屏能力

从26.0.0版本开始，Car模拟器支持多屏能力，通过添加副屏，可模拟驾驶舱主屏幕和副驾驶屏幕的场景。

在创建Car模拟器时，支持新增或删除屏幕，具体操作方式请参考[创建模拟器](ide-emulator-create.md)。新增屏幕后，启动模拟器会自动展示副屏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/e0TG2gxaRH-E_f6TuUUx4w/zh-cn_image_0000002779405192.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=766ED4791C01B2AE8445257B719168B6A86C2853F405A826578B941517216B78)

Car模拟器的每个屏幕对应一个独立用户，主屏与副屏的操作相互独立。例如安装、调试、卸载应用，主屏和副屏都需要独立操作。

* 安装应用：可以通过拖拽安装的方式同时安装主屏和副屏，或使用[hdc命令](hdc.md#安装应用文件)分别安装，通过-u参数指定用户，主屏是100，副屏是101。
* 调试应用：调试时默认对主屏进行调试，如需调试副屏，需要单独进行[attach调试](ide-debug-arkts-attach.md)。

新增屏幕后，如果使用时不需要展示副屏，可点击模拟器工具栏多屏按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/440aBe_lQkm1xUlWy7M6lQ/zh-cn_image_0000002779565152.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=BFCFA22B562D571A1B74F86B3700BA11FC6D5608701CFB9536F7AB3ABC17645A)，将对应屏幕去勾选并点击**应用**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/F996I2AJSJm0J17WtAqkxg/zh-cn_image_0000002808884869.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=BAA0764EB6AC85C43A068393FC5C3AA4163A14C8D00CEF2295EEE7D41A31536B)

Car模拟器支持两种布局方式，书页式层叠布局和平铺式布局，可通过工具栏多屏按钮进行切换，切换后点击**应用**。

书页式层叠布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/qqdwxFKER5-di7AZfubcnw/zh-cn_image_0000002808884799.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=5360A79DF7817542368F55DAFC4A4751704E8F6E5B3E0B54BA2EA506FCC59FAB)

平铺式布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/jtzsAkLeT1yr5rC5Sjzk3g/zh-cn_image_0000002779565240.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=9890751A613D5C443D132572C8E9353140CA1B12BC6EC5E6EFECAA917B9BD159)
