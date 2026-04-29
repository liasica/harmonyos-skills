---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/obtaining-target-app-url-info
title: 获取目标应用的URL信息
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > 应用间跳转 > 拉起指定应用 > 获取目标应用的URL信息
category: harmonyos-guides
scraped_at: 2026-04-29T13:25:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1ac6873c6ab2d73df0f3ea499dc7ee3d559b6370df99d299216f82e18a792199
---

## 场景介绍

开发者在使用[UIAbilityContext.openLink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口拉起目标应用时，需要传入目标应用的URL信息。本章节主要介绍如何获取目标应用的URL信息。

假设目标应用的UIAbility的[module.json5](module-configuration-file.md)配置信息如下：

```
1. {
2. "name": "EntryAbility",
3. "srcEntry": "./ets/entryability/EntryAbility.ets",
4. "icon": "$media:layered_image",
5. "label": "$string:EntryAbility_label",
6. // ···
7. "skills": [
8. {
9. "uris": [
10. {
11. "scheme": "appurl",
12. "host": "www.example.com",
13. "path": "path1"
14. // ...
15. }
16. ],
17. "domainVerify": false,
18. }
19. // ...
20. ]
21. }
```

## 环境要求

开发者需要先获取[hdc工具](hdc.md)。

## 操作步骤

1. 使用[bm工具](bm-tool.md)获取目标应用的bundleName。

   1. 获取当前设备上所有已安装应用的bundleName，保存结果。

      ```
      1. hdc shell bm dump -a
      ```
   2. 安装目标应用。
   3. 再次获取当前设备上所有已安装应用的bundleName，并与之前保存的结果进行对比。

      新增的bundleName即为目标应用包名，本例中假设为com.example.myapplication。
2. 根据bundleName获取目标应用的Mission ID。

   1. 使用[aa工具](aa-tool.md)，获取目标应用的abilityName。

      ```
      1. hdc shell "aa dump -l | grep com.examplmyapplication"
      ```
   2. 通过查看输出中的Mission ID部分，获取abilityName即为EntryAbility。

      ```
      1. # 执行结果
      2. Mission ID #48  mission name #[#com.example.myapplication:entry:EntryAbility] lockedStat#0 mission affinity #[]
      3. app name [com.example.myapplication]
      4. bundle name [com.example.myapplication]
      ```
3. 根据bundleName获取应用的uris信息。

   1. 使用bm工具，获取应用的完整配置信息，包括abilities、skills、uris等配置。

      ```
      1. hdc shell bm dump -n com.example.myapplication
      ```
   2. 通过查看输出中name为的EntryAbility下方的skills部分，获取应用支持的URL Scheme配置。

      ```
      1. // 输出示例（skills部分）：
      2. // ...
      3. "name": "EntryAbility",
      4. // ...
      5. {
      6. "skills": [
      7. {
      8. "actions": [
      9. "ohos.want.action.viewData"
      10. ],
      11. "domainVerify": false,
      12. "entities": [
      13. "entity.system.browsable"
      14. ],
      15. "permissions": [],
      16. "uris": [
      17. {
      18. "host": "www.example.com",
      19. "linkFeature": "",
      20. "maxFileSupported": 0,
      21. "path": "path1",
      22. "pathRegex": "",
      23. "pathStartWith": "",
      24. "port": "",
      25. "scheme": "appurl",
      26. "type": "",
      27. "utd": ""
      28. }
      29. ]
      30. }
      31. ]
      32. }
      ```
4. 根据获取到的配置信息拼接生成URL信息。

   URL格式如下：

   ```
   1. scheme://host:port/path
   ```

   以目标应用为例，其URL构成如下：

   | 配置项 | 值 |
   | --- | --- |
   | scheme | appurl |
   | host | www.example.com |
   | port | 未指定（可选） |
   | path | path1 |

   根据上述参数，拼接得到的完整URL为：

   ```
   1. appurl://www.example.com/path1
   ```

   说明

   * 不同应用的bundleName和URL配置可能因版本不同而有所变化。
   * 建议在实际使用前，通过hdc命令确认目标应用的最新配置信息。
   * 如果应用未配置skills中的uris字段，则不支持通过Deep Linking方式拉起。
5. 使用Deep Linking方式拉起目标应用。

   以下为通过[UIAbilityContext.openLink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口拉起目标应用的完整示例。

   说明

   * URL配置验证：在使用目标应用的URL之前，务必验证其正确性，避免因URL错误导致拉起失败。
   * 应用安装检测：在拉起目标应用前，建议先检测应用是否已安装。

   ```
   1. import { common } from '@kit.AbilityKit'
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. @Entry
   6. @Component
   7. struct SpecifiedPage {

   9. build() {
   10. Row() {
   11. Column() {
   12. Button("拉起目标应用")
   13. .onClick(() => {
   14. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   15. let link: string = 'appurl://www.example.com/path1';

   17. context.openLink(link, { appLinkingOnly: false })
   18. .then(() => {
   19. hilog.info(0x0000, 'testTag', `Succeeded in opening link.`);
   20. })
   21. .catch((error: BusinessError) => {
   22. hilog.error(0x0000, 'testTag', `Failed to open link, code: ${error.code}, message: ${error.message}`);
   23. });
   24. })
   25. }
   26. .width('100%')
   27. }
   28. .height('100%')
   29. }
   30. }
   ```
6. 调试验证。

   安装并启动拉起方应用后，点击"拉起目标应用"按钮即可拉起目标应用，演示效果如下：

   **图1** 拉起目标应用演示

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/i3rWdfHxRaCkEKkCo7raWg/zh-cn_image_0000002558763994.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052550Z&HW-CC-Expire=86400&HW-CC-Sign=9E6F9F66518FAD962B9FFB7A7BC27112DF7739407B6B48F491D6E0E6A49CB31A)
