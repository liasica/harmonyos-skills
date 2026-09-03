---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-more-features
title: 更多的扩展能力
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 使用模拟器 > 更多的扩展能力
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:653b80e5fb41e6d7b2fec8182c72289f36f19dca67d5a03bf9de4f1ed4ce449c
---

模拟器支持电池、GPS、虚拟传感器等扩展能力，具体使用方式参考以下介绍。点击模拟器菜单栏的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/IkOoJgvfSBOmqh1b-jeujg/zh-cn_image_0000002731381301.png)，打开扩展菜单栏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/6D9LzM6GQuGpLe7MI-u73Q/zh-cn_image_0000002701662064.png "点击放大")

## 电池

模拟器可以模拟不同电池状态。在扩展菜单栏上点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/XcjaNQ4SR0y27N_1DzCccg/zh-cn_image_0000002701822008.png)打开电池模拟界面。在该界面，可以手动输入或拖动滑块来改变电量百分比，也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/b3EAQAXZQRKm9CuG-D1Opg/zh-cn_image_0000002701822030.png)切换电池的充电/放电状态。电池具有以下三种充电状态：

* ENABLE：开启充电按钮，此时正在充电且电量未充满。
* NONE：关闭充电按钮，此时停止充电。
* FULL：开启充电按钮，且电量为100%，电量已充满。

在应用中，可以通过[@ohos.batteryInfo](../harmonyos-references/js-apis-battery-info.md)模块查询模拟器的剩余电量以及充电状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/QCZ4PVGATA2u1jpJUvP5_g/zh-cn_image_0000002701821936.gif "点击放大")

## GPS定位

模拟器可以模拟设备所处的位置。您可以打开扩展菜单，并点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/G6Wptu8pQaCrwJxVVaCO7w/zh-cn_image_0000002731541223.png)进行位置信息的设置。模拟器提供以下方式的GPS位置模拟：

* 手动设置：在该界面，可以手动输入此时所处位置的经度，纬度，海拔以及方位角，也可以通过点击城市下拉框，快速定位到所选城市。
* 导入：在导入界面可以注入一段时间内的连续位置信息。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/oczrWBxjQ4i12DgNkDYPWw/zh-cn_image_0000002701662058.png)导入本地的GPX文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/weyZu-pDTFSnuMJtDqf7Dw/zh-cn_image_0000002731381295.png)即可开始模拟GPX文件中的轨迹。此外，还可以选择不同回放速率来改变移动的速度。
* 场景模拟：如果没有本地的GPX文件，可以在场景模拟界面使用预置的GPX文件。模拟器预置了户外跑步、户外骑行、驾驶导航三种场景的GPX文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/CWJTgph0Q4OJHlGNDxUmpg/zh-cn_image_0000002731381245.png)即可开始轨迹模拟。

  **说明** 

  场景模拟功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

在应用中，您可以通过[@ohos.geoLocationManager](../harmonyos-references/js-apis-geolocationmanager.md)模块获取模拟器的位置信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/CAL6Q-uBT8aHYbXBHvhckw/zh-cn_image_0000002701822046.gif "点击放大")

## 虚拟传感器

模拟器提供了虚拟传感器来模拟硬件传感器的能力。在扩展菜单上点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/PL3e_onjQbyUrAwjlO29Aw/zh-cn_image_0000002731381241.png)打开虚拟传感器界面。在该界面，可以调节不同的传感器来测试应用，使用[@ohos.sensor](../harmonyos-references/js-apis-sensor.md)模块监听传感器值的变化。模拟器提供以下虚拟传感器：

* 计步传感器：用于测量步数，对应的SensorId为PEDOMETER。
* 环境光传感器：用于测量光照强度，对应的SensorId为AMBIENT\_LIGHT。
* 心率传感器：用于测量心率，对应的SensorId为HEART\_RATE。从DevEco Studio 6.1.0 Beta1版本开始，Wearable设备支持心率传感器。

可以拖动滑动条或者直接在文本框输入来改变不同传感器的值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/DNIWrmQDSU-ugfMOnn26ow/zh-cn_image_0000002701821986.png "点击放大")

## 网络

模拟器的网络功能支持配置代理服务器和DNS地址，打开扩展菜单栏，并点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/9yzGmVhWSRePfGIimWne5A/zh-cn_image_0000002701821966.png)打开网络界面。

**说明** 

代理和DNS设置不可同时使用。

**代理设置**

模拟器可以将网络请求代理到代理服务器，利用代理服务器去请求目标服务器。从而满足以下开发场景：

* 开发者处于内网环境，希望通过设置代理的方式访问外网；
* 开发者已经在DevEco Studio上配置了网络代理，不希望在模拟器上重复配置代理；
* 开发者需要将网络请求代理到三方抓包工具，方便查看请求信息。

模拟器提供以下三种代理模式：

* **使用DevEco Studio代理：**读取并应用[DevEco Studio上的网络代理配置](ide-environment-config.md#section10369436568)。

  **说明** 

  使用DevEco Studio代理时，模拟器不支持以下能力：

  + 不支持**自动检测代理（Auto-detect proxy settings）和SOCKS代理**，会自动切换到无代理模式；
  + 不支持**HTTP代理**下的**No proxy for**功能。
* **无代理：**不使用代理，即发送网络请求时会直接去请求目标服务器。
* **手工配置代理：**配置代理服务器的信息，将网络请求代理到代理服务器上。

配置代理后，可以点击**Check Connection**对当前的代理配置进行校验，并点击**Apply**按钮进行保存。在发起https请求时，需要安装网站的数字证书，请参考[使用模拟器发起https请求时如何安装数字证书](../harmonyos-faqs/faqs-app-running-27.md)。

**DNS设置**

从DevEco Studio 6.1.0 Beta2版本开始，新增DNS设置功能，开发者可以手动设置DNS服务器用于域名解析，设置后点击**Apply**提交。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/RXd5vv9YRXy8j3sVI1a7pA/zh-cn_image_0000002701662104.png "点击放大")

## 摇一摇

模拟器可以模拟用户对设备的摇一摇操作。点击工具栏上的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/PW-NHHj0QUC5p8xlvoJufw/zh-cn_image_0000002731381261.png)，可以模拟时长为1s的摇一摇操作。应用可以通过[@ohos.sensor](../harmonyos-references/js-apis-sensor.md)模块监听加速度传感器变化，当加速度传感器的变化量达到设定阈值时，触发摇一摇对应的业务逻辑。

**说明** 

仅phone和tablet类型的设备支持摇一摇。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/AXiBYl3dRae_TojFpYzsKQ/zh-cn_image_0000002731541267.gif "点击放大")

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

1. 在模拟器扩展菜单栏上点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/BOUjY7KiR6eKjTnHHrBU4Q/zh-cn_image_0000002701821972.png)打开虚拟相机页面，上传一张符合规格要求的图片作为预置图片，上传后图片会被裁剪至720p。上传图片的规格要求请参考界面提示。
2. 在应用中正常调用相机拍照接口，拉起摄像头时，相机预览界面会显示预置的图片。执行拍照操作，应用获取到的即为预置图片，并保存到应用指定的输出路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/DIuW3DNDS4mYLOJA6gs8tQ/zh-cn_image_0000002701662134.png)

## 表冠

穿戴模拟器可以模拟表冠功能。

* 鼠标单击表冠：根据当前所在页面，单击后跳转到表盘或桌面。
* 鼠标双击表冠：进入多任务管理界面。
* 在屏幕上使用鼠标滚轮：模拟表冠旋转。从26.0.0版本开始，在表冠区域使用鼠标滚轮，也可模拟表冠旋转功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/YR-biT6nQEuLs6ZoQ8Lmcg/zh-cn_image_0000002731541187.png "点击放大")

## 设置

模拟器支持设置主题、语言和截屏保存路径。打开扩展菜单栏，并点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/uy5QmOWYTuC-zGueF9_dgg/zh-cn_image_0000002701822010.png)打开设置面板。

* **主题****：**支持Light和Dark两种主题。
* **语言：**
  + **界面语言：**设置模拟器工具栏的语言。从DevEco Studio 6.1.0 Beta2版本开始，设置界面语言后，对所有模拟器都生效。
  + **OS语言：**从DevEco Studio 6.1.0 Beta2版本开始，支持设置模拟器镜像中的语言。此处的OS语言设置和模拟器的**设置 > 系统**中的语言设置效果相同。

  首次启动模拟器时，会根据当前计算机的系统语言，对模拟器的界面语言和OS语言进行初始化。如果计算机的系统语言不在模拟器的支持范围内，则模拟器语言默认使用英文。

  如需重置OS语言，可通过**Wipe User Data**进行清除重置。界面语言不支持重置，只能再次修改。
* **截屏保存路径：**设置模拟器工具栏的截屏功能对应的图片保存路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/UEFZK0xjSIKzrJaY7FsPow/zh-cn_image_0000002701822060.png)

## 多屏

从DevEco Studio 6.0.0 Beta1版本开始，模拟器支持使用多屏能力，基于同一个镜像创建不同分辨率、DPI的多屏幕模拟器，满足开发者快速测试不同分辨率、DPI场景下的UI布局等需求。

### 使用约束

* 模拟器旋转功能和多屏功能互斥，不能同时使用。
* 多屏状态下扩展屏不支持使用画中画功能、不支持鼠标滚轮操作。
* Phone类型的模拟器支持多屏能力。
* 从DevEco Studio 6.0.1 Beta1版本开始，新增Tablet类型的模拟器支持多屏能力。
* 从26.0.0版本开始，新增Car类型的模拟器支持多屏能力，具体请参考[Car设备多屏能力](ide-emulator-more-features.md#section5710121118389)。

### 添加屏幕

1. 启动模拟器，点击工具栏的多屏按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/shbmKki4S7qc_RCE0f2oLg/zh-cn_image_0000002701662096.png)，打开多屏界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/pBwxJDA5TNO3MFHY93eZ4g/zh-cn_image_0000002731381361.png "点击放大")
2. 点击**添加**，可以选择Mate系列、Pura系列、Nova系列等产品型号，点击**应用**即可添加对应的屏幕。

   默认情况下，所有的屏幕是整体拖动和缩放的，如需单独拖动和缩放单个屏幕，请勾选界面上的**每个副屏在独立窗口中显示**，并点击**应用**按钮。从DevEco Studio 6.0.1 Beta1版本开始支持。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/oSeP2-x_QoeyX44s1lVXyA/zh-cn_image_0000002701662014.png "点击放大")
3. 如需在多个屏幕上同时启动应用，请按界面提示，将module.json5中的launchType字段配置为multiton，具体请参考[UIAbility组件启动模式](uiability-launch-type.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/SeuvV5yuSwC1UnnhbGnAng/zh-cn_image_0000002701821978.png "点击放大")

### 修改屏幕参数

如需自定义屏幕分辨率、DPI或尺寸，可以在多屏界面上直接修改屏幕参数，取值范围参考界面提示，修改后点击**应用**。

* **Width**：宽度，单位为px。
* **Height**：高度，单位为px。
* **DPI**：像素密度，DPI 越高，UI组件占用的像素点越多，从而提供更精细的显示效果。
* **Size：**屏幕的对角线长度，单位为inch。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/CeahxxxyTI-ZmO3bAiqyGQ/zh-cn_image_0000002701662092.png "点击放大")

### 使用扩展屏

* 点击扩展屏，再点击模拟器工具栏返回按键![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/ft_hQW7EQZGmaxri2Q9dvA/zh-cn_image_0000002731541335.png)，即可返回上一级目录。按键主屏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/wIFRde0qSEizGTPK9V6wuQ/zh-cn_image_0000002731541213.png)和最近![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/MbXp2SEtQ8y6DNWAMtJc-Q/zh-cn_image_0000002701821920.png)暂不支持在扩展屏上使用。
* 从扩展屏底部上滑，可直接清除应用。

### 删除屏幕

点击多屏界面上的删除按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/YxCJSd64R-GqEbVqkVGiPQ/zh-cn_image_0000002701662118.png)，再点击**应用**，即可删除一块屏幕。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/87-mSmebRFqXYn74ddjLsg/zh-cn_image_0000002731381251.png "点击放大")

### Car设备多屏能力

从26.0.0版本开始，Car模拟器支持多屏能力，通过添加副屏，可模拟驾驶舱主屏幕和副驾驶屏幕的场景。

在创建Car模拟器时，支持新增或删除屏幕，具体操作方式请参考[创建模拟器](ide-emulator-create.md)。新增屏幕后，启动模拟器会自动展示副屏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/5_Ei_QjdSJuqDWq2g0Pl7w/zh-cn_image_0000002731381345.png)

Car模拟器的每个屏幕对应一个独立用户，主屏与副屏的操作相互独立。例如安装、调试、卸载应用，主屏和副屏都需要独立操作。

* 安装应用：可以通过拖拽安装的方式同时安装主屏和副屏，或使用[hdc命令](hdc.md#安装应用文件)分别安装，通过-u参数指定用户，主屏是100，副屏是101。
* 调试应用：调试时默认对主屏进行调试，如需调试副屏，需要单独进行[attach调试](ide-debug-arkts-attach.md)。

新增屏幕后，如果使用时不需要展示副屏，可点击模拟器工具栏多屏按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/AAXJL_G3R8qFRK5i3ya69Q/zh-cn_image_0000002701662072.png)，将对应屏幕去勾选并点击**应用**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/kxbyyqrXQZ639fwvbp_HwA/zh-cn_image_0000002731541227.png)

Car模拟器支持两种布局方式，书页式层叠布局和平铺式布局，可通过工具栏多屏按钮进行切换，切换后点击**应用**。

书页式层叠布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/ovnf1bLTSUyywWWnpyUtWw/zh-cn_image_0000002731541217.png)

平铺式布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/zcaeB0KcTOefk3i6TgXl7Q/zh-cn_image_0000002701662108.png)
