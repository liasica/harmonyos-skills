---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-api-map
title: 实况窗Live View Kit与Push Kit的API字段关联
breadcrumb: API参考 > 应用服务 > Live View Kit（实况窗服务） > ArkTS API > 实况窗Live View Kit与Push Kit的API字段关联
category: harmonyos-references
scraped_at: 2026-09-02T14:53:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:18353ede61c3c59a5022f0e9e120f6344975abaee7780d3a3cbd01f307d2ff59
---

针对开发者通过App调用Live View Kit在本地创建实况窗后，再使用Push Kit更新或结束实况窗的场景，开发者可参考Live View Kit与Push Kit的API字段关联表格，在项目中配置实况窗业务所需的API字段。

为便于阅读与描述，表格内统一使用**端侧**作为Live View Kit ArkTS API的简称，使用**云侧**作为Push Kit REST API的简称。

| Live View Kit ArkTS API | Push Kit REST API | 差异说明 |
| --- | --- | --- |
| liveViewManager.startLiveView  liveViewManager.updateLiveView  liveViewManager.stopLiveView  liveViewManager.startLiveViewByTrigger  liveViewManager.stopLiveViewByTrigger | liveViewPayload.operation | liveViewManager.startLiveView对应云侧operation值为0。  liveViewManager.updateLiveView对应云侧operation值为1。  liveViewManager.stopLiveView对应云侧operation值为2。  liveViewManager.startLiveViewByTrigger对应云侧operation值为4。  liveViewManager.stopLiveViewByTrigger对应云侧operation值为6。 |
| liveView | payload | NA |
| liveView.id | payload.activityId | NA |
| liveView.event | payload.event | 在创建实况窗时，云侧API仅支持FLIGHT、TAXI、TRAIN、DELIVERY、QUEUE、RENT、EXPRESS、CHECK\_IN、TRADE、SUBSCRIBE\_TIMER场景。 |
| liveView.subEvent | payload.subEvent | NA |
| NA | payload.status | 端侧API不支持实况活动状态字段。 |
| liveView.sequence | payload.version | NA |
| liveView.isMute | payload.mute | NA |
| liveView.lifeCycleMode | NA | 云侧API不支持实况窗生命周期模式字段。 |
| liveView.shareUrl | payload.shareUrl | NA |
| liveView.timer | NA | 云侧API不支持实况窗卡片计时器字段。 |
| liveView.timer.time | NA | NA |
| liveView.timer.isCountdown | NA | NA |
| liveView.timer.isPaused | NA | NA |
| liveView.timer.countdownPreset | NA | NA |
| liveView.timer.capsuleCountdownPreset | NA | NA |
| liveView.timer.countdownPreset.presetTitle | NA | NA |
| liveView.timer.countdownPreset.presetContent | NA | NA |
| liveView.liveViewData | payload.activityData | NA |
| liveView.liveViewData.primary | payload.activityData.notificationData | NA |
| NA | payload.activityData.notificationData.keywords | 端侧不支持实况窗关键词字段。 |
| liveView.liveViewData.primary.title | payload.activityData.notificationData.contentTitle | NA |
| liveView.liveViewData.primary.content | payload.activityData.notificationData.contentText | NA |
| liveView.liveViewData.primary.keepTime | payload.activityData.notificationData.keepTime | NA |
| liveView.liveViewData.primary.clickAction | payload.activityData.notificationData.clickAction | NA |
| liveView.liveViewData.primary.liveViewLockScreenPicture | payload.activityData.notificationData.lockScreen.picture | NA |
| liveView.liveViewData.primary.liveViewLockScreenAbilityName | payload.activityData.notificationData.lockScreen.abilityName | NA |
| liveView.liveViewData.primary.liveViewLockScreenAbilityParameters | NA | 云侧不支持锁屏沉浸实况窗扩展Ability参数字段。 |
| liveView.liveViewData.primary.backgroundType | payload.activityData.notificationData.backgroundType | 端侧backgroundType枚举SYS\_BACKGROUND\_UNDEFINED，对应云侧backgroundType值为0。  端侧backgroundType枚举SYS\_BACKGROUND\_FLIGHT\_MOON，对应云侧backgroundType值为100。  端侧backgroundType枚举SYS\_BACKGROUND\_FLIGHT\_SUNSET，对应云侧backgroundType值为101。 |
| liveView.liveViewData.primary.aliveTime | NA | 云侧不支持实况窗存活时间的字段。 |
| liveView.liveViewData.primary.extensionData | payload.activityData.notificationData.extend | NA |
| liveView.liveViewData.primary.extensionData.type | payload.activityData.notificationData.extend.type | 端侧type枚举EXTENSION\_TYPE\_DEFAULT，对应云侧type值为0。  端侧type枚举EXTENSION\_TYPE\_COMMON\_TEXT，对应云侧type值为1。  端侧type枚举EXTENSION\_TYPE\_CAPSULE\_TEXT，对应云侧type值为2。  端侧type枚举EXTENSION\_TYPE\_PIC，对应云侧type值为3。  端侧type枚举EXTENSION\_TYPE\_ICON，对应云侧type值为4。  端侧type枚举EXTENSION\_TYPE\_PROGRESS，云侧API不支持此枚举值。 |
| liveView.liveViewData.primary.extensionData.text | payload.activityData.notificationData.extend.text | NA |
| liveView.liveViewData.primary.extensionData.pic | payload.activityData.notificationData.extend.image | 云侧仅支持传入图片路径。 |
| NA | payload.activityData.notificationData.extend.imageUrl | 端侧不支持辅助区图片URL链接字段。  **说明：**  若应用需要通过端侧实现在实况窗辅助区上展示网络图片，可自行下载网络图片到本地，将其转换为PixelMap对象，通过[extensionData](liveview-liveviewmanager.md#extensiondata).pic字段传入。 |
| liveView.liveViewData.primary.extensionData.clickAction | payload.activityData.notificationData.extend.clickAction | NA |
| liveView.liveViewData.primary.extensionData.progress | NA | 云侧API不支持进度百分比。 |
| liveView.liveViewData.primary.layoutData | NA | 云侧不支持实况窗卡片扩展区结构体字段，相关API字段在结构体notificationData中体现。 |
| liveView.liveViewData.primary.layoutData.layoutType | payload.activityData.notificationData.type | 端侧layoutType枚举LAYOUT\_TYPE\_DEFAULT，对应云侧type值为-1。  端侧layoutType枚举LAYOUT\_TYPE\_PROGRESS，对应云侧type值为3。  端侧layoutType枚举LAYOUT\_TYPE\_PICKUP，对应云侧type值为4。  端侧layoutType枚举LAYOUT\_TYPE\_FLIGHT，对应云侧type值为5。  端侧layoutType枚举LAYOUT\_TYPE\_SCORE，对应云侧type值为7。  端侧layoutType枚举LAYOUT\_TYPE\_NAVIGATION，云侧API不支持此枚举值。  端侧layoutType枚举LAYOUT\_TYPE\_CUSTOM，对应云侧type值为100。 |
| liveView.liveViewData.primary.layoutData.serviceButtons | NA | 云侧不支持连续服务按钮字段。 |
| liveView.liveViewData.primary.layoutData.isServiceButtonsDisplayed | NA | 云侧不支持连续服务按钮是否显示字段。 |
| liveView.liveViewData.primary.layoutData.serviceButton.name | NA | NA |
| liveView.liveViewData.primary.layoutData.serviceButton.clickAction | NA | NA |
| liveView.liveViewData.primary.layoutData.weatherInfo | payload.activityData.notificationData.weather | NA |
| liveView.liveViewData.primary.layoutData.weatherInfo.weatherType | payload.activityData.notificationData.weather.weatherType | 端侧传入参数值为[WeatherType](liveview-liveviewmanager.md#weathertype)枚举，云侧传入参数值为[WeatherType](liveview-liveviewmanager.md#weathertype)枚举值。 |
| liveView.liveViewData.primary.layoutData.weatherInfo.locationType | payload.activityData.notificationData.weather.locationType | 端侧传入参数值为[WeatherLocationType](liveview-liveviewmanager.md#weatherlocationtype)枚举，云侧传入参数值为[WeatherLocationType](liveview-liveviewmanager.md#weatherlocationtype)枚举值。 |
| liveView.liveViewData.primary.layoutData.weatherInfo.highTemperature | payload.activityData.notificationData.weather.highTemperature | NA |
| liveView.liveViewData.primary.layoutData.weatherInfo.lowTemperature | payload.activityData.notificationData.weather.lowTemperature | NA |
| liveView.liveViewData.primary.progressLayout.progress | payload.activityData.notificationData.richProgress.progress | NA |
| liveView.liveViewData.primary.progressLayout.color | payload.activityData.notificationData.richProgress.color | NA |
| liveView.liveViewData.primary.progressLayout.backgroundColor | payload.activityData.notificationData.richProgress.bgColor | NA |
| liveView.liveViewData.primary.progressLayout.indicatorType | payload.activityData.notificationData.richProgress.indicatorType | NA |
| liveView.liveViewData.primary.progressLayout.indicatorIcon | payload.activityData.notificationData.richProgress.indicatorIcon | NA |
| liveView.liveViewData.primary.progressLayout.lineType | payload.activityData.notificationData.richProgress.type | NA |
| liveView.liveViewData.primary.progressLayout.nodeIcons | payload.activityData.notificationData.richProgress.nodeIcons | NA |
| liveView.liveViewData.primary.pickupLayout.title | payload.activityData.notificationData.singleTextBlock.firstLine | NA |
| liveView.liveViewData.primary.pickupLayout.content | payload.activityData.notificationData.singleTextBlock.secondLine | NA |
| liveView.liveViewData.primary.pickupLayout.underlineColor | payload.activityData.notificationData.singleTextBlock.underlineColor | NA |
| liveView.liveViewData.primary.pickupLayout.descPic | payload.activityData.notificationData.descPic | NA |
| NA | payload.activityData.notificationData.descPicUrl | 端侧不支持强调文本模板扩展区域描述图片URL链接字段。  **说明：**  若应用需要通过端侧实现在实况窗扩展区域描述图片上展示网络图片，可自行下载网络图片，将其转换为PixelMap对象，通过[pickupLayout](liveview-liveviewmanager.md#pickuplayout).descPic字段传入。 |
| liveView.liveViewData.primary.flightLayout.style | payload.activityData.notificationData.style | NA |
| liveView.liveViewData.primary.flightLayout.firstTitle | payload.activityData.notificationData.firstTextBlock.firstLine | NA |
| liveView.liveViewData.primary.flightLayout.firstContent | payload.activityData.notificationData.firstTextBlock.secondLine | NA |
| liveView.liveViewData.primary.flightLayout.lastTitle | payload.activityData.notificationData.lastTextBlock.firstLine | NA |
| liveView.liveViewData.primary.flightLayout.lastContent | payload.activityData.notificationData.lastTextBlock.secondLine | NA |
| liveView.liveViewData.primary.flightLayout.lastTitleSuperscript | payload.activityData.notificationData.lastTextBlock.firstLineSuperscript | NA |
| liveView.liveViewData.primary.flightLayout.lastContentSuperscript | payload.activityData.notificationData.lastTextBlock.secondLineSuperscript | NA |
| liveView.liveViewData.primary.flightLayout.spaceType | payload.activityData.notificationData.spaceType | NA |
| liveView.liveViewData.primary.flightLayout.spaceIcon | payload.activityData.notificationData.spaceIcon | NA |
| NA | payload.activityData.notificationData.spaceIconUrl | 端侧不支持左右文本模板间隔图标URL链接字段。  **说明：**  若应用需要通过端侧实现在实况窗左右文本模板间隔图标上展示网络图片，可自行下载网络图片，将其转换为PixelMap对象，通过[flightLayout](liveview-liveviewmanager.md#flightlayout).spaceIcon字段传入。 |
| liveView.liveViewData.primary.flightLayout.spaceText | payload.activityData.notificationData.spaceText | NA |
| liveView.liveViewData.primary.flightLayout.isHorizontalLineDisplayed | payload.activityData.notificationData.displayHorizontalLine | NA |
| liveView.liveViewData.primary.flightLayout.additionalText | payload.activityData.notificationData.additionalText | NA |
| liveView.liveViewData.primary.scoreLayout.hostName | payload.activityData.notificationData.game.host.name | NA |
| liveView.liveViewData.primary.scoreLayout.hostIcon | payload.activityData.notificationData.game.host.icon | NA |
| NA | payload.activityData.notificationData.game.host.iconUrl | 端侧不支持赛事比分模板展示区队伍图标URL链接字段。  **说明：**  若应用需要通过端侧实现在实况窗赛事比分模板主队展示区队伍图标上展示网络图片，可自行下载网络图片，将其转换为PixelMap对象，通过[scoreLayout](liveview-liveviewmanager.md#scorelayout).hostIcon字段传入。 |
| liveView.liveViewData.primary.scoreLayout.hostScore | payload.activityData.notificationData.game.host.score | NA |
| liveView.liveViewData.primary.scoreLayout.guestName | payload.activityData.notificationData.game.guest.name | NA |
| liveView.liveViewData.primary.scoreLayout.guestIcon | payload.activityData.notificationData.game.guest.icon | NA |
| NA | payload.activityData.notificationData.game.guest.iconUrl | 端侧不支持赛事比分模板展示区队伍图标URL链接字段。  **说明：**  若应用需要通过端侧实现在实况窗赛事比分模板客队展示区队伍图标上展示网络图片，可自行下载网络图片，将其转换为PixelMap对象，通过[scoreLayout](liveview-liveviewmanager.md#scorelayout).guestIcon字段传入。 |
| liveView.liveViewData.primary.scoreLayout.guestScore | payload.activityData.notificationData.game.guest.score | NA |
| liveView.liveViewData.primary.scoreLayout.competitionDesc | payload.activityData.notificationData.game.competition.desc|richDesc | NA |
| liveView.liveViewData.primary.scoreLayout.competitionTime | payload.activityData.notificationData.game.competition.time | NA |
| liveView.liveViewData.primary.scoreLayout.isHorizontalLineDisplayed | payload.activityData.notificationData.displayHorizontalLine | NA |
| liveView.liveViewData.primary.navigationLayout.currentNavigationIcon | NA | 云侧不支持实况窗导航模板。 |
| liveView.liveViewData.primary.navigationLayout.navigationIcons | NA | NA |
| liveView.liveViewData.primary.navigationLayout.isNavigationIconsDisplayed | NA | NA |
| liveView.liveViewData.primary.customLayout.abilityName | payload.activityData.notificationData.customLayout.abilityName | NA |
| liveView.liveViewData.primary.customLayout.abilityParameters | payload.activityData.notificationData.customLayout.abilityParameters | NA |
| liveView.liveViewData.capsule | payload.activityData.capsuleData | NA |
| liveView.liveViewData.capsule.type | payload.activityData.capsuleData.type | 端侧type枚举CAPSULE\_TYPE\_TEXT，对应云侧type值为1。  端侧type枚举CAPSULE\_TYPE\_TIMER，对应云侧type值为2。  端侧type枚举CAPSULE\_TYPE\_PROGRESS，对应云侧type值为3。 |
| liveView.liveViewData.capsule.status | payload.activityData.capsuleData.status | NA |
| liveView.liveViewData.capsule.icon | payload.activityData.capsuleData.icon | NA |
| NA | payload.activityData.capsuleData.iconUrl | 端侧不支持实况胶囊图标URL链接字段。  **说明：**  若应用需要通过端侧实现在实况胶囊图标上展示网络图片，可自行下载网络图片，将其转换为PixelMap对象，通过[capsule](liveview-liveviewmanager.md#capsuledata).icon字段传入。 |
| liveView.liveViewData.capsule.tailIcon | payload.activityData.capsuleData.tailIcon | NA |
| NA | payload.activityData.capsuleData.tailIconUrl | 端侧不支持实况胶囊尾部图标URL链接字段。  **说明：**  若应用需要通过端侧实现在实况胶囊尾部图标上展示网络图片，可自行下载网络图片，将其转换为PixelMap对象，通过[capsule](liveview-liveviewmanager.md#capsuledata).tailIcon字段传入。 |
| liveView.liveViewData.capsule.backgroundColor | payload.activityData.capsuleData.bgColor | NA |
| NA | payload.activityData.capsuleData.remind | 端侧不支持设置实况胶囊在状态栏的动态效果字段。 |
| liveView.liveViewData.capsule.isContentDisplayed | payload.activityData.capsuleData.isContentDisplayed | NA |
| liveView.liveViewData.capsule.isTailIconDisplayed | payload.activityData.capsuleData.isTailIconDisplayed | NA |
| liveView.liveViewData.textCapsule.title | payload.activityData.capsuleData.title | NA |
| liveView.liveViewData.textCapsule.content | payload.activityData.capsuleData.content | NA |
| liveView.liveViewData.timerCapsule.content | payload.activityData.capsuleData.content | NA |
| liveView.liveViewData.timerCapsule.time | payload.activityData.capsuleData.capsuleTimer.time | NA |
| liveView.liveViewData.timerCapsule.isCountdown | payload.activityData.capsuleData.capsuleTimer.countDown | NA |
| liveView.liveViewData.timerCapsule.isPause | payload.activityData.capsuleData.capsuleTimer.pause | NA |
| liveView.liveViewData.progressCapsule.max | payload.activityData.capsuleData.progress.max | NA |
| liveView.liveViewData.progressCapsule.progress | payload.activityData.capsuleData.progress.progress | NA |
| liveView.liveViewData.progressCapsule.indeterminate | payload.activityData.capsuleData.progress.indeterminate | NA |
| liveView.liveViewData.progressCapsule.content | payload.activityData.capsuleData.content | NA |
| liveView.liveViewData.external | payload.activityData.externalData | NA |
| liveView.liveViewData.externalData.title | payload.activityData.externalData.title | NA |
| liveView.liveViewData.externalData.content | payload.activityData.externalData.body | NA |
| liveView.liveViewData.externalData.type | payload.activityData.externalData.type | 端侧type枚举BACKGROUND\_COLOR，对应云侧type值0。  端侧type枚举BACKGROUND\_PICTURE，对应云侧type值1。 |
| liveView.liveViewData.externalData.backgroundColor | payload.activityData.externalData.bgColor | NA |
| liveView.liveViewData.externalData.backgroundPicture | payload.activityData.externalData.bgImage | NA |
| trigger | payload.trigger | NA |
| trigger.type | payload.trigger.type | NA |
| trigger.condition | payload.trigger.condition | NA |
| trigger.displayTime | payload.trigger.displayTime | NA |
| trigger.condition.longitude | payload.trigger.condition.longitude | NA |
| trigger.condition.latitude | payload.trigger.condition.latitude | NA |
| trigger.condition.coordinateSystemType | payload.trigger.condition.coordinateSystemType | NA |
| trigger.condition.radius | payload.trigger.condition.radius | NA |
| trigger.condition.monitorEvent | payload.trigger.condition.monitorEvent | NA |
| trigger.condition.delayTime | payload.trigger.condition.delayTime | NA |
| RichText.text | RichText.text | NA |
| RichText.textColor | RichText.foregroundColor | NA |
