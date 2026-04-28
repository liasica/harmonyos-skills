---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/change-description-600-beta1
title: 变更说明
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > DevEco Studio > 变更说明
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:45+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:25acf87ff814a30ec791a3f1d8de0f3331d5cfd8a1959c8dc02818193eefdcfc
---

## DevEco Studio 6.0.0 Beta3引入的变更

### hot reload不再支持箭头函数内this变量的首次新增或彻底删除

升级到DevEco Studio 6.0.0 Beta3及以上版本，在hot reload模式下对箭头函数内this变量进行首次新增或彻底删除会报错。

**变更影响**

hot reload不再支持箭头函数内this变量的首次新增或彻底删除。

如用户编写如下代码：

```
1. // test.ets
2. class Foo {
3. str: string = "this is string"
4. test() {
5. let a = () => {
6. console.log(this.str)
7. }
8. a()
9. }
10. }
11. let foo = new Foo()
```

使用hot reload模式进行调试。调试时，修改代码为：

```
1. class Foo {
2. str: string = "this is string"
3. test() {
4. let a = () => {
5. console.log("this is change")
6. }
7. a()
8. }
9. }
10. let foo = new Foo()
```

进行hot reload则会报错，报错内容如下：

```
1. compile error: 10706001 Unsupported Change in Hot Reload
2. compile error: Error Message: Found lexical variable added or removed in 'xxxxx', not supported!
3. compile error: [Patch] Found unspported change in file, will not generate patch!
```

**适配指导**

若需要在hot reload时对箭头函数内this变量进行首次新增或彻底删除，则需要重新编译并调试。

## DevEco Studio 6.0.0 Beta1引入的变更

### DevEco Studio底座升级，语言切换方式变更，部分插件不可使用

DevEco Studio 6.0.0 Beta1版本适配IntelliJ 2024.3.3底座升级后，语言切换方式变更，部分插件不可使用。

**变更影响**

1. 语言插件生效机制变更：之前版本需要通过Plugins中启用语言插件来控制界面语言的显示；新版本中，中文化插件无需下载，默认安装开启，切换界面显示语言方式变更。
2. 部分插件不可使用：如果插件未适配IntelliJ 2024.3.3版本，可能会出现不可使用的情况。

**适配指导**

1. 如需切换DevEco Studio语言显示效果，在菜单栏进入**File > Settings... > Appearance & Behavior > System Settings** > **Language**，语言选择**Chinese**并点击**Apply**，在弹窗中点击**Restart**重启即可完成语言切换。
2. 请更换使用已适配新底座IntelliJ 2024.3.3的插件版本。

### ArkTS日志位置调整

升级到DevEco Studio 6.0.0 Beta1及以上版本，ArkTS日志位置变更如下。

**表1**

| **场景** | **hvigor日志参数** | **输出位置** | **ArkTS的日志信息（变更前）** | **ArkTS的日志信息（变更后）** |
| --- | --- | --- | --- | --- |
| ArkTS报错 | --info | stdout | null | info |
| stderr | info、warn、error | warn、error |
| --warn | stdout | null | null |
| stderr | info、warn、error | warn、error |
| --error | stdout | null | null |
| stderr | info、warn、error | error |
| 编译成功 | --info | stdout | info、warn | info |
| stderr | error | warn、error |

**变更影响**

通过hvigor-config.json5文件的[level](../harmonyos-guides/ide-hvigor-set-options.md#section85176471028)字段指定日志级别，或通过[命令行方式](../harmonyos-guides/ide-hvigor-commandline.md#section682961710111)指定日志级别，不同的日志级别打印的信息变化如下：

* ArkTS报错场景：
  + --info：info日志的输出位置从stderr移动到stdout。
  + --warn：不再打印info日志。
  + --error：不再打印info、warn日志。
* 编译成功场景：
  + ArkTS的warn日志从stdout移动到stderr。

**适配指导**

根据上面表格找到变更后的日志位置进行适配。

### ArkUI-X工程配套的gradle版本变更

升级到DevEco Studio 6.0.0 Beta1及以上版本，历史版本创建的ArkUI-X工程会构建失败。

**变更影响**

如果ArkUI-X工程是使用DevEco Studio 6.0.0 Beta1以下版本创建的，升级到Beta1及以上版本，编译会失败，并提示Could not open settings generic class cache for settings file。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/PT5p_etyQ5KCkoWfFhs10w/zh-cn_image_0000002391137566.png?HW-CC-KV=V1&HW-CC-Date=20260427T233443Z&HW-CC-Expire=86400&HW-CC-Sign=E3CD4AC75478C4E8ADBAF1F0EA201D5FCBE1341F2F7AC0B1F558E55439D14FF8)

**适配指导**

* **方式一：升级gradle版本**

  修改gradle-wrapper.properties中的distributionUrl，升级为8.4版本。

  ```
  1. distributionUrl=https\://repo.huaweicloud.com/gradle/gradle-8.4-bin.zip
  ```

* **方式二：指定使用jdk17**

  如果本地有jdk17，可以在gradle.properties中通过org.gradle.java.home变量指定使用jdk17。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/UCtfLw7ySKC0AcfIIcNI7w/zh-cn_image_0000002457140953.png?HW-CC-KV=V1&HW-CC-Date=20260427T233443Z&HW-CC-Expire=86400&HW-CC-Sign=9E621BAD0CB35A4401192D96E855359B3CA44C6B4D97C326C9EAADCC39CFAC5A)
