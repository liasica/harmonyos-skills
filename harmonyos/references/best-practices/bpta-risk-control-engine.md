---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-risk-control-engine
title: 星盾机密风控引擎
breadcrumb: 最佳实践 > 技术创新 > 星盾机密风控引擎
category: best-practices
scraped_at: 2026-09-02T15:03:15+08:00
doc_updated_at: 2026-09-02
content_hash: sha256:277bdccb13777a2b36c3d987f04048be1b0cd2238c76b2d393d1c5386322e5ec
---

## 概述

星盾机密风控引擎是鸿蒙系统安全能力的重要组成部分，作为基于端侧机密空间的创新风控解决方案，在基于内核容器隔离安全的运行环境中运行，支持开发者灵活配置自适应风控策略，实现高效风险研判。该引擎既能保障用户数据隐私安全（数据不出机密空间），又能进行实时风险检测，为诈骗等关键风险场景提供全面安全防护，有效保护鸿蒙用户的财产与设备安全。

星盾机密风控引擎采用"云侧管理+端侧执行"的架构，功能原理如下：

* 云侧管理：应用在云侧管理台注册应用风险因子并配置风控策略规则，启用后可将策略配置加密下发至端侧设备；
* 端侧执行：端侧在机密计算空间中接收风险因子和风控策略配置，应用通过Device Security Kit的[riskControlEngine.importRiskFactors()](../harmonyos-references/devicesecurity-riskcontrolengine-api.md#riskcontrolengineimportriskfactors)接口写入业务风险因子数据，调用Device Security Kit的[riskControlEngine.getRiskControlResult()](../harmonyos-references/devicesecurity-riskcontrolengine-api.md#riskcontrolenginegetriskcontrolresult)接口执行策略规则，输出风险评估结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/G3ixLBqIR42SP575JTlHcQ/zh-cn_image_0000002624974657.png "点击放大")

基于星盾机密风控引擎的架构设计，具备以下三个特点：

* 可算不可取：系统与应用的风险因子，应用可以用于策略规则的计算，但是无法将数据拿出到系统外；
* 可知不可见：系统与应用的风险因子，应用可以知道因子意义，但是其明文内容无法看到；
* 可用不泄露：系统与应用的风控策略或风控数据，在计算和使用过程中，不会被逆向泄露出去。

本文围绕星盾机密风控引擎，阐述诈骗场景识别、风险预警落地方案，覆盖涉诈全链路的检测与安全防护。

## 涉诈风险检测

### 场景描述

当前电信诈骗呈现跨平台、多链路的复杂特征，诈骗分子通常不会在单一应用内完成全部诈骗流程，而是跨多个APP和平台流转，因此需要联合多方应用与系统共同构建联防联控体系。

典型电信诈骗链路往往首先通过电话、短信、社交软件等各类通信渠道触达目标用户并获取信任，接着引导用户访问恶意URL或下载未知来源APP，最后利用虚假支付、远程协助等隐蔽方式诱导用户转账，完成诈骗闭环。面对这种跨平台诈骗模式，单一应用或系统的防护能力显得力不从心，需要星盾机密风控引擎实现跨应用、跨平台的协同防护。

本场景示例展示金融类应用基于星盾机密风控引擎，融合三方风险因子、系统风险因子进行联合风险决策。通过这种多方协作机制，各类应用均可接入星盾机密风控引擎，基于自有风险因子、系统风险因子及其他应用授权的风险因子，实现跨应用、跨平台的策略检测，构建全方位的反诈防护。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/Zt-jRRl9QFiZznVGQkR4xw/zh-cn_image_0000002624976475.png "点击放大")

### 实现原理

云侧管理：①通联类应用、金融类应用在平台注册各自风险因子的属性；②金融类应用作为策略执行主体配置多因子融合风控策略；③金融类应用将其云侧配置下发至端侧机密空间。

端侧执行：①两类应用在风险发生时通过调用接口将风险因子写入端侧机密空间；②金融类应用在关键节点（例如：转账）主动调用接口获取策略执行结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/GWoUd4q-RTOlGIIYnZWaoQ/zh-cn_image_0000002594457686.png)

### 开发步骤

在开发前，可参考指南中[星盾机密风控引擎](../harmonyos-guides/devicesecurity-starshieldconfidentialriskcontrolengine.md)和API参考中[RiskControlEngine（星盾机密风控引擎）](../harmonyos-references/devicesecurity-riskcontrolengine-api.md)。

1. [开通Device Security服务](../harmonyos-guides/devicesecurity-deviceverify-activateservice.md)中的星盾机密风控引擎。

2. 通过星盾机密风控引擎配置管理平台注册风险因子和配置策略。

   1、通联类APP和金融类APP注册风险因子，通联类APP将其风险因子授权给金融类APP，本场景主要涉及的风险因子： ①通联类风险因子：由通联类应用检测发现当前用户存在被诈骗风险；②系统风险因子：由系统检测出安装未知应用；③金融类风险因子：由金融类应用检测当前用户正在首次向陌生账户转账等异常行为特征。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/Uxirh78hRiGN-fmmJ4sbJQ/zh-cn_image_0000002594229184.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/KyuRfTKHQMCK8WTzZCnpUA/zh-cn_image_0000002595064112.png "点击放大")

   2、金融类APP通过融合以上三个维度的风险因子，可在端侧机密计算环境中执行多因子联动策略，综合评估用户当前面临的诈骗风险等级。本场景的风控策略配置采用"一策略三规则"的设计，在实际场景中开发者可基于自有业务场景灵活定义：①策略配置：当前策略采用权重累加模式，即将三条规则的执行结果分值相加作为策略结果，同时通过策略结果映射将累加结果映射为0~3的风险等级输出，便于应用根据不同等级采取差异化应对措施；②规则配置：通过规则表达式描述风险因子的命中条件，当风险因子满足表达式定义的条件时，则返回预设的分值，该分值将参与策略结果的累加计算。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/Not2tJKNSyyzKT6WDGXeXQ/zh-cn_image_0000002624508809.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/kkwWgzzjR9u8QT6axlzUjg/zh-cn_image_0000002594069274.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/QiwUVrcWR_iNl-Q8HyIs-A/zh-cn_image_0000002594229190.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/Rh3_ycxWTfu6VtDFKdrroA/zh-cn_image_0000002624628653.png "点击放大")

3. 通过调用接口的方式，应用写入风险因子值和执行策略返回结果。

   1、调用Device Security Kit的[riskControlEngine.importRiskFactors()](../harmonyos-references/devicesecurity-riskcontrolengine-api.md#riskcontrolengineimportriskfactors)接口导入应用风险因子数据。

   风险因子写入机制分为两类：应用自有风险因子需要通过调用接口主动写入风险值，开发者可根据业务逻辑灵活控制写入时机；系统风险因子已预制至端侧系统，当系统检测到风险事件发生时，会自动更新风险值，无需主动写入。

   金融类APP导入风险因子：

   ```typescript
   let data: riskControlEngine.ImportData = {
     appFactorData: [
       { factorName: "isFirstTransfer", factorValue: true }
     ],
     nonce: base64.encodeToStringSync(randData.data)
   };
   try {
     await riskControlEngine.importRiskFactors(data);
   } catch (error) {
     hilog.error(0x0000, 'riskControlEngine', 'ImportRiskFactors failed: %{public}d %{public}s', error.code,
       error.message);
   }
   ```

   通联类APP导入风险因子：

   ```typescript
   let data: riskControlEngine.ImportData = {
     appFactorData: [
       { factorName: "isExistFraudRisk", factorValue: true }
     ],
     nonce: base64.encodeToStringSync(randData.data)
   };
   try {
     await riskControlEngine.importRiskFactors(data);
   } catch (error) {
     hilog.error(0x0000, 'riskControlEngine', 'ImportRiskFactors failed: %{public}d %{public}s', error.code,
       error.message);
   }
   ```

   2、金融类APP在转账环节调用Device Security Kit的[riskControlEngine.getRiskControlResult()](../harmonyos-references/devicesecurity-riskcontrolengine-api.md#riskcontrolenginegetriskcontrolresult)接口，传入策略名称，获取策略执行结果（需要对结果解析后才可使用）。

   本场景中策略执行结果会根据风险因子命中情况返回不同值，若三项风险因子全部命中（代表风险较高）则返回"3"，金融类APP可根据返回结果制定不同风险预警。

   ```typescript
   let rand = cryptoFramework.createRandom();
   let len = 32;
   let randData = rand.generateRandomSync(len);
   let base64 = new util.Base64Helper();
   const request: riskControlEngine.RiskControlDetectionRequest = {
     policyName: "antiFraudRiskEvaluation",
     nonce: base64.encodeToStringSync(randData.data)
   };
   try {
     await riskControlEngine.getRiskControlResult(request);
   } catch (error) {
     hilog.error(0x0000, 'riskControlEngine', 'ImportRiskFactors failed: %{public}d %{public}s', error.code,
       error.message);
   }
   ```

## 约束与限制

**注意** 

* 星盾机密风控引擎从API 26版本开始支持。
* 星盾机密风控引擎依赖AppGallery Connect（AGC）服务权限，开发者需在AGC控制台申请开通服务权限并完成审批流程后方可使用。
* 星盾机密风控引擎目前仅支持手机，平板和PC，不支持的设备则会返回错误码801，Capability not supported。
* 应用需要根据自身业务场景进行风险因子注册和创建策略，审批通过之后才能启用并下发端侧。

## 总结

本文主要介绍星盾机密风控引擎典型应用场景及实现步骤：在端侧机密计算空间中，金融类应用依托系统风险因子与App专属风险因子，灵活自定义风控策略，完成风险研判，实现多方联防联控。

**以电信诈骗识别为典型场景：**

1. 构建风控策略并下发至端侧机密计算空间；
2. 应用风险事件发生时，调用Device Security Kit的[riskControlEngine.importRiskFactors()](../harmonyos-references/devicesecurity-riskcontrolengine-api.md#riskcontrolengineimportriskfactors)接口，将专属风险因子写入端侧机密计算空间；
3. 应用在关键节点（支付/转账）环节调用Device Security Kit的[riskControlEngine.getRiskControlResult()](../harmonyos-references/devicesecurity-riskcontrolengine-api.md#riskcontrolenginegetriskcontrolresult)接口，获取自定义风控策略结果用于业务决策，具体策略结果应根据应用的特定需求使用。
