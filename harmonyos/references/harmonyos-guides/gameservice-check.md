---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-check
title: 开发后自检
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 基础游戏服务（必选） > 游戏登录 > 开发后自检
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:89ec138b488837ecfef11e106b61ae75e51ad2cdefe0f76bbd99678f8da44235
---

为减少提交审核后被驳回的概率，请参考如下自检CheckList进行自检。

自检通过后，再前往AppGallery Connect提交游戏上架审核，具体操作请参见[发布HarmonyOS游戏](../app/agc-help-release-game-0000002364930906.md)。

| 一级分类 | 二级分类 | 检查项 | 影响 |
| --- | --- | --- | --- |
| 合规检查 | 隐私、游戏资质等 | 游戏内容、游戏安全性、用户隐私等符合华为应用市场审核规定，具体参考[应用审核指南](../50104.md)。 | 如不符合华为应用市场审核要求，游戏将会被驳回。 |
| 合规检查 | 用户实名认证信息 | 游戏提交上架前在AppGallery Connect完成[版署实名认证申请](../games-guides/game-center-identification-applyfor-0000002392353221.md)并通过审核。 | 上架申请可能会被驳回。 |
| 配置检查 | 应用类型 | 登录AppGallery Connect，检查应用类型是否为游戏。 | 如果不是游戏类型，会导致游戏防沉迷异常，提交审核会被驳回。 |
| 配置检查 | 发布包版本 | 上架游戏要求使用release版本的发布包。在SDK目录下检查oh-uni-package.json文件，非release要求替换，或者出包后解压并查看HAP资源文件夹，检查pack.info文件的releaseType字段。 | 使用非release版本的发布包申请上架会被驳回。 |
| 配置检查 | 签名证书指纹信息 | 在发布阶段要求添加发布证书对应的指纹。 | 未添加发布证书对应的指纹会影响上架。 |
| 配置检查 | APP ID映射关系 | 前往AppGallery Connect[配置APP ID映射关系](gameservice-gameplayer-huawei.md#配置app-id映射关系)。 | 未配置APP ID映射关系会影响游戏上架。 |
| 配置检查 | module.json5文件 | 在工程的entry模块module.json5文件中，查看metadata中client\_id和app\_id是否配置准确。 | 如果配置错误，Game Service Kit的接口将调用失败。 |
| 代码检查 | 初始化 | 游戏启动后，要求先调用[init](../harmonyos-references/gameservice-gameplayer.md#gameplayerinit-1)接口，调用结束后再调用其他接口。 | 游戏如未调用init接口，将导致审核被驳回。 |
| 代码检查 | 登录 | 华为账号登录图标要求遵守[开发者使用Account Kit的登录能力的管理细则](account-detailedrules.md)。 | 如不符合规范，可能会影响游戏上架。 |
| 代码检查 | 登录 | - 使用华为账号登录HarmonyOS 4及以下游戏与HarmonyOS 5.0及以上游戏时，账号资产要保持互通。  - 使用游戏官方账号登录官包与HarmonyOS 5.0及以上游戏时，账号资产要保持互通。 | 账号资产不互通会影响上架。 |
| 代码检查 | 登录 | 游戏登录必须调用[unionLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerunionlogin)接口拉起联合登录面板进行登录。 | 游戏如未调用unionLogin接口将导致审核被驳回。 |
| 代码检查 | 登录 | 用户设备未登录华为账号时，[unionLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerunionlogin)接口会拉起设备登录华为账号的弹窗。在窗口上点击返回后，该窗口无需反复自动弹出，且玩家可以手动再次拉起该窗口。 | 若设备登录华为账号的弹窗无法手动拉起，或反复自动弹出，将导致上架审核被驳回。 |
| 代码检查 | 登录 | 已接入官方账号登录的游戏，用户登录游戏默认沿用上次选择的登录账号，建议在游戏内为玩家提供[游戏内切换账号](gameservice-gameplayer-official.md#游戏内切换账号)功能，支持玩家重新选择游戏的登录账号。游戏重新拉起联合登录面板时，要求调用[unionLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerunionlogin)接口将loginParam中的showLoginDialog参数设置为true。若调用[unionLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerunionlogin)接口，整个游戏登录流程无需再调用[getLocalPlayer](../harmonyos-references/gameservice-gameplayer.md#gameplayergetlocalplayer)接口。 | 建议游戏支持玩家重新选择游戏的登录账号，否则游戏的登录体验不佳。 |
| 代码检查 | 登录 | 游戏登录后，要求调用[verifyLocalPlayer](../harmonyos-references/gameservice-gameplayer.md#gameplayerverifylocalplayer)接口进行合规校验，华为侧将校验当前设备的华为账号实名认证和游戏防沉迷管控情况，如校验未通过将返回对应的错误码。 | 游戏如未调用verifyLocalPlayer接口将导致审核被驳回。 |
| 代码检查 | 支付 | 若游戏内提供商品购买，则要求接入[IAP Kit（应用内支付服务）](iap-introduction.md)。 | 游戏如未调用createPurchase接口将导致审核被驳回。 |
| 代码检查 | 支付 | purchase接口传入的商品ID和商品类型与AppGallery Connect创建的商品ID和商品类型一致。 | 如果支付时传入的商品ID或商品类型与AppGallery Connect不一致，将无法拉起支付页面。 |
| 代码检查 | 支付 | 支付接口调用返回时、应用启动时均进行了补单处理和错误码[1001860001](../harmonyos-references/iap-error-code.md#section1001860001-内部错误)、[1001860051](../harmonyos-references/iap-error-code.md#section1001860051-由于已经拥有该商品购买失败)。请参考[权益发放](iap-delivering-products.md)。 | 如未在适当时机进行补单处理，会导致异常场景下（如关闭进程、崩溃）商品未正常发放。 |
| 代码检查 | 游戏退出 | 发布中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）的游戏要求具备玩家退出功能。 | 如不具备退出功能，审核将会被驳回。 |
