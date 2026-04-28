---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-convert
title: ohpm convert
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm convert
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:45+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:d88a57c2746e65e0d14d1d5400a445a5b088626da7da995ae245715ab9f2cfa6
---

将npm三方库转换为ohpm三方库。因为语法差异，转换时仅对文件进行格式转换，不修改原npm包的代码逻辑。若HAR包在转换后出现代码不兼容的报错，开发者需修改原npm包的代码做适配。

## 命令格式

```
1. ohpm convert [[<@group>/]<pkg>[@<version> | @tag:<tag>]] --registry <string> [--publish]
2. ohpm convert <node_modules_path> [--publish]
```

说明

* @group：三方库的命名空间，可选。
* pkg：三方库名称，必选。
* version：三方库的版本号，可选。
* tag：三方库的标签，标签会标记三方库的某个版本号，可选。

## 功能描述

将指定npm仓库中的某个包或者本地node\_modules目录下的包转换成满足ohpm格式要求的HAR包，并保存至当前工作目录，转换后的包将支持上传至ohpm-repo私仓或OpenHarmony三方库中心仓。

* ohpm convert @group/pkg@version --registry <npm仓库地址>

  下载指定仓库中的某个包及其所有依赖项，并且将该包及其依赖转换为满足ohpm格式要求的HAR包。
* ohpm convert <node\_modules\_path>

  转换本地node\_modules中的所有包为满足ohpm格式要求的HAR包，<node\_modules\_path>必须为npm执行install命令后生成的node\_modules目录。

  示例：

  ```
  1. ohpm convert ./xxxx/node_modules
  ```

说明

ohpm convert命令仅保留npm包中package.json配置文件中的name、version、main、types、license、description、author、keywords、homepage、repository、artifactType、dependencies、devDependencies、dynamicDependencies、overrides、scripts、hooks，module、packageType、typesVersions、exports和jsnext:main字段，具体字段说明请参考[oh-package.json5 字段说明](ide-oh-package-json5.md#zh-cn_topic_0000001792256137_oh-packagejson5-字段说明)。

## Options

### registry

* 默认值：无
* 类型：URL

可以在convert命令后面配置 --registry <registry> 参数，指定仓库地址。如果指定了--registry，convert命令将从远程仓库地址下载指定的包及其依赖后，进行转换处理。如果没有指定--registry，convert命令将从本地node\_modules目录进行转换处理。

### publish

* 默认值：false
* 类型： Boolean

可以在 convert命令后面配置 --publish 参数 ，若指定该参数，执行convert命令前请确认.ohpmrc推包相关配置无误，当所有包转换完成后将根据.ohpmrc中的配置依次进行推包。

### log\_level

* 默认值：无
* 类型： String

从ohpm 6.0.2.636版本开始，可以在convert命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型： Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

## 示例

**转换远程npm三方库中的包**

转换npm三方库中的axios包，执行以下命令：

```
1. ohpm convert axios --registry https://registry.npmjs.org/
```

结果示例：

```
1. PS C:\Users\xxxxx\Desktop> ohpm convert axios --registry https://registry.npmjs.org
2. ...
3. ohpm INFO: > start convert package: asynckit@0.4.0
4. ohpm INFO: > start convert package: axios@1.6.8
5. ohpm INFO: > start convert package: combined-stream@1.0.8
6. ...
7. ohpm INFO: A total of 9 packets are converted successfully.
8. ohpm INFO: Converted packages are saved to the "C:\Users\xxxxx\Desktop\convert_1712127991590" directory.
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/5hs4_HwtSN2ee4_5tc-Elg/zh-cn_image_0000002561833683.png?HW-CC-KV=V1&HW-CC-Date=20260427T235744Z&HW-CC-Expire=86400&HW-CC-Sign=F256B22C0E2FDF9200FEF2DE4BB5EACB2EF92A2BB6F7994D3B3C5E1BB1328D17 "点击放大")

**转换本地node\_modules目录中的包**

执行npm install uuid后，转换本地node\_modules目录中的包，执行以下命令：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/be0J1qLmSiGkNO_IwlsaNg/zh-cn_image_0000002561753703.png?HW-CC-KV=V1&HW-CC-Date=20260427T235744Z&HW-CC-Expire=86400&HW-CC-Sign=4F2562B739EDBD027AB690F0829840E3D73C1CDD25D0F1B03918A0E5FBF3924B)

```
1. ohpm convert C:\Users\xxxxx\Desktop\uuidInstallDir\node_modules
```

结果示例：

```
1. PS C:\Users\xxxxx\Desktop> ohpm convert C:\Users\xxxxx\Desktop\uuidInstallDir\node_modules
2. ohpm INFO: > start convert package: uuid
3. ...
4. ohpm INFO: A total of 1 package(s) are converted successfully.
5. ohpm INFO: Converted packages are saved to the "C:\Users\xxxxx\Desktop\convert_1712128912583" directory.
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/7cllvYI7SgKeIRC_BLvvmA/zh-cn_image_0000002530913760.png?HW-CC-KV=V1&HW-CC-Date=20260427T235744Z&HW-CC-Expire=86400&HW-CC-Sign=F0671A36ED844A572ABB9AD6503E02203BA68227576B39510AB12F9C5CF4F79B)
