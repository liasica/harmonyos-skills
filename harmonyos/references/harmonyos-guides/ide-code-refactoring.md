---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-refactoring
title: 代码重构
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码重构
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:37+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:fadd819f0bc0d283b0ee97cbabbe249221f9dc5b75bd9be9b654fc4b3973ac08
---

## ArkTS/TS代码重构

### Refactor-Extract代码提取

在编辑器中支持将函数内、类方法内等区域代码块或表达式，提取为新方法/函数（Method）、常量（Constant）、接口（Interface）、变量（Variable）或类型别名（Type Alias）。准确便捷的将所选区域代码从当前作用域内进行提取，提升编码效率。选中所需要提取的代码块，右键单击**Refactor**，选择需要提取的类型。

**说明** 

Refactor-Extract代码提取为类型别名（Type Alias）能力仅TS语言支持。

方法/函数（Method）支持选中代码块或完整语句进行提取：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/UmBUWyupTVGVFc-40GSYOQ/zh-cn_image_0000002808887091.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A5D4C658A4180ADF367B38496260B35D5A068ADDA2293C9D15433E94D9C47DD "点击放大")

在ArkTS语言中，支持将组件调用代码块提取为@Builder装饰器装饰的方法，组件属性调用表达式可提取为@Styles或@Extend装饰器装饰的方法。

**使用方式**：选中需要提取的组件或属性，右键单击**Refactor**，选择**Extract Method...**，组件私有属性可提取为@Extend装饰的方法，通用属性可提取为@Styles或@Extend装饰的方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/y7r5YOJ4TjaJbsNaVuEmYA/zh-cn_image_0000002808887087.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=42F515B74297F72ECFDECCB4A2E0222500409BD1DDA0375E5D3D44173A0AE3F7 "点击放大")

常量（Constant）支持选中单行表达式进行提取：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/8rd_x2fFTLWf6abf3jbL1Q/zh-cn_image_0000002808767011.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=D32B3579CEBC549A2D1CE0B4C9FB75EDD78CA3BC2D5E708BDB74807BAF24503E "点击放大")

接口（Interface）支持选中对象自变量进行提取：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/zTG_YydjS5OjBCS-i9_6Ew/zh-cn_image_0000002779407450.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=C82A16C1861B1AC7779DFF47AC86F283948062FC0B83378BE9E537F270104353 "点击放大")

支持选中表达式提取为变量（Variable）：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/RXKzHHTSRQuIDAfI9drGYw/zh-cn_image_0000002779407458.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=CFFC9BF354543DC04DE00C5C7353169743219D21F86B3F599CBBA4452EC6052A "点击放大")

### Refactor-Convert代码转换

编辑器内提供Convert重构能力，支持Convert between named imports and namespace imports等高频转换操作，辅助开发者高效重构代码，提升代码质量。

**表1** Refactor-Convert功能支持清单

| 功能 | 说明 | 使用方法 | 支持转换的源码类型 |
| --- | --- | --- | --- |
| Convert to class | 将JS源码中的function转换为符合ES6标准的类 | 点击或选中function名，右键单击**Refactor** > **Convert**，或使用快捷键**Ctrl+Alt+Shift+R**（macOS为**Option+Shift+Command+R**），在弹窗中选择转换的方式。  说明：  若当前工程中已引用该方法，执行Convert to class后，在Find Usages中可查看引用的具体位置，点击**Do Refactor**可忽略冲突并执行转换；也可以逐条修改引用位置的代码后，重新执行上述操作。 | JS |
| Convert to anonymous function | 将箭头函数转换为匿名函数 | 选中箭头函数赋值变量，右键单击**Refactor** > **Convert**，或使用快捷键**Ctrl+Alt+Shift+R**（macOS为**Option+Shift+Command+R**），在弹窗中选择转换的方式。 | JS/TS |
| Convert to named function | 将箭头函数转换为普通函数 | 选中箭头函数赋值变量，右键单击**Refactor** > **Convert**，或使用快捷键**Ctrl+Alt+Shift+R**（macOS为**Option+Shift+Command+R**），在弹窗中选择转换的方式。 | JS/TS/ArkTS |
| Convert to arrow function | 将匿名函数转换为箭头函数 | 选中匿名函数赋值变量，右键单击**Refactor** > **Convert**，或使用快捷键**Ctrl+Alt+Shift+R**（macOS为**Option+Shift+Command+R**），在弹窗中选择转换的方式。 | JS/TS/ArkTS |
| Convert default export to named export | 支持named export和default export相互转换 | 完整选中export default语句，右键单击**Refactor** > **Convert**，或使用快捷键**Ctrl+Alt+Shift+R**（macOS为**Option+Shift+Command+R**），在弹窗中选择转换的方式。 | JS/TS/ArkTS |
| Convert named export to default export | 完整选中export语句，右键单击**Refactor** > **Convert**，或使用快捷键**Ctrl+Alt+Shift+R**（macOS为**Option+Shift+Command+R**），在弹窗中选择转换的方式。 |
| Convert named imports to namespace import | 支持在命名import和命名空间import形态间转换 | 完整选中import语句，右键单击**Refactor** > **Convert**，或使用快捷键**Ctrl+Alt+Shift+R**（macOS为**Option+Shift+Command+R**），在弹窗中选择转换的方式。 | JS/TS/ArkTS |
| Convert namespace import to named imports | 完整选中命名空间import语句，右键单击**Refactor** > **Convert**，或使用快捷键**Ctrl+Alt+Shift+R**（macOS为**Option+Shift+Command+R**），在弹窗中选择转换的方式。 |
| Convert to template string | 将字符串转换为模板字面量 | 选中字符串或完整表达式，右键单击**Refactor** > **Convert**，或使用快捷键**Ctrl+Alt+Shift+R**（macOS为**Option+Shift+Command+R**），在弹窗中选择转换的方式。 | JS/TS/ArkTS |
| Convert to optional chain expression | 将判空逻辑转换为可选链式调用 | 选中连续判空表达式，右键单击**Refactor** > **Convert**，或使用快捷键**Ctrl+Alt+Shift+R**（macOS为**Option+Shift+Command+R**），在弹窗中选择转换的方式。 | JS/TS/ArkTS |

### Refactor-Rename代码重命名

代码编辑支持Rename功能，可以快速更改变量、方法、对象属性等相关标识符及文件、模块的名称，并同步到整个工程中对其进行引用的位置。

**使用方式**：选中需要重新命名的标识符（变量、类、接口、自定义组件等），右键单击**Refactor**，选择**Rename...**（或使用**快捷键Shift+F6**），在弹框中输入新的标识符名称，并在**Scope**中选择替换的范围，点击**Refactor**完成重新命名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/Dcx1lSnNTLGXX_Y9oangvw/zh-cn_image_0000002808887093.png?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=DCEF8EA25BCB83A6DF658FA809EF65BB87D51E0D1EDB7D18D09D23E3917BA0A5)

代码编辑支持筛选并过滤不需要rename的引用位置。在**Rename...**弹窗中点击**Preview**，在弹出预览窗口中，用户选中无需Rename的选项，单击右键菜单**Exclude****/Remove**进行过滤/删除，完成筛选后点击左下角**Refactor**，重新执行Rename操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/NtNuPmZyTHeQ9Lyqbjr7MQ/zh-cn_image_0000002808887083.png?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A50F4FE97A44D15C69B025247CB99A89D9678889BDCB58D415FC4A3597F732E)

**说明** 

若ArkTS文件中存在C++接口调用，使用Rename进行重命名时，C++文件中涉及的函数名也会被重命名。

### Move File

在文件中单击右键，选择**Refactor > Move File...**，在弹窗中输入或点击**...**选择指定的目录，点击**Refactor**，可将当前文件移动至该目录下。勾选**Search for references**，可查找并更新工程中对该文件的引用；勾选**Open in editor**，可在编辑器中查看移动的文件。

从26.0.0版本开始，针对跨模块移动文件场景优化了移动符号的导入方式，移入、移出模块时Index.ets会适配改动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/wCnr31_aT9W-3bBhHVSG8A/zh-cn_image_0000002779567424.png?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=16F235FBD99FFC3623BC34164B14DAF2012B30C3BF54880EF17B40366EBD3CF8)

### Safe Delete

编辑器支持Safe Delete功能，帮助您安全地删除代码中的标识符对象（变量、函数或类等）或删除指定文件。在删除前，编辑器将先在代码中搜索对该对象的引用，如果存在引用，编辑器将提示您进行必要的检查和调整。

**使用方式**：在编辑器内选中需要删除的标识符对象或在工程目录选择待删除的文件，右键单击**Refactor**，选择**Safe Delete**，单击**OK**将自动检查当前对象在代码中被引用的情况，点击**Open in Find Window**可查看具体使用的代码内容，点击**Refactor** **Anyway**将直接删除该对象的定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/lr_Rbf6cRq-Eca-FTuQXeQ/zh-cn_image_0000002808887079.png?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=44328414D3962763E34763D9D17485E491B81EDA8A829A6E0BE4382E5C5D7E77)

## C++代码重构

编辑器提供C++代码重构能力，当前支持展开宏、交换if分支、移动函数体到声明处等使用场景下的重构能力，提升开发效率。

### 展开宏

支持在当前宏引用处展开宏。将光标移动至需要展开的宏，右键单击**Refactor**，选择**Inline**，展开此处引用的宏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/DbAS4t7IRLShA7N7PST-DA/zh-cn_image_0000002779567420.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=BC3F04E761A34A984014B1887E5DC77F787A222FFE088D77B8837672FE4563B1)

### 交换if分支

编辑器支持在选中if-else完整代码块的情况下，实现对if-else代码块的位置交换，并对条件取反。

**使用约束**

* 需要重构的代码块必须为完整的if-else代码结构，{}不能省略；
* if-else中的statement包含嵌套if-else语句时，只反转最外层的if-else语句。对于if() -else if()-else() 结构，仅支持对最后一层if-else结构进行交换；
* 不支持赋值语句的判断条件取反。

**使用方式**

编辑器内选择需要转换的代码区域，右键单击**Refactor**，选择**Swap If Branches**，对原有if条件取反，并交换if-else原代码块顺序。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/ylF60aeMSTyk5di3OqGCVQ/zh-cn_image_0000002808767009.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=379B293DE7D47B4A78E898FC9D4145A322D66BFBA489917A65798CB01BD547F6 "点击放大")

### 移动函数体到声明处

编辑器支持将函数体从源文件移动到头文件中，提高代码可读性。编辑器内选中函数名，右键单击**Refactor**，选择**Move to Declaration**，源文件中的函数实现将移动至头文件中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/uVzCQQ3cTZWBQ2fyuRcXtg/zh-cn_image_0000002779407456.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D917ADFD43DC327BD3E26947C190475832516DC497C7113B346898EAC157759)

### 移动函数体到实现处

在编辑器内将光标放在或选中函数名，右键单击**Refactor**，选择**Move to Implementation**，选择移动到的文件，将函数定义移动到该文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/4TNLQCItSI-PnGVFx7AXLA/zh-cn_image_0000002779567434.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=11AFD57416538269F4A2FE13AA26E221CE2CA96B9A37F82F01BD6ECB96F78BEC)

### 将语句转为原始字符串

编辑器提供重构能力，支持将带有 \n, \t, \", \\, \'五类转义字符的字符串转换为原始字符串。当前仅支持标准字符串，不支持 u8""等其他字符串。

在编辑器内选择字符串代码区域，右键单击**Refactor**，选择**Convert To Raw String**，将语句转换为原始字符串。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/S-CUoHswRKKrXj3aJWxT4w/zh-cn_image_0000002779567438.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0912FEE949B940EBD070A897691E907FF81F0549C1EFE936B94C55C1917590A "点击放大")

### 定义构造函数

编辑器提供重构能力，支持为类的成员变量生成默认的构造函数。

**规格限制**

1. 不支持未初始化成员变量的类
2. 不支持在（class标识符，类名，大括号）以外的位置触发
3. 不支持类已存在有入参的构造函数

**使用方法：**在类的定义的类名处，右键单击**Generate****...**，选择**Constructor**，在弹框中点击**Define**，为成员变量定义一个构造函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/7AMP71lTQuGCiTCRNABeXg/zh-cn_image_0000002779407442.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=E4EA30CFEEABA14D9918EB72C0559514E62D0F1CF99839178EF82F8A30AEC80E)

### 提取表达式到变量

在编辑器内，选中需要提取的表达式范围，右键单击**Refactor**，选择**Extract Variable**，支持提取表达式到变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/1hckFKTgQj2RPLAs6QLM9Q/zh-cn_image_0000002779567418.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=740991EA0B7E93B4214BCB708AF2D61ADDA7ADC84DF2163E517828EC184D2753 "点击放大")

### 移除namespace

光标停留在需要移除的namespace处，右键单击**Refactor**，选择**Remove Using Namespace**进行移除，可以避免命名冲突，提高代码可读性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/FDYQ6L3gR_um5CWVcZEdDw/zh-cn_image_0000002779407440.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=744A4C0F0F79DE3C57D614B941DE84F97B1BB2427DE8C90BCBF1B83FC07551EB)

### 添加using声明

编辑器内，光标停留在需要添加using声明处，右键单击**Refactor**，选择**Add Using**完成使用using定义类型别名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/kzy78-ZEQo2_A9HKh11xig/zh-cn_image_0000002808767003.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=3105FFCC803DBADEEC239FCC046E4ADCDD60CFF68496EF44DEA032345D9FEC2A)

### auto自动展开

在auto关键字处右键单击**Refactor**，选择**Expand Auto Type**，可以使用推断类型替换auto类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/ypPaQVJFQB6VVJFdxy4DuQ/zh-cn_image_0000002808767017.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A7FCE1BE118CEBC2A89C5DD4D6C92EAD1D180EB472EA749983C91A667F8D1AD)

### 声明隐式成员

编辑器支持在类中声明隐式复制/移动成员。光标停留在需要生成的类处，右键单击**Generate**..., 选择**Copy/Move Members**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/p4Y8Ach9SIa-DFOFtjp-Hw/zh-cn_image_0000002808767013.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023436Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B68BA3CA8CBF7F5683E9A510FC4FCA5E0F78F58D8D840934B51FACAD51E36A0)
