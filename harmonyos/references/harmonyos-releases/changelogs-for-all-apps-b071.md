---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-b071
title: 针对所有应用的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > 接口行为变更说明 > HarmonyOS NEXT Release引入的接口行为变更 > 针对所有应用的变更
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:08+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:0957e4d1e2a80a0b4192b57c042d050b328ed9650e93491975c95ecfb7ccf381
---

## Ability Kit

### 禁止通过wantAgent拉起ExtensionAbility

**变更原因**

三方应用创建拉起ExtensionAbility的wantAgent，并发送携带此wantAgent的通知。通过桌面点击通知拉起该ExtensionAbility，应用退出后，该ExtensionAbility进程无法退出从而影响功耗。

**变更影响**

此变更涉及应用适配。

变更前：

三方应用创建拉起ExtensionAbility的wantAgent，并发送携带此wantAgent的通知。通过桌面点击通知可以拉起该ExtensionAbility。

变更后：

三方应用创建拉起ExtensionAbility的wantAgent，并发送携带此wantAgent的通知。通过桌面点击通知无法拉起该ExtensionAbility。

**起始API Level**

9

**变更的接口/组件**

wantAgent.trigger接口

**适配指导**

建议不要创建拉起ExtensionAbility的wantAgent，否则通过wantAgent的trigger接口拉起该ExtensionAbility会拉起失败。

## ArkUI

### startAbility/openLink锁屏时限制拉起行为

**变更原因**

锁屏时对任意拉起应用的行为增加限制。

**变更影响**

此变更涉及应用适配。

变更前：锁屏时可调用startAbility/openLink接口正常拉起应用并正常保持应用窗口为前台状态。

变更后：锁屏时调用startAbility/openLink接口拉起应用时，当应用窗口到前台状态时会被窗口管理阻止进而关闭窗口和应用。

**起始API Level**

6

**变更的接口/组件**

startAbility/openLink

涉及相关接口:

UIAbilityContext:

* startAbility(want: Want, options?: StartOptions)
* startAbility(want: Want, callback: AsyncCallback<void>)
* startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>)
* startAbilityByCall(want: Want)
* startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>)
* startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>)
* startAbilityForResult(want: Want, options?: StartOptions)
* startAbilityAsCaller(want: Want, options?: StartOptions)
* startAbilityAsCaller(want: Want, options: StartOptions, callback: AsyncCallback<void>)
* startAbilityForResultWithAccount(want: Want, accountId: number, options?: StartOptions)
* startAbilityForResultWithAccount(want: Want, accountId: number, callback: AsyncCallback<AbilityResult>)
* startAbilityForResultWithAccount(want: Want, accountId: number, options: StartOptions, callback: AsyncCallback<void>)
* startAbilityWithAccount(want: Want, accountId: number, options?: StartOptions)
* startAbilityWithAccount(want: Want, accountId: number, callback: AsyncCallback<void>)
* startAbilityWithAccount(want: Want, accountId: number, options: StartOptions, callback: AsyncCallback<void>)
* startRecentAbility(want: Want, options?: StartOptions)
* startRecentAbility(want: Want, callback: AsyncCallback<void>)
* startRecentAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>)
* startAbilityByCallWithAccount(want: Want, accountId: number)
* startAbilityAsCaller(want: Want, callback: AsyncCallback<void>)
* openLink(link: string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>)

ServiceExtensionContext:

* startAbility(want: Want, options?: StartOptions)
* startAbility(want: Want, callback: AsyncCallback<void>)
* startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>)
* startAbilityWithAccount(want: Want, accountId: number, options?: StartOptions)
* startAbilityWithAccount(want: Want, accountId: number, callback: AsyncCallback<void>)
* startAbilityWithAccount(want: Want, accountId: number, options: StartOptions, callback: AsyncCallback<void>)
* startAbilityByCall(want: Want)
* startAbilityAsCaller(want: Want, options?: StartOptions)
* startAbilityAsCaller(want: Want, callback: AsyncCallback<void>)
* startAbilityAsCaller(want: Want, options: StartOptions, callback: AsyncCallback<void>)
* startRecentAbility(want: Want, options?: StartOptions)
* startRecentAbility(want: Want, callback: AsyncCallback<void>)
* startRecentAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>)
* startAbilityByCallWithAccount(want: Want, accountId: number)
* openLink(link:string, options?: OpenLinkOptions)

UIExtensionContext:

* startAbility(want: Want, options?: StartOptions)
* startAbility(want: Want, callback: AsyncCallback<void>)
* startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>)
* startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>)
* startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>)
* startAbilityForResult(want: Want, options?: StartOptions)
* startAbilityForResultAsCaller(want: Want, options?: StartOptions)
* openLink(link:string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>)
* openAtomicService(appId: string, options?: AtomicServiceOptions)

AbilityDelegator:

* startAbility(want: Want, callback: AsyncCallback<void>)

InsightIntentContext:

* startAbility(want: Want, callback: AsyncCallback<void>)

FeatureAbility:

* startAbility(parameter: StartAbilityParameter, callback: AsyncCallback<number>)
* startAbilityForResult(parameter: StartAbilityParameter, callback: AsyncCallback<AbilityResult>)

StaticSubscriberExtensionContext:

* startAbility(want: Want, callback: AsyncCallback<void>)

InputMethodExtensionContext:

* startAbility(want: Want)

AccessibilityExtensionContext:

* startAbility(want: Want)

FormExtensionContext:

* startAbility(want: Want, callback: AsyncCallback<void>)

WindowExtensionContext:

* startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>)

**适配指导**

锁屏时取消对相关接口的调用，否则会关闭被拉起的应用。

## Media Library Kit

### @ohos.file.photoAccessHelper相册添加资产、移除资产等接口行为变更

**变更原因**

为了优化资产的保存逻辑，修改了媒体库对于“资产-相册”的对应关系。修改前一个图片/视频资源可以通过关系映射存在于多个逻辑相册中，修改后一张照片仅能归属一个实体相册。

说明

该变更在10月18日更新的系统ROM版本引入，ROM版本号为NEXT.0.0.72。

**变更影响**

此变更涉及应用适配。

1. 向相册中添加资产addAssets：

   变更前：直接添加查询得到的资产。

   变更后：添加该资产的复制体，复制资产与原资产的内容和元数据一致，用户相册表现无差异。
2. 从相册中移除资产removeAssets：

   变更前：删除相册与资产的映射关系。

   变更后：将对应资产从相册移除到回收站。
3. 设置相册名称setAlbumName和commitModify：

   变更前：直接修改该相册的album\_name。

   变更后：删除该相册，并新建一条元数据相同的相册，命名为新名称。
4. 注册对指定uri的监听registerChange：

   变更前：注册查询出来的Asset uri监听，添加删除修改等行为通知查询出来的Asset Uri。

   变更后：操作的对象均为复制体，故通知时通知复制体uri变更。

**起始API Level**

10和11

**变更的接口/组件**

1. 向相册中添加资产：addAssets(assets: Array<PhotoAsset>): void
2. 从相册中移除资产：removeAssets(assets: Array<PhotoAsset>): void
3. 设置相册名称：
4. setAlbumName(name: string):void，

   commitModify(callback: AsyncCallback<void>): void
5. 注册对指定uri的监听：registerChange(uri: string, forChildUris: boolean, callback: Callback<ChangeData>): void

**适配指导**

接口使用方式没有变化，开发者在调用接口过程中无需额外适配，但接口行为发生变化，开发者应当注意其关联变化并适当调整。

1. 调用addAssets向相册添加照片后，并非将原照片加入到当前相册，而是将复制体添加到相册内。后续若想操作资产，应操作当前相册内的复制体资产。
2. 调用removeAssets移除资产后，资产将到回收站中。
3. 调用deleteAlbums删除相册，会将相册内资产一并放到回收站。
4. 调用setAlbumName和commitModify修改相册名称，会将原相册删除再新建一个新的改名相册。后续若想继续操作相册，应操作新建的相册。接口行为变更后，在调用setAlbumName和commitModify修改相册名后，需使用[getAlbums](../harmonyos-references-V5/js-apis-photoaccesshelper-V5.md#getalbums-2)获取新命名的相册进行后续操作。
5. 调用registerChange注册对指定uri的监听，在调用addAssets接口时会收到复制体资产添加的新增通知，在调用removeAssets和deleteAlbums时会收到相册内资产的删除通知，在调用setAlbumName和commitModify时，会收到相册更新通知。
