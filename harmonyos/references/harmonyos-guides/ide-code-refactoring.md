---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-refactoring
title: 代码重构
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码重构
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:27+08:00
doc_updated_at: 2026-03-24
content_hash: sha256:a37409ad86e5b523393af0933812a41e6a1123ab326770df6478312c5f94738b
---

## ArkTS/TS代码重构

### Refactor-Extract代码提取

在编辑器中支持将函数内、类方法内等区域代码块或表达式，提取为新方法/函数（Method）、常量（Constant）、接口（Interface）、变量（Variable）或类型别名（Type Alias）。准确便捷的将所选区域代码从当前作用域内进行提取，提升编码效率。选中所需要提取的代码块，右键单击**Refactor**，选择需要提取的类型。

说明

Refactor-Extract代码提取为类型别名（Type Alias）能力仅TS语言支持。

方法/函数（Method）支持选中代码块或完整语句进行提取：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/rmNJW-5xS1CKRRhn_pphbg/zh-cn_image_0000002530913856.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054626Z&HW-CC-Expire=86400&HW-CC-Sign=FF04E042F5A54A461E6B9726BED7135A8D15EC83142D46BD8FB6B9FFA971BA6E "点击放大")

在ArkTS语言中，支持将组件调用代码块提取为@Builder装饰器装饰的方法，组件属性调用表达式可提取为@Styles或@Extend装饰器装饰的方法。

**使用方式**：选中需要提取的组件或属性，右键单击**Refactor**，选择**Extract Method...**，组件私有属性可提取为@Extend装饰的方法，通用属性可提取为@Styles或@Extend装饰的方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/QqCGSbI7Tju-oO2Ga6cF0A/zh-cn_image_0000002561753799.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054626Z&HW-CC-Expire=86400&HW-CC-Sign=9D64BEFC0334607427F9EA60B484411F02D6649DB2D78E9336FBFCEC45A62C05 "点击放大")

常量（Constant）支持选中单行表达式进行提取：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/uUEV9xMRQ3ufHUdp9RjaoQ/zh-cn_image_0000002561753803.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054626Z&HW-CC-Expire=86400&HW-CC-Sign=12612FC9C803B9B37FDBEC473AFAD298B181D9BE6D7C8F241B4565A5242FDB90 "点击放大")

接口（Interface）支持选中对象自变量进行提取：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/g9tGIt68TjWlrCwv_0DWhg/zh-cn_image_0000002561833779.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054626Z&HW-CC-Expire=86400&HW-CC-Sign=71DC0C6450D1CB59D0266DB2EB33430EB024ABC2DBE6730CD70E417DF9A560D1 "点击放大")

支持选中表达式提取为变量（Variable）：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/-gUrKpFUSLaCDv6B1qtKgg/zh-cn_image_0000002561833783.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054626Z&HW-CC-Expire=86400&HW-CC-Sign=F7D2C606438115E23A28596517BC9A10EF5EB4C8F75CE3970951A942FC83492E "点击放大")

### Refactor-Convert代码转换

编辑器内提供Convert重构能力，支持Convert between named imports and namespace imports等高频转换操作，辅助开发者高效重构代码，提升代码质量。

**表1** Refactor-Convert功能支持清单

| 功能 | 说明 | 使用方法 | 支持转换的源码类型 |
| --- | --- | --- | --- |
| Convert to class | 将JS源码中的function转换为符合ES6标准的类 | 点击或选中function名，右键单击**Refactor** > **Convert**，或使用快捷键**Ctrl+Alt+Shift+R**（macOS为**Option+Shift+Command+R**），在弹窗中选择转换的方式。  说明  若当前工程中已引用该方法，执行Convert to class后，在Find Usages中可查看引用的具体位置，点击**Do Refactor**可忽略冲突并执行转换；也可以逐条修改引用位置的代码后，重新执行上述操作。 | JS |
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/F1NzrxFtQSaMbBMyRvo9eA/zh-cn_image_0000002530753866.png?HW-CC-KV=V1&HW-CC-Date=20260429T054626Z&HW-CC-Expire=86400&HW-CC-Sign=A14929E6FE9DF58D046B02D5F4FDDFCB5ABB4D705252FC56320C7C13E5D02EDC)

代码编辑支持筛选并过滤不需要rename的引用位置。在**Rename...**弹窗中点击**Preview**，在弹出预览窗口中，用户选中无需Rename的选项，单击右键菜单**Exclude****/Remove**进行过滤/删除，完成筛选后点击左下角**Do Refactor**，重新执行Rename操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/ta_LoJpURlS1K3O4W8Hl4A/zh-cn_image_0000002561833769.png?HW-CC-KV=V1&HW-CC-Date=20260429T054626Z&HW-CC-Expire=86400&HW-CC-Sign=C7567132E24D129FE1A7570B15DAA069FAF0E6883934EEFC02F40DD83626C00F)

说明

若ArkTS文件中存在C++接口调用，使用Rename进行重命名时，C++文件中涉及的函数名也会被重命名。

### Move File

在文件中单击右键，选择**Refactor > Move File...**，在弹窗中输入或点击**...**选择指定的目录，点击**Refactor**，可将当前文件移动至该目录下。勾选**Search for references**，可查找并更新工程中对该文件的引用；勾选**Open in editor**，可在编辑器中查看移动的文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/gkyybzZwQ4-Nai1656JPsA/zh-cn_image_0000002530913852.png?HW-CC-KV=V1&HW-CC-Date=20260429T054626Z&HW-CC-Expire=86400&HW-CC-Sign=9809F4C066162688A756A2C7EA263F05A3B7B96CE56176D5493F3E0510EAAD76)

### Safe Delete

编辑器支持Safe Delete功能，帮助您安全地删除代码中的标识符对象（变量、函数或类等）或删除指定文件。在删除前，编辑器将先在代码中搜索对该对象的引用，如果存在引用，编辑器将提示您进行必要的检查和调整。

**使用方式**：在编辑器内选中需要删除的标识符对象或在工程目录选择待删除的文件，右键单击**Refactor**，选择**Safe Delete**，单击**OK**将自动检查当前对象在代码中被引用的情况，点击**View Usages**可查看具体使用的代码内容，点击**Delete Anyway**将直接删除该对象的定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/Z9WW00frRUOJhGtQtTU4vw/zh-cn_image_0000002530753852.png?HW-CC-KV=V1&HW-CC-Date=20260429T054626Z&HW-CC-Expire=86400&HW-CC-Sign=A863BB5AFAA9DC08FA12FDCD146FF89DD01B0FDD496FB94F51B0721D0493380B)

## C++代码重构

编辑器提供C++代码重构能力，当前支持展开宏、交换if分支、移动函数体到声明处等使用场景下的重构能力，提升开发效率。

### 展开宏

支持在当前宏引用处展开宏。将光标移动至需要展开的宏，右键单击**Refactor**，选择**Inline**，展开此处引用的宏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/KVmVreQXRqS1YpkI5BLUzA/zh-cn_image_0000002561833773.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054626Z&HW-CC-Expire=86400&HW-CC-Sign=65F2D180CBF9A411CA4B7A4B488058ECE3828BDC56B8C2852F83CBAECFFA30FC)

### 交换if分支

编辑器支持在选中if-else完整代码块的情况下，实现对if-else代码块的位置交换，并对条件取反。

**使用约束**

* 需要重构的代码块必须为完整的if-else代码结构，{}不能省略；
* if-else中的statement包含嵌套if-else语句时，只反转最外层的if-else语句。对于if() -else if()-else() 结构，仅支持对最后一层if-else结构进行交换；
* 不支持赋值语句的判断条件取反。

**使用方式**

编辑器内选择需要转换的代码区域，右键单击**Refactor**，选择**Swap If Branches**，对原有if条件取反，并交换if-else原代码块顺序。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/lAeSFx30TgW72B5epC-bmA/zh-cn_image_0000002530753862.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054626Z&HW-CC-Expire=86400&HW-CC-Sign=A6FF53C8EF384C96E0D1EF8A3164925A7CB910D96825A1D166B4500450444557 "点击放大")

### 移动函数体到声明处

编辑器支持将函数体从源文件移动到头文件中，提高代码可读性。编辑器内选中函数名，右键单击**Refactor**，选择**Move to Declaration**，源文件中的函数实现将移动至头文件中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/1Pq2TF-CSHuEpCComCmRbQ/zh-cn_image_0000002561753807.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054626Z&HW-CC-Expire=86400&HW-CC-Sign=D5576BE3F2A9DDE1A3E0BD7FECB027DA6547182096F8051B98A73F1C0CFBCF01)

### 移动函数体到实现处

在编辑器内将光标放在或选中函数名，右键单击**Refactor**，选择**Move to Implementation**，选择移动到的文件，将函数定义移动到该文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/AekFM7DUQA6jMms7soXYoQ/zh-cn_image_0000002561833787.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054626Z&HW-CC-Expire=86400&HW-CC-Sign=FC0C37D213CE2D969290CA9937CBB3E0868A02FADF06CCED5ACDE7ABD9F23EB2)

### 将语句转为原始字符串

编辑器提供重构能力，支持将带有 \n, \t, \", \\, \'五类转义字符的字符串转换为原始字符串。当前仅支持标准字符串，不支持 u8""等其他字符串。

在编辑器内选择字符串代码区域，右键单击**Refactor**，选择**Convert To Raw String**，将语句转换为原始字符串。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/e57bJLOFSQmqgBzo7Tanew/zh-cn_image_0000002530913864.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054626Z&HW-CC-Expire=86400&HW-CC-Sign=0BADE52D143C8B858943C216DF74054F11D63164911A0744762C8B35BD9BA19E "点击放大")

### 定义构造函数

编辑器提供重构能力，支持为类的成员变量生成默认的构造函数。

**规格限制**

1. 不支持未初始化成员变量的类
2. 不支持在（class标识符，类名，大括号）以外的位置触发
3. 不支持类已存在有入参的构造函数

**使用方法：**在类的定义的类名处，右键单击**Generate****...**，选择**Constructor**，在弹框中点击**Define**，为成员变量定义一个构造函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/19Z4N2nLQqmhiQ-B8M62-Q/zh-cn_image_0000002561753793.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054626Z&HW-CC-Expire=86400&HW-CC-Sign=7EA3396F119E86EDCD25A50F246E7C81540309ADC1FE5CF5D224909832A78997)

### 提取表达式到变量

在编辑器内，选中需要提取的表达式范围，右键单击**Refactor**，选择**Extract Variable**，支持提取表达式到变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/LK6rEhTST3qmiXLMMY9mig/zh-cn_image_0000002530913846.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054626Z&HW-CC-Expire=86400&HW-CC-Sign=1FAFAECBC0CC3AD831E90EBB338A3E666FB5F25405C255DA59C3208438BB770C "点击放大")

### 移除namespace

光标停留在需要移除的namespace处，右键单击**Refactor**，选择**Remove Using Namespace**进行移除，可以避免命名冲突，提高代码可读性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/7Zcbxt-ISa24mnGskgfFMQ/zh-cn_image_0000002561753789.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054626Z&HW-CC-Expire=86400&HW-CC-Sign=91587B2E8FC342D0F52D6F51F7187E526F6558383D43C4B0699C84A981B915D4)

### 添加using声明

编辑器内，光标停留在需要添加using声明处，右键单击**Refactor**，选择**Add Using**完成使用using定义类型别名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/dDLSRji0QmesEUXm8-VNrQ/zh-cn_image_0000002530753858.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054626Z&HW-CC-Expire=86400&HW-CC-Sign=096AAEE4410939DE4F1DCD7D28B870097F6DB480FEB68F367B3EC9FEB0621AFB)

### auto自动展开

在auto关键字处右键单击**Refactor**，选择**Expand Auto Type**，可以使用推断类型替换auto类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/CSji4xnETGyNJkbj55ve_Q/zh-cn_image_0000002530753870.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054626Z&HW-CC-Expire=86400&HW-CC-Sign=0AF66B679340B60C72B9E29CBFB24D3751B5EDCBA6DA4F50339384A6E56975CE)

### 声明隐式成员

编辑器支持在类中声明隐式复制/移动成员。光标停留在需要生成的类处，右键单击**Generate**..., 选择**Copy/Move Members**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/1TZHETgTQZ24LWEmcPqEzg/zh-cn_image_0000002530913860.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054626Z&HW-CC-Expire=86400&HW-CC-Sign=29A7CF287B913A41D7D2FE314EBA20BD8D2970DCC88FDA3D3F31307E9F161F1B)
