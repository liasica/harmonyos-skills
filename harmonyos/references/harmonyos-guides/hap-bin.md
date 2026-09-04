---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hap-bin
title: 应用程序包集成bin文件（PC/2in1）
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 典型场景的开发指导 > 应用程序包集成bin文件（PC/2in1）
category: harmonyos-guides
scraped_at: 2026-09-05T06:13:44+08:00
doc_updated_at: 2026-08-03
content_hash: sha256:2636788e156b75e05b30abb4304b38fb320050308acb811b823d053c70e91b27
---

从API版本24开始，HAP包支持集成、加载并独立运行bin文件，有效拓展了应用的能力边界。开发者可在标准HAP应用内嵌入各类平台二进制工具与可执行程序，依托HarmonyOS运行时环境完成程序调度、脚本解析与任务执行，弥补无法直接调用本地化二进制工具的短板。基于此能力，应用可实现外部脚本解析、第三方工具调用等扩展功能；同时，bin文件的运行全程受系统安全机制管控，兼顾功能拓展性与系统安全性。

## 基本概念

* bin文件：二进制程序文件，是ELF格式的可执行程序文件。
* ELF文件的节：ELF格式文件中用于承载二进制内容的基本单元。

## 权限管控

与[应用权限管控](app-permission-mgmt-overview.md)相似，当应用包内集成的bin文件在运行时需要使用受权限保护的系统能力（例如，加载二进制证书签名的共享库）时，需要声明相应权限。声明后，bin文件在运行过程中可获得授权，在使用受保护的系统能力时不会被权限管控拦截。

### 声明bin文件的权限

bin文件的权限声明存放在二进制程序文件的.permission节中。当bin文件被集成的应用执行时，系统会根据该节中声明的权限进行授权。

1. .permission节内容

   .permission节中存放JSON格式的权限声明数据：

   | **属性名称** | **含义** | **数据类型** | **是否可缺省** |
   | --- | --- | --- | --- |
   | requestPermissions | 二进制程序声明的权限列表。 | Array<RequestPermission> | 是；缺省时表示该二进制程序不声明权限。 |
2. RequestPermission标签

   | **属性名称** | **含义** | **数据类型** | **是否可缺省** |
   | --- | --- | --- | --- |
   | name | bin文件所需使用的权限名称。 | string | 是；缺省时表示该二进制程序不声明权限。 |

   **说明** 

   1. 标签中声明的权限名称需要与[系统中应用权限](app-permissions.md)名称一致，若不一致则会导致该标签的权限声明无效。
   2. bin文件声明的权限不能超过集成它的应用声明的权限，否则在安装时会失败。
3. .permission节示例

   例如，需要给bin文件声明权限ohos.permission.A、ohos.permission.B、ohos.permission.C，可以按照如下格式编写.permission节内容：

   **说明** 

   下述json样例中的permission名称仅为示例，开发者在使用时，需要根据应用权限列表，配置真实可用的权限名。

   ```json
   {
     "requestPermissions": [
       {
         "name": "ohos.permission.A"
       },
       {
         "name": "ohos.permission.B"
       },
       {
         "name": "ohos.permission.C"
       }
     ]
   }
   ```

### bin文件在安装与启动加载时的权限管理

在安装集成了bin文件的HAP时，系统会校验HAP内bin文件声明权限的合法性。

对于权限声明合法且完成安装的bin文件，系统在bin文件启动加载时为其授予声明的权限，在权限使能后，bin文件可在运行时使用受该权限保护的受控系统能力。

应用内集成的bin文件随HAP安装到设备，安装过程中需满足以下条件：

1. bin文件声明的权限不能超出集成它的HAP应用声明的权限，否则会导致整体HAP安装失败；
2. bin文件中若存在.permission节，则要求.permission节内容是一个合法的json格式，否则会导致集成它的HAP应用安装失败。

**权限范围**

1. 系统已开放[应用权限](app-permissions.md)供应用及bin文件使用。bin文件可获取声明的[授权方式](app-permission-mgmt-overview.md#授权方式)为[system\_grant](app-permission-mgmt-overview.md#system_grant系统授权)，且[权限APL等级](app-permission-mgmt-overview.md#权限机制中的基本概念)为normal、system\_basic、system\_core的所有权限；
2. 应用内集成的bin文件声明的权限不能超过集成它的HAP应用声明的权限，否则在安装时会失败。

**权限继承**

系统为应用内集成的bin文件提供了继承父进程权限的机制，bin文件可在其权限声明中增加继承权限“[ohos.permission.INHERIT\_PARENT\_PERMISSION](permissions-for-all.md#ohospermissioninherit_parent_permission)”，在bin文件声明该权限后，其启动加载时可以获取到父进程的授权方式为system\_grant，且权限级别为normal、system\_basic、system\_core的所有权限。

**说明** 

[ohos.permission.INHERIT\_PARENT\_PERMISSION](permissions-for-all.md#ohospermissioninherit_parent_permission)权限本身不会被子进程继承。

## 在HAP中集成bin文件

bin文件被拉起后，如需使用受保护的系统能力，应独立声明自身所需的权限。

**说明** 

若bin文件运行时不需要使用受权限保护的系统能力，则bin文件无需声明权限，可跳过本小节。

参考[声明bin文件权限](hap-bin.md#声明bin文件的权限)，为bin文件EXAMPLE添加.permission节并声明所需权限。同时，HAP的配置文件module.json5中也需声明相同的权限。

由于bin文件为ELF格式，添加.permission节的方式有多种，本文提供以下两种参考方法：

1. 使用objcopy命令工具

   通过objcopy --add-section命令为bin文件添加.permission节，命令格式如下：

   ```text
   objcopy --add-section .permission=<file> input output
   ```

   参数说明：

   | **参数** | **说明** |
   | --- | --- |
   | -file | 内容将作为.permission节的文件 |
   | -input | 需要添加.permission节的二进制文件 |
   | -output | 添加.permission节后输出的二进制文件 |

   示例：

   为bin文件EXAMPLE添加.permission 节，节内容取自module.json，输出文件为EXAMPLE\_OUT：

   ```text
   objcopy --add-section .permission=module.json EXAMPLE EXAMPLE_OUT
   ```

   [Command Line Tools](ide-commandline-get.md)内置了对objcopy命令的支持，开发者也可选用其他objcopy工具。

   **说明** 

   使用不同来源的objcopy工具可能导致bin文件结构被破坏（如Windows版本的llvm-objcopy工具），进而引发加载时出现预期外的问题。建议在执行objcopy操作后，比对文件大小等属性，确认与原始文件是否存在差异。
2. 使用签名工具binary-sign-tool

   [binary-sign-tool](binary-sign-tool.md)签名工具用于在PC/2in1设备上对bin文件进行签名，并支持为其添加.permission 节。

   在[签名命令](binary-sign-tool.md#签名命令sign)中，-moduleFile参数所指定的文件即为需要添加到bin文件 .permission节内容。

### 在HAP工程中声明bin文件

在HAP工程entry目录下增加libs{abi}目录，{abi}值需要与HAP部署的设备abi类型保持一致。随后，将添加了.permission节的bin文件EXAMPLE放置在该目录下。

例如，需要将HAP部署在abi类型为arm64-v8a的PC/2in1设备上时，bin文件EXAMPLE应放置在如下目录：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/54i9x_8bT3iK3XzkJgSMBw/zh-cn_image_0000002712403202.png)

在[module.json5](module-configuration-file.md)中配置[executablebinarypaths标签](module-configuration-file.md#executablebinarypaths标签)，用于声明HAP中包含的可执行bin文件。该标签配置bin文件的路径，为相对路径，必须以libs/{abi}/为前缀，其中{abi}为设备CPU架构类型（如arm64-v8a、x86\_64、armeabi-v7a）：

```json5
{
  "module": {
    // ...
    "executableBinaryPaths": [
      {
        "path": "libs/arm64-v8a/EXAMPLE"
      }
    ],
    // ...
  },
}
```

### 编译与打包HAP

将bin文件集成至HAP包中，需完成以下配置：

1. HAP配置为解压模式

   在[module.json5](module-configuration-file.md)中配置extractNativeLibs标签为true，使应用安装时自动将libs库解压至安装目录，从而确保bin文件可正常加载运行。
2. HAP配置libs库打包选项

   参考[nativeLib字段](ide-hvigor-cpp.md#section15889929155720)，在bundle-profile.json5中配置collectAllLibs标签为true，使bin文件可被打包进HAP中，示例如下：

   ```json5
   {
   // ...
     "buildOptionSet": [
       {
         "name": "debug",
         "nativeLib": {
           "collectAllLibs": true,
         }
       }
     ],
     // ...
   }
   ```
3. debug包strip标签配置问题

   在开发调试场景下，debug包需要作额外配置。参考[配置CPP](ide-hvigor-cpp.md)中[debugSymbol标签](ide-hvigor-cpp.md#section2182144382320)，该标签用于移除.so文件中的符号表、调试信息。debugSymbol在模块级build-profile.json5配置示例如下：

   ```json5
   {
   // ...
     "buildOptionSet": [
       {
         "name": "debug",
         "nativeLib": {
           "collectAllLibs": true,
           "debugSymbol": {
             "strip": false,
             "exclude": []
           }
         }
       }
     ],
   }
   ```

   以上配置完成后，启动编译HAP，DevEco Studio会在编译过程中将bin文件打包进入HAP工程。
4. 快速获取配置项中的二进制

   当需将大量bin文件写入executableBinaryPaths字段时，若已设置collectAllLibs为true，可使用以下插件实现自动写入（下面插件在hap模块的hvigorfile.ts中配置）:

   ```ts
   // ...
   // 获取当前hvigorNode节点对象
   const node: HvigorNode = getNode(__filename);
   hvigor.nodesEvaluated(async () => {
     node.registerTask({
       name: 'default@CustomTask',
       run() {
         // 获取hap模块上下文信息
         const context = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
         // 获取构建产物根目录路径
         const buildProductRoot = context.getBuildProductRootPath();
         // 拼接module.json文件的完整路径，该文件包含模块的可执行文件配置
         const moduleJsonPath = path.resolve(buildProductRoot, 'build/${product}/intermediates/package/${target}/module.json');
         if (!fs.existsSync(moduleJsonPath)) {
           return;
         }
         // 读取并解析module.json文件内容为JSON对象
         const jsonContent = FileUtil.readJson5(moduleJsonPath);
         // 拼接libs目录的基础路径，该目录下存放编译后的库文件
         const libsBasePath = path.resolve(buildProductRoot, 'build/${product}/intermediates/libs/${target}');
         // 调用函数处理ELF文件，将可执行文件路径添加到module.json中
         processElfFiles(jsonContent, moduleJsonPath, libsBasePath);
       },
       dependencies: ['entry:default@GeneratePkgModuleJson'],
       postDependencies: ['entry:default@ProcessCompiledResources'],
     });
   });
   // ...
   ```

## 安装含bin文件的HAP

集成bin的HAP包无独立安装包，依托标准HAP包完成安装部署。其内嵌的二进制程序、脚本资源随HAP包一并安装至设备，安装流程与常规应用一致。应用安装后，bin文件文件自动解压至应用安装目录：

```text
/data/app/el1/bundle/public/<bundleName>
```

1. 通过DevEco Studio直接安装

   适用于开发阶段快速调试。开发者完成工程编译后，通过DevEco Studio连接设备并点击运行安装。工具自动将包含bin资源与脚本文件的HAP包推送至设备，并完成解压与安装。
2. 通过HDC命令安装

   适用于批量部署、自动化测试、离线安装场景。通过调试工具HDC执行安装命令，完成包含bin资源的HAP包的安装。

   核心操作流程：首先通过HDC连接设备，确认设备连接状态正常，随后执行HAP安装命令（hdc install）。
