---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-roadmap/all-changelogs-503
title: 5.0.3(15)的行为变更汇总
breadcrumb: 变更预告 > 变更预告 > 5.0.3(15)的行为变更汇总
category: harmonyos-roadmap
scraped_at: 2026-09-02T14:55:01+08:00
doc_updated_at: 2026-08-04
content_hash: sha256:c53fedd89696d9ee1463084df24e31c29fb19c13c44976dee63b04b723408d38
---

## OS平台API行为的变更

| Kit | 变更描述 | 变更引入版本 | 影响设备类型 | 变更生效规则 |
| --- | --- | --- | --- | --- |
| Ability | [installSource字段规格变更](../harmonyos-releases/changelogs-for-all-apps-5031.md#section317) | 5.0.3(15) Beta1 | phone, tablet, 2in1 | 全部生效 |
| AppGallery Kit | [kit.StoreKit.d.ts文件废弃，替换为kit.AppGalleryKit.d.ts文件](../harmonyos-releases/changelogs-for-all-apps-5031.md#section257) | 5.0.3(15) Beta1 | phone, tablet, 2in1 | 使用DevEco Studio 5.0.3 Release及以上版本时生效 |
| ArkTS | [信号处理方法注册接口sigaction支持SA\_RESETHAND标志位变更](../harmonyos-releases/changelogs-for-all-apps-5031.md#section233) | 5.0.3(15) Beta1 | phone, tablet, 2in1 | 全部生效 |
| ArkUI | [FrameNode被UINode包裹时isVisible接口返回值发生变更](../harmonyos-releases/changelogs-for-all-apps-5031.md#section322) | 5.0.3(15) Beta1 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.3(15)变更生效 |
| [富文本组件RichEditor的onCopy回调中设置preventDefault()时的行为变更](../harmonyos-releases/changelogs-for-all-apps-5031.md#section326) | 5.0.3(15) Beta1 | phone, tablet, 2in1 | 全部生效 |
| AVCodec Kit | [OH\_AVCodecOnStreamChanged在音频解码场景的默认行为变更](../harmonyos-releases/changelogs-for-all-apps-5031.md#section319) | 5.0.3(15) Beta1 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.3(15)变更生效 |
| Localization Kit | [变更缅甸文，马来文和泰文的显示名称](../harmonyos-releases/changelogs-for-all-apps-5031.md#section301) | 5.0.3(15) Beta1 | phone, tablet, 2in1 | 全部生效 |
| Media Kit | [系统录屏应用调用的截屏接口变更](../harmonyos-releases/changelogs-for-all-apps-5031.md#section309) | 5.0.3(15) Beta1 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.3(15)变更生效 |
| 应用配置文件 | [supportWindowModes选项配置fullscreen和split时，窗口全屏启动](../harmonyos-releases/changelogs-for-all-apps-5031.md#section328) | 5.0.3(15) Beta1 | 2in1 | targetSdkVersion ≥ 5.0.3(15)变更生效 |
| ArkUI | [Image、Text和ListItem组件onDragStart接口默认行为变更](../harmonyos-releases/changelogs-for-all-apps-5032.md#section363) | 5.0.3(15) Beta2 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.3(15)变更生效 |
| [轴事件支持BEGIN、END及CANCEL类型回调触发](../harmonyos-releases/changelogs-for-all-apps-5032.md#section356) | 5.0.3(15) Beta2 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.3(15)变更生效 |
| [TextController的SetStyledString接口支持保存设置的属性字符串信息到调用的TextController中](../harmonyos-releases/changelogs-for-all-apps-5032.md#section348) | 5.0.3(15) Beta2 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.3(15)变更生效 |
| [2in1设备上，悬浮窗层级由低于dock栏调整为高于dock栏](../harmonyos-releases/changelogs-for-all-apps-5032.md#section362) | 5.0.3(15) Beta2 | 2in1 | 全部生效 |
| Call Service Kit | [通话应用在前台时不显示通话胶囊](../harmonyos-releases/changelogs-for-all-apps-5032.md#section359) | 5.0.3(15) Beta2 | phone, tablet | targetSdkVersion ≥ 5.0.3(15)变更生效 |
| Performance Analysis Kit | [HiAppEvent模块onReceive、OH\_HiAppEvent\_OnReceive、takeNext接口支持应用分身故障日志订阅隔离](../harmonyos-releases/changelogs-for-all-apps-5032.md#section364) | 5.0.3(15) Beta2 | phone, tablet, 2in1 | 全部生效 |
| ArkUI | [C API轴事件接口OH\_ArkUI\_UIInputEvent\_GetSourceType和OH\_ArkUI\_UIInputEvent\_GetToolType接口返回值变更](../harmonyos-releases/changelogs-for-all-apps-5033.md#section367) | 5.0.3(15) Release | phone, tablet, 2in1 | 全部生效 |

## UX样式或效果的变更

| 变更描述 | 变更引入版本 | 影响设备类型 | 变更生效规则 |
| --- | --- | --- | --- |
| [半模态SheetMode.EMBEDDED模式支持响应ESC键退出](../harmonyos-releases/changelogs-ux-5031.md#section324) | 5.0.3(15) Beta1 | phone, tablet, 2in1 | 全部生效 |
| [动态照片自动播放效果变更](../harmonyos-releases/changelogs-ux-5032.md#section341) | 5.0.3(15) Beta2 | phone, tablet | 全部生效 |
| [NavDestination标题栏工具栏支持跟手滑动隐藏后，超过2秒未操作，不恢复显示](../harmonyos-releases/changelogs-ux-5032.md#section342) | 5.0.3(15) Beta2 | phone, tablet, 2in1 | 全部生效 |
| [Tabs组件TabBar的显示和隐藏动效变更](../harmonyos-releases/changelogs-ux-5032.md#section918554861317) | 5.0.3(15) Beta2 | phone, tablet, 2in1 | 全部生效 |

## 开发工具的变更

| 工具分类 | 变更描述 | 变更引入版本 | 影响设备类型 | 变更生效规则 |
| --- | --- | --- | --- | --- |
| 命令行工具 | [hilog日志在商用版本（nolog版本）开发者模式下默认日志级别由info变为warning](../harmonyos-releases/changelogs-for-all-apps-5031.md#section312) | 5.0.3(15) Beta1 | phone, tablet, 2in1 | 使用DevEco Studio 5.0.3 Release及以上版本时生效 |
