---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-configuration-file-overview-fa
title: 应用配置文件概述（FA模型）
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 应用配置文件（FA模型） > 应用配置文件概述（FA模型）
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b7332ba1f168a40ed3f84715d73b41d40d25a78135f10101f354f3e3441971e2
---

每个应用项目必须在项目的代码目录下加入配置文件，这些配置文件会向编译工具、操作系统和应用市场提供描述应用的基本信息。

应用配置文件需要声明以下内容：

* 应用的软件Bundle名称，应用的开发厂商，版本号等应用的基本配置信息，这些信息被要求设置在app这个字段下。
* 应用的组件的基本信息，包括所有的Ability，设备类型，组件的类型以及当前组件所使用的语法类型。
* 应用在具体设备上的配置信息，这些信息会影响应用在设备上的具体功能。

在FA模型的应用开发过程中，需要在config.json配置文件中对应用的包结构进行声明。

## 配置文件的内部结构

config.json由app、deviceConfig和module三个部分组成，缺一不可。

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| [app](app-structure.md) | 标识应用的全局配置信息。同一个应用的不同HAP的app配置必须保持一致。 | 对象 | 不可缺省。 |
| [deviceConfig](deviceconfig-structure.md) | 标识应用在具体设备上的配置信息。 | 对象 | 不可缺省。 |
| [module](module-structure.md) | 标识HAP的配置信息。该标签下的配置只对当前HAP生效。 | 对象 | 不可缺省。 |

config.json示例：

```
1. {
2. "app": {
3. "vendor": "example",
4. "bundleName": "com.example.demo",
5. "version": {
6. "code": 1000000,
7. "name": "1.0.0"
8. }
9. },
10. "deviceConfig": {
11. },
12. "module": {
13. "mainAbility": ".MainAbility_entry",
14. "deviceType": [
15. "tablet"
16. ],
17. "commonEvents": [
18. {
19. "name": ".EntryAbility",
20. "permission": "ohos.permission.GET_BUNDLE_INFO",
21. "data": [
22. "com.example.demo",
23. "100"
24. ],
25. "events": [
26. "install",
27. "update"
28. ]
29. }
30. ],
31. "abilities": [
32. {
33. "skills": [
34. {
35. "entities": [
36. "entity.system.home"
37. ],
38. "actions": [
39. "action.system.home"
40. ]
41. }
42. ],
43. "orientation": "unspecified",
44. "visible": true,
45. "srcPath": "MainAbility_entry",
46. "name": ".MainAbility_entry",
47. "srcLanguage": "ets",
48. "icon": "$media:icon",
49. "description": "$string:MainAbility_entry_desc",
50. "formsEnabled": false,
51. "label": "$string:MainAbility_entry_label",
52. "type": "page",
53. "launchType": "multiton"
54. }
55. ],
56. "distro": {
57. "moduleType": "entry",
58. "installationFree": false,
59. "deliveryWithInstall": true,
60. "moduleName": "myapplication"
61. },
62. "package": "com.example.myapplication",
63. "srcPath": "",
64. "name": ".myapplication",
65. "js": [
66. {
67. "mode": {
68. "syntax": "ets",
69. "type": "pageAbility"
70. },
71. "pages": [
72. "pages/index"
73. ],
74. "name": ".MainAbility_entry",
75. "window": {
76. "designWidth": 720,
77. "autoDesignWidth": false
78. }
79. }
80. ]
81. }
82. }
```
