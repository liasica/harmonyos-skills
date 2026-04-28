---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/network-navigator
title: 使用网络领航员进行网络模拟
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:10326fbbdafc361d81a69ad4d1319b99676d0b2344070c889c56a4387237605b
---

## 网络领航员功能简介

说明

网络领航员功能从API version 20开始支持，目前只支持手机和平板。

App上线之前需要优化和验证App在各种网络场景的体验，例如，App针对乘坐地铁时刷短视频进行优化后，卡顿情况是否有所改善，但需要在真实场景下验证。

网络领航员提供了网络模拟的能力，帮助开发者快速验证App在各种典型场景中的使用体验，提升App体验的测试验证效率，降低测试验证成本。例如，不需要真的乘坐高铁去验证高铁场景优化效果。

同时，网络领航员还提供这些网络场景下的数据传输优化建议，App接入华为[Network Boost Kit](network-boost-kit-guide.md)，实现应用和OS跨层协同，提升应用的上网流畅度。

例如，在进出电梯发生WLAN到移动数据切换时，App快速感知网络接口变化，及时将高优先级数据请求调度到新链路，实现WLAN和数据网络切换时不卡顿；在网络变弱时，Network boost kit上报QoS（Quality of Service）状态，帮助App做好传输调度。

## 预置网络模拟使用简介

网络领航员提供了两种使用入口，分别是设置界面和HDC命令行。

下面介绍通过设置界面使用网络领航员的方法，通过HDC命令行的使用方法见[netcopilot工具](network-netcopilot.md)。

当您首次使用该功能时，可根据 **[开启开发者选项](ide-developer-mode.md#section530763213432)** 指引先开启设备的开发者模式，然后点击**设置** -> **系统** -> **开发者选项** -> **网络领航员**即可进入网络领航员页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/Tqi3mVhPSRO9BEHRHeapfQ/zh-cn_image_0000002552798792.png?HW-CC-KV=V1&HW-CC-Date=20260427T234412Z&HW-CC-Expire=86400&HW-CC-Sign=ADA92D98FDCC19B75F868764FC8446243DB685A84BFA1D5AB5AA3B5C4AEC46EB)

网络领航员已预置如下常用网络模拟场景，您可以直接使用预置的网络模拟场景快速进行App使用体验测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/G1HCP3XyR4i6YYpfxHJYfg/zh-cn_image_0000002583438487.png?HW-CC-KV=V1&HW-CC-Date=20260427T234412Z&HW-CC-Expire=86400&HW-CC-Sign=011AEA1C8A42261E3B1BB69DE4D0AC5E9E52872E7FE8ED52C45CB285A5DF1ADE)

**如何启用一个网络模拟场景**

在**可用的网络模拟场景**中点击任意一个您需要模拟的场景即可启用网络模拟。例如，点击**进出电梯**后，即可启用该模拟场景，并可查看**已生效的网络模拟场景。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/Cy-zsvMiSSyYHeB0TWWSxg/zh-cn_image_0000002552958442.png?HW-CC-KV=V1&HW-CC-Date=20260427T234412Z&HW-CC-Expire=86400&HW-CC-Sign=051415DC6261913BE4929795D140F35EB5CB215D0A89F64FB60E8A262758DAF4)

同时您可在设备实况窗中查看到网络模拟内容（以进出电梯为例）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/Qz_i1BWCTZ2qvLhMzUL2Mg/zh-cn_image_0000002583478443.png?HW-CC-KV=V1&HW-CC-Date=20260427T234412Z&HW-CC-Expire=86400&HW-CC-Sign=118DCC61180C6460CE82D44DE5D2954D7286554235636045EC59CD1EDEAE79F0)

**如何停止一个网络模拟场景**

如果您需要停止网络模拟场景，可点击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/1m0Ug4sAT_q16_BLBPeSlA/zh-cn_image_0000002552798794.png?HW-CC-KV=V1&HW-CC-Date=20260427T234412Z&HW-CC-Expire=86400&HW-CC-Sign=39928626EC0CD6E421658A7A4729C88C2B3874A57F8FD60ED01D9274B544A73F)，然后点击退出该网络模拟场景即可退出模拟。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/HwFm3HFvSGC--ifGUz4fLQ/zh-cn_image_0000002583438489.png?HW-CC-KV=V1&HW-CC-Date=20260427T234412Z&HW-CC-Expire=86400&HW-CC-Sign=E0AD2B0EE626B1C3DBA5DAF271C579BD69A87822D837869206E155F68879DC7A)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/z_Ho2IQPRZirjkgyfsPKPA/zh-cn_image_0000002552958444.png?HW-CC-KV=V1&HW-CC-Date=20260427T234412Z&HW-CC-Expire=86400&HW-CC-Sign=31078EFBB666E416E4BB4918E9F0D10643A145A93CCF20AEF05A046E3AACB73B)

预置的网络模拟场景使用前置条件及模拟场景阶段说明如下：

| 网络模拟场景 | 使用前置条件 | 场景介绍及场景阶段说明 |
| --- | --- | --- |
| 进出电梯 | 连接 WLAN 并开启移动网络开关 | 模拟用户进出电梯，WLAN和移动网络间来回切换。此场景共6个阶段，总时长5分钟，循环执行。 |
| 离家断开WLAN | 连接 WLAN 并开启移动网络开关 | 模拟用户从家里到户外，WLAN断开，切换到移动网络。此场景共4个阶段，总时长3分钟，循环执行。 |
| 到家连接WLAN | 连接 WLAN 并开启移动网络开关 | 模拟用户从户外回到室内，连接WLAN，断开移动网络。此场景共3个阶段，总时长3分钟，循环执行。 |
| 拥挤的食堂 | 连接 WLAN 或移动网络 | 模拟网络接入设备多，空口竞争大，带宽小，时延大。此场景共3个阶段，总时长5分钟，循环执行。 |
| 停车场 | 连接 WLAN 或移动网络 | 模拟网络覆盖不佳，信号弱，带宽小，时延大。此场景共3个阶段，总时长5分钟，循环执行。 |
| 乘坐地铁 | 连接 WLAN 或移动网络 | 模拟网络波动大，站台上的网络强，站台间的网络弱。此场景共5个阶段，总时长5分钟，循环执行。 |
| 乘坐高铁 | 插入双SIM卡并开启移动网络开关 | 模拟网络波动大，频繁切换基站，间歇出现不可用。此场景共5个阶段，总时长10分钟，循环执行。 |
| 高速公路自驾 | 连接 WLAN 或移动网络 | 模拟网络波动大，城区网络强，隧道区域网络弱。此场景共5个阶段，总时长5分钟，循环执行。 |

预置的网络模拟场景包含的具体阶段及网络情况详见[附录](network-navigator.md#附录)。

## 自定义网络模拟场景配置

当上述预置网络模拟场景无法满足您的开发需要时，您也可以在网络领航员页面通过点击底部的 **添加自定义网络场景** 来新增所需网络配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/IZ_CuYxHTkWHeYd2IRCc1w/zh-cn_image_0000002583478445.png?HW-CC-KV=V1&HW-CC-Date=20260427T234412Z&HW-CC-Expire=86400&HW-CC-Sign=5ABD03EB68ABA33362819C141FD8842C9CF04723A17B5CEEC780DB3277B2F222)

参数的取值范围参考如下，输入参数取值后会自动添加单位。自定义场景的参数配置将应用于启动时的默认网络，建议在网络环境稳定时使用。

| 参数选项 | 参数取值范围 | 单位 |
| --- | --- | --- |
| 上行带宽 | 100 - 500000 | Kbps |
| 下行带宽 | 100 - 2000000 | Kbps |
| 上行丢包率 | 0.0 - 20.0 | % |
| 下行丢包率 | 0.0 - 20.0 | % |
| 上行延迟 | 1 - 1000 | ms |
| 下行延迟 | 1 - 1000 | ms |

自定义场景暂未接入Network Boost Kit，若开发者想模拟网络场景的注册回调，可使用[预置的网络模拟场景](network-navigator.md#预置网络模拟使用简介)。

## 网络优化建议

当您使用网络领航员能力时，可以通过实况窗实时了解网络变化，同时您也可以点击实况窗查看该场景的详细介绍，点击蓝色字体可**查看详细的网络参数**和**网络开发代码开发最佳实践**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/F4Eu0qbYR969MRRs0r8R9Q/zh-cn_image_0000002552798796.png?HW-CC-KV=V1&HW-CC-Date=20260427T234412Z&HW-CC-Expire=86400&HW-CC-Sign=83C6AD1601EEE38404B2EC93B62F97A2019B318C312F2C5B7FB33DFFFBCB83D6)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/0VIJvbMOQbqnCRxWltC25g/zh-cn_image_0000002583438491.png?HW-CC-KV=V1&HW-CC-Date=20260427T234412Z&HW-CC-Expire=86400&HW-CC-Sign=55BE896C905924197E45C6B9D641141BEB432B17448A248DA9A54B0E53C86EAC)

## 网络领航员代码优化建议

"网络领航员"功能在激活指定场景时，可智能模拟该场景下的网络QoS（服务质量）变化，帮助开发者快速构建目标网络环境。通过此功能，开发者能够前瞻性发现应用在不同网络环境中的兼容性问题，并基于本节的最佳实践指南进行针对性优化。

**代码优化建议**

当前支持8大类典型场景模拟（详见"[附录](network-navigator.md#附录)"章节），其网络特征可归纳为三类：网络切换、网络波动、网络质量差。如下为对应场景特征及代码开发建议。

**网络切换场景**

* 特征：设备在网络制式间切换（如WLAN与蜂窝网络互切）或多SIM卡切换时，会导致IP地址变更、TCP连接强制中断（触发RST复位），并伴随DNS重解析和新连接握手延迟。
* 典型场景：进出电梯、离家断开WLAN、高铁行驶（多SIM卡切换）
* 最佳实践：应用需及时识别网络切换并重建连接，解析DNS，重新发起未完成的请求，也可直接使用Network Kit的HTTP数据请求模块发起网络请求。Network Kit集成了通途协议栈的智能多网切换功能，能够在网络切换时自动将待发和进行中的请求切换至已激活的网络，有效避免网络切换环境下请求失败或业务响应延迟的问题。Network Kit HTTP请求示例代码如下：

  ```
  1. // 引入包名
  2. import { http } from '@kit.NetworkKit';
  3. import { BusinessError } from '@kit.BasicServicesKit';
  4. // 每一个httpRequest对应一个HTTP请求任务，不可复用
  5. let httpRequest = http.createHttp();
  6. httpRequest.request(
  7. // 填写HTTP请求的URL地址，可以带参数也可以不带参数。URL地址需要开发者自定义。请求的参数可以在extraData中指定
  8. "EXAMPLE_URL", (err: BusinessError, data: http.HttpResponse) => {
  9. if (!err) {
  10. // data.result为HTTP响应内容，可根据业务需要进行解析
  11. console.info('Result:' + JSON.stringify(data.result));
  12. // 当该请求使用完毕时，调用destroy方法主动销毁
  13. httpRequest.destroy();
  14. } else {
  15. console.error('error:' + JSON.stringify(err));
  16. // 当该请求使用完毕时，调用destroy方法主动销毁
  17. httpRequest.destroy();
  18. }
  19. }
  20. );
  ```

  **网络波动场景**

  + 特征：因信号强度快速变化（如移动穿行或高速运动），网络表现为带宽骤降（50Mbps→1Mbps）、时延剧烈抖动（RTT波动超300%）、短时丢包（0%~5%）。
  + 典型场景：乘坐地铁、高速公路自驾。
  + 最佳实践：
  1. 订阅Network Boost Kit的netQuality事件，实时感知网络质量，并进行针对性处理。

     ```
     1. // 引入包名
     2. import { netQuality } from '@kit.NetworkBoostKit';
     3. import { BusinessError } from '@kit.BasicServicesKit';
     4. try {
     5. netQuality.on('netQosChange', (list: Array<netQuality.NetworkQos>) => {
     6. if (list.length > 0) {
     7. list.forEach((qos) => {
     8. // 回调信息处理
     9. console.info(`该数据链路类型的上行带宽: ${JSON.stringify(qos.linkUpBandwidth)}.` );
     10. console.info(`该数据链路类型的下行带宽: ${JSON.stringify(qos.linkDownBandwidth)}.` );
     11. // 应用可根据上下行带宽等信息实时感知网络质量，调整请求策略
     12. });
     13. }
     14. });
     15. } catch (err) {
     16. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
     17. }
     ```
  2. 在网络质量好时进行请求预取，提前发送后续可能产生的请求，并缓存获取的资源。后续产生对应请求时直接加载缓存的资源，提高响应速度，避免卡顿。

     ```
     1. // 引入包名
     2. import { rcp } from '@kit.RemoteCommunicationKit';
     3. import { HashMap } from "@kit.ArkTS";
     4. export class PrefetchingRcp {
     5. private session = rcp.createSession();
     6. private responsePrefetched: HashMap<string, rcp.Response> = new HashMap<string, rcp.Response>();
     7. public async prefetch(url: string) {
     8. const request = new rcp.Request(url);
     9. try {
     10. // 发送预取请求
     11. let response: rcp.Response = await this.session.fetch(request);
     12. // 缓存预取结果
     13. this.responsePrefetched.set(url, response);
     14. return Promise.resolve();
     15. } catch (reason) {
     16. console.error(`Rcp prefetch failed: ${reason.code}`);
     17. return Promise.reject();
     18. }
     19. }
     20. }
     ```
  3. 在网络质量差时降低请求频率/请求数据量，避免加剧网络拥塞。

**网络质量差场景**

* 特征：在信号屏蔽区（如地下停车场）或高密度接入环境（如拥挤食堂），网络呈现持续低带宽（<1Mbps）、高延迟（>100ms）和高丢包率。
* 典型场景：拥挤的食堂、停车场。
* 最佳实践：在拥塞场景及时降低请求频率、请求数据量等，网络恢复时恢复请求。除通过netQosChange判断网络质量外，还可通过订阅网络场景识别事件，直接检测网络拥塞或网络信号差。检测到时及时减少请求，避免反复请求加剧网络拥塞。示例代码如下：

  ```
  1. // 引入包名
  2. import { netQuality } from '@kit.NetworkBoostKit';
  3. import { BusinessError } from '@kit.BasicServicesKit';
  4. try {
  5. netQuality.on('netSceneChange', (list: Array<netQuality.NetworkScene>) => {
  6. if (list.length > 0) {
  7. list.forEach((sceneInfo) => {
  8. // 网络场景识别回调信息处理
  9. if (sceneInfo.scene == 'congestion') {
  10. // 检测到当前为网络拥塞场景，应用处理
  11. }
  12. if (sceneInfo.scene == 'normal') {
  13. // 检测到网络不再拥塞，应用处理
  14. }
  15. if (sceneInfo.weakSignalPrediction) {
  16. // 弱信号场景预测，感知到网络质量即将变差，应用提前应对
  17. }
  18. });
  19. }
  20. });
  21. } catch (err) {
  22. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
  23. }
  ```

## 信息收集说明

当您使用网络领航员能力时，App的使用记录会被收集，并可能会通过您的华为账号对应的联系方式与您进行取得联系进行使用回访，以便我们进一步优化提升该能力。

当您使用该能力时，以下数据会被收集，请悉知：

* 您使用网络领航员时需要先关联您的华为账号，且当您选择打开关联体验改进计划的开关时，则默认表示同意上传使用日志；
* 您使用该能力时的App对应的bundle name以及版本号；
* 您使用该能力时的App使用的网络模拟场景以及对应的时间。

## 附录

**不同网络场景的QoS情况**：

**进出电梯**

该场景一共5分钟，循环执行。

| 子阶段 | 持续时间（分:秒） | 网络接口 | 下行带宽 | 下行带宽分布 | 上行带宽 | 上行带宽分布 | 时延 | 时延分布 | 丢包 | 丢包分布 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 等待电梯 | 0-30s | WLAN | 60-140Mbps | random | 30-60Mbps | random | 0-20ms | random | 0.00%-0.01% | random |
| 进入电梯 | 30-90s | WLAN | 90-50Mbps | linearDecrease | 30-8Mbps | linearDecrease | 2-20ms | linearIncrease | 0.00%-0.21% | random |
| 电梯关门 | 90-100s | WLAN | 1-0Mbps | random | 1-0Mbps | random | 0-200ms | random | 0.00%-0.00% | random |
| 电梯关门 | 100-110s | WLAN | 1-0Mbps | linearDecrease | 1-0Mbps | linearDecrease | 200-1000ms | linearIncrease | 0.00%-8.00% | linearIncrease |
| 电梯关门 | 110-120s | 蜂窝 | 20-50Mbps | random | 5-15Mbps | random | 0-20ms | random | 0.00%-0.20% | random |
| 电梯上行 | 120-180s | 蜂窝 | 20-50Mbps | random | 5-15Mbps | random | 0-30ms | random | 0.01%-0.20% | random |
| 电梯开门 | 180-210s | 蜂窝 | 30-100Mbps | linearIncrease | 15-50Mbps | linearIncrease | 30-0ms | linearDecrease | 0.01%-0.10% | random |
| 走出电梯 | 210-240s | 蜂窝 | 100-300Mbps | linearIncrease | 50-100Mbps | linearIncrease | 0-10ms | random | 0.00%-0.01% | random |
| 走出电梯 | 240-300s | WLAN | 60-140Mbps | random | 30-60Mbps | random | 10-20ms | random | 0.00%-0.01% | random |

**离家断开WLAN**

该场景一共3分钟，循环执行。

| 子阶段 | 持续时间（分:秒） | 网络接口 | 下行带宽 | 下行带宽分布 | 上行带宽 | 上行带宽分布 | 时延 | 时延分布 | 丢包 | 丢包分布 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 在家中 | 0-60s | WLAN | 60-140Mbps | random | 30-60Mbps | random | 0-15ms | random | 0.00%-0.00% | random |
| 在门口 | 60-90s | WLAN | 100-50Mbps | linearDecrease | 40-10Mbps | linearDecrease | 5-15ms | linearIncrease | 0.00%-0.00% | random |
| 越走越远 | 90-110s | WLAN | 5-0Mbps | random | 5-0Mbps | random | 0-200ms | random | 0.00%-0.00% | random |
| 越走越远 | 110-120s | WLAN | 5-0Mbps | linearDecrease | 5-0Mbps | linearDecrease | 200-1000ms | linearIncrease | 0.00%-8.00% | linearIncrease |
| 越走越远 | 120-150s | 蜂窝 | 200-400Mbps | random | 30-70Mbps | random | 0-35ms | random | 0.00%-0.00% | random |
| 在路上 | 150-180s | 蜂窝 | 300-500Mbps | random | 50-100Mbps | random | 0-25ms | random | 0.00%-0.00% | random |

**到家连接WLAN**

该场景一共3分钟，循环执行。

| 子阶段 | 持续时间（分:秒） | 网络接口 | 下行带宽 | 下行带宽分布 | 上行带宽 | 上行带宽分布 | 时延 | 时延分布 | 丢包 | 丢包分布 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 在走廊 | 0-60s | 蜂窝 | 300-500Mbps | random | 50-100Mbps | random | 0-25ms | random | 0.00%-0.00% | random |
| 在门口 | 60-90s | 蜂窝 | 200-400Mbps | random | 30-70Mbps | random | 0-35ms | random | 0.00%-0.00% | random |
| 在门口 | 90-120s | WLAN | 30-50Mbps | random | 10-30Mbps | random | 10-40ms | random | 0.00%-0.00% | random |
| 进入家中 | 120-180s | WLAN | 60-140Mbps | random | 30-60Mbps | random | 0-20ms | random | 0.00%-0.00% | random |

**拥挤的食堂**

该场景一共5分钟，循环执行。

| 子阶段 | 持续时间（分:秒） | 网络接口 | 下行带宽 | 下行带宽分布 | 上行带宽 | 上行带宽分布 | 时延 | 时延分布 | 丢包 | 丢包分布 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 进入食堂 | 0-60s | WLAN | 60-140Mbps | random | 30-60Mbps | random | 0-20ms | random | 0.00%-0.00% | random |
| 排队取餐 | 60-120s | WLAN | 0-5Mbps | random | 0-5Mbps | random | 10-100ms | random | 0.00%-2.4% | random |
| 就坐用餐 | 120-240s | WLAN | 15-60Mbps | random | 10-20Mbps | random | 0-55ms | random | 0.00%-0.2% | random |
| 离开食堂 | 240-300s | WLAN | 60-140Mbps | random | 30-60Mbps | random | 0-20ms | random | 0.00%-0.00% | random |

**信号弱的地库**

该场景一共5分钟，循环执行。

| 子阶段 | 持续时间（分:秒） | 网络接口 | 下行带宽 | 下行带宽分布 | 上行带宽 | 上行带宽分布 | 时延 | 时延分布 | 丢包 | 丢包分布 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 前往停车场 | 0-60s | 蜂窝 | 300-500Mbps | random | 50-100Mbps | random | 0-25ms | random | 0.00%-0.00% | random |
| 在停车场中 | 60-240s | 蜂窝 | 0-10Mbps | random | 0-10Mbps | random | 30-100ms | random | 0.00%-0.50% | random |
| 走出停车场 | 240-300s | 蜂窝 | 300-500Mbps | random | 50-100Mbps | random | 0-35ms | random | 0.00%-0.00% | random |

**乘坐地铁**

该场景一共5分钟，循环执行。

| 子阶段 | 持续时间（分:秒） | 网络接口 | 下行带宽 | 下行带宽分布 | 上行带宽 | 上行带宽分布 | 时延 | 时延分布 | 丢包 | 丢包分布 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 地铁站台候车 | 0-30s | 蜂窝 | 300-500Mbps | random | 50-100Mbps | random | 0-25ms | random | 0.00%-0.00% | random |
| 列车行驶 | 30-150s | 蜂窝 | 0-10Mbps | random | 0-10Mbps | random | 0-35ms | random | 0.00%-0.50% | random |
| 列车到站 | 150-180s | 蜂窝 | 300-500Mbps | random | 50-100Mbps | random | 0-35ms | random | 0.00%-0.00% | random |
| 列车行驶 | 180-270s | 蜂窝 | 0-10Mbps | random | 0-10Mbps | random | 0-35ms | random | 0.00%-0.50% | random |
| 列车到站 | 270-300s | 蜂窝 | 300-500Mbps | random | 50-100Mbps | random | 0-25ms | random | 0.00%-0.00% | random |

**乘坐高铁**

该场景一共10分钟，循环执行。

| 子阶段 | 持续时间（分:秒） | 网络接口 | 下行带宽 | 下行带宽分布 | 上行带宽 | 上行带宽分布 | 时延 | 时延分布 | 丢包 | 丢包分布 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 高铁站台候车 | 0-60s | 蜂窝（卡1） | 300-500Mbps | random | 50-100Mbps | random | 0-25ms | random | 0.00%-0.00% | random |
| 列车在市郊行驶 | 60-120s | 蜂窝（卡1） | 100-250Mbps | random | 20-50Mbps | random | 0-35ms | random | 0.00%-0.50% | random |
| 列车在山区行驶 | 120-240s | 蜂窝（卡1） | 0-8Mbps | random | 0-8Mbps | random | 300-2000ms | random | 0.00%-5.00% | random |
| 列车在山区行驶 | 240-360s | 蜂窝（卡2） | 30-50Mbps | random | 10-30Mbps | random | 300-2000ms | random | 0.00%-5.00% | random |
| 列车在市郊到站 | 360-480s | 蜂窝（卡1） | 200-400Mbps | random | 30-70Mbps | random | 0-35ms | random | 0.00%-0.50% | random |
| 下车出站 | 480-600s | 蜂窝（卡1） | 300-500Mbps | random | 50-100Mbps | random | 0-25ms | random | 0.00%-0.00% | random |

**高速公路自驾**

该场景一共5分钟，循环执行。

| 子阶段 | 持续时间 | 网络接口 | 下行带宽 | 下行带宽分布 | 上行带宽 | 上行带宽分布 | 时延 | 时延分布 | 丢包 | 丢包分布 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 汽车在市区行驶 | 0-60S | 蜂窝 | 300-500Mbps | random | 50-100Mbps | random | 0-25ms | random | 0.00%-0.00% | random |
| 汽车进出隧道 | 60-120s | 蜂窝 | 0-2Mbps | random | 0-2Mbps | random | 300-2000ms | random | 0.00%-5.00% | random |
| 汽车在市区行驶 | 120-180s | 蜂窝 | 300-500Mbps | random | 50-100Mbps | random | 0-25ms | random | 0.00%-0.00% | random |
| 汽车在高架行驶 | 180-240s | 蜂窝 | 0-10Mbps | random | 0-10Mbps | random | 0-35ms | random | 0.00%-0.00% | random |
| 汽车在市区行驶 | 240-300s | 蜂窝 | 300-500Mbps | random | 50-100Mbps | random | 0-25ms | random | 0.00%-0.00% | random |
