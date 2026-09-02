---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-17
title: 编译报错“Schema validate failed”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Schema validate failed”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:90a42d2a2b46fb41eaf8ad210cbbcaf612fd619da8ddfaa8d9a3a67dca2386df
---

**问题现象**

DevEco Studio编译时出现“Schema validate failed”错误。

**解决措施**

问题源于配置文件中字段缺失或拼写错误，请根据报错信息进行定位。

如将module.json5文件中abilities标签中的 “name” 错写为 “nam”，报错信息如下：

```json
Detail: Please check the following fields.
{
  instancePath: 'module.abilities[0]',
  keyword: 'required',
  params: { missingProperty: 'name' },
  message: "must have required property 'name'",
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 
{
  instancePath: 'module.abilities[0]',
  keyword: 'required',
  params: { missingProperty: 'srcEntrance' },
  message: "must have required property 'srcEntrance'",
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 
{
  instancePath: 'module.abilities[0]',
  keyword: 'required',
  params: { missingProperty: 'name' },
  message: "must have required property 'name'",
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 
{
  instancePath: 'module.abilities[0]',
  keyword: 'oneOf',
  params: { passingSchemas: null },
  message: 'must match exactly one schema in oneOf',
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 
{
  instancePath: 'module.abilities[0]',
  keyword: 'enum',
  params: {
    allowedValues: [
      'priority',
      'name',
      'srcEntrance',
      'srcEntry',
      'launchType',
      'description',
      'icon',
      'label',
      'permissions',
      'metadata',
      'visible',
      'exported',
      'skills',
      'backgroundModes',
      'continuable',
      'startWindowIcon',
      'startWindowBackground',
      'removeMissionAfterTerminate',
      'orientation',
      'supportWindowMode',
      'maxWindowRatio',
      'minWindowRatio',
      'maxWindowWidth',
      'minWindowWidth',
      'maxWindowHeight',
      'minWindowHeight',
      'excludeFromMissions'
    ]
  },
  message: 'must be equal to one of the allowed values',
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 
{
  instancePath: 'module.abilities[0]',
  keyword: 'propertyNames',
  params: { propertyName: 'nam' },
  message: 'property name must be valid',
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
}
```

以上报错为例，解释报错中关键词的含义，帮助开发者理解报错信息，从而完成问题定位和修改。

* instancePath：错误所在的文件位置。'module.abilities[0]'表示在module.json5文件中的第一个abilities。
* keyword：标识当前报错字段的可选属性，包括 'required'、'oneOf'、'enum'、'propertyNames'。
  + required：表示该字段为必选配置项。若缺失或拼写错误将导致属性未配置。
  + oneOf：表示当前配置不符合oneOf要求。通过instancePath已经确认报错出现在abilities标签，在DevEco Studio中，按住Ctrl点击"abilities"跳转到对应的module.json文件，可以查看到必须配置以下两组中的一组。根据对比排查，可识别到因拼写错误导致"name"属性未配置。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/V-DsHIcPTN6krqeCS560PQ/zh-cn_image_0000002654797847.png)
  + enum：所有可配置的属性。开发者可根据枚举值确认属性的正确写法。
  + propertyNames：字段拼写错误时，propertyName: 'nam'指明 "nam" 为错误属性。
* params：不同keyword对应不同的详细说明。例如，当keyword为'required'时，params的missingProperty: 'name'表示缺失的属性为“name”。
* message：修改要求的说明。例如，当keyword为'required'时，message表示必须配置name属性。
* location：错误位置，点击可以跳转。
