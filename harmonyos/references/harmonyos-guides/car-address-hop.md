---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/car-address-hop
title: 地址流转至车机
breadcrumb: 指南 > 系统 > 硬件 > Car Kit（车服务） > 实现车机导航流转 > 地址流转至车机
category: harmonyos-guides
scraped_at: 2026-04-29T13:33:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:715242ce0c8b2d366e94d2104515f629f1707aeb9c519f29669ddec50dbd18e1
---

将手机应用的地址文本流转至车机指定地图应用的能力。

## 场景介绍

碰一碰地址流转：用户在手机地址文本页面与车机中控屏指定区域碰一碰后，将手机上的地址数据流转至车机的地图应用，发起地址搜索。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/xLnCBQkrSAWCHRU4nRcPrQ/zh-cn_image_0000002558605312.png?HW-CC-KV=V1&HW-CC-Date=20260429T053328Z&HW-CC-Expire=86400&HW-CC-Sign=AE5E2057646506BB79DB5C973F3834EE88C318AF7378E7BD21327C563F4A90CA)

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [accessibilityTextHint](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitytexthint12)(value: string): T | 设置辅助功能文本提示。 |

### 参数value说明

value是一个Json格式的字符串，具体属性说明如下：

| 属性 | 描述 |
| --- | --- |
| type | 文本类型，必须是“**location**”。 |
| groupId | 地址编组ID，用于多个Text文本分组，同一组的地址文本流转到车机后会自动拼接到一起。 |
| index | 地址索引，用来标识同一组地址文本的顺序。同一组的地址文本流转到车机后会按照index由小到大拼接成一个完整地址。  例如：'XXX街道' + 'XXX商场' = 'XXX街道XXX商场' |

给手机地址文本（Text）设置accessibilityTextHint属性后即可使用地址流转能力。

## 开发步骤

1. 能力配置。

   碰一碰地址流转场景下，metadata的name取值为carHopCapability，value取值应为**carHopAddress**，具体配置请参考[配置能力](car-preparations.md#配置能力)。示例代码如下所示：

   ```
   1. "metadata": [
   2. {
   3. "name": "carHopCapability",
   4. "value": "carHopAddress"
   5. }
   6. ]
   ```
2. 定义accessibilityTextHint的value值。

   ```
   1. const hintContentValue = JSON.stringify({
   2. type: 'location', // 类型，必须是 'location'
   3. groupId: 1, // 分组id
   4. index: 2, // 索引
   5. });
   ```
3. 给地址文本设置accessibilityTextHint属性。

   ```
   1. Text('xxx一路')
   2. .fontSize(20)
   3. .fontWeight(FontWeight.Bold)
   4. .accessibilityTextHint(hintContentValue)

   6. // 单地址场景
   7. Text('xxx二路')
   8. .accessibilityTextHint(JSON.stringify({ type: 'location' }))

   10. // 多地址场景
   11. Text('xxx商场')
   12. .accessibilityTextHint(JSON.stringify({ type: 'location', groupId: 1, index: 1, }))
   13. Text('xxx街')
   14. .accessibilityTextHint(JSON.stringify({ type: 'location', groupId: 1, index: 0, }))
   ```
