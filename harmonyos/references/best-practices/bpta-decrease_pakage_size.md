---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-decrease_pakage_size
title: 应用包体积优化
breadcrumb: 最佳实践 > 性能 > 性能场景优化案例 > 资源与存储优化 > 应用包体积优化
category: best-practices
scraped_at: 2026-10-29T08:03:22+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:d8fb7e3da0b16f018fb444f69dc6dd05841b95d68cd8252ad7714badf00f9961
---

## 概述

减小应用包大小可以提升应用下载和安装体验。压缩、精简或复用代码和资源可以有效降低应用包体积。在优化包大小前，先了解HarmonyOS应用的[应用程序包结构](../harmonyos-guides/application-package-structure-stage.md)，对HAP、HAR、HSP等特点建立一定认知，然后使用扫描工具分析App包，根据报告优化应用。具体优化方法可以参考以下内容：

1. 对于含有so库的App工程，可以配置so库压缩选项，以减小应用包大小。
2. 在应用存在多包（HAP、HSP）的场景中，可以使用HSP动态共享包在多个包之间共享代码和资源。该方式可消除使用HAR静态共享包导致的代码和资源重复拷贝，从而减小应用包大小。

   但开发者需注意，大量使用HSP替代HAR会增加编译耗时和内存占用。因为在编译引用这些HSP共享包的模块时，会触发更多的语言编译任务。
3. 使用ohpm的override机制或开启 `[resolve\_conflict](../harmonyos-guides/ide-ohpmrc.md#section368717475562)` 解决依赖冲突，减少依赖包导致的重复编译问题。
4. 将不常用的功能作为按需加载的模块。

## 使用扫描工具分析App大小问题

[扫描工具](../harmonyos-guides/app-check-tool.md)可用于分析检测应用包，根据不同的参数设定，扫描指定路径的App、HAP、HSP包内容并输出检测结果报告，为开发者优化包结构或排查问题提供数据支撑。

根据扫描结果优化应用：

1. 重复文件

* 删除同一包内的重复资源。多包（HAP、HSP）间重复资源，可以使用HSP实现资源的复用，参考[多包情况下使用HSP共享代码及资源](bpta-decrease_pakage_size.md#section13745162092020)。

2. 较大文件

* 确认应用是否必需，是否可以删除。
* JPG、PNG、GIF等文件，可以考虑压缩图片。

3. 特定类型的文件

so文件，参考[配置so库压缩选项](bpta-decrease_pakage_size.md#section15826132851819)。

## 减小应用包大小的方法

### 配置so库压缩选项

应用安装包（HAP/HSP）中so库的存储方式由compressNativeLibs配置项控制，不仅影响应用包大小，还直接影响安装后的存储占用。HarmonyOS 7.0及以上版本支持安装包免解压能力，建议上架应用将compressNativeLibs配置为false以适配该能力。

**工作原理**

so库在应用包中可以压缩或非压缩存储。压缩存储时，编译出的应用包更小，但运行时需要未压缩的so库，安装时必须解压到安装目录，导致包内和安装目录存储冗余。非压缩存储时，HarmonyOS 7.0及以上支持安装包免解压能力，通过文件映射机制直接从包内加载，消除冗余。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/Jwyjw7rARoCdwOMbvI_BDg/zh-cn_image_0000002799032245.png "点击放大")

**配置方法**

修改应用模块配置文件module.json5中的compressNativeLibs字段，将值配置为false，重新编译、打包应用。

```screen
{
  "module": { 
    // ...
    
    "compressNativeLibs": false // Identify whether the so library is packaged in compressed storage. 'true' means compressed so library, 'false' means non-compressed. 
  }
}
```

两种配置在编译包大小、安装后大小及适用场景上的对比如下表所示。下载包大小方面，应用市场会对上架包再次压缩，两种配置下大小基本持平。

| 配置项 | 编译包大小 | 安装后大小 | 适用场景 |
| --- | --- | --- | --- |
| compressNativeLibs: false | 较大（so库原始大小存储） | 1. HarmonyOS 7.0及以上版本：较小（免解压，仅一份）  2. HarmonyOS 7.0以下版本：最大（两份均为原始大小） | 推荐配置，适配免解压能力 |
| compressNativeLibs: true | 较小（so库压缩存储） | 较大（包内 + 安装目录两份冗余） | 1. 编译包大小接近上架上限4GB  2. 预装应用（只读分区，无法随应用卸载删除） |

以一个libs体积约700MB的示例工程为例，配置"so压缩"（左图）因解压产生冗余导致安装后占用更大，而配置"so不压缩"（右图）借助免解压机制仅保留一份，占用反而更小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/U5De6uSWSzmraLPATozgvw/zh-cn_image_0000002769879828.png "点击放大")

### 解决依赖冲突，减少依赖包重复编译

对于ohpm 1.5.0之前的版本，如果hap依赖了不同版本的har（例如下图中的V1版本的harC和V2版本的harC），默认情况下，V1和V2两个版本的harC都会被打包到hap中。开发者可以使用ohpm的override机制，指定只打包一个版本。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/WFxb--VzTDGgVSByw6LGeg/zh-cn_image_0000002194011048.png "点击放大")

如果使用的是ohpm 1.4.0 版本，可以使用override机制，开发者可以在项目级别的 oh-package.json5 （即项目根目录下的 oh-package.json5）文件中添加 overrides 配置，将依赖树中的依赖替换为另一个版本。替换的版本既可以是一个具体的版本号，也可以是本地存在的HAR包或源码目录。

**注意：**

必须在项目级别的 oh-package.json5 中配置 [overrides](../doccenter-deveco-studio/ide-oh-package-json5.md#section13977152601510)，配置在模块级别的 oh-package.json5 中不会生效。

例如，这里以 'foo' 库为例，如果在项目中始终需要使用'1.0.0'版本，可在项目级的 oh-package.json5 中添加以下配置：

```screen
{
  "overrides": {
    "foo": "1.0.0"
  }
}
```

若本地存在 foo 的源码或 HAR 包，确保 foo 始终使用本地版本，可在项目级 oh-package.json5 中进行如下配置：

1. 本地存在"foo"的源码，即配置项目根目录下的foo目录，以"file:./foo"标识其路径。

```screen
{
  "overrides": {
    "foo": "file:./foo"
  }
}
```

2. 本地存在"foo.har"的HAR包，其存放在libs目录下，即配置"file:./libs/foo.har"。

```screen
{
  "overrides": {
    "foo": "file:./libs/foo.har"
  }
}
```

对于1.5.0版本之后的ohpm，可以通过开启`[resolve\_conflict](../harmonyos-guides/ide-ohpmrc.md#section368717475562)`，自动解决依赖冲突。依赖冲突的处理策略为：当项目同时依赖某个三方库的不同版本时，ohpm会选择其中的最高版本进行安装。

### 按需分发

对于应用中用户不常用的功能，可以考虑通过[产品特性按需分发](../harmonyos-guides/store-moduleinstall.md)的方式，将下载时机交由用户选择，使用时从应用市场获取安装，减少用户初次下载的包大小。

### 多包场景下使用HSP共享代码和资源

当前系统提供了两种共享包：HAR静态共享包和HSP动态共享包。二者都用于实现代码和资源的共享，可以包含代码、C++库、资源和配置文件。

HAR中的代码和资源跟随使用方编译，多个使用方会存在多份相同拷贝。HSP中的代码和资源独立编译，在运行时进程中只存在一份。

在多包场景下，如果多个HAP或HSP包使用HAR包共享代码和资源，打包后每个包都会包含HAR包的拷贝。这就是App包中存在冗余代码和资源的原因。

如下图示例：应用模块HAP1和HAP2/HSP1都引用了HAR2和HAR3。打包后，HAR2和HAR3在App包中有多份重复拷贝，导致体积较大。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/Fgpliw4aQG-15r1S8sL_0w/zh-cn_image_0000002229451341.png "点击放大")

推荐使用HSP代替HAR实现代码和资源共享。如下图示例，使用HSP2对原应用进行升级改造，打包后，APP包中HAR2和HAR3仅保留一份拷贝。当HAR2和HAR3的总大小超过HSP时，可以减小应用包大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/okIB2x9XQEqP_1WN8dFLZg/zh-cn_image_0000002229336845.png "点击放大")
