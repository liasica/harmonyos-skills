---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-map
title: ArkTS API错误码
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:17:26+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:20068688d73c25ecb5c13c50e7779732338e66c30868419208ac52102f137a96
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)。

## 1002600001 系统内部错误

PhonePC/2in1TabletWearable

**错误信息**

System internal error.

**错误描述**

当发生系统内部错误时，将返回该错误码。

**可能原因**

其他未知错误。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600002 应用连接地图服务失败

PhonePC/2in1TabletWearable

**错误信息**

Failed to connect to the Map Kit server.

**错误描述**

应用连接地图服务失败。

**可能原因**

1. 设备网络存在问题。
2. 使用自动签名时，未连接上地图服务。

**处理步骤**

1. 检查设备网络状态。
2. 清除旧证书配置后，重新自动签名，并配置client\_id和证书指纹；从HarmonyOS 5.0.2(14)版本开始，可参考[开发准备](../harmonyos-guides/map-config-agc.md)进行配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/ouTPmvV8QDOuSX4PxR5pAQ/zh-cn_image_0000002583480901.png?HW-CC-KV=V1&HW-CC-Date=20260428T001725Z&HW-CC-Expire=86400&HW-CC-Sign=E82DA83B2AB3A4F9D4F82F7B344F769168221DEB128D7679B1275D4A4363C811)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/YiNn_ByiSaepBmpaCHHQVg/zh-cn_image_0000002552801252.png?HW-CC-KV=V1&HW-CC-Date=20260428T001725Z&HW-CC-Expire=86400&HW-CC-Sign=F9014751530922F8C4C02E3112D3DFC5B3FD9C62A67A6219390D275033B8011B)
3. 如未解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600003 应用身份校验失败

PhonePC/2in1TabletWearable

**错误信息**

App authentication failed.

**错误描述**

应用身份校验失败。

**可能原因**

1. 项目module.json5文件中配置的client\_id与AGC上不一致。
2. AGC上公钥指纹为空或错误。
3. 设备网络状态差，身份认证超时。
4. 公钥指纹配置后还未生效。
5. 配置profile文件之前，未开通地图服务开关。
6. 配置自动签名时，重复配置导致AGC上调试证书和本地使用证书不匹配。

**处理步骤**

1. 检查module.json5文件中配置的client\_id与AGC上是否一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/VXTtae1mQPuZSpZlekJGoQ/zh-cn_image_0000002583440947.png?HW-CC-KV=V1&HW-CC-Date=20260428T001725Z&HW-CC-Expire=86400&HW-CC-Sign=12026677A3FE2CC396513D4D9FF1416F8EA0A7E1602F0F3A3BA7C5A650E766FC)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/hWuqT4k1QoK29gkOeGdY1Q/zh-cn_image_0000002552960902.png?HW-CC-KV=V1&HW-CC-Date=20260428T001725Z&HW-CC-Expire=86400&HW-CC-Sign=AD2BA1674A40D641974E4B0B54CA197763436D3F40DA3256FFED89DED1F0AEAA)
2. 重新生成公钥指纹（[自动生成签名证书指纹](../app/agc-help-signature-info-0000001628566748.md#section958212134217)/[手动生成签名证书指纹](../app/agc-help-signature-info-0000001628566748.md#section2049119231438)），然后在AGC上[配置公钥指纹](../app/agc-help-cert-fingerprint-0000002278002933.md)。
3. 检查设备网络状态后重新尝试。
4. 将设备的系统时间往后调整1天。
5. 请根据[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)，先打开地图服务开关，然后重新[申请调试Profile](../app/agc-help-add-debugprofile-0000001914423102.md)，并[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)。
6. 自动签名证书不匹配有两种解决方案：

   方案一：将本地已生成的csr签名，通过AGC重新生成新的调试证书，然后通过新的调试证书选择生成新的指纹证书。

   自动签名默认已生成的csr签名在如下图路径下，马赛克部分为用户名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/ImoLA3CNQxuO6qwC626eQg/zh-cn_image_0000002583480903.png?HW-CC-KV=V1&HW-CC-Date=20260428T001725Z&HW-CC-Expire=86400&HW-CC-Sign=21225E6CEA9D3746F453A4B291F8189BB5F83FDD16AF242657A85CEDAEEC50BC)

   在AGC上新增证书，将上述所选csr文件选中并生成新的调试证书。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/H8mXX_mSQ4-kwrs8RlSy1A/zh-cn_image_0000002552801254.png?HW-CC-KV=V1&HW-CC-Date=20260428T001725Z&HW-CC-Expire=86400&HW-CC-Sign=30F8F1BFC9F1600ACB55D99638BDDC923677FDECB276A1FEC33354BB759A928B)

   然后添加公钥指纹，选中刚才自己生成调试证书即可。（需注意，配置完成后由于鉴权缓存，可能还是无法马上显示地图，须清除缓存或者将设备的系统时间往后调整1天，才能立刻显示地图。）

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/YPOx3OQ6Qva8k2ctiKkTLw/zh-cn_image_0000002583440949.png?HW-CC-KV=V1&HW-CC-Date=20260428T001725Z&HW-CC-Expire=86400&HW-CC-Sign=90533909795698235D8D8B6D83EB10C70230D8D4E6EAFD56CB29D7C3EFCE83C4)

   方案二：将本地配置自动签名证书和AGC上调试证书全部删除，重新生成新的自动签名，调试证书会自动生成，并用新的调试证书生成公钥指纹。

   将build-profile.json5文件下signingConfigs参数删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/liOPgu5fRqiyjMazwQZKfQ/zh-cn_image_0000002552960904.png?HW-CC-KV=V1&HW-CC-Date=20260428T001725Z&HW-CC-Expire=86400&HW-CC-Sign=8365B3BA316DF656DDCC3258C940D53321939328208E4F1C2EBFF70DC5975BD9)

   将config文件夹下所有内容删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/bzJGFHmKR0uL80kuc1MHXw/zh-cn_image_0000002583480905.png?HW-CC-KV=V1&HW-CC-Date=20260428T001725Z&HW-CC-Expire=86400&HW-CC-Sign=0102DFEA89CE108A08F7EB04C71234F888A3AC26C6106C2491AEFC3D4C3F95CE)

   将AGC上自动签名生成的调试证书删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/Z_G6tH3ISHKjxD5qPswh5g/zh-cn_image_0000002552801256.png?HW-CC-KV=V1&HW-CC-Date=20260428T001725Z&HW-CC-Expire=86400&HW-CC-Sign=0BC04AB4112A49D628852C5669DE79645368A7579D7A4D974A4DDAACA1D0D31F)

   将旧证书删除后生成新的自动签名，调试证书会被同步创建，然后用新生成的调试证书生成新的指纹即可。（需注意，配置完成后由于鉴权缓存，可能还是无法马上显示地图，须清除缓存或者将设备的系统时间往后调整1天，才能立刻显示地图。）

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/FBEMQINPTN6hSJPNIBOK1w/zh-cn_image_0000002583440951.png?HW-CC-KV=V1&HW-CC-Date=20260428T001725Z&HW-CC-Expire=86400&HW-CC-Sign=878E3D65E28AEE59DFB7C35DF3EE9690FBB0DFE63B480076E1E7FC3B2C22116A)
7. 如未解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600004 应用没有开通地图服务权限

PhonePC/2in1TabletWearable

**错误信息**

The Map permission is not enabled.

**错误描述**

应用没有开通地图服务权限。

**可能原因**

1. 没有开通地图服务权限。
2. client\_id未配置。

**处理步骤**

1. [开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)。
2. 配置client\_id。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/cdEX8ZQyTlONYgZaGZYQgQ/zh-cn_image_0000002552960906.png?HW-CC-KV=V1&HW-CC-Date=20260428T001725Z&HW-CC-Expire=86400&HW-CC-Sign=450EF1C57C1F319695ED2D30B139C889D3E119EA364C9EFCEE096B4F5D43F610)
3. 如未解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600005 网络不可用

PhonePC/2in1TabletWearable

**错误信息**

The network is unavailable.

**错误描述**

网络不可用。

**可能原因**

网络不可用。

**处理步骤**

检查网络后尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600006 API调用量超出配额

PhonePC/2in1TabletWearable

**错误信息**

The API call times exceed the quota.

**错误描述**

API调用量超出配额。

**可能原因**

API调用量超出配额。

**处理步骤**

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600007 API的QPS超过配额

PhonePC/2in1TabletWearable

**错误信息**

The API QPS exceeds the quota.

**错误描述**

API的QPS超过配额。

**可能原因**

API的QPS超过配额。

**处理步骤**

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600008 接口已经欠费

PhonePC/2in1TabletWearable

**错误信息**

The API is in arrears.

**错误描述**

接口欠费。

**可能原因**

接口欠费。

**处理步骤**

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600009 API未订购付费套餐

PhonePC/2in1TabletWearable

**错误信息**

The API has not subscribed to any pay-as-you-go package.

**错误描述**

API未订购付费套餐。

**可能原因**

未订购付费套餐。

**处理步骤**

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600010 服务器繁忙，请稍后再试

PhonePC/2in1TabletWearable

**错误信息**

The server is busy. Please wait and try again.

**错误描述**

服务器繁忙。

**可能原因**

服务器繁忙。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600011 服务器异常

PhonePC/2in1TabletWearable

**错误信息**

Server error.

**错误描述**

当发生系统内部错误时，将返回该错误码。

**可能原因**

1.服务器异常。

2.网络不可用。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600012 国家或地区码异常

PhonePC/2in1TabletWearable

**错误信息**

The country code is not supported.

**错误描述**

当传入国家/地区码错误时，将返回该错误码。

**可能原因**

不支持该国家/地区码。

**处理步骤**

更换国家/地区码。

## 1002600013 当前路由地未知，稍后重试

PhonePC/2in1TabletWearable

**错误信息**

The current routing location is unknown. Try again later.

**错误描述**

当前路由地未知。

**可能原因**

获取当前设备的路由地失败。

**处理步骤**

1. 检查设备网络是否可用。
2. 尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600014 地图应用启动失败。

PhonePC/2in1TabletWearable

**错误信息**

Failed to start the map app.

**错误描述**

地图应用启动失败。

**可能原因**

设备未安装地图应用且拉起应用市场地图下载详情页失败。

**处理步骤**

1. 通过应用市场搜索下载地图应用。
2. 尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600015 热力图ID已存在

PhonePC/2in1TabletWearable

**错误信息**

The heatmap ID already exists.

**错误描述**

热力图ID已存在。

**可能原因**

热力图ID已存在。

**处理步骤**

尝试更换ID或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002600999 未知错误

PhonePC/2in1TabletWearable

**错误信息**

Unknown error.

**错误描述**

当发生系统内部错误时，将返回该错误码。

**可能原因**

其他未知错误。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002601001 要操作的对象已经不存在

PhonePC/2in1TabletWearable

**错误信息**

The object to be operated does not exist.

**错误描述**

操作的对象不存在。

**可能原因**

操作的对象不存在。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002601002 自定义地图样式文件不存在

PhonePC/2in1TabletWearable

**错误信息**

The custom map style file does not exist.

**错误描述**

自定义地图样式文件不存在。

**可能原因**

1.自定义地图样式文件不存在。

2.设备网络不可用。

**处理步骤**

1.在[Petal Maps Studio](https://developer.petalmaps.com/console/studio/)网站检查样式id是否存在。

2.检查设备网络是否可用。

3.尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002601004 样式内容格式不正确

PhonePC/2in1TabletWearable

**错误信息**

The style content format is incorrect.

**错误描述**

样式内容格式不正确。

**可能原因**

样式内容格式不正确。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002601005 生成自定义组件图标失败

PhonePC/2in1TabletWearable

**错误信息**

Failed to generate the icon of the custom component.

**错误描述**

生成自定义组件图标失败。

**可能原因**

生成自定义组件图标失败。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002602001 起终点无归属国家，或服务错误

PhonePC/2in1TabletWearable

**错误信息**

The start and end points do not have home countries, or a service error occurred.

**错误描述**

起终点无归属国家，或服务错误。

**可能原因**

参数错误。

**处理步骤**

请检查起终点后尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1002602002 不支持跨区进行路径规划

PhonePC/2in1TabletWearable

**错误信息**

Cross-region route planning is not supported.

**错误描述**

不支持跨区进行路径规划。

**可能原因**

参数错误。

**处理步骤**

检查入参是否涉及跨区。

## 1002602003 起始点或结束点超过100个

PhonePC/2in1TabletWearable

**错误信息**

The number of start points or end points exceed 100.

**错误描述**

起始点或结束点超过100个。

**可能原因**

参数错误。

**处理步骤**

检查入参，起点或终点个数是否超限。

## 1002602004 两点直线距离超过限制的距离

PhonePC/2in1TabletWearable

**错误信息**

The linear distance between the start point and end point exceeds the upper limit.

**错误描述**

两点直线距离超过限制的距离。

**可能原因**

参数错误。

**处理步骤**

检查入参，两点直线距离是否超过接口限制的距离。

## 1002602005 起点/终点/途经点不支持导航

PhonePC/2in1TabletWearable

**错误信息**

The start point, end point, or waypoint does not support navigation.

**错误描述**

起点/终点/途经点不支持导航。

**可能原因**

参数错误。

**处理步骤**

检查入参。

## 1002602006 请求点位映射到道路同一点上

PhonePC/2in1TabletWearable

**错误信息**

The request point is mapped to the same point on the road.

**错误描述**

请求点位映射到道路同一点上。

**可能原因**

参数错误。

**处理步骤**

检查入参。

## 1002603001 空结果

PhonePC/2in1TabletWearable

**错误信息**

Zero result.

**错误描述**

空结果。

**可能原因**

参数错误。

**处理步骤**

检查入参。

## 1022100001 要操作的地图控制器不存在

PhonePC/2in1Tablet

**错误信息**

The map controller to be operated does not exist.

**错误描述**

要操作的地图控制器不存在。

**可能原因**

要操作的地图控制器不存在。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 401 入参无效

PhonePC/2in1TabletWearable

**错误信息**

Invalid input parameter.

**错误描述**

入参无效。

**可能原因**

入参不符合要求。

**处理步骤**

检查入参。

## 801 功能不支持。设备能力受限，调用接口失败。

PhonePC/2in1TabletWearable

**错误信息**

Capability not supported. Failed to call the API due to limited device capabilities.

**错误描述**

功能不支持。设备能力受限，调用接口失败。

**可能原因**

当前设备不支持调用该接口。

**处理步骤**

更换设备或者使用其他接口。
