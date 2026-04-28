---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelog-overview
title: 总览
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.1(13) > OS平台能力 > OS平台行为变更说明 > 总览
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:56+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:8173ba6b3bf108ded3dd025aacf162367c9445c573c38cb7f1bf92ff74394830
---

## OS平台API行为的变更

| Kit | 变更描述 | 变更引入版本 | 变更影响 | 影响设备类型 | 变更生效规则 |
| --- | --- | --- | --- | --- | --- |
| Ability Kit | [禁止Extension进程拉起启动框架](changelogs-for-all-apps-b106.md#禁止extension进程拉起启动框架) | 5.0.1(13) Beta3 | 小 | phone, tablet, 2in1 | 全部生效 |
| ArkTS | [convertXml模块未支持parentKey属性的行为变更](changelogs-for-all-apps-b106.md#convertxml模块未支持parentkey属性的行为变更) | 5.0.1(13) Beta3 | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.1(13)变更生效 |
| ArkUI | [在字节码HAR中通过router.getState()获取的path内容变更](changelogs-for-all-apps-b106.md#在字节码har中通过routergetstate获取的path内容变更) | 5.0.1(13) Beta3 | 小 | phone, tablet, 2in1 | 全部生效 |
| ArkUI | [禁止在转场动画过程中，更新消失节点的属性](changelogs-for-all-apps-b106.md#禁止在转场动画过程中更新消失节点的属性) | 5.0.1(13) Beta3 | 中 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.1(13)变更生效 |
| ArkUI | [优化getWindowProperties，增加返回值中drawableRect的实时性，调用行为变更](changelogs-for-all-apps-b106.md#优化getwindowproperties增加返回值中drawablerect的实时性调用行为变更) | 5.0.1(13) Beta3 | 小 | tablet, 2in1 | 全部生效 |
| ArkUI | [RichEditor（富文本）从组件外拖入内容onWillChange、onDidChange回调变更](changelogs-for-all-apps-b106.md#richeditor富文本从组件外拖入内容onwillchangeondidchange回调变更) | 5.0.1(13) Beta3 | 小 | phone, tablet, 2in1 | 全部生效 |
| ArkUI | [RichEditor（富文本）onWillChange接口返回值变更](changelogs-for-all-apps-b106.md#richeditor富文本onwillchange接口返回值变更) | 5.0.1(13) Beta3 | 小 | phone, tablet, 2in1 | 全部生效 |
| ArkUI | [RichEditor（富文本）TypingStyle默认字体大小变更](changelogs-for-all-apps-b106.md#richeditor富文本typingstyle默认字体大小变更) | 5.0.1(13) Beta3 | 小 | phone, tablet, 2in1 | 全部生效 |
| ArkUI | [RichEditor（富文本）onDidChange接口变更](changelogs-for-all-apps-b106.md#richeditor富文本ondidchange接口变更)  \* 该变更在11月19日更新的ROM版本引入，ROM版本号为5.0.0.107。 | 5.0.1(13) Beta3 | 小 | phone, tablet, 2in1 | 全部生效 |
| ArkUI | [RichEditor（富文本）删除完成后光标位置变更](changelogs-for-all-apps-b106.md#richeditor富文本删除完成后光标位置变更)  \* 该变更在11月19日更新的ROM版本引入，ROM版本号为5.0.0.107。 | 5.0.1(13) Beta3 | 小 | phone, tablet, 2in1 | 全部生效 |
| Localization Kit | [国家、地区本地化名称变更](changelogs-for-all-apps-b106.md#国家地区本地化名称变更) | 5.0.1(13) Beta3 | 小 | phone, tablet, 2in1 | 全部生效 |
| Localization Kit | [时间日期格式“十一月”格式化结果错误问题修改](changelogs-for-all-apps-b106.md#时间日期格式十一月格式化结果错误问题修改)  \* 该变更在11月19日更新的ROM版本引入，ROM版本号为5.0.0.107。 | 5.0.1(13) Beta3 | 小 | phone, tablet, 2in1 | 全部生效 |
| Localization Kit | [日期时间段格式化在zh-Hant-HK下结果错误问题修改](changelogs-for-all-apps-b106.md#日期时间段格式化在zh-hans-hk下结果错误问题修改) | 5.0.1(13) Beta3 | 小 | phone, tablet, 2in1 | 全部生效 |
| Localization Kit | [归属地获取接口对无效号码的归属计算错误问题修改](changelogs-for-all-apps-b106.md#归属地获取接口对无效号码的归属计算错误问题修改) | 5.0.1(13) Beta3 | 小 | phone, tablet, 2in1 | 全部生效 |
| Localization Kit | [系统支持国家地区列表变更](changelogs-for-all-apps-b106.md#系统支持国家地区列表变更)  \* 该变更在11月19日更新的ROM版本引入，ROM版本号为5.0.0.107。 | 5.0.1(13) Beta3 | 小 | phone, tablet, 2in1 | 全部生效 |
| ArkUI | [鼠标按键处理行为变更](changelogs-for-all-apps-b112.md#鼠标按键处理行为变更) | 5.0.1(13) Release | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.1(13)变更生效 |
| ArkUI | [动画接口在播放次数为无限循环时的行为变更](changelogs-for-all-apps-b112.md#动画接口在播放次数为无限循环时的行为变更) | 5.0.1(13) Release | 小 | phone, tablet, 2in1 | 全部生效 |
| ArkUI | [系统对单应用最大创建UIAbility数量限制变更](changelogs-for-all-apps-b112.md#系统对单应用最大创建uiability数量限制变更) | 5.0.1(13) Release | 小 | phone, 2in1 | 全部生效 |
| ArkUI | [Video组件不再默认解析并自动播放拖拽信息中的视频资源](changelogs-for-all-apps-b112.md#video组件不再默认解析并自动播放拖拽信息中的视频资源)  \* 该变更在2025年1月8日更新的ROM版本引入，ROM版本号为5.0.0.123。 | 5.0.1(13) Release | 小 | phone, tablet, 2in1 | 全部生效 |
| ArkWeb | [onErrorReceive接口在首次加载woff等在线字体资源不再触发的行为变更](changelogs-for-all-apps-b112.md#onerrorreceive接口在首次加载woff等在线字体资源不再触发的行为变更) | 5.0.1(13) Release | 小 | phone, tablet, 2in1 | 全部生效 |
| Form Kit | [PostCardAction的router事件允许拉起Ability类型范围变更](changelogs-for-all-apps-b112.md#postcardaction的router事件允许拉起ability类型范围变更)  \* 该变更在2025年1月8日更新的ROM版本引入，ROM版本号为5.0.0.123。 | 5.0.1(13) Release | 小 | phone, tablet, 2in1 | 全部生效 |
| 公共能力 | [app.json中bundleName字段正则匹配规则修改](changelogs-for-all-apps-b112.md#appjson中bundlename字段正则匹配规则修改)  \* 该变更在2024年12月8日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.5.306。 | 5.0.1(13) Release | 小 | phone, tablet, 2in1 | 使用DevEco Studio 5.0.1 Release及以上版本时生效 |

## UX样式或效果的变更

| 变更描述 | 变更引入版本 | 变更影响 | 影响设备类型 | 变更生效规则 |
| --- | --- | --- | --- | --- |
| [QRCode深浅色适配修改](changelogs-ux-b106.md#qrcode深浅色适配修改) | 5.0.1(13) Beta3 | 小 | phone, tablet, 2in1 | 全部生效 |
| [属性动画onFinish结束回调在UIAbility退后台时因有限循环动画被终止而提前触发](changelogs-ux-b106.md#属性动画onfinish结束回调在uiability退后台时因有限循环动画被终止而提前触发) | 5.0.1(13) Beta3 | 小 | phone, tablet, 2in1 | 全部生效 |
| [TextInput组件在非标准字体场景下showCounter接口布局变更](changelogs-ux-b106.md#textinput组件在非标准字体场景下showcounter接口布局变更) | 5.0.1(13) Beta3 | 小 | phone, tablet, 2in1 | 全部生效 |
| [MenuItem组件在非2in1设备上超长文本布局由缩略显示变更为换行显示](changelogs-ux-b106.md#menuitem组件在非2in1设备上超长文本布局由缩略显示变更为换行显示) | 5.0.1(13) Beta3 | 小 | phone, tablet | targetSdkVersion ≥ 5.0.1(13)变更生效 |
| [Tabs组件barOverlap接口默认效果变更](changelogs-ux-b106.md#tabs组件baroverlap接口默认效果变更) | 5.0.1(13) Beta3 | 小 | phone, tablet, 2in1 | 全部生效 |
| [Tabs组件底部页签默认高度由52vp变更为48vp](changelogs-ux-b112.md#tabs组件底部页签默认高度由52vp变更为48vp) | 5.0.1(13) Release | 小 | phone, tablet, 2in1 | 全部生效 |
| [画布组件在绘制文本时设置globalCompositeOperation、fillStyle和globalAlpha属性的效果变更](changelogs-ux-b112.md#canvasrenderingcontext2d和offscreencanvasrenderingcontext2d的globalcompositeoperation属性变更为在绘制文本时生效) | 5.0.1(13) Release | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.1(13)变更生效 |
| [NavDestination的Dialog模式默认支持系统动画](changelogs-ux-b112.md#navdestination的dialog模式默认支持系统动画) | 5.0.1(13) Release | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.1(13)变更生效 |

## 开发工具的变更

| 工具分类 | 变更描述 | 变更引入版本 | 变更等级 | 影响设备类型 | 变更生效规则 |
| --- | --- | --- | --- | --- | --- |
| 命令行工具 | [禁止bm命令进行跨用户操作](changelogs-for-all-apps-b106.md#禁止bm命令进行跨用户操作)  \* 该变更在11月19日更新的ROM版本引入，ROM版本号为5.0.0.107。 | 5.0.1(13) Beta3 | 小 | phone, tablet, 2in1 | 使用DevEco Studio 5.0.1 Release及以上版本时生效 |
| 命令行工具 | [应用发生OOM时Heapdump产物文件格式变更](changelogs-for-all-apps-b112.md#应用发生oom时heapdump产物文件格式变更)  \* 该变更在2024年12月8日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.5.306。 | 5.0.1(13) Release | 小 | phone, tablet, 2in1 | 使用DevEco Studio 5.0.1 Release及以上版本时生效 |
