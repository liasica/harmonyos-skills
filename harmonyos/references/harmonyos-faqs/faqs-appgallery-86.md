---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-86
title: AGC上传软件包常见报错和解决方案
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > AGC上传软件包常见报错和解决方案
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:30+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:a129e7c52858f79d7ed80970c821fb5ba293bfaba0573ddffa514a94916ecda6
---

## 问题现象

应用开发完成后，打好的app包上传应用市场，经常会遇到软件包报错的情况，阻塞上架流程。报错有错误码和无错误码两种场景：

* 常见的错误码：
  + 上传软件包，提示软件包无效缺少依赖的包，错误码9。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/gylWaxJATjSULqLpjik5BQ/zh-cn_image_0000002689330382.png "点击放大")
  + 上传软件包，提示非法软件包，错误码991。
  + 使用Profile打包，上传软件包报错误码993。
  + 上传软件包，提示包解析失败，错误码1015。
  + 流水线构建的包，上传软件包报错码996。
  + 在软件打包过程中提示错误码7014。
  + 邀请测试上传软件包，提示错误码999。
  + 上传软件包后，报错软件包Profile版本不符合要求，错误码7017。
  + 上传软件包后，报错Profile非法，错误码7019。
  + 上传软件包后，报错系统异常，错误码7021。
  + 上传软件包后，报错当前软件包不支持上架到应用市场，错误码7022，7023，7024或7025。
* 无错误码：

  上传软件包，提示"软件包解析失败，请联系客服处理"。

  上传软件包，提示"The bundle name xxx is already in use. Change and rebuild the .app bundle."。

## 背景知识

* [软件包解析错误说明](../app/agc-help-harmonyoserror-0000001651912985.md)：不同的错误码表示不同的问题原因。
* [定制hvigor插件](../best-practices/bpta-custom-hvigor-plugin.md)：在进行编译构建的过程中，开发者可以通过定制hvigor插件，扩展构建逻辑，实现个性化的打包流程。定制hvigor插件可以满足自定义任务需求、加强构建任务可维护性、提升团队协作效率。

## 解决方案

* **报错返回错误码。**
  + [错误码9](../app/agc-help-harmonyoserror-0000001651912985.md#section148217589452)表示：软件包无效，缺少依赖的包。可以根据以下方向排查问题：
    - 压缩软件包时是否压缩掉依赖包？

      解决措施：如果项目中配置了包依赖，压缩掉依赖包会导致AGC找不到项目依赖包，上传时可以不压缩依赖包上传。

      参考链接：[远程三方包](../harmonyos-guides/ide-hvigor-dependencies.md#section0999112011818)。
    - 打app包时使用的DevEco Studio是否不是最新版本，导致打出的包AGC解析异常？

      解决措施：安装使用最新版本的DevEco Studio。
  + [错误码991](../app/agc-help-package-errorcode-0000002312513009.md#section522814356119)，表示非法软件包，按照下面步骤排查原因：
    - 是否错误上传了hap类型的包，app包和hap包存放路径不同，app包在工程目录的build/default/outputs下，hap包在entry模块build/default/outputs目录。
    - 检查签名和证书是否匹配，可以重新生成p12文件还有p7b和cer文件，然后再打包上传。
    - hap包的名字与pack.info中name值不同。
    - 在File > Project Structure > Project > Signing Configs窗口中，取消勾选"Automatically generate signature"（如果是HarmonyOS应用，请勾选"Support HarmonyOS"）然后配置工程的签名信息。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/7oPmgH5-SbuKfE_r6L42_g/zh-cn_image_0000002718889951.png "点击放大")
  + [错误码993](../app/agc-help-package-errorcode-0000002312513009.md#section411361491513)，表示Profile文件非法，出现此错误涉及多种原因，请根据[官网步骤](../app/agc-help-package-errorcode-0000002312513009.md#section411361491513)排查。若排查后依旧报错，可能有以下原因：
    - 工程级目录build-Profile.json5文件中可能配置了多个签名，需确保打包时使用的签名正确，即products下的signingConfig需为配置了发布证书、发布Profile的签名。
    - build-profile.json5文件中没有配置签名，而是在hvigorfile.ts内overrides重写加载签名。需要将签名写入build-profile.json5文件中。
  + [错误码1015](../app/agc-help-package-errorcode-0000002312513009.md#section1861774891113)，表示压缩包格式安全检查失败，按照下面步骤排查原因：
    - BuildApp打包生成的包后，不能修改包命名，修改包命名上传应用市场，会导致应用包安全检查失败。
    - 包里面可能存在exe之类的特殊文件。
    - 软件包被损坏，首先把软件包的扩展名改为zip，并解压其中的hap文件确保原始包没有问题，如果有问题，需要重新打包。
    - 传输过程中丢包导致被破坏，请检查网络连接状态以及代理设置是否影响连接，更换电脑和网络尝试。
  + [错误码996](../app/agc-help-package-errorcode-0000002312513009.md#section451313022017)，表示未知异常导致软件包解析失败，按照如下步骤排查原因。
    - 是否最新版本IDE。
    - 检查pack.info里面的packages里面的name和文件名是否一致。hap包的名字与pack.info中name值不同，需要更改hap包的名字与name相同。
    - base/media里面必须有保底的资源文件，比如图标，当resource下面其他目录有media类型的资源文件的情况下，必须保证base/media下面同目录的位置下也有一份。
    - 前面两步都没问题，也可以提供AppId，提[在线工单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/89?level2=101594901521145579)求助相关华为开发工程师。
  + [错误码7014](../app/agc-help-package-errorcode-0000002312513009.md#section9225124218158)，表示软件包内权限与Profile权限不一致。需要更改软件包内权限，或者重新生成Profile，使得hap包内权限与Profile权限一致。按照下面步骤排查原因。
    - 重新配置软件包内权限，删除Profile内没有的权限。
    - 若软件包内的权限是必须要用到的，则建议重新[申请Profile](../app/agc-help-release-profile-0000002248341090.md)，增加对应的权限。

      若Profile要申请特殊权限，可以参见[ACL权限](../app/agc-help-apply-acl-0000002394212138.md#section156171230179)。ACL权限为受限权限，仅部分场景允许申请使用。应用上架审核会根据您的使用场景对该权限进行审核，为了避免您的应用上架申请被驳回，请优先使用Picker/控件等系统机制替代相关权限使用。

      **说明** 

      单次可申请的ACL权限数量最多为10个。
  + [错误码999](../app/agc-help-package-errorcode-0000002312513009.md#section1070911435820)，表示上传的软件包使用的Profile类型错误。可能原因是软件包使用的是调试证书和调试Profile，上传应用市场时，需使用发布证书和发布Profile后重新上传。
  + [错误码7017](../app/agc-help-package-errorcode-0000002312513009.md#section154421017114817)，表示：软件包Profile版本不符合要求。出现此错误，表示软件包内的Profile版本不符合要求，请前往"证书、APP ID和Profile > Profile"页面重新下载Profile，然后重新打包上传。
  + [错误码7019](../app/agc-help-package-errorcode-0000002312513009.md#section14575111134518)，表示Profile文件非法。可能原因是当前共享库软件包内的Profile文件未申请AllowAppShareLibrary权限。若已申请权限，[申请新的Profile](../app/agc-help-release-profile-0000002248341090.md)，重新打包即可。
  + [错误码7021](../app/agc-help-harmonyoserror-0000001651912985.md#section17113329141212)，表示系统异常。可能原因是使用了不支持的字符串，如emoji表情，请删除再构建软件包。
  + [错误码7022](../app/agc-help-harmonyoserror-0000001651912985.md#section1936943132217)，表示当前软件包不支持上架到应用市场，In-house应用不支持上架到应用市场，请您确认软件包类型无误。
  + [错误码7023](../app/agc-help-harmonyoserror-0000001651912985.md#section198231451111115)，表示当前软件包不支持上架到应用市场，企业MDM应用不支持上架到应用市场，请您确认软件包类型无误。
  + [错误码7024](../app/agc-help-harmonyoserror-0000001651912985.md#section18589194601117)，表示当前软件包不支持上架到应用市场，企业应用不支持上架到应用市场，请您确认软件包类型无误。
  + [错误码7025](../app/agc-help-harmonyoserror-0000001651912985.md#section114444379357)，表示当前软件包不支持上架到应用市场。原因是使用了内部测试Profile打包。内部测试Profile用于发布内部测试应用，不支持上架到应用市场。如您需要将软件包上架到应用市场，请使用[发布证书](../app/agc-help-add-releasecert-0000001946273961.md)和[发布Profile](../app/agc-help-add-releaseprofile-0000001914714796.md)打包。
* **报错未返回错误码。**

  上传软件包，提示"软件包解析失败，请联系客服处理"，可能是软件包内资源文件的名称包含了/\*?|"<>字符或者名称的长度超过了100个字符，建议修改或者删除软件包内违规命名的资源文件后重新打包上传。

  上传软件包，提示"The bundle name xxx is already in use. Change and rebuild the .app bundle."，根因为包名已被其他团队占用。请在AppGallery Connect的"证书、APP ID和Profile > APP ID"下检查是否存在该包名，右上角可以切换团队查看。若确认所属团队有该包名但依旧报错，请提[在线工单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/89?level2=101594901521145579)求助。

## 常见FAQ

Q：重新生成Profile文件，增加权限重新生成Profile是否会对软件更新产生影响？

A：保证证书是通过同一个CSR文件生成的，即需要确保密钥库文件（.p12）不变的情况下更换证书与Profile并不会导致应用更新失败的问题。

**说明** 

更换证书需同时更新Profile文件。

Q：Profile为什么支持100个？用途是什么，使用在什么场景？

A：100个上限是我们的要求。应用不同版本可能权限不一样，以及Profile还承载了一些业务在里面，存在更新的场景，更新时老Profile得正常存在并生效。使用场景在手动配置签名及后续编译打包上架时会使用。

Q：若证书文件删除后，再次生成Profile文件，跟原来的是否一致？

A：不一致。Profile里面不仅仅有证书信息，还有其他信息。

Q：在生成.cer文件的时候，申请说选择25年及以上的有效期，指的是什么的有效期？

A：25年及以上有效期是指CSR文件。cer证书文件有效期为：调试证书有效期是180天，发布证书有效期是3年。证书失效后依赖证书生成的Profile同步失效。

Q：关于调试证书有效期的问题，是否可以延长调试证书的有效期？

A：证书设置有效期是用于动态验证应用来源合法性。目前实名认证开发者的调试证书有效期为180天，发布证书有效期为3年，未实名开发者的调试证书有效期为14天，证书过期后不可以延期，需要重新申请证书。

Q：上传更新包报错106，根据[版本升级错误码说明](../app/agc-help-update-errorcode-0000002322270833.md#section19598144518319)排查未修改module.json5，还有什么原因会导致该报错？

A：检查AppGallery Connect[配置支持设备](../app/agc-help-release-app-devicetype-0000002271592112.md)的勾选范围，确保其在升级包工程模块的module.json5文件中deviceTypes字段配置声明范围内。

Q：应用经检测含有【h.COLLECTOR.ClipboardLeaker.15[PUA]这类应用收集用户剪贴板数据，监听到剪贴板数据变化后，在用户无感知且未授权的情况下，将剪贴板数据通过网络或其他途径上传到远程服务器】病毒，不符合华为应用市场《审核指南》第2.19项。

A：[审核指南](../app/50104.md)识别为病毒是因为无条件外发。目前的整改方向需要调整为识别出特定格式才可以调接口或者在调接口前弹窗获取用户授权并且让用户知道自己的数据被使用的场景。

Q：软件包上传后页面一直转圈卡住，该如何处理，是否影响软件包上传？

A：软件包上传后会进行包体解析，页面显示解析中是现象正常，一般最高解析10分钟。解析过程是后台执行，可以停留在当前页面等待解析结果，或者切换其他页面，不影响软件包的解析，后续解析结果可以进入软件包管理页面查看。

Q：上传软件包时提示"上传的软件包与声明支持设备不一致"？

A：检查工程"entry"路径下，"module.json5"文件中的"deviceTypes"是否和AGC平台上应用支持的设备勾选的应用基本信息中支持的设备保持一致。如支持设备勾选手机，那么"module.json5"中"deviceTypes"需配置为"phone"。

Q：上传软件包时提示"软件包数量已达上限"？

A：AGC对每个应用有软件包数量限制，需手动清理。删除状态为"已过期"或"待优化"的旧软件包（优先保留正式上架版本）。

Q：应用无法提交，提示"授权书及其他材料"压缩包解析失败。

A：建议检查压缩包中是否存在除支持的图片格式（JPG、JPEG、BMP格式）文件外的其他格式文件，删除之后再进行上传。
