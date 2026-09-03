---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-overview-2600
title: 总览
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > OS平台行为变更说明 > 总览
category: harmonyos-releases
scraped_at: 2026-09-04T06:23:40+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:2ab9aada0076ec1e80ad59c9a8110f2b0697f27a41ca05b0e076ac622bc9b697
---

## OS平台API行为的变更

| Kit | 变更描述 | 变更引入版本 | 变更生效规则 |
| --- | --- | --- | --- |
| Ability Kit | [部分公共事件行为变更，增加管控](changelogs-for-all-apps-7001.md#ch2026020567372) | 26.0.0 Beta1 | targetSdkVersion ≥ 26.0.0变更生效 |
| [新增默认浏览器权限](changelogs-for-all-apps-7003.md#ch2026071666391) | 26.0.0 Release | 全部生效 |
| Agent Framework Kit | [OnDataCallback接口变更](changelogs-for-all-apps-7003.md#ch2026072498744) | 26.0.0 Release | targetSdkVersion ≥ 26.0.0变更生效 |
| ArkTS | [JSVM基于上游社区的Chromium/v8内核从132升级为144版本](changelogs-for-all-apps-7001.md#ch2026031811135) | 26.0.0 Beta1 | 全部生效 |
| [async函数类型判定修复](changelogs-for-all-apps-7001.md#ch2026030208973) | 26.0.0 Beta1 | 全部生效 |
| [JSVM支持Wasm解释器，jitless默认行为发生变更](changelogs-for-all-apps-7001.md#ch2026031127532) | 26.0.0 Beta1 | targetSdkVersion ≥ 26.0.0变更生效 |
| [修复ConvertXML的fastConvertToJSObject接口解析时丢失同级text节点的问题](changelogs-for-all-apps-7001.md#ch2026030646632) | 26.0.0 Beta1 | 全部生效 |
| ArkUI | [NodeAdapter的onAttachToNode回调触发时机变更](changelogs-for-all-apps-7001.md#ch2026010926267) | 26.0.0 Beta1 | targetSdkVersion ≥ 26.0.0变更生效 |
| [鼠标事件rawDeltaX和rawDeltaY的返回值变更](changelogs-for-all-apps-7001.md#ch2025112446948) | 26.0.0 Beta1 | 全部生效 |
| [属性字符串段落首个占位为CustomSpan或ImageAttachment时，支持设置段落样式](changelogs-for-all-apps-7001.md#ch2026031362881) | 26.0.0 Beta1 | targetSdkVersion ≥ 26.0.0变更生效 |
| [LayoutPolicy.matchParent父组件为Row、Column、Flex组件时，单方向设置matchParent的子组件布局行为变更](changelogs-for-all-apps-7001.md#ch2026031815681) | 26.0.0 Beta1 | targetSdkVersion ≥ 26.0.0变更生效 |
| [EmbeddedComponent获焦能力变更](changelogs-for-all-apps-7001.md#ch2026031800777) | 26.0.0 Beta1 | targetSdkVersion ≥ 26.0.0变更生效 |
| [WithTheme相关组件行为变更](changelogs-for-all-apps-7001.md#ch2026031417380) | 26.0.0 Beta1 | targetSdkVersion ≥ 26.0.0变更生效 |
| [ArkUI接口新增仅支持Stage模型的约束](changelogs-for-all-apps-7001.md#ch2026010615012) | 26.0.0 Beta1 | 全部生效 |
| [主页NavDestination中使用queryNavDestinationInfo接口和onResult接口的行为变更](changelogs-for-all-apps-7001.md#ch2026033084250) | 26.0.0 Beta1 | 全部生效 |
| [NODE\_SWIPER\_EVENT\_ON\_CONTENT\_DID\_SCROLL事件回调的返回值行为变更](changelogs-for-all-apps-7001.md#ch2026042449863) | 26.0.0 Beta1 | targetSdkVersion ≥ 26.0.0变更生效 |
| [@ReusableV2组件复用的reuse属性支持动态复用标识](changelogs-for-all-apps-7001.md#ch2026010512168) | 26.0.0 Beta1 | 全部生效 |
| [组件的阴影模糊半径规格变更](changelogs-for-all-apps-7001.md#ch2026022422576) | 26.0.0 Beta1 | targetSdkVersion ≥ 26.0.0变更生效 |
| [List组件onScrollVisibleContentChange事件行为变更](changelogs-for-all-apps-7002.md#ch2026032364747) | 26.0.0 Beta2 | targetSdkVersion ≥ 26.0.0变更生效 |
| [Image组件autoResize属性默认行为变更](changelogs-for-all-apps-7003.md#ch2026082810311) | 26.0.0 Release | 全部生效 |
| [沉浸光感新增生效约束](changelogs-for-all-apps-7003.md#section126372211) | 26.0.0 Release | targetSdkVersion ≥ 26.0.0变更生效 |
| ArkWeb | [ArkWeb基于上游社区的Chromium内核从132升级为144版本](changelogs-for-all-apps-7001.md#ch2026032368425) | 26.0.0 Beta1 | 全部生效 |
| [Cookie存储目录变更](changelogs-for-all-apps-7002.md#ch2026051550855) | 26.0.0 Beta2 | 全部生效 |
| Core File Kit | [沙箱路径/storage/Users/currentUser/appdata下无权限目录的stat和access行为变更](changelogs-for-all-apps-7003.md#ch2026072798462) | 26.0.0 Release | targetSdkVersion ≥ 26.0.0变更生效 |
| Localization Kit | [国际化-I18n模块部分新增接口错误码的类型从string变更为number](changelogs-for-all-apps-7003.md#ch2026080646373) | 26.0.0 Release | targetSdkVersion ≥ 26.0.0变更生效 |
| MDM Kit | [企业设备管理服务部分接口错误码的类型从string变更为number](changelogs-for-all-apps-7003.md#ch2026081113549) | 26.0.0 Release | targetSdkVersion ≥ 26.0.0变更生效 |
| Media Library Kit | [ohos.permission.READ\_IMAGEVIDEO权限变更](changelogs-for-all-apps-7001.md#ch2026042864213) | 26.0.0 Beta1 | 全部生效 |
| Network Kit | [getUidRxBytes、getUidTxBytes接口权限变更](changelogs-for-all-apps-7001.md#ch2026032458158) | 26.0.0 Beta1 | targetSdkVersion ≥ 26.0.0变更生效 |
| 权限管控 | [权限策略变更说明](changelogs-for-all-apps-7001.md#ch2026031760265) | 26.0.0 Beta1 | targetSdkVersion ≥ 26.0.0变更生效 |

## UX样式或效果的变更

| 变更描述 | 变更引入版本 | 变更生效规则 |
| --- | --- | --- |
| [notofonts三方件小语种字体升级变更](changelogs-ux-7001.md#ch2026022857472) | 26.0.0 Beta1 | 全部生效 |
| [表单类组件触摸热区最小高度变更](changelogs-ux-7001.md#ch2026031846233) | 26.0.0 Beta1 | targetSdkVersion ≥ 26.0.0变更生效 |
| [内置文本的组件文本样式优化](changelogs-ux-7001.md#ch2026032801249) | 26.0.0 Beta1 | targetSdkVersion ≥ 26.0.0变更生效 |
| [Dialog、Toast、AlphabetIndexer和文本选择菜单默认开启沉浸式系统材质](changelogs-ux-7001.md#ch2026032761266) | 26.0.0 Beta1 | targetSdkVersion ≥ 26.0.0变更生效 |
| [半模态居中弹窗最大高度变更](changelogs-ux-7001.md#ch2026031731268) | 26.0.0 Beta1 | targetSdkVersion ≥ 26.0.0变更生效 |
