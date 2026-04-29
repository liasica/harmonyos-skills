---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-more-features
title: 更多的扩展能力
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 使用模拟器 > 更多的扩展能力
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a89c4f6e682bfa32033afc2295ebf7b8580550f647867e518f1cf05ddb1d504a
---

模拟器支持电池、GPS、虚拟传感器等扩展能力，具体使用方式参考以下介绍。点击模拟器菜单栏的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/PgVFiI6IQJCYpESEFRwFqg/zh-cn_image_0000002561831033.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=452370A7224632F89EE4AFA180D317CD27323E09B6D9DD6D86BC182D015F17C5)，打开扩展菜单栏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/Z2ArUQAdQiCKGBxgTGZnXQ/zh-cn_image_0000002561751059.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=485EF9F6F655BC9CD08DFC4DDFF2B081F0C5D52E35D92BE07EFB7AB9A1A11E0D "点击放大")

## 电池

您可以在模拟器上模拟不同电池状态。在扩展菜单栏上点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/kkspWeeWTd-yaEcaEpDT6A/zh-cn_image_0000002530911102.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=138525309ABA5D6E9A468F570F4A5CCA28F8A1C5A444EBC8F37B509CC15C10E4)打开电池模拟界面。在该界面，您可以手动输入或拖动滑块来改变电量百分比，也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/CIf-8BRUR3ajDIXZxqtV7g/zh-cn_image_0000002561751049.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=2A4A566E27AC83F4DEB2A440E3C936C17515EA4811BBBF0F67C1ED165F432841)切换电池的充电/放电状态。电池具有以下三种充电状态：

* ENABLE：开启充电按钮，此时正在充电且电量没充满。
* NONE：关闭充电按钮，此时停止充电。
* FULL：开启充电按钮，且电量为100%，电量已充满。

在应用中，您可以通过[@ohos.batteryInfo](../harmonyos-references/js-apis-battery-info.md)模块查询模拟器的剩余电量以及充电状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/iEGbTTlJTxOgBIkUr3nK9A/zh-cn_image_0000002561751079.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=75D8DE906B86A785E14F60BCDE60EAA02FE5D7824BA5BB2F99A85F9C1D3335BD "点击放大")

## GPS定位

模拟器可以模拟设备所处的位置。您可以打开扩展菜单，并点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/nqVU9R7lQnSCvFB3ghYPhg/zh-cn_image_0000002561831019.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=D870C8156CB9990B8AC8B5AE3204A95CEBF3E7B302D6510B481B196A20A7BA9B)进行位置信息的设置。模拟器提供以下方式的GPS位置模拟：

* 手动设置：在该界面，您可以手动输入此时所处位置的经度，纬度，海拔以及方位角。您也可以通过点击城市下拉框，快速定位到所选城市。
* 导入：在导入界面您可以注入一段时间内的连续位置信息。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/xoDTFF4hQCuRji5_rVrnuA/zh-cn_image_0000002530911124.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=8CF83C87213D0E78EC76344C9D227A8B6DF4D52A789DCB047B42472FD12E9593)导入本地的GPX文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/C2ocQORoSRKXFonXnyq94g/zh-cn_image_0000002561751031.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=69B55D06010E150F050088E30D96C070EA40D8E3549C8BD24366D9952ED1E4F0)即可开始模拟GPX文件中的轨迹。此外，您还可以选择不同回放速率来改变移动的速度。
* 场景模拟：如果没有本地的GPX文件，您可以在场景模拟界面使用我们预置的GPX文件。我们在模拟器内部预置了户外跑步、户外骑行、驾驶导航三种场景的GPX文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/e4Q4lGVFRmGC33xstF4vKA/zh-cn_image_0000002561751061.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=0AEA9ACD676D1AD7C15560F73E41DFA0D1762731C7FD6792BBF4B9EE6B48A62E)即可开始轨迹模拟。

  说明

  场景模拟功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

在应用中，您可以通过[@ohos.geoLocationManager](../harmonyos-references/js-apis-geolocationmanager.md)模块获取模拟器的位置信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/EHECejVTTnWkD5thZuVgbg/zh-cn_image_0000002530751110.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=1C421A09199C0C6895F3AC2054A373E7E0537125239714ECA640B870B198F1E4 "点击放大")

## 虚拟传感器

模拟器提供了虚拟传感器来模拟硬件传感器的能力。在扩展菜单上点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/WIVJh-2STGi1S-WXC6stJg/zh-cn_image_0000002530751098.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=997378A5F6CD35E58E2A9D9E432E274755DBB09E1D254A334B497B194EC56B64)打开虚拟传感器界面。在该界面，您可以调节不同的传感器来测试您的应用，使用[@ohos.sensor](../harmonyos-references/js-apis-sensor.md)模块监听传感器值的变化。模拟器提供以下虚拟传感器：

* 计步传感器：用于测量步数，对应的SensorId为PEDOMETER。
* 环境光传感器：用于测量光照强度，对应的SensorId为AMBIENT\_LIGHT。
* 心率传感器：用于测量心率，对应的SensorId为HEART\_RATE。从DevEco Studio 6.1.0 Beta1版本开始，Wearable设备支持心率传感器。

您可以拖动滑动条或者直接在文本框输入来改变不同传感器的值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/pomnItrnTSid0yKMEa8C_Q/zh-cn_image_0000002530751104.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=2F149C65AD9D01B2666533DA79C8F34837DEA865C82FA29F7DBBC5CD236BF9EE "点击放大")

## 网络

说明

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

模拟器的网络功能支持配置代理服务器和DNS地址，打开扩展菜单栏，并点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/aNjLIAoYTnyNXDc-hTuj5Q/zh-cn_image_0000002530911118.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=AE2F812750C1E243066408AD7F1F334C7C4EB55AE7484EE2F26DA05339280639)打开网络界面。

**代理设置**

模拟器可以将网络请求代理到代理服务器，利用代理服务器去请求目标服务器。从而满足以下开发场景：

* 开发者处于内网环境，希望通过设置代理的方式访问外网；
* 开发者已经在DevEco Studio上配置了网络代理，不希望在模拟器上重复配置代理；
* 开发者需要将网络请求代理到三方抓包工具，方便查看请求信息。

模拟器提供以下三种代理模式：

* **使用DevEco Studio代理：**读取并应用[DevEco Studio上的网络代理配置](ide-environment-config.md#section10369436568)。

  说明

  使用DevEco Studio代理时，模拟器不支持以下能力：

  + 不支持**自动检测代理（Auto-detect proxy settings）和SOCKS代理**，会自动切换到无代理模式；
  + 不支持**HTTP代理**下的**No proxy for**功能。
* **无代理：**不使用代理，即发送网络请求时会直接去请求目标服务器。
* **手工配置代理：**配置代理服务器的信息，将网络请求代理到代理服务器上。

配置代理后，可以点击**Check Connection**对当前的代理配置进行校验，并点击**Apply**按钮进行保存。在发起https请求时，需要安装网站的数字证书，请参考[使用模拟器发起https请求时如何安装数字证书](../harmonyos-faqs/faqs-app-running-27.md)。

**DNS设置**

从DevEco Studio 6.1.0 Beta2版本开始，新增DNS设置功能，开发者可以手动设置DNS服务器用于域名解析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/gYGc2OnTRviaP9Za_ZDy8A/zh-cn_image_0000002530911112.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=9902452F6B9F777605E0193D059A0D964308FFAFD25DD6B046E3C055ABDAD78C "点击放大")

## 摇一摇

模拟器可以模拟用户对设备的摇一摇操作。点击工具栏上的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/4GOIzWH6R3eq_SBpAaJyYA/zh-cn_image_0000002530751088.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=41638DFC253A0F691E934DE7374A94559544B8A1DE9B62729E56E583D398E325)，您可以模拟时长为1s的摇一摇操作。您的应用可以通过[@ohos.sensor](../harmonyos-references/js-apis-sensor.md)模块监听加速度传感器变化，当加速度传感器的变化量达到设定阈值时，触发摇一摇对应的业务逻辑。

说明

仅phone和tablet类型的设备支持摇一摇。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/8C288oRgTjaWm2vC2k8Hog/zh-cn_image_0000002530911126.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=03EDCD14A8D564EEBFAA3657405EF6958869B439BF023086EEF7677ADF0B1014 "点击放大")

## 音频输入

模拟器当前仅支持Audio Kit（音频服务）提供的音频输入能力，您可以使用本地计算机上的麦克风设备向模拟器中传输音频数据。使用步骤如下：

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

从DevEco Studio 5.1.0 Release版本开始，模拟器支持调用本地计算机摄像头。例如通过调用Camera Kit（相机服务）提供的接口，可以在模拟器上实现拍照和预览功能；通过Scan Kit（统一扫码服务），可以在API 20及以上版本的模拟器上实现扫码功能。其他依赖摄像头能力的Kit，请参考对应Kit简介中的模拟器支持情况。

模拟器调用摄像头开发步骤如下：

1. 请确保本地计算机上存在可用的摄像头，不支持通过USB连接的摄像头。
2. 应用调用对应Kit提供的API接口，通过电脑摄像头实现预览、拍照、扫码等功能。

   说明

   使用模拟器开发相机时，[相机配置信息](../harmonyos-references/arkts-apis-camera-i.md#profile)请使用：RGBA\_8888格式、1280 \* 720分辨率。

## 表冠

穿戴模拟器可以模拟表冠功能。

* 鼠标单击表冠：根据当前所在页面，单击后跳转到表盘或桌面。
* 鼠标双击表冠：进入多任务管理界面。
* 在屏幕上使用鼠标滚轮：模拟表冠旋转。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/c-4QkKb3SaqM1QAuE8plTw/zh-cn_image_0000002561751067.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=D5771F7FA168D488D164E4AB47E533F7070918DE207CFD0B2299C87105F28444 "点击放大")

## 设置

模拟器支持设置主题、语言和截屏保存路径。打开扩展菜单栏，并点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/uYsqvhOYT1G54MUxU-K33w/zh-cn_image_0000002530911116.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=27A6EEDD39F6FB5CA42473B4FAF39F3D788850EB8F715EDDEC60DB3E8CBDE422)打开设置面板。

* **主题****：**支持Light和Dark两种主题。
* **语言：**
  + **界面语言：**设置模拟器工具栏的语言。从DevEco Studio 6.1.0 Beta2版本开始，设置界面语言后，对所有模拟器都生效。
  + **OS语言：**从DevEco Studio 6.1.0 Beta2版本开始，支持设置模拟器镜像中的语言。此处的OS语言设置和模拟器的**设置 > 系统**中的语言设置效果相同。

  首次启动模拟器时，会根据当前计算机的系统语言，对模拟器的界面语言和OS语言进行初始化。如果计算机的系统语言不在模拟器的支持范围内，则模拟器语言默认使用英文。

  如需重置OS语言，可通过**Wipe User Data**进行清除重置。界面语言不支持重置，只能再次修改。
* **截屏保存路径：**设置模拟器工具栏的截屏功能对应的图片保存路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/DDFwhiu-QnKBOuHmtFgC9A/zh-cn_image_0000002561751035.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=A7E608C4B9CDECD1D1D1784FAE2FCEAD7AA0195F24E7BCCFACF191BED18D7531)

## 多屏

从DevEco Studio 6.0.0 Beta1版本开始，模拟器可以使用多屏能力，基于同一个镜像创建不同分辨率、DPI的多屏幕模拟器，满足开发者快速测试不同分辨率、DPI场景下的UI布局等需求。

### 使用约束

* 模拟器旋转功能和多屏功能互斥，不能同时使用。
* 仅phone类型的模拟器支持多屏能力。从DevEco Studio 6.0.1 Beta1版本开始，新增tablet类型的模拟器支持多屏能力。
* 多屏状态下扩展屏不支持使用画中画功能、不支持鼠标滚轮操作。

### 添加屏幕

1. 启动模拟器，点击工具栏的多屏按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/_qYhTrZVSDmdLnxjOwVtDQ/zh-cn_image_0000002530911122.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=3B69D1F01138A52C82DD7639126DCB9274713847905F873DEA600403DFFA1D6A)，打开多屏界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/oxLY0j1xSWW5ZCud7ZO5kg/zh-cn_image_0000002530911132.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=D798B73FD1D5E85B6A5ECA793DA34B6173A39FF5555C11A5BFD7054D5DCFC9D0 "点击放大")
2. 点击**添加**，可以选择Mate系列、Pura系列、Nova系列等产品型号，点击**应用**即可添加对应的屏幕。

   默认情况下，所有的屏幕是整体拖动和缩放的，如需单独拖动和缩放单个屏幕，请勾选界面上的**每个副屏在独立窗口中显示**，并点击**应用**按钮。从DevEco Studio 6.0.1 Beta1版本开始支持。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/MM7BqldwSe-hoL8PZtMvtw/zh-cn_image_0000002561751057.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=EA18F2F3CEB545EF18465204B0DE8FA445714FB337825143A13E7F154A7A4057 "点击放大")
3. 如需在多个屏幕上同时启动应用，请按界面提示，将module.json5中的launchType字段配置为multiton，具体请参考[UIAbility组件启动模式](uiability-launch-type.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/C0yvvRj2R1K_JVebE2Ukfw/zh-cn_image_0000002530911104.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=FE377E878FB15171B1A9DD51D12F093482E8B933B91D5EE52B6F369821082DD6 "点击放大")

### 修改屏幕参数

如需自定义屏幕分辨率、DPI或尺寸，可以在多屏界面上直接修改屏幕参数，取值范围参考界面提示，修改后点击**应用**。

* **Width**：宽度，单位为px。
* **Height**：高度，单位为px。
* **DPI**：像素密度，DPI 越高，UI组件占用的像素点越多，从而提供更精细的显示效果。
* **Size：**屏幕的对角线长度，单位为inch。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/b1PVzxlIQFSTVy1509KQ-w/zh-cn_image_0000002561751063.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=B44E5E699A4DE5404CF1FEC9233664C0AFA1796BCF73CE592372239B833777F7 "点击放大")

### 使用扩展屏

* 点击扩展屏，再点击模拟器工具栏返回按键![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/oT3yR81XSeuVf7LVGIpIEQ/zh-cn_image_0000002561751069.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=6471BF7A42022DF2D72DBA6178A3D4738B257FC62ECB04352E5AEBF86C83C4D0)，即可返回上一级目录。按键主屏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/DwrNhe-iQZyGY6SZDxcD-Q/zh-cn_image_0000002530911110.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=709B67446EF982C277B5268B7CFCF4A10F21F9B4D7AD96D575C9E5D09D4E37E7)和最近![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/FUSoapqgSHu23Gv4zjWjGA/zh-cn_image_0000002530911114.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=BEBABAD1D3634595FD1B2EF6A50C1EA236DB100E0255C096C9F4D44E9A9161F4)暂不支持在扩展屏上使用。
* 从扩展屏底部上滑，可直接清除应用。

### 删除屏幕

点击多屏界面上的删除按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/8oOPHI6pQra8PKXfYgjsXQ/zh-cn_image_0000002561751037.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=762A0D2D2D7FDB4A8E1ED14F98D82C248CC288D35FD9ADE1DE6CE3856DAF0E51)，再点击**应用**，即可删除一块屏幕。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/ThSJbzToT9ioiU807W9IgQ/zh-cn_image_0000002530751092.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=670EAC8CD36EB2FA7F31FEB3295973FE1D4A52A32201AACDF127BD0D451B9C25 "点击放大")
