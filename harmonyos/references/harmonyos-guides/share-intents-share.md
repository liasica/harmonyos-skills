---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-intents-share
title: 共享联系人信息到分享推荐区
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 目标应用处理分享内容 > 共享联系人信息到分享推荐区
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c0f8130a6634dbabb5bfed6014744918a4692d2b391281d07a29f6f96a0a7cf8
---

通过意图框架服务，目标应用可以将联系人信息共享到分享推荐区。参考：[习惯推荐-接入方案](intents-habit-rec-access-programme.md)。

说明

该示例代码无法直接运行，需要申请意图框架白名单。参见：[Intents Kit接入流程](intents-access-flow.md)。

## 开发步骤

1. 导入相关模块。

   ```
   1. import BuildProfile from 'BuildProfile';
   2. import { util } from '@kit.ArkTS';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { insightIntent } from '@kit.IntentsKit';
   ```
2. 目标应用构造联系人数据。

   ```
   1. const intent: insightIntent.InsightIntent = {
   2. intentName: 'SendMessage', // 意图名
   3. intentVersion: '1.0', // 意图版本
   4. identifier: util.generateRandomUUID(), // 意图标识符
   5. intentActionInfo: { // 意图执行信息
   6. actionMode: 'EXECUTED', // 动作模式
   7. executedTimeSlots: { // 实际发生时间段
   8. executedStartTime: new Date().getTime(),
   9. executedEndTime: new Date().getTime(),
   10. }
   11. },
   12. intentEntityInfo: { // 意图实体信息
   13. entityId: 'this-is-id', // 实体Id
   14. entityName: 'Contact', // 实体名称
   15. name: 'Nickname', // 联系人昵称
   16. icon: 'data:image/png;base64,...', // 联系人头像
   17. phoneNumbers: [], // 联系人电话号码
   18. extras: {
   19. shareParams: {
   20. bundleName: BuildProfile.BUNDLE_NAME, // 应用包名
   21. moduleName: 'entry', // 应用模块名 根据实际填写
   22. abilityName: 'SampleContactAbility', // 应用ability名 根据实际填写
   23. action: 'ohos.want.action.sendData', // 标识分享 不可修改
   24. }
   25. }
   26. }
   27. };
   ```
3. 目标应用共享联系人数据。

   ```
   1. let uiContext: UIContext = this.getUIContext();
   2. let context: Context = uiContext.getHostContext() as Context;
   3. insightIntent.shareIntent(context, [intent]).then(() => {
   4. console.info('shareIntent ok');
   5. }).catch((err: BusinessError) => {
   6. console.error(`shareIntent failed. Code: ${err.code}. message: ${err.message}`);
   7. });
   ```
