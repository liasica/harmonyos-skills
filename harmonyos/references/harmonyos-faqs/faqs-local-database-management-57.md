---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-57
title: 如何解决preferences中报错15501002问题
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 如何解决preferences中报错15501002问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:29+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:d55724b22178239ef552302eae84eeb33a38ff5e5668f40ca85fd241ada5bdd6
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

```ts
  Error message:The data group id is not valid
  Error code:15501002
  SourceCode:
  let preferences = dataPreferences.getPreferencesSync(this.context, options);
  ^
  Stacktrace:
  at onWindowStageCreate (entry/src/main/ets/entryability/EntryAbility.ets:25:27)
```

## 背景知识

* [用户首选项](../harmonyos-references/js-apis-data-preferences.md)为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。

  数据存储采用键值对形式，键为字符串类型，值可为数字、字符、布尔类型及其对应的数组。
* [15501002](../harmonyos-references/errorcode-preferences.md#section15501002-options中传入的datagroupid参数非法)代表Options中传入的[dataGroupId](../harmonyos-references/js-apis-data-preferences.md#options10)参数非法。dataGroupId代表应用组Id，需要向应用市场获取，详见dataGroupId[申请流程](../harmonyos-guides/ime-kit-security.md#共享沙箱介绍)。

  注意：dataGroupId为可选参数。指定在此dataGroupId对应的沙箱路径下创建preferences实例。当此参数不填时，默认在本应用沙箱目录下创建preferences实例。模型约束：此属性仅在Stage模型下可用。

* dataGroupId的数据共享支持两种场景：

  1.同一应用的不同进程间共享，只支持三方应用中输入法和输入法的扩展场景使用；

  2.不同应用间的数据共享，只支持系统应用使用。

## 问题定位

报错信息显示数据组Id无效，判断是getPreferences的传参Options里的dataGroupId不对，代码中的dataGroupId是自定义的，而不是通过应用市场申请，就会导致运行后报错。

## 分析结论

dataGroupId必须向应用市场[申请](../harmonyos-guides/ime-kit-security.md#共享沙箱介绍)获取，自定义无效。上述代码中使用了自定义的dataGroupId，所以运行后代码报错。

## 修改建议

如果业务场景中无需使用dataGroupId，可以选择不设置dataGroupId进行数据初始化，参考[用户首选项开发步骤](../harmonyos-guides/data-persistence-by-preferences.md#开发步骤)。

## 常见FAQ

Q：在开发中，使用preferences缓存的数据，会把上次缓存的数据全部清除掉，这种情况如何解决？

A：preferences存入数据到preferences实例后，需要使用[flush](../harmonyos-references/js-apis-data-preferences.md#flush)方法实现数据持久化，在写入数据后再调用flush，如果是多次写入数据，只需要在最后一次写入数据后调用一次flush。

Q：使用IDE每次run项目（先卸载当前应用，再安装新的安装包），其在设备上产生的数据库文件及临时文件也会被移除，那么如何保存数据？

A：在‘Run/Debug Configurations’-‘General’-‘Installation Options’-中勾选‘Keep Application Data’。
