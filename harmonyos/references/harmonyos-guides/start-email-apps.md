---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-email-apps
title: 拉起邮件类应用（startAbilityByType）
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > 应用间跳转 > 拉起指定类型的应用 > 拉起邮件类应用（startAbilityByType）
category: harmonyos-guides
scraped_at: 2026-04-29T13:25:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f350d072bed93dd4f41629c0fcbf68f64346f77492143ee3f3f809ba6a8ea1d9
---

本章节介绍如何拉起邮件类应用扩展面板。

说明

如果拉起方的参数为mailto协议字符串，可以[使用mailto方式拉起邮件应用](start-email-apps-by-mailto.md)。邮件应用会解析收到的mailto协议字符串，并填充发件人、收件人、邮件内容等信息。

## 邮件类应用扩展面板参数说明

startAbilityByType接口中type字段为mail，对应的wantParam参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| email | string[ ] | 否 | 收件人邮箱地址（支持多个且以逗号分隔）。 |
| cc | string[ ] | 否 | 抄送人邮箱地址（支持多个且以逗号分隔）。 |
| bcc | string[ ] | 否 | 密送人邮箱地址（支持多个且以逗号分隔）。 |
| subject | string | 否 | 邮件主题。 |
| body | string | 否 | 邮件内容。 |
| ability.params.stream | string[ ] | 否 | 邮件附件（附件的uri地址列表）。 |
| ability.want.params.uriPermissionFlag | [wantConstant.Flags](../harmonyos-references/js-apis-app-ability-wantconstant.md#flags) | 否 | 给邮件附件赋予至少读权限。邮件附件参数存在时，该参数也必须要传。 |
| sceneType | number | 否 | 意图场景，表明本次请求对应的操作意图。1：发邮件。默认为1。 |

说明

* 邮件类应用扩展面板中的类型为string的参数，都要经过encodeURI编码。
* 邮件类应用扩展面板中的类型为string[]的参数，数组中的元素都要经过encodeURI编码。

## 拉起方开发步骤

1. 导入相关模块。

   ```
   1. import { common, wantConstant } from '@kit.AbilityKit';
   ```
2. 构造接口参数并调用startAbilityByType接口。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. @State hideAbility: string = 'hideAbility'

   6. build() {
   7. Row() {
   8. Column() {
   9. Text(this.hideAbility)
   10. .fontSize(30)
   11. .fontWeight(FontWeight.Bold)
   12. .onClick(() => {
   13. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   14. let wantParam: Record<string, Object> = {
   15. 'sceneType': 1,
   16. 'email': [encodeURI('xxx@example.com'), encodeURI('xxx@example.com')], // 收件人邮箱地址，多值以逗号分隔，对数组内容使用encodeURI()方法进行url编码
   17. 'cc': [encodeURI('xxx@example.com'), encodeURI('xxx@example.com')], // 抄送人邮箱地址，多值以逗号分隔，对数组内容使用encodeURI()方法进行url编码
   18. 'bcc': [encodeURI('xxx@example.com'), encodeURI('xxx@example.com')], // 密送人邮箱地址，多值以逗号分隔，对数组内容使用encodeURI()方法进行url编码
   19. 'subject': encodeURI('邮件主题'), // 邮件主题，对内容使用encodeURI()方法进行url编码
   20. 'body': encodeURI('邮件正文'), // 邮件正文，对内容使用encodeURI()方法进行url编码
   21. 'ability.params.stream': [encodeURI('附件uri1'), encodeURI('附件uri2')], // 附件uri，多值以逗号分隔，对数组内容使用encodeURI()方法进行url编码
   22. 'ability.want.params.uriPermissionFlag': wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION
   23. };
   24. let abilityStartCallback: common.AbilityStartCallback = {
   25. onError: (code: number, name: string, message: string) => {
   26. console.error(`onError code ${code} name: ${name} message: ${message}`);
   27. },
   28. onResult: (result) => {
   29. console.info(`onResult result: ${JSON.stringify(result)}`);
   30. }
   31. }

   33. context.startAbilityByType("mail", wantParam, abilityStartCallback,
   34. (err) => {
   35. if (err) {
   36. console.error(`startAbilityByType fail, err: ${JSON.stringify(err)}`);
   37. } else {
   38. console.info(`success`);
   39. }
   40. });
   41. });
   42. }
   43. .width('100%')
   44. }
   45. .height('100%')
   46. }
   47. }
   ```

   效果示例图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/CCkymBI-QX6g4uMEjLF8uQ/zh-cn_image_0000002589323865.png?HW-CC-KV=V1&HW-CC-Date=20260429T052552Z&HW-CC-Expire=86400&HW-CC-Sign=D58DA3694EA374346C418130FED07321370C527CD6D0A0C90AB0979D21B14B6E)

## 目标方开发步骤

1. 在module.json5中新增[linkFeature](module-configuration-file.md#skills标签)属性并设置声明当前应用支持的特性功能，从而系统可以从设备已安装应用中找到当前支持该特性的应用，取值范围如下：

   | 取值 | 含义 |
   | --- | --- |
   | ComposeMail | 声明应用支持撰写邮件功能 |

   ```
   1. {
   2. "abilities": [
   3. {
   4. "skills": [
   5. {
   6. "uris": [
   7. {
   8. "scheme": "mailto", // 这里仅示意，应用需确保这里声明的uri能被外部正常拉起
   9. "host": "",
   10. "path": "",
   11. "linkFeature": "ComposeMail" // 声明应用支持撰写邮件功能
   12. }
   13. ]
   14. }
   15. ]
   16. }
   17. ]
   18. }
   ```
2. 解析面板传过来的参数并做对应处理。

   ```
   1. UIAbility.onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void
   ```

   在参数**want.parameters**中会携带Caller方传入的参数（与调用方传入的有些差异），如下表所示：

   | 参数名 | 类型 | 必填 | 说明 |
   | --- | --- | --- | --- |
   | email | string[ ] | 否 | 收件人邮箱地址（支持多个且以逗号分隔）。 |
   | cc | string[ ] | 否 | 抄送人邮箱地址（支持多个且以逗号分隔）。 |
   | bcc | string[ ] | 否 | 密送人邮箱地址（支持多个且以逗号分隔）。 |
   | subject | string | 否 | 邮件主题。 |
   | body | string | 否 | 邮件内容。 |
   | stream | string[ ] | 否 | 邮件附件列表（附件的uri地址列表）。 |

   说明

   * 目标方接收的类型为string的参数，都要经过decodeURI解码。
   * 目标方接收的类型为string[]的参数，数组中的元素都要经过decodeURI解码。

**完整示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { window } from '@kit.ArkUI';

5. const TAG = 'MailTarget1.EntryAbility'

7. export default class EntryAbility extends UIAbility {
8. windowStage: window.WindowStage | null = null;

10. email: string[] | undefined;
11. cc: string[] | undefined;
12. bcc: string[] | undefined;
13. subject: string | undefined;
14. body: string | undefined;
15. stream: string[] | undefined;

17. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
18. hilog.info(0x0000, TAG, `onCreate, want=${JSON.stringify(want)}`);
19. super.onCreate(want, launchParam);
20. this.parseWant(want);
21. }

23. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
24. hilog.info(0x0000, TAG, `onNewWant, want=${JSON.stringify(want)}`);
25. super.onNewWant(want, launchParam);
26. this.parseWant(want);
27. if (!this.windowStage) {
28. hilog.error(0x0000, TAG, 'windowStage is null');
29. this.context.terminateSelf();
30. return;
31. }
32. this.loadPage(this.windowStage);
33. }

35. private parseWant(want: Want): void {
36. this.email = this.decodeStringArr(want.parameters?.email as string[]);
37. this.cc = this.decodeStringArr(want.parameters?.cc as string[]);
38. this.bcc = this.decodeStringArr(want.parameters?.bcc as string[]);
39. this.subject = decodeURI(want.parameters?.subject as string);// 使用decodeURI()方法对邮件主题进行url解码，其他字段处理方法相同
40. this.body = decodeURI(want.parameters?.body as string);// 使用decodeURI()方法对邮件内容进行url解码，其他字段处理方法相同
41. this.stream = this.decodeStringArr(want.parameters?.stream as string[]);
42. }

44. // 使用decodeURI()方法对string数组内容进行解码
45. private decodeStringArr(source: string[] | undefined): string[] {
46. let target: string[] = [];
47. source?.forEach(e => {
48. target.push(decodeURI(e));
49. })
50. return target;
51. }

53. private loadPage(windowStage: window.WindowStage): void {
54. const storage: LocalStorage = new LocalStorage({
55. "email": this.email,
56. "cc": this.cc,
57. "bcc": this.bcc,
58. "subject": this.subject,
59. "body": this.body,
60. "stream": this.stream
61. } as Record<string, Object>);

63. windowStage.loadContent('pages/ComposeMailPage', storage);

65. }

67. onDestroy(): void {
68. hilog.info(0x0000, TAG, `onDestroy`);
69. }

71. onWindowStageCreate(windowStage: window.WindowStage): void {
72. hilog.info(0x0000, TAG, `onWindowStageCreate`);
73. this.windowStage = windowStage;
74. this.loadPage(this.windowStage);
75. }

77. onWindowStageDestroy(): void {
78. hilog.info(0x0000, TAG, `onWindowStageDestroy`);
79. }

81. onForeground(): void {
82. hilog.info(0x0000, TAG, `onForeground`);
83. }

85. onBackground(): void {
86. hilog.info(0x0000, TAG, `onBackground`);
87. }
88. }
```
