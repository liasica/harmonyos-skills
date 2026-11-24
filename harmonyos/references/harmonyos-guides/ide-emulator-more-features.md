---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-more-features
title: 更多的扩展能力
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 使用模拟器运行应用 > 使用模拟器 > 更多的扩展能力
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:29+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:e596c7e3d2007226f6a9305291001d93718c0f3c4f0e04ea92fdf5c84cbc1e2e
---

模拟器支持电池、GPS、虚拟传感器等扩展能力，具体使用方式参考以下介绍。点击模拟器菜单栏的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/VFXzFK5zRQWe-7Fksj3AVA/zh-cn_image_0000002808884821.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=2981771AC224997917ADFC09B5B295243B0830BD75D5C9DEB1BC3987EF789F26)，打开扩展菜单栏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/kStWIyoRSMqFQ70sRJV2hw/zh-cn_image_0000002808764795.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4D422FC0D3DBD10D3B182704563BAFE1D69BD4B096FEF4F5990FE8C4E90609D "点击放大")

## 电池

模拟器可以模拟不同电池状态。在扩展菜单栏上点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/Q1U8uNQdTEmWhbr-dCjEEA/zh-cn_image_0000002779565158.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=D87E4487A951BC6D7250680FDB13E7C3A5C46298B696BE72080AF2D6B6B545B6)打开电池模拟界面。在该界面，可以手动输入或拖动滑块来改变电量百分比，也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/1dpgjXkFT0CVvvG_3hY3QQ/zh-cn_image_0000002779405260.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3B2889E93D1C6A47D3F822177269F7B211368ADC203C948D316CDA824A1FE00)切换电池的充电/放电状态。电池具有以下三种充电状态：

* ENABLE：开启充电按钮，此时正在充电且电量未充满。
* NONE：关闭充电按钮，此时停止充电。
* FULL：开启充电按钮，且电量为100%，电量已充满。

在应用中，可以通过[@ohos.batteryInfo](../harmonyos-references/js-apis-battery-info.md)模块查询模拟器的剩余电量以及充电状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/6PG9--kfSc2MWL2jPNoqNg/zh-cn_image_0000002808764771.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=B87FBF3D7060B11AE1101F121B8ADDAB6E09B6977C1BD65DDE2076CC552F7132 "点击放大")

## GPS定位

模拟器可以模拟设备所处的位置。您可以打开扩展菜单，并点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/0S32xWQgSuG80NSgF4V2IA/zh-cn_image_0000002779405226.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5EC5308CD293FF1B23DE06460463DFD35053DC6AFB4F008950B62C3B874B1DD)进行位置信息的设置。模拟器提供以下方式的GPS位置模拟：

* 手动设置：在该界面，可以手动输入所处位置的经度、纬度、海拔以及方位角，也可以通过点击城市下拉框，快速定位到所选城市。
* 导入：在导入界面可以注入一段时间内的连续位置信息。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/Qq3P9bHHS_qBNrQhz4ujtQ/zh-cn_image_0000002779405234.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=0F28F4E278D7C30B8B1D7A8BA05F438A0BD5767822DD8FA32A4F465CFC66A949)导入本地的GPX文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/_F1YHkBKS4qGZ7cwDT_Rdg/zh-cn_image_0000002779565222.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=80478E0EA32F4C34925E1C73E1200B7E0046435F7362143BA8A0E9A8D6B6BDD3)即可开始模拟GPX文件中的轨迹。此外，还可以选择不同回放速率来改变移动的速度。
* 场景模拟：如果没有本地的GPX文件，可以在场景模拟界面使用预置的GPX文件。模拟器预置了户外跑步、户外骑行、驾驶导航三种场景的GPX文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/6koxUOXwS5apzewncQRUFA/zh-cn_image_0000002808884861.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=8DEF7936AA84A3C77998010BD488E88871931C8C117B1A0FA708CEFC8940564A)即可开始轨迹模拟。

  **说明** 

  场景模拟功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

在应用中，您可以通过[@ohos.geoLocationManager](../harmonyos-references/js-apis-geolocationmanager.md)模块获取模拟器的位置信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/PbykxSyER-KI3nai26Y0EA/zh-cn_image_0000002808884837.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=88B00867B69FA3A510EB92A64355031CA3A46EE392D649C01C67687EE23AC73E "点击放大")

## 虚拟传感器

模拟器提供了虚拟传感器来模拟硬件传感器的能力。在扩展菜单上点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/MliIqPtuROST2D7pgKn-TQ/zh-cn_image_0000002779565132.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=62E412F02F1F7EA7A9B6122574BCFFFA843342B7394ECE1B812BD9C23753B086)打开虚拟传感器界面。在该界面，可以调节不同的传感器来测试应用，使用[@ohos.sensor](../harmonyos-references/js-apis-sensor.md)模块监听传感器值的变化。模拟器提供以下虚拟传感器：

* 计步传感器：用于测量步数，对应的SensorId为PEDOMETER。
* 环境光传感器：用于测量光照强度，对应的SensorId为AMBIENT\_LIGHT。
* 心率传感器：用于测量心率，对应的SensorId为HEART\_RATE。从DevEco Studio 6.1.0 Beta1版本开始，Wearable设备支持心率传感器。

可以拖动滑动条或者直接在文本框输入来改变不同传感器的值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/88MJpZW_Q36sU7rSpVTT-Q/zh-cn_image_0000002779405240.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=F88D2FC6DB770E708718FAA53BDBE60AB5AC925706DDD5D2CA668A85D83871C3 "点击放大")

## 网络

模拟器的网络功能支持配置代理服务器和DNS地址，打开扩展菜单栏，并点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/a-UjQ0iMSJiIG3xPd3LBag/zh-cn_image_0000002808884807.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E4507F36830FC95F4CD82EBB4C665870BE61DC08B2639AE14A833195B57BB81)打开网络界面。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/GH2c4GGNRJisKT5s90Qmhg/zh-cn_image_0000002808884901.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=ADC7EA0477BEA8776FB3451140EA848A853EE426F074C0DBDFC41E7D2B594AAA "点击放大")

## 摇一摇

模拟器可以模拟用户对设备的摇一摇操作。点击工具栏上的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/4MI5lPw7S9muAe7aUQySUA/zh-cn_image_0000002779565142.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=03A15148F6EB69174969D1A031B0B10A448FC2BE71D204A4B076D2FCDE878751)，可以模拟时长为1s的摇一摇操作。应用可以通过[@ohos.sensor](../harmonyos-references/js-apis-sensor.md)模块监听加速度传感器变化，当加速度传感器的变化量达到设定阈值时，触发摇一摇对应的业务逻辑。

**说明** 

仅phone和tablet类型的设备支持摇一摇。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/TAfg_0kmR225Ai90Juzdow/zh-cn_image_0000002808764733.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=A2FF6BAF4AD9D62860F22D4BB60BF7EA5D7D66C336FE5A835B97DDFB6B8B27DB "点击放大")

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

1. 在模拟器扩展菜单栏上点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/5Qvq6tQYSr6L5fLY9ICrWA/zh-cn_image_0000002808764723.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=56FFA60F66F615C8AB0DA65F0E1D86271AFF788D483AD2CBF0E9496454421A40)打开虚拟相机页面，上传一张符合规格要求的图片作为预置图片，上传后图片会被裁剪至720p。上传图片的规格要求请参考界面提示。
2. 在应用中正常调用相机拍照接口，拉起摄像头时，相机预览界面会显示预置的图片。执行拍照操作，应用获取到的即为预置图片，并保存到应用指定的输出路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/9bT39g6LSX6a_dD35paLJA/zh-cn_image_0000002808764755.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C807F878A49BA3A1C984FB57442B122F7C12C27A70561D49D51A4C6B3372DA6)

## 表冠

穿戴模拟器可以模拟表冠功能。

* 鼠标单击表冠：根据当前所在页面，单击后跳转到表盘或桌面。
* 鼠标双击表冠：进入多任务管理界面。
* 在屏幕上使用鼠标滚轮：模拟表冠旋转。从26.0.0版本开始，在表冠区域使用鼠标滚轮，也可模拟表冠旋转功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/kmuvqMhWT2u8YvtwHPiQoA/zh-cn_image_0000002808764707.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD94928FB93B862A79436A586C775C3D77952C75B746F125467425C32C3842E2 "点击放大")

## 设置

模拟器支持设置主题、语言和截屏保存路径。打开扩展菜单栏，并点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/H_GmW_mRTNuYtN8yrkueow/zh-cn_image_0000002779405250.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=4422B4EF223335B96E8BD9554C1FA3623398BA8C63B678E8375D66BAC5B38FC5)打开设置面板。

* **主题****：**支持Light和Dark两种主题。
* **语言：**
  + **界面语言：**设置模拟器工具栏的语言。从DevEco Studio 6.1.0 Beta2版本开始，设置界面语言后，对所有模拟器都生效。
  + **OS语言：**从DevEco Studio 6.1.0 Beta2版本开始，支持设置模拟器镜像中的语言。此处的OS语言设置和模拟器的**设置 > 系统**中的语言设置效果相同。

  首次启动模拟器时，会根据当前计算机的系统语言，对模拟器的界面语言和OS语言进行初始化。如果计算机的系统语言不在模拟器的支持范围内，则模拟器语言默认使用英文。

  如需重置OS语言，可通过**Wipe User Data**进行清除重置。界面语言不支持重置，只能再次修改。
* **截屏保存路径：**设置模拟器工具栏的截屏功能对应的图片保存路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/M09bYf9bRUePDK4WYIfskA/zh-cn_image_0000002779405264.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=84A1EB03280D0F612D06C3BA7D3FE63CE8B186C76C77FA747344068458BAFFCF)

## 多屏

从DevEco Studio 6.0.0 Beta1版本开始，模拟器支持使用多屏能力，基于同一个镜像创建不同分辨率、DPI的多屏幕模拟器，满足开发者快速测试不同分辨率、DPI场景下的UI布局等需求。

### 使用约束

* 模拟器旋转功能和多屏功能互斥，不能同时使用。
* 多屏状态下扩展屏不支持使用画中画功能、不支持鼠标滚轮操作。
* Phone类型的模拟器支持多屏能力。
* 从DevEco Studio 6.0.1 Beta1版本开始，新增Tablet类型的模拟器支持多屏能力。
* 从26.0.0版本开始，新增Car类型的模拟器支持多屏能力，具体请参考[Car设备多屏能力](ide-emulator-more-features.md#section5710121118389)。

### 添加屏幕

1. 启动模拟器，点击工具栏的多屏按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/38jSRlxyS3GaVOR8hEX8bw/zh-cn_image_0000002779565230.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=B1B2E1E1FF02D0D41ACC34CD846A0FED01CD381B25CB52FD8AD73799FC88DD29)，打开多屏界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/ARFpUr0BToSfXezi6lgh8w/zh-cn_image_0000002779565184.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=5BA5DB8F8B204F909FFA02B943D552FE6B3FB5DE27C74F6C8FF23778DC9A71D5 "点击放大")
2. 点击**添加**，可以选择Mate系列、Pura系列、Nova系列等产品型号，点击**应用**即可添加对应的屏幕。

   默认情况下，所有的屏幕是整体拖动和缩放的，如需单独拖动和缩放单个屏幕，请勾选界面上的**每个副屏在独立窗口中显示**，并点击**应用**按钮。从DevEco Studio 6.0.1 Beta1版本开始支持。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/SK937zK5Qza8uJqbklff-Q/zh-cn_image_0000002779565190.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=FB1D6654B8A9FECCEB9DC2A3F3BBFB9085CBD73429696D505247383E3E58BD1F "点击放大")
3. 如需在多个屏幕上同时启动应用，请按界面提示，将module.json5中的launchType字段配置为multiton，具体请参考[UIAbility组件启动模式](uiability-launch-type.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/YDZ1PA_HQkWNtnaWikw9fQ/zh-cn_image_0000002808884879.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=B12EAA2EC4C5FF84AE7145440F32E1F23BB3CF65A40A650F5413E87C68DA1D9C "点击放大")

### 修改屏幕参数

如需自定义屏幕分辨率、DPI或尺寸，可以在多屏界面上直接修改屏幕参数，取值范围参考界面提示，修改后点击**应用**。

* **Width**：宽度，单位为px。
* **Height**：高度，单位为px。
* **DPI**：像素密度，DPI 越高，UI组件占用的像素点越多，从而提供更精细的显示效果。
* **Size：**屏幕的对角线长度，单位为inch。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/FzxKfakQTZeb7vjl8ssqvQ/zh-cn_image_0000002808764741.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF395673E53001ABC858F79CCBDD62FBDAA9BB874D4125CC9A1007A32BF3E66F "点击放大")

### 使用扩展屏

* 点击扩展屏，再点击模拟器工具栏返回按键![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/0uq5IMMcTeSJoXiMrqKtHA/zh-cn_image_0000002808764763.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A5C5BEDB3F148FC9B9942F5BAAF467EECE1EE2E8914BFC657DB91098BEA1172)，即可返回上一级目录。按键主屏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/XnUduDnhQKidm4hduCb62Q/zh-cn_image_0000002808764713.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=A832C3FD9684BC8E0AA2E41941F532EA32F59B62CFF9B5C488B72D68D9A9E521)和最近![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/hEu9xeDHQvSvHgMUpDlWfQ/zh-cn_image_0000002779405210.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=476FD0BC8CDDCEDFC5177BE8C70ADE4C405FF2C8FB324CF5B754CEE4523F97D3)暂不支持在扩展屏上使用。
* 从扩展屏底部上滑，可直接清除应用。

### 删除屏幕

点击多屏界面上的删除按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/SZgRrD3BS8-BtHmw1vq1_A/zh-cn_image_0000002808884903.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=A8613C5AF07E4424C00C12A2921D5CB221C2DF9CA5B048E5CC738AA993706708)，再点击**应用**，即可删除一块屏幕。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/s4Ka4yPcRSu-j4l1DeJ33Q/zh-cn_image_0000002779565138.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F2BB3E787C5E543FEBABC46F8D168F6EA22CAF1385B8762F894BE7EFC2F051F "点击放大")

### 使用HiCar能力

从26.0.1版本开始，Phone模拟器支持HiCar投屏能力，通过多屏界面，可模拟手机接入车机后的开发场景，支撑应用适配HiCar模式。

**使用约束**

* 仅直板机品类可使用HiCar能力，且不可与添加副屏功能共用。
* 仅支持一块HiCar屏幕，随主屏整体拖动和缩放。
* HiCar状态下不可使用旋转功能，扩展屏不支持画中画功能、不支持鼠标滚轮操作。

**添加HiCar屏幕**

1. 启动模拟器，点击工具栏的多屏按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/RbB-wcZ1QsacoQ7vSa7pAQ/zh-cn_image_0000002808884907.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A61FC8433E385D1F40246A36D50DD8CD200B708FBCC75D7BC2D13E37F049755)，打开多屏界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/G_G80MbuTPiJYqL0fn8cEw/zh-cn_image_0000002779405162.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=0497B1333D44F6188B169BAA4B58E1A54C5626B2A98ACF56B95DAE472D9EF5A7 "点击放大")
2. 选择HiCar模式，点击**添加**，可选择添加默认HiCar屏幕或自定义屏幕参数，可以在多屏界面上直接修改屏幕参数，取值范围参考界面提示，修改后点击**应用**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/en4669hfRjOh7DYx8hXleQ/zh-cn_image_0000002779565198.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=65129F3AEC93E2BC801F5A82ABD5EB305EE786677AAB577FCEFDA027B6EF5B09)
3. HiCar屏创建成功后，即可进行应用调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/CA-EMQhKRK6eNJ2DD065Kw/zh-cn_image_0000002779405170.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=48DBD736396F38873FE3FA00DCDD9D1A26CE530FF50CC73EF745552FABD9BB8E "点击放大")

### Car设备多屏能力

从26.0.0版本开始，Car模拟器支持多屏能力，通过添加副屏，可模拟驾驶舱主屏幕和副驾驶屏幕的场景。

在创建Car模拟器时，支持新增或删除屏幕，具体操作方式请参考[创建模拟器](ide-emulator-create.md)。新增屏幕后，启动模拟器会自动展示副屏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/gyeHSAqeT6K_I6xh8mnBFQ/zh-cn_image_0000002779405192.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=CBC9CAF6CD0C54F54C3E12C3BE16E47100C5C0B484D9519DCA7E4FE3825EC285)

Car模拟器的每个屏幕对应一个独立用户，主屏与副屏的操作相互独立。例如安装、调试、卸载应用，主屏和副屏都需要独立操作。

* 安装应用：可以通过拖拽安装的方式同时安装主屏和副屏，或使用[hdc命令](hdc.md#安装应用文件)分别安装，通过-u参数指定用户，主屏是100，副屏是101。
* 调试应用：调试时默认对主屏进行调试，如需调试副屏，需要单独进行[attach调试](ide-debug-arkts-attach.md)。

新增屏幕后，如果使用时不需要展示副屏，可点击模拟器工具栏多屏按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/8LgHzjVvRxqUT-50W-cRbg/zh-cn_image_0000002779565152.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=4584EF67E8E9D0AB8BE01FC3DB12244C30E3D3403DCF4A639FE6BE09A6BBF3AD)，将对应屏幕去勾选并点击**应用**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/Z7TsmtyNScWkfFUQsAbPQA/zh-cn_image_0000002808884869.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=174245105C9011BC88FA3183B9056DF9AB342AE4401F082D142BE7E71130F3CF)

Car模拟器支持两种布局方式，书页式层叠布局和平铺式布局，可通过工具栏多屏按钮进行切换，切换后点击**应用**。

书页式层叠布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/IZ_qwukdRWOdg-Mq2K3BPQ/zh-cn_image_0000002808884799.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=F018069A920C3C910666C4E6197ABF720E7D23B70ABA5046767D4C96973AF252)

平铺式布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Lu3TMyNPQbqa2VaGE9-3MQ/zh-cn_image_0000002779565240.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED5CC7E9B8243CA453792D85E9169BC1B3D1CC58B0F850B0831E7EC37EFB2EE0)
