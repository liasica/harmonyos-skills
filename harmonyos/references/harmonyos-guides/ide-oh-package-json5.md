---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-oh-package-json5
title: oh-package.json5
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > oh-package.json5
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7a0f7783b76e770eee4098f4557dd94e50cd7df33fd3277e77eb403ee9b91cb9
---

从OHPM 5.0.0版本开始，支持区分工程级与模块级oh-package.json5配置。其中：

* 工程级oh-package.json5文件：位于工程根目录下，主要用来描述全局配置，如：依赖覆盖（overrides）、依赖关系重写（overrideDependencyMap）和参数化配置（parameterFile）等，详情请见：[工程级oh-package.json5 字段说明](ide-oh-package-json5.md#section02162312018)；
* 模块级oh-package.json5文件：位于工程各个模块的根目录下，用来描述包名、版本、入口文件（类型声明文件）和依赖项等信息，详情请见：[模块级oh-package.json5 字段说明](ide-oh-package-json5.md#zh-cn_topic_0000001792256137_oh-packagejson5-字段说明)。

开发者可将标准的DevEco Studio工程下的各个模块打成HAR包后，发布到OpenHarmony三方库中心仓；所有发布到仓库的包必须包含模块级oh-package.json5文件，以描述当前包基本信息。

## 工程级oh-package.json5字段说明

| 配置项 | 字段名称 | 字段说明 | 字段要求 | 字段类型 | 默认值 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| **开发态版本** | modelVersion | 开发态版本号 | **必选** | 字符串 | 无 | 开发态版本号。  默认版本号为DevEco Studio配套的modelVersion，以[DevEco Studio 6.1.1 Release](../harmonyos-releases/deveco-studio-new-features-611.md#section1376764215234)为例，配套的modelVersion为"6.1.1"。如需修改modelVersion，修改后的值不能小于5.0.0，且不能大于DevEco Studio配套的modelVersion。 |
| **描述配置** | description | 简介 | 可选 | 字符串 | 无 | 用于描述工程信息的字符串。 |
| **依赖配置** | dependencies | 生产依赖 | 可选 | 对象 | {} | 用于配置参与编译/运行阶段使用的依赖，声明需要在代码中import的三方库（不建议在工程级oh-package.json5中配置生产依赖）。 |
| devDependencies | 开发依赖 | 可选 | 对象 | {} | 配置开发态依赖，配置只能参与项目的开发或测试阶段的依赖。如果被依赖的组件最终要与依赖的组件一起发布到目标机器（如手机）上使用，则不能在其中配置。 |
| dynamicDependencies | 动态依赖 | 可选 | 对象 | {} | 配置项目动态依赖的HSP模块。在开发者需要动态加载HSP的时候配置使用（不建议在工程级oh-package.json5中配置动态依赖）。 |
| overrides | 依赖覆盖配置 | 可选 | 对象 | {} | 支持将依赖树中的包替换为另一个指定版本，详情见[overrides](ide-oh-package-json5.md#zh-cn_topic_0000001792256137_overrides)。 |
| overrideDependencyMap | 重写依赖关系 | 可选 | 对象 | {} | 支持将依赖树中包的子依赖替换为配置文件中配置的依赖，详情见[overrideDependencyMap](ide-oh-package-json5.md#section106151513236)。 |
| exclusions | 第三方依赖的子依赖排除配置 | 可选 | 对象 | {} | 支持移除第三方依赖（远程依赖、本地文件依赖）中的一个或多个子依赖，详情见[exclusions](ide-oh-package-json5.md#section18586313199)。 |
| **其他** | scripts | 自定义脚本 | 可选 | 对象 | {} | 维护一个脚本别名到脚本内容的映射表，开发者可以通过ohpm run <脚本别名>来触发对应脚本内容的执行。 |
| hooks | 钩子 | 可选 | 对象 | {} | 安装或卸载的钩子设置，包含 "preInstall"，"postInstall"，"preUninstall"，"postUninstall"，"preVersion"，"postVersion"，"prePublish"，"postPublish" 字段。仅支持执行当前工程中的 hooks，不支持执行依赖中的 hooks。 |
| parameterFile | 参数化配置文件路径 | 可选 | 字符串 | 无 | 标识是否开启参数化。未配置：关闭参数化；已配置：开启参数化。需同时指定参数化配置文件路径，详情见[parameterFile](ide-oh-package-json5.md#section122411462820)。 |
| properties | 多环境依赖管理参数 | 可选 | 对象 | {} | 该配置参数用于多环境下的依赖管理。  开发者通过parameterFile完成依赖配置后，在parameterFile字段中使用properties参数，详情见[properties](ide-oh-package-json5.md#section12230213121314)。  说明：  如debug和beta环境下需要配置不同的parameterFile，实现不同的包依赖管理，诸如此类场景称为多环境。 |

**注意** 

不建议在工程级依赖中配置非devDependencies的依赖，即一个Hsp/Har模块的非开发态依赖都要在相应模块的dependencies和dynamicDependencies中声明。

## 模块级oh-package.json5字段说明

模块级oh-package.json5文件位于工程各个模块的根目录下，用来描述当前模块被其他模块依赖时的相关信息，包括：作为依赖时的依赖名（name）、作为依赖时的版本号（version）、入口文件（main/types）和子依赖项等信息。

| 配置项 | 字段名称 | 字段说明 | 字段要求 | 字段类型 | 默认值 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| **描述配置** | name | 名称 | 必选 | 字符串 | 无 | 该模块作为依赖时的依赖名，用于唯一标识该依赖。  格式为：@group/packagename或packagename，长度：[1, 128]，全局唯一，即一个应用中，不同依赖的依赖名不能重复。建议name命名时包含组织名称group，便于管理和识别三方依赖。  name中只有在存在组织名称group时，才能有且仅能有一个'@'符号，有且仅有一个路径分隔符'/'。  **组织名称group格式：**  1、仅允许以小写字母开头，可由小写字母、数字、中划线（-）、下划线（\_）组成。  2、禁止以中划线（-）、下划线（\_）结尾。  3、不允许为ArkTS 的保留关键字。  **packagename格式：**  1、仅允许以小写字母开头，可由小写字母、数字、点（.）、中划线（-）、下划线（\_）组成。  2、禁止以点（.）、中划线（-）、下划线（\_）结尾。  3、不允许为ArkTS的保留关键字。 |
| version | 版本号 | 必选 | 字符串 | 1.0.0 | 该模块构建产物（HAR/HSP）的版本号。  规范：采用X.Y.Z（主版本.次版本.修订号）三段式结构，遵循 [semver](https://semver.org/) 语义化规范，从1.0.0开始。 |
| description | 简介 | 可选 | 字符串 | 无 | 用于描述该模块构建产物（HAR/HSP）的信息，有助于被搜索发现。长度范围为0-512字符。 |
| keywords | 关键字 | 可选 | 数组 | [] | 关键字信息数组，便于搜索使用。例如：["tools", "project"]。 |
| author | 作者 | 可选/必选 | 对象或字符串 | 无 | author包含 name 字段（必选）、 email 字段（可选）、url字段（可选），可通过格式对象或字符串格式配置。  name字段允许使用字母、数字，点（.），中划线（-），下划线（\_），空格，中文，长度范围为[1,128]，email长度范围为[1,64]，url长度范围为[1,256]。  * 对象格式："author": {"name": "xxx" , "email": "\*\*\*@example.com" , "url": "https://xxx.com" }。 * 字符串格式："author": "name<\*\*\*@example.com>(https://xxx.com)"。  仅发布到[OpenHarmony三方库中心仓](https://ohpm.openharmony.cn/)时，必须填写，其他场景可选填。 |
| homepage | 主页链接 | 可选 | 字符串 | "" | 通常是项目gitee链接。 |
| repository | 仓库地址 | 可选 | 字符串 | "" | 开源代码仓库地址。在私仓管理界面的系统设置处可定义是否为必填。 |
| license | 开源协议 | 可选/必选 | 字符串 | "ISC" | 当前项目的开源许可证。遵循 [spdx license](https://spdx.org/licenses/) 规范。许可证若为 GPL，repository 建议不为空。  仅发布开源三方库到[OpenHarmony三方库中心仓](https://ohpm.openharmony.cn/)时，必须填写，其他场景可选填。 |
| **依赖配置** | dependencies | 生产依赖 | 可选 | 对象 | {} | 用于配置参与编译/运行阶段使用的依赖，声明需要在代码中import的三方库（参与编译/运行阶段使用的依赖）。 |
| devDependencies | 开发依赖 | 可选 | 对象 | {} | 用于配置开发态依赖，只能参与项目的开发或测试阶段。如果被依赖的组件最终要与依赖的组件一起发布到目标机器（手机）上使用，则不能在其中配置。通过devDependencies引入的依赖，不校验循环依赖。 |
| dynamicDependencies | 动态依赖 | 可选 | 对象 | {} | 用于配置项目动态依赖的HSP模块。在开发者需要动态加载HSP的时候配置使用。 |
| **文件配置** | main | 入口 | 必选 | 字符串 | 无 | 指定加载的入口文件。 |
| types | 类型定义 | 可选 | 字符串 | "" | 指定类型定义的文件名。当用 typescript 定义新的类型，需要提供给其他开发者使用，则需要指定其声明文件，一般为 .d.ts，.d.ets 文件。 |
| oh-exports | 控制导出模块 | 可选 | 对象 | {} | 通过oh-exports字段控制导出模块中文件，实现包的可见性控制。支持导出目录文件（导出时不校验文件，全量导出目录内容）和特定后缀文件（ets/ts/js）。详情见[oh-exports](ide-oh-package-json5.md#section203908482324)配置示例。 |
| **兼容性检测相关配置** | compatibleSdkVersion | SDK版本 | 可选 | 字符串 | 无 | 三方库开发者使用的SDK版本，构建时由Hvigor自动填充，提供给SDK做兼容性检测。  在prepublish、publish时，ohpm会对该字段进行检测（非空和长度校验），并根据.ohpmrc中开关 [compability\_log\_level](ide-ohpmrc.md#section96369529419)配置的值进行提示或报错处理。  详情见[兼容性字段配置示例](ide-oh-package-json5.md#section194621247204911)。 |
| compatibleSdkType | SDK类型 | 可选 | 字符串 | 无 | 三方库开发者使用的SDK类型，构建时由Hvigor自动填充，提供给SDK做兼容性检测, 示例值："OpenHarmony"、"HarmonyOS"。  在prepublish、publish时，ohpm会对该字段进行检测（非空和长度校验），并根据.ohpmrc中开关 [compability\_log\_level](ide-ohpmrc.md#section96369529419)配置的值进行提示或报错处理。  详情见[兼容性字段配置示例](ide-oh-package-json5.md#section194621247204911)。 |
| obfuscated | 混淆标识 | 可选 | 布尔 | 无 | 三方库是否开启混淆标识，构建时由Hvigor自动填充，提供给SDK做兼容性检测。  在prepublish、publish时，ohpm会对该字段进行检测（非空校验），并根据.ohpmrc中开关 [compability\_log\_level](ide-ohpmrc.md#section96369529419)配置的值进行提示或报错处理。  详情见[兼容性字段配置示例](ide-oh-package-json5.md#section194621247204911)。 |
| nativeComponents | native so依赖配置 | 可选 | 数组 | 无 | 三方库使用的so包配置，构建时由Hvigor自动填充，提供给SDK做兼容性检测。  对于用户自行引入的so依赖（存放于libs目录），需要用户手动维护该数组，数组单个元素类型为对象，对象内可配置的字段有：name、compatibleSdkVersion、compatibleSdkType。  在prepublish、publish时，如果包内存在so包，则ohpm会对该字段进行检测，并根据.ohpmrc中开关 [compability\_log\_level](ide-ohpmrc.md#section96369529419) 配置的值进行提示或报错处理；反之则不检测该字段。  详情见[兼容性字段配置示例](ide-oh-package-json5.md#section194621247204911)。 |
| **其他** | artifactType | 类型 | 可选 | 字符串 | "original" | OpenHarmony包制品类型，有两个选项：original、obfuscation。original：源码，即发布源码（.ts/.ets）；obfuscation：混淆代码，即源码经过混淆之后发布上传。 |
| scripts | 自定义脚本 | 可选 | 对象 | {} | 维护一个脚本别名到脚本内容的映射表，开发者可以通过ohpm run <脚本别名>来触发对应脚本内容的执行。 |
| hooks | 钩子 | 可选 | 对象 | {} | 安装或卸载的钩子设置，包含 "preInstall", "postInstall", "preUninstall", "postUninstall","preVersion", "postVersion", "prePublish", "postPublish" 字段。仅支持执行当前工程中的 hooks，不支持执行依赖中的 hooks。 |
| category | 检查规则白名单 | 可选 | 字符串 | {} | 在私仓管理界面配置后自动生成，白名单为分号隔开的字符串列表，每个列表项必须是一个由大小写字母或下划线组成的字符串，包含在白名单中的配置项，不再做规则检查。 |
| packageType | 包类型 | 可选 | 字符串 | InterfaceHar | 标识模块是否为HSP包，在新建Shared Library时会自动生成该字段，并默认赋值为"InterfaceHar"；Static Library中没有该字段，表示为普通HAR包。 |
| dependencyMode | BundledHar类型 | 可选 | 字符串 | loose | 该字段由编译构建自动生成，不推荐开发者手动配置。  用于标识当前HAR包编译时是否开启[bundledAllDependencies](ide-hvigor-build-har.md#section121297571296)。若开启填入bundled，若未开启填入loose或缺省。  三方中心仓仅支持bundled和loose两种取值，其他取值会导致校验失败。 |

**注意** 

**依赖名使用要求：**

1、在oh-package.json5文件中dependencies、devDependencies、dynamicDependencies节点声明本地依赖时，允许配置的依赖名和依赖包的包名（即包内oh-package.json5中配置的name）不一致，但不推荐该用法，在默认情况下ohpm会通过告警日志来提示此类问题。

若希望将告警升级为报错并中断命令执行，可以通过在.ohpmrc中配置[enforce\_dependency\_key](ide-ohpmrc.md#section920325116547)=true；或在项目级[build-profile.json5](ide-hvigor-build-profile-app.md)文件中将strictMode字段下配置useNormalizedOHMUrl=true。

2、使用[参数化配置](ide-oh-package-json5.md#section122411462820)时，依赖名和依赖包的包名（即包内oh-package.json5中配置的name）必须保持一致，否则会报错并中断命令执行。

3、在oh-package.json5、overrideDependencyMap、parameterFile文件中，不建议使用无效的转义字符（例如：\a、\e、\o等）或Unicode编码（例如：\uxxxx）。

## 兼容性字段配置示例

三方库开发者使用的SDK和当前集成该三方库工程编译时使用的SDK可能存在不一致的情况。因此，ohpm新增了兼容性检测相关配置以帮助SDK做兼容性分析。配置示例如下：

```screen
{
  "name": "library",
  "version": "1.0.0",
  "description": "Please describe the basic information.",
  "main": "Index.ets",
  "license": "Apache-2.0",
  "dependencies": {
    "liblibrary.so": "file:./src/main/cpp/types/liblibrary"
  },
  "compatibleSdkVersion": "12",
  "compatibleSdkType": "HarmonyOS",
  "obfuscated": false,
  "nativeComponents": [
    {
      "name": "liblibrary.so",
      "compatibleSdkVersion": "12",
      "compatibleSdkType": "HarmonyOS"
    }
  ]
}
```

## 创建一个新的oh-package.json5文件

通过命令行创建 oh-package.json5文件，执行如下命令：

1. 导航到包的目录。

   ```screen
   cd /path/to/package
   ```
2. 执行初始化命令，并按照问卷填写相关参数。

   * 对无命名空间模块，执行以下命令：

     ```screen
     ohpm init
     ```
   * 对有命名空间模块，执行以下命令：

     ```screen
     ohpm init --group group_name
     ```
3. 若跳过问卷填写，创建默认文件，可在初始化命令行加上配置参数 --yes。

   ```screen
   ohpm init --yes
   ```

   默认创建的oh-package.json5 文件示例：

   ```screen
   {
    "name": "package_name",
    "version": "1.0.0",
    "description": "",
    "main": "index.ts",
    "author": "",
    "license": "ISC",
    "dependencies": {}
   }
   ```

## 依赖配置说明

ohpm 存在 dependencies，devDependencies和dynamicDependencies 三种依赖类型。同时支持具体版本号，范围版本号，tag标签，本地har/tgz文件路径、本地源码目录和使用@module通过模块名指向模块目录（示例："module\_key": "@module:module\_name"）多种方式引入依赖。当依赖的三方库版本号配置为 \* 时，表示当前依赖的包版本为该三方库的最新包版本。

**说明** 

1、从DevEco Studio 6.0.0 Beta1开始支持@module配置方式；从DevEco Studio 6.0.2 Beta1开始，通过devDependencies引入的依赖，不校验循环依赖。

2、@module配置中，module\_name必须在project/build-profile.json5文件或者project/.hvigor/dependencyMap/dependencyMap.json5（hvigor生成）文件的modules节点下存在。

3、@module配置中，module\_key需和"@module:module\_name"指向的模块目录下oh-package.json5文件中配置的name一致。

1. dependencies：生产依赖，即参与编译/运行阶段使用的依赖，用来定义生产态HAR/HSP包依赖，声明在代码中被 import的三方库。如果被依赖的组件最终要与依赖的组件一起发布到目标机器（手机）上使用，则必须配置。
2. devDependencies：开发态依赖，只能参与项目的开发或测试阶段的依赖。如果被依赖的组件最终要与依赖的组件一起发布到目标机器（如手机）上使用，则不能配置在该字段中。通过devDependencies引入的依赖，不校验循环依赖。
3. dynamicDependencies：动态依赖，用来配合[动态import](arkts-dynamic-import.md)，表达动态 import 使用的HSP 包依赖。动态依赖不会在加载时就被编译，而是根据条件导入模块或者按需导入模块，具有更高效的依赖加载速度。
4. 依赖配置示例：

   ```json5
   {
     "dependencies": {
       // 具体版本号引入，支持符合semver标准的版本号
       "specific_version": "1.0.0",

       // 范围版本号引入，^引入1.x.x的最新版本，~引入1.0.x的最新版本。范围版本优先选取正式版本，无匹配的正式版本才会选取先行版本
       "scope_version": "^1.0.1",

       // tag标签引入，示例引入标签为"beta"对应的版本号
       "tag_version": "tag:beta",

       // 本地文件引入，可引入本地har/tgz文件
       "local_file": "file:./xx.har",

       // 本地源码引入，可引入本地其他模块的源码，示例直接引入本地的"module1"模块
       "local_source_code": "file:../module1"

       // 项目存在Foo模块，即build-profile.json5文件或dependencyMap.json5文件中modules节点下存在名称为Foo的模块；该模块Foo的oh-package.json5中name为：foo_test
       "foo_test": "@module:Foo"
     },
     "devDependencies": {
       // 支持依赖引入类型同dependencies
     },
     "dynamicDependencies": {
       // 支持依赖引入类型同 dependencies
     }
   }
   ```
5. devDependencies引入的依赖，不校验循环配置示例：

   如下oh-package.json5配置所示，模块ma通过配置dependencies依赖模块mb，同时模块mb通过配置devDependencies依赖模块ma，进而构造成循环依赖。

   ```json5
   // 模块ma的oh-package.json5
   {
     "name": "ma",
     "version": "1.0.0",
     "description": "Please describe the basic information.",
     "main": "Index.ets",
     "author": "",
     "license": "Apache-2.0",
     "dependencies": {
       "mb": "../mb"
     }
   }

   // 模块mb的oh-package.json5
   {
     "name": "mb",
     "version": "1.0.0",
     "description": "Please describe the basic information.",
     "main": "Index.ets",
     "author": "",
     "license": "Apache-2.0",
     "devDependencies": {
       "ma": "../ma"
     }
   }
   ```

## overrides

ohpm客户端在1.4.0版本开始支持Override机制，可以在项目级别的oh-package.json5（即项目根目录下的oh-package.json5）文件中添加overrides配置，方便将依赖树中的依赖替换为另一个版本。替换的版本可以是一个具体的版本号或模糊版本、本地存在的HAR包或源码目录、[parameterFile](ide-oh-package-json5.md#section122411462820)配置（示例："foo": "@param:dependencies.foo"），也可以使用@module通过模块名指向模块目录（示例："module\_key": "@module:module\_name"）。

例如，想要确保foo始终安装1.0.0版本，可以在**项目级**的oh-package.json5中增加如下配置：

**说明** 

1. overrides必须配置在项目级别的oh-package.json5中，配置在模块级别的oh-package.json5中将不会生效。
2. 从DevEco Studio 6.0.0 Beta1开始支持@module配置方式。
3. @module配置中module\_name必须在project/build-profile.json5文件或者project/.hvigor/dependencyMap/dependencyMap.json5（hvigor生成）文件的modules节点下存在，否则报错处理。
4. @module配置中，module\_key需和"@module:module\_name"指向的模块目录下oh-package.json5文件中配置的name一致，否则报错处理。

```json5
{
  "overrides": {
    "foo": "1.0.0"
  }
}
```

若本地存在foo的源码、HAR包或者@module配置，想确保foo始终使用您本地的版本，可以在**项目级**的oh-package.json5中如下配置：

```json5
{
   "overrides": {
      // 项目存在Foo模块，即build-profile.json5文件或dependencyMap.json5文件中modules节点下存在名称为Foo的模块；该模块Foo的oh-package.json5中name为：foo_test
      // "foo_test": "@module:Foo"
      // 本地存在"foo"的源码目录，如项目根目录下的foo目录
      // "foo": "file:./foo" 
      // 本地存在"foo"的HAR文件，如项目根目录下的libs目录中的foo.har
      "foo": "file:./libs/foo.har"
   }
}
```

## exclusions

ohpm客户端在5.3.0版本开始支持exclusions机制，可以在项目级oh-package.json5（即项目根目录下的oh-package.json5）文件中添加exclusions配置，即可实现移除第三方依赖（远程依赖、本地文件依赖）中的一个或多个子依赖。

### 配置说明

* 配置格式

  ```json5
  // key: value形式配置
  "[@group/]libname[@spec]" : ['exclude_sub_libname']
  ```

  + 配置key部分：[@group/]libname[@spec]，代表需要做子依赖排除的依赖名称及其版本，'[]'代表该内容为可选配置。当依赖没有组织名称时，[@group/]部分可不配置；当不需要精确匹配具体版本号或具体某个本地文件依赖时，[@spec]部分可不配置；spec可以是一个具体的版本号、本地文件路径（支持相对路径和绝对路径，配置为相对路径时指相对于项目根路径）。
  + 配置value部分，['exclude\_sub\_libname']是一个字符串数组，可配置多个，代表需要被排除的子依赖名称列表。

* 配置示例

```json5
{
  "exclusions": {
    "@ohos/lib1@1.0.0": ['@ohos/sub_lib1']      // 排除远程依赖@ohos/lib1的子依赖：@ohos/sub_lib1
    "@ohos/lib2@./lib2.har": ['@ohos/sub_lib2'] // 排除本地文件依赖@ohos/lib2的子依赖：@ohos/sub_lib2
  }
}
```

* 配置约束
  + exclusions必须配置在项目级别的oh-package.json5中，配置在模块级别的oh-package.json5中将不会生效。
  + exclusions配置只能移除远程依赖、本地文件依赖的子依赖，对源码依赖不生效。
  + exclusions只能移除dependencies、dynamicDependencies下配置的依赖。
  + exclusions中配置的key不能和[overrideDependencyMap](ide-oh-package-json5.md#section106151513236)中配置的key一致，否则报配置冲突错误并中断程序。
  + 自动解决依赖版本冲突功能开启（.ohpmrc中resolve\_conflict=true）后，如果exclusions配置中配置项指定了spec，但spec对应的依赖在版本决策中被移除时，exclusions配置将不会生效；建议该场景下不要配置spec部分。

### 示例

下面演示如何移除远程依赖或本地文件依赖的oh-package.json5中dependencies、dynamicDependencies下配置的依赖。示例中以<project>代表项目根路径进行说明。

1、模块级oh-package.json5内容如下，将安装依赖@ohos/lib1、@ohos/lib2。

```json5
{
  "name": "entry",
  "version": "1.0.0",
  "description": "Please describe the basic information.",  
  "dependencies": {
    "@ohos/lib1": "1.0.0" // 远程依赖
    "@ohos/lib2": "file:../lib2.har" // 本地文件依赖
  }
}

// @ohos/lib1的oh-package.json5配置
{
  "name": "@ohos/lib1",
  "version": "1.0.0",
  "description": "Please describe the basic information.",  
  "dependencies": {
    "@ohos/lib1_sub1": "1.0.0" // 子依赖1
    "@ohos/lib1_sub2": "2.0.0" // 子依赖2
  }
}

// @ohos/lib2的oh-package.json5配置
{
  "name": "@ohos/lib2",
  "version": "1.0.0",
  "description": "Please describe the basic information.",  
  "dependencies": {
    "@ohos/lib2_sub1": "1.0.0" // 子依赖1
    "@ohos/lib2_sub2": "2.0.0" // 子依赖2
  }
}
```

2、项目级oh-package.json5内容如下，添加exclusions配置，其中lib2.har放置在项目根目录下。

```json5
{
  "modelVersion": "6.1.1",
  "description": "Please describe the basic information.",
  "exclusions": {
    "@ohos/lib1@1.0.0": ['@ohos/lib1_sub1'],  // 排除远程依赖@ohos/lib1的子依赖：@ohos/lib1_sub1
    "@ohos/lib2@./lib2.har": ['@ohos/lib2_sub2'] // 排除本地文件依赖@ohos/lib2的子依赖：@ohos/lib2_sub2
  }
}
```

3、执行ohpm安装命令。

```json5
ohpm install --all
```

4、ohpm安装完成后，在entry目录下执行：ohpm list -d 10，打印依赖结构如下。

```json5
entry 1.0.0 <project>\entry
├─┬ @ohos/lib1 1.0.0
│ └── @ohos/lib1_sub2 1.0.0 // 安装了子依赖@ohos/lib1_sub2,@ohos/lib1_sub1已被排除
├─┬ @ohos/lib2 <project>\lib2.har
  └── @ohos/lib2_sub1 1.0.0 // 安装了子依赖@ohos/lib2_sub1,@ohos/lib2_sub2已被排除
```

## parameterFile

OHPM新增了参数化配置功能。开发者可在项目根目录配置一个参数化文件（json5格式文件），在该文件中维护模块或依赖版本信息，不同模块将根据该文件中的版本进行配置，满足不同构建场景下，开发者快速切换依赖版本的需要。同时，支持通过命令行指定参数化文件，降低流水线场景下模块和依赖版本的变更难度。

OHPM客户端在1.6.0版本开始支持参数化配置。可以在项目级别的oh-package.json5文件（即项目根目录下的oh-package.json5）中添加parameterFile配置，并同时指定parameterFile文件路径。配置规则如下：

* parameterFile文件路径支持配置相对路径，并以项目根目录为起点，如："parameterFile": "./parameterFile.json5"。
* 配置文件内容采用json5格式，支持多层json对象嵌套；
* 参数化key支持的字符与包名一致，请见[模块级oh-package.json5字段说明](ide-oh-package-json5.md#zh-cn_topic_0000001792256137_oh-packagejson5-字段说明)中name字段要求，大小写敏感；
* 参数化value类型为是"string"或"object"。 value类型为string时，可以是符合[semver规范](https://semver.org/)的版本号，也可以使用本地相对路径（相对于parameterFile文件所在目录）或本地绝对路径。

**说明** 

1. parameterFile字段必须配置在项目级别的oh-package.json5中，否则将不会生效或产生报错提示。
2. parameterFile配置文件位置可以通过命令行选项'-pf <string>' 或 '--parameterFile <string>'指定，但必须先在项目级别oh-package.json5中配置parameterFile字段，否则会报错提示；支持该选项的命令有：install、list、version。
3. parameterFile字段配置后，不允许执行update命令、uninstall命令和指定包名安装（如：'ohpm i <pkg>'）。
4. parameterFile文件路径大小写不敏感，不建议通过大小写来区分不同的配置文件。
5. oh-package.json5中支持参数化的字段有：version、dependencies、devDependencies和dynamicDependencies、overrides，未列举的字段均不支持参数化配置。overrides从DevEco Studio 6.0.0 Beta1开始支持参数化配置。

### 基础配置示例

工程级oh-package.json5示例：

```json5
{
  "modelVersion": "6.1.1",
  "description": "Please describe the project information.",
   ...
  "parameterFile": './parameterFile/parameterFile.json5', // 开启参数化并指定参数化配置文件路径
  "overrides": {
    "libtest1": "@param:dependencies.libtest1", // 所有依赖名称为：libtest1的版本会被替换为：1.0.1
    "libnative": "@param:dependencies.libnative" // 所有依赖名称为：libnative的版本会被替换为：libnative源码依赖路径  
  }
}
```

模块级oh-package.json5示例：

```json5
{
  "name": "parameter-test",
  "version": "@param:version", //使用时必须以 '@param:' 开头
  "description": "test desc.",
  "main": "index.ets",
  "author": "test author",
  "license": "ISC",
  "dependencies": {
    "libtest1": "@param:dependencies.libtest1"
  },
  "devDependencies": {
    "libtest2": "@param:devDependencies.libtest2"
  },
  "dynamicDependencies": {
    "libtest3": "@param:dynamicDependencies.libtest3"
  }
 }
```

parameterFile所指向文件的配置示例：

```json5
{
  "version": "1.0.0",
  "dependencies": {
    "libtest1": "1.0.1",
    "libnative": "../libnative" // 相对于parameterFile配置文件所在目录
  },
  "devDependencies": {
    "libtest2": "*"
  },
  "dynamicDependencies": {
    "libtest3": "latest"
  }
}
```

### 一仓多包示例

一个代码仓有多个har/hsp模块，发包时，一般需要开发者手动修改所有模块的版本号后再打包发布，若模块较多，操作繁琐且效率低下，建议使用参数化配置解决该问题，详细示例如下。

**当所有模块版本不一致**：

如下工程结构所示，所有模块的oh-package.json5中version字段均配置参数化版本（'@param:'开头部分），不同模块的版本均不一致，但都由参数化配置文件'parameter.json'全局统一管理；发包前，只需修改'parameter.json'文件中相关模块的版本，再构建所有模块即可；打包构建时，所有模块的参数化版本均会被替换为'parameter.json'中配置的具体版本（如：@param:har1会被替换为：1.0.0）。

```screen
AppTest
└── har1(模块)
    └── oh-package.json5
        └── "version": "@param:har1"
└── har2(模块)
    └── oh-package.json5
        └── "version": "@param:har2"
... harn(模块)
    └── oh-package.json5
        └── "version": "@param:harn"
└── oh-package.json5 
    └── "parameterFile": "./parameter.json"    
└── parameter.json(参数化配置文件)
    └── "har1": "1.0.0"
    └── "har2": "2.0.0"
    ...
    └── "harn": "n.0.0"
```

**当所有模块版本一致**：

如下工程结构所示，所有模块均使用同一个参数化版本（@param:module\_version），发包前，只需修改'parameter.json'中module\_version的值，再构建所有模块即可；打包构建时，所有模块的参数化版本均会被替换为'parameter.json'中module\_version对应的版本（如：@param:module\_version会被替换为：1.0.0）。

```screen
AppTest
└── har1(模块)
    └── oh-package.json5
        └── "version": "@param:module_version"
└── har2(模块)
    └── oh-package.json5
        └── "version": "@param:module_version"
... harn(模块)
    └── oh-package.json5
        └── "version": "@param:module_version"
└── oh-package.json5 
    └── "parameterFile": "./parameter.json" 
└── parameter.json(参数化配置文件)
    └── "module_version": "1.0.0"
```

## properties

从ohpm 6.1.2.268版本开始，在工程级的oh-package.json5中新增properties参数，该配置参数用于多环境下的依赖管理。

开发者通过parameterFile完成依赖配置后，再在parameterFile字段中使用properties参数，实现工程多环境下的依赖管理。

**参数引用方式**

支持如下三种参数引用方式：

* 使用${key}方式获取参数值。
* 使用json属性访问方式获取参数值。
* 使用字符串拼接的方式获取参数值。

**基础配置示例**

```json5
// 使用${key}方式获取参数值
{
  "modelVersion": "6.1.1",
  "description": "Please describe the project information.",
   ...
  "parameterFile": '${ohpm_environment}', 
  "properties": {
    "ohpm_environment":"./parameterFile/debug.json5",
  }
}

// 使用json属性访问方式获取参数值
{
  "modelVersion": "6.1.1",
  "description": "Please describe the project information.",
   ...
  "parameterFile": '${versions.release}',
  "properties": {
    "ohpm_environment":"./parameterFile/debug.json5",
    "versions": {
      "release": "./parameterFile/release.json5",
    }
  }
}

// 使用字符串拼接的方式获取参数值
{
  "modelVersion": "6.1.1",
  "description": "Please describe the project information.",
   ...
  "parameterFile": './parameterFile/${versions.debug}.json5',
  "properties": {
    "ohpm_environment":"",
    "versions": {
      "debug": "debug-1.0.0",
    }
  }
}
```

## overrideDependencyMap

OHPM客户端在1.7.0版本开始支持使用overrideDependencyMap机制重写源码模块或三方库的依赖关系。开发者可在工程级oh-package.json5文件中新增overrideDependencyMap配置，在该配置对象中通过key-value形式配置依赖关系重写文件；其中，key为依赖标识符，value为依赖关系重写文件路径。在依赖安装时， ohpm会将依赖树中的某个依赖节点的所有直接子依赖替换为对应依赖关系重写文件中配置的依赖项，依赖关系重写文件中支持配置的依赖类型为dependencies、devDependencies、dynamicDependencies，通过使用overrideDependencyMap机制，可以满足开发者在不同场景下，动态变更依赖的需求。

同时，支持在.ohpmrc中使用projectPackageJson配置项来覆盖项目根目录下oh-package.json5中的配置，方便开发者快速切换配置，详情见 [ohpmrc](ide-ohpmrc.md)中projectPackageJson配置。

**配置说明**

* 配置格式

  "[@group/]libname[@version]" : "config\_path"，其中 [@group/]libname[@version] 为依赖标识符key, config\_path为配置文件路径value。

* 配置示例

  ```screen
  {
    "overrideDependencyMap": {
    "@group/libname": "dep-test.json5" 
    }
  }
  ```

* 配置约束
  + overrideDependencyMap必须配置在工程级oh-package.json5中，配置在模块级oh-package.json5中将不会生效。
  + key中@version部分可选，未指定@version时，替换所有名称为@group/libname的依赖的直接子依赖；指定@version时，替换所有名称为@group/libname且版本为version的依赖的直接子依赖，同时，version需符合semver规范，不支持tags标签、范围版本号。
  + value是一个json5文件路径，文件内只支持配置：dependencies、devDependencies、dynamicDependencies。
  + value对应的文件路径只支持绝对路径，配置为相对路径时，需要手动设置.ohpmrc文件中odm\_r2\_project\_root=true, 此时，相对路径会从项目根目录为起点开始解析。

**overrideDependencyMap场景示例**

* 模块entry下oh-package.json5配置了一个远程包依赖libbase，如下所示：

  ```screen
  {
    "name": "entry",
    "version": "1.0.0",
    "main": "Index.ets",
    "license": "Apache-2.0",
    "dependencies": {
      "libbase": "1.0.0"
    }
  }
  ```
* 模块级oh-package.json5文件内容，依赖项libbase中存在一个子依赖lib1，如下所示：

  ```screen
  {
    "name": "libbase",
    "version": "1.0.0",
    "description": "Please describe the basic information.",
    "main": "Index.ets",
    "author": "",
    "license": "Apache-2.0",
    "dependencies": {
      "lib1": "1.0.0" //子依赖
    }
  }
  ```
* 项目根目录oh-package.json5内容，如下所示：

  ```screen
  {
    "name": "overridedependencymaptest",
    "version": "1.0.0",
    "description": "Please describe the basic information.",
    "overrideDependencyMap": {      
      "libbase": "D:\\overrideDependencyMapTest\\dep-debug.json5" //overrideDependencyMap依赖替换配置，可配置多条
    }
  }
  ```
* 配置文件dep-debug.json5中依赖配置如下所示：

  ```screen
  {
    "dependencies": { // 详细依赖配置
      "lib1": "2.0.0",
      "log4js": "2.0.0"
    },
    "devDependencies": {
    },
    "dynamicDependencies": {
    }
  }
  ```
* entry模块下执行：ohpm i, 由于entry下依赖了libbase，而libbase在overrideDependencyMap有配置，此时会使用dep-debug.json5文件内的依赖覆盖libbase的dependencies、devDependencies、dynamicDependencies节点，最终，entry模块会安装libbase、lib1、log4js（无overrideDependencyMap配置覆盖时，只会安装：libbase、lib1）。
* entry list结果如下：

  ```screen
  entry 1.0.0 D:\overrideDependencyMapTest\entry
  └── libbase 1.0.0
      └── lib1 2.0.0
      └── log4js 2.0.0
  ```

## oh-exports

从ohpm 6.1.1.816版本开始，支持通过oh-exports字段控制导出模块中文件，实现包的可见性控制。

* 配置示例

  ```screen
  {
    "oh-exports": [
      'src',
      './src',
      'src/main',
      'src/main/ets/components/MainPage1.ets',
      'src/main/ets/components/MainPage2.ts'
      'src/main/ets/components/MainPage2.js'
    ]
  }
  ```
* 配置约束
  + oh-exports为选填字段，字段值为字符串数组。
  + oh-exports配置的值为目录的相对路径或者特定文件的相对路径，不支持特殊字符和通配符。
  + 支持的命令行：publish、prepublish。

## .ohpmrc中projectPackageJson配置

通过在.ohpmrc文件中配置projectPackageJson，可同时实现对overrides、overrideDependencyMap字段配置的效果，替换项目级oh-package.json5文件中相应的配置，方便开发者在不同使用场景下快速切换使用。配置格式及使用约束如下所示：

* 配置格式

  projectPackageJson:<project\_root>=<config\_path>, 其中 projectPackageJson:<project\_root> 部分视做key, config\_path 部分视做value。配置key指定项目根目录路径（绝对路径），配置value指定json5格式配置文件路径用以覆盖项目级oh-package.json5中的配置。
* 配置示例

  projectPackageJson:D:\test\TestProject=projectPackageJson.json5
* 配置约束
  + key必须以 'projectPackageJson:' 开头；project\_root表示项目根路径。
  + value对应json5文件内只支持配置：overrides、overrideDependencyMap，不支持 parameterFile（编辑器和编译器无法识别）。
  + 对同一个project\_root，如存在多条projectPackageJson配置路径，仅最后一条会生效。
  + value对应的文件路径支持绝对路径和相对路径，配置为相对路径时，从项目根目录为起点开始解析。

**示例**

下面演示在.ohpmrc中配置同一工程的不同环境下的projectPackageJson配置，当配置生效时，会直接覆盖项目级oh-package.json5中对应配置。

* 在项目级或用户级.ohpmrc中增加2条配置，分别对应开发、Release环境，如下所示：

  ```screen
  registry=http://localhost:8088/repos/ohpm
  log_level=debug
  strict_ssl=false
  projectPackageJson:D:\overrideDependencyMapTest=oh-pkg-debug.json5 //debug环境配置
  projectPackageJson:D:\overrideDependencyMapTest=oh-pkg-release.json5 //release环境配置，.ohpmrc中存在同一工程的多条配置时默认按配置先后顺序取最后一条，即当前配置生效
  ```

* 文件oh-pkg-release.json5配置，新增了一条依赖libbase的配置，如下所示：

  ```screen
  {
    "overrideDependencyMap": {
      "libbase": "D:\\overrideDependencyMapTest\\dep-release.json5"
    }
  }
  ```
* Release环境下libbase的依赖替换文件dep-release.json5中依赖配置如下所示：

  ```screen
  {
    "dependencies": {
      "lib1": "1.0.0",
      "lib2": "2.0.0",
      "lib3": "3.0.0"
    }
  }
  ```
* 基于 [overrideDependencyMap场景示例](ide-oh-package-json5.md#section106151513236) 工程，在entry模块下执行：ohpm i，此时，在ohpm运行时中会将项目级oh-package.json5中的配置会变更为：

  ```screen
  {
    "name": "overridedependencymaptest",
    "version": "1.0.0",
    "description": "Please describe the basic information.",
    "overrideDependencyMap": {
      "libbase": "D:\\overrideDependencyMapTest\\dep-release.json5"
    }
  }
  ```

* 最终安装结果如下：

  ```screen
  entry 1.0.0 D:\overrideDependencyMapTest\entry
  └── libbase 1.0.0
      └── lib1 1.0.0
      └── lib2 2.0.0
      └── lib3 3.0.0
  ```

## oh-package-lock.json5

oh-package-lock.json5用于锁定所有依赖的版本，以及缓存依赖的元数据信息。不建议开发者手动修改该文件的内容，也不建议开发者使用其他分析工具直接读取该文件的内容。

建议将oh-package-lock.json5文件提交到代码仓库中进行版本管理。优点如下：

* 确保构建可复现： oh-package-lock.json5文件记录了三方包安装时确切的依赖树，其中包括每个依赖的版本、子依赖及其版本等详细信息。将该文件提交到代码仓库，能够确保团队成员、持续集成（CI）服务器或其他任何克隆该项目的用户，在执行ohpm install时可以获得完全一致的依赖版本，从而保证项目的可复现构建。
* 提高安装速度： ohpm在安装依赖时，会优先使用oh-package-lock.json5锁定的版本信息，避免重新解析依赖版本，有效地加快安装过程。
* 安全性： 通过锁定依赖版本，oh-package-lock.json5可以帮助防止因上游依赖更新引入的安全漏洞。当发现依赖存在安全问题时，可以针对性地更新特定依赖版本，并将更新后的oh-package-lock.json5提交到仓库，确保所有使用者都获取到修复后的版本。
* 便于协同工作： 当团队成员在项目中添加、更新或删除依赖时，他们应运行ohpm update以更新oh-package-lock.json5。提交这些变更到仓库，可以让其他成员了解到依赖的变化，并在拉取最新代码后自动获取正确的依赖版本。
