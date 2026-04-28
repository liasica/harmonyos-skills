---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-avsession-avmusictemplate
title: 使用音频模板
breadcrumb: 指南 > 媒体 > AVSession Kit（音视频播控服务） > 音频模板 > 使用音频模板
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8a3eca337320563042efe87c387c9e801890cc4c257c5b5f4ff63de22c8ec37e
---

从API version 23开始，支持媒体应用通过音频模板接入播控中心（系统应用），实现音视频在播控中心进行统一的界面显示和播控管理，减少应用侧开发工作量。该文档介绍音频模板接口能力及开发基本流程，包括通过音模板接入播控中心、上报媒体相关信息（标题、作者、播放状态等）至播控中心、响应播控中心下发的操作（播放、暂停、搜索、收藏）指令等。

音频模板同时支持音频和视频内容，且两者的接入方式相同。本文档以音频场景为例进行说明。

说明

本功能仅支持在API version 23及以上版本的Car设备工程中使用。创建工程时，请在Device type中选择“Car”。

## 基本概念

音频模板（AVMusicTemplate）：用于描述音频模板相关能力的类，包含标识当前媒体会话的ID（sessionId）、会话标签（sessionTag）等属性，以及与播控中心进行数据交互的操作方法。媒体应用可通过音频模板向播控中心上报媒体相关信息，以及响应播控中心的操作指令。

## 接口说明

详细的API说明请参考[AVMusicTemplate](../harmonyos-references/arkts-apis-avmusictemplate-avmusictemplate.md)。

## 开发步骤

媒体应用接入音频模板的基本步骤如下所示：

1. 在进程启动时，调用接口[createAVMusicTemplate](../harmonyos-references/arkts-apis-avmusictemplate-f.md#avmusictemplatecreateavmusictemplate)创建音频模板实例（每个媒体应用创建一个音频模板实例，不需要重复创建）并拉起音频模板。

   以下示例代码仅展示创建AVMusicTemplate对象的接口调用，应用在真正使用时，需要参考接口[@ohos.backgroundTaskManager (后台任务管理)](../harmonyos-references/js-apis-backgroundtaskmanager.md)确保AVMusicTemplate对象实例在应用后台播放业务活动期间一直存在，避免被系统回收、释放，导致后台发声时被系统管控。

   ```
   1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { TemplateManager } from '../manager/TemplateManager';

   5. export default class EntryAbility extends UIAbility {
   6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   7. console.info('onCreate');
   8. TemplateManager.getInstance().createTemplate();
   9. }

   11. // ...
   12. onForeground(): void {
   13. console.info('onForeground');
   14. this.startTemplateControllerAbility();
   15. }

   17. private startTemplateControllerAbility() {
   18. let want: Want = {
   19. bundleName: 'com.example.templatecontroller',
   20. abilityName: 'EntryAbility',
   21. parameters: {
   22. bundleName: 'com.example.templateprovider'
   23. }
   24. }
   25. this.context.startAbility(want).then(() => {
   26. console.info('startTemplateControllerAbility: startAbility success');
   27. }).catch((e: BusinessError) => {
   28. console.error(`startTemplateControllerAbility: startAbility: errCode: ${e?.code}}`);
   29. });
   30. }
   31. }
   ```

   ```
   1. import { avMusicTemplate } from '@kit.AVSessionKit';
   2. // ...

   4. export class TemplateManager {
   5. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
   6. private static sInstance: TemplateManager;
   7. // ...
   8. private constructor() {
   9. }

   11. /**
   12. * 获取模板控制器实例。
   13. *
   14. * @returns 模板控制器实例。
   15. */
   16. public static getInstance(): TemplateManager {
   17. if (!TemplateManager.sInstance) {
   18. TemplateManager.sInstance = new TemplateManager();
   19. }
   20. return TemplateManager.sInstance;
   21. };

   23. /**
   24. * 创建音频模板。
   25. */
   26. public createTemplate() {
   27. if (this.template) {
   28. console.warn('createTemplate: template not undefined');
   29. return
   30. }
   31. try {
   32. this.template = avMusicTemplate.createAVMusicTemplate(avMusicTemplate.AVMusicTemplateType.DEFAULT);
   33. console.info('createTemplate: success');
   34. // ...
   35. } catch (e) {
   36. console.error(`createTemplate, errCode: ${e?.code}`);
   37. }
   38. }
   39. // ...
   40. }
   ```
2. 注册事件监听，在监听到事件后可提供应用数据给音频模板使用。监听接口详情请查看[AVMusicTemplate](../harmonyos-references/arkts-apis-avmusictemplate-avmusictemplate.md)。

   音频模板主界面显示需要同时注册如下两个接口：

   * [onQueryMainTabs](../harmonyos-references/arkts-apis-avmusictemplate-avmusictemplate.md#onquerymaintabs)：注册查询主标签事件监听。提供主界面展示的TAB数据集合，并规定“我的主页”的tabId为"minePage"。
   * [onQueryMediaTabContent](../harmonyos-references/arkts-apis-avmusictemplate-avmusictemplate.md#onquerymediatabcontent)：注册查询媒体标签内容事件监听。根据tabId提供页面展示内容数据。

   ```
   1. import { avMusicTemplate } from '@kit.AVSessionKit';
   2. // ...

   4. export class TemplateManager {
   5. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
   6. // ...
   7. private queryMainTabsEvent: avMusicTemplate.QueryMainTabsEvent = async () => {
   8. return new Promise<avMusicTemplate.MediaTab[]>(async (resolve, reject) => {
   9. try {
   10. let tabs: avMusicTemplate.MediaTab[] = await this.getMainTabs();
   11. resolve(tabs);
   12. } catch (e) {
   13. console.error(`queryMainTabsEvent fail, errCode: ${e?.code}`);
   14. reject(e);
   15. }
   16. });
   17. };
   18. private queryMediaTabContentEvent: avMusicTemplate.QueryMediaTabContentEvent = async (tabId: string) => {
   19. return new Promise<avMusicTemplate.MediaTabContent>(async (resolve, reject) => {
   20. try {
   21. let tabContent: avMusicTemplate.MediaTabContent = await this.createMediaTabContent();
   22. resolve(tabContent);
   23. } catch (e) {
   24. console.error(`queryMediaTabContentEvent fail, errCode: ${e?.code}`);
   25. reject(e);
   26. }
   27. });
   28. };
   29. // ...

   31. /**
   32. * 注册监听。
   33. */
   34. private registerListener() {
   35. this.template?.onQueryMainTabs(this.queryMainTabsEvent);
   36. this.template?.onQueryMediaTabContent(this.queryMediaTabContentEvent);
   37. // ...
   38. };

   40. // ...
   41. /**
   42. * 模拟获取主界面的所有TAB。
   43. *
   44. * @returns Promise类型MediaTab数组。
   45. */
   46. private async getMainTabs(): Promise<avMusicTemplate.MediaTab[]> {
   47. let homeTab: avMusicTemplate.MediaTab = {
   48. tabId: 'home',
   49. tabName: '首页'
   50. };
   51. let mineTab: avMusicTemplate.MediaTab = {
   52. tabId: 'mine',
   53. tabName: '我的'
   54. };
   55. let mainTabs: avMusicTemplate.MediaTab[] = [homeTab, mineTab];
   56. return mainTabs;
   57. };

   59. /**
   60. * 模拟获取TAB内容。
   61. *
   62. * @returns 标签页内容。
   63. */
   64. private async createMediaTabContent(): Promise<avMusicTemplate.MediaTabContent> {
   65. let compilation: avMusicTemplate.Compilation = await this.createCompilation();
   66. let mediaTabContent: avMusicTemplate.MediaTabContent = {
   67. errorCode: 0,
   68. tabId: 'tabId',
   69. compilations: [compilation]
   70. }
   71. return mediaTabContent;
   72. };

   74. /**
   75. * 模拟获取合集数据。
   76. *
   77. * @returns 合集。
   78. */
   79. private async createCompilation(): Promise<avMusicTemplate.Compilation> {
   80. let mediaEntity: avMusicTemplate.MediaEntity = await this.createMediaEntity();
   81. let compilation: avMusicTemplate.Compilation = {
   82. errorCode: 0,
   83. id: '',
   84. title: '',
   85. hasMoreData: false,
   86. totalSize: 1,
   87. memberMediaType: avMusicTemplate.EntityType.SINGLE,
   88. topElements: [mediaEntity],
   89. }
   90. return compilation;
   91. };

   93. /**
   94. * 模拟获取媒体数据。
   95. *
   96. * @returns 媒体数据。
   97. */
   98. private async createMediaEntity(): Promise<avMusicTemplate.MediaEntity> {
   99. let mediaEntity: avMusicTemplate.MediaEntity = {
   100. mediaId: 'mediaId',
   101. mediaType: avMusicTemplate.EntityType.SINGLE,
   102. parentId: 'parentId',
   103. parentMediaType: avMusicTemplate.EntityType.SINGLE,
   104. title: 'title',
   105. imageUrl: 'imageUrl',
   106. playState: avMusicTemplate.PlaybackState.PLAYBACK_STATE_PREPARE
   107. };
   108. return mediaEntity;
   109. };
   110. // ...
   111. }
   ```
3. 在音频模板无法直接感知的场景（登录，下载等），需要媒体应用主动向音频模板同步数据。同步接口详情请查看[AVMusicTemplate](../harmonyos-references/arkts-apis-avmusictemplate-avmusictemplate.md)。

   例如，扫码登录成功的场景。当用户在音频模板界面扫码登录时，由于登录状态只有媒体应用能感知，所以需要调用接口[setUserInfo](../harmonyos-references/arkts-apis-avmusictemplate-avmusictemplate.md#setuserinfo)给音频模板同步数据。

   ```
   1. import { avMusicTemplate } from '@kit.AVSessionKit';
   2. // ...

   4. export class TemplateManager {
   5. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
   6. // ...
   7. private isLogin: boolean = false;
   8. // ...

   10. /**
   11. * 模拟登录状态改变。
   12. *
   13. * @param isLogin 是否登录。
   14. */
   15. public setLoginState(isLogin: boolean) {
   16. this.isLogin = isLogin;
   17. this.setUserInfo();
   18. }

   20. /**
   21. * 用户信息发生变化后通知界面刷新用户信息，如登陆账号后。
   22. */
   23. public setUserInfo() {
   24. let userInfo: avMusicTemplate.UserInfo = {
   25. userInfoId: this.isLogin ? 'userInfoId' : '',
   26. nickName: this.isLogin ? '昵称' : '',
   27. profilePicUrl: this.isLogin ? 'profilePicUrl' : '',
   28. tips: this.isLogin ? 'tips' : '',
   29. isLogin: this.isLogin,
   30. isVip: false
   31. };
   32. this.template?.setUserInfo(userInfo);
   33. };
   34. // ...
   35. }
   ```
4. 媒体应用启动时注册的事件监听需要在应用退出时注销，以释放资源。注销接口详情请查看[AVMusicTemplate](../harmonyos-references/arkts-apis-avmusictemplate-avmusictemplate.md)。

   ```
   1. import { avMusicTemplate } from '@kit.AVSessionKit';
   2. // ...

   4. export class TemplateManager {
   5. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
   6. // ...
   7. /**
   8. * 注销监听。
   9. */
   10. public unregisterListener() {
   11. this.template?.offQueryMainTabs();
   12. this.template?.offQueryMediaTabContent();
   13. this.template?.offQueryMediaEntity();
   14. this.template?.offQueryCompilation();
   15. this.template?.offQueryPlaylist();
   16. this.template?.offQueryCurrentSingle();
   17. this.template?.offQueryCompilationByKeyword();
   18. this.template?.offQueryMediaEntityByKeyword();
   19. this.template?.offQueryRecommendMediaEntityList();
   20. this.template?.offQueryHotWords();
   21. this.template?.offQuerySearchHistory();
   22. this.template?.offClearSearchHistory();
   23. this.template?.offLogin();
   24. this.template?.offRequestDialogInfo();
   25. this.template?.offHandleMemberPurchase();
   26. this.template?.offQueryMemberPurchase();
   27. this.template?.offQueryCustomContent();
   28. this.template?.offDownloadMediaEntity();
   29. this.template?.offSettingsChange();
   30. this.template?.offProblemAndAdvice();
   31. this.template?.offPlayForSearch();
   32. this.template?.offExecuteAction();
   33. this.template?.offPlayMediaEntity();
   34. this.template?.offFavoriteMediaEntity();
   35. this.template?.destroy();
   36. this.template = undefined;
   37. };
   38. // ...
   39. }
   ```
