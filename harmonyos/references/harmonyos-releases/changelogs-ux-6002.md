---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-ux-6002
title: UX样式或效果的变更
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > OS平台行为变更说明 > 6.0.0(20) Beta2引入的行为变更 > UX样式或效果的变更
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:06+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:9a04fbf50695edb25df8556ad5dd6a2a9278bfcf9da0323a4476d1a1b82fa0cb
---

## selectDynamicIcon接口新增错误码

**变更原因**

开发者可以通过selectDynamicIcon接口切换应用图标为自定义图标，但是用户设置了主题且主题对该应用有在线图标时，会存在自定义图标与主题风格不一致的体验。

**变更影响**

此变更涉及应用适配。

变更前selectDynamicIcon有如下错误码：

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006800009 | System internal error. |
| 1006800011 | Select dynamic icon failed. |

变更后：

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006800009 | System internal error. |
| 1006800011 | Select dynamic icon failed. |
| 1006800013 | Failed to switch to the custom icon because a custom theme icon is currently in use. |

**起始API Level**

6.0.0(20)

**变更的接口/组件**

AppGalleryKit提供的selectDynamicIcon接口

**适配指导**

如果应用调用appInfoManager.selectDynamicIcon接口是由用户触发，可以在catch中判断错误码是否是1006800013。如果是1006800013则根据自身业务场景，选择合适的UI样式提醒用户：当前应用存在主题在线图标，所以设置自定义图标失败。需要先在“设置 -> 桌面与个性化”，或“主题 -> 官方主题”，切换至官方主题后，再尝试重新设置图标。

```
1. import { appInfoManager } from "@kit.AppGalleryKit";
2. import { BusinessError } from "@kit.BasicServicesKit";
3. import { hilog } from "@kit.PerformanceAnalysisKit";
4. import promptAction from '@ohos.promptAction';

6. export class DynamicIcon {
7. private readonly SHORT_TOAST_DURATION: number = 2000;

9. private selectDynamicIcon(iconId: string) {
10. appInfoManager.selectDynamicIcon(iconId).then(() => {
11. this.showToast('图标设置成功');
12. }).catch((error: BusinessError) => {
13. if (error?.code === 1006800013) {
14. this.showToast('图标暂时未生效，当前应用存在主题在线图标，请先切换至官方主题后再尝试设置图标');
15. } else {
16. hilog.error(0, 'DynamicIcon',
17. `selectDynamicIcon failed, code: ${error.code}, exception message: ${error.message}`);
18. }
19. });
20. }

22. private showToast(toastMessage: string): void {
23. promptAction.openToast({
24. message: toastMessage,
25. duration: this.SHORT_TOAST_DURATION
26. });
27. }
28. }
```
