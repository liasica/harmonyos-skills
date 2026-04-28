---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-lock-screen-ability
title: LiveViewLockScreenExtensionAbility
breadcrumb: API参考 > 应用服务 > Live View Kit（实况窗服务） > ArkTS API > LiveViewLockScreenExtensionAbility
category: harmonyos-references
scraped_at: 2026-04-28T08:17:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d051522e13a9e33885eae412d3bc761f47261dfe8665083d50d75e63908c534e
---

LiveViewLockScreenExtensionAbility为锁屏沉浸实况窗扩展Ability，继承自[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)。有如下约束：

* LiveViewLockScreenExtensionAbility为独立子进程，不能跨进程拉起其他Ability。
* 不允许调用通知API、窗口API、卡片API、后台任务API、联系人API、分布式数据管理API、相机API、NFC API、上传下载API、蜂窝通信API。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { LiveViewLockScreenExtensionAbility } from '@kit.LiveViewKit';
```

**设备行为差异：** 该模块在Phone、Tablet中可正常调用，在其他设备类型中无效果。

## 属性

PhonePC/2in1Tablet

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [LiveViewLockScreenExtensionContext](liveview-lock-screen-context.md) | 否 | 否 | LiveViewLockScreenExtensionAbility的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。 |

**示例：**

```
1. import { LiveViewLockScreenExtensionAbility } from '@kit.LiveViewKit';
2. import { UIExtensionContentSession, Want } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. export default class LiveViewLockScreenExtAbility extends LiveViewLockScreenExtensionAbility {
6. onCreate(): void {
7. hilog.info(0x0000, 'LiveViewLockScreenTag', 'LiveViewLockScreenExtAbility onCreate begin.');
8. }

10. onSessionCreate(want: Want, session: UIExtensionContentSession): void {
11. hilog.info(0x0000, 'LiveViewLockScreenTag', 'LiveViewLockScreenExtAbility onSessionCreate begin.');
12. let param: Record<string, UIExtensionContentSession> = {
13. 'session': session
14. };
15. let storage: LocalStorage = new LocalStorage(param);

17. // 解析从liveViewLocalScreenAbilityParameters中传入的参数
18. const parameters = want?.parameters;
19. let words: string = parameters?.['words'] ? parameters?.['words'] as string : 'Hello World!';
20. storage.setOrCreate('words', words);

22. // 加载锁屏沉浸实况窗页面
23. session.loadContent('pages/LiveViewLockScreenPage', storage);
24. }
25. }
```
