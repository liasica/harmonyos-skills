---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-overview-502-beta1
title: 总览
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > OS平台行为变更说明 > 总览
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:44+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:517090ea222bbc89a12d940dcba86b6c9f01e12310237a8c3fc25f9e0828aa3d
---

## OS平台API行为的变更

| Kit | 变更描述 | 变更引入版本 | 变更影响 | 影响设备类型 | 变更生效规则 |
| --- | --- | --- | --- | --- | --- |
| Ability | [包管理bundleManager/AbilityInfo中新增必选属性orientationId](changelogs-for-all-apps-b123sp16.md#包管理bundlemanagerabilityinfo中新增必选属性orientationid) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | 使用DevEco Studio 5.0.2 Release及以上版本时生效 |
| ArkData | [数据库插入长度为0的Uint8Array的数据，getRow、getValue 接口返回值发生变化](changelogs-for-all-apps-b123sp16.md#数据库插入长度为0的uint8array的数据getrowgetvalue-接口返回值发生变化) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.2(14)变更生效 |
| [关系型数据管理@ohos.data.relationalStore.d.ts中getRdbStore接口新增错误码14800020，用于业务侧进行恢复重建数据库](changelogs-for-all-apps-b123sp16.md#关系型数据管理ohosdatarelationalstoredts中getrdbstore接口新增错误码14800020用于业务侧进行恢复重建数据库) | 5.0.2(14) Beta1 | 中 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.2(14)变更生效 |
| ArkTS | [延迟加载（lazy import）影响异步任务执行时序变更为不影响异步任务执行时序](changelogs-for-all-apps-b123sp16.md#延迟加载lazy-import影响异步任务执行时序变更为不影响异步任务执行时序) | 5.0.2(14) Beta1 | 大 | phone, tablet, 2in1 | 全部生效 |
| [执行幂运算（\*\*）当底数是1，指数是NaN或ToNumber之后是NaN的情况的返回值变更](changelogs-for-all-apps-b123sp16.md#执行幂运算当底数是1指数是nan或tonumber之后是nan的情况的返回值变更) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | 全部生效 |
| [String.prototype.lastIndexOf接口查找空字符串行为变更](changelogs-for-all-apps-b123sp16.md#stringprototypelastindexof-接口查找空字符串行为变更) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | 全部生效 |
| ArkUI | [ImageAttributeModifier支持new方式创建ColorFilter对象传入colorFilter接口变更](changelogs-for-all-apps-b123sp16.md#imageattributemodifier支持new方式创建colorfilter对象传入colorfilter接口变更) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.2(14)变更生效 |
| [轴事件分发机制变更](changelogs-for-all-apps-b123sp16.md#轴事件分发到xcomponent组件变更) | 5.0.2(14) Beta1 | 小 | 2in1 | 全部生效 |
| [List组件首次创建布局时，Scroller控制器的跳转方法优先级变更为高于initialIndex的优先级](changelogs-for-all-apps-b123sp16.md#list组件首次创建布局时scroller控制器的跳转方法优先级变更为高于initialindex的优先级) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.2(14)变更生效 |
| [Image组件的borderRadius接口支持动态修改](changelogs-for-all-apps-b123sp16.md#image组件的borderradius接口支持动态修改) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.2(14)变更生效 |
| [RichEditor（富文本）在光标处于文本起始位置情况时向前删除空文本onWillChange回调变更](changelogs-for-all-apps-b123sp16.md#richeditor富文本在光标处于文本起始位置情况时向前删除空文本onwillchange回调变更) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.2(14)变更生效 |
| [修复zIndex接口会影响组件在3D变换中的透视效果的错误行为](changelogs-for-all-apps-b123sp16.md#修复zindex接口会影响组件在3d变换中的透视效果的错误行为) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.2(14)变更生效 |
| [屏幕Display对象rotation和orientation属性变更](changelogs-for-all-apps-b123sp16.md#屏幕display对象rotation和orientation属性变更) | 5.0.2(14) Beta1 | 大 | tablet | targetSdkVersion ≥ 5.0.2(14)变更生效 |
| [@ohos.arkui.uiExtension中uiExtension命名空间下新增properties必选属性](changelogs-for-all-apps-b123sp16.md#ohosarkuiuiextension中uiextension命名空间下新增properties必选属性) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | 使用DevEco Studio 5.0.2 Release及以上版本时生效 |
| [Navigation的menus接口、NavDestination的title和menus接口支持Resource类型资源](changelogs-for-all-apps-b123sp16.md#navigationnavdestination的title和menus接口支持resource类型资源) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | 使用DevEco Studio 5.0.2 Release及以上版本时生效 |
| [在PC/2in1设备上getWindowStatus和on('windowStatusChange')接口在窗口最大化状态返回值变更](changelogs-for-all-apps-b123sp16.md#在2in1设备上getwindowstatus和onwindowstatuschange接口在窗口最大化状态返回值变更) | 5.0.2(14) Beta1 | 中 | tablet, 2in1 | targetSdkVersion ≥ 5.0.2(14)变更生效 |
| [setWindowLayoutFullScreen、setImmersiveModeEnabledState接口在PC/2in1设备的自由多窗模式上禁用](changelogs-for-all-apps-b123sp16.md#setwindowlayoutfullscreensetimmersivemodeenabledstate接口在2in1设备和平板设备的自由多窗模式上禁用) | 5.0.2(14) Beta1 | 小 | tablet, 2in1 | 全部生效 |
| [setWindowBrightness在PC/2in1设备的行为变更](changelogs-for-all-apps-b123sp16.md#setwindowbrightness在2in1设备的行为变更) | 5.0.2(14) Beta1 | 小 | 2in1 | 全部生效 |
| Basic Service Kit | [setAppAccess错误码变更](changelogs-for-all-apps-b123sp16.md#setappaccess错误码变更) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | 全部生效 |
| Call Service Kit | [kit.CallKit.d.ts文件废弃，替换为kit.CallServiceKit.d.ts文件访问级别](changelogs-for-all-apps-b123sp16.md#kitcallkitdts文件废弃替换为kitcallservicekitdts文件访问级别) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | 使用DevEco Studio 5.0.2 Release及以上版本时生效 |
| Core File Kit | [持久化权限激活接口实现从sandbox\_manager模块切换到UPMS模块](changelogs-for-all-apps-b123sp16.md#持久化权限激活接口实现从sandbox_manager模块切换到upms模块) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | 全部生效 |
| Core Vision Kit | [@hms.ai.vision.objectDetection.d.ts和@hms.ai.vision.skeletonDetection.d.ts方法文件变更](changelogs-for-all-apps-b123sp16.md#hmsaivisionobjectdetectiondts和hmsaivisionskeletondetectiondts方法文件变更) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | 全部生效 |
| Form Kit | [FormLink的router事件允许拉起Ability类型范围变更](changelogs-for-all-apps-b123sp16.md#formlink的router事件允许拉起ability类型范围变更) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | 全部生效 |
| Image Kit | [image.ImageSource.DecodingOptionsForPicture接口的desiredAuxiliaryPictures属性系统能力变更](changelogs-for-all-apps-b123sp16.md#imageimagesourcedecodingoptionsforpicture接口的desiredauxiliarypictures属性系统能力变更) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | 全部生效 |
| [image.Component.setAuxiliaryPictureInfo接口行为变更](changelogs-for-all-apps-b123sp16.md#imagecomponentsetauxiliarypictureinfo接口行为变更) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.2(14)变更生效 |
| [image.Component.OH\_AuxiliaryPictureNative\_SetInfo()接口行为变更](changelogs-for-all-apps-b123sp16.md#imagecomponentoh_auxiliarypicturenative_setinfo接口行为变更) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.2(14)变更生效 |
| [image接口Heif格式类型变更](changelogs-for-all-apps-b123sp16.md#imagecomponentoh_packingoptions结构体heif格式编码参数变更) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.2(14)变更生效 |
| Media Kit | [AVErrorCode枚举值变更](changelogs-for-all-apps-b123sp16.md#averrorcode枚举值变更) | 5.0.2(14) Beta1 | 中 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.2(14)变更生效 |
| Scan Kit | [自定义界面扫码权限校验错误码变更](changelogs-for-all-apps-b123sp16.md#自定义界面扫码权限校验误码变更变更原因) | 5.0.2(14) Beta1 | 小 | phone, tablet | targetSdkVersion ≥ 5.0.2(14)变更生效 |
| [集成自定义界面扫码应用适配窗口子系统属性变更](changelogs-for-all-apps-b123sp16.md#集成自定义界面扫码应用适配窗口子系统属性变更) | 5.0.2(14) Beta1 | 大 | tablet | targetSdkVersion ≥ 5.0.2(14)变更生效 |

## UX样式或效果的变更

| 变更描述 | 变更引入版本 | 变更影响 | 影响设备类型 | 变更生效规则 |
| --- | --- | --- | --- | --- |
| [borderImage的outset属性按照实际的延伸距离来绘制边框向外扩展的效果](changelogs-ux-b123sp16.md#borderimage的outset属性按照实际的延伸距离来绘制边框向外扩展的效果) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.2(14)变更生效 |
| [Canvas使用toDataURL接口生成图片，对于带有透明度的图片，创建为“image/png”或“image/webp”格式时，其效果可能会发生变更](changelogs-ux-b123sp16.md#canvas使用todataurl接口生成图片对于带有透明度的图片创建为imagepng或imagewebp格式时其效果可能会发生变更) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.2(14)变更生效 |
| [bindSheet半模态面板视觉样式增加](changelogs-ux-b123sp16.md#bindsheet半模态面板视觉样式增加) | 5.0.2(14) Beta1 | 小 | phone | targetSdkVersion ≥ 5.0.2(14)变更生效 |
| [bindSheet半模态面板标题与关闭按钮布局变更](changelogs-ux-b123sp16.md#bindsheet半模态面板标题与关闭按钮布局变更) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.0.2(14)变更生效 |

## 命令行工具的变更

| 变更描述 | 变更引入版本 | 变更影响 | 影响设备类型 | 变更生效规则 |
| --- | --- | --- | --- | --- |
| [hdc file recv命令不支持操作媒体库目录](changelogs-for-all-apps-b123sp16.md#hdc命令file-recv命令不支持操作媒体库目录) | 5.0.2(14) Beta1 | 大 | phone, tablet, 2in1 | 使用DevEco Studio 5.0.2 Release及以上版本时生效 |
| [hdc的file recv命令及shell读取权限变更](changelogs-for-all-apps-b123sp16.md#hdc命令file-recv命令及shell读取权限变更) | 5.0.2(14) Beta1 | 中 | phone, tablet, 2in1 | 使用DevEco Studio 5.0.2 Release及以上版本时生效 |
| [hidumper组件内存输出显示每列后新增一个空格](changelogs-for-all-apps-b123sp16.md#hidumper组件内存输出显示每列后新增一个空格) | 5.0.2(14) Beta1 | 小 | phone, tablet, 2in1 | 使用DevEco Studio 5.0.2 Release及以上版本时生效 |
| [安装的应用是已卸载的预置应用时校验签名是否一致](changelogs-for-all-apps-b123sp16.md#安装的应用是已卸载的预置应用时校验签名是否一致) | 5.0.2(14) Beta1 | 中 | phone, tablet, 2in1 | 使用DevEco Studio 5.0.2 Release及以上版本时生效 |
