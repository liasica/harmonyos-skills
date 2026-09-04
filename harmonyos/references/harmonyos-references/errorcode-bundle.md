---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bundle
title: 包管理子系统通用错误码
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > 错误码 > 包管理子系统通用错误码
category: harmonyos-references
scraped_at: 2026-09-05T06:16:27+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a83902044db9f269e9affb0c0ab702b7d754ad8a81d5d714ca7afe663ccb271f
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 17700001 指定的bundleName不存在

**错误信息**

The specified bundle name is not found.

**错误描述**

指定的bundleName不存在。

**可能原因**

1. 输入的bundleName有误。
2. 系统中对应的应用没有安装。

**处理步骤**

1. 检查bundleName拼写是否正确。
2. 可以使用[查询应用信息命令（dump）](../harmonyos-guides/bm-tool.md#查询应用信息命令dump)查看应用是否安装。查看输出的打印信息，应用未安装时，该命令执行会报错。

   ```shell
   # 需要将com.xxx.demo替换为实际查询的bundleName
   hdc shell bm dump -n com.xxx.demo
   ```

## 17700002 指定的moduleName不存在

**错误信息**

The specified module name is not found.

**错误描述**

指定的moduleName不存在。

**可能原因**

1. 输入的moduleName有误。
2. 系统中对应的应用没有安装该模块。

**处理步骤**

1. 检查moduleName拼写是否正确。
2. 可以使用[查询应用信息命令（dump）](../harmonyos-guides/bm-tool.md#查询应用信息命令dump)查看对应的模块是否安装。查看输出的打印信息中hapModuleNames字段对应的列表是否存在该moduleName，不存在则说明应用未安装该模块。

   ```shell
   # 需要将com.xxx.demo替换为实际查询的bundleName
   hdc shell bm dump -n com.xxx.demo
   ```

## 17700003 指定的abilityName不存在

**错误信息**

The specified ability name is not found.

**错误描述**

指定的abilityName不存在。

**可能原因**

1. 输入的abilityName有误。
2. 系统中对应的应用不存在该abilityName对应的ability。
3. 调用[bundleManager.getProfileByAbility](js-apis-bundlemanager.md#bundlemanagergetprofilebyability)、[bundleManager.getProfileByExtensionAbility](js-apis-bundlemanager.md#bundlemanagergetprofilebyextensionability) 等通过abilityName、moduleName组合查询的接口时，对应的应用没有安装moduleName对应的模块，对应模块下的ability也不存在。

**处理步骤**

1. 检查abilityName拼写是否正确。
2. 可以使用[查询应用信息命令（dump）](../harmonyos-guides/bm-tool.md#查询应用信息命令dump)查看对应的应用是否存在这个abilityName。查看输出的打印信息中hapModuleInfos字段对应的abilityInfos下是否包含name等于该abilityName，不包含则说明该abilityName不存在。
3. 可以使用[查询应用信息命令（dump）](../harmonyos-guides/bm-tool.md#查询应用信息命令dump)查看输出的打印信息中hapModuleNames字段对应的列表是否存在对应的moduleName，不存在则说明应用未安装该模块，对应模块下的ability也不存在。

   ```shell
   # 需要将com.xxx.demo替换为实际查询的bundleName
   hdc shell bm dump -n com.xxx.demo
   ```

## 17700004 指定的用户不存在

**错误信息**

The specified user ID is not found.

**错误描述**

调用与用户相关接口时，传入的用户不存在。

**可能原因**

1. 输入的用户编号有误。
2. 系统中没有该用户。

**处理步骤**

1. 检查用户编号拼写是否正确。
2. 确认系统中存在该用户。

## 17700010 文件解析失败导致应用安装失败

**错误信息**

Failed to install the HAP because the HAP fails to be parsed.

**错误描述**

传入的HAP或APP解析失败。

**可能原因**

1. HAP或APP的格式不是zip格式。
2. HAP的配置文件不满足json格式。
3. HAP的配置文件缺少必要的字段。
4. HAP中配置了可执行二进制文件（即module.json5中配置了[executableBinaryPaths标签](../harmonyos-guides/module-configuration-file.md#executablebinarypaths标签)），但是没有配置解压模式，或当前设备不支持安装配置了该标签的HAP。
5. 传入的安装路径中或目录下存在多个APP。
6. APP中不包含适合在当前设备类型上安装的HAP。
7. 应用配置了skill，但配置的skill名称、skill目录名与SKILL.md中frontmatter的name不一致。

**处理步骤**

1. 确认HAP或APP的格式是zip。
2. 确认HAP的配置文件满足[配置文件json格式](../harmonyos-guides/application-configuration-file-overview-stage.md)。
3. 检查DevEco Studio编译HAP或APP时是否有错误提示，缺省字段时会有相应的报错。
4. 配置应用为解压模式，即在应用的[module.json5配置文件](../harmonyos-guides/module-configuration-file.md#配置文件标签)中设置compressNativeLibs标签为true；或更换为PC/2in1设备。
5. 检查传入的路径下是否包含多个APP。
6. 确认APP内是否存在支持当前设备类型的HAP。
7. 检查module.json中skillProfiles下skill的name、skills目录下的子目录名称、SKILL.md中frontmatter的name，确保三者一致。

## 17700011 签名校验失败导致应用安装失败

**错误信息**

Failed to install the HAP because the HAP signature fails to be verified.

**错误描述**

签名校验失败导致应用安装失败。

**可能原因**

1. HAP或APP没有签名。
2. HAP或APP签名信息来源不可靠。
3. 升级的HAP与已安装的HAP签名信息不一致。
4. 多个HAP的签名信息不一致。

**处理步骤**

1. 确认HAP包或APP包是否签名成功。
2. 确认HAP包或APP包的签名证书是从应用市场申请。
3. 确认多个HAP包签名时使用的证书相同。
4. 确认升级的HAP包签名证书与已安装的HAP包相同。

## 17700012 安装包路径无效或者文件过大导致应用安装失败

**错误信息**

Failed to install the HAP because the HAP path is invalid or the HAP is too large.

**错误描述**

安装包路径无效或者文件过大导致应用安装失败。

**可能原因**

1. 输入错误，HAP或APP的文件路径不存在。
2. HAP或APP的路径无法访问。
3. HAP的大小超过最大限制4GB。

**处理步骤**

1. 确认HAP或APP是否存在。
2. 查看HAP或APP的可执行权限，是否可读。
3. 查看HAP的大小是否超过4GB。

## 17700015 多个HAP配置信息不同导致应用安装失败

**错误信息**

Failed to install the HAPs because they have different configuration information.

**错误描述**

多个HAP配置信息不同导致应用安装失败。

**可能原因**

多个HAP包中配置文件中app标签下面的字段信息或者签名信息不一致。

**处理步骤**

确认多个HAP中配置文件app下面的字段是否一致或者检查工程的[signingConfigs](../harmonyos-guides/ide-hvigor-build-profile-app.md#section153288223224)配置是否一样。

## 17700016 系统磁盘空间不足导致应用安装失败

**错误信息**

Failed to install the HAP because of insufficient system disk space.

**错误描述**

系统磁盘空间不足导致应用安装失败。

**可能原因**

系统空间不足。

**处理步骤**

确认系统是否有足够的空间。

## 17700017 新安装的应用版本号低于已安装的版本号导致应用安装失败

**错误信息**

Failed to install the HAP since the version of the HAP to install is too early.

**错误描述**

新安装的应用版本号低于已安装的版本号导致应用安装失败。

**可能原因**

新安装的应用版本号低于已安装的版本号。

**处理步骤**

确认新安装的应用版本号是否不低于已安装的同应用版本号。

1. 已安装应用版本号查询，依赖[hdc工具](../harmonyos-guides/hdc.md#环境准备)。执行命令行后会输出已安装应用的版本号versionCode，如果输出多个versionCode，选择大于0的。如果该命令无打印值输出，表示应用未安装。

   ```shell
   # 需要将com.xxx.demo替换为查询的bundleName
   hdc shell "bm dump -n com.xxx.demo |grep versionCode"
   ```
2. 新安装的应用查看版本，HAP或者HSP用DevEco Studio打开，查看里面module.json文件中的versionCode字段配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/UDorGOccSJqU6XBxQO72Nw/zh-cn_image_0000002742124659.png)

## 17700021 指定的uid无效

**错误信息**

The specified uid is invalid.

**错误描述**

调用bundleManager模块中的[getBundleNameByUid](js-apis-bundlemanager.md#bundlemanagergetbundlenamebyuid14)时，指定的uid无效。

**可能原因**

传入的uid对应的应用不存在。

**处理步骤**

检查系统中是否存在对应的应用uid值。可以使用[查询应用信息命令（dump）](../harmonyos-guides/bm-tool.md#查询应用信息命令dump)查看已安装应用的uid。执行命令行后会输出对应已安装应用的uid，如果输出多个uid，选择大于0的。如果该命令无打印值输出，表示应用未安装。

```shell
# 需要将com.xxx.demo替换为实际查询的bundleName
hdc shell "bm dump -n com.xxx.demo |grep uid"
```

## 17700024 没有相应的配置文件

**错误信息**

Failed to get the profile because the specified profile is not found in the HAP.

**错误描述**

调用查询profile文件的相关接口时，没有相应的配置文件。

**可能原因**

1. 输入的metadata name在配置文件中不存在。
2. 配置文件的内容不是json格式。

**处理步骤**

1. 确认要查询的ability或者extensionAbility中的metadata name是否存在。
2. 确认指定查询的profile文件的内容是否为json格式。

## 17700026 指定应用被禁用

**错误信息**

The specified bundle is disabled.

**错误描述**

当调用查询应用的相关信息接口时，指定应用被禁用。

**可能原因**

设备上对应的应用已经被禁用，无法查询。

**处理步骤**

确认设备上对应的应用是否被禁用。

## 17700029 指定的ability被禁用

**错误信息**

The specified ability is disabled.

**错误描述**

当调用查询ability相关信息的接口时，指定的ability被禁用。

**可能原因**

指定的ability被禁用。

**处理步骤**

确认指定的ability是否被禁用，可以使用[bm工具](../harmonyos-guides/bm-tool.md)查询对应的应用信息。

## 17700032 指定的应用不包含overlay特征的module

**错误信息**

The specified bundle does not contain any overlay module.

**错误描述**

查询指定应用中overlay特征module的overlayModuleInfo时，指定的应用不包含overlay特征module。

**可能原因**

指定的应用不包含overlay特征module。

**处理步骤**

检查指定的应用是否不包含overlay特征module。

## 17700033 指定的module不是overlay特征的module

**错误信息**

The specified module is not an overlay module.

**错误描述**

查询指定的overlay特征module的overlayModuleInfo时，指定的module不是overlay特征module。

**可能原因**

指定的module不是overlay特征的module。

**处理步骤**

检查指定的module是否不为overlay特征的module。

## 17700034 指定的module是overlay特征的module

**错误信息**

The specified module is an overlay module.

**错误描述**

查询指定的目标module所关联的overlayModuleInfo时，指定的module是overlay特征module。

**可能原因**

指定的module是overlay特征的module。

**处理步骤**

检查指定的module是否为overlay特征的module。

## 17700048 代码签名校验失败

**错误信息**

Failed to install the HAP because the code signature verification failed.

**错误描述**

安装应用时，安装包的代码签名文件校验失败。

**可能原因**

1. 代码签名文件对应的module在安装包中不存在。
2. 代码签名文件路径无效。
3. 代码签名文件和对应的安装包不匹配。

**处理步骤**

1. 检查代码签名文件对应的module是否包含在安装包路径之中。
2. 检查提供的代码签名文件的路径是否合法。
3. 使用和安装包匹配的代码签名文件。

## 17700052 非开发者模式下不允许安装调试自分发插件或调试应用

**错误信息**

Failed to install the HAP because a debug bundle can be installed only in developer mode.

**错误描述**

安装调试应用时，设备处于非开发者模式，不允许安装。

**可能原因**

应用为调试应用，而设备处于非开发者模式。

**处理步骤**

执行hdc shell param get const.security.developermode.state，若返回结果为false，说明该设备无法安装调试应用。

## 17700055 指定的link无效

**错误信息**

The specified link is invalid.

**错误描述**

调用bundleManager模块中的[canOpenLink](js-apis-bundlemanager.md#bundlemanagercanopenlink12)时，指定的link无效。

**可能原因**

输入的link格式有误。

**处理步骤**

检查link格式是否正确。

## 17700056 指定link的scheme未在querySchemes字段下配置

**错误信息**

The scheme of the specified link is not in the querySchemes.

**错误描述**

调用bundleManager模块中的[canOpenLink](js-apis-bundlemanager.md#bundlemanagercanopenlink12)时，指定link的scheme未在querySchemes字段下配置。

**可能原因**

未在querySchemes字段下配置指定link的scheme。

**处理步骤**

检查是否在querySchemes字段下配置了相应的URL scheme，可以参考[使用canOpenLink判断应用是否可访问](../harmonyos-guides/canopenlink.md)。

## 17700061 指定的应用分身索引无效

**错误信息**

The appIndex is invalid.

**错误描述**

调用应用分身相关的接口时，指定的应用分身索引无效。

**可能原因**

1. 分身索引超出允许的范围。
2. 应用没有该索引的分身。

**处理步骤**

1. 检查索引是否在允许范围内。
2. 检查应用是否有该索引的分身。

## 17700070 指定的快捷方式id不合法

**错误信息**

The specified shortcut id is illegal.

**错误描述**

快捷方式id是不合法的。

**可能原因**

已经存在相同包名、分身索引、用户id和快捷方式id的快捷方式信息；传参对应的快捷方式id不存在，或快捷方式id为空字符串。

**处理步骤**

1. 检查包名或者快捷方式id是否正确。

## 17700072 Launch Want不存在

**错误信息**

The launch want is not found.

**错误描述**

调用[bundleManager.getLaunchWant](js-apis-bundlemanager.md#bundlemanagergetlaunchwant13)接口时，应用的启动组件Want信息不存在。

**可能原因**

应用没有entities配置包含“entity.system.home”和actions配置包含“ohos.want.action.home”的UIAbility。

**处理步骤**

应用需要有entities配置包含“entity.system.home”并且actions配置包含“ohos.want.action.home”的UIAbility。

## 17700073 由于设备上存在具有相同包名称但不同签名信息的应用程序，导致安装失败

**错误信息**

Failed to install the HAP because an application with the same bundle name but different signature information exists on the device.

**错误描述**

由于设备上存在具有相同包名称但不同签名信息的应用程序，导致安装失败。

**可能原因**

1. 由于设备上存在具有相同包名称但不同签名信息的已安装应用程序，导致安装失败。
2. 设备上存在相同包名但签名信息不一致的应用被保留数据地卸载，导致安装失败。

**处理步骤**

1. 卸载设备上相同包名的应用。
2. 若设备上存在相同包名但签名信息不一致的应用被保留数据地卸载，导致安装失败，则先安装已卸载的应用之后不保留数据地卸载掉。

## 17700087 当前设备不支持安装插件

**错误信息**

Failed to install the plugin because the current device does not support plugins.

**错误描述**

当前设备不支持插件能力。

**可能原因**

设备不具备插件能力，安装插件失败。

**处理步骤**

使用[param工具](../harmonyos-guides/param-tool.md)设置const.bms.support\_plugin的值为true，即执行hdc shell param set const.bms.support\_plugin true。

## 17700091 插件与主体同包名

**错误信息**

Failed to install the plugin because the plugin name is the same as the host bundle name.

**错误描述**

插件的包名与应用的包名一致，不符合插件与应用之间异包名的规格，安装插件失败。

**可能原因**

插件的包名与应用的包名一致。

**处理步骤**

重新配置插件的包名。

## 17700092 插件包名不存在

**错误信息**

Failed to uninstall the plugin because the specified plugin is not found.

**错误描述**

插件包名不存在，导致插件卸载时失败。

**可能原因**

插件没有在应用中安装。

**处理步骤**

使用[bm dump -n 命令](../harmonyos-guides/bm-tool.md#查询应用信息命令dump)查询应用信息，确认插件是否安装。

## 17700093 指定的skillName不存在

**错误信息**

The specified skillName is not found.

**错误描述**

未找到与指定skillName匹配的Skill信息，指定的skillName不存在。

**可能原因**

1. 传入查询接口的skillName有误。
2. 传入查询接口的Skill没有安装。

**处理步骤**

1. 排查skillName，确认拼写无误。
2. 使用[bm工具](../harmonyos-guides/bm-tool.md)安装对应Skill所在的应用。

## 17700101 包管理服务异常

**错误信息**

Bundle manager service exception.

**错误描述**

包管理服务异常。

**可能原因**

场景一：

系统出现未知的异常，导致包管理服务已停止或者异常退出。

场景二：

系统抛出未捕获的错误码，例如IPC失败、文件拷贝失败等。

**处理步骤**

1. 重启手机后再次尝试请求接口。
2. 重复上述步骤3到5次后依旧请求失败，请查询设备的/data/log/faultlog/faultlogger/目录下是否存在包含foundation字样的crash文件。

   ```shell
   hdc shell
   cd /data/log/faultlog/faultlogger/
   ls -ls
   ```
3. 导出crash文件和日志文件提[新增Issue](https://atomgit.com/HarmonyOS/docs/issues)获取帮助。

   ```shell
   hdc file recv /data/log/faultlog/faultlogger/
   hdc file recv /data/log/hilog/
   ```

## 17700308 备用图标名称没有在配置文件中配置

**错误信息**

The alternateIconName must match the name field under alternateIcons in the app.json5 file.

**错误描述**

备用图标名称必须与app.json5中[alternateIcons标签](../harmonyos-guides/app-configuration-file.md#alternateicons标签)配置的name字段匹配。

**可能原因**

传入的alternateIconName在app.json5的[alternateIcons标签](../harmonyos-guides/app-configuration-file.md#alternateicons标签)中未配置。

**处理步骤**

1. alternateIconName传入app.json5的[alternateIcons标签](../harmonyos-guides/app-configuration-file.md#alternateicons标签)中配置的name。
2. 在app.json5的[alternateIcons标签](../harmonyos-guides/app-configuration-file.md#alternateicons标签)中配置接口传入的alternateIconName。

## 17700309 当前没有设置备用图标

**错误信息**

No alternate icon is enabled.

**错误描述**

没有设置备用图标。

**可能原因**

当前应用未设置备用图标，在alternateIconName传入空字符串恢复默认图标时会抛出17700309。

**处理步骤**

当前应用未设置备用图标，不需要取消备用图标。

## 17700310 设置备用图标失败

**错误信息**

Failed to set the alternate icon.

**错误描述**

设置备用图标失败。

**可能原因**

1. 分身应用暂不支持设置备用图标。
2. 用户使用了自定义主题（例如在主题应用中设置了非官方的主题），主题包内包含了本应用的图标资源。此时调用接口启用备用图标会失败，并抛出17700310错误码。

**处理步骤**

检查当前使用的主题是否为自定义主题，可以切换为官方主题后重新调用接口。

## 17700311 查询备用图标失败

**错误信息**

Failed to obtain alternate icon.

**错误描述**

查询备用图标失败。

**可能原因**

分身应用暂不支持备用图标。当分身应用查询备用图标会失败，抛出17700311错误码。

**处理步骤**

检查当前应用是否是分身应用，分身应用暂不支持查询备用图标，请使用主应用查询备用图标。
