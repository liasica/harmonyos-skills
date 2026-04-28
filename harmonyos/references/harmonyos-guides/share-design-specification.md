---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-design-specification
title: 目标应用设计规范
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 目标应用处理分享内容 > 目标应用设计规范
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7d2501610599559fc164deae7b6e614fbd7364f7af00738f53079423d68c9f1d
---

本章节主要介绍目标应用接入系统分享面板时，所涉及的设计规范要求。具体参见：[设计指南-分享方式区](../design-guides/share-0000001957076313.md#section132401520173711)

## 应用名称和图标规范

当应用实现了用于接收分享内容的[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)或者[UIExtensionAbility](../harmonyos-references/js-apis-app-ability-uiextensionability.md)后，可在配置文件（src/main/module.json5）的[skills](module-configuration-file.md#skills标签)配置中注册。并配置actions为ohos.want.action.sendData。

当分享内容类型为应用所支持的类型时，应用图标将出现在分享面板的分享方式区内。

应用可以针对不同的ability，设置不同的名称和图标。

示例：

```
1. "abilities": [
2. {
3. "name": "TestUIAbility",
4. "srcEntry": "./ets/entryability/TestUIAbility.ets",
5. "label": "$string:EntryAbility_label", // ability名称
6. "icon": "$media:layered_image", // ability图标
7. "description": "$string:EntryAbility_desc",
8. "startWindowIcon": "$media:startIcon",
9. "startWindowBackground": "$color:start_window_background",
10. "exported": true,
11. "skills": [
12. {
13. "actions": [
14. "ohos.want.action.sendData"
15. ],
16. "uris": [
17. {
18. "scheme": "file",
19. "utd": "general.text",
20. "maxFileSupported": 1
21. }
22. ]
23. }
24. ]
25. }
26. ],
27. "extensionAbilities": [
28. {
29. "name": "TestShareAbility",
30. "srcEntry": "./ets/abilities/TestShareAbility.ts",
31. "type": "share", // 支持分享数据处理
32. "exported": true,
33. "label": "$string:xx_label", // ability名称
34. "icon": "$media:icon", // ability图标
35. "description": "$string:TestShareAbility_desc",
36. "skills": [
37. {
38. "actions": [
39. "ohos.want.action.sendData"
40. ],
41. "uris": [
42. {
43. "scheme": "file",
44. "utd": "general.text",
45. "maxFileSupported": 1
46. }
47. ]
48. }
49. ]
50. }
51. ]
```
