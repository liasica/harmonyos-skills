---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-17
title: 编译报错“Schema validate failed”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Schema validate failed”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:24+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:bcc84c12a4e82856ca13bda763af079b3a940148001cdc8863958bfcceb8437b
---

**问题现象**

DevEco Studio编译时出现“Schema validate failed”错误。

**解决措施**

问题源于配置文件中字段缺失或拼写错误，请根据报错信息进行定位。

如将module.json5文件中abilities标签中的 “name” 错写为 “nam”，报错信息如下：

```
1. Detail: Please check the following fields.
2. {
3. instancePath: 'module.abilities[0]',
4. keyword: 'required',
5. params: { missingProperty: 'name' },
6. message: "must have required property 'name'",
7. location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
8. }
9. {
10. instancePath: 'module.abilities[0]',
11. keyword: 'required',
12. params: { missingProperty: 'srcEntrance' },
13. message: "must have required property 'srcEntrance'",
14. location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
15. }
16. {
17. instancePath: 'module.abilities[0]',
18. keyword: 'required',
19. params: { missingProperty: 'name' },
20. message: "must have required property 'name'",
21. location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
22. }
23. {
24. instancePath: 'module.abilities[0]',
25. keyword: 'oneOf',
26. params: { passingSchemas: null },
27. message: 'must match exactly one schema in oneOf',
28. location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
29. }
30. {
31. instancePath: 'module.abilities[0]',
32. keyword: 'enum',
33. params: {
34. allowedValues: [
35. 'priority',
36. 'name',
37. 'srcEntrance',
38. 'srcEntry',
39. 'launchType',
40. 'description',
41. 'icon',
42. 'label',
43. 'permissions',
44. 'metadata',
45. 'visible',
46. 'exported',
47. 'skills',
48. 'backgroundModes',
49. 'continuable',
50. 'startWindowIcon',
51. 'startWindowBackground',
52. 'removeMissionAfterTerminate',
53. 'orientation',
54. 'supportWindowMode',
55. 'maxWindowRatio',
56. 'minWindowRatio',
57. 'maxWindowWidth',
58. 'minWindowWidth',
59. 'maxWindowHeight',
60. 'minWindowHeight',
61. 'excludeFromMissions'
62. ]
63. },
64. message: 'must be equal to one of the allowed values',
65. location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
66. }
67. {
68. instancePath: 'module.abilities[0]',
69. keyword: 'propertyNames',
70. params: { propertyName: 'nam' },
71. message: 'property name must be valid',
72. location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
73. }
```

以上报错为例，解释报错中关键词的含义，帮助开发者理解报错信息，从而完成问题定位和修改。

* instancePath：错误所在的文件位置。'module.abilities[0]'表示在module.json5文件中的第一个abilities。
* keyword：标识当前报错字段的可选属性，包括 'required'、'oneOf'、'enum'、'propertyNames'。
  + required：表示该字段为必选配置项。若缺失或拼写错误将导致属性未配置。
  + oneOf：表示当前配置不符合oneOf要求。通过instancePath已经确认报错出现在abilities标签，在DevEco Studio中，按住Ctrl点击"abilities"跳转到对应的module.json文件，可以查看到必须配置以下两组中的一组。根据对比排查，可识别到因拼写错误导致"name"属性未配置。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/joXujhYmQ-im9vYytJ70Fw/zh-cn_image_0000002194158784.png?HW-CC-KV=V1&HW-CC-Date=20260429T062023Z&HW-CC-Expire=86400&HW-CC-Sign=BBB154B9E714E95F5DBF26C8D072BA78D88DD1D82B430F9C7D5AB3820C9E80FD)
  + enum：所有可配置的属性。开发者可根据枚举值确认属性的正确写法。
  + propertyNames：字段拼写错误时，propertyName: 'nam'指明 "nam" 为错误属性。
* params：不同keyword对应不同的详细说明。例如，当keyword为'required'时，params的missingProperty: 'name'表示缺失的属性为“name”。
* message：修改要求的说明。例如，当keyword为'required'时，message表示必须配置name属性。
* location：错误位置，点击可以跳转。
