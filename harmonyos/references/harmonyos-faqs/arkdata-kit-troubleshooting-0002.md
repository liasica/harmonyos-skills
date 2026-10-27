---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkdata-kit-troubleshooting-0002
title: Preferences数据持久化报错15501002问题排查与解决
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 故障排查 > Preferences数据持久化报错15501002问题排查与解决
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:58+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:3f83ebba5e5b7c19465e3b06df44ff61adac82c64d90e69e9e4d0bbf24a41f27
---

## 问题现象

在UIAbility中onWindowStageCreate方法中调用如下代码初始化preferences实例：

```ts
  let options: dataPreferences.Options = {
    name: 'byStore', dataGroupId: '01'
  };
  let preferences = dataPreferences.getPreferencesSync(this.context, options);
```

运行后提示如下错误，错误码为15501002，错误信息为“The data group id is not valid”：

```txt
  Error message:The data group id is not valid
  Error code:15501002
  SourceCode:
  let preferences = dataPreferences.getPreferencesSync(this.context, options);
  ^
  Stacktrace:
  at onWindowStageCreate (entry/src/main/ets/entryability/EntryAbility.ets:25:27)
```

## 定位过程

报错信息显示数据组Id无效，判断是getPreferences的传参Options里的dataGroupId不对，代码中的dataGroupId是自定义的，而不是通过应用市场申请，就会导致运行后报错。

## 分析结论

dataGroupId必须向应用市场[申请](../doccenter-capabilities/ime-kit-security.md#共享沙箱介绍)获取，自定义无效。上述代码中使用了自定义的dataGroupId，所以运行后代码报错。

## 修改建议

如果业务场景中无需使用dataGroupId，可以选择不设置dataGroupId进行数据初始化，参考[用户首选项开发步骤](../harmonyos-guides/data-persistence-by-preferences.md#开发步骤)。
